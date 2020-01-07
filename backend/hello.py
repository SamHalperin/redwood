from flask import Flask, Response, request, jsonify, make_response
import random
import json
import time

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/add', methods=["POST"])
def add():
    a = 0
    b = 0
    emsg=""
    try :
        a = float(request.form['a'])
        b = float(request.form['b'])
    except Exception as e:
        emsg = str(e)
        
    mode = random.randint(0,5)
    print(f"Mode is {mode}")
    if emsg != "":
       return make_response(jsonify({"exception": emsg}), 400)
    elif mode in range(0,4): #add
        return jsonify({"sum" : a+b})
    elif mode == 4: #timeout
        time.sleep(30)
        return jsonify({"exception": "we should have timed out before seeing this data"}, 400 )
    elif mode == 5: #service unavailable
        return make_response(jsonify({}), 503)
