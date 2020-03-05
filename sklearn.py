fibonacci=[0,1,1,2,3,5,8,13,21,34,55,89,144]
import numpy as np
from sklearn import preprocessing

label = np.array(range(13))
#print(label)

# scalling
features = preprocessing.scale(fibonacci)
print(label,features)

#splitting into testing and training data
fron sklearn inport model_selection
(x_train,x_test,y_train,y_test) = \

model_selection.train_test_split(features,label)
print("train features ",x_train,'\n train label',\
    y_train,'\n test features',x_test,'\ntest label',y_test)

y_train= x_train.reshape(-1,1)
#print(x_train)
x_test= x_test.reshape(-1,1)

# calculation of linear regression
from sklearn import linear_model
linear_regression = linear_model.LinearRegression()
model= linear_regression.fit(x_train,y_train)
x_test_new=model.predict(x_test)
print(y_test_new)
print(y_test)
#model.predict(x_test)

# scoreprediction 
print(modwl.score(x_test,y_test))
