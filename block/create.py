from itertools import chain
from flask import Blueprint, render_template,redirect, url_for , json,session
import blockchain
from time import time
from uuid import uuid4
from flask import jsonify
from flask import request
import hashlib
import json
from textwrap import dedent
from time import time
from uuid import uuid4


node_identifier = str(uuid4()).replace('-', '')


blocky_blueprint = Blueprint('blocky_blueprint', __name__)


all_chain=[]

@blocky_blueprint.route('/mine', methods=['GET','POST'])
def mine(id):
    return id

@blocky_blueprint.route('/transactions/new', methods=['POST'])
def new_transaction():
    return "We'll add a new transaction"

@blocky_blueprint.route('/chain', methods=['GET'])
def full_chain():
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain),
    }
    return jsonify(response), 200


@blocky_blueprint.route('/create',methods=['GET','POST'])
def create():
     if request.method == 'POST':
        session['coinname'] = request.form.get('coinname')
        session['infa']=request.form.get('infa')
        session['chain']=request.form.get('chain')
        session['minfee']=request.form.get('minfee')
        return redirect(url_for('blocky_blueprint.public'))
     else:
          return render_template('create.html')
@blocky_blueprint.route('/public',methods=['GET','POST'])
def public():
    if request.method == 'POST':
        dchain = blockchain.Blockchain(session['coinname'],request.form.get('consensus'),session['minfee'])
        all_chain.append(dchain)
        return render_template('join.html',all_chain=all_chain,id=all_chain[0].get_id()-1)
    else:
        return render_template('public.html',coin=session['coinname'])

@blocky_blueprint.route('/mine',methods=['GET','POST'])
def letmine():
    return "Mining..."





