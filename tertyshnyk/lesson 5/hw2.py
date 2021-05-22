# Дан словарь такого типа:
# sample_dict = {
#    "class_a":{
#       "student1":{
#          "name":"Misha",
#          "marks":{
#             "math":90,
#             "history":85
#          }
#       }
#    }
# }
# 1. Вывести значение ключа "name";
# 2. Вывести значение ключа "history";
# 3. Добавить нового студента в "class_a", соответственно его "name" и "marks";
# 4. Добавить новый класс со студентами (в sample_dict нужно добавить class_b, в котором будет 2 студента);
# 5. Добавить каждому студенту в "marks" предмет "physics" с оценкой;
# 6. Подсчитать средний бал по каждому студенту (результат округлить до 2 знаков после запятой);
# 7. Создать словарь со средним баллом за каждого студента;
# 8. Определить лучшего студента по успеваемости;
# 9. Подсчитать средний бал по каждому классу (результат округлить до 2 знаков после запятой);
# 10. Создать словарь со средним баллом за классы;
# 11. Определить лучший класс по успеваемости.
import statistics

sample_dict = {
   "class_a": {
      "student1": {
         "name":"Misha",
         "marks":{
            "math":90,
            "history":85
         }
      }
   }
}
print(sample_dict)

#1
print(sample_dict['class_a']['student1']['name'])

#2
print(sample_dict['class_a']['student1']['marks']['history'])

#3
sample_dict['class_a']['student2'] = {
         "name": "Kolya",
         "marks": {
            "math": 70,
            "history": 65
         }
}
print(sample_dict)

#4
sample_dict['class_b'] = {
      "student3":  {
         "name": "Galya",
         "marks": {
            "math": 100,
            "history":55
         }
      },
      "student4": {
         "name": "Lusya",
         "marks": {
            "math": 46,
            "history": 111
         }
      }
}
print(sample_dict)

#5
sample_dict['class_a']['student1']['marks']['physics'] = 51
sample_dict['class_a']['student2']['marks']['physics'] = 52
sample_dict['class_b']['student3']['marks']['physics'] = 53
sample_dict['class_b']['student4']['marks']['physics'] = 54
print(sample_dict)

#6
# student1_avg = round(statistics.mean(sample_dict['class_a']['student1']['marks'].values()), 2)
student1_avg = sum(sample_dict['class_a']['student1']['marks'].values())
student1_avg /= len(sample_dict['class_a']['student1']['marks'].values())
student1_avg = round(student1_avg, 2)
print(student1_avg)

student2_avg = sum(sample_dict['class_a']['student2']['marks'].values())
student2_avg /= len(sample_dict['class_a']['student2']['marks'].values())
student2_avg = round(student2_avg, 2)
print(student2_avg)

student3_avg = sum(sample_dict['class_b']['student3']['marks'].values())
student3_avg /= len(sample_dict['class_b']['student3']['marks'].values())
student3_avg = round(student3_avg, 2)
print(student3_avg)

student4_avg = sum(sample_dict['class_b']['student4']['marks'].values())
student4_avg /= len(sample_dict['class_b']['student4']['marks'].values())
student4_avg = round(student4_avg, 2)
print(student4_avg)

#7
studentsAVG = {
   'student1': student1_avg,
   'student2': student2_avg,
   'student3': student3_avg,
   'student4': student4_avg,
}
print(studentsAVG)

#8
max_val = max(list(studentsAVG.values()))
max_val_index = list(studentsAVG.values()).index(max_val)
max_student = list(studentsAVG.keys())[max_val_index]
# print(max_val)
# print(max_val_index)
print(max_student)

#9
class_a_avg = list(sample_dict['class_a']['student1']['marks'].values())
class_a_avg.extend(list(sample_dict['class_a']['student2']['marks'].values()))
# print(class_a_avg)
class_a_avg = round(sum(class_a_avg) / len(class_a_avg), 2)
print(class_a_avg)

class_b_avg = list(sample_dict['class_b']['student3']['marks'].values())
class_b_avg.extend(list(sample_dict['class_b']['student4']['marks'].values()))
class_b_avg = round(sum(class_b_avg) / len(class_b_avg), 2)
print(class_b_avg)

#10
classAVG = {
   'class_a': class_a_avg,
   'class_b': class_b_avg,
}
print(classAVG)

#11
max_val = max(list(classAVG.values()))
max_val_index = list(classAVG.values()).index(max_val)
max_student = list(classAVG.keys())[max_val_index]
print(max_student)
