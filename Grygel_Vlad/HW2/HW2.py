# 1. Вывести значение ключа "name";
# 2. Вывести значение ключа "history";
# 3. Добавить нового студента в "class_a", соответственно его "name" и "marks";
# 4. Добавить новый класс со студентами (в sample_dict нужно добавить class_b, в котором будет 2 студента);
# 5. Добавить каждому студенту в "marks" предмет "physics" с оценкой;
# 6. Подсчитать средний бал по каждому студенту (результат округлить до 2 знаков после запятой);
# 7. Создать словарь со средним баллом за каждого студента;
# 8. Определить лучшего студента по успеваемости;
# 9. Подсчитать средний бал по каждому классу (результат округлить до 2 знаков после запятой);
# 8. Создать словарь со средним баллом за классы;
# 9. Определить лучший класс по успеваемости.

sample_dict = {
   'class_a': {
      'student1': {
         'name': 'Misha',
         'marks': {
            'math': 90,
            'history': 85
         }
      }
   }
}

# 1.
print(sample_dict.get('class_a').get('student1').get('name'))


# 2.
print(sample_dict['class_a']['student1']['marks']['history'])


# 3.
dict_student2 = {'student2': dict(name='Sasha',
                                  marks=dict(math=93, history=75))}
sample_dict['class_a'].update(dict_student2)
print(sample_dict)


# 4.
dict_class_b = {'class_b': dict(student1={'name': 'Olia'},
                                student2={'name': 'Kostya'},)}
sample_dict.update(dict_class_b)
print(sample_dict)


# 5.
sample_dict['class_a']['student1']['marks']['physics'] = 83
sample_dict['class_a']['student2']['marks']['physics'] = 84
sample_dict['class_b']['student1']['marks']['physics'] = 72
sample_dict['class_b']['student2']['marks']['physics'] = 97
print(sample_dict)


# 6.

cl_a_st1 = round(sum(sample_dict['class_a']['student1']['marks'].values())
    / len(sample_dict['class_a']['student1']['marks'].values()), 2)

cl_a_st2 = round(sum(sample_dict['class_a']['student2']['marks'].values())
    / len(sample_dict['class_a']['student2']['marks'].values()), 2)

cl_b_st1 = round(sum(sample_dict['class_b']['student1']['marks'].values())
    / len(sample_dict['class_b']['student1']['marks'].values()), 2)

cl_b_st2 = round(sum(sample_dict['class_b']['student2']['marks'].values())
    / len(sample_dict['class_b']['student2']['marks'].values()), 2)


# 7.

averange_skore = {'class_a_student1': cl_a_st1,
                  'class_a_student2': cl_a_st2,
                  'class_b_student1': cl_b_st1,
                  'class_b_student2': cl_b_st2, }
print(averange_skore)

# 8.

best_student = max(averange_skore.keys(), key=averange_skore.get)
print(best_student)

# 9.

A_av_sk = list(sample_dict['class_a']['student1']['marks'].values())
A_av_sk.extend(list(
    sample_dict['class_a']['student2']['marks'].values()))
total_a = round(sum(A_av_sk) / len(A_av_sk), 2)
print(total_a)

B_av_sk = list(sample_dict['class_b']['student1']['marks'].values())
B_av_sk.extend(list(
    sample_dict['class_b']['student2']['marks'].values()))
total_b = round(sum(B_av_sk) / len(B_av_sk), 2)
print(total_b)

# 10.

class_skore = {
    'class_a': total_a,
    'class_b': total_b,
}
print(class_skore)

# 11.

best_class = max(class_skore.keys(), key=class_skore.get)
print(best_class)
