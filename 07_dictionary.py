

a = {
    "name": "Saaria",
    "age": 15,
    "hobbies": ["reading", "painting", "cooking"],
    "friends": ["zahid","sudaes","kabir"],
    "address":{
        "street":"123 street",
        "city":"New York",
    }

}


print(a["name"])
# Output - Saaria

print(a["age"])
# Output - 15
print(a["address"]["city"])
# Output - New York


print(a.keys())
# Output - dict_keys(['name', 'age', 'hobbies', 'friends', 'address'])
print(a.values())
# Output - dict_values(['Saaria', 15, ['reading', 'painting', 'cooking'], ['zahid', 'sudaes', 'kabir'], {'street': '123 street', 'city': 'New York'}])

print(a.items())
# Output - dict_items([('name', 'Saaria'), ('age', 15), ('hobbies', ['reading', 'painting', 'cooking']), ('friends', ['zahid', 'sudaes', 'kabir']), ('address', {'street': '123 street', 'city': 'New York'})])

print(a["agee"]) # agee is not correct spelling not exist in data so it will throw exception
# Output - KeyError: 'agee'

print(a.get("agee")) # agee is not correct spelling incase to handle excepion use get method
# Output - None
