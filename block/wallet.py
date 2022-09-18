from flask import Blueprint, render_template

wall_blueprint = Blueprint('wall_blueprint', __name__)

from block.create  import all_chain

@wall_blueprint.route('/wallet',methods=['GET','POST'])
def wallet():
    id=0
    network="Network"
    if (len(all_chain )== 0):
        id=0
    else:
        id=len(all_chain)
        network=all_chain[0].name
    return render_template('wallet.html',all_chain=all_chain,id=id,network=network)

def duka():
     print("miao")