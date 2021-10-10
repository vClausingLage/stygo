from cltk.languages.pipelines import GreekPipeline
a_pipeline = GreekPipeline()
from cltk.stem.lemma import LemmaReplacer
sentence = 'τὰ γὰρ πρὸ αὐτῶν καὶ τὰ ἔτι παλαίτερα σαφῶς μὲν εὑρεῖν διὰ χρόνου πλῆθος ἀδύνατα ἦν'
lemmatizer = LemmaReplacer('greek')

print(a_pipeline.description)

lemmatizer.lemmatize(sentence)