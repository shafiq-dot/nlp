#Tokenization using Gensim

#pip install gensim
from gensim.utils import tokenize
# Create a string input
str = "I love to study Natural Language Processing in Python"

# tokenizing the text
print(list(tokenize(str)))