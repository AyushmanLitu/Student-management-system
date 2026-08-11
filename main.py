import json
import myModules


try:
    with open("studentData.json","r") as file:
        data = json.load(file)
except (FileNotFoundError , json.JSONDecodeError):
    data = []

# student class
class Student:
    def __init__(self,student_id,name,age,qualification):
        self.id = student_id
        self.name = name
        self.age = age
        self.qualificaiton = qualification

    def to_dict(self):
        return {
            "id":self.id,
            "name":self.name,
            "age":self.age,
            "qualification":self.qualificaiton
        }

# Check if the given object is already in the json file or not
studentNameList = [info["name"] for info in data if "name" in info]
def check_if_exits(obj):
    if obj.name in studentNameList:
        print(f"{obj.name} is already exsits.")
        return False
    else:
        return True


# making unique ids
studentIds = [info["id"] for info in data if "id" in info]
def generate_unique_id():
    while True:
        new_id = myModules.idGenerator(7)
        if new_id not in studentIds:
            return new_id
        

# send the new_student to json 
def saveInDatabase(obj):
    global studentIds , studentNameList
    if not check_if_exits(obj):
        return
    
    new_id = generate_unique_id()
    obj.id = new_id
    
    studentIds.append(new_id)
    studentNameList.append(obj.name)

    data.append(obj.to_dict())
    with open("studentData.json","w")as file:
        json.dump(data,file,indent=4)


# Show all the students who are present in the database
def displayStudents():
    for info in data:
        print(info["name"],info["age"])


# # making new studetns
Litu = Student(None,"Ayushman",20,"Graduation")
saveInDatabase(Litu)
vicky = Student(None,"Niranjan",20,"Graduation")
saveInDatabase(vicky)
babul = Student(None,"Sambit",21,"Diploma")
saveInDatabase(babul)

# # Search using unique ids
def searchStudentbyId(student_id):
    realId = student_id.upper()
    if len(student_id) != 7:
        print("given Id is invalid.")
    for info in data:
        if realId == info["id"]:
            print(f"| name : {info["name"]},| age : {info["age"]},| qualification : {info["qualification"]} |")
            return
    print("Student with id doesn't exists")
searchStudentbyId("l16ti40")
