import secrets
import string

chrector = string.ascii_letters + string.digits + string.punctuation

length = int(input ("Enter your length  : "))

password = " "

for i in range (length):
    password +=secrets.choice(chrector)

print("Genrate password : ",password)