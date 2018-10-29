from student import Student

def readStudents(filename):
    """return a List of Student object"""
    infile = open(filename,'r')
    stulist = []
    for line in infile:
        stulist.append(Student.makeStudent(line))
    infile.close()
    return stulist

def writeStudents(stus,filename):
    """output the data to a file"""
    outfile = open(filename, 'w')
    for s in stus:
        print("{0:<15}{1:<10}{2:<10}{3:.2f}".format(s.name,s.getHours(),s.getPoints(),s.gpa()),file = outfile)
    outfile.close()

def main():
    data_filename = input("filename:")
    data = readStudents(data_filename)
    data.sort(key=Student.gpa,reverse=True) # descending
    result_filename = input("outfile:")
    writeStudents(data,result_filename)
    pass

if __name__ == '__main__':
    main()