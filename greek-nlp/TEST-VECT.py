## strings
str1 = "οσιοι"
str2 = "κακοι"
## Hamming distance
"""
hamming distance is only applicable to strings with EQUAL LENGTH
"""
def hamming_distance(string1, string2):
	dist_counter = 0
	for n in range(len(string1)):
		if string1[n] != string2[n]:
			dist_counter += 1
	return dist_counter
# d_str_ham = hamming_distance(str1,str2)
# print(d_str_ham)
## Levenstein distance
"""
levenstein distance allows insertion, deletion, substitution
"""
from difflib import ndiff
def levenshtein_distance(str1, str2, ):
    counter = {"+": 0, "-": 0}
    distance = 0
    for edit_code, *_ in ndiff(str1, str2):
        if edit_code == " ":
            distance += max(counter.values())
            counter = {"+": 0, "-": 0}
        else: 
            counter[edit_code] += 1
    distance += max(counter.values())
    return distance
d_str_lev = levenshtein_distance(str1,str2)
print(d_str_lev)