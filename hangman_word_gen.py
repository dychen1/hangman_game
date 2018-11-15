import urllib.request
import random

def word_generator():
    word_url = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
    response = urllib.request.urlopen(word_url)
    long_txt = response.read().decode()
    words_array = long_txt.splitlines()
    generated_word = words_array[random.randint(0, len(words_array))]
    return generated_word