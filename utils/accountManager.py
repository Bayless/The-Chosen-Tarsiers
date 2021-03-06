
#Manages the account info tables in the db
import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O



''' 
1. authenticate: authenticate credentials
2. register: make sure username not used
'''

from hashlib import sha1

'''testing purposes
p = """INSERT INTO users VALUES("%s","%s",%d)""" %("firstEnrty","hashedpass",0)
c.execute(p)
'''
#authenticate user returns true if authentication worked

def authenticate(user,password):

    f="database.db"
    db = sqlite3.connect(f) #open if f exists, otherwise create
    c = db.cursor()  #facilitate db ops  <-- I don't really know what that means but ok
    isLogin = False #Default to false; login info correct?
    loginStatusMessage = "" #what's wrong
    messageNumber = 0 #represents what kind of error it is
    passHash = sha1(password).hexdigest()#hash it

    checkUser = 'SELECT * FROM users WHERE username=="%s";' % (user)  #checks if the user is in the database
    c.execute(checkUser)
    l = c.fetchone() #listifies the results
    if l == None:
        isLogin = False
        messageNumber = 0
        loginStatusMessage = "user does not exist"
    elif l[1] == passHash:
        isLogin = True
        messageNumber = 1
        loginStatusMessage = "login info correct"
    else:
        isLogin = False
        messageNumber = 2
        loginStatusMessage = "wrong password"

    db.commit() #save changes
    db.close()  #close database
    return messageNumber

#returns true if register worked
def register(user,password,pwd):    #user-username, password-password, pwd-retype
    f="database.db"
    db = sqlite3.connect(f) #open if f exists, otherwise create
    c = db.cursor()  #facilitate db ops  <-- I don't really know what that means but ok
    isRegister = False #defualt not work
    registerStatus = ""
    messageNumber = 0 #for message


    checkUser = 'SELECT * FROM users WHERE username=="%s";' % (user)  #checks if the user is in the database
    c.execute(checkUser)
    l = c.fetchone() #listifies the results

    if l != None:
        isRegister = False
        messageNumber = 0
        registerStatus = "username taken"
    elif (len(password) < 8 or len(pwd) < 8 ):
        isRegister = False
        messageNumber = 3 #two is already used below :/
        registerStatus = "password too short"
    elif (len(user) == 0):
        isRegister = False
        messageNumber = 4 #so this happened :/
        registerStatus = "username left blank"
    elif (password != pwd):
        isRegister = False
        messageNumber = 1
        registerStatus = "passwords do not match"
    elif (password == pwd):
        passHash = sha1(password).hexdigest()#hash it
        insertUser = 'INSERT INTO users VALUES ("%s","%s");' % (user,passHash) #sqlite code for inserting new user

        c.execute(insertUser)

        isRegister = True
        messageNumber = 2
        registerStatus = "user %s registered!" % (user)

    db.commit() #save changes
    db.close()  #close database
    return messageNumber

register("bayle","T@rsi3rs","T@rsi3rs")
