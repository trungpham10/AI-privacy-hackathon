import pandas as pd

### Read csv file to return the score features

data = pd.read_csv("training_labels.csv")

score_all = []
for i in all_ids:
    index = data.index[data['id']==i].tolist()[0]
    score = data['score'][index]
    score_all.append(score)
#print(score_all)