import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

df=pd.read_csv('week.csv')
x=df.iloc[:,:-1].values
y=df.iloc[:,-1].values

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=42)

cl=KNeighborsClassifier(n_neighbors=9)
cl.fit(x_train,y_train)

print("Accuracy: ",cl.score(x_test,y_test))

pred=[[5.2,2.8],[5.6,2.7],[4.9 , 2.4]]

predict=cl.predict(pred)
print(predict)


    



    
    
   
    
    
    



    
    
   
    

