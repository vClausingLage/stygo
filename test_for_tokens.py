import re

# input

# join disjunct tokens
def joinWords(query_string):
  for index,string in enumerate(query_string):
    string.strip()
    if string[-1] == "-":
      string = list(string)
      string.remove("-")
      string = "".join(string)
      query_string[index] = string
      query_string[index] = query_string[index] + query_string[index + 1]
      query_string.pop(index + 1)
  return query_string

# remove noise
def removeNoise(query_string, noise_terms):
  noise_terms = noise_terms.strip()
  noise_terms = noise_terms.split()
  for term in noise_terms:
    query_string = re.sub(rf'\b{term}\b', '', query_string)
  query_string = re.sub('\s\s+', ' ', query_string)
  return query_string

# find tokens
def findToken(text, query_str):
  result = []
  query_str = query_str.split()
  for query in query_str:
    result = result + re.findall(rf'\b{query}\w+', text)
  return result

# count occurrences of tokens 
def word_count(query_string):
   counts = dict()
   words = query_string.split()
   for word in words:
       if word in counts:
           counts[word] += 1
       else:
           counts[word] = 1
   counts = sorted(counts.items(), key=lambda item: item[1])
   return counts

# output