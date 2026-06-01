import matplotlib.pyplot as plt

#Tempo de conexión total (ms)
f, ax = plt.subplots()
Cs = ['m5a', 'c6id']
x1=[1, 5]
x2=[2, 6]
x4=[3, 7]
#y1 = [46.824, 69, 21.33]
y1 = [46.824, 30.156]
y2 = [69, 69]
y4 = [21.33, 14.086]
#y2 = [30.156, 69, 14.086]
#y4 = [30.156, 69, 14.086]

plot1 = ax.bar(x1, y1, label='N=1')
plot2 = ax.bar(x2, y2, label='N=2')
plot3 = ax.bar(x4, y4, label='N=4')

ax.bar_label(plot1, label_type='edge', size='x-large')
ax.bar_label(plot2, label_type='edge', size='x-large')
ax.bar_label(plot3, label_type='edge', size='x-large')
plt.xticks(ticks=x2, labels=Cs, size='x-large')
ax.legend(fontsize='x-large')
#x label
plt.xlabel('Clúster HPC', size='x-large')
#y label
plt.ylabel('Tiempo de ejecución (s)', size='x-large')
#title
plt.title('Tiempo de ejecución para el kernel MG (clase C)', size='xx-large')
plt.show()
