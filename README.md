preprocess_PerDep
=================

#日本語説明

##ファイルの説明
*  annotation_to_conll.py:annotation用のフォーマットからCoNLL Dep.のフォーマットに変換するスクリプト  
*  pos_map_to_perdep.py:perlexのPOSをperdepのPOSにマップするスクリプト  
*  check_words_in_pos.py:perdepで，各POSの中にどんな語が属しているのか？を知りたい時に使う．
*  pos_index_dictionary.json:上のスクリプトで使うjsonファイル．make_pos_index_json.pyにより生成する．  
*  calc_entry_number_treebank.py:perdepをもし語彙辞書として用いたならば，項目数はどれくらいだろう？という疑問で書いたスクリプト  
*  wordset.json:POSのマップを行う際に，表層単語を見ないと分類できない場合が多々ある．そのためにつくったjsonファイル．pos_map_to_perdepで使う．  
*  make_specific_wordset.py:上のjsonファイルを作るスクリプト  
*  treebank/:perdepツリーバンクのローマ字化したファイルだけを保存するディレクトリ  
*  crf_format:CRF++で利用するためのフォーマットファイル  
*  conll_format:CoNLL Dependency Parsingのフォーマットファイルを保存  
*  test_corpus:口承文芸コーパスのannotationフォーマットを保存するディレクトリ  
*  python_virastart:アラビア文字とローマ字の相互変換スクリプト
*  annotation_to_crf.py:CRF++でPOSタグ付けに利用できるフォーマットに出力するスクリプト  



##Document in English

I'll write later.  
