import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

df=pd.read_csv("week.csv")
x=df.iloc[:,:-1].values
y=df.iloc[:,-1].values

knn=KNeighborsClassifier(n_neighbors=5)
knn.fit(x,y)

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3)
print("Accuracy: ",knn.score(x_test,y_test))

new=[[5.2,2.8],[5.6,2.7],[4.9 , 2.4]]
predict=knn.predict(new)
print("Predict:",predict)

