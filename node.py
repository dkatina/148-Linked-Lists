

class Node():

    def __init__(self, data):
        self.data = data
        self.next = None

day1 = Node("Monday")
day2 = Node("Tuesday")
day3 = Node("Wednesday")

day1.next = day2
day2.next = day3

print(day1.next.next.data)


#traverse

print("Traverse")
current = day1
while current:
    print(current.data)
    current = current.next