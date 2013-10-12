#! /usr/bin/python
# -*- coding:utf-8 -*-

__author__='Kensuke Mitsuzawa';
__date__='2013/10/13';

import codecs, sys, re, json;

word_pos_dict={};
with codecs.open('./treebank/train.conll.roman', 'r', 'utf-8') as lines:
    for line in lines:
        if line==u'\n' or line==u'\r\n':
            pass
        
        else:
            try:
                items=line.split(u'\t');
                word=items[1]; coarse_pos=items[3]; fine_pos=items[4];

                if coarse_pos in word_pos_dict:
                    word_list=word_pos_dict[coarse_pos];
                    if (word, fine_pos) not in word_list:
                        word_pos_dict[coarse_pos].append( (word, fine_pos) );
                
                else:
                    word_pos_dict.setdefault(coarse_pos, [(word, fine_pos)]);


            except IndexError:
                print 'Error line\n{}'.format([line])

with codecs.open('./pos_index_dictionary.json', 'w', 'utf-8') as f:
    json.dump(word_pos_dict, f, indent=4, ensure_ascii=False);
f.close();
