class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        dict_a = [2,3,5,7,11,17,23,29,31,37,41,43,47,53,59,67,71,73,73,79,83,89,97,101,103,107,109]
        ransomPrd = 1
        for i in ransomNote:
            print(ord(i)-96)
            ransomPrd *= (dict_a[ord(i)-96])

        magazinePrd = 1
        for j in magazine:
            magazinePrd *= (dict_a[ord(j)-96])

        print(magazinePrd)
        print(ransomPrd)
        if magazinePrd % ransomPrd == 0:
            return True
        else:
            return False
