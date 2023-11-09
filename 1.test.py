import tkinter as tk
from tkinter import messagebox as ms
import random as rd
################################ 시간표 틀 #################################

def frame():
    global timetable

    if hasattr(frame, "window"):
        frame.window.destroy()

    frame.window = tk.Tk()
    frame.window.title("인공지능학과 시간표")
    frame.window.geometry("1000x1000")
    frame.window.resizable(True, True)

    t = [
        "1교시 09:00 ~ 10:30",
        "2교시 10:30 ~ 12:00",
        "3교시 13:00 ~ 14:30",
        "4교시 14:30 ~ 16:00",
        "5교시 16:00 ~ 17:30",
        "6교시 17:30 ~ 19:00"
    ]

    d = [
        "월요일",
        "화요일",
        "수요일",
        "목요일",
        "금요일",
    ]

    for column in range(1, 6):
        day = tk.Button(frame.window, width=15, height=5, relief="sunken",
                        text=d[column - 1], bg="#ABDEE6", activebackground="#ABDEE6")
        day.place(x=(column + 1) * 115 + 20, y=0)

        for row in range(1, 7):
            globals()[f"object_{column}_{row}"] = tk.Button(frame.window, width=15, height=5, relief="groove",text=f"{timetable[column][row][0]}\n{timetable[column][row][1]}\n{timetable[column][row][2]}", command = lambda column=column, row=row : modify_GUI(column,row))
            globals()[f"object_{column}_{row}"].place(x=(column + 1) * 115 + 20, y=row * 85)

            time = tk.Button(frame.window, text=t[row - 1], relief="sunken",width=20, height=5, bg="#FFFFB5", activebackground="#FFFFB5")
            time.place(x=100, y=row * 85)

    import_button = tk.Button(frame.window,width=15,height=2,relief="groove",text="시간표 불러오기",bg="#FFECB3", command = import_file_GUI)
    import_button.place(x=50, y=650)

    save_button = tk.Button(frame.window, width=15, height=2, relief="groove",text="시간표 저장하기", bg="#FFECB3", command=file_save_GUI)
    save_button.place(x=200, y=650)

    save_button = tk.Button(frame.window, width=15, height=2, relief="groove",text="시간표 자동 생성", bg="#FFECB3", command=time_rand_GUI)
    save_button.place(x=350, y=650)

    frame.window.mainloop()

################################ 시간표 불러오기 #################################

# - 파일 불러오기
def file_read(event):
    global timetable

    file_name = input_path.get()
    input_path.delete(0, len(file_name))
    file_name = f"./{file_name}.txt"

    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            timetable = eval(file.read())


    except :
        print(timetable)
        ms.showwarning("경고","파일이 없거나 파일명이 잘못되어 기본값으로 설정되었습니다.")
        Nn = ["없음", "없음", "없음"]
        timetable = {i: {j: list(Nn) for j in range(1, 7)} for i in range(1, 6)}

    frame()


# - GUI
def import_file_GUI():
    global input_path

    import_file = tk.Toplevel()
    import_file.title("파일 불러오기 (txt)")
    import_file.geometry("250x200")
    import_file.resizable(False, False)
    import_file.grab_set()  # 모달 대화 상자로 설정

    input_path_label = tk.Label(import_file,text="파일명 작성후 엔터를 눌러주세요")
    input_path_label.place(x=30,y=30)

    input_path = tk.Entry(import_file)
    input_path.place(x=45,y=60)
    input_path.bind("<Return>", file_read) # 실행시 이벤트 객체 전달
    import_file.mainloop()

################################ 시간표 수정 #################################

def modify_GUI(column,row):
    g_name = []
    g_subject = []
    g_place = []

    def subject_modify(event):
        sub = subject.get()
        timetable[column][row][0] = sub
        globals()[f"object_{column}_{row}"].config(text=f"{timetable[column][row][0]}\n{timetable[column][row][1]}\n{timetable[column][row][2]}")
        g_subject.append(f"{column}_{row}_{sub}")
        judgment()

    def name_modify(evnet):
        na = name.get()
        timetable[column][row][1] = na
        globals()[f"object_{column}_{row}"].config(text=f"{timetable[column][row][0]}\n{timetable[column][row][1]}\n{timetable[column][row][2]}")
        g_name.append(f"{column}_{row}_{na}")
        judgment()

    def place_modify(evnet):
        pl = place.get()
        timetable[column][row][2] = pl
        globals()[f"object_{column}_{row}"].config(text=f"{timetable[column][row][0]}\n{timetable[column][row][1]}\n{timetable[column][row][2]}")
        g_place.append(f"{column}_{row}_{pl}")

    window_modify = tk.Toplevel()
    window_modify.title("시간표 수정")
    window_modify.geometry("250x250+0+0")
    window_modify.resizable(False, False)
    window_modify.grab_set()

    if column == 1: day = "월요일"
    elif column == 2: day = "화요일"
    elif column == 3: day = "수요일"
    elif column == 4: day = "목요일"
    elif column == 5: day = "금요일"

    new = tk.Label(window_modify,text=f"{day} {row}교시")
    new.place(x=75, y=200)

    tk.Label(window_modify,text="과목명").place(x=25,y=0)
    subject = tk.Entry(window_modify)
    subject.insert(0,timetable[column][row][0])
    subject.place(x=25, y=30)
    subject.bind("<Return>",subject_modify)

    tk.Label(window_modify,text="교수님 이름").place(x=25,y=60)
    name = tk.Entry(window_modify)
    name.insert(0,timetable[column][row][1])
    name.place(x=25,y=90)
    name.bind("<Return>",name_modify)

    tk.Label(window_modify,text="강의실").place(x=25,y=120)
    place = tk.Entry(window_modify)
    place.insert(0,timetable[column][row][2])
    place.place(x=25,y=150)
    place.bind("<Return>",place_modify)

    window_modify.mainloop()

################################ 시간표 저장 #################################
def file_save(event):
    path = output_path.get()
    path = f"./{path}.txt"

    print(timetable)
    try:
        with open(path, 'w', encoding='utf-8') as file:
            file.write(str(timetable))
        ms.showinfo("저장 완료!","현재 경로에 저장되었습니다. ")

    except :
        ms.showerror("저장 실패","파일 경로가 올바르지 않거나, 파일 저장중에 오류가 생겼습니다.")

# - GUI
def file_save_GUI():
    global output_path

    file_save_win = tk.Toplevel()
    file_save_win.title("시간표 저장")
    file_save_win.geometry("250x250+0+0")
    file_save_win.resizable(False, False)
    file_save_win.grab_set()

    input_path_label = tk.Label(file_save_win,text="파일명 작성후 엔터를 눌러주세요")
    input_path_label.place(x=30,y=30)

    output_path = tk.Entry(file_save_win)
    output_path.place(x=45,y=60)
    output_path.bind("<Return>", file_save) # 실행시 이벤트 객체 전달

    file_save_win.mainloop()

################################ 경고창 #################################

def judgment():

    # 같은날 중복된 과목 확인하는 코드
    duplicates_1 = set()
    for i in range(1, 6):  # 월요일부터 금요일까지
        subjects_1 = set()  # 각 요일별로 중복된 과목을 저장할 세트

        for j in range(1, 7):  # 1교시부터 6교시까지
            subject_name_1 = timetable[i][j][0]

            if subject_name_1 != "없음":  # "없음"이 아닌 경우에만 처리
                if subject_name_1 in subjects_1:
                    duplicates_1.add(subject_name_1)
                else:
                    subjects_1.add(subject_name_1)

    if duplicates_1:
        # 중복된 과목이 있는 경우, 경고 팝업을 띄워줄 수 있습니다.
        ms.showwarning("중복된 과목 발견", "다음 과목이 중복되었습니다 /// " + ", ".join(duplicates_1))



    # 같은날 특정 교수님 수업 3교시 이상이면 경고창
    duplicates_2 = set()
    for i in range(1, 6):  # 월요일부터 금요일까지
        dup_name_1 = set()  # 각 요일별로 중복된 과목을 저장할 세트
        dup_name_2 = set()

        for j in range(1, 7):  # 1교시부터 6교시까지
            name = timetable[i][j][1]

            if name != "없음":  # "없음"이 아닌 경우에만 처리
                if name in dup_name_1:
                    if name in (dup_name_1 & dup_name_2):
                        duplicates_2.add(name)
                    else:
                        dup_name_2.add(name)
                else:
                    dup_name_1.add(name)

    if duplicates_2 :
        # 중복된 과목이 있는 경우
        ms.showwarning("경고", f"같은날에 {str(duplicates_2)[2:-2]}교수님의 수업이 많이 배정되었습니다.")


    # 시간표 전체에서 할당된 과목이 3교시 이상일시
    subject_count = {}

    # 시간표를 순회하면서 중복된 과목을 찾음
    for i in range(1, 6):  # 월요일부터 금요일까지
        for j in range(1, 7):  # 1교시부터 6교시까지
            subject = timetable[i][j][0]  # 과목명 가져오기

            if subject != "없음":  # "없음"이 아닌 경우에만 처리
                if subject in subject_count:
                    subject_count[subject] += 1
                else:
                    subject_count[subject] = 1

    # 중복 횟수가 3 이상인 과목을 찾음
    duplicates = [subject for subject,
                  count in subject_count.items() if count >= 3]

    if duplicates:
        # 중복된 과목이 있는 경우, 경고 팝업을 띄움
        ms.showwarning("경고", f"다음 과목이 3교시 이상 할당되었습니다: {', '.join(duplicates)}")

    # 수업 일자가 붙어있는지 판단
    search_dict = {
        1: [2, 4, 5],
        2: [1, 3, 5],
        3: [2, 4],
        4: [1, 3, 5],
        5: [1, 2, 4]
    }

    for i in range(1, 6):
        sub = set(subject for j in range(1, 7) if (subject := timetable[i][j][0]) != "없음")
        f = True
        for k in search_dict[i]:
            sj = timetable[k].values()
            if any(m in sub for l in sj for m in l):
                ms.showwarning("경고", f"다음 과목이 수정한 가까이 있거나 멀리 있습니다 /// {', '.join(sub)}")
                f = False
                break

        if f == False:
            break

################################ 시간표 자동 생성 ################################# // 미완성

def time_rand_GUI():
    global sub_ip, name_ip, pla_ip
    time_rand_win = tk.Toplevel()
    time_rand_win.title("시간표 자동 생성")
    time_rand_win.geometry("250x250+0+0")
    time_rand_win.resizable(False, False)
    time_rand_win.grab_set()

    tk.Label(time_rand_win,text="과목명").place(x=30,y=30)
    tk.Label(time_rand_win,text="교수명").place(x=30,y=90)
    tk.Label(time_rand_win,text="강의실명").place(x=30,y=150)


    sub_ip = tk.Entry(time_rand_win)
    sub_ip.insert(0,"확률과통계,딥러닝,AI알고리즘,기계학습,AI수학,논리적문제해결1,인공지능기초,서비스러닝") # ,논리적문제해결2,영상이해,AI프로그래밍,리눅스운영체제
    sub_ip.place(x=30,y=60)
    name_ip = tk.Entry(time_rand_win)
    name_ip.insert(0,"고선우,고선우,권수태,권수태,민정익,민정익,이근호,이근호") # ,송주환,송주환,김영수,김영수
    name_ip.place(x=30,y=120)
    pla_ip = tk.Entry(time_rand_win)
    pla_ip.insert(0,"423,423,423,423,423,423,423,423") # ,423,423,423,423
    pla_ip.place(x=30,y=180)


    # sub_ip = tk.Entry(time_rand_win)
    # sub_ip.insert(0,"확률과통계,딥러닝,AI알고리즘,기계학습,AI수학,논리적문제해결1,인공지능기초,서비스러닝,논리적문제해결2,영상이해,AI프로그래밍,리눅스운영체제")
    # sub_ip.place(x=30,y=60)
    # name_ip = tk.Entry(time_rand_win)
    # name_ip.insert(0,"고선우,고선우,권수태,권수태,민정익,민정익,이근호,이근호,송주환,송주환,김영수,김영수")
    # name_ip.place(x=30,y=120)
    # pla_ip = tk.Entry(time_rand_win)
    # pla_ip.insert(0,"423,423,423,423,423,423,423,423,423,423,423,423")
    # pla_ip.place(x=30,y=180)

    save_button = tk.Button(time_rand_win, width=15, height=2, relief="groove",text="시간표 자동 생성", bg="#FFECB3", command=time_rand)
    save_button.place(x=30, y=210)

    time_rand_win.mainloop()


def time_rand():
    global juju, timetable

    while True:
        Nn = ["없음", "없음", "없음"]
        timetable = {i: {j: list(Nn) for j in range(1, 7)} for i in range(1, 6)}
        juju = True
        for aa in range(2):
            for i in range(1, 6):
                for j in range(1, 7):
                    globals()[f"object_{i}_{j}"].config(
                                    text=f"{timetable[i][j][0]}\n{timetable[i][j][1]}\n{timetable[i][j][2]}")

            subjects = sub_ip.get().split(',')
            professors = name_ip.get().split(',')
            rooms = pla_ip.get().split(',')

            if len(subjects) != len(professors) or len(professors) != len(rooms):
                ms.showerror("입력 오류", "과목, 교수, 강의실의 개수가 일치하지 않습니다.")
                return

            for subject, professor, room in zip(subjects, professors, rooms):
                while True:
                    c = rd.randint(1, 5)  # 1부터 5까지 (월요일부터 금요일까지)
                    r = rd.randint(1, 6)  # 1부터 6까지 (1교시부터 6교시까지)

                    timetable[3][5][0] = "진로탐색 세미나"
                    timetable[3][5][1] = "외부"
                    timetable[3][5][2] = "423"

                    if timetable[c][r][0] == "없음":
                        timetable[c][r][0] = subject
                        timetable[c][r][1] = professor
                        timetable[c][r][2] = room
                        break

    # ### 수정 필요 ###
    # 연강 , 중복 판단 알고리즘
    #     for i in range(1, 6):  # 월요일부터 금요일까지
    #         subjects_1 = set()  # 각 요일별로 중복된 과목을 저장할 세트

    #         for j in range(1, 7):  # 1교시부터 6교시까지
    #             subject_name_1 = timetable[i][j][0]

    #             if subject_name_1 != "없음":  # "없음"이 아닌 경우에만 처리
                        # 수정 @@@@@@@@
    #                 if subject_name_1 in subjects_1:
    #                     # 같은 과목이 연속으로 나오는 경우, juju를 True로 설정하고 루프 종료
    #                     juju = False
    #                     break
                        # 수정 @@@@@@@@
    #                 else:
    #                     subjects_1.add(subject_name_1)

    #         if not juju:
    #             # juju가 False인 경우, 루프 종료
    #             print("3")
    #             break


        # 같은날 특정 교수님 수업 4교시 이상이면 juju=False
        duplicates_2 = set()
        professor_count = {}

        for i in range(1, 6):  # 월요일부터 금요일까지
            for j in range(1, 7):  # 1교시부터 6교시까지
                name = timetable[i][j][1]

                if name != "없음":  # "없음"이 아닌 경우에만 처리
                    if name in professor_count:
                        professor_count[name] += 1
                    else:
                        professor_count[name] = 1

        for professor, count in professor_count.items():
            if count >= 5:  # 5교시 이상인 경우
                juju = False

        # 중복된 과목이 있는 경우
        if duplicates_2:
            juju = False



        # 수업 일자가 붙어있는지 판단
        search_dict = {
            1: [2, 4, 5],
            2: [1, 3, 5],
            3: [2, 4],
            4: [1, 3, 5],
            5: [1, 2, 4]
        }

        for i in range(1, 6):
            sub = set(subject for j in range(1, 7) if (subject := timetable[i][j][0]) != "없음")
            f = True
            for k in search_dict[i]:
                sj = timetable[k].values()
                if any(m in sub for l in sj for m in l):
                    juju = False
                    f = False
                    print("2")
                    break

            if f == False:
                break
        print("1")

        if juju == True:
            break

    # 시간표 업데이트
    for i in range(1, 6):
        for j in range(1, 7):
            if timetable[i][j][0] != "없음":
                globals()[f"object_{i}_{j}"].config(text=f"{timetable[i][j][0]}\n{timetable[i][j][1]}\n{timetable[i][j][2]}")
        print("1",timetable)


################################ 실행 #################################

Nn = ["없음", "없음", "없음"]
timetable = {i: {j: list(Nn) for j in range(1, 7)} for i in range(1, 6)}

frame()



################################ 시간표 색상 ################################# // 미완성

# def time_table_color():

#         color = {
#         1:"#D4F0F0",
#         2:"#A2E1DB",
#         3:"#55CBCD",
#         4:"#CBAACB",
#         5:"#ECD5E3",
#         6:"#CCE2CB",
#         7:"#F6EAC2",
#         8:"#A2E1DB",
#         9:"#55CBCD",
#         10:"#FF968A",
#         11:"#FCB9AA",
#         12:"#FFAEA5",
#         13:"#F3B0C3",
#         14:"#FFC5BF",
#         15:"#FEE1E8",
#         }