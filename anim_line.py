import numpy as np
from matplotlib import image
from matplotlib import pyplot as plt
from PIL import Image
from PIL import ImageDraw

class labPlot:
    def func(self, identification, xplot, yplot):
        self.id = identification
        self.xplot = xplot
        self.yplot = yplot

data = [[1,230,240],
        [2,235,220],
        [3,235,250],
        [4,235,350],
        [5,235,390],
        [6,235,430],
        [7,235,490],
        [8,235,520],
        [9,235,560],
        [10,235,620],
        [11,235,650],
        [12,235,700],
            [13,300,670],
            [14,300,640],
            [15,300,580],
            [16,300,510],
            [17,300,480],
            [18,300,430],
            [19,300,390],
            [20,300,350],
            [21,300,290],
            [22,300,270],
            [23,300,240],
        [24,200,240],
        [25,200,270],
        [26,200,290],
        [27,200,350],
        [28,200,400],
        [29,200,430],
        [30,200,480],
        [31,200,520],
        [32,200,550],
        [33,200,600],
        [34,200,660],
        [35,200,690],
        [36,135,680],
        [37,130,660],
        [38,135,630],
        [39,135,600],
            [40,300,700],
            [41,300,720],
        [42,240,720],
        [43,135,240],
        [44,135,270],
        [45,135,290],
        [46,135,350],
        [47,135,400],
        [48,135,430],
        [49,135,480],
        [50,135,520],
            [51,135,550]]



im = image.imread('floorplan.jpeg')
print(im.shape)

for x in range(len(data)):
    #plt.plot(data[x][1], data[x][2], color="yellow", linewidth=3)
    plt.plot(data[x][1],data[x][2], marker='s', markersize=2, color="green")
    plt.imshow(im, aspect='auto')

#x = 548
#y = 1669
#plt.plot(x,y, color="yellow", linewidth=3)
#plt.imshow(im)
plt.show()


#plt.plot(data[x][1],data[x][2], color="yellow", linewidth=3)
#plt.imshow(data)