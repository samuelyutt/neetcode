class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        nodes = []
        record = {} # email -> idx

        for i, acc in enumerate(accounts):
            name, emails = acc[0], acc[1:]
            node = Node(name, emails)
            nodes.append(node)

            for email in emails:
                if email in record:
                    neighbor = nodes[record[email]]
                    neighbor.neighbors.add(node)
                    node.neighbors.add(neighbor)
                else:
                    record[email] = i

        ret = []
        for i in range(len(nodes)):
            if nodes[i].used:
                continue

            emails = set()
            group = [nodes[i]]
            while group:
                node = group.pop()
                if node.used:
                    continue
                emails.update(node.emails)
                node.used = True
                for nei in node.neighbors:
                    group.append(nei)
            emails = list(emails)
            emails.sort()
            ret.append([nodes[i].name] + emails)

        return ret



class Node:
    def __init__(self, name, emails):
        self.name = name
        self.emails = emails
        self.neighbors = set()
        self.used = False