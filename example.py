#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
""" text_colors version 0.8.3 """

import text_colors

SHELL: str = text_colors.py_shell()


def main():

    text_colors.color_print(text_colors.FG_DICT(
        'PURPLEHAZE'), 'Jimmi sang a fabulous song.')
    text_colors.c
