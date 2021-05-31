name = input('your name')
age = input('your age')
sex = input('your sex')

text = ('Hello, my name is ' +  name + '. Im ' + age + ' and Im a ' + sex + '.')
text1 = ('Hello, my name is %s. Im %s. Im %s.') % (name, age, sex)
text2 = ('Hello, my name is {}. Im {}. Im {}'.format(name, age, sex))
about_me_fstring = (f'Hello, my name is {name}. Im {age}. Im {sex}.')

about_me_fstring1 = (about_me_fstring[:25])
about_me_fstring2 = (about_me_fstring[26:32])
about_me_fstring3 = (about_me_fstring[33:])

name1 = 'Lena'
age1 = '23'
sex1 = 'female'

about_me_fstring = about_me_fstring.replace(name, name1)
about_me_fstring = about_me_fstring.replace(age, age1)
about_me_fstring = about_me_fstring.replace(sex, sex1)

list_from_str = about_me_fstring.split()

(type(list_from_str))

str_from_list = (' '.join(list_from_str))

text3 = (about_me_fstring.swapcase())
