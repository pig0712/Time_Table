import WinGUI, Generator, Auto, Modify, File, Judgment

rows = [
    "09:00 ~ 10:30",
    "10:30 ~ 12:00",
    "13:00 ~ 14:30",
    "14:30 ~ 16:00",
    "16:00 ~ 17:30",
]

columns = [
    "월요일",
    "화요일",
    "수요일",
    "목요일",
    "금요일"
]


df = File.ExcelFile.read("./save.xlsx") # 나중에 바꿔야함

# print(df)

window = WinGUI.WindowGen()
window.normal("시간표", x=1000, y=750, xrs=True, yrs=True)

# 시간표 위치 지정
dx = 10
dy = 10

for i in range(5):
    day = Generator.Widget()
    day.LabelWidget(window, columns[i], (dx+111)+(111*i), dy, 15, 4, "black", "solid")

    time = Generator.Widget()
    time.LabelWidget(window, rows[i], dx, (dy+65)+(72*i), 15, 4, "black", "solid")  # 라벨을 먼저 생성

    for j in range(5):
        aa = Generator.Widget()
        aa.ButtonWidget(window, f"{eval(df[columns[i]][j])[1]}\n{eval(df[columns[i]][j])[0]}",
                         (dx + 111)+(111*i), (dy + 65)+(71*j), 15, 4, "#FFFFFF", "solid")

window.run()
