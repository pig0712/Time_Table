import tkinter as tk

class WindowGen:
    def __init__(self):
        self.window = tk.Tk()

    def normal(self, name="Unknown", x=1000, y=750, xrs=True, yrs=True):
        self.window.title(name)
        self.window.geometry(f"{x}x{y}")
        self.window.resizable(xrs, yrs)

    def toplvl(self, name="Unknown", x=1000, y=750, xrs=True, yrs=True):
        self.window = tk.Toplevel(name)
        self.window.title(name)
        self.window.geometry(f"{x}x{y}")
        self.window.resizable(xrs, yrs)

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    window_gen = WindowGen()
    window_gen.normal(name="test", x=800, y=600, xrs=False, yrs=False)
    window_gen.run()
