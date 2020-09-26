#!/bin/bash

CORPUS=$1

mkdir -p data
git clone https://github.com/hyperreality/American-British-English-Translator
python3 gen_british_american_english_dataset.py \
    --american-wordlist American-British-English-Translator/data/american_spellings.json \
    --british-wordlist American-British-English-Translator/data/british_spellings.json \
    --output-british data/british.txt \
    --output-american data/american.txt \
    --corpus $CORPUS \
    --n 4000
rm -r American-British-English-Translator
