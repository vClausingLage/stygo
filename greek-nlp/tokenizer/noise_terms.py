import re
from tokenizer import dediacritcializer

# sort items 
articles = 'τηδ ὅδ τάνδε τᾶσδ τήνδε τῷ τόδε τὰς τοῖς τοὺς τάδε τὴν ὁ τῆς τὸν τῶν τὸ τὰ τόδ τῶνδε τῶνδ τῆσδε τοῦ ἡ τοῦδ τόνδ τὰν τῆσδ τῇδε τάσδε τῷδ τοῖσδε τόνδε τήνδ ἅδε τόν τάδ τοῦδε ὧν ἐμῶν'
pronouns = 'αυτον καγω τοὐμὸν ὃν οὐδέν τούτων ταῦτα ταῦτ τοῦτ ὑμῖν τινί μου σοὶ ἐγώ σὲ ἃ τι σὸν ὃς σὺ σοι σε με τίς ἐγὼ μοι νιν τί τις τοι ἐμοῦ σέθεν ὅστις οἱ τιν ἡμῖν ἐμοῖς ἐμοὶ ἐμοί σύ οὔτις ἐμῆς οἷς σῆς κἀμὲ τοιοῖσδε σόν οὔτιν τοῦτο οὔτοι αὐτὸς'
particles = 'ιω ἆρ οὐχὶ ὥς δῆτα οὔ ἒ μηδ οὐδὲν μὴν οὖν οὐδ μή οὐχ ἀλλὰ ἀλλ γε γάρ δέ ὦ μὲν δὲ δ γὰρ ἂν μὴ οὐ οὐκ δὴ πῶς ἦ οὐδὲ οὔτε μέν μήτ ἄν ὅμως δή ἆρα ἠδὲ οὔτ'
adverbs = 'αυθις εὖ ποτ νῦν ἤδη τότ αὖ τάχ ὧδ ἔτι πάλιν ἔνδον νυν οὕτως αὑτῷ ὁμοῦ ποτε'
prepositions = 'περ ἄνευ εἰς ἐν ὡς πρὸς ἐκ ἐπ ἐπὶ ἐς ἐξ ὑπὸ ἀμφὶ ὅπως ὑπ πάρα ἀπὸ πάρα ξὺν δι κατὰ κατ παρ ἀπ διὰ σύν τἀπὶ σὺν περι'
subjunctions = 'εἰ ἢ καὶ τε ἐπεὶ εἴ ἔτ καί πρὶν ὅτ ὅταν ὥστε εἴπερ ὅτι ὥσπερ ἵν'
base_verbs = 'ἦν ὢν'
noise_and_names = 'ελενη Ὀδυσσευς Κρεουσα Ἡρακλης Θησευς Τειρεσίας Τεῦκρος Κῆρυξ Ἄρης Δαρεῖος Ἑρμῆς Δαναός Χορός Κασάνδρα Κλυταιμήστρα Ἠλέκτρα Προμηθεύς Ὀρέστης Ἀπόλλων Ἀντιγόνη Κασάνδρα Ἄτοσσα Βασιλεύς Ἐτεοκλής Ἰσμήνη Ἄγγελος Ξέρξης'
singles = 'μ σ θ γ τ'
noise_terms = articles + ' ' + pronouns + ' ' + particles + ' ' + adverbs + ' ' + articles + ' ' + prepositions + ' ' + subjunctions + ' ' + base_verbs + ' ' + noise_and_names + ' ' + singles

def removeNoise(query_string, noise_terms):
  noise_terms = dediacritcializer.dediacriticalizer(noise_terms)
  noise_terms = noise_terms.strip()
  noise_terms = noise_terms.split()
  for term in noise_terms:
    query_string = re.sub(rf'\b{term}\b', '', query_string)
  query_string = re.sub('\s\s+', ' ', query_string)
  return query_string