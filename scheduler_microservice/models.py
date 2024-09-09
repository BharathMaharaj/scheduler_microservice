from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    job_name = db.Column(db.String(128), nullable=False)
    interval = db.Column(db.String(50), nullable=False)
    last_run = db.Column(db.DateTime, nullable=True)
    next_run = db.Column(db.DateTime, nullable=True)

    def to_dict(self):
        return {
            'id': self.id,
            'job_name': self.job_name,
            'interval': self.interval,
            'last_run': self.last_run,
            'next_run': self.next_run
        }
