import matplotlib.pyplot as plt

x = [1,2,3,4]
y = [1500,1200,1100,1800]
legend = ["January","February","March","April"]

plt.plot(x,y)
plt.show()

plt.plot(x,legend)
plt.show()

plt.bar(x,y)
plt.ylabel("Sales in US$")
plt.title("Monthly Sales")
plt.show()


