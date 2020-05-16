from app.main import db
from sqlalchemy.schema import Sequence

class entry(db.Model):
    __tablename__ = "diary_entry"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    entry_date_time = db.Column(db.DateTime, nullable=False)
    entry_title = db.Column(db.String(100), unique=False, nullable=False)
    entry_desc = db.Column(db.String(255), unique=False, nullable=False)

    def __repr__(self):
        return "<entry '{}'>".format(self.entry_title)

    def __init__(self,id, entry_date_time, entry_title, entry_desc):
        self.id = id
        self.entry_date_time = entry_date_time
        self.entry_title = entry_title
        self.entry_desc = entry_desc

    def __init__(self, entry_date_time, entry_title, entry_desc):
        self.entry_date_time = entry_date_time
        self.entry_title = entry_title
        self.entry_desc = entry_desc