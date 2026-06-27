class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
    #Function to insert a word
    def addWord(self, word: str) -> None:
        #Start from the root
        cur = self.root
        #Go through each letter.
        for c in word:
            #Create a node if letter doesn’t exist.
            if c not in cur.children:
                cur.children[c] = TrieNode()
            #Move to next node.
            cur = cur.children[c]
        #Mark end of word.
        cur.word = True
        
    #Function to search a word
    def search(self, word: str) -> bool:
        #Recursive function to explore all possibilities.j → current index in word,root → current Trie node
        def dfs(j, root):
            #Start from given node.
            cur = root
            #Loop through remaining letters.
            for i in range(j, len(word)):
                c = word[i]
                #"." means any letter is allowed
                if c == ".":
                    #Try all possible branches.
                    for child in cur.children.values():
                        #If any path works → return True.
                        if dfs(i + 1, child):
                            return True
                    #If none work → return False.
                    return False
                #If letter not found → word doesn’t exist.
                else:
                    if c not in cur.children:
                        return False
                    #Move forward.
                    cur = cur.children[c]
            #Return True only if it's a complete word.
            return cur.word
        #Start DFS from index 0 and root.
        return dfs(0, self.root)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)