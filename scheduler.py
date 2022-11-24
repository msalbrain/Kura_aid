# from fastapi import BackgroundTasks
import json
import time

from sms import SMS

s = SMS()


is_scheduler = False

onetime_schedule = {
    "phone": {
        "time": None,
        "phone": None,
        "msg": "",
        "sent_time": int
    }
}

repeat_schedule = {
    "phone": {
        "time": None,
        "phone": None,
        "msg": "",
    }
}


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
            pre_time = int(time.time())
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
            pre_time = int(time.time())
            if not sch.get(None, None):
                break
            elif not sch.get("msg"):
                continue
            elif 60 > int(sch.get("time")) - pre_time > 0:
                s.send(sch.get("msg"), sch.get("phone"))
                sch.update({"msg": None})
                write_to_file(sch, "repeat.json")

        time.sleep(60)
