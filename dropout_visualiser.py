import matplotlib.pyplot as plt
import numpy as np

names = []
average_acc = []
min_acc = []
best_acc = []
average_loss = []
min_loss = []
max_loss = []
fileName = open("DropoutNotes.csv",'r')
data = fileName.read().split("\n")
fileName.close()

for line in data[1:-1]: # skip first line
    content = line.split(',')
    #print(content)
    names.append(content[1])
    average_acc.append(float(content[2]))
    min_acc.append(float(content[4]))
    best_acc.append(float(content[3]))
    average_loss.append(float(content[5]))
    min_loss.append(float(content[7]))
    max_loss.append(float(content[6]))

bar_colors = ['C0'] * len(names)
bar_hatches = [""] * len(names)

fig, ax = plt.subplots()
ax.bar(names,average_acc, color=bar_colors, linewidth=1.25, edgecolor='black', hatch=bar_hatches, width=0.4)
ax.set_ylabel("Accuracy (%)",fontsize=16)
ax.set_xlabel("Dropout Ratio",fontsize=16)
ax.set_title("Results of randomised hyperparameter testing", fontsize=16)

plt.xticks(rotation=40,fontsize=14)  # X-tick labels font size
plt.yticks(fontsize=14)  # Y-tick labels font size

for i in range(len(average_acc)):
    ax.vlines(x=i, ymin=min_acc[i], ymax=best_acc[i], color='black', linestyles='dashed',linewidth=2)



plt.show()