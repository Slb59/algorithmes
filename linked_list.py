"""
    <==> from collections import deque
    Linked list of int:
    >> read in input a list of int and add to the list
    >> print the list
    > give the length of the list
    > join 2 lists
    > intersect 2 lists
    >> add at the beginning
    >> add at the end
    >> insert in a specifique position
    > search an element
    >> remove an element
    > copy a list
    > sort a list
    > reverse the list
"""


class Node:
    """
    _summary_
        a Node of anything
    """

    def __init__(self, data, next=None) -> None:
        self.data = data
        self.next = next

    def __repr__(self):
        return self.data
    
    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext

class UnorderedList:

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self,item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count

    def search(self,item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    def remove(self,item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
            
class LinkedList:
    """
    _summary_
        a linked list of anything
    """

    def __init__(self) -> None:
        self._head = None
        self._tail = None

    def __repr__(self):
        node = self._head
        nodes = []
        while node is not None:
            nodes.append(str(node.data))
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    def __iter__(self):
        node = self._head
        while node is not None:
            yield node
            node = node.next

    def remove(self, data) -> None:
        if self._head == None:
            raise Exception("List is empty")
        
        if self._head.data == data:
            self._head = self._head.next
            return

        before_node = self._head
        for node in self:
            if node.data == data:
                before_node.next = node.next
                return
        raise Exception("Data %s not found" % data)


    def addbefore(self, data, new_node: Node) -> None:
        if self._head == None:
            raise Exception("List is empty")
        
        if self._head.data == data:
            return self.addfirst_data(data)
        
        before_node = self._head
        for node in self:
            if node.data == data:
                new_node.next = node   
                before_node.next = new_node             
                return
            before_node = node

        raise Exception("Data %s not found" % data)

    def addafter(self, data, new_node: Node) -> None:
        if self._head == None:
            raise Exception("List is empty")

        for node in self:
            if node.data == data:
                new_node.next = node.next
                node.next = new_node
                return

        raise Exception("Data %s not found" % data)

    def addlist(self, data: list) -> None:
        """_summary_
            Add a list in the linked list with addfirst logic
        Args:
            data (list): _description_
        """
        for elem in data:
            self.addend_data(elem)

    def addfirst_data(self, data) -> None:
        new_node = Node(data, self._head)
        if self._head == None:
            self._tail = new_node
        self._head = new_node

    def print_linkedlist(self) -> None:
        current = self._head
        while current != None:
            print(f"{str(current.data)} ", end="")
            current = current.next
        print("")

    def addend_data(self, data) -> None:
        new_node = Node(data)
        if self._tail == None:
            self._head = new_node
            self._tail = self._head
        else:
            self._tail.next = new_node
            self._tail = new_node


def main():
    my_list = LinkedList()

    values = map(int, (input().split(" ")))  # for exemple a list of int

    my_list.addlist(values)

    my_list.print_linkedlist()

    print(my_list)

    new_node = Node(555)
    my_list.addbefore(84, new_node)
    print(my_list)

    # for elem in my_list:
    #     print(elem)


if __name__ == "__main__":
    main()
