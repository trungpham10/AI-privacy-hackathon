# import text-processing libraries
import nltk
import spacy
import pandas as pd
import numpy as np
import re
from textstat.textstat import textstatistics, easy_word_set, legacy_round 
# read data from text file
#with open('document1060.txt') as f:
#    content = f.readlines()
#
## Convert dict to string 
#text = ''.join(content)
#asdfasdf
# Splits the text into sentences, using 
# Spacy's sentence segmentation which can 
# be found at https://spacy.io/usage/spacy-101 
def is_minor(text):
    match = re.search(r'minor',text)
    if match:
        return 1
    else: 
        return 0
    
def is_how_collect(text):
    match = re.search(r'how_collect',text)
    if match:
        return 1
    else: 
        return 0
    
def is_geo_location(text):
    match = re.search(r'geo-location',text)
    if match:
        return 1
    else: 
        return 0

def email(text):
    match = re.search(r'\S+@\S+',text)
    if match:
        return 1
    else:
        return 0

def is_vendor(text):
    match = re.search(r'vendor',text)
    if match:
        return 1
    else: 
        return 0


def break_sentences(text): 
    nlp = spacy.load('en') 
    doc = nlp(text) 
    sentences = [sent.string.strip() for sent in doc.sents]
    return sentences 

# Returns Number of Words in the text 
def word_count(text): 
    sentences = break_sentences(text) 
    words = 0
    for sentence in sentences: 
        words += len([token for token in sentence]) 
    return words 

# Returns the number of sentences in the text 
def sentence_count(text): 
    sentences = break_sentences(text) 
    return len(sentences) 

# Returns average sentence length 
def avg_sentence_length(text): 
    words = word_count(text) 
    sentences = sentence_count(text) 
    average_sentence_length = float(words / sentences) 
    return average_sentence_length 

def syllables_count(word): 
    return textstatistics().syllable_count(str(word)) 

# Returns the average number of syllables per 
# word in the text 
def avg_syllables_per_word(text): 
    syllable = syllables_count(text) 
    words = word_count(text) 
    ASPW = float(syllable) / float(words) 
    return legacy_round(ASPW, 1) 

# Return total Difficult Words in a text 
def difficult_words(text): 

    # Find all words in the text 
    words = [] 
    sentences = break_sentences(text) 
    for sentence in sentences: 
        words += [token for token in sentence] 

    # difficult words are those with syllables >= 2 
    # easy_word_set is provide by Textstat as 
    # a list of common words 
    diff_words_set = set() 
    
    for word in words: 
        syllable_count = syllables_count(word) 
        if word not in easy_word_set and syllable_count >= 2: 
            diff_words_set.add(word) 

    return len(diff_words_set) 

# A word is polysyllablic if it has more than 3 syllables 
# this functions returns the number of all such words 
# present in the text 
def poly_syllable_count(text): 
    count = 0
    words = [] 
    sentences = break_sentences(text) 
    for sentence in sentences: 
        words += [token for token in sentence] 


    for word in words: 
        syllable_count = syllables_count(word)
        if syllable_count >= 3: 
            count += 1
    return count 

def flesch_reading_ease(text): 
    """ 
        Implements Flesch Formula: 
        Reading Ease score = 206.835 - (1.015 × ASL) - (84.6 × ASW) 
        Here, 
        ASL = average sentence length (number of words 
            divided by number of sentences) 
            ASW = average word length in syllables (number of syllables 
            divided by number of words) 
    """
    FRE = 206.835 - float(1.015 * avg_sentence_length(text)) -float(84.6 * avg_syllables_per_word(text)) 
    return legacy_round(FRE, 2) 

def gunning_fog(text): 
    per_diff_words = (difficult_words(text) / word_count(text) * 100) + 5
    grade = 0.4 * (avg_sentence_length(text) + per_diff_words) 
    return grade 

def smog_index(text): 
    """ 
        Implements SMOG Formula / Grading 
        SMOG grading = 3 + ?polysyllable count. 
        Here, polysyllable count = number of words of more 
        than two syllables in a sample of 30 sentences. 
    """

    if sentence_count(text) >= 3: 
        poly_syllab = poly_syllable_count(text) 
        SMOG = (1.043 * (30*(poly_syllab / sentence_count(text)))**0.5) + 3.1291
        return legacy_round(SMOG, 1) 
    else: 
        return 0
    
# =============================================================================
# block comment is Ctrl+4
# =============================================================================


def dale_chall_readability_score(text): 
    """ 
        Implements Dale Challe Formula: 
        Raw score = 0.1579*(PDW) + 0.0496*(ASL) + 3.6365 
        Here, PDW = Percentage of difficult words. ASL = Average sentence length 
    """
    words = word_count(text) 
    # Number of words not termed as difficult words 
    count = words - difficult_words(text) 
    if words > 0: 

        # Percentage of words not on difficult word list 
        per = float(count) / float(words) * 100

    # diff_words stores percentage of difficult words 
    diff_words = 100 - per 

    raw_score = (0.1579 * diff_words) + (0.0496 * avg_sentence_length(text)) 

    # If Percentage of Difficult Words is greater than 5 %, then; 
    # Adjusted Score = Raw Score + 3.6365, 
    # otherwise Adjusted Score = Raw Score 

    if diff_words > 5:

        raw_score += 3.6365

    return legacy_round(raw_score, 2) 



from spacy.matcher import PhraseMatcher
nlp = spacy.blank('en')
matcher = PhraseMatcher(nlp.vocab)

def not_sell_data(text):
    terminology_list1 = ['not sell']
    patterns = [nlp(text) for text in terminology_list1]
    matcher.add('TerminologyList', None, *patterns)
    matches = matcher(nlp(text))
    if matches:
        return 1
    else:
        return 0
    
def sell_data(text):
    terminology_list = ['sell']
    patterns = [nlp(text) for text in terminology_list]
    matcher.add('TerminologyList', None, *patterns)
    matches = matcher(nlp(text))
    if matches:
        return 1
    else:
        return 0
    
def share_data(text):
    terminology_list2 = ['share']
    patterns = [nlp(text) for text in terminology_list2]
    matcher.add('TerminologyList', None, *patterns)
    matches = matcher(nlp(text))
    if matches:
        return 1
    else:
        return 0

def not_share_data(text):
    terminology_list3 = ['not share']
    patterns = [nlp(text) for text in terminology_list3]
    matcher.add('TerminologyList', None, *patterns)
    matches = matcher(nlp(text))
    if matches:
        return 1
    else:
        return 0
    
def is_cookies(text):
    match = re.search(r'cookies',text)
    if match:
        return 1
    else: 
        return 0
    
# Create dataframe with features
#import os
#
## create the list containing all files from the current dir
#filelistall = os.listdir(os.getcwd())
#
## create the list containing only data files end with ".txt" 
#filelist = filter(lambda x: x.endswith('.txt'), filelistall)

# Get all IDs 
#all_ids = []
#for filename in filelist:
##   print(filename)
#   f = open(filename, "r")
#   number = float(filename[8:-4])
#   all_ids.append(number)
#   f.close()

# Function: get features list for each text file
def features_list(ids):
    pass
   
# Get features for each file
#all_text=[]
#for filename in filelist:
##    print(filename)
#    f = open(filename,"r")
##    print(f)
#    content = f.readlines()
##    print(content)
#    text = ''.join(content)
#    all_text.append(text)
#    f.close()

# Create the data matrix
#data = {'id': all_ids,
#        'is_minor':['minor' in text],
#        'is_how_collect':['how_collect' in text],
#        'is_geo-location':['geo-location' in text],
#        'email':[],
#        'is_not_sell':[],
#        'is_sell':[],
#        'is_share':[],
#        'is_not_share':[],
#        'is_vendor':['vendor' in text],
#        'is_cookies':['cookies' in text],
#        'gunning_fog':[gunning_fog(text)],
#        'smog_index':[smog_index(text)],
#        'avg_sentence_length':[avg_sentence_length(text)],
#        'flesch_reading_ease':[flesch_reading_ease(text)],
#        'dale_chall_readability_score':[dale_chall_readability_score(text)]
#        }

#df = pd.DataFrame(data)
#df = pd.DataFrame(np.array(all_ids),columns=["ids"])
