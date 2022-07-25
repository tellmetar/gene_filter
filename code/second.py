from openpyxl import load_workbook
wb = load_workbook(filename = 'h.csv')

sheet = wb.active

index = 1
while index < 300:
    
    b1 = sheet['B'+ str(index)]
    d1 = sheet['D'+ str(index)]
    f1 = sheet['F'+ str(index)]
    h1 = sheet['H'+ str(index)]
    j1 = sheet['J'+ str(index)]
    l1 = sheet['L'+ str(index)]
    n1 = sheet['N'+ str(index)]
    p1 = sheet['P'+ str(index)]
    r1 = sheet['R'+ str(index)]

    print(index)


    if int(b1.value) + int(d1.value) + int(f1.value)+ int(h1.value)+ int(j1.value)+ int(l1.value)+ int(n1.value)+ int(p1.value)+ int(r1.value) == 0: 
        sheet.delete_rows(index, 1)
        index -= 1

    index += 1

wb.save(filename = 'h2.xlsx')
