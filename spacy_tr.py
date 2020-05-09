"""A wrapper around spacy cli tools for injecting the extended Turkish data

train cli bunun üstünden çalıştırılınca Kendi TurkishDefault modelim çalışacak
"""

import sys
import plac
from spacy import cli, util
from tr.tr import Turkish


if __name__ == '__main__':
    util.set_lang_class('tr', Turkish)

    command_name = sys.argv[1].replace('-', '_')
    command = getattr(cli, command_name)
    plac.call(command, sys.argv[2:])