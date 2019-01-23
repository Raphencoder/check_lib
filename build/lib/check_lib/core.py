#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Verification des objets passés en parametre

    Usage:

    >>> from check_lib import check_obj
    >>> check_obj(obj, first, second)
"""

def check_obj(obj, first, second):
    if type(obj) == list:
        type_obj = type(obj[0])
    else:
        return {"error": "WRONG_PARAMETERS", "note": "check_obj need an list argument"}
    if type_obj == dict:
        return check_dict(obj, first, second)
    if type_obj == str:
        return check_list(obj)
    return {"error": "WRONG_PARAMETERS", "note": "check_obj need an list of string or list of dict"}

def check_dict(obj, first_element, second_element):
    check = []
    for dico in obj:
        check.append(dico.get(first_element, 'errorDico'))
        check.append(dico.get(second_element, 'errorDico'))
    if 'errorDico' in check or check == []:
        return {"error": "WRONG_PARAMETERS", "note": "check_dict need a list argument type [{'"+first_element+"': 'PRP', '"+second_element+"': Ceci}]"}
    return True

def check_list(obj):
    if not all(isinstance(token, str) for token in obj):
        return {"error": "WRONG_PARAMETERS", "note": "check_list need a string argument"}
    return True


if __name__ == "__main__":
    check_obj()
