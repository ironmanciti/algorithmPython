class Graph:
    def __init__(self):
        self.adjacentList = {}

    def __iter__(self):
        return iter(self.adjacentList.items())

    def add_vertex(self, vertex):
        if not vertex in self.adjacentList:
            self.adjacentList[vertex] = []

    def add_edge(self, v1, v2, weight):
        self.adjacentList[v1].append(v2)
        self.adjacentList[v2].append(v1)

class WeightedGraph(Graph):

    def add_edge(self, v1, v2, weight):
        self.adjacentList[v1].append({'node': v2, 'weight': weight})
        self.adjacentList[v2].append({'node': v1, 'weight': weight})

g = WeightedGraph()

g.add_vertex('a')
g.add_vertex('b')
g.add_vertex('c')
g.add_vertex('d')
g.add_vertex('e')
g.add_vertex('f')

g.add_edge('a', 'b', 7)
g.add_edge('a', 'c', 9)
g.add_edge('a', 'f', 14)
g.add_edge('b', 'a', 7)
g.add_edge('b', 'c', 10)
g.add_edge('b', 'd', 15)
g.add_edge('c', 'a', 9)
g.add_edge('c', 'b', 10)
g.add_edge('c', 'd', 11)
g.add_edge('c', 'f', 2)
g.add_edge('d', 'b', 15)
g.add_edge('d', 'c', 11)
g.add_edge('d', 'e', 6)
g.add_edge('e', 'd', 6)
g.add_edge('e', 'f', 9)
g.add_edge('f', 'a', 14)
g.add_edge('f', 'c', 2)
g.add_edge('f', 'e', 9)

def Dijkstra(Graph, start, target):
    Q = []                                  #미방문 꼭지점 집합 (queue)
    dist = {}                              #각 node 의 출발점으로부터의 거리
    prev = {}                             #현재 node 와 최단 경로로 연결된 이전 node

    for v in Graph.adjacentList.keys():      #graph 의 node 들을 모두 미방문 꼭지점으로 초기화
        dist[v] = float("inf")                       #vertex 들의 시작점으로부터의 거리를 모르므로 모두 inf 로 초기화
        prev[v] = None                             #아직 각 vertex 와 연결된 이전 최단 node 를 모르므로 None 으로 초기화
        Q.append(v)

    dist[start] = 0                                    #start node 의 출발점으로부터의 거리 = 0

    while len(Q) > 0:                               #Q 에 방문할 node 가 남아 있으면 True
        min = float("inf")
        for vertex in Q:                              #Q 에 남아있는 모든 node 들 방문
            if min > dist[vertex]:
                min = dist[vertex]                  #출발점으로부터의 거리가 가장 작다고 표시된 node 의 거리값을 min value 로 update
                u = vertex                             #방문한 node 로 표시

        Q.pop(Q.index(u))                         #방문한 node 중 출발점으로부터의 거리가 가장 작다고 결정된 node 를 Q 에서 제거

        for v in Graph.adjacentList[u]:
            alt  = dist[u] + v['weight']         #방문한 node 의 neighbor node 들의 거리 갱신
            if alt < dist[v['node']]:
                dist[v['node']] = alt              #새로운 최단 경로가 발견되면 최단 거리 갱신
                prev[v['node']] = u               #최적경로로 연결된 이전 node 갱신

    S = []                                              #최적 경로 출력을 위한 stack 생성
    t = target                                        #target 부터 역으로 최적 경로 생성을 위해 target 을 현재 node 로 초기화
    while prev[t] is not None:
        S.insert(0, t)                               #현재 node 를 stack 에 추가
        t = prev[t]                                  #최단경로 이전 node 를 현재 node 로 갱신

    S.insert(0, t)                                   # 마지막 현재 node stack 추가

    return (dist, prev, S)

dist, prev, shortest = Dijkstra(g, 'a', 'e')
print('Shortest Path = ' ,shortest)
