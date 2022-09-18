
from functools import wraps
from flask import Blueprint, render_template
from user.models import User
from flask import Flask
from flask import request
from user.models import User
from flask import jsonify , redirect , session , flash
from functools import wraps


user_blueprint = Blueprint('user_blueprint', __name__)






@user_blueprint.route('/user/signup',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        reply= User().signup() 
        if reply== 200:
            return redirect('/join')
        else:
            flash(reply)

    else:
        return render_template('signup.html', reply="")

@user_blueprint.route('/user/signout',methods=['GET'])
def out():
    return User().signout()


@user_blueprint.route('/user/signin',methods=['GET','POST'])
def getin():
    if request.method == 'POST':
        reply=User().signin()
        if reply == 200:
            return redirect('/join')
        else:
            return render_template('signin.html',reply=reply)
    else :
        return render_template('signin.html')

