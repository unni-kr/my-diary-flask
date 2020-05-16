from flask import request,jsonify,Blueprint
from flask_restplus import Resource
from flask import Flask

from app.main.service.entry_service import addEntry

entry = Blueprint('entry', __name__)

@entry.route('/', methods=['GET'])
def home():
    return jsonify('Welcome')

@entry.route('/saveentry', methods=['POST'])
def addEntryController():
    newEntry = request.get_json()
    return addEntry(newEntry)
    # req_data = request.get_json()
    # print(req_data)
    # title = req_data['entry_title']
    # return '''title is : {}'''.format(title)
