
f1=open("C:\\Users\\hp\\OneDrive\\Desktop\\Pythonworks\\data_sets\\all_students.txt")

failed=open("C:\\Users\\hp\\OneDrive\\Desktop\\Pythonworks\\data_sets\\failed_students.txt")

passed=set()

fail=set()

for line in f1:

    line=line.rstrip("\n")

    passed.add(line)

for line in failed:

    line=line.rstrip("\n")

    fail.add(line)

passed_students=passed.difference(fail)

# print(passed_students)

failed_students=fail.difference(passed_students)

print(failed_students)