from student import Student

def readStudents(data_filename):
    with open(data_filename,'r') as data_file:
        student_list = []
        for line in data_file:
            student_list.append(Student.makeStudent(line))
        data_file.close()
        return student_list

def writeStudents(student_list,result_filename):
    with open(result_filename, 'w') as result_file:
        for s in student_list:
            print("{0:<15}{1:<10}{2:<10}{3:.2f}".format(s.getName(),s.getHours(),s.getPoints(),s.gpa()),file = result_file)
        result_file.close()

def main():
    data_filename = input("Please input the data file name:")
    student_list = readStudents(data_filename)
    student_list.sort(key=Student.gpa,reverse=True) # descending
    result_filename = input("Please input the result file name:")
    writeStudents(student_list,result_filename)
    pass

if __name__ == '__main__':
    main()