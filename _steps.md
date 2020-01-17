# Training steps

https://universaldependencies.org/treebanks/tr_imst/index.html
https://github.com/UniversalDependencies/docs/blob/pages-source/_tr/index.md

http://coltekin.github.io/gk-treebank/

http://coltekin.github.io/gk-treebank/pos/
Part of speech tags

http://coltekin.github.io/gk-treebank/feat/
Morphological features
Animacy, Aspect, Case

http://coltekin.github.io/gk-treebank/dep/
Dependencies

## Links to train

https://github.com/explosion/spaCy/tree/master/spacy/lang/tr
https://github.com/UniversalDependencies/UD_Turkish-IMST

https://spacy.io/usage/training#basics
https://spacy.io/usage/saving-loading#basics
https://spacy.io/usage/adding-languages#tag-map

https://spacy.io/api/cli#pretrain
https://spacy.io/api/cli#train

Other language examples:
https://github.com/aajanki/spacy-fi
https://github.com/ipipan/spacy-pl
https://github.com/buriy/spacy-ru


Adding models for new languages master thread
https://github.com/explosion/spaCy/issues/3056

https://stackoverflow.com/questions/56779217/train-spacys-existing-pos-tagger-with-my-own-training-examples
adding tag_map after loading language model

previous try:
https://github.com/explosion/spaCy/issues/3056#issuecomment-470068902

-----------------------------------------------------------------------------------------------

## Steps to train from UD dataset

git clone https://github.com/UniversalDependencies/UD_Turkish-IMST
mkdir imst-json
py -m spacy convert UD_Turkish-IMST/tr_imst-ud-train.conllu imst-json
py -m spacy convert UD_Turkish-IMST/tr_imst-ud-dev.conllu imst-json
(To create)
The spacy convert CLI command has an argument that specifies whether to merge morphological features with the coarse-grained POS tags, 
to make the fine-grained tags. If this is set differently than the tag_map is expecting, you might see the error you're experiencing.
https://github.com/explosion/spaCy/issues/2503
py -m spacy convert UD_Turkish-IMST/tr_imst-ud-train.conllu imst-json-m --morphology

### Debug

py -m spacy debug-data tr imst-json\tr_imst-ud-train.json imst-json\tr_imst-ud-dev.json

### Train

mkdir tr-models
py -m spacy train tr tr-models imst-json/tr_imst-ud-train.json imst-json/tr_imst-ud-dev.json
>tag_map i dikkate alarak (tr folder) tarining
py spacy_tr.py train tr models\model1 imst-json\tr_imst-ud-train.json imst-json\tr_imst-ud-dev.json --pipeline tagger,parser


### Package

py -m spacy package tr-models/model-best tr-models/_x
python setup.py sdist
pip install tr-models\_x\tr_model0-0.0.0\dist\tr_model0-0.0.0.tar.gz

Train cmd details:
python -m spacy train [lang] [output_path] [train_path] [dev_path]
[--base-model] [--pipeline] [--vectors] [--n-iter] [--n-early-stopping]
[--n-examples] [--use-gpu] [--version] [--meta-path] [--init-tok2vec]
[--parser-multitasks] [--entity-multitasks] [--gold-preproc] [--noise-level]
[--orth-variant-level] [--learn-tokens] [--textcat-arch] [--textcat-multilabel]
[--textcat-positive-label] [--verbose]