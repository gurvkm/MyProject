//This code is how to stem words by deleting extra words from them
//In this case we are stemming these words "Python","Pythoner","Pythoned","Pythoning","Pythons","Pythonly" into Python as there stem is python.
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
ps=PorterStemmer()
example_words=["Python","Pythoner","Pythoned","Pythoning","Pythons","Pythonly"]
new_text="It is very important to be Pythonly,while you are Pythoning with Python. All Pythoners have Pythoned once."
words=word_tokenize(new_text)
for w in words:
   print(ps.stem(w))
