'''
Process Data
'''
import numpy as np
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LogisticRegression,LinearRegression
from sklearn import svm, linear_model
from sklearn.svm import SVC
from sklearn.metrics import f1_score,classification_report,confusion_matrix
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.cluster import KMeans

#X = df_normalize.iloc[:,0:15]
#X = df_normalize[[0,1,2,3,4,9,10,11,12,13,14]]
X = df_normalize[[3,4,8,10,11,12,13,14]]
y = df_normalize['score_all']

# Split into training and testing
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3,
                                                    random_state=42)

# Apply a ML classifier to the training set
logmodel = LogisticRegression(random_state=0,C=1e5,solver='lbfgs',
                         multi_class='multinomial')
lm = LinearRegression()
knn = KNeighborsClassifier(n_neighbors=1)
dtree = DecisionTreeClassifier()
model = SVC()
kmeans = KMeans(n_clusters=10)

# Fit the model on data
logmodel.fit(X_train, y_train)
lm.fit(X_train, y_train)
knn.fit(X_train, y_train)
dtree.fit(X_train, y_train)
model.fit(X_train,y_train)
kmeans.fit(X_train,y_train)

# Predictions
predictions = knn.predict(X_test)
pred2 = knn.predict(df2_normalize[[3,4,8,10,11,12,13,14]])

# Use F-1 score to access the performance of the classifier
print(f1_score(y_test, predictions, average='macro'))
#print(classification_report(y_test,predictions))
#print(confusion_matrix(y_test,predictions))

# =============================================================================
# BEST RESULT:
# knn_macro features [3,4,8,(10),11,(12),(14)]: 93.41% 
# knn_macro features [3,4,8,(10),11,(12),13,14]: 92.67% 
# knn_macro features [3,8,11,13,14]: 87.5% 
# knn_macro 85.47%
# dtree_macro 80.46%
# model_micro 54.96%
# =============================================================================
