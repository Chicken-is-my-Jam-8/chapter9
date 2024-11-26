employees = {
        'Alice':{'age':25,'department':'Sales'},
        'Bob':{'age':30,'department':'Marketing'},
        'Charlie':{'age':28,'department':'Sales'},
        'Daisy':{'age':22,'department':'IT'},
        }
sales_personel = {}
for x, y in employees.items():
    for a in y.values():
        if a == 'Sales':
            sales_personel[x] = y

print(sales_personel)
