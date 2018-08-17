from django.shortcuts import render
from TraceSrc.Algorithm import findPath
from TraceSrc.Algorithm import py2js
import json

# index front-to-end connector
def index(req):
    ctx = dict()
    startNum = 34
    # 在这里调整追踪0还是溯源1
    # 前端只需要在这里处理即可
    direct = {'forwards':0, 'backwards':1}
    tracePath = findPath.process('V%d' % startNum, direct['backwards'])
    ctx['graph'] = py2js.parse(tracePath)
    return render(req, r'../templates/pages/graph.html', ctx)
