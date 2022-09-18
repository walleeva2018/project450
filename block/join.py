
from flask import Blueprint, render_template
from flask import Flask
from flask import request
from flask import jsonify , redirect , session
from functools import wraps
from block.create import all_chain

block_blueprint = Blueprint('block_blueprint', __name__)


#decorator 
def login_require(f):
    @wraps(f)
    def wrap(*args,**kwargs):
        if session['logging'] == "LogPut":
            return redirect('/user/signin')
        else:
            return f(*args, **kwargs)
           
    return wrap


@block_blueprint.route('/join',methods=['GET'])
@login_require
def blocking():
    id=0
    if (len(all_chain )== 0):
        id=0
    else:
        id=len(all_chain)
    return render_template('join.html',all_chain=all_chain,id=id)