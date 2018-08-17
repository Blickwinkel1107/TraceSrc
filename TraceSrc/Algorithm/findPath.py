def find_all_paths(graph, start, end, path=[]):
    path = path + [[start]]
    if start == end:
        return [path]
    if (start in graph.keys() == False):
        return []
    paths = []
    for itemtemp in graph[start]:
        if itemtemp[0] not in path:
            newpaths = find_all_paths(graph, itemtemp[0], end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths


def route_merge(list, graph):
    for item in list:
        for i in range(1, len(item)):
            for key in graph:
                if (key == item[i - 1][0]):
                    for x in graph[key]:
                        if (x[0] == item[i][0] and x[1] not in item[i]):
                            item[i].append(x[1])
    dict = {}
    for i in list:
        for j in range(0, len(i)):
            dict[i[j][0]] = []
    if len(list) == 1:
        for i in range(0, len(list[0]) - 1):
            dict[list[0][i][0]].append(list[0][i + 1])
        return dict
    else:
        for i in list:
            for num in range(0, len(i) - 1):
                if (i[num + 1] not in dict[i[num][0]]):
                    dict[i[num][0]].append(i[num + 1])
        return dict


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
    'V32': [['VEND', ""]], 'V33': [['VEND', ""]], 'V34': [['VEND', ""]], 'VEND': []}

if __name__ == '__main__':
    while True:
        vertice = input("请输入起始节点序号：")
        while (vertice not in graph.keys()):
            vertice = input("图中不包含该节点，请重新输入起始节点序号：")
        temp = int(input("追踪->0,溯源->1："))
        if (temp == 0):
            '''print(find_all_paths(graph,vertice,'VEND'))'''
            print(route_merge(find_all_paths(graph, vertice, 'VEND'), graph))
        elif (temp == 1):
            '''print(find_all_paths(graph,'V0',vertice))'''
            print(route_merge(find_all_paths(graph, 'V0', vertice), graph))
        else:
            print("输入不合法，请重新输入信息：")