class Student:
    def __init__(self, name, hours, qpoints): # name,credit hours,quality points
        self.name = name
        self.hours = float(hours)
        self.qpoints = float(qpoints)


    def getName(self):
        return self.name


    def getHours(self):
        return self.hours


    def getQPoints(self):
        return self.qpoints

    def gpa(self):
        return self.qpoints/self.hours

    @staticmethod
    def makeStudent(info_line):
        # line: name,housr,qpoints
        # return a Student object
        name,housr,qpoints = info_line.split(' ')
        return Student(name,housr,qpoints)
