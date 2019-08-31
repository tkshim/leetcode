#!/usr/bin/env python
#coding: utf-8

m_map = {"a":".-","b":"-...","c":"-.-.","d":"-..","e":".","f":"..-.","g":"--.","h":"....","i":"..","j":".---","k":"-.-","l":".-..","m":"--","n":"-.","o":"---","p":".--.","q":"--.-","r":".-.","s":"...","t":"-","u":"..-","v":"...-","w":".--","x":"-..-","y":"-.--","z":"--.."}

def changeMorse(message):
    newMessage =""
    for i in message:
        newMessage += m_map[i]
    return newMessage

print changeMorse("xy")
print m_map["a"]

#https://leetcode.com/problems/unique-morse-code-words/
