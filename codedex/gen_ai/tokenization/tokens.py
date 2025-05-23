import nltk

# Then import and use it
from nltk.tokenize import word_tokenize


# Download the correct tokenizer model
nltk.download('punkt_tab')


sample_text = 'I love programming!'
tokens = word_tokenize(sample_text)

print('Tokens:', tokens)