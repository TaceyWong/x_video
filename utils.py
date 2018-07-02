# coding:utf-8

"""
utils.py
:
by tacey@AtomPai on 18-7-2
"""

import os
import shutil

def check_path(file_path):
    if os.path.exists(file_path):
        if os.path.isdir(file_path):
            shutil.rmtree(file_path)
        else:
            os.remove(file_path)


def get_font_list():
    fonts = []
    for font_path in ["/Library/Fonts", os.path.expanduser("~/Library/Fonts")]:
        if os.path.isdir(font_path):
            fonts.extend(
                [os.path.join(font_path, cur_font)
                 for cur_font in os.listdir(font_path)
                ]
            )
    return fonts
