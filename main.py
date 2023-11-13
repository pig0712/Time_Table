import WinGUI, Generator

window = WinGUI.WindowGen()
window.normal("시간표", x=1000, y=750, xrs=True, yrs=True)

for i in range(1,7):
    time = Generator.Widget()
    time.LabelWidget(window, "시간표", 100, 50, 10, 5, "black", "solid")  # 라벨을 먼저 생성

window.run()