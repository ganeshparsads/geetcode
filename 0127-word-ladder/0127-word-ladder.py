class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        deq = collections.deque()
        bank = set(wordList)
        deq.append(beginWord)
        count = 0
        n = len(beginWord)
        while deq:
            for _ in range(len(deq)):
                cur_word = deq.popleft()
                if cur_word == endWord:
                    return count + 1
                for i in range(n):
                    for ch in [chr(ord('a') + i) for i in range(26)]:
                        new_word = f'{cur_word[:i]}{ch}{cur_word[i + 1:]}'
                        if new_word in bank:
                            deq.append(new_word)
                            bank.discard(new_word)
            count += 1
        return 0