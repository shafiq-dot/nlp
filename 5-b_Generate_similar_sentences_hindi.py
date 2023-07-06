# Generate similar sentences from a given Hindi text input

#!pip install torch==1.3.1+cpu -f https://download.pytorch.org/whl/torch_stable.html
#!pip install inltk
#!pip install tornado==4.5.3
from inltk.inltk import setup
setup('hi')
from inltk.inltk import get_similar_sentences
# get similar sentences to the one given in hindi
output = get_similar_sentences('मैंआज बहुि खुश हूं', 5, 'hi')
print(output)

#Output:
#['मैंआजकल बहुि खुश हूं', 'मैंआज अत्यतिक खुश हूं', 'मैंअभी बहुि खुश हूं', 'मैंवितमान बहुि
#खुश हूं', 'मैंवितमान बहुि खुश हूं']
