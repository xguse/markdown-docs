# pandoc.py is part of the 'markdown-docs' package.
# It was written by Gus Dunn and was created on 12/29/14.
# 
# Please see the license info in the root folder of this package.

"""
=================================================
pandoc.py
=================================================
Purpose:

"""
__author__ = 'Gus Dunn'


import re


def citekeys_from_latex_cite_command(cite_string):
    """
    Returns list of citekeys.

    :param cite_string:
    :type cite_string:
    :return:
    :rtype:
    """
    assert isinstance(cite_string, str)

    return cite_string.lstrip('\cite{').rstrip('}').split(',')


def citekeys_to_pandoc_cite_command(citekeys):
    """
    Returns a pandoc citation command with given citekeys.

    :param citekeys:
    :type citekeys:
    :return:
    :rtype:
    """
    assert isinstance(citekeys, list)

    decorate = lambda x: "@{}".format(x)

    cite_command = '; '.join([decorate(key) for key in citekeys])

    return "[{}]".format(cite_command)


def cite_latex_to_pandoc(text):
    """
    Returns a string that has had a replacement operation applied converting latex form
    citations to pandoc form.
    :param string:
    :type string:
    :return:
    :rtype:
    """
    assert isinstance(text, str)

    lcite = re.compile('\\\cite\{[^\{]+\}')

    latex_cites = list(set(lcite.findall(text)))

    new_text = text
    for cite in latex_cites:
        keys = citekeys_from_latex_cite_command(cite)
        pandoc_cite = citekeys_to_pandoc_cite_command(keys)
        new_text = new_text.replace(cite, pandoc_cite)

    return new_text


