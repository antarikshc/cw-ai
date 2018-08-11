from collections import deque

class Node:
    def __init__(self, state, parent = None, action = None):
        self.state = state
        self.parent = parent
        self.action = action

    def __repr__(self):
        return "<Node {})>".format(self.state)

    def expand(self, problem):
        return [self.child_node(problem, action)
        for action in problem.actions(self.state)]

    def child_node(self, problem, action):
        next_state = problem.result(self.state, action)
        next_node = Node(next_state, self, action)
        return next_node

class Graph:
    def __init__(self, graph_dict = None, directed = True):
        self.graph_dict = graph_dict or {}
        self.directed = directed
        if not directed:
            self.make_undirected()

    def make_undirected(self):
        for a in list(self.graph_dict.keys()):
            for (b, dist) in self.graph_dict[a].items():
                self.connect_more(b, a, dist)

    def connect(self, A, B, distance = 1):
        self.connect_more(A, B, distance)
        if not self.directed:
            self.connect(B, A, distance)

    def connect_more(self, A, B, distance):
        self.graph_dict.setdefault(A, {}) [B] = distance

    def get(self, a, b = None):
        links = self.graph_dict.setdefault(a, {})
        if b is None:
            return links
        else:
            return links.get(b)

def UndirectedGraph(graph_dict = None):
    return Graph(graph_dict = graph_dict, directed = False)

class Problem(object):
    def __init__(self, initial, goal = None):
        self.initial = initial
        self.goal = goal

    def goal_test(self, state):
        if isinstance(self.goal, list):
            return is_in(state, self.goal)
        else:
            return state == self.goal

class GraphProblem(Problem):
    def __init__(self, initial, goal, graph):
        Problem.__init__(self, initial, goal)
        self.graph = graph

    def actions(self, A):
        return list(self.graph.get(A).keys())

    def result(self, state, action):
        return action

def breadth_first_tree_search(problem):
    frontier = deque([Node(problem.initial)])
    print("Starting from: ", frontier)
    while frontier:
        node = frontier.popleft()
        print("Going to: ", node)
        if problem.goal_test(node.state):
            return node
        frontier.extend(node.expand(problem))
        
    return None


romania_map = UndirectedGraph(dict(
    Arad = dict(Zerind = 75, Sibiu = 140, Timisoara = 118),
    Bucharest = dict(Urziceni = 85, Pitseti = 101, Giurgiu = 90, Fagaras = 211),
    Craiova = dict(Drobeta = 120, Rimnicu = 146, Pitesti = 138),
    Drobeta = dict(Mehadia = 75),
    Eforie = dict(Hirsova = 86),
    Fagaras = dict(Sibiu = 99),
    Hirsova = dict(Urziceni = 98),
    Iasi = dict(Vaslui = 92, Neamt = 87),
    Lugoj = dict(Timisoara = 111, Mehadia = 70),
    Ordea = dict(Zerind = 71, Sibiu = 151),
    Pitesti = dict(Rimnicu = 97),
    Rimnicu = dict(Sibiu = 80),
    Urziceni = dict(Vaslui = 142)
))

romania_problem = GraphProblem('Arad', 'Bucharest', romania_map)
print(breadth_first_tree_search(romania_problem))

