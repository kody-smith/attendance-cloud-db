import firebase_admin
import attendance_db
from firebase_admin import firestore
from firebase_admin import credentials
import random

db = firestore.client()

from google.cloud import firestore

cred = credentials.Certificate("C:/Users/krsmi_u3swyjx/Downloads/attendance-1b61c-firebase-adminsdk-ha3w4-a3b4c25139.json")



class Module_Count(object):
    """
    A shard is a distributed counter. Each shard can support being incremented
    once per second. Multiple shards are needed within a Counter to allow
    more frequent incrementing.
    """

    def __init__(self):
        self._count = 0

    def to_dict(self):
        return {"count": self._count}


class Counter(object):
    """
    A counter stores a collection of shards which are
    summed to return a total count. This allows for more
    frequent incrementing than a single document.
    """

    def __init__(self, num_modules):
        self._num_modules = num_modules


class Student(object):
    def __init__(self, name, email, student_id = 0, age=0, attendance=0):
        self.name = name
        self.email = email
        self.attendance = attendance
        self.student_id = student_id
        self.age = age

    @staticmethod

    def from_dict(source):
        # [START_EXCLUDE]
        student = Student(source[u'name'], source[u'student_id'], source[u'email'])

        if u'attendance' in source:
            student.attendance = source[u'attendance']

        if u'age' in source:
            student.age = source[u'age']

        return student
        # [END_EXCLUDE]

    def to_dict(self):
        # [START_EXCLUDE]
        dest = {
            u'name': self.name,
            u'email': self.email,
            u'attendance': self.attendance,
            u'student_id': self.student_id,
            u'age': self.age
        }

        if self.name:
            dest[u'name'] = self.name

        if self.email:
            dest[u'email'] = self.email
        
        if self.attendance:
            dest[u'attendance'] = self.attendance

        if self.student_id:
            dest[u'student_id'] = self.student_id

        if self.age:
            dest[u'age'] = self.age

        return dest
        # [END_EXCLUDE]

    def __repr__(self):
        return(
            f'Student(\
                name={self.name}, \
                email={self.email}, \
                attendance={self.attendance}, \
                student_id={self.student_id}, \
                age={self.age}\
            )'
        )



ans=True
while ans:
    print ("""
    1.Add a New Student
    2.Delete a Student
    3.Look Up Student Records
    4.Look Up Module Records
    5.Look Up Student Attendance Score
    6.Update Student Information
    7.Exit
    """)
    ans= input("What would you like to do? ")
    if ans=="1": 
        name = input("Enter the name of the new student: ")
        email = input("Enter the email of the new student: ")
        student_id = input("Enter the new student ID of the new student: ")
        age = input("Enter the age of the new student: ")
        attendance = input("Enter the attendance of the new student(if has not yet attended class enter 0): ")
        student_ref = db.collection(u'students')
        new_student = Student(f"{name}",f"{email}",f"{student_id}",f"{age}",f"{attendance}")
        student_ref.document(f'{student_id}').set(new_student.to_dict())
    elif ans=="2":
        student = input("Enter the student ID of the student you would like to delete: ")
        db.collection('students').document(f"{student}").delete()
        print("\n Student Deleted") 
    elif ans=="3":
        record = input("Enter the student ID of the student you would like to see: ")
        pull_student = db.collection(u'students').document(f"{record}")
        print("\n Student Record Found") 
        doc = pull_student.get()
        if doc.exists:
            print(f'Student data: {doc.to_dict()}')
        else:
            print(u'No such student!')
    elif ans=="4":
        module_record = input("Enter the module id of the module you want to see: ")
        pull_module = db.collection(u'modules').document(f"{module_record}")
        print("\n Student Record Found") 
        doc = pull_module.get()
        if doc.exists:
            print(f'Module data: {doc.to_dict()}')
        else:
            print(u'No such module!')
    elif ans=="5":
        student_attendance = input("Enter the ID of the student for which you would like to see an attendance score: ")
        modules = db.collection("modules").list_documents()
            
        get_student = db.collection("students").document(student_attendance)

        get_attendance = (get_student.get(field_paths={'attendance'}))

        print(student_attendance)

        print(get_student.get().to_dict())

        attendance = int(get_attendance.to_dict()['attendance'])

        score = (attendance/(len(list(modules))))

        print(score)
    elif ans=="6":
        update_student = input("Which student would you like to update? ")
        update_option = input("What would you like to update (ex. age, name, email, or attendance)? ")
        if update_option == "age":
            value = input("What is the new data? ")
            db.collection('students').document(update_student).update({update_option: value})
        elif update_option == "name":
            value = input("What is the new data? ")
            db.collection('students').document(update_student).update({update_option: value})
        elif update_option == "email":
            value = input("What is the new data? ")
            db.collection('students').document(update_student).update({update_option: value})
        elif update_option == "attendance":
            value = input("What is the new data? ")
            db.collection('students').document(update_student).update({update_option: value})
        else:
            print("Invalid entry, try again.")
            update_student
    elif ans=="7":
        print("Goodbye")
        break
    elif ans !="":
      print("\n Not Valid Choice Try again") 