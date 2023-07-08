f=open("D:\\python\\stud.csv","r")
info_dataset=[]
while True:
    data=f.readline()
    if data:
        info_dataset.append(data.replace("\n","").split(","))
    else:
        break;
print(info_dataset)
Name=[]
Rollno=[]
Section=[]
Batch=[]
for row in info_dataset[1:]:
    Name.append(row[0])
    Rollno.append(row[1])
    Section.append(row[2])
    Batch.append(row[3])
    f2=open("D:\\python\\marks.csv","r")
student_dataset=[]
while True:
    data1=f2.readline()
    if data1:
        student_dataset.append(data1.replace("\n","").split(","))
    else:
        break;
print(student_dataset)
Maths=[]
Physics=[]
for row in student_dataset[1:]:
    Maths.append(row[0])
    Physics.append(row[1])
f4=open("student_details.csv","w")
student_details=[]
for i in range (len(student_dataset)):
    student_details.append(info_dataset[i]+student_dataset[i])
print(student_details)
data_to_write=[]
for i in range(len(student_details[0])):#10 rows
    row=list()
    for j in range(len(student_details)):#12 col
        data=student_details[j][i]
        row.append(data)
    row.append('\n')
    data_to_write.append(",".join(row))
    Name=[]
    Rollno=[]
    Section=[]
    Batch=[]
    Maths=[]
    Physics=[]
    studentdetail=[]
    studentdetail.append(Name)
    studentdetail.append(Rollno)
    studentdetail.append(Section)
    studentdetail.append(Batch)
    studentdetail.append(Maths)
    studentdetail.append(Physics)
    print("math marks=",Maths)
    print("physics marks=",Physics)
    Maths=[int(i) for i in Maths]
    Physics=[int(i) for i in Physics] 
    sum_of_marks=[]
    average=[]
    for i in range(len(Maths)):
        sum_of_marks.append(Maths[i]+Physics[i])
        average.append(round(sum_of_marks[i],2))
        print("sum_of_marks=",sum_of_marks)
        print("Average of marks=",average)
