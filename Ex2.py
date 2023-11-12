employees = {}
name_list = []

print("----------------------------")
print("{:^23s}".format("員工薪資輸入"))
print("{:^20s}".format("若姓名處未輸入則代表結束"))
print("----------------------------")

while True:
    name = input("請輸入姓名: ")
    if not name:
        break

    name_list.append(name)
    money = input("請輸入薪資: ")
    employees[name] = int(money)
    print()

print("----------------------------")

for name, salary in employees.items():
    print(f'員工 {name} 的薪資為 {format(salary, ",")}')

print("----------------------------")

total_salary = sum(employees.values())
average_salary = round(total_salary / len(employees), 2)

print(f'合計薪資: {format(total_salary, ","):>10}')
print(f'平均薪資: {format(average_salary, ","):>10}')