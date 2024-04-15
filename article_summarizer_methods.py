def sentence_length(sentence):
    '''
    Returns the count of words in a spaCy sentence while omitting punctuation and whitespace tokens
    --------------------------
    1. sentence - a spaCy parsed sentence object
    '''
    count = 0
    for token in sentence:
        #filter out tokens that are not words, but keep stopwords:
        if not(token.is_space or token.is_punct):
            count += 1
    return count

###############################################################################


def score_sentence_by_token(sentence, interesting_tokens):
    '''
    Returns the porportion of frequency of interesting tokens to the total words in a sentence.  Return value is a float.
    -------------------------

    1. sentence - a spaCy parsed sentence object

    2. interesting_tokens - a python set of 1 or more tokens the user wants to observe.

    -------------------------
    '''
    # find length of sentence
    length = sentence_length(sentence)

    # Find count of interesting tokens in sentence
    interesting_token_count = 0
    for token in sentence:
        if token.text.lower() in interesting_tokens:
            interesting_token_count += 1
    
    # print(f"{length=}")
    # print(f"{interesting_token_count=}")

    score = interesting_token_count / length
    return score

###############################################################################

def score_sentence_by_lemma(sentence, interesting_lemmas):
    '''
    Returns the porportion of frequency of interesting lemmas to the total words in a sentence.  Return value is a float.
    -------------------------

    1. sentence - a spaCy parsed sentence object

    2. interesting_lemmas - a python set of 1 or more lemmas the user wants to observe. Care should be taken to make these are lemmas

    -------------------------
    '''
    # find length of sentence
    length = sentence_length(sentence)

    # Find count of interesting tokens in sentence
    interesting_lemma_count = 0

    for token in sentence:
        if token.lemma_.lower() in interesting_lemmas:
            interesting_lemma_count += 1

    # print(f"{length=}")
    # print(f"{interesting_lemma_count=}")
    
    score = interesting_lemma_count / length
    return score


#####################################################################