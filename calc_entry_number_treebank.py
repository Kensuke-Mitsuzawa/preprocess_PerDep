#! /usr/bin/python
# -*- coding:utf-8 -*-

"""
PerDep treebankを辞書として用いることを想定して，語項目数を計上するスクリプト．
表層語が同じでもcoarse_pos, fine_posが異なれば，別のentryとして登録する
"""

__author__='Kensuke Mitsuzawa';
__date__='2013/10/13';

import codecs, sys, re, json;

entry_list=[];
with codecs.open('./treebank/train.conll.roman', 'r', 'utf-8') as lines:
    for line in lines:
        if line==u'\n' or line==u'\r\n':
            pass
        
        else:
            try:
                items=line.split(u'\t');
                word=items[1]; coarse_pos=items[3]; fine_pos=items[4];

                word_pos_tuple=(word, coarse_pos, fine_pos);
                entry_list.append(word_pos_tuple);

            except IndexError:
                print 'Error line\n{}'.format([line])

num_entry=len(entry_list);
print 'The num. of entry is {}'.format(num_entry);
