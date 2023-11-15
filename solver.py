import re
from itertools import chain

puzzle = [["p","n","b"],["o","u","c"],["a","r","i"],["k","t","m"]]
flattened_puzzle = list(chain(*puzzle))
strLetters = "".join(flattened_puzzle)

def getsAllLetters(word1, word2):
    comboWord = word1 + word2
    for l in strLetters:
        if l not in comboWord:
            return False
    
    return True

badCombos = []
for i in range(4):
    for j in range(3):
        if j == 2:
            k = 0
        else:
            k = j+1
        badCombos.append(puzzle[i][j]+puzzle[i][k])
        badCombos.append(puzzle[i][k]+puzzle[i][j])
        badCombos.append(puzzle[i][k]+puzzle[i][k])

file_path = 'words_alpha.txt' 
with open(file_path, 'r') as file:
    lines_array = [line.strip() for line in file.readlines()]


correct_letters = [word for word in lines_array if re.search(f"[{strLetters}]{'{4,}'}", word) is not None and len(re.search(f"[{strLetters}]{'{4,}'}", word).group(0)) == len(word)]
valid_words = []
for word in correct_letters:
    good = True
    for combo in badCombos:
        if combo in word:
            good = False
            break
    if good:
        valid_words.append(word)

valid_words = sorted(valid_words, key=len)
valid_combos = []

for word1 in valid_words:
    for word2 in valid_words:
        if (word1[0] == word2[-1] or word1[-1] == word2[0]) and getsAllLetters(word1, word2):
            valid_combos.append([word1,word2])

print(valid_combos)