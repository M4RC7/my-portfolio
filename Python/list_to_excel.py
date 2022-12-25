import xlsxwriter

workbook = xlsxwriter.Workbook('write_list.xlsx')
worksheet = workbook.add_worksheet()

my_list = [[1, 1, 1, 1, 1],
           [2, 2, 2, 2, 1],
           [3, 3, 3, 3, 1],
           [4, 4, 4, 4, 1],
           [5, 5, 5, 5, 1]]

for row_num, row_data in enumerate(my_list):
    for col_num, col_data in enumerate(row_data):
        worksheet.write(row_num, col_num, col_data)

workbook.close()