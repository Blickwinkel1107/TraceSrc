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
                        if (x[0] == item[i][0]):
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
                dict[i[num][0]].append(i[num + 1])
        return dict


graph = {'A': [['B', "30goods A"], ['C', "20 goods A"]], 'B': [['D', "10 goods A"]], 'C': [['D', "10 goods A"]],
         'D': []}
while True:
    vertice = input("请输入起始节点序号：")
    while (vertice not in graph.keys()):
        vertice = input("图中不包含该节点，请重新输入起始节点序号：")
    temp = int(input("追踪->0,溯源->1："))
    if (temp == 0):
        print(route_merge(find_all_paths(graph, vertice, 'D'), graph))
    elif (temp == 1):
        print(route_merge(find_all_paths(graph, 'A', vertice), graph))
    else:
        print("输入不合法，请重新输入信息：")