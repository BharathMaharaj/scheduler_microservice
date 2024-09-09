from celery import Celery
from celery.schedules import crontab

app = Celery('scheduler', broker='redis://localhost:6379/0')

@app.task
def dummy_job(job_id):
    print(f"Executing Job ID: {job_id}")

# Schedule a job every Monday
app.conf.beat_schedule = {
    'execute-every-monday': {
        'task': 'scheduler.dummy_job',
        'schedule': crontab(day_of_week=1, hour=0, minute=0),
        'args': (1,),  # Pass job_id here
    },
}
