import nltk
import string
import pandas as pd
#nltk.download_shell()

import matplotlib.pyplot as plt

from email import message
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer


messages = pd.read_csv(r'C:\Users\megam\source\repos\Data_Science_ML_DL_lectures\Machine_Learning\SMSSpamCollection', sep='\t', names=['label', 'message'])
print(len(messages))
print(messages.iloc[0])

messages['length']=messages['message'].apply(len)

print(messages.head(10))

messages['length'].hist(bins=150)
plt.show()

print(messages[messages['length']>900]['message'].iloc[0])

messages.hist(column='length', by='label', bins=60, figsize=(12,4))
plt.show()

# removing punctuations example

mess = 'my name is/ jethro, in the heaven: okay'

no_punc = [c for c in mess if c not in string.punctuation]
print(no_punc)

# joining items on a list together
no_punc = ''.join(no_punc)
print(no_punc)

# stop words

#print(stopwords.words('english'))

clean_word = [word for word in no_punc.split() if word.lower() not in stopwords.words('english')] 
print(clean_word)

#Tokenization
def text_process(mess):
    """
    Takes in a string of text, then performs the following:
    1. Remove all punctuation
    2. Remove all stopwords
    3. Returns a list of the cleaned text
    """
    # Check characters to see if they are in punctuation
    nopunc = [char for char in mess if char not in string.punctuation]

    # Join the characters again to form the string.
    nopunc = ''.join(nopunc)
    
    # Now just remove any stopwords
    return [word for word in nopunc.split() if word.lower() not in stopwords.words('english')]

messages['message'].apply(text_process)

# Check to make sure its working
#print(messages['message'].head(5).apply(text_process))

#Vectorization

#1. Count how many times does a word occur in each message (Known as term frequency)

#2. Weigh the counts, so that frequent tokens get lower weight (inverse document frequency)

#3. Normalize the vectors to unit length, to abstract from the original text length (L2 norm)

c_vect = CountVectorizer(analyzer = text_process).fit(messages['message'])# bag of words transformer
print(len(c_vect.vocabulary_))

vect5 = messages['message'][3]
vect5 = c_vect.transform([vect5])
print(vect5)

print(c_vect.get_feature_names_out()[4068])

message_bow = c_vect.transform(messages['message'])

print('Shape of Sparse Matrix: ', message_bow.shape)
print('Amount of Non-Zero occurences: ', message_bow.nnz)

# checking the sparcity
sparsity = (100.0 * message_bow.nnz / (message_bow.shape[0] * message_bow.shape[1]))
print('sparsity: {}'.format(round(sparsity)))

#TF_IDF

tfidf_transformer = TfidfTransformer()
tfidf = tfidf_transformer.fit_transform(message_bow)  

tfidf5 =tfidf_transformer.transform(vect5)
print(tfidf5)