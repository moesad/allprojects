import random
import string
print("welcome to password generator")
def passlength():
  print("how long do you want the password to be")
  global passlen
  try:
    input1=input()
    passlen=int(input1)
  except:
    print("choose a number")
    passlength()
  if passlen<5:
    print("too short, try again")
    passlength()
  elif passlen>30:
    print("thats too long")
    passlength()
  else:
    print("ok")
passlength()
def passwordgen():
  chars=string.ascii_letters+string.digits+"@$*!?/"
  password=""
  for x in range(passlen):
    password=password+random.choice(chars)
  print("your password is "+password)
passwordgen()