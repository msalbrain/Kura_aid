from fastapi import FastAPI, Request, responses
import time

app = FastAPI()





fake_db = {
    "09032097223":
        {
            "location": "Ikpoba Okha, Edo Satte",
            "name": "",
            "phone": "902346829",
            "joined": 897643289,
            "history": [
                {
                    "date": 6781982376,
                    "complain": "",
                }
            ]
        },
}
locationDictionary = {
    "state": {
        "LGA": "Lat Log"
    }
}


def location(LGA, State):
    locationDictionary.get("state")


def unregisteredUser(text, phone):
    user = fake_db.get(phone)
    user.update({"name": text})

    fake_db.update({str(phone): user})

    response = "CON Welcome to Kura where yo have access to quality health services\n"
    response += "1. Specialist \n"
    response += "2. Reminder \n"
    response += "3. Pharmacy \n"
    response += "4. Hospital \n"
    response += "5. Caretaker\n"

    return response
    # return "State Your Name"


@app.get("/test")
def check():
    return ('jj')


@app.post("/app", response_class=responses.PlainTextResponse)
async def index(request: Request):
    form = await request.form()
    session_id = form["sessionId"]
    serviceCode = form["serviceCode"]
    phone_number = form["phoneNumber"]
    text = form["text"]
    response = ""
    user = fake_db.get(phone_number)
    if user:
        if user["name"] == "":
            return unregisteredUser(text, phone_number)
        # elif user["location"] == "":
        #     return unregisteredlocation(text, phone_number)
        else:

            s = text
            s_list = s.split("*")
            # e.g s_list = ['salman', '1']

            j = 0
            real_string = ""
            for i in s_list:
                if i.isdigit():
                    for k in s_list[j:]:
                        real_string += k + "*"

                    # real_string = "".join(s_list[j:])
                    # print(real_string)
                    break
                j += 1
            text = real_string[:-1]

            # return f"END the text is {text}"

            if text == "":
                response = "CON Welcome to Kura where yo have access to quality health services\n"
                response += "1. Specialist \n"
                response += "2. Reminder \n"
                response += "3. Pharmacy \n"
                response += "4. Hospital \n"
                response += "5. Caretaker\n"
                return response
            elif text == "1":
                response = "END welldone you can read english"
                return response
            elif text == "2":
                response = "reminder"
                return response
            elif text == "3":
                response = "Pharmacy"
            elif text == "4":
                response = "Hospital"
            elif text == "5":
                response = "Caretaker"
                return response
            else:
                return "Invalid Input"

    else:
        fake_db.update(
            {
                phone_number: {
                    "location": "",
                    "name": "",
                    "phone": phone_number,
                    "joined": time.time(),
                    "history": [
                        {}
                    ]
                }}
        )
        return "CON please type your name"
