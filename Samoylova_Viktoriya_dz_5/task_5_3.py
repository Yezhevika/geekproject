from itertools import islice, zip_longest

tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

couples = (i for i in zip_longest(tutors, klasses))

print(type(couples))
print(*(islice(couples, 100)))
print(list(islice(couples, 1)))
