k_values = ()
k = 1

while k<= 25:
    knn =  NeighborsClassifier(n_neighbors=k)
    knn.fit(x_train,y_train)
    predictions = knn.predict(x_test)
    performance = metrics.accuracy_score(y_test,predictions)
    k_values[k] = round(performance,4)
    k += 1

print(k_values)

import matplotlib.pyplot as plt
imatplot inline

plt.plot(list(k_values.keys()),list(k_values.values())
plt.xlabel("Values of K")
plt.ylabel = ("Performance")
plt.show()
