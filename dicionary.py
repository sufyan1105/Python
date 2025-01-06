# Dictionaries
# student = {
#     "name": "Mark",
#     "student_id": 15163,
#     "marks": [70, 80, 90, 60, 50],
#     "age": 25,
# }
# print(student["name"])
# student["name"] = "James"
# print(student["name"])

# Nested dictionaries

# student = {
#     "name" : "Mark",
#     "subjects" : {
#         "maths" : 70,
#         "physics" : 80,
#         "chemistry" : 90,
#     }
# }
# print(student["subjects"]["maths"])
# print(student.keys())
# print(list(student.keys()))
# print(student.values())
# print(len(student))
# print(student.items())
# print(student.get("name"))
# print(student.update({"city": "Mumbai"}))
# print(student)

# furniture = {
#     "table" : ["a piece of furniture" "list of facts & figures"],
#     "cat" : "a small animal",
# }
# print(furniture)

marks = {}

maths = int(input("Enter the number of students: "))
chemistry = int(input("Enter the number of students: "))
physics = int(input("Enter the number of students: "))

marks.update({"maths": maths})
marks.update({"chemistry": chemistry})
marks.update({"physics": physics})

print(marks)

