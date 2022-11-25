# from fastapi import BackgroundTasks
import json
import time

import datetime

from sms import SMS

s = SMS()

is_scheduler = False

onetime_schedule = {
    "phone": {
        "time": None,
        "phone": None,
        "msg": "",
    }
}

repeat_schedule = {
    "phone": {
        "time": None,
        "phone": None,
        "msg": "",
    }
}


def make_time():
    d = datetime.datetime.utcnow()
    return int(time.mktime(d.timetuple()))


def set_time_in_file(user_time, filename, phone):
    split_time = str(user_time).split(" ")
    if len(split_time) < 2 or len(split_time) > 2:
        return "END time supplied with incorrect format"
    elif not split_time[0].isdigit() and not split_time[0].isdigit():
        return "END time supplied with incorrect format"
    else:
        c_d = datetime.datetime.utcnow()
        c_datetime = datetime.date(c_d.year, c_d.month, c_d.day)

        h_s = int(split_time[0]) * 3600
        m_s = int(split_time[1]) * 60

        c_datetime_unix = int(time.mktime(c_datetime.timetuple()))
        c_datetime_unix += h_s + m_s

        if c_datetime_unix < make_time():
            c_datetime_unix += 86400

        p = read_from_file(filename)
        p = p.get(phone, {"phone": phone, "time": c_datetime_unix, "msg": ""})
        p.update({"time": c_datetime_unix})
        update_file(p, "onetime.json", uptype="update")

        res = f"END your reminder has been set for {user_time}"
        return res


def write_to_file(data: dict, filename: str):
    json_object = json.dumps(data, indent=4)

    # Writing to sample.json
    with open(filename, "w") as outfile:
        outfile.write(json_object)


def read_from_file(filename) -> dict:
    with open(filename, 'r') as openfile:
        # Reading from json file
        json_object = json.load(openfile)

        return json_object


def update_file(data: dict, filename: str, uptype: str):
    if uptype == "pop":
        p = read_from_file(filename)
        p[data.get("phone")] = {}
        write_to_file(p, filename)
    elif uptype == "add":
        p = read_from_file(filename)
        p[data.get("phone")] = data
        write_to_file(p, filename)
    elif uptype == "update":
        p = read_from_file(filename)
        p[data.get("phone")] = data
        write_to_file(p, filename)


def repeat_schedule_func():
    while True:
        r = read_from_file("repeat.json")
        for i in r:
            sch: dict = r[i]
            pre_time = int(make_time())
            if not sch.get(None, None):
                break
            elif not sch.get("msg"):
                continue
            elif 60 > int(sch.get("time")) - pre_time > 0:
                s.send(sch.get("msg"), sch.get("phone"))
                sch.update({"time": (sch.get("time") + 86400)})
                write_to_file(sch, "repeat.json")

        time.sleep(60)


def onetime_schedule_func():
    while True:
        r = read_from_file("onetime.json")
        for i in r:
            sch: dict = r[i]
            print(sch, make_time())
            pre_time = int(make_time())
            if sch.get(None):
                print("this is onetime under none none")
                break
            elif not sch.get("msg"):
                print(f"this is onetime under msg == '{str(sch)}'")

            elif 60 > int(sch.get("time")) - pre_time > 0:
                print(f"this is onetime under msg == {str(sch)}")
                s.send(sch.get("msg"), sch.get("phone"))
                sch.update({"msg": None})
                write_to_file(sch, "repeat.json")

        time.sleep(60)
