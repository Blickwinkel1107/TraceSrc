from django.shortcuts import render
from TraceSrc.Algorithm import findPath
from TraceSrc.Algorithm import py2js
import json

# index front-to-end connector
def index(req):
    ctx = dict()
    ctx['testBlock'] = py2js.parseTest()
    return render(req, r'../templates/pages/graph.html', ctx)
