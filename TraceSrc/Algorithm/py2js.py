# created by yx @ 2018/8/17
import json
from TraceSrc.Algorithm.data import allVertices, allEdges

# main func
def parse(pyData):
    jsData = {
        'state':[],
        'edg':[]
    }
    vectexVec = []
    edgeVec = []
    # generate trace path
    for src, destVec in pyData.items():
        vectexVec.append(src)
        for destInfo in destVec:
            dest = destInfo[0]
            edgeVec.append((src, dest))
    #print(vectexVec)
    #print(edgeVec)
    # generate json
    for vertexDict in allVertices:
        if 'V%d' % vertexDict['id'] in vectexVec:
            jsData['state'].append(vertexDict)
    for edgeDict in allEdges:
        edge = ('V%d' % edgeDict['start'], 'V%d' % edgeDict['end'])
        if edge in edgeVec:
            jsData['edg'].append(edgeDict)
    encodeData = json.dumps(jsData, separators=(',', ':'), ensure_ascii=False)
    return encodeData   #parse(pyData)


# for test
def parseTest():
    testBlock = {
        'start': 17,
        'end': 18,
        'option': {
            'label': '25特仑苏25酸酸乳25新养道'
        }
    }
    encodeData = json.dumps(testBlock, separators=(',', ':'), ensure_ascii=False)
    return encodeData   #parseTest()

# unit test
if __name__ == '__main__':
    pass