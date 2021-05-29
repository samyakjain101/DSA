class TrieNode:
    def __init__(self):
        self.child = dict()
        self.end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, string: str):
        p = self.root
        for char in string:
            if char in p.child:
                p = p.child[char]
            else:
                p.child[char] = TrieNode()
                p = p.child[char]
        p.end = True

    def has_word(self, word: str):
        p = self.root
        for char in word:
            if char in p.child:
                p = p.child[char]
            else:
                return False

        if p.end:
            return True
        return False

    def has_prefix(self, prefix: str):
        p = self.root
        for char in prefix:
            if char in p.child:
                p = p.child[char]
            else:
                return False

        return True


if __name__ == "__main__":
    t = Trie()
    t.insert("hello")
    t.insert("data")
    t.insert("algebra")
    print(t.has_word("data"))
    print(t.has_prefix("al"))
