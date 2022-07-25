import xlsxwriter

workbook = xlsxwriter.Workbook('h.csv')
worksheet = workbook.add_worksheet()

with open('../GSE119101/GSM3358028_170036_II_1_S8_L001.txt', encoding='utf-8') as file:
    line = file.readline()
    print(line)
    line = file.readline()
    print(line)

    print("-------------")
    row = 0
    col = 0
    while line:
        # if row > 3000:
        #     break
        line = file.readline()

        rowData = line.split("\t")
        # print(rowData[0], rowData[-1])
        worksheet.write_string(row,col,     rowData[0])
        worksheet.write_string(row,col +1,  rowData[-1])
        row += 1

with open('../GSE119101/GSM3358029_170036_II_2_S10_L001.txt', encoding='utf-8') as file2:
    line2 = file2.readline()
    line2 = file2.readline()

    print("-------------")
    row2 = 0
    col2 = 2
    while line2:
        # if row > 3000:
        #     break
        line2 = file2.readline()

        rowData2 = line2.split("\t")
        # print(rowData[0], rowData[-1])
        # worksheet.write_string(row2,col2,     rowData2[0])
        worksheet.write_string(row2,col2 +1,  rowData2[-1])
        row2 += 1

with open('../GSE119101/GSM3358030_170036_II_3_S3_L001.txt', encoding='utf-8') as file3:
    line3 = file3.readline()
    line3 = file3.readline()

    print("-------------")
    row3 = 0
    col3 = 4
    while line3:
        # if row > 3000:
        #     break
        line3 = file3.readline()

        rowData3 = line3.split("\t")
        # print(rowData[0], rowData[-1])
        # worksheet.write_string(row3,col3,     rowData3[0])
        worksheet.write_string(row3,col3 +1,  rowData3[-1])
        row3 += 1

with open('../GSE119101/GSM3358031_170036_II_4_S4_L001.txt', encoding='utf-8') as file4:
    line4 = file4.readline()
    line4 = file4.readline()

    print("-------------")
    row3 = 0
    col3 = 6
    while line4:
        # if row > 3000:
        #     break
        line4 = file4.readline()

        rowData3 = line4.split("\t")
        # print(rowData[0], rowData[-1])
        # worksheet.write_string(row3,col3,     rowData3[0])
        worksheet.write_string(row3,col3 +1,  rowData3[-1])
        row3 += 1


with open('../GSE119101/GSM3358032_170036_II_5_S5_L001.txt', encoding='utf-8') as file5:
    line5 = file5.readline()
    line5 = file5.readline()

    print("-------------")
    row3 = 0
    col3 = 8
    while line5:
        # if row > 3000:
        #     break
        line5 = file5.readline()

        rowData3 = line5.split("\t")
        # print(rowData[0], rowData[-1])
        # worksheet.write_string(row3,col3,     rowData3[0])
        worksheet.write_string(row3,col3 +1,  rowData3[-1])
        row3 += 1


with open('../GSE119101/GSM3358033_170036_II_6_S6_L001.txt', encoding='utf-8') as file5:
    line5 = file5.readline()
    line5 = file5.readline()

    print("-------------")
    row3 = 0
    col3 = 10
    while line5:
        # if row > 3000:
        #     break
        line5 = file5.readline()

        rowData3 = line5.split("\t")
        # print(rowData[0], rowData[-1])
        # worksheet.write_string(row3,col3,     rowData3[0])
        worksheet.write_string(row3,col3 +1,  rowData3[-1])
        row3 += 1


with open('../GSE119101/GSM3358034_170036_II_7_S7_L001.txt', encoding='utf-8') as file5:
    line5 = file5.readline()
    line5 = file5.readline()

    print("-------------")
    row3 = 0
    col3 = 12
    while line5:
        # if row > 3000:
        #     break
        line5 = file5.readline()

        rowData3 = line5.split("\t")
        # print(rowData[0], rowData[-1])
        # worksheet.write_string(row3,col3,     rowData3[0])
        worksheet.write_string(row3,col3 +1,  rowData3[-1])
        row3 += 1



with open('../GSE119101/GSM3358035_170036_II_8_S9_L001.txt', encoding='utf-8') as file5:
    line5 = file5.readline()
    line5 = file5.readline()

    print("-------------")
    row3 = 0
    col3 = 14
    while line5:
        # if row > 3000:
        #     break
        line5 = file5.readline()

        rowData3 = line5.split("\t")
        # print(rowData[0], rowData[-1])
        # worksheet.write_string(row3,col3,     rowData3[0])
        worksheet.write_string(row3,col3 +1,  rowData3[-1])
        row3 += 1



with open('../GSE119101/GSM3358036_170036_II_9_S1_L001.txt', encoding='utf-8') as file5:
    line5 = file5.readline()
    line5 = file5.readline()

    print("-------------")
    row3 = 0
    col3 = 16
    while line5:
        # if row > 3000:
        #     break
        line5 = file5.readline()

        rowData3 = line5.split("\t")
        # print(rowData[0], rowData[-1])
        # worksheet.write_string(row3,col3,     rowData3[0])
        worksheet.write_string(row3,col3 +1,  rowData3[-1])
        row3 += 1



workbook.close()