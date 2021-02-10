#!/bin/python3

import re


def validate_html(html):
    '''
    this function performs a limited version of html validation by
    checking whether every opening tag has a corresponding closing tag.
    >>> validate_html('<strong>example</strong>')
    True
    >>> validate_html('<strong>example')
    False
    '''
    stack = []
    tags = _extract_tags(html)

    for tag in tags:
        if not tag.startswith("</"):
            stack.append(tag)
        else:
            if len(stack) == 0:
                return False
            if stack[-1][1:] == tag[2:]:
                stack.pop()
    return len(stack) == 0

    # HINT:
    # use the _extract_tags function below to generate a list of
    # html tags without any extra text;
    # then process these html tags using the balanced parentheses
    # algorithm from the book
    # the main difference between your code and the book's code will
    # be that you will have to keep track of not just the 3 types of
    # parentheses,
    # but arbitrary text located between the html tags


def _extract_tags(html):

    '''
    This is a helper function for `validate_html`.
    By convention in Python, helper functions that are not meant
    to be used directly by the user are prefixed with an underscore.

    This function returns a list of all the html tags contained in
    the input string, stripping out all text not contained within
    angle brackets.

    >>> _extract_tags('Python <strong>rocks</strong>!')
    ['<strong>', '</strong>']
    '''

    return list(re.findall(r'<[^>]+>', html))
