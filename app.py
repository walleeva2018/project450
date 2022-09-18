from flask import Flask
from flask import render_template
from flask_cors import CORS
from user.routes import user_blueprint
from block.join import block_blueprint
from block.create import blocky_blueprint
from block.wallet import wall_blueprint
from block.discover import mining_blueprint
import blockchain
import hashlib
import json
from time import time
from uuid import uuid4
from flask import jsonify

app = Flask(__name__)
app.register_blueprint(user_blueprint)
app.register_blueprint(block_blueprint)
app.register_blueprint(blocky_blueprint)
app.register_blueprint(wall_blueprint)
app.register_blueprint(mining_blueprint)


app.secret_key='b\xd1B\xd1@nS\xd3\xdb\xb9.\x07y!\xd8\xa7'

node_identifier = str(uuid4()).replace('-', '')



@app.route("/")
def hello_world():
    return render_template('homepage.html')



if __name__ == '__main__':
    app.run(debug=True)


