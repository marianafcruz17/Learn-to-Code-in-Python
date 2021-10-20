from sklearn.linear_model import LogisticRegression

logreg = LogisticRegression()
logreg.fit(x_train,y_train)
print(logreg.predict([[6.7,3.3,5.7,2.5]]))

predictions_logreg = logreg.predict(x_test)
performance_logreg = metrics.accuracy_Score(y_test,predictions_logreg)
print(performance_logreg)

