def dijkstra(graph, s): #接收图和源点
    if not graph:
        return None
    #定义一个存放所有结点的列表
    Nodes = [i for i in range(len(graph))]
    #定义一个存放已经求得最短路径的点的列表
    visited = []
    if s in Nodes:
        visited.append(s)
        Nodes.remove(s) #匹配到列表中第一个满足条件的匹配项

    else:
        return None
    #定义一个字典，存放由源点到各个点的最短距离
    distance = {s:0}
    #对字典进行初始化
    for node in Nodes:
        distance[node] = graph[s][node]


    while Nodes:
        for v in visited:
            min_distance = float('inf')
            for n in Nodes:
                new_distance = graph[s][v]+graph[v][n]
                if new_distance < min_distance:
                    min_distance = new_distance
                    graph[s][n] = new_distance
                    Node = n
                if graph[s][n] < distance[n]:
                    distance[n] = graph[s][n]

            # print(distance)
        print(Node)
        visited.append(Node)
        Nodes.remove(Node)

    return distance

if __name__ == '__main__':
    graph_list = [ [0, 6, 3, float('inf'), float('inf'), float('inf')],
            [6, 0, 7, 5, float('inf'), 2],
            [3, 7, 0, 3, 4, float('inf')],
            [float('inf'), 5, 3, 0, 2, 3],
            [float('inf'), float('inf'), 4, 2, 0, 5],
            [float('inf'), 2, float('inf'), 3, 5, 0]]

    distance = dijkstra(graph_list, 0)  # 查找从源点0开始带其他节点的最短路径
    print(distance)
