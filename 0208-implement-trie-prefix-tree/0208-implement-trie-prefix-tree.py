class TrieNode:
    def __init__(self):
        #Stores next letters
        self.children = {}
        #tells if a word ends here(For "cat", t node will have endOfWord = True)
        self.endOfWord = False

class Trie:
    def __init__(self):
        #root → starting point of the tree
        self.root = TrieNode()

    #Function to insert a word into the Trie.
    def insert(self, word: str) -> None:
        #Start from the root node.
        cur = self.root
        #Loop through each character in the word.
        for c in word:
            #Check if the character path does not exist.
            if c not in cur.children:
                #Create a new node for that character.
                cur.children[c] = TrieNode()
            #Move to the next node.
            cur = cur.children[c]
        #Mark the end of the word.
        cur.endOfWord = True
    #Function to check if a word exists.
    def search(self, word: str) -> bool:
        #Start from the root node.
        cur = self.root
        #Loop through each character.
        for c in word:
            #If character not found, word doesn’t exist.
            if c not in cur.children:
                #Return False immediately.
                return False
            #Move to the next node.
            cur = cur.children[c]
        #Return True only if it's a complete word.
        return cur.endOfWord
        
    #Function to check if any word starts with given prefix.
    def startsWith(self, prefix: str) -> bool:
        #Start from the root node.
        cur = self.root
        #Loop through each character of prefix
        for c in prefix:
            #If character not found, prefix doesn’t exist.
            if c not in cur.children:
                #Return False immediately.
                return False
            #Move to the next node.
            cur = cur.children[c]
        #Return True if all prefix characters exist.
        return True
        

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)