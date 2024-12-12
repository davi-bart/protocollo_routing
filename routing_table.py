class RoutingTable:
    def __init__(self, edges, n):
        # initialize the routing table from the given edges
        self.tables = []
        self.edges = edges
        self.adj_list = [[] for _ in range(n)]
        for start in range(n):
            table = []
            for _ in range(n):
                table.append((float('inf'), None))
            table[start] = (0, start)
            self.tables.append(table)
        for (s, e, cost) in edges:
            self.tables[s][e] = (cost, e)
            self.tables[e][s] = (cost, s)
            self.adj_list[s].append((e, cost))
            self.adj_list[e].append((s, cost))

    def update_table(self, node_id):
        # update the routing table for the given node
        updated = False
        for dest in range(len(self.tables)):
            if dest == node_id:
                continue
            dist, next = self.tables[node_id][dest]
            for (neighbor, cost) in self.adj_list[node_id]:
                if neighbor == node_id:
                    continue
                dist1 = cost + self.tables[neighbor][dest][0]
                if dist1 < dist:
                    dist = dist1
                    next = neighbor
                    updated = True
            self.tables[node_id][dest] = (dist, next)
        return updated

    def update(self):
        # update all the routing tables
        updated = False
        for node in range(len(self.tables)):
            if self.update_table(node):
                updated = True
        return updated

    def display(self):
        # display the routing tables
        print("."*20)
        for i, table in enumerate(self.tables):
            print(f"Node {i} Routing Table: {table}")
        print("."*20)
        print()

    def lookup(self, destination):
        return self.table.get(destination)
