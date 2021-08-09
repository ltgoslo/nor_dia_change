#! python3

import sys
from smart_open import open


def check_word(token, pos, nofunc=None, nopunct=True, noshort=True, stopwords=None):
    outword = '_'.join([token, pos])
    if nofunc:
        if pos in nofunc:
            return None
    if nopunct:
        if pos == 'PUNCT':
            return None
    if stopwords:
        if token in stopwords:
            return None
    if noshort:
        if len(token) < 2:
            return None
    return outword


def num_replace(word):
    newtoken = 'x' * len(word)
    nw = newtoken + '_NUM'
    return nw


def clean_token(token, misc):
    """
    :param token:
    :param misc:
    :return:
    """
    out_token = token.strip().replace(' ', '')
    if token == 'Файл' and 'SpaceAfter=No' in misc:
        return None
    return out_token


def clean_lemma(lemma, pos, lowercase=True):
    """
    :param lowercase:
    :param lemma:
    :param pos:
    :return:
    """
    out_lemma = lemma.strip().replace(' ', '').replace('_', '')
    if lowercase:
        out_lemma = out_lemma.lower()
    if '|' in out_lemma or out_lemma.endswith('.jpg') or out_lemma.endswith('.png'):
        return None
    if pos != 'PUNCT':
        if out_lemma.startswith('«') or out_lemma.startswith('»'):
            out_lemma = ''.join(out_lemma[1:])
        if out_lemma.endswith('«') or out_lemma.endswith('»'):
            out_lemma = ''.join(out_lemma[:-1])
        if out_lemma.endswith('!') or out_lemma.endswith('?') or out_lemma.endswith(',') \
                or out_lemma.endswith('.'):
            out_lemma = ''.join(out_lemma[:-1])
    return out_lemma


def extract_proper(source_file, outfile, sentencebreaks=True, entities=None, lowercase=True):
    """
    :param lowercase:
    :param source_file:
    :param outfile:
    :param sentencebreaks:
    :param entities:
    :return:
    """
    if entities is None:
        entities = {'PROPN'}
    print('Processing CONLLU input %s...' % source_file, file=sys.stderr)
    print('Writing lemmas to %s...' % outfile, file=sys.stderr)
    tempfile0 = open(outfile, 'a')

    nr_lines = 0
    named = False
    memory = []
    mem_case = None
    mem_number = None
    current_sentence = None

    for line in open(source_file, 'r'):
        if line.startswith('#'):
            if line.startswith('# text ='):
                current_sentence = line.strip()[9:]
            continue
        if not line.strip():
            if sentencebreaks:
                tempfile0.write('\t' + current_sentence + '\n')
            named = False
            if memory:
                past_lemma = '::'.join(memory)
                memory = []
                tempfile0.write(past_lemma + '_PROPN ')  # Lemmas and POS tags
            continue
        res = line.strip().split('\t')
        if len(res) != 10:
            continue
        (word_id, token, lemma, pos, xpos, feats, head, deprel, deps, misc) = res
        nr_lines += 1
        token = clean_token(token, misc)
        if lowercase:
            lemma = clean_lemma(lemma, pos)
        else:
            lemma = clean_lemma(lemma, pos, lowercase=False)
        if not lemma or not token:
            continue
        if pos in entities:
            if '|' not in feats:
                tempfile0.write('%s_%s ' % (lemma, pos))  # Lemmas and POS tags
                continue
            morph = {el.split('=')[0]: el.split('=')[1] for el in feats.split('|')}
            if 'Case' not in morph or 'Number' not in morph:
                tempfile0.write('%s_%s ' % (lemma, pos))  # Lemmas and POS tags
                continue
            if not named:
                named = True
                mem_case = morph['Case']
                mem_number = morph['Number']
            if morph['Case'] == mem_case and morph['Number'] == mem_number:
                memory.append(lemma)
                if 'SpacesAfter=\\n' in misc or 'SpacesAfter=\s\\n' in misc:
                    named = False
                    past_lemma = '::'.join(memory)
                    memory = []
                    tempfile0.write(past_lemma + '_PROPN ')  # Lemmas and POS tags
            else:
                named = False
                past_lemma = '::'.join(memory)
                memory = []
                tempfile0.write(past_lemma + '_PROPN ')  # Lemmas and POS tags
                tempfile0.write('%s_%s ' % (lemma, pos))  # Lemmas and POS tags
        else:
            if not named:
                tempfile0.write('%s_%s ' % (lemma, pos))  # Lemmas and POS tags
            else:
                named = False
                past_lemma = '::'.join(memory)
                memory = []
                tempfile0.write(past_lemma + '_PROPN ')  # Lemmas and POS tags
                tempfile0.write('%s_%s ' % (lemma, pos))  # Lemmas and POS tags
    tempfile0.close()
    return nr_lines
