'''
word_count.py

I am using the string module (though it's not strictly necessary),
it's a good opportunity to introduce it to students. Also, accounting 
for certain specific characters like the curly open (close) quotes. 
This can be an extra credit for students to account for characters
aside from whitespace. 
Generally solution closely follows 'think python' solution to similar problem.

'''


import string

def process_line(line, hist):
    line = line.replace('-', ' ')

    for word in line.split():
        word = word.strip(string.punctuation + string.whitespace \
                + "“" + "”" + "‘" + "’")
        word = word.lower()

        hist[word] = hist.get(word, 0) + 1


def word_count(text_file, n):
    with open(text_file) as f:
        article = f.readlines()
    
    hist = {}

    for line in article:
        process_line(line, hist)

    r = sorted(hist.items(), key=lambda x: (-x[1], x[0]))
    if n > len(r):
        n = len(r)
    return r[:n]


print(word_count("article.txt", 10))
