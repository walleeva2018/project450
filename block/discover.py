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
import blockchain
from block.create import all_chain




mining_blueprint = Blueprint('mining_blueprint', __name__)

@mining_blueprint.route('/discover',methods=['GET','POST'])
def mine_baby():
    id=0
    if (len(all_chain )== 0):
        id=0
    else:
        id=len(all_chain)
    if request.method=='POST':
        block_index=request.form.get('submit_button')
        print(block_index)
        return render_template('block.html',block=all_chain[int(block_index)-1])
    return render_template('discover.html', all_chain=all_chain,id=id)