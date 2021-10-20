from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x,y,test_Size=0.25)
print(x_train)
print(x_test.shape)

knn.fit(x_train,y_train)
predictions = knn.predict(x_test)
print(predictions)

print(y_test)

from sklearns import metrics

performance = metrics.accuracy_score(y_test,predictions)
print(performance)
