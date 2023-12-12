import File
import pandas as pd

class Warning:
    def __init__(self, data):
        self.df = data
        # self.df = pd.DataFrame(columns=["월요일","화요일","수요일","목요일","금요일"],index=[0,1,2,3,4])

        self.days = {
            "월요일" : ["화요일","목요일","금요일"],
            "화요일" : ["월요일","수요일","금요일"],
            "수요일" : ["화요일","목요일"],
            "목요일" : ["월요일","수요일","금요일"],
            "금요일" : ["월요일","화요일","목요일"]
        }

    # 오전 시간 수업이 오후 시간에 있나 판단.
    def lunch_break(sefl):
        jm = True

        st1 = []
        for i in df.columns:
            for j in df[i][:2]:
                st1.append(eval(j)[1])
        st1 = set(st1)

        st2 = []
        for i in df.columns:
            for j in df[i][2:]:
                st2.append(eval(j)[1])
        st2 = set(st2)

        for i in st1:
            if i in st2:
                jm = False
                break

        return jm


    # 바로 전날 혹은 다음날 같은 과목이 배정되었는지 판단
    def every_other_day(self,day):
        jm = True


        st1 = []
        for i in self.df[day]:
            print(i)
            print(type(i))
            st1.append(eval(i)[1])
        st1 = set(st1)

        st2 = []
        for i in self.days[day]:
            for j in df[i]:
                st2.append(eval(j)[1])
        st2 = set(st2)

        for i in st1:
            if i in st2:
                jm = False
                break

        return jm


    # 같은 날짜에 같은 과목 배정되었는지 판단
    def same_day(self,day):
        jm = True

        st = []
        for i in range(5):
            st.append(eval(df[day][i])[1])

        if len(st) != len(set(st)):
            jm = False

        return jm


    # 특정 교수님의 시간이 같은날 많이 있는지 판단
    def time_balance(self,day):
        jm = True

        st = []
        for i in range(5):
            st.append(eval(df[day][i])[0])

        for i in set(st):
            if st.count(i) >= 3:
                jm = False
                break

        return jm

    def data(self):
        return self.df

if __name__ == "__main__":
    df = File.ExcelFile.read("./save.xlsx")
    # df = File.ExcelFile.read("./save.xlsx")
    aa = Warning(df)
    print(aa.lunch_break())
    # print(aa.same_day("수요일"))