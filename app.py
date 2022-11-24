from fastapi import FastAPI, Request, responses

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
    fake_db["phone"].update(user)
    return "State Your Name"

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
        if user["name"] == "" and user["location"] == "":
           return unregisteredUser(text, phone)
        else: 
            if text == "":
                response = "CON Welcome to Kura where yo have access to quality health services"
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
    
        

