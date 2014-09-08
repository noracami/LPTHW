from urllib.request import urlopen

WORD_URL = "http://learncodethehardway.org/words.txt"
#f = urllib.request.urlopen('http://learncodethehardway.org/words.txt')

words = []

for word in urlopen(WORD_URL).readlines():
    words.append(word.decode('utf8').strip())

for x in range(10):
    print(x, "\t", words[x])