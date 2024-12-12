from routing_table import RoutingTable
N = 4
edges = []
edges.append((0, 1, 3))
edges.append((0, 3, 1))
edges.append((1, 2, 3))
edges.append((2, 3, 4))


def simulate_routing():
    routingTable = RoutingTable(edges, N)
    updated = True
    iteration = 0
    routingTable.display()
    while updated:
        print(f"\nIteration {iteration}:")
        updated = routingTable.update()
        routingTable.display()
        iteration += 1
    print("DONE!")


print("Starting simulation...")
simulate_routing()
