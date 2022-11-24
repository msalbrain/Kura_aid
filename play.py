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
