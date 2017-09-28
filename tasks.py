import json
from celery import Celery

app = Celery('tasks', backend='rpc://', broker='pyamqp://guest@localhost//')

@app.task
def test(x):
    data= json.loads(x)
    result = {'escalate': True}
    return json.dumps(result)
