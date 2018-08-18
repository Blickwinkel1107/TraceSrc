from django.shortcuts import render
from TraceSrc.Algorithm import findPath
from TraceSrc.Algorithm import py2js
from django.views.decorators.csrf import csrf_exempt

# index front-to-end connector
@csrf_exempt
def index(req):
    ctx = dict()
    # 在这里调整追踪0还是溯源1
    # 前端只需要在这里处理即可
    direct = {'forwards':0, 'backwards':1}
    '''pyPath = findPath.process('V%d' % startNum, direct[directNum])
    jsPath = py2js.parse(pyPath)
    print(jsPath)
    print(type(jsPath))
    f.write(jsPath)
    f.close()'''
    if req.is_ajax():
        #print(req.POST)
        f = open(r'templates/scripts/args.txt', 'w')
        startNum = int(req.POST['point'])
        directNum = req.POST['direct']
        pyPath = findPath.process('V%d' % startNum, direct[directNum])
        jsPath = py2js.parse(pyPath)
        f.write(jsPath)
        f.close()
    f = open(r'templates/scripts/args.txt', 'r')
    ctx['graph'] = f.read()
    # print(ctx['graph'])
    f.close()
    return render(req, r'../templates/pages/graph.html', ctx)
