from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

db = client["student_db"]
# this will create the data base

items = db['student']
# this will create the collection inside the db items_db



students_data = [
    {"name": "Atharva", "age": 21, "marks": 85},
    {"name": "Rahul", "age": 20, "marks": 70},
    {"name": "Aman", "age": 22, "marks": 92},
    {"name": "Priya", "age": 19, "marks": 65},
    {"name": "Neha", "age": 21, "marks": 78}
]
# items.insert_many(students_data)

# for student in  items.find({"marks" : { "$gt" : 75}}).sort({"marks" : -1}):
#     print(student["name"],student['marks'])

# for student in items.find({} , {"name":1 ,"marks" : 1}):
#     print(student)


# for student in items.find().sort({"marks":-1}).limit(5):
#     print(student)

# for student in items.find({"marks":{"$gt" : 60}}):
#     print(student)

# for student in items.find({"marks" : {"$gt" : 75}}):
    # marks = student["marks"]
    # bonous = 5
    # marks +=bonous
    # items.update_one({
    #     "$set" : {"marks" : marks}
    # })
    # print(student["name"], print["marks"])
    # print(student["name"],student["age"])

# for student in items.find({} , {"age":1}):
#     items.update_one(
#     {
#         "_id": student["_id"]
#     }, {"$set" :{"age" : 19}})

#     print(student["age"])

# for student in items.aggregate([{
#     "$group" :{
    
#        "_id" : "$None",
#        "average_marks" : {"$sum" : "$marks"}}
      
#    } ]):
#     print(student)

# for student in items.aggregate([
#    { "$group" :{
#         "_id" :"$marks",
#         "no" : {"$sum":1},
#         "average_age" : {"$avg" :"$age"}
#     }
# }]):
#     print(student)
    


