persons = {
        'Danny':'New Yourk',
        'ben':'New Jersey',
        'Bob':'Chicago',
        'Tom':'Houston',
        'Sam':'Phoenix',
        'Tim':'Philadelphia',
        'Nancy':'Chicago'
        }
chicago = []
for x, y in persons.items():
    if y == 'Chicago':
        chicago.append(x)
print(chicago)
