import matplotlib.pyplot as plt
import numpy as np

date_ = []
time_ = []
Q_cfs = []

my_file = open("data.txt", "r")
my_file_data = my_file.readlines()

list_data = []
for x in my_file_data:
    list_data.append(x)
    
list_data = list_data[1:]

for x in range(0, len(list_data)):
    list_data[x] = list_data[x].split("\t")
    for y in range(0, len(list_data[x])):
        if y== 0:
            date_.append(list_data[x][y])
        if y== 1:
            time_.append(x)
        if y== 2:
            Q_cfs.append(float(list_data[x][y].rstrip("\n")))
            
starting_x = 0
starting_y = 0
start_slope = []
flag = False
for x in range(0, len(Q_cfs)-1):
    x1 = time_[x]
    y1 = Q_cfs[x]
    x2 = time_[x+1]
    y2 = Q_cfs[x+1]
    z = (y2-y1)/(x2-x1)
    start_slope.append(z)
    if (z>=0.2) & (flag ==False):
        flag = True
        starting_x = x1
        starting_y = y1
    else:
        continue
    
end_x = 0
end_y = 0
end_slope = []
flag = False
for x in range(0, len(Q_cfs)-1):
    x1 = time_[x]
    y1 = Q_cfs[x]
    x2 = time_[x+1]
    y2 = Q_cfs[x+1]
    z = (y2-y1)/(x2-x1)
    end_slope.append(z)
    if (z==-0.09999999999999964) & (flag ==False):
        flag = True
        end_x = x1
        end_y = y1
    else:
        continue

dx = np.diff(time_)
dy = np.diff(Q_cfs)
d = dy/dx 
dd = np.diff(d)
dx = np.diff(time_)
c = dy/dx

infx = 0
infy = 0
flag = False
for x in range(Q_cfs.index(max(Q_cfs)), end_x):
    if (c[x] == 0.00e+00) & (flag == False):
        infx = time_[x]
        infy = Q_cfs[x]
        flag =True
        
x_peak = []
y_peak = []
x_peak.append(Q_cfs.index(max(Q_cfs)))
x_peak.append(Q_cfs.index(max(Q_cfs)))
y_peak.append(max(Q_cfs))
y_peak.append(starting_y)

x_lbase = []
y_lbase = []
x_lbase.append(starting_x)
x_lbase.append(Q_cfs.index(max(Q_cfs)))
y_lbase.append(starting_y)
y_lbase.append(starting_y)

x_rbase = []
y_rbase = []
x_rbase.append(infx)
x_rbase.append(infx)
x_rbase.append(end_x)
y_rbase.append(infy)
y_rbase.append(end_y)
y_rbase.append(end_y)

x_base = []
y_base = []
x_base.append(Q_cfs.index(max(Q_cfs)))
x_base.append(infx)
y_base.append(starting_y)
y_base.append(end_y)

        
plt.plot(x_lbase, y_lbase, color="black")
plt.plot(x_rbase, y_rbase, color="black")
plt.plot(x_base, y_base, color="red")
plt.plot(starting_x, starting_y, color="red", marker = "o")
plt.plot(infx, infy, color="olive", marker = "o")
plt.plot(end_x, end_y, color="blue", marker=("o"))
plt.plot(x_peak, y_peak, color="blue")
plt.plot(time_, Q_cfs, color="green")
plt.title('Hydrograph Separation')
plt.xlabel('Delta T')
plt.ylabel('Q(CFS)')
plt.grid(True)
plt.savefig('Hydrograph Separation.jpg')
plt.show()

