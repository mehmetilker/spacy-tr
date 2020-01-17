# coding: utf8
from __future__ import unicode_literals


# from ...symbols import POS, PUNCT, SYM, ADJ, NUM, DET, ADV, ADP, X, VERB
# from ...symbols import NOUN, PROPN, PART, INTJ, SPACE, PRON, SCONJ, AUX, CONJ

from spacy.symbols import POS, PUNCT, SYM, ADJ, NUM, DET, ADV, ADP, X, VERB
from spacy.symbols import NOUN, PROPN, PART, INTJ, SPACE, PRON, SCONJ, AUX, CONJ, CCONJ, INTJ


# fmt: off
TAG_MAP = {
    # "ADJ___": {"morph": "_", POS: ADJ},
    # "ADJ__AdpType=Prep": {"morph": "AdpType=Prep", POS: ADJ},
    # "ADJ__AdpType=Preppron|Gender=Masc|Number=Sing": {"morph": "AdpType=Preppron|Gender=Masc|Number=Sing", POS: ADV},
    # "ADJ__AdvType=Tim": {"morph": "AdvType=Tim", POS: ADJ},
    # "ADJ__Gender=Fem|Number=Plur": {"morph": "Gender=Fem|Number=Plur", POS: ADJ},
    # "ADJ__Gender=Fem|Number=Plur|NumType=Ord": {"morph": "Gender=Fem|Number=Plur|NumType=Ord", POS: ADJ},
    # "ADJ__Gender=Fem|Number=Plur|VerbForm=Part": {"morph": "Gender=Fem|Number=Plur|VerbForm=Part", POS: ADJ},
    # "ADJ__Gender=Fem|Number=Sing": {"morph": "Gender=Fem|Number=Sing", POS: ADJ},

    #Ordered by POS

    'NAdj': {POS: ADJ},
    'Adj': {POS: ADJ},
    'Adverb': {POS: ADV},
    'Det': {POS: DET},
    'Num': {POS: NUM},
    'ANum': {POS: NUM},
    'NNum': {POS: NUM},
	'Noun': {POS: NOUN},
    'Pron': {POS: PRON},
    'Reflex': {POS: PRON}, ##kendini	kendi	PRON	Reflex
    'Prop': {POS: PROPN}, #Erdoğan'ın	Erdoğan	PROPN	Prop
    'Abr': {POS: PROPN}, #CHP	CHP	PROPN	Abr
    #'Propn': {POS: PROPN}, #no examples
    'Punc': {POS: PUNCT},
	'Verb': {POS: VERB},
    'Neg': {POS: VERB}, #değilse	değil	VERB	Neg
    'Foreign': {POS: X},

    'Dup': {POS: X}, #pörçük	pörçük	X	Dup
    
    
    
    'PCAcc': {POS: ADP}, #aşkın	aşkın	ADP	PCAcc
    'PCAbl': {POS: ADP}, #sonra	sonra	ADP	PCAbl
    'PCGen': {POS: ADP}, #kadar	kadar	ADP	PCGen
    'PCDat': {POS: ADP}, #kadar	kadar	ADP	PCDat
    'PCIns': {POS: ADP}, #birlikte	birlikte	ADP	PCIns
    'PCNom': {POS: ADP}, #için	için	ADP	PCNom
    'With': {POS: ADP}, #lı	li	ADP	With
    'Without': {POS: ADP}, #siz	siz	ADP	Without
    'Rel': {POS: ADP}, #ki	ki	ADP	Rel
    'Ness': {POS: ADP}, #lık	lik	ADP	Ness
    'Since': {POS: ADP}, #dır	dir	ADP	Since

    'Zero': {POS: AUX}, #sa	i	AUX	Zero / mış	i	AUX	Zero
    'Postp': {POS: AUX}, #ise	i	AUX	Postp
    'Conj': {POS: CCONJ}, #ve	ve	CCONJ	Conj
    'Interj': {POS: INTJ}, #Ah	ah	INTJ	Interj
    'Quant': {POS: PRON}, #hiçbiri	PRON	Quant
    'Pers': {POS: PRON}, #Ona	o	PRON	Pers
    'Demons': {POS: PRON}, #bunların	bu	PRON	Demons
    'Ques': {POS: PRON}, #Ne	ne	PRON	Ques
    
    #'PART': {POS: PART}, #no examples
    #'SCONJ': {POS: SCONJ}, #no examples
    #'SYM': {POS: SYM},#no examples
    

}

#    "tagger":[
#   
#       "PCAbl",
#       "PCAcc",
#       "PCDat",
#       "PCGen",
#       "PCIns",
#       "PCNom",
#       "Postp",
#       "Quant",
#       "Ques",
#       "Reflex",
#       "Rel",
#       "Since",
#       "With",
#       "Without",
#       "Zero",
#       "_SP"
#     ],

# fmt: on
