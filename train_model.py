import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

data ={
    "experience":[1,2,3,4,5],
    "salary":[10000,20000,30000,40000,50000]
}

df = pd.DataFrame(data)

x= df[["experience"]]
y= df[["salary"]]

model = LinearRegression()
model.fit(x,y)

pickle.dump(model,open('model.pk1','wb'))

print("Model trained and saved.")