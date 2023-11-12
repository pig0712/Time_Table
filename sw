import pandas as pd

# Excel 파일 불러오기
excel_file = pd.read_excel('나라.xlsx')

# Excel 파일의 특정 시트를 불러오려면 시트 이름 또는 인덱스를 지정할 수 있습니다.
# 예를 들어, 시트 이름이 'Sheet1'인 경우:
# excel_file = pd.read_excel('파일이름.xlsx', sheet_name='Sheet1')

# 데이터를 확인
print(excel_file)
