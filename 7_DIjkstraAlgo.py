import math

#-----1.Data-----

# graph{} : stores nodes and edge weights
graph = {
    "start": {"a": 6, "b": 2},
    "a":     {"fin": 1},
    "b":     {"a": 3, "fin": 5},
    "fin":   {}
}

infinity = math.inf

# costs{} : shortest distance from start to each node
#renewable
costs = {
    "a": 6,
    "b": 2,
    "fin": infinity
}

# parents{} : tracks which node we came from
#renewable
parents = {
    "a": "start",
    "b": "start",
    "fin": None
}

# Processed[] : nodes already visited
processed = []

def find_lowest_cost_node(costs):
    lowest_cost = math.inf
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

node = find_lowest_cost_node(costs)

#Main_Loop #Most important & Difficult
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)

print(f"Shortest distance: {costs['fin']}")