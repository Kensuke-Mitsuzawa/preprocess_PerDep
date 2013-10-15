#! /usr/bin/python
# -*- coding:utf-8 -*-

import sys, codecs, re;
import pos_map_to_perdep;

__author__='Kensuke Mitsuzawa';
__date__='2013/10/15';

def conll_format(annotated_corpus_path):
    wordset_dic=pos_map_to_perdep.load_wordset();
    with codecs.open(annotated_corpus_path, 'r', 'utf-8') as lines:
        conll_format_stack=[];
        for line in lines:
            if line[0]==u'#' or line==u'\n':
                pass;

            else:
                if line==u'!end\n':
                    conll_format_stack.append(u'\n');

                else:
                    token_sent_id, features=line.strip(u'\n').split(u'\t');
                    tokenid, sentid=token_sent_id.split(u'@');
                    
                    surface, POS, stem, tag, category, inflection, blank=features.split(u'|');
                    stem=re.sub(ur'_+[1-9]', u'', stem);
                    stem=re.sub(ur'_*MTE', u'', stem);

                    information_tuple=(POS, category, inflection);
                    perdep_information_tuple=pos_map_to_perdep.map_pos(wordset_dic,\
                                                                       surface,\
                                                                       information_tuple);
                    coarse_pos=perdep_information_tuple[0];
                    fine_pos=perdep_information_tuple[1];
                   
                    #結果がNoneのときのチェック用に残しておく
                    if perdep_information_tuple==None:
                        print information_tuple;
                        print surface;

                    if len(perdep_information_tuple)==3:
                        if perdep_information_tuple[0]==u'N':
                            feature_column=u'attachment=ISO|number={}'.format(perdep_information_tuple[2]);
                            if perdep_information_tuple[2]==None:
                                print u'Warning! the number feature for N is None. It must be something mistaken';

                        elif perdep_information_tuple[0]==u'V':
                            number_info=u'number={}'.format(perdep_information_tuple[2][0]);
                            person_info=u'person={}'.format(perdep_information_tuple[2][1]);
                            tma_info=u'tma={}'.format(perdep_information_tuple[2][2]);
                  

                            feature_column=person_info+u'|attachment=ISO|'+number_info+u'|'+tma_info;   
                            feature_column=re.sub(ur'^person=None\|', u'', feature_column);
                            feature_column=re.sub(ur'\|number=None', u'', feature_column);
                            feature_column=re.sub(ur'\|tma=None', u'', feature_column);

                    #attachment=ISOはこのバージョンでのみ有効
                    else:
                            feature_column=u'attachment=ISO';

                    
                    conll_token_format=u'{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}\t{8}\t{9}\n'\
                            .format(tokenid,surface,stem,coarse_pos,fine_pos,feature_column,u'',u'',u'_', u'_');

                    conll_format_stack.append(conll_token_format);

    return conll_format_stack;

def main(annotated_corpus_path, conll_file_path):
    conll_format_stack=conll_format(annotated_corpus_path);
    with codecs.open(conll_file_path, 'w', 'utf-8') as f:
        for item in conll_format_stack:
            f.write(item);
    f.close();

if __name__=='__main__':
    annotated_corpus_path='./test_corpus/e1998t0001.annotation_2nd.validated';
    conll_file_path='./test'
    main(annotated_corpus_path, conll_file_path);





