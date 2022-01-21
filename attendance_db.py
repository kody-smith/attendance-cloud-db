import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


cred = credentials.Certificate("C:/Users/krsmi_u3swyjx/Downloads/attendance-1b61c-firebase-adminsdk-ha3w4-a3b4c25139.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

class Student(object):
    def __init__(self, name, email, attendance=0, student_id = 0, age=0):
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

class Module(object):
    def __init__(self, mod_one, mod_two, mod_three, exam_name, week_id=0):
        self.mod_one = mod_one
        self.mod_two = mod_two
        self.mod_three = mod_three
        self.exam_name = exam_name
        self.week_id = week_id

    @staticmethod

    def from_dict(source):
        # [START_EXCLUDE]
        module = Module(source[u'mod_one'], source[u'mod_two'], source[u'mod_three'])

        if u'week_id' in source:
            module.week_id = source[u'week_id']

        return module
        # [END_EXCLUDE]

    def to_dict(self):
        # [START_EXCLUDE]
        dest = {
            u'mod_one': self.mod_one,
            u'mod_two': self.mod_two,
            u'mod_three': self.mod_three,
            u'exam_name': self.exam_name,
            u'week_id': self.week_id,
        }

        if self.mod_one:
            dest[u'mod_one'] = self.mod_one

        if self.mod_two:
            dest[u'mod_two'] = self.mod_two

        if self.mod_three:
            dest[u'mod_three'] = self.mod_three
        
        if self.exam_name:
            dest[u'exam_name'] = self.exam_name

        if self.week_id:
            dest[u'week_id'] = self.week_id

        return dest
        # [END_EXCLUDE]

    def __repr__(self):
        return(
            f'Module(\
                mod_one={self.mod_one}, \
                mod_two={self.mod_two}, \
                mod_three={self.mod_three}, \
                exam_name={self.exam_name}, \
                week_id={self.week_id}\
            )'
        )



# jJohnson = Student(u'John Johnson',u'jJohnson@gmail.com',u'b',10,11223,21)
# student_ref.document('jJohnson').set(jJohnson.to_dict())

# kSmith = Student(u'Kody Smith',u'ksmith@gmail.com',u'A',12,12345,22)
# student_ref.document('kSmith').set(kSmith.to_dict())

# kSmith = Student(u'Kody Smith',u'ksmith@gmail.com',u'A',12,12345,22)
# student_ref.document('kSmith').set(kSmith.to_dict())

# kSmith = Student(u'Kody Smith',u'ksmith@gmail.com',u'A',12,12345,22)
# student_ref.document('kSmith').set(kSmith.to_dict())

# kSmith = Student(u'Kody Smith',u'ksmith@gmail.com',u'A',12,12345,22)
# student_ref.document('kSmith').set(kSmith.to_dict())

# kSmith = Student(u'Kody Smith',u'ksmith@gmail.com',u'A',12,12345,22)
# student_ref.document('kSmith').set(kSmith.to_dict())

# kSmith = Student(u'Kody Smith',u'ksmith@gmail.com',u'A',12,12345,22)
# student_ref.document('kSmith').set(kSmith.to_dict())


# module_ref = db.collection(u'modules')
# week1 = Module(u'W01 Prepare',u'W01 Prove',u'W01 Ponder',u'None',1)
# week2 = Module(u'W02 Prepare',u'W02 Prove',u'W02 Ponder',u'None',2)
# week3 = Module(u'W03 Prepare',u'W03 Prove',u'W03 Ponder',u'None',3)
# week4 = Module(u'W04 Prepare',u'W04 Prove',u'W04 Ponder',u'None',4)
# week5 = Module(u'W05 Prepare',u'W05 Prove',u'W05 Ponder',u'None',5)
# week6 = Module(u'W06 Prepare',u'W06 Prove',u'W06 Ponder',u'None',6)
# week7 = Module(u'W07 Prepare',u'W07 Prove',u'W07 Ponder',u'None',7)
# week8 = Module(u'W08 Prepare',u'W08 Prove',u'W08 Ponder',u'None',8)
# week9 = Module(u'W09 Prepare',u'W09 Prove',u'W09 Ponder',u'None',9)
# week10 = Module(u'W010 Prepare',u'W010 Prove',u'W010 Ponder',u'None',10)
# week11 = Module(u'W011 Prepare',u'W011 Prove',u'W011 Ponder',u'None',11)
# week12 = Module(u'W012 Prepare',u'W012 Prove',u'W012 Ponder',u'None',12)
# week13 = Module(u'W013 Prepare',u'W013 Prove',u'W013 Ponder',u'None',13)
# week14 = Module(u'W014 Prepare',u'W014 Prove',u'W014 Ponder',u'None',14)

# module_ref.document('w01').set(week1.to_dict())
# module_ref.document('w02').set(week2.to_dict())
# module_ref.document('w03').set(week3.to_dict())
# module_ref.document('w04').set(week4.to_dict())
# module_ref.document('w05').set(week5.to_dict())
# module_ref.document('w06').set(week6.to_dict())
# module_ref.document('w07').set(week7.to_dict())
# module_ref.document('w08').set(week8.to_dict())
# module_ref.document('w09').set(week9.to_dict())
# module_ref.document('w010').set(week10.to_dict())
# module_ref.document('w011').set(week11.to_dict())
# module_ref.document('w012').set(week12.to_dict())
# module_ref.document('w013').set(week13.to_dict())
# module_ref.document('w014').set(week14.to_dict())


# doc = k_smith.get()
# if doc.exists:
#     print(f'Document data: {doc.to_dict()}')
# else:
#     print(u'No such document!')

# # Store attendance in a variable
# total_modules = 14
# get_attendance = k_smith.get(field_paths={'attendance'})
# kSmith_attendance = ('{:.2f}'.format(int(get_attendance.to_dict()['attendance'])))
# print(kSmith_attendance)


# db.collection(u'students').document(u'1').delete()
# db.collection(u'students').document(u'jJohnson').delete()

