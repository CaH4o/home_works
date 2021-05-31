# Дан словарь такого типа:
sample_dict = {
   "class_a":{
      "student1":{
         "name":"Misha",
         "marks":{
            "math":90,
            "history":85
         }
      }
   }
}
# 1. Вывести значение ключа "name";
print(sample_dict["class_a"]['student1']['name'])
# 2. Вывести значение ключа "history";
print(sample_dict.get('class_a').get('student1').get('marks').get('history'))
# 3. Добавить нового студента в "class_a", соответственно его "name" и "marks";
sample_dict['class_a']['student2']= {'name': 'Natasha', 'marks': {'math': 60, 'history': 95}}
print(sample_dict)
# 4. Добавить новый класс со студентами (в sample_dict нужно добавить class_b, в котором будет 2 студента);
sample_dict['class_b'] = {'student1':
                      {'name':
                          'Oksana','marks':
                         {'math':40,'history':50}
                       },
                         'student2':
                     {'name':
                           'Nikolay','marks':
                           {'math':80,'history':50}
                     }
                        }
print(sample_dict)
# 5. Добавить каждому студенту в "marks" предмет "physics" с оценкой;
sample_dict['class_a']['student1']['marks']['physics'] = 90
sample_dict['class_a']['student2']['marks']['physics'] = 80
sample_dict['class_b']['student1']['marks']['physics'] = 100
sample_dict['class_b']['student2']['marks']['physics'] = 60
print(sample_dict)
# 6. Подсчитать средний бал по каждому студенту (результат округлить до 2 знаков после запятой);
student1a_marks = list(sample_dict['class_a']['student1']['marks'].values())
student1a_avg = round(sum(student1a_marks) / len(student1a_marks),2)
student2a_marks = list(sample_dict['class_a']['student2']['marks'].values())
student2a_avg = round(sum(student2a_marks) / len(student2a_marks),2)
student1b_marks = list(sample_dict['class_b']['student1']['marks'].values())
student1b_avg = round(sum(student1b_marks) / len(student1b_marks),2)
student2b_marks = list(sample_dict['class_b']['student2']['marks'].values())
student2b_avg = round(sum(student2b_marks) / len(student2b_marks),2)

# 7. Создать словарь со средним баллом за каждого студента;
avg_marks_dict = {sample_dict['class_a']['student1']['name']:student1a_avg,
                  sample_dict['class_a']['student2']['name']:student2a_avg,
                  sample_dict['class_b']['student1']['name']:student1b_avg,
                  sample_dict['class_b']['student2']['name']:student2b_avg
                  }
print(avg_marks_dict)
# 8. Определить лучшего студента по успеваемости;
max_mark = max(avg_marks_dict.values())
best_student = list(avg_marks_dict.keys())[list(avg_marks_dict.values()).index(max_mark)]
print(f'the best student is {best_student} ')
# 9. Подсчитать средний бал по каждому классу (результат округлить до 2 знаков после запятой);
class_a_avg = round((student1a_avg + student2a_avg) /len(sample_dict['class_a']),2)
class_b_avg = round((student1b_avg + student2b_avg) /len(sample_dict['class_b']),2)
# 8. Создать словарь со средним баллом за классы;
avg_class_dict = {'class_a': class_a_avg, 'class_b': class_b_avg}
print(avg_class_dict)
# 9. Определить лучший класс по успеваемости.
max_mark_class = max(avg_class_dict.values())
best_class = list(avg_class_dict.keys())[list(avg_class_dict.values()).index(max_mark_class)]
print(f'the best class is {best_class}')
