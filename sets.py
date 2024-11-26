baseball = set(['Jodi', 'Carmen', 'Aida', 'Alicia'])
basketball = set(['Eva', 'Carmen', 'Alicia', 'Sarah'])
print("The following students are on the baseball team:")
for x in baseball:
    print(x)

print()
print("The following students are on the bascketball team:")
for x in basketball:
    print(x)

print()
bothsets = baseball.intersection(basketball)
print("The following students play both baseball and basketball:")
for x in bothsets:
    print(x)

print()
eitherset = baseball.union(basketball)
print("The following students play either baseball or basketball:")
for x in eitherset:
    print(x)

print()
only_baseball = baseball.difference(basketball)
print("The following students play baseball, but not basketball:")
for x in only_baseball:
    print(x)

print()
only_basketball = basketball.difference(baseball)
print("The following students play basketball, but not baseball:")
for x in only_basketball:
    print(x)

print()
or_set = baseball.symmetric_difference(basketball)
print("The following students play one sport, but noth both:")
for x in or_set:
    print(x)
