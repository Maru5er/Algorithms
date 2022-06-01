class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return
        
        queue = collections.deque()
        
        queue.append(root)
        
        while queue:
            cur = queue.popleft()
            left, right = None, None
            if cur.left:
                left = cur.left
                queue.append(left)
            if cur.right:
                right = cur.right
                if left:
                    left.next = right
                #left.next = right if left else None
                queue.append(right)
                

                #right.next = cur.next.left
                while cur.next:
                    if cur.next.left:
                        right.next = cur.next.left
                        break

                    elif cur.next.right:
                        right.next = cur.next.right
                        break
                        
                    else:
                        cur = cur.next
                        
                        
            elif left:
                while cur.next:
                    if cur.next:
                        if cur.next.left:
                            left.next = cur.next.left
                            break

                        elif cur.next.right:
                            left.next = cur.next.right
                            break
                            
                        else:
                            cur = cur.next

                        
        return root
