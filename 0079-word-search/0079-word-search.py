class Solution:
    def exist(self, board, word):
        rows = len(board)
        cols = len(board[0])
        
        def dfs(i, j, k):
            # If index is out of bounds or character doesn't match, return False
            if i < 0 or i >= rows or j < 0 or j >= cols or board[i][j] != word[k]:
                return False
            # If all characters are matched
            if k == len(word) - 1:
                return True
            
            temp = board[i][j]
            board[i][j] = '#'  # mark as visited
            
            # Explore in all 4 directions
            found = (
                dfs(i+1, j, k+1) or
                dfs(i-1, j, k+1) or
                dfs(i, j+1, k+1) or
                dfs(i, j-1, k+1)
            )
            
            board[i][j] = temp  # backtrack
            return found
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:  # possible starting point
                    if dfs(i, j, 0):
                        return True
        return False


        








board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
a = Solution()
print(a.exist(board,word))
        