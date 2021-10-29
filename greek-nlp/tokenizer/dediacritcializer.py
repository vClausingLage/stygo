import re

diacritics = {"α": ["ά", "ὰ", "ἀ", "ἁ", "ἂ", "ἃ", "ἄ", "ᾶ", "ἆ", "ἇ", "ἅ", "ᾳ", "ᾇ", "ᾷ", "Α", "Ἀ", "Ἄ", "Ἁ"], 
"ε": ["έ", "ὲ", "ἐ", "ἑ", "ἒ", "ἓ", "ἔ", "ἕ", "Ἑ", "Ἕ"], 
"ι": ["ί", "ὶ", "ἰ", "ἱ", "ἲ", "ἳ", "ἵ", "ῖ", "ἷ", "ἴ", "ΐ", "ῖ", "ἶ", "Ἰ"], 
"ο": ["ό", "ὸ", "ὀ", "ὁ", "ὂ", "ὃ", "ὄ", "ὅ", "ὅ"], 
"υ": ["ύ", "ὺ", "ὐ", "ὑ", "ὒ", "ὓ", "ὔ", "ῦ", "ὗ", "ὖ", "ὕ", "Ὑ"], 
"ω": ["ώ", "ὼ", "ὠ", "ὡ", "ὢ", "ὣ", "ῶ", "ῳ", "ῷ", "ὧ", "ὦ", "ᾦ", "ῷ", "ᾢ"], 
"η": ["ή", "ὴ", "ἠ", "ἡ", "ἢ", "ἣ", "ῆ", "ἦ", "ῃ", "ἧ", "ἦ", "ᾖ", "ῇ", "ᾒ", "ἤ", "ᾔ", "ῄ"]}

def dediacriticalizer(string):
  # remove all ᾽ in string
  string = string.replace("᾽", "")
  for x in diacritics["α"]:
    string = re.sub(f"{x}", "α", string)
  for x in diacritics["ε"]:
    string = re.sub(f"{x}", "ε", string)
  for x in diacritics["ι"]:
    string = re.sub(f"{x}", "ι", string)
  for x in diacritics["ο"]:
    string = re.sub(f"{x}", "ο", string)
  for x in diacritics["υ"]:
    string = re.sub(f"{x}", "υ", string)
  for x in diacritics["ω"]:
    string = re.sub(f"{x}", "ω", string)
  for x in diacritics["η"]:
    string = re.sub(f"{x}", "η", string)
  return string