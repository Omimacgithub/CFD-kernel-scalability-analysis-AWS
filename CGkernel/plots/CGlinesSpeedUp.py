import matplotlib.pyplot as plt

#f, ax = plt.subplots()
Cs = ['HTC', 'HPC']

#Speed up
x = [1, 2, 4, 8, 16]
yt = [0, 1.128, 2.191, 6.939, 10.213]
yp = [0, 1.132, 2.163, 7.294, 12.649]

plot1 = plt.scatter(x, yt, label='HTC')
plot2 = plt.scatter(x, yp, label='HPC')
plt.plot(x, yt, linestyle='-', linewidth=2)
plt.plot(x, yp, linestyle='--', linewidth=2)
plt.legend(fontsize='x-large')
#x label
plt.xlabel('Nº de cores', size='x-large')
#y label
plt.ylabel('Speed up', size='x-large')
#title
plt.title('Speed up para el kernel CG (clase C)', size='xx-large')
plt.show()

#Eficiencia paralela
yt = [0, 0.564, 0.548, 0.867, 0.638]
yp = [0, 0.566, 0.541, 0.912, 0.791]

plot1 = plt.scatter(x, yt, label='HTC')
plot2 = plt.scatter(x, yp, label='HPC')
plt.plot(x, yt, linestyle='-', linewidth=2)
plt.plot(x, yp, linestyle='--', linewidth=2)
#plt.plot(x, yt, '-o'), labels=Cs)
plt.legend(fontsize='x-large')
#x label
plt.xlabel('Nº de cores', size='x-large')
#y label
plt.ylabel('Eficiencia paralela', size='x-large')
#title
plt.title('Eficiencia paralela para el kernel CG (clase C)', size='xx-large')
plt.show()
