import spacy
from spacy.matcher import Matcher
#from spacy import cli, util
#from spacy.language import Language
#from spacy.lang.tr import Turkish, TurkishDefaults
#from tag_map import TAG_MAP

#nlp = spacy.load("models/model-cc-md/model-best")
nlp = spacy.load("tr_model0") #packaged model

#nlp = spacy.load('tr-models/model-best', disable=['tagger', 'parser', 'ner']) #to add tagger later
#nlp = Language().from_disk('tr-models/model-best')
#nlp = l.from_disk('tr-models/model-best')
#nlp = Turkish() #no pos

#nlp.Defaults.tag_map = TAG_MAP
#nlp.Defaults = tr_defaults

#ValueError: [E109] Model for component 'tagger' not initialized. Did you forget to load a model, or forget to call begin_training()?
# tagger = nlp.create_pipe("tagger")
# for tag, values in TAG_MAP.items():
#     tagger.add_label(tag, values)
# nlp.add_pipe(tagger)

text0 = 'Kendileriyle 19. görüştüğümden edindiğim izlenim, "gazeteciye verilen bilgilerle" alakasız bir haberin kere yayımlanmış olduğudur.'
text = "Karşısında, pantolonu dizlerine dek ıslak, önlük torbası ham eriklerle dolu İbrahim dikiliyordu."
text1= "Bu İstanbul'dan bir test cümlesidir. Hayır değildir."
#doc = nlp(text)

# for token in doc:
# 	print(f"{token.is_sent_start} - {token.text:{30}} - {token.lemma_:{20}} - {token.pos_:{5}} - {token.tag_:{5}} - {token.dep_:{5}} ")

#pipe test:
batch_array = [(text0, 0), (text, 1), (text1, 2)]
#docs = list(nlp.pipe(texts))
for nlp_doc, doc_id in nlp.pipe(batch_array, as_tuples=True, batch_size=2):
	for token in nlp_doc:
		print(f"{token.is_sent_start} - {token.text:{30}} - {token.lemma_:{20}} - {token.pos_:{5}} - {token.tag_:{5}} - {token.dep_:{5}} ")

	matcherForW = Matcher(nlp.vocab)
	matcherForW.add("MoneyW", None, *[
		[{'POS': 'VERB'}, {'POS': 'NOUN'}]
	])
	matches = matcherForW(nlp_doc)	
	for (match_id, start, end) in matches:
		print(match_id, start, end, nlp_doc[start:end])

