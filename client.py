import sys
import json
import requests

conv=open('tester').read()
middle = json.loads(conv)
s = json.dumps(middle)
res = requests.post("http://130.239.81.123:5000/determine_escalation/", json=s).json()
data = json.loads(res)
print(data['escalate'])
