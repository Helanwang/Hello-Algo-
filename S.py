class Nodes:
    def __init__(self, data):
        self.data = data
        self.next = None


n1 = Nodes("data1")
n2 = Nodes("data2")
n3 = Nodes("data3")
n4 = Nodes("data4")

n1.next = n2
n2.next = n3
n3.next = n4

header = n1
while header:  # still have question about this part, come back later.
    print(header.data, end="->")
    header = header.next

print("null")
