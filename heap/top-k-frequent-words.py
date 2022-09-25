class WordRank:
	def __init__(self, word, freq):
		self.word = word
		self.freq = freq

	# override equals
	def __eq__(self, next):
		return self.word == next.word and self.freq == next.freq

	# override less than
	def __lt__(self, next):
		if self.freq < next.freq:
			


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        pass