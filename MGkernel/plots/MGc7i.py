import matplotlib.pyplot as plt

#Tempo de conexión total (ms)
f, ax = plt.subplots()
Cs = ['m5a', 'c7i', 'm5a', 'c7i', 'm5a', 'c7i','m5a', 'c7i', 'm5a', 'c7i']
x1=[1, 2, 4, 5, 7, 8, 10, 11, 13, 14]

y1 = [46.412, 36.14]
y2 = [38.836, 27.988]
y4 = [20.434, 15.224]
y8 = [8.916, 7.724]
y16 = [5.146, 4.69]

plot1 = ax.bar(x1[0:2], y1, label='N=1')
plot2 = ax.bar(x1[2:4], y2, label='N=2')
plot3 = ax.bar(x1[4:6], y4, label='N=4')
plot4 = ax.bar(x1[6:8], y8, label='N=8')
plot5 = ax.bar(x1[8:10], y16, label='N=16')

ax.bar_label(plot1, label_type='edge', size='x-large')
ax.bar_label(plot2, label_type='edge', size='x-large')
ax.bar_label(plot3, label_type='edge', size='x-large')
ax.bar_label(plot4, label_type='edge', size='x-large')
ax.bar_label(plot5, label_type='edge', size='x-large')

plt.xticks(ticks=x1, labels=Cs, size='x-large')
ax.legend(fontsize='x-large')
#x label
plt.xlabel('Tipo de instancia (dentro de clúster HPC)', size='x-large')
#y label
plt.ylabel('Tiempo de ejecución (s)', size='x-large')
#title
plt.title('Tiempo de ejecución para el kernel MG (clase C)', size='xx-large')
plt.show()
