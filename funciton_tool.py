import pandas as pd
import os
from typing import Union
import charset_normalizer

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SAVE_DATA_PATH = os.path.join(BASE_DIR, '新数据.csv')
GET_DATA_PATH = os.path.join(BASE_DIR, '淘宝爆款采集_20230424_172100(1).csv')
global gl_data
gl_data = pd.read_csv(GET_DATA_PATH, keep_date_col=False)


def show_menu():
    print("*" * 80)
    print('{:^65}'.format('欢迎来到淘宝数据分析筛选系统！\n'))
    print("1.对标题进行筛选\t\t2.对销量进行筛选\t\t3.对价格进行筛选")
    print("4.对类型进行筛选\t\t5.对卖家旺旺进行筛选\t\t6.对一级类目进行筛选")
    print("7.对子类目进行筛选\t\t8.对多级类目进行筛选\t\t9.对关键词进行筛选")
    print("10.退出系统")
    print("请根据屏幕的提示语句选择你的操作")
    print("*" * 80)


def kw_upload_manual(kw_colum_name: str, keywords_list: list = []):
    while True:
        keywords = input(f"请输入对{kw_colum_name}的搜索词：")
        keywords_list.append(keywords)
        print("请问还需要继续添加搜索词吗？ y/n")
        action_str = input()
        if action_str.upper() == "Y":
            continue
        else:
            break
    return keywords_list


def kw_upload_file(kw_colum_name: str, keywords_list: list = []):
    while True:
        file_name = input(f"请输入对{kw_colum_name}搜索词文件名字：")
        key_words_path = os.path.join(BASE_DIR, f"{file_name}.txt")
        with open(key_words_path, 'rb') as f:
            encoding = charset_normalizer.detect(bytearray(
                f.read()))['encoding']
        with open(key_words_path, mode='r', encoding=encoding) as file:
            for line in file:
                line = line.strip()
                if line:
                    keywords_list.append(line)
        print("请问还需要继续添加搜索词吗？ y/n")
        action_str = input()
        if action_str.upper() == "Y":
            continue
        else:
            break
    return keywords_list


def save_data(new_data: pd.DataFrame, old_data: pd.DataFrame, column_name: str,
              keywords_list: list, keep_data: bool):
    if keep_data:
        if os.path.exists(SAVE_DATA_PATH):
            old_data = pd.read_csv(SAVE_DATA_PATH, keep_default_na=False)
            old_data = old_data[old_data[column_name].str.contains(
                '|'.join(keywords_list), regex=True, na=False)]
            old_data.to_csv(SAVE_DATA_PATH, mode="w", index=False)
            print("数据筛选成功！！已经保存")
        else:
            new_data = new_data[new_data[column_name].str.contains(
                '|'.join(keywords_list), regex=True, na=False)]
            new_data.to_csv(SAVE_DATA_PATH, mode="w", index=False)
            print("数据已经筛选完成，已经创建新的csv文件！")
    else:
        if os.path.exists(SAVE_DATA_PATH):
            old_data = pd.read_csv(SAVE_DATA_PATH, keep_default_na=False)
            old_data = old_data[~old_data[column_name].str.contains(
                '|'.join(keywords_list), regex=True, na=False)]
            old_data.to_csv(SAVE_DATA_PATH, mode="w", index=False)
            print("数据筛选成功！！已经保存")
        else:
            new_data = new_data[~new_data[column_name].str.contains(
                '|'.join(keywords_list), regex=True, na=False)]
            new_data.to_csv(SAVE_DATA_PATH, mode="w", index=False)
            print("数据已经筛选完成，已经创建新的csv文件！")


def num_input(num_str: str = ""):
    while True:
        try:
            if num_str:
                new_num = input(num_str)
            else:
                new_num = input("请输入你指定的数值：(不输入的话默认是400): ")
                if not new_num:
                    return float(400)
                else:
                    return float(new_num)
        except ValueError:
            print("输入错误，请重新输入数字")


def str_filter(
    str_column_name: str,
    str_new_data: Union[pd.DataFrame, None] = None,
    str_old_data: Union[pd.DataFrame, None] = None,
):
    while True:
        print(f"请问你要对{str_column_name}作何种筛选？")
        print("1.删除指定行\t\t2.保留指定行")
        choice_str = input("")
        keywords_list = []
        if choice_str == "1":
            print("你选择对%s列进行删除筛选" % str_column_name)
            print(f"请选择上传{str_column_name}搜索词的方式：1.手动输入\t\t\t2.批量上传")
            operation_choice = input()
            if operation_choice == "1":
                keywords_list = kw_upload_manual(str_column_name)
                save_data(new_data=str_new_data,
                          old_data=str_old_data,
                          column_name=str_column_name,
                          keywords_list=keywords_list,
                          keep_data=False)
            elif operation_choice == "2":
                keywords_list = kw_upload_file(str_column_name)
                save_data(new_data=str_new_data,
                          old_data=str_old_data,
                          column_name=str_column_name,
                          keywords_list=keywords_list,
                          keep_data=False)
            break

        elif choice_str == "2":
            print("你选择对%s列进行保留筛选" % str_column_name)
            print(f"请选择上传{str_column_name}搜索词的方式：1.手动输入\t\t\t2.批量上传")
            operation_choice = input()
            if operation_choice == "1":
                keywords_list = kw_upload_manual(str_column_name)
                save_data(new_data=str_new_data,
                          old_data=str_old_data,
                          column_name=str_column_name,
                          keywords_list=keywords_list,
                          keep_data=True)
            elif operation_choice == "2":
                keywords_list = kw_upload_file(str_column_name)
                save_data(new_data=str_new_data,
                          old_data=str_old_data,
                          column_name=str_column_name,
                          keywords_list=keywords_list,
                          keep_data=True)
            break
        else:
            print("你的输入有误，请按屏幕的提示信息选择你要进行的操作")
            continue


def num_filter(num_colum_name: str, num_data: pd.DataFrame, num_str: str = ""):
    while True:
        print("请问你需要对%s这一列作哪一种筛选？" % num_colum_name)
        print("1.删除数值大于我的指定值的行\t\t2.删除数值小于我的指定值的行")
        print("3.删除数值等于我的指定值的行\t\t4.保留数值等于我的指定值的行")
        choice_str = input()
        num = num_input(num_str)
        if os.path.exists(SAVE_DATA_PATH):
            num_data = pd.read_csv(SAVE_DATA_PATH, keep_default_na=False)
        else:
            pass
        if choice_str == "1":
            num_data = num_data[~num_data[num_colum_name].ge(float(num))]
            break
        elif choice_str == "2":
            num_data = num_data[num_data[num_colum_name].ge(float(num))]
            break
        elif choice_str == "3":
            num_data = num_data[~num_data[num_colum_name].eq(float(num))]
            break
        elif choice_str == "4":
            num_data = num_data[num_data[num_colum_name].eq(float(num))]
            break
        else:
            print("你的输入有误，请按屏幕的提示信息选择你所需要的操作")
            continue
    num_data.to_csv(SAVE_DATA_PATH, mode="w", index=False)
    print("数据筛选成功！！已经保存")
