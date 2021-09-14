import csv, pprint, random
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk.tokenize import blankline_tokenize
from nltk.util import bigrams, trigrams, ngrams

fdist = FreqDist()
pp = pprint.PrettyPrinter(indent=3)

correct_in = list(open("bibtex/correct.bibtex", "r"))
incorrect_a_in = list(open("bibtex/not_correct_a.bibtex", "r"))
incorrect_b_in = list(open("bibtex/not_correct_b.bibtex", "r"))

fieldnames = ['in', 'out']
rows = []

def pretty_print(list):
   for i in range(len(list)):
      print(f"{i}. {list[i]}")

def contains_letter(string):
   return string.lower().islower()

def preprocessing(list):
   striped = [i.strip() for i in list]
   for i in range(len(striped)):
      if not contains_letter(list[i]):
         del striped[i]
   return [item for item in striped if item[:8]=='<authors']

def transformation(list):
   to_return = []
   for i in range(len(list)):
      to_return.append('author:'+"'"+list[i][17:-3]+"'")
   return to_return

def lists_to_vocab(list_of_lists):
   vocab = """
           """
   for list in list_of_lists:
      for i in range(len(list)):
         vocab+=" "
         vocab+=list[i]
         vocab+=" "
   return vocab

def add_spaces_list(list):
   for i in range(len(list)):
      if "'" in list[i]:
         list[i] = list[i].replace("'", " ' ")
      if '"' in list[i]:
         list[i] = list[i].replace('"', ' " ')
   return list

def add_spaces_str(word):
   if '"' in word:
      word = word.replace('"', ' " ')
   if "'" in word:
      word = word.replace("'", " ' ")
   return word

def print_grams(grams):
   for gram in grams:
      print(gram)
   print("===")

correct_in = preprocessing(correct_in)
incorrect_a_in = preprocessing(incorrect_a_in)
incorrect_b_in = preprocessing(incorrect_b_in)

# replace " by '
for i in range(len(correct_in)):
   if '"' in list(correct_in[i]):
      correct_in[i] = correct_in[i].replace('"', "'")

correct_out = transformation(correct_in)
incorrect_a_out = transformation(incorrect_a_in)
incorrect_b_out = transformation(incorrect_b_in)

# delete shift between incorrect lists
shift = abs(len(incorrect_a_out)-len(incorrect_b_out))
biggest = [incorrect_a_in, incorrect_a_out] if len(incorrect_a_out)>len(incorrect_b_out) else [incorrect_b_in, incorrect_b_out]

for i in range(shift):
   for list in biggest:
      del list[-1]

# create final lists
input_ = correct_in + incorrect_a_in[:len(incorrect_a_in)//2]
output_ = correct_out + incorrect_b_out[:len(incorrect_b_out)//2]

# shuffle lists
random.Random(4).shuffle(input_)
random.Random(4).shuffle(output_)

incorr, tt = 0, 0

if len(input_)==len(output_):
   for i in range(len(input_)):
      # print(f"{i}. {input_[i]} -> {output_[i]}")
      if input_[i][17:-3]!=output_[i][8:-1]:
         incorr+=1
      tt+=1
      rows.append(
         {
            'in': add_spaces_str(input_[i]),
            'out': add_spaces_str(output_[i])
         }
      )

print(f"Preprocessing successfully operated !\n>>> Pourcentage de vrais négatifs: {round(100*incorr/tt, 1)}%")

# add spaces to tokenize correctly
input_ = add_spaces_list(input_)
output_ = add_spaces_list(output_)

with open('dataset.csv', 'w', encoding='utf-8', newline='') as outfile:
   writer = csv.DictWriter(outfile, fieldnames=fieldnames)
   writer.writeheader()
   writer.writerows(rows)

# === TOKENIZE ===
# create vocab
vocab = lists_to_vocab([input_, output_])
# print(vocab)

# create tokens
tokens = word_tokenize(vocab)
print(len(tokens))
# pretty_print(tokens[0:10])

# freqdist
for word in tokens:
   fdist[word.lower()]+=1
# pp.pprint(dict(fdist))
pp.pprint(dict(fdist.most_common(15)))

# blank tokenizer
vocab_blank = blankline_tokenize(vocab)

def test_xgrams():
   string = "<authors author= ' Simon Duperray ' />"
   test_token = word_tokenize(string)
   bigrams = bigrams(test_token)
   trigrams = trigrams(test_token)
   ngrams = ngrams(test_token, 5)

   print_grams(bigrams)
   print_grams(trigrams)
   print_grams(ngrams)

