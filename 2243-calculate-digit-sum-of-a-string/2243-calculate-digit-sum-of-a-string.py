class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            next_round = []
            # step through the string in chunks of size k 
            for i in range(0,len(s),k):
                chunk = s[i:i+k]
                chunk_sum = 0 
                #sum the chunk value for each character in the string 
                chunk_sum += sum(int(char) for char in chunk)
                next_round.append(str(chunk_sum))
            # Merge groups together for the next round
            s = "".join(next_round)
        
        return s 
        