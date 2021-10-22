
lemmata = [("πατηρ", "πατρος"), ("ανηρ", "ανδρος"), ("βροτος", "βροτου")]

endingsK = ["ι", "ος", "α", "ες", "ων", "σι", "σιν", "ας"]
endingsOm = ["ου", "ω", "ον", "οι", "ων", "οις", "ους"]
endingsOn = ["ου", "ω", "ον", "α", "ων", "οις"]


lemmata_list = []


def replaceLemmata(text, lemmata_list):
  for lemmata in lemmata_list:
    for lemma in lemmata:
      print(lemma)
      print(lemmata[0])
      text = text.replace(lemma, lemmata[0])
  return text
