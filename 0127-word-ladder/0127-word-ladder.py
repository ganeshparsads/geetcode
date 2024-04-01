class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        words = set(wordList)

        bfs = deque()
        bfs.append((beginWord, 1))
        visited = set()

        while bfs:
            curr_word, hops = bfs.popleft()

            if curr_word == endWord:
                return hops

            for idx, i in enumerate(curr_word):
                new_word = list(curr_word)
                skip_idx = 97 - ord(i)
                for ch in range(26):
                    if ch == skip_idx:
                        continue
                    new_word[idx] = chr(97 + ch)

                    newW = "".join(new_word)
                    
                    if newW in words and newW not in visited:
                        visited.add(newW)
                        bfs.append((newW, hops+1))

        return 0