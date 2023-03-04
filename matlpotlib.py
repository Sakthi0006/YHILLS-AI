
import matplotlib.pyplot as plt
import numpy as np

xpoints=np.array([1,2])
ypoints=np.array([10,200])
plt.plot(xpoints,ypoints)
plt.show()


xpoints = np.array([1,20])
ypoints=np.array([10,200])
plt.plot(xpoints,ypoints)
plt.show()


xpoints=np.array([1,6])
ypoints=np.array([4,5])
plt.plot(xpoints,ypoints)
plt.show()


xpoints=np.array([1,6])
ypoints=np.array([4,5])
plt.plot(xpoints,ypoints,'*')
plt.show()


ypoints=np.array([3,8,1,10])
plt.plot(ypoints, '*''g')
plt.show()


ypoints = np.array([3,8,1,12])
xpoints = np.array([5,6,7,9])
plt.plot(xpoints,ypoints, marker = '*',ms=30,color='red')
plt.show()


ypoints = np.array([3,8,1,10])
plt.plot(ypoints, marker = 'o',ms=20,mfc='g',mec='k')
plt.show()
     

ypoints = np.array([3,8,1,10,12,16])
plt.plot(ypoints, marker = 'o',ms=30,mec='r',color='black')
plt.show()


ypoints=np.array([3,8,1,12])
xpoints=np.array([5,6,7,9])
plt.plot(xpoints,ypoints,marker = '+',ms=100,color='red')
plt.show()


ypoints=np.array([3,8,1])
plt.plot(ypoints,marker = 'o',ms=30,mec='r',color='black')
plt.show()


ypoints=np.array([3,8,1,10])
plt.plot(ypoints,marker ='o',ms=20,mfc='g',mec='k')
plt.show()


ypoints=np.array([3,8,1,10])
plt.plot(ypoints,marker='o',ms=20,mfc='g',mec='k')
plt.show()


ypoints=np.array([2,8,1,10])
plt.plot(ypoints,linestyle= 'dashed' ,marker='o',mec='hotpink',ms=20,mfc='blue',linewidth=3)
plt.show()

plt.plot(ypoints,linestyle= 'dotted' ,marker="o",ms=25,
         mfc="green",mec="red")

ypoints=np.array([3,8,1,10])
plt.plot(ypoints,marker='o',ms =200,mec='y',mfc='k')
plt.show()


ypoints=np.array([3,8,1,10])
plt.plot(ypoints,linestyle= 'dotted' ,marker="o",mec="hotpink",ms=20,mfc='blue',linewidth=3)
plt.show()


xpoints=np.array([10,20,30])
ypoints=np.array([1,2,6])
plt.plot(xpoints,ypoints,marker="*",color="red",mfc="g",mec="r",ms=20,linestyle="dashed")


ypoints=np.array([3,8,1,10])
plt.plot(ypoints,linewidth=5)
plt.show()



y1=np.array([3,8,1,10])
y2=np.array([6,2,5,11])
plt.plot(y1)
plt.plot(y2)
plt.show()


x=np.array([80,85,90,95,100,105,110,115,120,125])
y=np.array([240,250,260,270,280,290,300,310,320,330])
plt.plot(x,y,color="r",linewidth=1)

plt.xlabel("average pulse",fontsize=30,color='red')
plt.ylabel("calorie burnage",fontsize=10,color='g')
plt.show()


x=np.array([80,85,90,95,100,105,110,115,120,125])
y=np.array([240,250,260,270,280,290,300,310,320,330])
plt.plot(x,y,color="r",linewidth=1)

plt.xlabel("average pulse",fontsize=30,color='red')
plt.ylabel("calorie burnage",fontsize=10,color='g')
plt.title("sample",fontsize=50,color="blue")
plt.show()

x=np.array([80,85,90,95,100,105,110,115,120,125])
y=np.array([240,250,260,270,280,290,300,310,320,330])

plt.title("sports watch data")
plt.xlabel("average pulse")
plt.ylabel("calorie burnage")
plt.plot(x,y)
plt.grid(color="green")
plt.show()

x=np.array([80,85,90,95,100,105,110,115,120,125])
y=np.array([240,250,260,270,280,290,300,310,320,330])

plt.title("sports watch data")
plt.xlabel("average pulse")
plt.ylabel("calorie burnage")
plt.plot(x,y,color="0")
plt.grid(color="green",linestyle="dotted")
plt.show()


x=np.array([80,85,90,95,100,105,110,115,120,125])
y=np.array([240,250,260,270,280,290,300,310,320,330])

plt.title("sports watch data")
plt.xlabel("average pulse")
plt.ylabel("calorie burnage")
plt.plot(x,y)
plt.grid(axis='x')
plt.show()


x=np.array([80,85,90,95,100,105,110,115,120,125])
y=np.array([240,250,260,270,280,290,300,310,320,330])

plt.title("sports watch data")
plt.xlabel("average pulse")
plt.ylabel("calorie burnage")
plt.plot(x,y,color="orange")
plt.grid(color="green",linestyle="dotted")
plt.show()

x=np.array([5,7,8,7,2,13,17,11,12,9,6,9,10])
y=np.array([23,12,45,23,86,103,87,94,78,77,85,86,12])

plt.scatter(x,y)
plt.show()
   
  
x=np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y=np.array([23,12,45,23,86,103,87,94,78,77,85,86,12])

plt.scatter(x,y)

x=np.array([5,7,8,7,2,17,2,9,4,11,12,9,6,9,10])
y=np.array([23,12,45,23,86,103,87,94,78,77,85,86,12,8,90])

plt.scatter(x,y)
plt.show()


x=np.array(["a","b","c","d"])
y=np.array([3,8,1,10])
plt.bar(x,y,color="black")
plt.show()

x=np.array(["a","b","c","d"])
y=np.array([3,8,1,10])
plt.barh(x,y,color="green")
plt.show()

x=np.array(["a","b","c","d"])
y=np.array([3,8,1,10])
plt.bar(x,y, width=0.2)
plt.show()


plt.hist(x)

plt.hist(x)
plt.show()

y=np.array([10,135,25,15,19])
plt.pie(y)
plt.show()


y=np.array([10,25,15,10])
mylabels=["cherries","apples","bananas","dates"]
plt.pie(y,labels=mylabels)
plt.show()

y=np.array([30,25,15,10])
mylabels=["cherries","apples","bananas","dates"]
myexplode=[0,0.5,0.8,0.2]
plt.pie(y,labels=mylabels,explode=myexplode)
plt.show()


y=np.array([30,25,15,10])
mylabels=["cherries","apples","bananas","dates"]

plt.pie(y,labels=mylabels,startangle=90)
plt.show()
     
y=np.array([30,25,15,10])
mylabels=["cherries","apples","bananas","dates"]
mycolors=["black","hotpink","b","yellow"]
plt.pie(y,labels=mylabels,colors=mycolors,startangle=180)
plt.show()
     
  
y=np.array([30,25,15,10])
##mylabels=["cherries","apples","bananas","dates"]

plt.pie(y)
plt.legend(labels=mylabels)
plt.show()



