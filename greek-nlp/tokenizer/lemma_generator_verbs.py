# grammar tables https://en.wiktionary.org/wiki/Appendix:Ancient_Greek_grammar_tables

optative = "οι"
augment = "ε"
temp_aor_fut = "σ"
temp_perf = "κ"
pers_pres = ["ω", "εις", "ει", "ετον", "ετον", "ομεν", "ετε", "ουσι", "ουσιν", "ειν"]
pers_pres_mid = ["ο", "ομαι", "η", "εται", "ομεθα", "εσθε", "ονται", "εσθαι"]
pers_pres_conj = ["ω" "ης" "η" "ωμεν" "ητε" "ωσι" "ωσιν"]
pers_pres_mid_conj = ["ωμαι", "η", "ηται", "ωμεθα", "ησθε", "ωνται"]
pers_pres_opt = []
pers_pres_mid_opt = []
pers_pres_fut_opt = []
present = [x for x in [pers_pres, pers_pres_mid, pers_pres_conj, pers_pres_mid_conj, pers_pres_opt, pers_pres_mid_opt, pers_pres_fut_opt]]
pers_imperf = ["ον", "ες", "εν", "ε", "ομεν", "ετε"]
pers_aor = []
pers_perf = []
stem = "βαλλω"

# make pres
def agglutinate(*args):
  # args[0]: stem args[1]: ending args[2]: temp_sign
  stem = args[0]
  ending = args[1]
  temp_sign = ""
  augment = ""
  if len(args) > 2:
    temp_sign = args[2]
    if len(args) > 3:
      augment = "ε"
  if stem[-1] != "ω":
    print("no 1. Pers. Sg. input")
  if stem[-2] != "ο" or stem[-2] != "α" or stem[-2] != "ε":
    stem = stem[:-1]
    return augment + stem + temp_sign + ending
forms_present = [agglutinate(stem, ending) for ending in present]
print(forms_present)