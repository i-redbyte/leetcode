class WordDictionary:
    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        current = self.trie
        for w in word:
            if w not in current:
                current[w] = {}
            current = current[w]
        current["#"] = {}

    def search(self, word) -> bool:
        def find(search_word, trie):
            if not search_word:
                return "#" in trie
            if search_word[0] == ".":
                return any(find(search_word[1:], v) for v in trie.values())
            if search_word[0] not in trie:
                return False
            return find(search_word[1:], trie[search_word[0]])

        return find(word, self.trie)


wd = WordDictionary()
wd.addWord("Lenin")
wd.addWord("Assembler")
wd.addWord("C++")
wd.addWord("Kotlin")
print(wd.search("Stalin"))
print(wd.search("C++"))
print(wd.search("C.+"))
print(wd.search("Kot.."))
print(wd.search("Kot..n"))
