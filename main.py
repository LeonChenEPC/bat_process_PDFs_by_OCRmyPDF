# 导入os模块和sys模块
import os
import sys

# 提示程序运行所需的第三方开源免费软件，提醒用户提前安装OCRmyPDF。
print("本程序通过调用OCRmyPDF进行OCR转换，请先安装开源的OCRmyPDF软件。")
print("将调用命令：ocrmypdf --force-ocr -l eng+chi_sim \"输入文件名.pdf\" \"输出文件名.pdf\"")
print("开源的OCRmyPDF软件，在windows/linux/macOS上都能免费安装。")
print("扫描版的PDF，经过OCRmyPDF的OCR转换之后，能够在全文搜索其内容")
print("----------------------------------------------------")

# 获取当前所在的工作目录
path = os.getcwd()
print("本程序将批量转换当前工作目录:")
print(path)
print("中的PDF文件。")

# 由于OCRmyPDF转换非常耗费时间，请删除无需转换的PDF文件。
# 提示用户删除这些文件，防止重复转换浪费时间
print("由于OCRmyPDF转换非常耗费时间，最好先删除无需转换的PDF文件。")
print("如果一个PDF文件的文件名中包含OCR，本程序认为它已经被转换过了。")
print("----------------------------------------------------")

# 计算发现了多少个PDF文件，是否有些PDF文件名已经包含了OCR字符串。
# 获取文件列表+检测文件名称+等待用户决定的循环。
while True:
    # 获取程序所在文件夹中所有的文件名，生成一个文件名列表
    filelist = os.listdir()

    # 文件夹中pdf文件数量的计数器
    pdf_count = 0
    pdf_count_no_OCR = 0
    pdf_count_with_OCR = 0

    # 统计PDF文件的数量
    for i in filelist:
        if i.endswith('pdf'):
            pdf_count += 1
            # 统计文件名中不包含OCR字符串的PDF文件数量
            if (i.find("OCR") == -1) and (i.find("ocr") == -1):
                pdf_count_no_OCR += 1

    # 计算文件名中已经带有OCR字符的PDF文件的数量。
    pdf_count_with_OCR = pdf_count - pdf_count_no_OCR

    print("总共发现", pdf_count, "个PDF文件。")
    print("其中有", pdf_count_with_OCR, "个PDF文件的文件名包含OCR，它们将不被执行OCRmyPDF转换。")
    if pdf_count_with_OCR > 0:
        print("这些pdf文件的文件名中包含OCR，他们可能已经被转换过了")
    print("还有", pdf_count_no_OCR, "个PDF文件的文件名不包含OCR，它们将执行OCRmyPDF转换。")

    print("----------------------------------------------------")
    print("输入Y.转换已知的PDF文件。注意：它将不转换文件名中带有OCR的PDF文件")
    print("输入N.手动调整哪些需要转换的PDF文件。程序会暂停等待。")
    print("输入其他任意字符串，退出程序")
    print("----------------------------------------------------")

    str_choice = input("让请输你的选择：")
    if str_choice == "y" or str_choice == "Y":
        break
    elif str_choice == "n" or str_choice == "N":
        print("等待用户手动调整调整，完成后按任意键继续。")
        input()
    else:
        print("输入了Y和N之外的其他字符，程序退出。")
        sys.exit()

# 刷新文件列表
filelist = os.listdir()
# 打印提示
print("本程序不转换文件名中带有OCR的PDF文件")

# 对文件名列表中的所有PDF文件调用OCRmyPDF进行转换。
for i in filelist:
    # 判断这些文件是不是pdf文件，判断文件名是否包含OCR。
    if i.endswith('pdf') and i.find('OCR') == -1 and i.find('ocr') == -1:
        # 获取要进行ocr转换的文件的文件名
        input_file_name = '\"' + i + '\"'
        # 设置转换后的文件名为 OCR+源文件名
        output_file_name = '\"OCR' + i + '\"'

        # 检查是否有文件已经被转换过，产生了重名的文件。
        already_done_flag = 0
        for any_file in filelist:
            if output_file_name == ('\"' + any_file + '\"'):
                print(input_file_name, "这个文件已经被转换过了，有一个对应的文件", output_file_name)
                already_done_flag = 1

        if already_done_flag != 1:
            # 显示将要转换文件
            print("现在转换文件", input_file_name, ", 如果转换成功,输出文件保存为", output_file_name)
            # 用原文件名 和 转换后要存的文件名 组合出 ocrmypdf命令行
            command = "ocrmypdf --force-ocr -l eng+chi_sim " + input_file_name + " " + output_file_name
            # 通过os模块，在cmd里面调用ocrmypdf的命令行
            os.system(command)

print("----------------------------------------------------")
print("所有的可以执行的转换已经完成！")
print("如果某个PDF文件无法通过OCRmyPDF转换，会有错误提示")
