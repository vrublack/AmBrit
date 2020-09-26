import argparse
import json


def read_wordlist(path):
    with open(path, encoding='utf8') as f:
        l = json.load(f)
    return l.keys()


def contains_word(wordlist, sentence):
    for word in sentence:
        if word in wordlist:
            return True
    return False


def main(args):
    british_wordlist = read_wordlist(args.british_wordlist)
    american_wordlist = read_wordlist(args.american_wordlist)

    n_british, n_american = 0, 0
    with open(args.corpus, encoding='utf8') as f, \
            open(args.output_british, 'w', encoding='utf8') as out_british, \
            open(args.output_american, 'w', encoding='utf8') as out_american:
        for line in f:
            sentence = line.rstrip().split(' ')
            contains_british, contains_american = contains_word(british_wordlist, sentence), contains_word(
                american_wordlist, sentence)
            if contains_british and not contains_american and n_british < args.n:
                n_british += 1
                out_british.write(line)
            elif not contains_british and contains_american and n_american < args.n:
                n_american += 1
                out_american.write(line)

            if n_british == args.n and n_american == args.n:
                break


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--british-wordlist')
    parser.add_argument('--american-wordlist')
    parser.add_argument('--corpus', help='Tokenized corpus')
    parser.add_argument('--n', type=int, help='How many sentence per dialect to extract')
    parser.add_argument('--output-british')
    parser.add_argument('--output-american')
    main(parser.parse_args())
