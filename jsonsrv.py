from flask import Flask
from flask import request
from tasks import test
import json
import time

app = Flask(__name__)

@app.route('/determine_escalation/', methods = ['POST'])
def determine_escalation():
    jsondata = request.get_json()
    data = json.loads(jsondata)
    result = test.delay(jsondata)

    while result.ready() == False:
        time.sleep(0.5)

    return json.dumps(result.get(timeout=1))


if __name__ == '__main__':
    app.run(host='0.0.0.0')
