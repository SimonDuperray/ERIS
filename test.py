from nltk.tokenize import word_tokenize

def pretty_printer(list):
   for i in range(len(list)):
      print(f"{i}. {list[i]}")

vocab = "<authors author= ' Simon Duperray ' />"

tokens = word_tokenize(vocab)
print(len(tokens))
pretty_printer(tokens)