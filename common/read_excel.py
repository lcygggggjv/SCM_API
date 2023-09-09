import openpyxl
from openpyxl.worksheet.worksheet import Worksheet
import yaml


def read_excel(file_path, sheet_name='Sheet1'):

    work_book = openpyxl.load_workbook(file_path)

    # 类型注解， Worksheet类型
    sheet: Worksheet = work_book[sheet_name]

    data = list(sheet.values)

    title = data[0]

    rows = data[1:]

    datas = [dict(zip(title, row)) for row in rows]

    return datas


def read_yaml():
    with open(file=r'D:\project_git\SCM_API\test_case\material_case\test_data.yaml', encoding='utf-8') as f:
        # 多个用例用safe_load_all，转换成list，否则返回的是对象
        cases = list(yaml.safe_load_all(f))

        return cases


if __name__ == '__main__':

    sd = read_yaml()
    sds = sd[0]["data"]["age"]
    # sd3 = sd[1]["data"]["age"]
    print(sd)
    # print(type(sds))
    #
    # # print(type(sd3))
