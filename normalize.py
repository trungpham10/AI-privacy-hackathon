### Normalize the data matrix and add labels

from sklearn import preprocessing

#x = df.values[:,1:14] #returns a numpy array
#x = df.values
#min_max_scaler = preprocessing.MinMaxScaler()
#x_scaled = min_max_scaler.fit_transform(x)
#df_normalize = pd.DataFrame(x_scaled)
#
##print(df.head(n=10))
#df_normalize['score_all'] = score_all

#
x2 = df2.values
min_max_scaler2 = preprocessing.MinMaxScaler()
x_scaled2 = min_max_scaler2.fit_transform(x2)
df2_normalize = pd.DataFrame(x_scaled2)

#print(df.head(n=10))
#df2_normalize['score_all'] = score_all