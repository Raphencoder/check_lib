#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Ce module va verifier l'objet recu en parametre. Il faut que ca soit une
    liste de dictionnaire ou une liste de string. Si c'est une liste de dict
    on verifie que chaque dictionnaire continent bien les premiers et second
    arguments en keys.
"""
__version__="0.0.1"
from .core import check_obj
