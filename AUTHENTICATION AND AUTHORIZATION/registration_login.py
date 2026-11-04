from pwdlib import PasswordHash

# step -1 : create the object for PasswordHash

password_hash = PasswordHash.recommended()

email = "kcssr62@gmail.com"

password = "Chaitu@123"

# password hashing 

hashed_password = password_hash.hash(password)

user_db = {

    "user_email" : email,
    "password" :  hashed_password
}

login_email = input("enter your email : ")

login_pass = input("Enter the password : ")

if login_email == user_db["user_email"] :

    result = password_hash.verify(login_pass, user_db["password"])

    if(result):

        print("user login successful ... ")
    else :

        print("wrong password ..!")       

else :

    print("Email not found in the database ")        