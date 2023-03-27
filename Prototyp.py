#!/usr/bin/env python
# coding: utf-8

# In[3]:


#build
from textblob import TextBlob
import nltk as nltk

#Methoden
def tokenization(sentence):
        tokens = nltk.word_tokenize(sentence)
        tagged = nltk.pos_tag(tokens)
        print(tagged)
        return tokens

def ssplit(sentence):
    return ""

def pos(sentence):
    return sentence.tags

def lemma(sentence):
    words = []
    for word in sentence:
        words.append(word.lemmatize())
    return words

def stemming(words):
    return ""

#input
file = open('input.txt','r')
text = file.read()
print(text)

#split lines and sentences
sentences = nltk.sent_tokenize(text)
print(sentences)

#main

print("Tokenization:")
tokenization(text)
print("\n")

#refrence
wiki = TextBlob("Python is a high-level, general-purpose programming language.")
print(wiki.tags)
print(wiki.noun_phrases)


#clean up
file.close()

