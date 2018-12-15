import os
import re
from text_analysis import sell_data,not_sell_data,share_data,not_share_data,gunning_fog,smog_index,avg_sentence_length,flesch_reading_ease,dale_chall_readability_score 

filelistall = os.listdir(os.getcwd())

filelist = filter(lambda x: x.endswith(".txt"),filelistall)

# Get all text of 434 files into all_text
all_text = []
all_ids = []
for filename in filelist:
    f = open(filename,"r")
    number = float(filename[8:-4])
    all_ids.append(number)
    text = ''.join(f.readlines())
    all_text.append(text)
    f.close()

### Process all features for all files
is_minor_all = []
is_how_collect_all = []
is_geo_location_all = []
email_all = []
is_vendor_all = []
not_sell_data_all = []
sell_data_all = []
share_data_all = []
not_share_data_all = []
is_cookies_all = []
gunning_fog_all = []
smog_index_all = []
avg_sentence_length_all = []
flesch_reading_ease_all = []
dale_chall_readability_score_all = []

# Run through each file for each feature
for i in range(len(all_text)):
    is_minor_all.append(is_minor(all_text[i]))
    is_how_collect_all.append(is_how_collect(all_text[i]))
    is_geo_location_all.append(is_geo_location(all_text[i]))
    email_all.append(email(all_text[i]))
    is_vendor_all.append(is_vendor(all_text[i]))
    not_sell_data_all.append(not_sell_data(all_text[i]))
    sell_data_all.append(sell_data(all_text[i]))
    not_share_data_all.append(not_share_data(all_text[i]))
    share_data_all.append(share_data(all_text[i]))
    is_cookies_all.append(is_cookies(all_text[i]))
    gunning_fog_all.append(gunning_fog(all_text[i]))
    smog_index_all.append(smog_index(all_text[i]))
    avg_sentence_length_all.append(avg_sentence_length(all_text[i]))
    flesch_reading_ease_all.append(flesch_reading_ease(all_text[i]))
    dale_chall_readability_score_all.append(dale_chall_readability_score(all_text[i]))
    print(len(email_all))
#print(not_share_data_all)
#    print(np.array(gunning_fog_all))
#    print(np.array(smog_index_all))
#    print(np.array(avg_sentence_length_all))
#    print(np.array(flesch_reading_ease_all))
#    print(np.array(dale_chall_readability_score_all))    
    
# Create DATA MATRIX