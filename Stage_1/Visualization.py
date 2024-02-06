import operator
import matplotlib.pyplot as plt

with open("Cardinals.txt") as f:
    lines = (line.strip() for line in f)
    lines = list(line for line in lines if line.find("{"))

lines2=[l.split(",") for l in lines]

lines3=[l for l in lines2[0] if not l=='']+[l for l in lines2[1] if not l=='']+[l for l in lines2[2] if not l=='']+[l for l in lines2[3] if not l=='']+[l for l in lines2[4] if not l=='']+[l for l in lines2[5] if not l=='']+[l for l in lines2[6] if not l=='']+[l for l in lines2[7] if not l=='']

print(lines3)
def plotter(lang_set):
    plt.xlabel('Numbers')
    plt.ylabel('Cardinals')
    t=range(0,100)
    t2=list(zip(t,lang_set))
    t2=sorted(t2,key=operator.itemgetter(1))
    Y=[l[0] for l in t2]
    #plt.scatter(t,Y)
    plt.scatter(t,Y)
    #Hide every values except 0,99
    plt.yticks([0, 99])
    #Replace those 2 with first and last
    plt.yticks([0, 99],['First', 'Last'])
    plt.title('Scatter Plot of Numbers vs. Cardinals')
    plt.show()
    
plotter(lines3)
