import re

diacritics = {"α": ["ά", "ὰ", "ἀ", "ἁ", "ἂ", "ἃ", "ἄ", "ἆ", "ἇ", "ἅ", "Α"], 
"ε": ["έ", "ὲ", "ἐ", "ἑ", "ἒ", "ἓ", "ἔ", "Ἑ"], 
"ι": ["ί", "ὶ", "ἰ", "ἱ", "ἲ", "ἳ", "ῖ", "ἷ", "ἴ", "ΐ", "ἶ"], 
"ο": ["ό", "ὸ", "ὀ", "ὁ", "ὂ", "ὃ", "ὄ", "ὅ", "ὅ"], 
"υ": ["ύ", "ὺ", "ὐ", "ὑ", "ὒ", "ὓ", "ῦ", "ὗ", "ὖ", "Ὑ"], 
"ω": ["ώ", "ὼ", "ὠ", "ὡ", "ὢ", "ὣ", "ῶ", "ῳ", "ῷ", "ὧ", "ὦ", "ᾦ", "ῷ", "ᾢ"], 
"η": ["ή", "ὴ", "ἠ", "ἡ", "ἢ", "ἣ", "ῆ", "ἦ", "ῃ", "ἧ", "ἦ", "ᾖ", "ῇ", "ᾒ", "ἤ"]}

def dediacriticalizer(string):
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