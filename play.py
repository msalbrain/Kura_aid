d = {
    "Edo": ["oredo"]
}

loc = d.get(state, None)

if loc == None:
    return "END "

for i in d[state]:
    response += i




if loc == None and state == "":
    return "CON please provide your state"



lga_nd_hospital = {
    "oredo": ["la hospital"]
}

from app import fake_db

user = fake_db.get(phone) // tryin to get user data


user_lga = user["LGA"]   // getting lga from user data

list_of_hospital = lga_nd_hospital.get(user_lga) // checking lga_nd_hospital for list of hospital

response = "CON this are the hospital"
for i in list_of_hospital:      // iterating through and concatenating to response
    response += f"{i}\n"

return response









