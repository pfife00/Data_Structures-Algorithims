# -*- coding: utf-8 -*-

#Linked List implementation

#first define Node class
class Node(object):
    
    #constructor
    def __init__(self, data = None, next_node = None):
        self.data = data
        self.next_node = next_node
        
    #method to return current node
    def get_data(self):
        return self.data
    
    #method to return next node
    def get_next(self):
        return self.next_node
    
    #reset pointer to next node
    def set_next(self, new_next):
        self.new_next = new_next
        

#Linked List implementation
class LinkedList(object):
    
    #constructor
    def __init__(self, head = None):
        self.head = head
        
    #insert new head method
    def insert(self, data):
        #create new node
        new_node = Node(data)
        
        #use set_next method to point new node to old head
        new_node.set_next(self.head)
        
        #set new head
        self.head = new_node
        
    #size method which counts nodes until no more nodes (O(n) time complexity)
    def size(self):
        
        #start at the head node
        current = self.head
        
        #initialize counter
        count = 0
        
        #loop through nodes until None is reached
        while current:
            #increment counter
            count += 1
            #set current to next node using get_next method
            current = current.get_next()
            
    
    #search method, checks each node for requested data. If found, returns
    #node holding the data
    #(O(n) time complexity)
    def search(self, data):
        #set value to head
        current = self.head
        
        #initialize value to check if value found in list or not
        found = False
        
        #loop until value found
        while current and found is False:
            
            #if value found, set found to True
            if current.get_data() == data:
                found = True
                
            else:
                current = current.get_next()
                
        #if value not found in list, raise exception error
        if current is None:
            raise ValueError("value not in list")
            
        return current
            
    #delete method, traverses list and when finds target node to be deleted, 
    #changes previous node pointer to point to next node, bypassing the target
    #node
    def delete(self, data):
        #set value to head
        current = self.head
        
        #initialize values to store previous and whether target node was found
        previous = None
        found = False
        
        #loop until find target node
        while current and found is False:
            #if find the target node, set found to be True
            if current.get_data() == data:
                found = True
                
            #otherwise, set the previous value to current and move current to 
            #next node
            else:
                previous = current
                current = current.get_next()
                
        #if the target node not found, raise error
        if current is None:
            raise ValueError("value not found in list")
            
        if previous is None:
            self.head = current.get_next()
            
        else:
            previous.set_next(current.get_next())



