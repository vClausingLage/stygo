# STEMS_DECL
# RULE : DICT_semantics | {"oDecl": [], "aDecl": []}
stems_decl_full = {
  "angry": {"aDecl": [], "oDecl": [], "kDecl": [], "result": []}, 
  "nasty": {"aDecl": [], "oDecl": [], "kDecl": [], "result": []}, 
  "affectionate": {"aDecl": [], "oDecl": [], "kDecl": [], "result": []}, 
  "nice": {"aDecl": [], "oDecl": [], "kDecl": [], "result": []}
}

# add stems
# RULE : semantic | declination || conjugation
angry_o = "φόβος πόλεμος ἐχθρός στυγερός"
angry_a = "βλάβη ἐχθρά στυγερά ὀργή αἰσχύνη"
angry_k = ""

nasty_o = "ψόγος"
nasty_a = ""
nasty_k = "δεῖμα"

angry_o = angry_o.split()
angry_a = angry_a.split()
angry_k = angry_k.split()

nasty_o = nasty_o.split()
nasty_a = nasty_a.split()
nasty_k = nasty_k.split()

# ADD variables to STEMS_DECL DICT
stems_decl_full["angry"]["oDecl"].append(angry_o)
stems_decl_full["angry"]["aDecl"].append(angry_a)
stems_decl_full["angry"]["kDecl"].append(angry_k)
stems_decl_full["nasty"]["oDecl"].append(nasty_o)
stems_decl_full["nasty"]["aDecl"].append(nasty_a)
stems_decl_full["nasty"]["kDecl"].append(nasty_k)

angry_str = ' βίᾳ βία θαν κακ   μένο ἐπιθαν ἔχθρ πολεμ πόλεμ βλάβ'
nasty_str = 'καταισχύν αἶσχ ψόγ ἀνοσί ποιν πόν δακρύ ἀλγειν γόο δαΐ πικρ μέριμνα δάκ δόλ δεῖμ'
affectionate_str = 'φίλ φιλ γάμ γαμηλί κοίτ σωτηρί χαίρε εὔνοι'
nice_str = 'εὐχ ἡδον θέλκτορ θέλκτωρ οἰκεῖν βέλτερον προξένῳ φιλόξενον καλῶς ἁγνοῦ σέβας ὀρθοῖ εὖ ἀσφάλεια πανδίκως χρηστήρια ἀγαθ ἁγν'
affection_regex = 'εὐ συν συμ ξυμ ξυν'
reluctance_regex = 'δυσ'
exceptions = 'μένοι μένοις μένοιεν μένουσι'