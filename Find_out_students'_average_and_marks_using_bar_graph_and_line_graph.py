import matplotlib.pyplot as plt
sudents_names = ['Sanjay', 'Rahul', 'Karan', 'Wasim', 'Ramesh', 'Ajay', 'Partaj', 'Priya']
students_marks = [35,50,20,45,25,40,25,40]
marks_perc = []
for x in students_marks:
    res = (x/50)*100
    marks_perc.append(res)
print(marks_perc)
def marks_line_chart():
    plt.plot(sudents_names, students_marks)
    plt.title("Students Marks Graph")
    plt.xlabel("--Students Names-->")
    plt.ylabel("--Students Marks-->")
    plt.show()
marks_line_chart()

def percentage_bar_chart():
    plt.bar(sudents_names, marks_perc)
    plt.title("Student's Percentage Graph")
    plt.xlabel("--Students Names-->")
    plt.ylabel("--Students Percentage-->")
    plt.show()
percentage_bar_chart()