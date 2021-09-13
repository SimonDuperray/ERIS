import csv

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

incorr, tt = 0, 0

if len(input_)==len(output_):
   for i in range(len(input_)):
      if input_[i][17:-3]!=output_[i][8:-1]:
         incorr+=1
         # print("===")
      tt+=1
      rows.append(
         {
            'in': input_[i],
            'out': output_[i]
         }
      )

print(f"Preprocessing successfully operated !\n>>> Pourcentage de vrais négatifs: {round(100*incorr/tt, 1)}%")

with open('dataset.csv', 'w', encoding='utf-8', newline='') as outfile:
   writer = csv.DictWriter(outfile, fieldnames=fieldnames)
   writer.writeheader()
   writer.writerows(rows)