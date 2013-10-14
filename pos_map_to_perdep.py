#! /usr/bin/python
# -*- coding:utf-8 -*-

"""
PerlexとPerDepは若干，違うPOSの体系を採用している．このため，PerlexのタグをPerDep用にマップを行う．
"""

__author__='Kensuke Mitsuzawa';
__date__='2013/10/14';

import sys, codecs, re, json;

def load_wordset():
    with codecs.open('./wordset.json', 'r', 'utf-8') as f:
        wordset_dic=json.load(f);

    return wordset_dic;

def map_pos(wordset_dic, word, information_tuple):
    N_ANM=wordset_dic['N_ANM'];
    N_IANM=wordset_dic['N_IANM'];
    V_ACT=wordset_dic['V_ACT'];
    V_PASS=wordset_dic['V_PASS'];
    PRENUM_set=wordset_dic['PRENUM']

    pos=information_tuple[0];
    category_info=information_tuple[1];
    inflection_info=information_tuple[2];

    if pos==u'ADJ':
        if re.findall(ur'Cmp.*', inflection_info):
            target_tuple=(u'ADJ', u'AJCM');
        elif re.findall(ur'Sup.*', inflection_info):
            target_tuple=(u'ADJ', u'AJSUP');
        
        elif re.findall(ur'@ORD', inflection_info):
            target_tuple=(u'PRENUM', u'PRENUM');

        else:
            target_tuple=(u'ADJ', u'AJP');

    elif pos==u'N':
        number=None;
        if re.findall(ur'Sing.*', inflection_info):
            number=u'SING';
        elif re.findall(ur'Plur', inflection_info):
            number=u'PLUR';

        if word in N_ANM:
            target_tuple=(u'N', u'ANM', number);
        elif word in N_IANM:
            target_tuple=(u'N', u'IANM', number);
        else:
            target_tuple=(u'N', u'N', number);

    elif pos==u'V':
        number=None;
        person=None;
        if re.findall(ur'sg', inflection_info):
            number=u'SING';
        elif re.findall(ur'Plur', inflection_info):
            number=u'PLUR';

        if re.findall(ur'1p', inflection_info):
            person=u'1';
        elif re.findall(ur'2p', inflection_info):
            person=u'2';
        elif re.findall(ur'3p', inflection_info):
            person=u'3';

        if word in V_PASS:
            target_tuple=(u'V', u'PASS', (number, person));
        elif word in V_ACT:
            target_tuple=(u'V', u'ACT', (number, person));
        else:
            target_tuple=(u'V', u'V', (number, person))

    if pos==u'INTexcel':
        target_tuple=(u'ADR', u'ADR');

    if pos==u'CON':
        if category_info in [u'CONJ', u'ADVcond', u'ADVrel', u'ADVcoord']:
            target_tuple=(u'CONJ', u'CONJ');

        if category_info==u'SUBR':
            target_tuple=(u'SUBR', u'SUBR');

    #IDENは未実装

    elif pos==u'ADV':
        if category_info==u'PART':
            target_tuple=(u'PART', u'PART');
        
        else:
            target_tuple=(u'ADV', u'SADV');

    elif pos==u'DETquant':
        if word in PRENUM_set:
            target_tuple=(u'PRENUM', u'PRENUM');

        elif re.findall(ur'[0-9]+', word):
            target_tuple=(u'PRENUM', u'PRENUM');

        else:
            target_tuple=(u'PREM', u'QUAJ');

    elif pos==u'P':
        if category_info==u'POSTP':
            target_tuple=(u'POSTP', u'POSTP');

        else:
            target_tuple=(u'PREP', u'PREP');

    elif pos==u'PROpers':
        target_tuple=(u'PR', u'SEPER');

    elif pos==u'PROindef':
        target_tuple=(u'PR', u'SEPER');

    elif pos==u'PROdem':
        target_tuple=(u'PR', u'PROdem');

    elif pos==u'PROinter':
        target_tuple=(u'PR', u'INTG');

    elif pos==u'PROrefl':
        if word==u'xwd': 
            target_tuple=(u'PR', u'CREFX');
        else:
            target_tuple=(u'PR', u'UCREFX');

    elif pos==u'DETdem':
        target_tuple=(u'PREM', u'DEMAJ');

    elif pos==u'DET':
        if category_info==u'EXAJ':
            target_tuple=(u'PREM', u'EXAJ');

        elif category_info==u'QUAJ':
            target_tuple=(u'PREM', u'QUAJ');

        elif category_info==u'AMBAJ':
            target_tuple=(u'PREM', u'AMBAJ');

    elif pos==u'DELM':
        target_tuple=(u'PUNC', u'PUNC');

    return target_tuple;

def main(word, information_tuple):
    wordset_dic=load_wordset();
    target_tuple=map_pos(wordset_dic, word, information_tuple);
    
    return target_tuple
if __name__==u'__main__':
    main(u'5', (u'DETquant', u'DETquant', u''));
