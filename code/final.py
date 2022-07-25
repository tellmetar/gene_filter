import os
from shutil import copyfile


# 批量删除文件

# file_list = os.listdir("./")
# for file in file_list:
#     if file.endswith(".txt.result"):
#         os.remove(file)


# 取两列

# file_list = os.listdir("../GSE119101")
# for file in file_list:
#     if file.endswith(".txt"):
#         print(file)
#         with open("../GSE119101/" + file, encoding="utf-8") as file2, open(
#             file, mode="w"
#         ) as tempFile:
#             line = file2.readline()
#             line = file2.readline()
#             while line:
#                 line = file2.readline()
#                 rowData = line.split("\t")
#                 tempFile.write(rowData[0] + "\t" + rowData[-1])

# 遍历文件夹

file_list = os.listdir(".")
txt_file_list = []
for txtfile in file_list:
    if txtfile.endswith(".txt"):
        txt_file_list.append(txtfile)


# 复制文件

# copyfile( txt_file_list[0], txt_file_list[0] + ".result" )


# 过滤部分缺失基因， 一一对齐

# for i in range(1, len(txt_file_list)):
#     print(txt_file_list[i])
#     with open("./" + txt_file_list[i-1] + ".result", mode="r") as file, open("./" + txt_file_list[i]) as file2, open("./" + txt_file_list[i]+".result", mode="w" ) as wf:
#         line = file.readline()
#         while line:
#             key = line.split("\t")[0]
#             line2 = file2.readline()
#             key2 = line2.split("\t")[0]
#             if key == key2:
#                 wf.write(line.rstrip() + "\t" + line2.split("\t")[-1])
#             else:
#                 # print("===" + key)
#                 file2.seek(0, 0)
#                 line2 = file2.readline()
#                 # print("===>" + line2)
#                 while line2:
#                     if line2.split("\t")[0] == key:
#                         # print("+++" + line + line2.split("\t")[-1])
#                         wf.write(line.rstrip() + "\t" + line2.split("\t")[-1])
#                         break
#                     line2 = file2.readline()

#             line = file.readline()


# 过滤全0基因

with open("./" + txt_file_list[-1] + ".result") as file, open("./final_result", mode="w") as wf:
    line = file.readline()
    lineNum = 0
    while line: 
        lineList = line.split("\t")
        sum = 0
        lineNum+=1
        for i in range(1, len(lineList)):
            if (not lineList[i] == ""):
                sum = sum + int(lineList[i])
            else:
                print(line)
        if not sum == 0:
            wf.write(line)
        line = file.readline()
