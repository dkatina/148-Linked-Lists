

class Node():

    def __init__(self, data):
        self.data = data
        self.next = None


class SongQueue():

    def __init__(self):
        self.head = None
        self.tail = None

    
    def enqueue(self, data):

        new_song = Node(data)
        if self.head == None:
            self.head = new_song
            self.tail = new_song
        else:
            self.tail.next = new_song
            self.tail = new_song


    def traverse(self):
        print("TRAVERSING")
        print("~~~~~~~~~~~")
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def dequeue(self):
        if self.head == None:
            return "Can't dequeue from an empty list"
        else:
            removed = self.head
            self.head = self.head.next
            return removed.data


class_queue = SongQueue()

class_queue.enqueue("I Surrender")
class_queue.enqueue("By Fire")
class_queue.enqueue("Lip Gloss and Black")
class_queue.enqueue("Sci-fi")
class_queue.enqueue("The Fall")
class_queue.enqueue("Break Even")

class_queue.traverse()

playing_song = class_queue.dequeue()

print("PLAYING:", playing_song)

class_queue.traverse()


