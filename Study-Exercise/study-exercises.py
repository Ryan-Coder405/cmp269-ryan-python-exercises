
# Exercise 1
class LehmanCourse:
    def __init__(self,course_name,credits):
        self.course_name = course_name
        self.credits = credits
        self._student_count = 0
    
    def enroll_student(self):
        self._student_count += 1

    def display_info(self):
        print(f"course name: {self.course_name}, credits: {self.credits}, enrolled students: {self._student_count}")

class LabCourse(LehmanCourse):
    def __init(self,course_name,credits,lab_fee):
        super().__init__(course_name,credits)
        self.lab_fee = lab_fee

    def display_info(self):
        print(f"course name: {self.course_name}, credits: {self.credits}, lab fee: {self.lab_fee}, enrolled students: {self._student_count}")

class Professor:
    def get_role(self):
        return "Teaching and Research"
    
class Student:
    def get_role(self):
        return "Learning and Coding"

def print_role(person):
    return person.get_role()


if __name__ == "__main__":
    print("-------------------------------------") # So the terminal won't drive me insane
    course1 = LehmanCourse("Fuck","40")
    professor1 = Professor()
    student1 = Student()
    course1.display_info()
    course1.enroll_student()
    course1.display_info()

    print(print_role(professor1))
    print(print_role(student1))