#! /usr/bin/python
# -*- coding:utf-8 -*-

__author__='Kensuke Mitsuzawa';
__date__='2013/10/14';

"""
名詞と動詞の分類は，表層単語をみないことにはFine-POSのクラスに分類できない．
そのために，wordsetを構築する．
出力はjsonファイル
"""


import codecs, sys, re, json;

N_ANM_set=[];
N_IANM_set=[];
V_ACT_set=[];
V_PASS_set=[];
PRENUM_set=[];

with codecs.open('./treebank/train.conll.roman', 'r', 'utf-8') as lines:
    for line in lines:
        if line==u'\n' or line==u'\r\n':
            pass
        
        else:
            try:
                items=line.split(u'\t');
                word=items[1]; coarse_pos=items[3]; fine_pos=items[4];

                if coarse_pos=='N' and fine_pos=='ANM':
                    N_ANM_set.append( word );

                elif coarse_pos=='N' and fine_pos=='IANM':
                    N_IANM_set.append(word);

                if coarse_pos=='V' and fine_pos=='ACT':
                    V_ACT_set.append(word);

                elif coarse_pos=='V' and fine_pos=='PASS':
                    V_PASS_set.append(word);

                if coarse_pos==u'PRENUM':
                    PRENUM_set.append(word);

            except IndexError:
                print 'Error line\n{}'.format([line])

wordset_dic={'N_ANM':N_ANM_set,\
             'N_IANM':N_IANM_set,\
             'V_ACT':V_ACT_set,\
             'V_PASS':V_PASS_set,\
             'PRENUM':PRENUM_set};

with codecs.open('./wordset.json', 'w', 'utf-8') as f:
    json.dump(wordset_dic, f, indent=4, ensure_ascii=False);

