#Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = ListNode() #Defining a new ListNode that stores the results of the sum
        currentResult = result #It's the pointer that moves through each node of the result
        currentL1 = l1 #pointer that moves through each node of l1
        currentL2 = l2 #pointer that moves through each node of l2
        while(currentL1 != None or currentL2 != None): #Checks if at least one node has a value stored
            if(currentL1 == None): #Checks if L1 reached to the end before L2
                currentResult.val += currentL2.val #Only adds L2 value to the node
                currentL2 = currentL2.next #Only moves to the next node of L2
            elif(currentL2 == None): #Checks if L2 reached to the end before L1
                currentResult.val += currentL1.val #Only adds L1 value to the node
                currentL1 = currentL1.next #Only moves to the next node of L1
            else: #Both L1 and L2 have not reached to their end
                currentResult.val += currentL2.val + currentL1.val #Adds both values L1 and L2 to the node of result
                #Moves to the next nodes of L1 and L2
                currentL2 = currentL2.next 
                currentL1 = currentL1.next
            if currentResult.val // 10 != 0: #Checks if the node of the result contains two digits instead of one
                currentResult.next = ListNode() #Initializes the next node of result
                #Sets the value of the next node to the tens digit of the current node
                currentResult.next.val = currentResult.val // 10 
                currentResult.val %= 10 #Sets the current value to the units of the current node
            #Checks if the nodes L1 or L2 have not reached the end
            if currentL1 != None or currentL2 != None:
                #Checks if the next node of result has not been initialized yet
                if currentResult.next == None:
                    #initializes the next node
                    currentResult.next = ListNode()
                #moves to the next node
                currentResult = currentResult.next
        #Finally, it returns the result
        return result