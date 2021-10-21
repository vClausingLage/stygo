# STEMS_DECL
# RULE : DICT_semantics | {"oDecl": [], "aDecl": []}
stems_decl_full = {
  "angry": {"aDecl": [], "oDecl": [], "kDecl": [], "Adj": [], "result": []}, 
  "nasty": {"aDecl": [], "oDecl": [], "kDecl": [], "Adj": [], "result": []}, 
  "affectionate": {"aDecl": [], "oDecl": [], "kDecl": [], "Adj": [], "result": []}, 
  "nice": {"aDecl": [], "oDecl": [], "kDecl": [], "Adj": [], "result": []}
}

# add stems
# RULE : semantic | declination || conjugation
angry_o = "φόβος πόλεμος"
angry_a = "βλάβη ὀργή αἰσχύνη"
angry_k = ""
angry_adj = "στυγερός ἐχθρός"

nasty_o = "ψόγος"
nasty_a = ""
nasty_k = "δεῖμα"
nasty_adj = ""

affectionate_o = ""
affectionate_a = ""
affectionate_k = ""
affectionate_adj = ""

nice_o = ""
nice_a = ""
nice_k = ""
nice_adj = ""

angry_o = angry_o.split()
angry_a = angry_a.split()
angry_k = angry_k.split()
angry_adj = angry_adj.split()

nasty_o = nasty_o.split()
nasty_a = nasty_a.split()
nasty_k = nasty_k.split()
nasty_adj = nasty_adj.split()

affectionate_o = affectionate_o.split()
affectionate_a = affectionate_a.split()
affectionate_k = affectionate_k.split()
affectionate_adj = affectionate_adj.split()

nice_o = nice_o.split()
nice_a = nice_a.split()
nice_k = nice_k.split()
nice_adj = nice_adj.split()

# ADD variables to STEMS_DECL DICT
stems_decl_full["angry"]["oDecl"].append(angry_o)
stems_decl_full["angry"]["aDecl"].append(angry_a)
stems_decl_full["angry"]["kDecl"].append(angry_k)
stems_decl_full["angry"]["Adj"].append(angry_adj)
stems_decl_full["nasty"]["oDecl"].append(nasty_o)
stems_decl_full["nasty"]["aDecl"].append(nasty_a)
stems_decl_full["nasty"]["kDecl"].append(nasty_k)
stems_decl_full["nasty"]["Adj"].append(nasty_adj)
stems_decl_full["affectionate"]["oDecl"].append(affectionate_o)
stems_decl_full["affectionate"]["aDecl"].append(affectionate_a)
stems_decl_full["affectionate"]["kDecl"].append(affectionate_k)
stems_decl_full["affectionate"]["Adj"].append(affectionate_adj)
stems_decl_full["nice"]["oDecl"].append(nice_o)
stems_decl_full["nice"]["aDecl"].append(nice_a)
stems_decl_full["nice"]["kDecl"].append(nice_k)
stems_decl_full["nice"]["Adj"].append(nice_adj)

angry_str = 'βίᾳ βία θαν κακ   μένο ἐπιθαν ἔχθρ πολεμ πόλεμ βλάβ'
nasty_str = 'καταισχύν αἶσχ ψόγ ἀνοσί ποιν πόν δακρύ ἀλγειν γόο δαΐ πικρ μέριμνα δάκ δόλ δεῖμ'
affectionate_str = 'φίλ φιλ γάμ γαμηλί κοίτ σωτηρί χαίρε εὔνοι'
nice_str = 'εὐχ ἡδον θέλκτορ θέλκτωρ οἰκεῖν βέλτερον προξένῳ φιλόξενον καλῶς ἁγνοῦ σέβας ὀρθοῖ εὖ ἀσφάλεια πανδίκως χρηστήρια ἀγαθ ἁγν'
affection_regex = 'εὐ συν συμ ξυμ ξυν'
reluctance_regex = 'δυσ'
exceptions = 'μένοι μένοις μένοιεν μένουσι'