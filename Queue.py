
class Queue:
    def __init__(self, ):
	    self.client = []
	
    def isEmpty(self):
	    return self.items == []
	
    def enqueue(self, client):
	    self.client.insert(0,client)
	
    def dequeue(self):
	    return self.client.pop()
	
    def size(self):
	    return len(self.items)