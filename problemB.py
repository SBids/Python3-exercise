# B. Create a console application for an IT Academy with the following features:

# a)The academy program should have a fixed course of study.
# b) If a new student is interested in the academy program the student can
# inquiry about the course of study.
# c) Student Registration with Rs. 20000 (deposit). Students are allowed to
# pay in two installments with Rs. 10000 each.
# d) Display all the student’s information from the academy with their payments
# and remaining payments.
# e) Update the student information if needed.
# f) Delete the student information if he/she left the program.
# g) Return the deposit amount (Rs. 20000) to the students after the
# successful completion of the course and check the balance.
# Remember it should be a full feature CONSOLE APP. You can store
# the course of study and the student’s detail in your preferred file
# format (.csv, .txt, etc).
# Ignore the permissions for now. Anyone who runs the script is allowed to
# access all the features. Develop the app with OOP Approach.

class Student:

    def __init__(self, full_name, address, contact_number, payment=0, due=0):
        self.full_name = full_name
        self.address = address
        self.contact_number = contact_number
        self.payment = payment
        self.due = due

    def courseStudy(self):
        import csv
        row_list = [["SN", "Course", "Estimated duration", "Lectures", "Guest Lectures"],
                    [1, "The Big Picture: Software Engineering ", "1 weeks", "4 Hrs", "1 Hr"],
                    [2, "Fundamentals of Web Development", "2 weeks", "8 Hrs", "1 Hr"],
                    [3, "Python programming", "2 weeks", "8 Hrs", "1 Hr"],
                    [4, "Backend Framework: Django", "3 weeks", "12 Hrs", "1 Hr"],
                    [5, "Django REST framework", "1 weeks", "4 Hrs", "1 Hr"],
                    [6, "Frontend Library: React", "1 weeks", "4 Hrs", "1 Hr"],
                    [7, "Capstone Project: Final Project", "2 weeks"]]

        with open('course.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(row_list)

    def courseInquiry(self, filename='course.csv'):
        import csv
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)


    def studentRegistration(self):
        import csv
        student_list = []
        self.full_name = input('Enter full name')
        self.address = input('Enter address')
        self.contact_number = input('Enter your contact number')
        self.payment = int(input('Enter the paid amount'))
        student_list.append(self.full_name)
        student_list.append(self.address)
        student_list.append(self.contact_number)
        student_list.append(self.payment)
        student_list.append(20000 - self.payment)
        print(student_list)

        with open('student.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(student_list)

    def getStudentInfo(self):
        import csv
        with open('student.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)




ram = Student('ram caste', 'Kathmandu', '98403939292')
ram.courseStudy()
ram.courseInquiry()
#ram.studentRegistration()
ram.getStudentInfo()





