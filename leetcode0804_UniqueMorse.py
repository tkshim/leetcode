#!/usr/bin/env python
#coding: utf-8
import collections

class Solution(object):
    m_map = {"a":".-","b":"-...","c":"-.-.","d":"-..","e":".","f":"..-.","g":"--.","h":"....","i":"..","j":".---","k":"-.-","l":".-..","m":"--","n":"-.","o":"---","p":".--.","q":"--.-","r":".-.","s":"...","t":"-","u":"..-","v":"...-","w":".--","x":"-..-","y":"-.--","z":"--.."}
    inputLists=[]
    def changeMorse(self, message):
        newMessage =""
        for i in message:
            newMessage += self.m_map[i]
        return newMessage

    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        if len(words) == 0:
            return 0
        for i in words:
            self.inputLists.append(self.changeMorse(i))
        c = collections.Counter(self.inputLists)
        return len(c)

#inputWords = ["gin", "zen", "gig", "msg"]
#inputWords = ["aaa", "aaa", "bbb", "ccc", "ddd", "ddd"]
inputWords = []

instance001 = Solution()
print instance001.uniqueMorseRepresentations(inputWords)




#https://leetcode.com/problems/unique-morse-code-words/
