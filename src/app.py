"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# create the jackson family object
jackson_family = FamilyStructure("Jackson")

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/members', methods=['GET', 'POST'])
def handle_member():
    # Method GET
    if request.method == 'GET':
        members = jackson_family.get_all_members()
        return members, 200
    
    # Method POST
    if request.method == 'POST':
        data = request.json
        members = jackson_family.add_member(data)
        return {'message' : members}, 200

    # Method NOT FOUND
    else:
        return {'message' : 'method not allowed'}, 405
  

@app.route('/members/<int:member_id>', methods=['GET', 'DELETE'])
def handle_member_id(member_id):
    # Method GET
    if request.method == 'GET':
        member = jackson_family.get_member(member_id)
        if member == []:
            return {'message' : 'member not found'}, 400
        return member[0], 200

    # Method DELETE
    if request.method == 'DELETE':
        member = jackson_family.delete_member(member_id)
        if member == 0:
            return {'message' : str(member_id) + ' deleted succesfully'}, 200
        else:
            return {'message' : str(member_id) + ' not found!'}, 400

    # Method NOT FOUND
    else:
        return {'message' : 'method not allowed'}, 405


# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
