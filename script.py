import json

correct_in = list(open("bibtex/correct.bibtex", "r"))
not_correct_a_in = list(open("bibtex/not_correct_a.bibtex", "r"))
not_correct_b_in = list(open("bibtex/not_correct_b.bibtex", "r"))

in_files = [correct_in, not_correct_a_in, not_correct_b_in]

def contains_letter(string):
   return string.lower().islower()

def display_list(list):
   for i in range(len(list)):
      print(f"{i}. {list[i]}")

# IN FILES TREATMENT

def get_processed_list_in_files(list):
   striped = [i.strip() for i in list]
   for i in range(len(striped)):
      if not contains_letter(striped[i]):
         del striped[i]
   filtered = [item for item in striped if item[:8]=="<authors"]
   return filtered

correct_in = get_processed_list_in_files(correct_in)
not_correct_a_in = get_processed_list_in_files(not_correct_a_in)
not_correct_b_in = get_processed_list_in_files(not_correct_b_in)

# OUT FILES TREATMENT

correct_in_authors_only, not_correct_a_in_authors_only, not_correct_b_in_authors_only = [], [], []

for i in range(len(correct_in)):
   correct_in_authors_only.append(correct_in[i][17:-3])
for i in range(len(not_correct_a_in)):
   not_correct_a_in_authors_only.append(not_correct_a_in[i][17:-3])
for i in range(len(not_correct_b_in)):
   not_correct_b_in_authors_only.append(not_correct_b_in[i][17:-3])

correct_out, not_correct_a_out, not_correct_b_out = [], [], []

for i in range(len(correct_in_authors_only)):
   correct_out.append('author:\"'+str(correct_in_authors_only[i])+'\"')
for i in range(len(not_correct_a_in_authors_only)):
   not_correct_a_out.append('author:\"'+str(not_correct_a_in[i])+'\"')
for i in range(len(not_correct_b_in_authors_only)):
   not_correct_b_out.append('author:\"'+str(not_correct_b_in[i])+'\"')

if len(correct_in)==len(correct_out):
   for i in range(len(correct_in)):
      print(f"in: {correct_in[i]} -> out: {correct_out[i]}")

