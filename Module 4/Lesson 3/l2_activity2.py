students = {
    "id1" : {"Name": "Alice",   "Subject": "Computer Science", "Grade": "VII"},
    "id2" : {"Name": "Bob",     "Subject": "Mathematics",      "Grade": "VIII"},
    "id3" : {"Name": "Charlie", "Subject": "Physics",          "Grade": "VI"},
    "id4" : {"Name": "Diana",   "Subject": "Chemistry",        "Grade": "VII"},
    "id5" : {"Name": "Ethan",   "Subject": "Biology",          "Grade": "IX"},
    "id6" : {"Name": "Alice",   "Subject": "Computer Science", "Grade": "VII"},
}

result = {}

for key, value in students.items():
    name = value["Name"]
    if name not in result:
        result[name] = value

for i in result.values():
    print(i)