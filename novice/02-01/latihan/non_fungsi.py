dictionary = ['fox', 'boss', 'orange', 'toes', 'fairy', 'cup']
def puralize(words):
   for i in range(len(words)):
       word = words[i]
       if word.endswith('s') or word.endswith('x'):
           word += 'es'
       if word.endswith('y'):
           word = word[:-1] + 'ies'
       else:
           word += 's'
       words[i] = word

def test_pluralize():
    pluralize(dictionary)
    assert dictionary == ['foxes', 'bosses', 'oranges', 'toeses', 'fairies', 'cups']