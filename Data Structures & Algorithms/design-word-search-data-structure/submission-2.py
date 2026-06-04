class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.endOfWord = True

    def search(self, word: str) -> bool:
        def dfs(j, curr):   # idx, curr
            if j == len(word):
                return curr.endOfWord
            if word[j] == '.':
                for child in curr.children.values():
                    if dfs(j+1, child):
                        return True
                return False
            else:
                if word[j] not in curr.children:
                    return False
                return dfs(j+1, curr.children[word[j]]) 
        return dfs(0, self.root)
