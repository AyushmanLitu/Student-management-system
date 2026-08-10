import json
# import myModules

# Id = myModules.idGenerator(7)

with open("studentData.json","r") as file:
    data = json.load(file)

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
    


new_id = len(data)+1


Litu = Student(new_id,"Ayushman",20,"Graduation")


# send the new_student to json 
def sentTOJsonfile(obj):
    dictData = obj.to_dict()
    data.append(dictData)
    with open("studentData.json","w")as file:
        json.dump(data,file,indent=4)

vicky = Student(new_id,"Niranjan",20,"graduation")
sentTOJsonfile(vicky)