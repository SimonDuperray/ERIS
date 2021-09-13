import json

correct_in = list(open("bibtex/correct.bibtex", "r"))
not_correct_a_in = list(open("bibtex/not_correct_a.bibtex", "r"))
not_correct_b_in = list(open("bibtex/not_correct_b.bibtex", "r"))

correct_out = list(open("xmi/correct_out.xmi"))
not_correct_a_out = list(open("xmi/not_correct_a_out.xmi"))
not_correct_b_out = list(open("xmi/not_correct_b_out.xmi"))

in_files = [correct_in, not_correct_a_in, not_correct_b_in]
out_files = [correct_out, not_correct_a_out, not_correct_b_out]

def contains_letter(string):
   return string.lower().islower()

def get_processed_list(list):
   to_return = []
   striped = [i.strip() for i in list]
   for i in range(len(striped)):
      if not contains_letter(striped[i]):
         del striped[i]
   filtered = [item for item in striped if item[:8]=="<authors"]
   return filtered

def display_list(list):
   for i in range(len(list)):
      print(f"{i}. {list[i]}")

correct_in = get_processed_list(correct_in)
not_correct_a_in = get_processed_list(not_correct_a_in)
not_correct_b_in = get_processed_list(not_correct_b_in)

while True:
   which = input("Quelle liste ? c, a, b")
   if which=='c':
      display_list(correct_in)
   elif which=='a':
      display_list(not_correct_a_in)
   elif which=='b':
      display_list(not_correct_b_in)
   else:
      pass

processed_correct_in = get_processed_list(correct_in)
for i in range(len(processed_correct_in)):
   print(f"{i}. {processed_correct_in[i]}")
