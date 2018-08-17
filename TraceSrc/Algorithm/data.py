# vertex & edge

allVertices = [
    {"id": 1, "label": 'V1\n供货商A', "class": 'type-suss'},
    {"id": 2, "label": 'V2\n供货商B', "class": 'type-suss'},
    {"id": 3, "label": 'V3\n供货商C', "class": 'type-init'},
    {"id": 4, "label": 'V4\n供货商D', "class": 'type-ready'},
    {"id": 5, "label": 'V5\n供货商E', "class": 'type-fail'},
    {"id": 6, "label": 'V6\n供货商F', "class": 'type-suss'},
    {"id": 7, "label": 'V7\n供货商G', "class": 'type-suss'},
    {"id": 8, "label": 'V8\n供货商H', "class": 'type-freeze'},
    {"id": 9, "label": 'V9\n供货商I', "class": 'type-suss'},
    {"id": 10, "label": 'V10\n供货商J', "class": 'type-queue'},
    {"id": 11, "label": 'V11\n供货商K', "class": 'type-run'},
    {"id": 12, "label": 'V12\n特仑苏工厂', "class": 'type-suss'},
    {"id": 14, "label": 'V14\n酸酸乳工厂', "class": 'type-fail'},
    {"id": 15, "label": 'V15\n新养道工厂', "class": 'type-freeze'},
    {"id": 16, "label": 'V16\n蒙牛制造总部', "class": 'type-suss'},
    {"id": 17, "label": 'V17\n蒙牛行销总部', "class": 'type-queue'},
    {"id": 18, "label": 'V18\n北京分公司', "class": 'type-run'},
    {"id": 19, "label": 'V19\n武汉分公司', "class": 'type-suss'},
    {"id": 20, "label": 'V20\n温州分公司', "class": 'type-init'},
    {"id": 21, "label": 'V21\n卖场A', "class": 'type-fail'},
    {"id": 22, "label": 'V22\n卖场B', "class": 'type-fail'},
    {"id": 23, "label": 'V23\n卖场C', "class": 'type-fail'},
    {"id": 24, "label": 'V24\n卖场D', "class": 'type-fail'},
    {"id": 25, "label": 'V25\n卖场E', "class": 'type-fail'},
    {"id": 26, "label": 'V26\n客户A', "class": 'type-run'},
    {"id": 27, "label": 'V27\n客户B', "class": 'type-run'},
    {"id": 28, "label": 'V28\n客户C', "class": 'type-run'},
    {"id": 29, "label": 'V29\n客户D', "class": 'type-run'},
    {"id": 30, "label": 'V30\n客户E', "class": 'type-run'},
    {"id": 31, "label": 'V31\n客户F', "class": 'type-run'},
    {"id": 32, "label": 'V32\n客户G', "class": 'type-run'},
    {"id": 33, "label": 'V33\n客户H', "class": 'type-run'},
    {"id": 34, "label": 'V34\n客户I', "class": 'type-run'}
]

allEdges = [
    {"start": 1, "end": 12, "option": {"label": "生牛乳"}},
    {"start": 2, "end": 12, "option": {"label": "生牛乳"}},
    {"start": 3, "end": 12, "option": {"label": "生牛乳"}},
    {"start": 4, "end": 12, "option": {"label": "白砂糖"}},
    {"start": 5, "end": 12, "option": {"label": "食品添加剂"}},

    {"start": 6, "end": 14, "option": {"label": "生牛乳"}},
    {"start": 7, "end": 14, "option": {"label": "白砂糖"}},
    {"start": 8, "end": 14, "option": {"label": "食品添加剂"}},

    {"start": 9, "end": 15, "option": {"label": "生牛乳"}},
    {"start": 10, "end": 15, "option": {"label": "白砂糖"}},
    {"start": 11, "end": 15, "option": {"label": "食品添加剂"}},

    {"start": 12, "end": 16, "option": {"label": "50特仑苏"}},
    {"start": 14, "end": 16, "option": {"label": "60酸酸乳"}},

    {"start": 15, "end": 17, "option": {"label": "55新养道"}},

    {"start": 17, "end": 18, "option": {"label": "25特仑苏25酸酸乳25新养道"}},
    {"start": 17, "end": 19, "option": {"label": "15特仑苏15酸酸乳10新养道"}},
    {"start": 17, "end": 20, "option": {"label": "10特仑苏20酸酸乳20新养道"}},

    {"start": 18, "end": 21, "option": {"label": "15特仑苏10酸酸乳10新养道"}},
    {"start": 18, "end": 22, "option": {"label": "10特仑苏15酸酸乳15新养道"}},

    {"start": 19, "end": 23, "option": {"label": "15特仑苏15酸酸乳15新养道"}},

    {"start": 20, "end": 24, "option": {"label": "5特仑苏15酸酸乳5新养道"}},
    {"start": 20, "end": 25, "option": {"label": "5特仑苏5酸酸乳15新养道"}},

    {"start": 21, "end": 26, "option": {"label": "2 1 2"}},
    {"start": 21, "end": 27, "option": {"label": "3 2 2"}},

    {"start": 22, "end": 28, "option": {"label": "2 4 1"}},

    {"start": 23, "end": 29, "option": {"label": "2 3 3"}},

    {"start": 24, "end": 30, "option": {"label": "2 1 1"}},
    {"start": 24, "end": 31, "option": {"label": "3 1 2"}},

    {"start": 25, "end": 32, "option": {"label": "2 2 4"}},
    {"start": 25, "end": 33, "option": {"label": "1 0 2"}},
    {"start": 25, "end": 34, "option": {"label": "0 1 3"}}
]

graph = {
    'V0': [['V1', ""], ['V2', ""], ['V3', ""], ['V4', ""], ['V5', ""], ['V6', ""], ['V7', ""], ['V8', ""], ['V9', ""],
           ['V10', ""], ['V11', ""]], 'V1': [['V12', "生牛乳"]], 'V2': [['V12', "生牛乳"]], 'V3': [['V12', "生牛乳"]],
    'V4': [['V12', "白砂糖"]]
    , 'V5': [['V12', "食品添加剂"]], 'V6': [['V14', "生牛乳"]], 'V7': [['V14', "白砂糖"]], 'V8': [['V14', "食品添加剂"]],
    'V9': [['V15', "生牛乳"]],
    'V10': [['V15', "白砂糖"]], 'V11': [['V15', "食品添加剂"]], 'V12': [['V16', "50 特仑苏"]], 'V14': [['V16', "60 酸酸乳"]],
    'V15': [['V17', "55 新养道"]],
    'V16': [['V17', "50特仑苏 60酸酸乳"]],
    'V17': [['V18', "25特仑苏 25酸酸乳 25新养道"], ['V19', "15特仑苏 15酸酸乳 10新养道"], ['V20', "10特仑苏 20酸酸乳 20新养道"]],
    'V18': [['V21', "15特仑苏 10酸酸乳 10新养道"], ['V22', "10特仑苏 15酸酸乳 15新养道"]], 'V19': [['V23', "15特仑苏 15酸酸乳 15新养道"]],
    'V20': [['V24', "5特仑苏 15酸酸乳 5新养道"], ['V25', "5特仑苏 5酸酸乳 15新养道"]],
    'V21': [['V26', "2特仑苏 1酸酸乳 2新养道"], ['V27', "3特仑苏 2酸酸乳 2新养道"]], 'V22': [['V28', "2特仑苏 4酸酸乳 1新养道"]],
    'V23': [['V29', "2特仑苏 3酸酸乳 3新养道"]], 'V24': [['V30', "2特仑苏 1酸酸乳 1新养道"], ['V31', "3特仑苏 1酸酸乳 2新养道"]],
    'V25': [['V32', "2特仑苏 2酸酸乳 4新养道"], ['V33', "1特仑苏 0酸酸乳 2新养道"], ['V34', "0特仑苏 1酸酸乳 3新养道"]], 'V26': [['VEND', ""]],
    'V27': [['VEND', ""]], 'V28': [['VEND', ""]], 'V29': [['VEND', ""]], 'V30': [['VEND', ""]], 'V31': [['VEND', ""]],
    'V32': [['VEND', ""]], 'V33': [['VEND', ""]], 'V34': [['VEND', ""]], 'VEND': []
}