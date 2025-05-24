
class Solution(object):
    def findWordsContaining(self, words, x):
        """
        :type words: List[str]
        :type x: str
        :rtype: List[int]
        """
        answerStorage = []
        for s in range(0, len(words)):
            if x in words[s]:
                answerStorage.append(s)
                
        return answerStorage
                
                
