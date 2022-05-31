class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        province = 0
        visited = []     
        def dfs(city):
            visited.append(city)
            
            for node in range(len(isConnected)):
                if isConnected[city][node] == 1 and node not in visited:
                    dfs(node)
                
        for city in range(len(isConnected)):
            for node in range(len(isConnected)):
                if city not in visited:
                    dfs(city)
                    province += 1
                               
        return province
