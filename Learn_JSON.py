import json
data = {
    'president':
        {
            'name': "Ram",
            'age': 60
        },
    'prime-minister':
        {
            'name': 'Modi',
            "age": 65,
            'salary': 100000
        }
}
# data = ["adadadad"]

# json.dumps(data)
# with open("json_file.txt", 'a+') as wf:
#     json.dump(data, wf, indent=4)

with open("json_file.txt", "r+") as rf:
    z = json.load(rf)
    print(isinstance(z, object))
    print(z)

for i,j in z.items():
    if "prime" in i:
        z[i]['name'] = "Narendra"
print(z)


# ## 1. Write a Python program to convert JSON data to Python object
json_data = {'a': 1, 'b': 2}
py_obj = json.dumps(json_data)
print(py_obj)
print(type(json_data))
print(type(py_obj))

# ## 2. Write a Python program to convert Python object to JSON data.
json_data = {'a': 1, 'b': 2}
py_obj = json.dumps(json_data)
new_jso_data = json.loads(py_obj)
print(new_jso_data)
print(type(new_jso_data))
print(type(py_obj))

# ## 3. Write a Python program to convert Python objects into JSON strings. Print all the values. 

# ## 4. Write a Python program to convert Python dictionary object (sort by key) to JSON data.
# Print the object members with indent level 4. 

# ## 5. Write a Python program to convert JSON encoded data into Python objects.

# ## 6. Write a Python program to create a new JSON file from an existing JSON file.
# Read exisiting json file
with open("json_file.txt", 'r+') as rf:
    z = json.load(rf)
    print(z)
with open("new_test_json_file.json", 'w') as wf:
    json.dump(z, wf)

# ## 7. Write a Python program to check whether an instance is complex or not.

# ## 8. Write a Python program to check whether a JSON string contains complex object or not.

# ## 9. Write a Python program to access only unique key value of a Python object
with open("json_file.txt", 'r+') as rf:
    z = json.load(rf)

keys = z.keys()
vals = set(list(z.values())[1].keys()).difference(set(list(z.values())[0].keys()))
print(vals)
# s1 = set(vals[0].keys())
# s2 = set(vals[1].keys())
# unique = s2.difference(s1)
# print(s1,s2, unique)

import json
python_obj = '{"a":  1, "a":  2, "a":  3, "a": 4, "b": 1, "b": 2}'
print("Original Python object:")
print(python_obj)
json_obj = json.loads(python_obj)
print("\nUnique Key in a JSON object:")
print(json_obj)

