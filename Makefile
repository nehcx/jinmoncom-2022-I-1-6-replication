build_bitext:
	cd src;	python make_bitext.py -s ../data/hachidaishu/hachidai.db -t ../data/translations/allTranslations.txt -o ../cache/bitexts.csv
build_metacode2lemma_dict:
	cd src;	python make_metacode2lemma.py -f ../data/hachidaishu/hachidai.db -o ../cache/metacode2lemma_src.pkl -t source; python make_metacode2lemma.py -f ../data/translations/allTranslations.txt -o ../cache/metacode2lemma_tar.pkl -t target
train_save_ibm2:
	cd src; python train_save_model.py -c ../cache/bitexts.csv -f ibm2_fwd.model -b ibm2_bwd.model -m ibm2
test_class:
	cd test; python test_bitexts.py
save_db:
	cd src; python bitexts.py -o ../cache/bitexts.db -m ibm2 -t kaneko katagiri kojimaarai komachiya kubota kyusojin matsuda okumura ozawa takeoka
basic_stat:
	cd src; python stat.py
accuracy:
	cd src; python accuracy.py

ARGS := $(wordlist 2,$(words $(MAKECMDGOALS)),$(MAKECMDGOALS))
$(eval $(ARGS):;@:)
plot:
	cd src; python visualize.py -w $(ARGS) -b translator
