from __future__ import unicode_literals

from tr.tokenizer_exceptions import TOKENIZER_EXCEPTIONS
from tr.tag_map import TAG_MAP
from tr.stop_words import STOP_WORDS

from spacy.lang.tokenizer_exceptions import BASE_EXCEPTIONS
from spacy.lang.norm_exceptions import BASE_NORMS
from spacy.language import Language
from spacy.attrs import LANG, NORM
from spacy.util import update_exc, add_lookups


class TurkishDefaults(Language.Defaults):
    lex_attr_getters = dict(Language.Defaults.lex_attr_getters)
	#lex_attr_getters.update(LEX_ATTRS)
    lex_attr_getters[LANG] = lambda text: "tr"
    lex_attr_getters[NORM] = add_lookups(
        Language.Defaults.lex_attr_getters[NORM], BASE_NORMS
    )
    tokenizer_exceptions = update_exc(BASE_EXCEPTIONS, TOKENIZER_EXCEPTIONS)
    tag_map = TAG_MAP
    stop_words = STOP_WORDS
	#syntax_iterators = SYNTAX_ITERATORS

class Turkish(Language):
    lang = "tr"
    Defaults = TurkishDefaults


__all__ = ["Turkish"]