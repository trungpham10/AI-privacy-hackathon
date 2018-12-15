import numpy as np
import pandas as pd

# Create the data matrix
data2 = {'id': np.array(all_ids2),
        'is_minor':np.array(is_minor_all2),
        'is_geo_location':np.array(is_geo_location_all2),
        'email':np.array(email_all2),
        'is_vendor':np.array(is_vendor_all2),
        'sell_data':np.array(sell_data_all2),
        'not_sell_data':np.array(not_sell_data_all2),
        'share_data':np.array(share_data_all2),
        'not_share_data':np.array(not_share_data_all2),
        'is_cookies':np.array(is_cookies_all2),
        'smog_index':np.array(smog_index_all2),
        'fog_index':np.array(gunning_fog_all2),
        'avg_sentence_length':np.array(avg_sentence_length_all2),
        'flesch_reading_ease':np.array(flesch_reading_ease_all2),
        'dale_chall_reading_score':np.array(dale_chall_readability_score_all2),
#        'score_all':np.array(score_all),
        }

#data2 = {'id': np.array(all_ids2),
#         'email':np.array(email_all2),
#         'is_vendor':np.array(is_vendor_all2),
#         'not_share_data':np.array(not_share_data_all2),
#         'smog_index':np.array(smog_index_all2),
#        }

df2 = pd.DataFrame(data2)
#print(df.head(n=10))

#df2 = pd.DataFrame(data2)
#
#from sklearn import preprocessing
#
#x = df.values #returns a numpy array
#min_max_scaler = preprocessing.MinMaxScaler()
#x_scaled = min_max_scaler.fit_transform(x)
#df = pd.DataFrame(x_scaled)
#
#print(df.head(n=10))