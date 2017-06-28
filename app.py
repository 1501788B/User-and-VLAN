#!/usr/bin/python
import json
import vymgmt
import user
import vlan
from flask import Flask, jsonify
from flask.ext.httpauth import HTTPBasicAuth

app  = Flask(__name__)

auth = HTTPBasicAuth()

@auth.get_password
def get_password(username):
        if username == 'ariffin':
                return 'mohd'
        return None

@auth.error_handler
def unauthorised():
        return make_response(jsonify( {'error': 'Unauthorised access' } ), 403)

@app.errorhandler(400)
def not_found(error):
        return make_response(jsonify( {'error' : 'Bad Request' } ), 400)
        
@app.errorhandler(404)
def not_found(error):
        return make_response(jsonify( {'error' : 'Not Found' } ),404)

@app.route('/createuser', methods=['POST'])
def createuser():
	name = request.json['name']
	fullname = request.json['fullname']
	userlevel = request.json['userlevel']
	password = request.json['password']
	user.createuser(name, fullname, userlevel, password)
	return jsonify({'user created' : name}), 201

@app.route('/deleteuser/<name>', methods=['DELETE'])

def deleteuser(name):

	user.deleteuser(name)
	return jsonify({'User deleted':name}), 201


@app.route('/readuser', methods=['GET'])

def readuser():
	user=user.readuser()
	return jsonify({'user':user.splitlines()})




@app.route('/updateuser/<name>', methods=['PUT'])
def updateuser(name):
	fullname = request.json['fullname']
	userlevel = request.json['userlevel']
	password = request.json['password']
	user.updateuser(name, fullname, userlevel, password)
	return jsonify({'User updated':name,
			'fullname':fullname,
			'userlevel':userlevel,
			'password':password}), 201

@app.route('/createvlan', methods=['POST'])
def createvlan():
	interface = request.json['interface']
	number = request.json['number']
	description = request.json['description']
	address = request.json['address']
	vlan.createvlan(interface, number, description, address)
	return jsonify ({'interface':interface,
			'number':number,
			'description':description,
			'address':address}), 201

@app.route('/deletevlan/<interface>', methods=['DELETE'])
def deletevlan(interface):

	
	number = request.json['number']
	vlan.deletevlan(interface, number)
	return jsonify({'VLAN deleted':interface,
			'Number deleted':number}), 201

@app.route('/updatevlan/<interface>', methods=['PUT'])
def updatevlan(interface):

	number = request.json('number')
	description = request.json('description')
	address = request.json('address')
	vlan.updatevlan(interface, number, description, address)
	return jsonify({'interface':interface,
			'number':number,
			'description':description,
			'address':address}), 201


if __name__=='__main__':
	app.run(debug=True)