class Solution:
  #solution uses Floyd's cycle finding algorithm to detect a cycle... ends main while loop if a cycle is found
    def isHappy(self, n: int) -> bool:
        def getNext(number):
            totalsum = 0
            while number > 0:
                number, x = divmod(number, 10)
                totalsum += x ** 2
                
            return totalsum
        
        slow = n
        fast = getNext(n)
        
        #main loop
        while fast != 1 and slow != fast:
            slow = getNext(slow)
            fast = getNext(getNext(fast))
            
        return fast == 1
