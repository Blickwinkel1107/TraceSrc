from django.shortcuts import render
from TraceSrc.Algorithm import findPath
from TraceSrc.Algorithm import py2js
import json

# index front-to-end connector
def index(req):
    ctx = dict()
    jsonEncoder = json.JSONEncoder()
    testBlock = {
        'start': 17,
        'end': 18,
        'option': {
            'label': '25特仑苏25酸酸乳25新养道'
        }
    }
    encodeData = json.dumps(testBlock, separators=(',', ':'), ensure_ascii=False)
    ctx['testBlock'] = encodeData
    return render(req, r'../templates/pages/graph.html', ctx)
