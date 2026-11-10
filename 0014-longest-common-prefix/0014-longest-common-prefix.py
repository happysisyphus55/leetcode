class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    # insert a word into the trie 
    def insert(self,word):
        current = self.root 
        for char in word:
            # if the current char path doesnt exist, create a new node
            if char not in current.children:
                current.children[char] = TrieNode()
            
            # move to the child node 
            current = current.children[char]
        # mark the end of the word
        current.is_end_of_word = True
    
    def longest_common_prefix(self) -> str:
        # find and return the longest common prefix among all inserted 
        prefix = []
        current = self.root

        # traverse down the tree while there is a unique path
        while len(current.children) == 1 and not current.is_end_of_word:
            # get the only character at this level
            char = list(current.children.keys())[0]
            prefix.append(char)
        
            # move to that single child node
            current = current.children[char]
        
        return "".join(prefix)


class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        # two pointer approach, just start move the pointers start from each string 
        trie = Trie()
        for string in strs:
            trie.insert(string)
        
        return trie.longest_common_prefix()


        