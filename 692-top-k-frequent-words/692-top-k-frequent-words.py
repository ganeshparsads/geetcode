# Build a class, that stores word, it's frequency.
# Overwrite compare functions, to prioritize words on frequency, alphabetical order.
class Word_Rank:
	def __init__(self, word, frequency):
		self.word = word # string
		self.frequency = frequency  # int

	# Overrides the == operator. eq = equal
	def __eq__(self, other):
		return self.frequency == other.frequency and self.word == other.word

	# Overrides the != operator. ne = not equal
	def __ne__(self, other):
		return self.word != other.word or self.frequency != other.frequency
			
	# Overrides the < operator. lt = less than
	def __lt__(self, other):
		if self.frequency < other.frequency:
			return True
		elif self.frequency > other.frequency:
			return False
		elif self.word > other.word:
			return True
		else:
			return False

	# Overrides the <= operator. le = less than or equal
	def __le__(self, other):
		return self.__lt__(other) or self.__eq__(other)

	# Overrides the > operator. gt = greater than
	def __gt__(self, other):
		if self.frequency > other.frequency:
			return True
		elif self.frequency < other.frequency:
			return False
		elif self.word < other.word:
			return True
		else:
			return False

	# Overrides the >= operator. gt = greater than or equal
	def __ge__(self, other):
		return self.__gt__(other) or self.__eq__(other)


class Solution:
	def topKFrequent(self, words: List[str], k: int) -> List[str]:
		import heapq
		
		# 1. Build frequency-map. O(N)
		frequency_count = {}
		for i in words:
			if i in frequency_count:
				frequency_count[i] += 1
			else:
				frequency_count[i] = 1
		
		# 2. Build list of word-rank objects. O(N)
		words = [Word_Rank(i, frequency_count[i]) for i in frequency_count.keys()]
		
		# 3. Build heap (min-heap in python) O(nlogk)
		pq = []  # Initialize min-heap
		for i in words:
			# Add to heap if heap size less than k, or if word has higher priority than min element in current heap.
			if len(pq) < k or (len(pq) >= k and i > pq[0]):
				heapq.heappush(pq, i)
			
			if len(pq) > k:
				heapq.heappop(pq)
		
		# 4. Our PQ now contains the k top words based on:
			# a. Frequency of occurence
			# b. Alphabetical ordering
		# Build a list of k words sorted in ascending order of priority. O(N)
		answer = []
		while pq:
			# heappop() pops the least priority object in heap first.
			answer.append(heapq.heappop(pq).word)

		print(answer)
		
		# 5. Return the answer list in reverse order.
		return answer[::-1]

