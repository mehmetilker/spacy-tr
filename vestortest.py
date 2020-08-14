import spacy


def vector_convert():
	from gensim.models import Word2Vec, KeyedVectors   
	from gensim.test.utils import datapath

	#model = Word2Vec.load(r"C:\Users\imete\spacy-tr\vectors\CoNLL17-w2vec\model.bin")
	#model.wv.save_word2vec_format('modeltest.txt', binary=False)

	wv_from_bin = KeyedVectors.load_word2vec_format(datapath(r"vectors/_org-files/model.bin"), binary=True)
	wv_from_bin.wv.save_word2vec_format('model-tr.txt', binary=False)

def vector_test():
	#nlp = spacy.load("vectors/tr_vectors_cc_sm")
	nlp = spacy.load("vectors/tr_vectors_cc_md")
	#nlp = spacy.load("vectors/tr_vectors_cc_lg")
	#nlp = spacy.load("vectors/tr_vectors_wiki_lg")


	doc1 = nlp("Ben buraya gelirken oraya uğradım.")
	doc2 = nlp("Ben buraya gelirken oraya uğramadım.")
	x = doc1.similarity(doc2)
	print(x)

	doc1 = nlp("geldim")
	doc2 = nlp("geliyorum")
	x = doc1.similarity(doc2)
	print(x):
