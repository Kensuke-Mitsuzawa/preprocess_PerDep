#! /usr/bin/python
# -*- coding:utf-8 -*-

import sys, codecs, re, json;

__author__='Kensuke Mitsuzawa';
__date__='2013/10/13';

"""
Persian Depedency Treebank中の特定のPOSに属する単語を調べるためのスクリプト

ARGS: COARSE_POS_NAME FINE_POS_NAME
"""


with codecs.open('./pos_index_dictionary.json', 'r', 'utf-8') as f:
    pos_index_dictionary=json.load(f);

if len(sys.argv)==2:
    target_pos=sys.argv[1].decode('utf-8');

    word_list=pos_index_dictionary[target_pos]
    for item in word_list:
        print '{}\t{}'.format(item[0].encode('utf-8'), item[1].encode('utf-8') );

elif len(sys.argv)==3:
    target_pos=sys.argv[1].decode('utf-8');
    target_pos_sub=sys.argv[2].decode('utf-8');

    word_list=pos_index_dictionary[target_pos];
    for item in word_list:
        if item[1]==target_pos_sub:
            print '{}\t{}'.format(item[0].encode('utf-8'), item[1].encode('utf-8'));
