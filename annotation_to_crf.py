#! /usr/bin/python
# -*- coding:utf-8 -*-

"""
annotated用のフォーマットからCRF++のフォーマットへ変換する．
ARGS: アノテーションフォーマットのコーパスファイルパス CFR化したコーパスの保存先パス

TODO:stemの部分をValencey Lexicon for Persian Verbsで代用できるようにがんばる
https://github.com/rasoolims/PersianVerbAnalyzer/
"""
import sys, codecs, re;
import pos_map_to_perdep;

__author__='Kensuke Mitsuzawa';
__date__='2013/10/17';

def crf_format(annotated_corpus_path):
    wordset_dic=pos_map_to_perdep.load_wordset();
    with codecs.open(annotated_corpus_path, 'r', 'utf-8') as lines:
        crf_format_stack=[];
        crf_format_stack_layer2=[];
        for line in lines:
            if line[0]==u'#' or line==u'\n':
                pass;

            else:
                if line==u'!end\n':
                    crf_format_stack.append( (u'\n', u'\n') );
                    crf_format_stack_layer2.append( (u'\n', u'\n') );

                else:
                    token_sent_id, features=line.strip(u'\n').split(u'\t');
                    
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
                            if perdep_information_tuple[2]==None:
                                print u'Warning! the number feature for N is None. It must be something mistaken';

                        elif perdep_information_tuple[0]==u'V':
                            number_info=u'number={}'.format(perdep_information_tuple[2][0]);
                            person_info=u'person={}'.format(perdep_information_tuple[2][1]);
                            tma_info=u'tma={}'.format(perdep_information_tuple[2][2]);


                    
                    crf_token_format_layer1_gold=u'{} {}\n'.format(surface, perdep_information_tuple[0]);
                    crf_token_format_layer1_test=u'{}\n'.format(surface);


                    crf_token_format_layer2_gold=u'{} {} {}\n'.format(surface,\
                                                               perdep_information_tuple[0],\
                                                               perdep_information_tuple[1]);
                    crf_token_format_layer2_test=u'{} {}\n'.format(surface, perdep_information_tuple[0]);


                    crf_format_stack.append( (crf_token_format_layer1_test, crf_token_format_layer1_gold) );
                    crf_format_stack_layer2.append( (crf_token_format_layer2_test, crf_token_format_layer2_gold) );

    return crf_format_stack, crf_format_stack_layer2;

def main(annotated_corpus_path, crf_file_path):
    crf_format_stack, crf_format_stack_layer2=crf_format(annotated_corpus_path);

    crf_dir='./crf_format/'
    gold_f=codecs.open(crf_dir+'layer_1/'+crf_file_path+'.gold', 'w', 'utf-8');
    with codecs.open(crf_dir+'layer_1/'+crf_file_path+'.test', 'w', 'utf-8') as f:
        for item in crf_format_stack:
            f.write(item[0]);
            gold_f.write(item[1]);
    f.close();
    gold_f.close();

    gold_f=codecs.open(crf_dir+'layer_2/'+crf_file_path+'.gold', 'w', 'utf-8');
    with codecs.open(crf_dir+'layer_2/'+crf_file_path+'.test', 'w', 'utf-8') as f:
        for item in crf_format_stack_layer2:
            f.write(item[0]);
            gold_f.write(item[1]);
    f.close();
    gold_f.close();

if __name__=='__main__':
    annotated_corpus_path='./test_corpus/e1998t0001.annotation_2nd.validated';
    crf_file_path='test'
    main(annotated_corpus_path, crf_file_path);
