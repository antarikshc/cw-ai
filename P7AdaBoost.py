import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction import DictVectorizer
from sklearn.ensemble import AdaBoostClassifier

data = pd.read_csv('data.csv')
cols_to_retain = ['Alt','Bar','Fri','Hun','Pat','Price','Rain','Res','Type','Est']

X_feature = data[cols_to_retain]
X_dict = X_feature.T.to_dict().values()

# Turn list of dicts into a numpy array
vect = DictVectorizer(sparse=False)
X_vector = vect.fit_transform(X_dict)
print(X_vector)

X_Train = X_vector[:-1]
X_Test = X_vector[-1:]
print('Train set')
print(X_Train)
print('test set')
print(X_Test)

# Used to vectorize the class label
le = LabelEncoder()
y_train = le.fit_transform(data['Goal'][:-1])

scaler = StandardScaler()
scaler.fit(X_Train)

X_train = scaler.transform(X_Train)
X_test = scaler.transform(X_Test)

model = AdaBoostClassifier(random_state=1)
model.fit(X_train, y_train)

print(model.predict(X_test))