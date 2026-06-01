import matplotlib.pyplot as plt

#f, ax = plt.subplots()
Cs = ['m5a', 'c7i']

#Speed up
x = [1, 2, 4, 8, 16]
yt = [0, 1.195, 2.271, 5.205, 9.019]
yp = [0, 1.291, 2.374, 4.679, 7.706]

plot1 = plt.scatter(x, yt, label='m5a')
plot2 = plt.scatter(x, yp, label='c7i')
plt.plot(x, yt, linestyle='-', linewidth=2)
plt.plot(x, yp, linestyle='--', linewidth=2)
plt.legend(fontsize='x-large')
#x label
plt.xlabel('Nº de cores', size='x-large')
#y label
plt.ylabel('Speed up', size='x-large')
#title
plt.title('Speed up para el kernel MG (clase C)', size='xx-large')
plt.show()

#Eficiencia paralela
yt = [0, 0.598, 0.568, 0.568, 0.564]
yp = [0, 0.646, 0.593, 0.585, 0.482]

plot1 = plt.scatter(x, yt, label='m5a')
plot2 = plt.scatter(x, yp, label='c7i')
plt.plot(x, yt, linestyle='-', linewidth=2)
plt.plot(x, yp, linestyle='--', linewidth=2)
#plt.plot(x, yt, '-o'), labels=Cs)
plt.legend(fontsize='x-large')
#x label
plt.xlabel('Nº de cores', size='x-large')
#y label
plt.ylabel('Eficiencia paralela', size='x-large')
#title
plt.title('Eficiencia paralela para el kernel MG (clase C)', size='xx-large')
plt.show()
