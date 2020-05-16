from ..model.entry import entry
import uuid
import datetime
from app.main import db
import json

def addEntry(newEntry):
    entry.__table__.drop()
    print(newEntry['date_time'])
    date_object = datetime.datetime.strptime(newEntry['date_time'], '%Y-%m-%d').date()
    new_entry = entry(
        date_object,
        newEntry['entry_title'],
        newEntry['entry_desc']
    )
    return saveEntry(new_entry)
    
def saveEntry(new_entry):
    failed=False
    entry.__table__.drop(engine)
    try:
        db.session.add(new_entry)
        db.session.commit() 
        response_object = {
            'status': 'success',
            'message': 'Successfully registered.'
        }
        return response_object, 201
    except Exception as e:
        print(e)
        db.session.rollback()
        db.session.flush()
        failed=True
        response_object = {
            'status': 'failure',
            'message': 'internal error occured.'
        }
        return response_object, 500




