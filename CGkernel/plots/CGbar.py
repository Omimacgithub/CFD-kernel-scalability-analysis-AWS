import matplotlib.pyplot as plt

#Tempo de conexión total (ms)
f, ax = plt.subplots()
Cs = ['HTC', 'HPC']
x1=[1, 7]
x2=[2, 8]
x4=[3, 9]
x8=[4, 10]
x16=[5, 11]

y1 = [227.018, 229.662]
y2 = [201.196, 202.92]
y4 = [103.616, 106.176]
y8 = [32.714, 31.486]
y16 = [22.228, 18.156]

plot1 = ax.bar(x1, y1, label='N=1')
plot2 = ax.bar(x2, y2, label='N=2')
plot3 = ax.bar(x4, y4, label='N=4')
plot4 = ax.bar(x8, y8, label='N=8')
plot5 = ax.bar(x16, y16, label='N=16')

ax.bar_label(plot1, label_type='edge', size='x-large')
ax.bar_label(plot2, label_type='edge', size='x-large')
ax.bar_label(plot3, label_type='edge', size='x-large')
ax.bar_label(plot4, label_type='edge', size='x-large')
ax.bar_label(plot5, label_type='edge', size='x-large')

plt.xticks(ticks=x4, labels=Cs, size='x-large')
ax.legend(fontsize='x-large')
#x label
plt.xlabel('Tipo de clúster', size='x-large')
#y label
plt.ylabel('Tiempo de ejecución (s)', size='x-large')
#title
plt.title('Tiempo de ejecución para el kernel CG (clase C)', size='xx-large')
plt.show()
