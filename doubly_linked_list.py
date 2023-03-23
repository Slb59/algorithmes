class Node :
    
    def __init__ ( self, data, prev=None, next=None):
        self. data = data
        self._prevnode = prev
        self._nextnode = next

    def __repr__(self):
        return self.data
    
class DLinkedList:

    def __init__(self) -> None:
        self._head = None
        self._tail = None

    def __repr__(self):
        node = self._head
        nodes = []
        while node is not None:
            nodes.append(str(node.data))
            node = node._nextnode
        return " <-> ".join(nodes)
    
    def __iter__(self):
        node = self._head
        while node is not None:
            yield node
            node = node._nextnode

    def print_forward(self):
        node = self._head
        nodes = []
        while node is not None:
            nodes.append(str(node.data))
            node = node._nextnode
        nodes.append('End')    
        print(" -> ".join(nodes))

    def print_backward(self):
        node = self._tail
        nodes = []
        while node is not None:
            nodes.append(str(node.data))
            node = node._prevnode
        nodes.append('Start')    
        print(" -> ".join(nodes))

    def addlist(self, data: list) -> None:
        for elem in data:
            self.addfirst_data(elem)
    
    def addfirst_data(self, data) -> None:
        new_node = Node(data, None, self._head)
        if self._head == None:
            self._tail = new_node
        else:    
            self._head._prevnode = new_node    
        self._head = new_node

    def addend_data(self, data) -> None:
        new_node = Node(data)
        if self._tail == None:
            self._head = new_node
            self._tail = self._head
        else:
            self._tail._nextnode = new_node
            new_node._prevnode = self._tail
            self._tail = new_node

    def addafter(self, data, new_node: Node) -> None:
        if self._head == None:
            raise Exception("List is empty")

        for node in self:
            if node.data == data:
                new_node._nextnode = node._nextnode
                new_node._prevnode = node
                node._nextnode._prevnode = new_node
                node._nextnode = new_node                
                return

        raise Exception("Data %s not found" % data)
    
    def remove(self, data) -> None:
        if self._head == None:
            raise Exception("List is empty")
        
        if self._head.data == data:
            self._head._nextnode._prevnode = None
            self._head = self._head._nextnode            
            return
        
        if self._tail.data == data:
            self._tail._prevnode._nextnode = None
            self._tail = self._tail._prevnode            
            return

        for node in self:
            if node.data == data:
                node._prevnode._nextnode = node._nextnode
                node._nextnode._prevnode = node._prevnode
                return
            
        raise Exception("Data %s not found" % data)

def main():
    tab = [10, 100, 50, 98, 1, 14]
    dll = DLinkedList()
    dll.addlist(tab)
    print(dll)
    dll.print_backward()
    dll.addend_data(555)
    print(dll)
    dll.addafter(50,Node(25))
    print(dll)
    dll.print_forward()
    dll.print_backward()
    dll.remove(14)
    dll.print_forward()
    dll.print_backward()
    dll.remove(555)
    dll.print_forward()
    dll.print_backward()
    dll.remove(50)
    dll.print_forward()
    dll.print_backward()

if __name__ == "__main__":
    main()