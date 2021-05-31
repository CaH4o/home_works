# Home Work №2

sample_dict = {
   "class_a": {
      "student1": {
         "name": "Misha",
         "marks": {
            "math": 90,
            "history": 85
         }
      }
   }
}
# 1
task_1 = sample_dict["class_a"]["student1"]["name"]
print(task_1)
# # 2
task_2 = sample_dict["class_a"]["student1"]["marks"]["history"]
print(task_2)
# 3
student2_dict = {
      "name": "Max",
      "marks": {
         "math": 85,
         "history": 60
      }
}
sample_dict["class_a"]["student2"] = student2_dict
print(sample_dict)
# 4
class_b_dict = {
   "class_b": {
      "student3": {
         "name": "Lev",
         "marks": {
            "math": 85,
            "history": 65
         }
      }
   }
}
class_b_dict["class_b"]["student4"] = {
   "name": "Alex",
   "marks": {
      "math": 75,
      "history": 100
   }
}
print(class_b_dict)
# 5
sample_dict["class_a"]["student1"]["marks"]["physics"] = 30
sample_dict["class_a"]["student2"]["marks"]["physics"] = 75
class_b_dict["class_b"]["student3"]["marks"]["physics"] = 70
class_b_dict["class_b"]["student4"]["marks"]["physics"] = 90
print(sample_dict)
print(class_b_dict)
# 6
Misha_m1 = sample_dict["class_a"]["student1"]["marks"]["math"]
Misha_m2 = sample_dict["class_a"]["student1"]["marks"]["history"]
Misha_m3 = sample_dict["class_a"]["student1"]["marks"]["physics"]
Max_m1 = sample_dict["class_a"]["student2"]["marks"]["math"]
Max_m2 = sample_dict["class_a"]["student2"]["marks"]["history"]
Max_m3 = sample_dict["class_a"]["student2"]["marks"]["physics"]
Lev_m1 = class_b_dict["class_b"]["student3"]["marks"]["math"]
Lev_m2 = class_b_dict["class_b"]["student3"]["marks"]["history"]
Lev_m3 = class_b_dict["class_b"]["student3"]["marks"]["physics"]
Alex_m1 = class_b_dict["class_b"]["student4"]["marks"]["math"]
Alex_m2 = class_b_dict["class_b"]["student4"]["marks"]["history"]
Alex_m3 = class_b_dict["class_b"]["student4"]["marks"]["physics"]
# 6
a = (Misha_m1 + Misha_m2 + Misha_m3) / 2
b = (Max_m1 + Max_m2 + Max_m3) / 2
c = (Lev_m1 + Lev_m2 + Lev_m3) / 2
d = (Alex_m1 + Alex_m2 + Alex_m3) / 2
print(round(a, 2))
print(round(b, 2))
print(round(c, 2))
print(round(d, 2))
# 7
task_7 = {"Misha": a, "Max": b, "Lev": c, "Alex": d}
print(task_7)
