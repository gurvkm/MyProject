#learning to use stopword
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
example_sentence="This is an example sentence showing off stop word filteration" #is,an and off are stop words so it will be removed
stop_words=set(stopwords.words("english")) #all predefined stopwords will assinged in stop_words set
words=word_tokenize(example_sentence) #it will tokenize the example sentence and assing to words list
filtered_sentence=[] #list created
for w in words:
    if w not in stop_words: #compare if any word in stop_words set are similar to words in list named words
       filtered_sentence.append(w) #append words which are not the stop words
#filtered_sentence=[w for w in words if not w in stop_words] #one liner fancy use

print(filtered_sentence)


