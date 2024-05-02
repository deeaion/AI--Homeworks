import random

import numpy as np


def read_file(path):
    data=[]
    with open(path) as f:
        lines = f.readlines()
        return [line.strip('\n') for line in lines]


separators = ['.', '!', '?']

import re

from nltk.tokenize import word_tokenize
def normalizeText(text, include_punctuation=False):
    cleaned = []
    for line in text:
        line = line.lower()

        # Optionally, use regex to ensure punctuation is separated from words
        line = re.sub(r'([,.!?"])', r' \1 ', line)  # Add space around specific punctuation marks

        # Tokenize the line
        tokens = word_tokenize(line)

        # Optionally filter to remove any unwanted characters (kept simple here)
        words = [token for token in tokens if token.isalpha() or token in [".", ",", "!", "?", '"']]

        # Append tokens to the cleaned list
        cleaned.extend(words)
    return cleaned


def train_markov_chain_one_State(sentences):
    words = []
    for sentence in sentences:
        for word in sentence.split():
            if word[-1] in separators:
                separator = word[-1]
                word_sep = word.split(separator)[0]
                words.append(word_sep)
                words.append(separator)
            else:
                words.append(word)
    words = set(words)
    words = list(words)
    # print(words)
    return words
def generate_sentence_one_state(words,length):
    sentence = []
    for i in range(length):
        sentence.append(random.choice(words))
    proverb= ' '.join(sentence)
    return proverb


from collections import defaultdict

separiators = ['.', '!', '?']

from collections import defaultdict

from nltk import ngrams

def normalizeText(text):
    cleaned=[]
    for line in text:
        line=line.lower()
       # line=re.sub(r"[,.\"\'!@#$%^&*(){}?/;`~:<>+=-\\]", "", line)

        tokens=word_tokenize(line)
        words=[word for word in tokens if word.isalpha()]
        cleaned+=words
        # cleaned.append('.')
    return cleaned
class MyMarkov2:
    def __init__(self, n=1):
        self.n = n
        self.markov_chain = {}
        self.tex_saved = ""

    def generate_n_gram(self, text):
        text = normalizeText(text)
        n_grams = ngrams(text.split(), self.n)
        n_grams = list(n_grams)
        return n_grams

    def get_start_words(self, text):
        start_words = []
        for sentence in text:
            sentence = re.sub(r'([,.!?"])', r' \1 ', sentence)
            sentence = word_tokenize(sentence)
            n_words = random.randint(1, max(len(sentence)-1, self.n)-1)
          #  print(sentence, n_words)

            list_of_start_words = [sentence[i] for i in range(n_words)]
            words = [word.lower() for word in list_of_start_words if word.isalpha()]
            start_words.append(' '.join(words))
        start_words = set(start_words)

        # Loop until we find a non-empty list of expressions containing the start_word
        while True:
            start_word = random.choice(list(start_words))
            if (len(start_word.split()) == 1):
                start_word += ' '
            expr = self.markov_chain.keys()
            expressions_containing = [exp for exp in expr if exp.startswith(start_word)]
            if expressions_containing:  # If the list is not empty, break out of the loop
                break
            else:  # Remove the start_word from the set and try again
                start_words.remove(start_word)
                if not start_words:  # If there are no more start_words to try, return an error or default value
                    return "Error: No valid starting words found."

        choice = random.choice(expressions_containing)
        return choice

    def train(self, text):
        self.tex_saved = text.copy()
        text = normalizeText(text)
        #print(text)

        for i in range(len(text) - self.n -self.n+1):
            curr_state, next_state = "", ""

            for j in range(self.n):
                #print(i, j)
                curr_state += text[i + j] + " "
                next_state += text[i + j + self.n] + " "
                #print(curr_state, next_state)

            curr_state = curr_state[:-1]
            next_state = next_state[:-1]
            if curr_state not in self.markov_chain:
                self.markov_chain[curr_state] = {}
                self.markov_chain[curr_state][next_state] = 1
            else:
                if next_state not in self.markov_chain[curr_state]:
                    self.markov_chain[curr_state][next_state] = 1
                else:
                    self.markov_chain[curr_state][next_state] += 1
            # calculate probabilities
            for curr_state, transition in self.markov_chain.items():
                total = sum(transition.values())
                for next_state, count in transition.items():
                    self.markov_chain[curr_state][next_state] = count / total

    def get_model(self):
        return self.markov_chain

    def generate_sentence(self, limit=100, sentences=[], start=''):
        n = 0
        #curr_state = start
        next_state = ""
        if (start == ''):
            curr_state =self.get_start_words(self.tex_saved)
        else:
            curr_state = start

        story = ""
        story += curr_state.capitalize() + " "
        while n < limit:
            if curr_state not in self.markov_chain:
                story+= ". "
                curr_state = self.get_start_words(self.tex_saved)
                story += curr_state.capitalize() + " "
            next_state = random.choices(list(self.markov_chain[curr_state].keys()),
                                        list(self.markov_chain[curr_state].values()))
            curr_state = next_state[0]
            story += curr_state + " "
            n +=self.n
        return story



proverbe=read_file("data/proverbe.txt")

print(proverbe[:10])

def generate_some_sentences_n(sentences,lenghts=[10],states=2):
    markov=MyMarkov2(states)
    markov.train(sentences)
    for length in lenghts:
        print(markov.generate_sentence(sentences=sentences,limit=length))
        print('\n')
        print('----------------------------------------------------------\n')

proverbe=read_file("data/proverbe.txt")
print(generate_some_sentences_n(proverbe,[10,20,15,5],4))
# proverbe[:10]

print(generate_some_sentences_n(proverbe,[10,20,15,5],2))


proverbe=read_file("data/proverbe.txt")
print(generate_some_sentences_n(proverbe,[10,20,15,5],2))
# proverbe[:10]