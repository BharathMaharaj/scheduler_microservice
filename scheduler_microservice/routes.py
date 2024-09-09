from flask import Flask, jsonify, request
from models import Job, db
from datetime import datetime

app = Flask(__name__)

@app.route('/jobs', methods=['GET'])
def get_jobs():
    jobs = Job.query.all()
    return jsonify([job.to_dict() for job in jobs])

@app.route('/jobs/<int:job_id>', methods=['GET'])
def get_job(job_id):
    job = Job.query.get(job_id)
    if job:
        return jsonify(job.to_dict())
    else:
        return jsonify({'error': 'Job not found'}), 404

@app.route('/jobs', methods=['POST'])
def create_job():
    data = request.json
    job_name = data.get('job_name')
    interval = data.get('interval')

    if not job_name or not interval:
        return jsonify({'error': 'Invalid input'}), 400

    job = Job(
        job_name=job_name,
        interval=interval,
        last_run=None,
        next_run=datetime.utcnow()
    )

    db.session.add(job)
    db.session.commit()

    return jsonify(job.to_dict()), 201
