from pwdlib import PasswordHash

# creating a object for PasswordHash
password_hash = PasswordHash.recommended()

# original password

original_pass = "Chaitu@123"

hashed_pas = password_hash.hash(original_pass)

print("Original password : ",original_pass)

print("Hashed password : ", hashed_pas)

password = input("Enter your password : ")

result = password_hash.verify(password,hashed_pas)

if(result):

    print("user logins : ")

else:

    print("password wrong ")    