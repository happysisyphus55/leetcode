class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid),len(grid[0])

        # count the servers in each row and column 
        row_counts = [0] * rows
        col_counts = [0] * cols 

        # first pass: count the servers in each row and column 
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    row_counts[i] += 1
                    col_counts[j] += 1
        
        # second pass: count the servers that can communicate 
        # a server can communicate if there is at least one other server in the same row or column 
        connected_servers = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (row_counts[i] > 1 or col_counts[j] > 1):
                    connected_servers += 1
        return connected_servers 