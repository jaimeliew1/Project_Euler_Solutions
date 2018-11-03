# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 16:37:57 2018

@author: J
"""
def run(verbose=True):
    # get list of lists of word anagrams from file
    with open('Data/p098_words.txt') as f:
        words = [x[1:-1] for x in f.read().split(',')]
    anagrams = {}
    for word in words:
        key = ''.join(sorted(word))
        if key in anagrams.keys():
            anagrams[key].append(word)
        else:
            anagrams[key] = [word]
    anagrams = [x for x in anagrams.values() if len(x) > 1]

    # get list of lists of anagrams of square numbers less than 1e10
    anagram_squares = {}
    for square in [str(x**2) for x in range(31623)]:
        key = ''.join(sorted(square))
        if key in anagram_squares.keys():
            anagram_squares[key].append(square)
        else:
            anagram_squares[key] = [square]
    anagram_squares = [x for x in anagram_squares.values() if len(x) > 1]

    # loop through all anagram sets, creating a mapping to the square anagrams
    # and see if any of them have matching pairs. store the square number in
    # ans then return the largest square number.
    ans = []
    for word_set in anagrams:
        if len(word_set) == 3:
            continue # skipping the one set with more than 2 anagrams as its too hard
        # choose only squares with same number of characters
        square_sets = [x for x in anagram_squares if len(x[0]) == len(word_set[0])]
        # choose only squares with the same number of unique characters
        square_sets = [x for x in square_sets if len(set(x[0])) == len(set(word_set[0]))]

        word = word_set[0] # compare to the first word in the word_set
        for square_set in square_sets:
            for square in square_set:
                mapping = {n:l for n, l in zip(square, word)}
                for s in square_set:
                    mapped_word = s
                    for n, l in mapping.items():
                        mapped_word = mapped_word.replace(n, l)
                    if mapped_word in word_set[1:]:
                        print(word, mapped_word, s)
                        ans.append(s)

    return max(int(x) for x in ans)

if __name__ == '__main__':
    print(run())



