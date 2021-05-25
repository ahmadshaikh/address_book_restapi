from mongoengine import *
from datetime import datetime
import os
import json
from flask import render_template, request, redirect, jsonify, make_response

connect ("mongo-dev-db")

from flask import Flask,jsonify

app = Flask(__name__)

@app.route('/json', methods =["Post"])
def json():
    if request.is_json :
        req = request.get_json()

        response = {
            "name " : req.get("name"),
            "email_address": req.get("email_address"),
            "phone_numbers": req.get("phone_numbers"),
            "address": "122,street,Mumbai",
            "city": "Mumbai",
            "state": "Maharashtra",
            "country": "India",
            "pincode": "401017"
        }
        res = make_response(jsonify(response)), 200
        return res

    else:
        res = make_response(jsonify({"message":"No Json recieved"})), 400

        return res

class Address(Document):
    name = StringField()
    address = StringField()
    city = StringField()
    state = StringField()
    country = StringField()
    pincode = StringField()
    phone_numbers = IntField()
    email_address = StringField()

    def payload(self):
        return {
            "id": str(self.id),
            "name" : self.name,
            "address" : self.address,
            "city" : self.city,
            "state" : self.state,
            "country" : self.country,
            "pincode" : self.pincode,
            "phone_numbers" : self.phone_numbers,
            "email_address" : self.email_address
        }

user = Address(
    name="Ahmad",
    email_address="Ahmad@gmail.com",
    phone_numbers =98653122314,
    address = "122,street,Mumbai",
    city = "Mumbai",
    state = "Maharashtra",
    country = "India",
    pincode= "401017",
)
user = Address(
    name="Ram",
    email_address="Ram@gmail.com",
    phone_numbers =9683906093,
    address = "875,Junagad,Gujrat",
    city = "Ahemadabad",
    state = "Gujrat",
    country = "India",
    pincode= "908749",
)
user = Address(
    name="Jasmin",
    email_address="Jasmin@yahoo.com",
    phone_numbers =8345937685489,
    address = "699,almel,Banglore",
    city = "Banglore",
    state = "Karnataka",
    country = "India",
    pincode= "987345",
)
user = Address(
    name="Nausheen",
    email_address="Nausheen@gmail.com",
    phone_numbers =9479384578924,
    address = "321,Bunckingamm,Mumbai",
    city = "Mumbai",
    state = "Maharashtra",
    country = "India",
    pincode= "309888",
)
user = Address(
    name="Farheen",
    email_address="Farheen@gmail.com",
    phone_numbers =9847287289057,
    address = "787,Arizona,jupiter,Delhi",
    city = "Delhi",
    state = "Haryana",
    country = "India",
    pincode= "349285",
)
user = Address(
    name="Rahul",
    email_address="Rahul@gmail.com",
    phone_numbers =9835984068,
    address = "699,Greencomplex,Miraroad",
    city = "Mumbai",
    state = "Maharashtra",
    country = "India",
    pincode= "4680985",
)
#
# from api import api
# np = Namespace("address")
#
# class AddressRoutes(Resource):
#     def get(self, id = None):
#         try:
#             if id:
#                 try:
#                     address = Address.objects.get(id = id)
#                     return address.payload()
#                 except DoesNotExist:
#                     return {'msg': "Address not found"}, 404
#             else:
#                 addresses = Address.objects.all()
#                 response = list()
#                 for address in addresses:
#                     response.append(address.payload())
#                 return response
#         except Exception as e:
#             return {'msg': 'Server Error'}, 500
#
#     @np.expect(add_address)
#     def post(self):
#         try:
#             # adding new address to database
#             address = Address(**np.payload)
#             address.save()
#             return {"id" : str(address.id)}, 201
#         except Exception as e:
#             print(e)
#             return {"msg": "Server Error"}, 500
#
# np.add_resource(AddressRoutes, "", methods = ['GET', 'POST'])
# np.add_resource(AddressRoutes,'/<id>', methods = ['GET', 'PUT', 'DELETE'])
#
# def create_app():
#     app = Flask(__name__)
#     from .address.routes import np as address_namespace
#     api.add_namespace(address_namespace, path="/api/v1/address")
#     return app


if __name__ == '__main__':

    app.run(debug=True)