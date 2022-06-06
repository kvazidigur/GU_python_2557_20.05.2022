tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А']

students = ((tutors[idx], klasses[idx] if len(klasses) >= idx + 1 else None) for idx in range(0, len(tutors)))

print(type(students))

for i in range(0, len(tutors)):
    print(next(students))
