import tkinter as tk

class Widget:

    # LabelWidget(생성할 트킨터 객체, txt="넣을 텍스트", x=좌표, y=좌표, w=밑넓이, h=높이, f=색, r=모양)
    # relief : flat, groove, raised, ridge, solid, sunken
    def LabelWidget(self, object, txt="None", ix=0, iy=0, w=10, h=5, f="red", r="solid"):
        self.lbobj = tk.Label(object, text=txt, width = w, height = h, fg=f , relief= r)
        self.lbobj.place(x = ix, y = iy)
        return self

    def ButtonWidget(self, object, txt="None", ix=0, iy=0, w=10, h=5, f="red", r="solid"):
        self.btobj = tk.Button(object, text=txt)
        return self

    def EnterWidget(self, object, txt="None", ix=0, iy=0, w=10, h=5, f="red", r="solid"):
        return self

if __name__ == "__main__":
    pass