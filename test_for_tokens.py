import re
import json
from tokenizer import dediacritcializer
from tokenizer import noise_terms

with open("tokenizer/input.txt", "r") as f:   # input
  input = f.read()
with open("tokenizer/queryTokens.json", "r") as f:
  query_tokens = f.read()
  query_tokens = json.loads(query_tokens)

tokens = []
for el in query_tokens:   # prepare a STRING for QUERY_TOKENS
  for x in el:
    tokens.append(x)
tokens = " ".join(tokens)

input = dediacritcializer.dediacriticalizer(input)

def joinWords(query_string):    # join disjunct tokens
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

input = joinWords(input)

def removeNoise(query_string, noise_terms):   # remove noise
  noise_terms = noise_terms.strip()
  noise_terms = noise_terms.split()
  for term in noise_terms:
    query_string = re.sub(rf'\b{term}\b', '', query_string)
  query_string = re.sub('\s\s+', ' ', query_string)
  return query_string

input = removeNoise(input, noise_terms.noise_terms)
print(input)

def findToken(text, query_str):   # find tokens
  result = []
  query_str = query_str.split()
  for query in query_str:
    result = result + re.findall(rf'\b{query}\b', text)
  return result

input_results = findToken(input, tokens)
print(input_results)

def word_count(query_string):   # count occurrences of tokens 
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