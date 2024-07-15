class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

# size = 0 

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_beg(self, data):
        temp = Node(data, self.head)
        self.head = temp

    def insert_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        
        step = self.head
        while step.next:
            step = step.next

        step.next = Node(data, None)

    def insert_at(self, index, data):
        if index < 0 or index > self.get_lenght():
            raise Exception("Invalid Index [!]")
        
        if index == 0:
            self.insert_beg(data)
            return
        
        count = 0 
        step = self.head
        while step:
            if count == index-1:
                node = Node(data, step.next)
                step.next = node
                break

            step = step.next
            count += 1

    # Usign the tools above to create a linked list from a collection of data
    def inert_from_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_end(data)

    # Calculate the length
    def get_lenght(self):
        count = 0
        step = self.head
        while step:
            count += 1
            step = step.next
        # print("Lenght of the Linked-List is: ", count)
        return count

    # Remove Element at Index
    def remove_index(self, index):
        if index < 0 or index >= self.get_lenght():
            raise Exception("Invalid Index input [!]")
        
        if index == 0:
            self.head = self.head.next
            return
        
        count = 0
        step = self.head
        while step:
            if count == index - 1:
                step.next = step.next.next
                break
            step = step.next
            count += 1

    def insert_after_val(self, data_after, data):
        # Search for the first occurance of data_after 
        # Insert data after data_after
        
        step = self.head
        count = 0
        while step:
            if step.data == data_after:
                node = Node(data, step.next)
                step.next = node
                break

            if count >= self.get_lenght():
                raise Exception("[!] Data Not found in the list")
            
            step = step.next
            count += 1

    def remove_by_val(self, data):
        # Remove first node that contains the data
        if not self.head:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        
        step = self.head
        while step.next:
            if step.next.data == data:
                step.next = step.next.next
                return
            step = step.next    

    #Reversing the linked-list as iterative
    def rev_i(self):
        curr, prev = self.head, None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
    
    #Reversing the linked-list as recursive
    def rev_r(self):
        if not self.head:
            return None
        
        temp = self.head
        if self.head.next:
            temp = self.rev_r()
            self.head.next.next = self.head
        self.head.next = None

        return temp


    def print(self):
        if self.head is None:
            print("Empty head makes more noise")
            return
        
        start = self.head
        word = ''

        while start:
            word += str(start.data) + ' --> ' 
            start = start.next

        print('Head --> ' + word + ' End')
        self.print_index()

    def print_index(self):
        if self.head is None:
            print("Empty head makes more noise")
            return
        
        start = self.head
        word = ''
        count = 0

        while start:
            word += str(count) + ' --> ' 
            count += 1
            start = start.next

        print('Head --> ' + word + ' End')
            

if __name__ == '__main__':
    b = LinkedList()
    b.insert_beg(10)
    b.insert_beg(9)
    b.insert_beg(8)
    b.insert_beg(7)
    b.insert_end(11)
    b.insert_end(12)
    b.insert_end(13)
    b.print()
    print("Original length of the Linked-List is :",b.get_lenght(), "\n")

    # Removing value
    b.remove_index(5)
    b.print()
    print("Length of the Linked-List is :",b.get_lenght(), "\n")

    # Adding value
    b.insert_at(4, 30)
    b.insert_at(5, 300)
    b.insert_at(6, 3000)
    b.print()
    print("Length of the Linked-List is :",b.get_lenght(), "\n")

    # Insert after value
    b.insert_after_val(10, 21)
    b.print()
    print("Length of the Linked-List after insertion after data :",b.get_lenght(), "\n")

    # Remove at value
    b.remove_by_val(7)
    b.print()
    print("Length of the Linked-List after removing at given data :",b.get_lenght(), "\n")

    # Reversed list
    b.rev_i()
    b.print()

    # Converting a list to a linkedlist
    c = LinkedList()
    c.inert_from_values(["Student", "Fresher", " Junior Developer", "Senior Developer", "Senior Developer II", "Lead Developer", " Product Manager", "Chapter Head", "CEO", "Dead"])
    c.print()
