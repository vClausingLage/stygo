import re
import json

# To Do 

with open('euripides.txt', 'r', encoding='utf8') as file:
    text = file.read()
    text = json.loads(text)

author = 'Euripides'

text_str = " ".join(text)

def joinWords(text_str):
  text_str = re.sub('-\s', '', text_str)
  return text_str

def removeNoise(query_string):
  noise_terms = 'γάρ νιν δέ θ γ εἰ ἢ τί ὦ μὲν τὴν δὲ καὶ ὁ τῆς τὸν τῶν δ Χορός γὰρ τε ἐν τὸ ὡς τ πρὸς ἂν μὴ οὐ οὐκ ἀλλ ἐκ νῦν τὰ τις τόδ ἐπ ἐπὶ ἤδη δὴ ἐς πῶς'
  noise_terms = noise_terms.strip()
  noise_terms = noise_terms.split()
  for term in noise_terms:
    query_string = re.sub(rf'\b{term}\b', '', query_string)
  return query_string

def word_count(str):
    counts = dict()
    words = str.split()
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    counts = sorted(counts.items(), key=lambda item: item[1])
    return counts

text_str = joinWords(text_str)
text_str = removeNoise(text_str)
print(word_count(text_str))

word_total = len(text)

def findAnger(text, query_str):
  result = []
  query_str = query_str.split()
  for query in query_str:
    result = result + re.findall(rf'\b{query}\w+', text)
  return result

angry_str = 'ἐχθρ φόβ στυγ βίᾳ βία θαν κακ ὀργ δεῖμ μένο ἐπιθαν'
nasty_str = 'καταισχύν αἶσχ ψόγ ἀνοσί ποιν πόν δακρύ ἀλγειν'
affectionate_str = 'φίλ φιλ γάμ γαμηλί κοίτ σωτηρί'
nice_str = 'ἡδον θέλκτορ θέλκτωρ οἰκεῖν βέλτερον προξένῳ φιλόξενον καλῶς ἁγνοῦ σέβας ὀρθοῖ εὖ ἀσφάλεια πανδίκως χρηστήρια'
affection_regex = 'εὐ συν συμ ξυμ ξυν'
reluctance_regex = 'δυσ'

#print('anger', findAnger(text_str, angry_str))
#print('nasty',findAnger(text_str, nasty_str))
#print('affectionate',findAnger(text_str, affectionate_str))
#print('nice',findAnger(text_str, nice_str))

anger = len(findAnger(text_str, angry_str))
nasty = len(findAnger(text_str, nasty_str))
affectionate = len(findAnger(text_str, affectionate_str))
nice = len(findAnger(text_str, nice_str))

with open('euripidesData.json', 'w', encoding='utf8') as file:
  data = {"author": author, "total": word_total, "angry": anger / word_total, "nasty": nasty / word_total , "affectionate": affectionate / word_total , "nice": nice / word_total}
  output = json.dumps(data, ensure_ascii=False)
  file.write(output)
