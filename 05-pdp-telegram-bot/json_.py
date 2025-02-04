import json

#################### 1 ####################

# # try:
# with open('users.json', 'r') as file:
#     users = json.load(file)
#
#
# user = {
#   "fullname": "Sobirjon Abdumajid",
#   "age": 19,
#   "phone": "+9112345678",
#   "location": {
#       "long": 51352,
#       "lat": 1554
#   }
# }
#
# users.append(user)
# with open('users.json', mode='w') as file:
#     json.dump(users, file, indent=3)  # method to write to file


#################### 2 ####################

with open('users.json') as f:
    users = json.load(f)

for user in users:
    if user['fullname'] == "Sanjar Alisher":
        print(user)
