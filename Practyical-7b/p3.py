class Student:
    def __init__(self):
        print("__init__(self) is Called");
    def input(self):
        self.__rno=int(input("Enter Roll Number :"));
        self.__name=input("Enter Name :");
        self.__c_mark=int(input("Enter C_Marks :"));
        self.__cpp_mark=int(input("Enter CPP_Marks :"));
        self.__python_mark=int(input("Enter Python_Marks :"));

    def calc_total(self):
        self.__total=self.__c_mark + self.__cpp_mark + self.__python_mark;

    def calc_percentage(self):
        self.__per = self.__total/3;

    def calc_grade(self):

        if self.__per >= 70:
            self.__grade = "Distinct Class";

        elif self.__per >=60:
            self.__grade = "First Class";

        elif self.__per >=50:
            self.__grade = "Second Class";

        elif self.__per >=40:
            self.__grade = "Pass Class";

        else:
            self.__grade = "Fail";
    def show(self):
        print("\nRoll no\tName\tC_marks\tCpp_marks\tPython_marks\tTotal\tPercentage\tGrade");
        print(self.__rno,"\t",self.__name,"\t",self.__c_mark,"\t",self.__cpp_mark,"\t\t",self.__python_mark,"\t\t",self.__total,"\t",self.__per,"\t\t",self.__grade);
s1=Student();
s1.input();
s1.calc_total();
s1.calc_percentage();
s1.calc_grade();
s1.show();
