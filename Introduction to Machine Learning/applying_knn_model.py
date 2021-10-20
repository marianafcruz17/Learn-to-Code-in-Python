from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier(n_neighbors=1)

x = iris.data
y = iris.target
knn.fit(x,y)

print(knn.predict([ [5.1,3.5,1.4,0.2] ]))
