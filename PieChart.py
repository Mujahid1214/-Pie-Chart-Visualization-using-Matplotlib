import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
labels = ("Python", "Java", "Scala", "C#")
sizes = [45, 30, 15, 10]
plt.pie(
    sizes,
    labels=labels,
    autopct='%1.f%%',
    counterclock=False,
    startangle= 105
)
plt.show()