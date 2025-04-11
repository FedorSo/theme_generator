import tkinter as tk
import customtkinter as ctk

from color_frame import ColorFrame

ctk.set_appearance_mode("light")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Color Theme Generator")

        self.configure(padx=10, pady=10)
        self.resizable(0,0)

        self.color_frames = []

        for i in range(4):
            cf = ColorFrame(self)
            cf.grid(column=i, row=0, padx=10, pady=10)
            self.color_frames.append(cf)

        self.menu = tk.Menu()
        self.configure(menu=self.menu)
        self.menu.add_command(label="Save", command=self.save_colors)
        self.menu.add_command(label="Return colors")

    def save_colors(self):
        with open("colors.txt", "w", encoding="UTF-8") as file:
            for i in self.color_frames:
                file.write(i.selected_color + "\n")
                print(i.selected_color)

if __name__ == "__main__":
    app = App()
    app.mainloop()