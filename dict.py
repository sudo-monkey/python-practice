import json

# load a dictionary
dictionary = {'name': 'shane', 'age': '29'}
# convert dictionary into json string
json_str = json.dumps(dictionary)
# convert json string into object
new_dictionary = json.loads(json_str)
# use the object to call out JSON key
print(new_dictionary['name', 'age'])
