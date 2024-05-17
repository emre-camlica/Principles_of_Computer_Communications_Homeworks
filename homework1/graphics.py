import numpy as np
import matplotlib.pyplot as plt

arrays=[]

with open('averages_distance_ordered.txt', 'r') as file:
    for i in range(10):
        array=[]
        for i in range(12):
            line = file.readline()
            row = [float(x) for x in line.strip().split('\t')]
            array.append(row)
        arrays.append(array)

x1=[]
y1=[]
x2=[]
y2=[]
x3=[]
y3=[]

for i in range(10):
    row=np.mean(arrays[i],axis=0)
    y1.append(row)


x1=[0.1, 4, 15, 49, 351, 578, 1060, 2486, 4545, 10803]
y1=np.transpose(y1)

plt.plot(x1, y1[0], label=f'RTT1')
plt.plot(x1, y1[1], label=f'RTT2')
plt.plot(x1, y1[2], label=f'RTT3')

# Customize the plot
plt.xlabel('Distance(km)')
plt.ylabel('Delays (ms)')
plt.title('Delays vs Distance')
plt.legend()

# Show the plots
plt.show()

y2=np.zeros((3, 3))

for j in range(10):
    for i in range(12):
        if(i%3==0):
            y2[0]+=arrays[j][i]
        elif(i%3==1):
            y2[1]+=arrays[j][i]
        else:
            y2[2]+=arrays[j][i]

for i in range(3):
    y2[i]/=40

y2=np.transpose(y2)
x2=['Morning', 'Afternoon', 'Evening']

plt.figure()  # Create a new figure
plt.bar(x2, y2[0], color='blue', label=f'RTT1')
plt.bar(x2, y2[1], color='yellow', label=f'RTT2')
plt.bar(x2, y2[2], color='green', label=f'RTT3')
# Labeling and titling
plt.xlabel('Time of the Day')
plt.ylabel('Delays (ms)')
plt.title('Delays vs Time of the Day')
plt.legend()
# Display the chart
plt.show()

y3=np.zeros((4, 3))
for j in range(10):
    for i in range(12):
        if(i<3):
            y3[0]+=arrays[j][i]
        elif(i>=3 and i<6):
            y3[1]+=arrays[j][i]
        elif(i>=6 and i<9):
            y3[2]+=arrays[j][i]
        else:
            y3[3]+=arrays[j][i]
for i in range(4):
    y3[i]/=30
y3=np.transpose(y3)
x3=['Wednesday', 'Thursday', 'Friday', 'Saturday']

plt.figure()  # Create a new figure
plt.bar(x3, y3[0], color='blue', label=f'RTT1')
plt.bar(x3, y3[1], color='yellow', label=f'RTT2')
plt.bar(x3, y3[2], color='green', label=f'RTT3')
# Labeling and titling
plt.xlabel('Days')
plt.ylabel('Delays (ms)')
plt.title('Delays vs Days')
plt.legend()
# Display the chart
plt.show()