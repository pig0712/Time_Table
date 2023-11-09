import tkinter as tk

class WindowGenerator:
    def Normal(self,name : str = "Unknown", x : int = 1000, y : int = 750, xrs : bool = True, yrs : bool = True):
        window = tk.Tk()
        window.title(name)
        window.geometry(f"{x}x{y}")
        window.resizable(xrs, yrs)
        window.mainloop()

    def Toplvl(self,name : str = "Unknown", x : int = 1000, y : int = 750, xrs : bool = True, yrs : bool = True):
        window = tk.Toplevel()
        window.title(name)
        window.geometry(f"{x}x{y}")
        window.resizable(xrs, yrs)
        window.mainloop()

if __name__ == "__main__":
    window_gen = WindowGenerator()
    window_gen.Normal(name="test", x=800, y=600, xrs=False, yrs=False)
    # 인자 설명
    # 1. 윈도우 창 이름
    # 2. 윈도우 x 축 길이
    # 3. 윈도우 y 축 길이
    # 4. 윈도우 x 축 길이 변환 가능 여부
    # 5. 윈도우 y 축 길이 변환 가능 여부
