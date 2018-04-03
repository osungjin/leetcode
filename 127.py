import collections

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """

#        cw = beginWord
#        word_length = len(cw)
#        cnt = 0
#        while True:
#            if cw == endWord:
#                return cnt
#            else:
#                for idx, ww in enumerate(wordList):
#                    if len(set(cw) & set(ww)) == word_length - 1:
#                        cw = ww
#                        wordList.pop(idx)
#            if len(wordList) == 0:
#                return 0
        wordList = set(wordList)
        wordList.add(endWord)
        queue = collections.deque([[beginWord, 1]])
        while queue:
            word, length = queue.popleft()
            if word == endWord:
                return length
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    next_word = word[:i] + c + word[i+1:]
                    if next_word in wordList:
                        wordList.remove(next_word)
                        queue.append([next_word, length + 1])
        return 0


if __name__ == '__main__':
    s = Solution()
    print(s.ladderLength("hit", "cog", ["hot","dot","dog","lot","log"]))   
        
        
