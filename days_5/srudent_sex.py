students = ['Male', 'Female', 'female', 'male', 'male', 'male','female', 'male', 'Female', 'Male', 'Female', 'Male', 'female']

male_count = 0
female_count = 0

for student in students:
    if student.lower()=='male':
        male_count +=1
    elif student.lower() == 'female':
        female_count +=1

gender_count = [('male', male_count), ('female' , female_count)]
print(gender_count)