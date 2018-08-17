# created by yx @ 2018/8/17
import json

# main func
def parse(pyData):
    encodeData = json.dumps(pyData, separators=(',', ':'), ensure_ascii=False)
    return encodeData   #parse()


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