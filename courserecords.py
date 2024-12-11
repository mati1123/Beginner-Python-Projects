# tee ratkaisusi tänne
class Course:
    def __init__(self,name:str,grade:int,credits:int):
        self.__name = name
        self.__grade = grade
        self.__credits = credits
    
    def name(self):
        return self.__name
    
    def grade(self):
        return self.__grade
    
    def credits(self):
        return self.__credits
    
    def update_grade(self,grade:int):
        if grade > self.__grade:
            self.__grade = grade


class CourseRecords:
    def __init__(self):
        self.__courses = {}
    
    def add_course(self,name:str,grade:int,credits:int):
        if name in self.__courses:
            self.__courses[name].update_grade(grade)
        else:
            self.__courses[name] = Course(name,grade,credits)
        
    def get_course(self,name:str):
        return self.__courses.get(name,None)
    
    def all_courses(self):
        return self.__courses.values()


class CourseApplication:
    def __init__(self):
        self.__records = CourseRecords()
    
    def help(self):
        print("commands: ")
        print("0 exit")
        print("1 add course")
        print("2 get course data")
        print("3 statistics")
    
    def add_course(self):
        name = input("course: ")
        grade = int(input("grade: "))
        credits = int(input("credits: "))
        self.__records.add_course(name,grade,credits)
    
    def get_course_data(self):
        name = input("course: ")
        course = self.__records.get_course(name)
        if course is None:
            print("no entry for this course")
        else:
            print(f"{course.name()} ({course.credits()} cr) grade {course.grade()}")

    def statistics(self):
        courses = list(self.__records.all_courses())

        if not courses:
            print("no courses yet")
            return
        
        total_credits = sum(course.credits() for course in courses)
        num_courses = len(courses)
        mean_grade = sum(course.grade() for course in courses) / num_courses

        grade_distribution = [0] * 5
        for course in courses:
            grade_distribution[course.grade() - 1] += 1



        print(f"{num_courses} completed courses, a total of {total_credits} credits")
        print(f"mean {mean_grade:.1f}")
        print("grade distribution")
        for grade in range(5, 0, -1):  # Loopa från betyg 5 till 1
            print(f"{grade}: {'x' * grade_distribution[grade - 1]}")       

    def execute(self):
        self.help()
        while True:
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_course()
            elif command == "2":
                self.get_course_data()
            elif command == "3":
                self.statistics()
            else:
                self.help()





app = CourseApplication()
app.execute()
