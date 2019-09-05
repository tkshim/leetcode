#!/usr/bin/env python
#coding: utf-8
m_map = {"a":".-","b":"-...","c":"-.-.","d":"-..","e":".","f":"..-.","g":"--.","h":"....","i":"..","j":".---","k":"-.-","l":".-..","m":"--","n":"-.","o":"---","p":".--.","q":"--.-","r":".-.","s":"...","t":"-","u":"..-","v":"...-","w":".--","x":"-..-","y":"-.--","z":"--.."}

MORSE = [".-","-...","-.-.","-..",".","..-.","--.",
                 "....","..",".---","-.-",".-..","--","-.",
                 "---",".--.","--.-",".-.","...","-","..-",
                 "...-",".--","-..-","-.--","--.."]

words = ["gin", "zen", "gig", "msg"]

# setのlen()は重複しないCountを返す
seen = set(words)
print seen, len(seen)

# joinでリストを１文字に連結
# {}でset型に変更できる
s = {''.join(words)}
print s
print type(s), len(s)

# 以下は、文字列をモールス信号に変更
w  = "gin"
newMessage=""
for i in w:
    newMessage += m_map[i]
print newMessage

#seen = {"".join(MORSE[ord(c) - ord('a')] for c in word) for word in words}
