from flask import Flask , jsonify,request,redirect
from database import Database
from passlib.hash import pbkdf2_sha256
from flask import session
from ecdsa import SigningKey
private_key = SigningKey.generate() # uses NIST192p
public_key = private_key.verifying_key


class User:

    def start_seission(self,user):
        session['logging'] = True
        session['name']=user['name']
        session['secret_key']=user['secretKey']
        session['public_key']=user['publicKey']
        return 

    def signup(self):
        private_key = SigningKey.generate() # uses NIST192p
        public_key = private_key.verifying_key
        user={
           "name": request.form.get('name'),
           "email": request.form.get('email'),
           "password": request.form.get('password'),
           "Phrase": "",
           "extra": "",
           "network": [],
           "amount": [],
           "publicKey": public_key,
           "secretKey": private_key,
           "extralist": [],
           "extramap": {},
        }
        if user['name'] =="":
            return "Please enter a user name"
        if user['email'] == "":
            return "Please enter a valid email"
        if user['password'] == "":
            return "Please enter a secure password"
        else:
            user['password']= pbkdf2_sha256.encrypt(user['password'])
        
  


        if Database.Storage.find_one({'email': user['email']}):
            return "Email already Used"
        if Database.Storage.insert_one(user):
            self.start_seission(user)
            return 200
        return 200
    def signout(self):
        session.clear()
        session['logging']="LogPut"
        return redirect('/user/signup')
    def signin(self):
        user=Database.Storage.find_one({
            "email":request.form.get('email')
        })
        if user:
            if pbkdf2_sha256.verify(request.form.get('password'),user['password']):
                self.start_seission(user)
                return 200
            else:
                return "Invalid Password"
        return "Wrong Email"

