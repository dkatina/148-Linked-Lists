

class Node():

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None #Doubly Linked Nodes need a previous attribute

class Stack():

    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):

        new_node = Node(data) #creating new node with data passed in

        if self.head == None: #Checking if our list is empty
            self.head = new_node #if so this new node becomes our head
            self.tail = new_node #also becomes tail as it is the last thing in the list
        else:
            self.tail.next = new_node #New-node comes next after current tail
            new_node.prev = self.tail # the current tail is now the prev node of our new_node
            self.tail = new_node #assign title of Tail to new_node (at the end)

    def traverse(self, reverse=False):

        print("TRAVERSING")
        print("~~~~~~~~~~~")
        if not reverse:

            current = self.head
            while current:
                print(current.data)
                current = current.next
        else:
            current = self.tail
            while current:
                print(current.data)
                current = current.prev

    def pop(self):

        if self.tail == None:
            return "Cannot pop from empty list"
        
        popped = self.tail
        self.tail = popped.prev
        self.tail.next = None

        return popped.data
    
    def insert(self, idx, data):
        print("ADDING", data, "To the List")
        new_node = Node(data)
        current = self.head
        count = 1

        while count < idx:
            current = current.next
            count += 1

        new_node.next = current.next
        new_node.prev = current 
        current.next = new_node
        new_node.next.prev = new_node
        



    

shows = Stack()

shows.append("The Boys")
shows.append("Atlanta")
shows.append("Severence")
shows.append("The Good Doctor")
shows.append("Rick and Morty")
shows.append("House of Dragon")
shows.append("Boardwalk Empire")
shows.append("Scrubs")

shows.traverse()

watching = shows.pop()

print("WATCHING:", watching)

shows.traverse()

shows.insert(3, "The Office")

shows.traverse()




