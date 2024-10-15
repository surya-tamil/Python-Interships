a={
    "name":"Surya",
    "age":23,
    "Location":"Bangalore",
    "Frinends":["bala","hari","vasanth"]
}
print(a)
print(a.values())
print(a.keys())
a.update({"age":30})
print(a)
del a["age"]
print(a)