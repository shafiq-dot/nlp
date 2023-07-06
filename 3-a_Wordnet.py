'''WordNet provides synsets which is the collection of synonym words also called
“lemmas”'''
import nltk
from nltk.corpus import wordnet
print(wordnet.synsets("computer"))
# definition and example of the word ‘computer’
print(wordnet.synset("computer.n.01").definition())
#examples
print("Examples:", wordnet.synset("computer.n.01").examples())
#get Antonyms
print(wordnet.lemma('buy.v.01.buy').antonyms())