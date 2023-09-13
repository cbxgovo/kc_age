# -*- coding: UTF-8 -*-
import pandas as pd

#过滤空白行
def clean():   
    with open('data_source/all_txt_14k.txt', 'r') as f:
        lines = f.readlines()

    filtered_lines = [line.strip() for line in lines if line.strip()]

    with open('out/clean_14k.txt', 'w') as f:
        # 将过滤后的行写入新文件
        f.writelines('\n'.join(filtered_lines))

    print("空白行已过滤并写入新文件。")

# 1 替换部分字符，然后抽取所有含Ma信息单位的子集
def get_all_Ma():
    search_string = " Ma"
    # 打开原始文件以供读取
    with open('out/clean_14k.txt', 'r') as file:
        # 读取文件的所有行
        lines = file.readlines()

    # 打开新文件以供写入
    with open('out/all_Ma.txt', 'w') as output_file:
        # 遍历每一行，查找包含搜索字符串的句子，并写入新文件
        for line in lines:
            line = line.replace(' ca. ',' ca:')   #防止错误分句
            line = line.replace('–','-')
            line = line.replace('-+','±')
            line = line.replace('+/-','±')
            
            if search_string in line:
                output_file.write(line)

    print("匹配的句子已写入新文件。")

#excel 矿床名一列转为列表输出
def out_kc():
    file_path = 'data_source/kc_name.xlsx'  # 替换为你的 Excel 文件路径
    column_name = 'kc_NAME'  # 替换为你要读取的列名

    try:
        df = pd.read_excel(file_path, engine='openpyxl')
        
        if column_name in df.columns:
            column_data = df[column_name].tolist()
            # print(column_data)
            return column_data
        else:
            print(f"Column '{column_name}' not found in the Excel file.")
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == '__main__':
    get_all_Ma() # 1 