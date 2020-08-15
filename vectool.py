import spacy


def vector_convert():
	from gensim.models import Word2Vec, KeyedVectors   
	from gensim.test.utils import datapath

	#model = Word2Vec.load(r"C:\Users\imete\spacy-tr\vectors\CoNLL17-w2vec\model.bin")
	#model.wv.save_word2vec_format('modeltest.txt', binary=False)

	#wv_from_bin = KeyedVectors.load_word2vec_format(datapath(r"./vectors/_org-files/model.bin"), binary=True, limit=100000)
	f = r"./vectors/_org-files/cc.tr.300.vec.gz"
	f = r"./vectors/_org-files/CoNLL17-w2vec/model.bin"
	wv_from_bin = KeyedVectors.load_word2vec_format(f, binary=True)
	
	
	#wv_from_bin.wv.save_word2vec_format('./vectors/_org-files/model-tr.txt', binary=False)
	print("vocab size:", len(wv_from_bin.vocab))
	print("index2entity size:", len(wv_from_bin.index2entity))
	print("most freq:", wv_from_bin.index2entity[:150])
	for item in wv_from_bin.index2entity[:20]:
		print(wv_from_bin.vocab[item].count)

	print("most sim:", wv_from_bin.most_similar(["istanbul"]))
	print("most sim:", wv_from_bin.most_similar(["kolay"]))

def vector_test():
	#nlp = spacy.load("vectors/tr_vectors_cc_sm")
	nlp = spacy.load("vectors/tr_vectors_cc_20K")
	#nlp = spacy.load("vectors/tr_vectors_cc_lg")
	#nlp = spacy.load("vectors/tr_vectors_wiki_lg")


	doc1 = nlp("Ben buraya gelirken oraya uğradım.")
	doc2 = nlp("Ben buraya gelirken oraya uğramadım.")
	x = doc1.similarity(doc2)
	print(x)

	doc1 = nlp("istanbul")
	doc2 = nlp("ankara")
	x = doc1.similarity(doc2)
	print(x)

	doc1 = nlp("basit")
	doc2 = nlp("kolay")
	x = doc1.similarity(doc2)
	print(x)

vector_convert()
#vector_test()