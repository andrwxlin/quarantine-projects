import json

with open('./credentials.json') as f:
    data = json.load(f)

def login(un, pw):

    if data['username'] == un and data['password'] == pw:
        print("logged in successfully")
        return True
    else:
        print("invalid credentials")
        return False

while True:
    try:
        uName = input("Username:")
        pwd = input("Password:")

        if login(uName, pwd):
            break
    except Exception as e:
        print (e)