# tkinter 모듈을 가져와서 tk.Tk 및 tk.Toplevel을 상속받는 WindowGen 클래스를 정의
# WindowGen 클래스는 기본 창(tk.Tk)과 팝업 창(tk.Toplevel)을 모두 생성 가능

import tkinter as tk

class WindowGen(tk.Tk, tk.Toplevel):
    def __init__(self):
        super().__init__()

    # 일반 창을 생성하고 속성을 설정하는 메서드
    def normal(self, name="Unknown", x=1000, y=750, xrs=True, yrs=True):
        self.title(name)
        self.geometry(f"{x}x{y}")
        self.resizable(xrs, yrs)
        return self

    # 팝업 창을 생성하고 속성을 설정하는 메서드
    def toplvl(self, name="Unknown", x=1000, y=750, xrs=True, yrs=True):
        new_window = tk.Toplevel(master=self)
        new_window.title(name)
        new_window.geometry(f"{x}x{y}")
        new_window.resizable(xrs, yrs)
        return new_window

    # 생성한 창을 실행하는 메서드
    def run(self):
        self.mainloop()
        return self

# 이 파일 실행시키면 동작하는 코드
if __name__ == "__main__":
    # WindowGen 클래스의 인스턴스를 생성하고 일반 창을 생성하여 실행
    window_gen = WindowGen()
    window_gen.normal(name="test", x=800, y=600, xrs=False, yrs=False)
    window_gen.run()

    # tkinter 모듈의 위치를 출력
    print(tk.__file__)
