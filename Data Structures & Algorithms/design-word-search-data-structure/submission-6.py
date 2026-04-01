class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class WordDictionary:

    def __init__(self):
       self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isEnd = True


    def search(self, word: str) -> bool:
        def dfs(node, j):
            cur = node

            for i in range(j, len(word)):
                c = word[i]
                if c == '.':
                    for ch in cur.children.values():
                        if dfs(ch, i + 1):
                            return True
                    return False
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            return cur.isEnd
    
        return dfs(self.root, 0)
