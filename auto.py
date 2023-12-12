import pandas as pd
import random as rd

class auto:
    def __init__(self,sample):
        self.sample = sample
        self.column = ["월요일","화요일","수요일","목요일","금요일"]
        self.row = [1,2,3,4,5]
        self.data = pd.DataFrame(index = self.row, columns=self.column)
        # 모든 값에 None으로 채우기
        self.data = self.data.applymap(lambda x: " ")

    def timetable(self):
        
        def deployment(column,row,data): # 빈 부분 판단
            co = 0
            while co <= 100:
                x = rd.choice(column)
                y = rd.choice(row)
                
                # print(x,y)
                
                if x == "월요일":
                    dy = ["월요일","화요일"]
                
                elif x == "화요일":
                    dy = ["월요일","화요일","수요일"]
                
                elif x == "수요일":
                    dy = ["화요일","수요일","목요일"]
                
                elif x == "목요일":
                    dy = ["수요일","목요일","금요일"]
                
                elif x == "금요일":
                    dy = ["목요일","금요일"]
                    
                aaa = []
                
                for i in dy:
                    for j in range(1,6):
                        if self.data[i][j] != " ":
                            aaa.append(self.data[i][j]) # 필터링 후 과목들만 aaa 리스트에 저장 
                
                # print(aaa)
                
                if (self.data[x][y] == " ") and (data not in aaa):
                    self.data[x][y] = data
                    print(1)
                    break
                co += 1
                
                if co >= 100:
                    self.data = self.data.applymap(lambda x: " ")
                    print("초기화")
                
        def testcase(data):
            
            days = self.column
            lst = []
            for i in days:
                lst.append(len(self.data[i][self.data[i] != ""])) # 채워진 개수 카운트
                
            if all(element == lst[0] for element in lst): # 개수가 전부 같으면 월~금 랜덤으로 넣기
                deployment(self.column,self.row,data) 
                print("같음")
                
            elif max(lst) != min(lst) :
                lst2 = []
                c = 0
                for i in lst:
                    if i == min(lst):
                        d = self.column[c]
                        lst2.append(d)
                    c += 1    
                    
                # deployment(lst2,self.row,data)
                
                   
            # a = self.data      
            # print(self.data["월요일"],self.data["화요일"],self.data["수요일"],self.data["목요일"],self.data["금요일"],)
            # print(a)
            
            
            
        # 1. 수요일 5교시에 진로 세미나
        self.data["수요일"][5] = ["???","진로 세미나"]
        
        for i in range(12):
            testcase(self.sample[i])
            testcase(self.sample[i])
        
        print(self.data)


    # 색 자동 생성
    def cloor(self):
        pass



if __name__ == "__main__":

    # import File
    # df = File.ExcelFile.read("./save.xlsx")

    sample = [
    ["고선우","확률과통계"],
    ["고선우","딥러닝"],
    ["권수태","AI알고리즘"],
    ["권수태","기계학습"],
    ["민정익","AI수학"],
    ["민정익","논리적문제해결1"],
    ["이근호","인공지능기초"],
    ["이근호","서비스러닝"],
    ["송주환","논리적문제해결2"],
    ["송주환","영상이해"],
    ["김영수","AI프로그래밍"],
    ["김영수","리눅스운영체제"]
    ]

    deployment = auto(sample).timetable()