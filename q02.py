# Title
print('-'*30)
print('{:^25}'.format('員工薪資輸入'))
print('{:^20}'.format('若姓名處未輸入則代表結束'))
print('-'*30)

staff = []

while True:
    name = str(input('請輸入姓名:'))
    if not name: break
    salary = float(input('請輸入薪資:'))
    staff.append({"eName":name, "eSalary":salary})
    print()

print('-'*30)

sumSalary = 0.0
for item in staff:
    print(f'員工{item["eName"]:<10}的薪資為{item["eSalary"]:>12,.2f}')
    sumSalary += item["eSalary"]
staffNum = len(staff) if len(staff) > 0 else 1
avgSalary = sumSalary / staffNum

print('-'*30)

print(f'合計薪資{sumSalary:>15,.2f}')
print(f'平均薪資{avgSalary:>15,.2f}')

print('='*30)