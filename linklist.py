"""Find the middle item in a singly linked list, or two middle items if it contains an even number of nodes."""
# A single node of a singly linked list
class Node:
  # constructor
  # variable table
  def __init__(self, data = None, next=None): 
    self.data = data               # data = 5
    self.next = next               # next = None

class Node:  
  
    # Function to initialise the node object  
    # variable table
   
    def __init__(self, data):  
        self.data = data            # data = 5                           
        self.next = None            # next = None
  
class LinkedList: 
    # variable table
                         
    def __init__(self): 
        self.head = None            # head=None
    
    def push(self, new_data):       # new_data=5
        new_node = Node(new_data)   # new_node=Node(5)
        new_node.next = self.head   #new_node = None
        self.head = new_node        #self.head= Node(5)
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        slow_ptr = self.head        # slow_ptr = Node(5)
        fast_ptr = self.head        # fast_ptr = Node(5)
  
        if self.head is not None: 
            while (fast_ptr is not None and fast_ptr.next is not None): # fast_ptr != None 
                fast_ptr = fast_ptr.next.next   # fast_ptr = 2 next interation fast_ptr=1
                slow_ptr = slow_ptr.next        # slow_ptr = 4 next interation slow_ptr=2
            print("The middle element is: ", slow_ptr.data) 
  
# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(3) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 
