import operator
import matplotlib.pyplot as plt

with open("Cardinals.txt") as f:
    lines = (line.strip() for line in f)
    lines = list(line for line in lines if line.find("{"))

lines2=[l.split(",") for l in lines]

lines3=[l for l in lines2[0] if not l=='']+[l for l in lines2[1] if not l=='']+[l for l in lines2[2] if not l=='']+[l for l in lines2[3] if not l=='']+[l for l in lines2[4] if not l=='']+[l for l in lines2[5] if not l=='']+[l for l in lines2[6] if not l=='']+[l for l in lines2[7] if not l=='']

print(lines3)
linelatin="Nulla, Uno, Duo, Tri, Quatuor, Quinque, Sex, Septem, Octo, Nono, Decem, Undecim, Duodecim, Tredecim, Quatuordecim, Quindecim, Sedecim, Septendecim, Duodeviginti, Undeviginti, Viginti, Viginti unus, Viginti duo, Viginti tres, Viginti quattuor, Viginti quinque, Viginti sex, Viginti septem, Viginti octo, Viginti novem, Triginta, Triginta unus, Triginta duo, Triginta tres, Triginta quattuor, Triginta quinque, Triginta sex, Triginta septem, Triginta octo, Triginta novem, Quadraginta, Quadraginta unus, Quadraginta duo, Quadraginta tres, Quadraginta quattuor, Quadraginta quinque, Quadraginta sex, Quadraginta septem, Quadraginta octo, Quadraginta novem, Quinquaginta, Quinquaginta unus, Quinquaginta duo, Quinquaginta tres, Quinquaginta quattuor, Quinquaginta quinque, Quinquaginta sex, Quinquaginta septem, Quinquaginta octo, Quinquaginta novem, Sexaginta, Sexaginta unus, Sexaginta duo, Sexaginta tres, Sexaginta quattuor, Sexaginta quinque, Sexaginta sex, Sexaginta septem, Sexaginta octo, Sexaginta novem, Septuaginta, Septuaginta unus, Septuaginta duo, Septuaginta tres, Septuaginta quattuor, Septuaginta quinque, Septuaginta sex, Septuaginta septem, Septuaginta octo, Septuaginta novem, Octoginta, Octoginta unus, Octoginta duo, Octoginta tres, Octoginta quattuor, Octoginta quinque, Octoginta sex, Octoginta septem, Octoginta octo, Octoginta novem, Nonaginta, Nonaginta unus, Nonaginta duo, Nonaginta tres, Nonaginta quatuor, Nonaginta quinque, Nonaginta sex, Nonaginta septem, Nonaginta octo, Nonaginta novem"
linelatin=linelatin.split(",")
def plotter(lang_set):
    plt.xlabel('Numbers')
    plt.ylabel('Cardinals')
    t=range(0,100)
    t2=list(zip(t,lang_set))
    t2=sorted(t2,key=operator.itemgetter(1))
    Y=[l[0] for l in t2]
    plt.plot(t,Y)
    #plt.scatter(t,Y)
    #Hide every values except 0,99
    plt.yticks([0, 99])
    #Replace those 2 with first and last
    plt.yticks([0, 99],['First', 'Last'])
    plt.title('Scatter Plot of Numbers vs. Cardinals')
    plt.show()
    
plotter(lines3)
plotter(linelatin)
