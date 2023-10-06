import re

def replace_and_save(input_file, output_file):
    try:
        # 读取原始文本文件
        with open(input_file, 'r',encoding='UTF-8') as file:
            content = file.read()

        # 使用正则表达式替换大写字母"AE"为"±"
        replaced_content = re.sub(r'AE', '±', content)

        # 将替换后的内容保存到新文本文件
        with open(output_file, 'w',encoding='UTF-8') as file:
            file.write(replaced_content)

        print('替换完成并保存到新文件。')
    except FileNotFoundError:
        print('文件不存在。')

# 输入文件和输出文件的路径
# input_file_path = 'out/AE_test.txt'  # 替换为实际的文件路径
# output_file_path = 'out/AE_test_out.txt'  # 替换为实际的文件路径
input_file_path = 'out/all_Ma_out.txt'  # 替换为实际的文件路径
output_file_path = 'out/all_Ma_out_quAE.txt'  # 替换为实际的文件路径

# 调用函数进行替换和保存
replace_and_save(input_file_path, output_file_path)



