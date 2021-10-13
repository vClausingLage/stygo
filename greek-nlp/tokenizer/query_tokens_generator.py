# STEMS_DECL
# RULE : DICT | {"oDecl": [], "aDecl": []}
stems_decl = {"aDecl": "", "oDecl": ""}


# add stems
# RULE : semantic | declination || conjugation
anger_o = "φόβος πόλεμος"
anger_a = "βλάβη"

# ADD variables to STEMS_DECL DICT
stems_decl["oDecl"] = anger_o
stems_decl["aDecl"] = anger_a