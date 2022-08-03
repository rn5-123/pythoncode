import time
start=time.time()
class Stack:
    def __init__(self):
        self.items=[]
        def isEmpty(self):
            return self.items==[]
        def push(self,item):
            self.items.append(item)
            print(item)
            def pop(self):
                return self.item.pop()
            def peek(self):
                  return self.items[len(self.items)-1]
            def size(self):
                  return len(self.items)
                s=Stack()
                print(s.isEmpty(),"-because stack is empty")
                print("element are pushed into stack for operation")
                s.push(11)
                s.push(12)
                s.push(13)
                print("size",s.size())
                print("Peek",s.peek())
                print("pop operation")
                print(s.pop())
                print(s.pop())
                print("Size",s.size())
                print(40*"*")
                class Queue:
                    def__init__(self):
                        self.items=[]
                        def is Empty(self):
                            return self.items==[]
                        def enqueue(self,items):
                            self.items.append(item)
                            print(item)
                            def front(self):
                                return self.items[len(self.items)-1]
                            def size(self):
                                return len(self.items)
                            q=Queue()
                            print(q.isEmpty(),"-because queue is empty")
                            print("Enquee")
                            q.enqueue(11)
                            q.enqueue(12)
                            q.enqueue(13)
                            print("Front",q.front())
                            print("Dequee")
                            print(q.dequeue() )
                            print(q.dequeue())
                            print("Size",q.size())
                            end=time.time()
                            print(f"Runtime of the program is {end - start}")
                            
