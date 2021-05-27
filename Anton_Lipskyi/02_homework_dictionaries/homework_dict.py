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
print('1:', sample_dict['class_a']['student1']['name'])

# 2
print('2:', sample_dict['class_a']['student1']['marks']['history'])

# 3
dict2 = {
"student2":{
         "name": "Alex",
         "marks": {
            "math": 60,
            "history": 65
         }
      }
}

sample_dict['class_a'].update(dict2)
print('3:', sample_dict)

# 4
cl2 = {
   "class_b": {
      "student1": {
         "name": "Ivan",
         "marks": {
            "math": 85,
            "history": 70
         }
      },
      "student2": {
         "name": "Dima",
         "marks": {
            "math": 60,
            "history": 95
         }
      }
   }
}
sample_dict.update(cl2)
print('4:', sample_dict)

# 5
sample_dict['class_a']['student1']['marks'].update({'phisics': 60})
sample_dict['class_a']['student2']['marks'].update({'phisics': 91})
sample_dict['class_b']['student1']['marks'].update({'phisics': 64})
sample_dict['class_b']['student2']['marks'].update({'phisics': 90})
print('5:', sample_dict)

# 6
val1 = sample_dict['class_a']['student1']['marks']
mean1 = round(sum(val1.values()) / len(val1), 2)

val2 = sample_dict['class_a']['student2']['marks']
mean2 = round(sum(val2.values()) / len(val2), 2)
val3 = sample_dict['class_b']['student1']['marks']
mean3 = round(sum(val3.values()) / len(val3), 2)
val4 = sample_dict['class_b']['student2']['marks']
mean4 = round(sum(val4.values()) / len(val4), 2)

print('6:', mean1, mean2, mean3, mean4)

# 7
dict_mean = {

   sample_dict['class_a']['student1']['name']: mean1,
   sample_dict['class_a']['student2']['name']: mean2,
   sample_dict['class_b']['student1']['name']: mean3,
   sample_dict['class_b']['student2']['name']: mean4,
}
print('7:', dict_mean)

# 8
# лучший средний бал:
max_mean = max(dict_mean.values())
# лучший средний был знаем, теперь нужно по ключу достать имя студента:
max_index = list(dict_mean.values()).index(max_mean)
best_student = list(dict_mean.keys())[max_index]

print(f'8: {best_student}: {max_mean}')

# 9
#class_a
class_a_marks = []
class_a_stud1 = sample_dict['class_a']['student1']['marks'].values()
class_a_stud2 = sample_dict['class_a']['student2']['marks'].values()
class_a_marks.extend(class_a_stud1)
class_a_marks.extend(class_a_stud2)
class_a_mean = round(sum(class_a_marks) / len(class_a_marks), 2)

#class_b
class_b_marks = []
class_b_stud1 = sample_dict['class_b']['student1']['marks'].values()
class_b_stud2 = sample_dict['class_b']['student2']['marks'].values()
class_b_marks.extend(class_b_stud1)
class_b_marks.extend(class_b_stud2)
class_b_mean = round(sum(class_b_marks) / len(class_b_marks), 2)

# 10
class_list = list(sample_dict.keys())
mean_class_dict = {
   class_list[0]: class_a_mean,
   class_list[1]: class_b_mean,
}
print(f'10: {mean_class_dict}')

# 11:
max_mean_class = max(mean_class_dict.values())
max_index_cl = list(mean_class_dict.values()).index(max_mean_class)
best_class = list(mean_class_dict.keys())[max_index_cl]

print(f'11: {best_class}: {max_mean_class}')

