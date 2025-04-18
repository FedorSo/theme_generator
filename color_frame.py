import customtkinter as ctk

class ColorFrame(ctk.CTkFrame):
    def __init__(self, container):
        super().__init__(container)

        self.red_value, self.green_value, self.blue_value = '00', '00', '00'
        self.selected_color = '#' + self.red_value + self.green_value + self.blue_value

        self.color_box = ctk.CTkLabel(self, fg_color=self.selected_color, text='', height=100, width=100)
        self.color_box.grid(row=0, column=0, columnspan=2, padx=35, pady=10)

        self.color_hex = ctk.CTkEntry(self, justify='center', width=100)
        self.color_hex.insert('end', self.selected_color)
        self.color_hex.grid(row=1, column=0, columnspan=2)


        self.red_label = ctk.CTkLabel(self, text="R")
        self.red_label.grid(row=2, column=0, padx=(5, 0))

        self.red_slider = ctk.CTkSlider(self, from_=0, to=255, command=lambda value:self.get_value(value, "red"))
        self.red_slider.grid(row=2, column=1, padx=5)
        self.red_slider.set(0)


        self.green_label = ctk.CTkLabel(self, text="G")
        self.green_label.grid(row=3, column=0, padx=(5, 0))

        self.green_slider = ctk.CTkSlider(self, from_=0, to=255, command=lambda value:self.get_value(value, "green"))
        self.green_slider.grid(row=3, column=1, padx=5)
        self.green_slider.set(0)


        self.blue_label = ctk.CTkLabel(self, text="B")
        self.blue_label.grid(row=4, column=0, padx=(5, 0))

        self.blue_slider = ctk.CTkSlider(self, from_=0, to=255, command=lambda value:self.get_value(value, "blue"))
        self.blue_slider.grid(row=4, column=1, padx=5)
        self.blue_slider.set(0)

    def get_value(self, value, color):
        value = hex(int(value))
        value = value.replace("0x", "")
        value = value.rjust(2, "0")

        if color == "red":
            self.red_value = value
        elif color == "green":
            self.green_value = value
        elif color == "blue":
            self.blue_value = value

        self.update_color()

    def update_color(self):
        self.selected_color = '#' + self.red_value + self.green_value + self.blue_value
        self.color_box.configure(fg_color=self.selected_color)

        self.color_hex.delete(0, "end")
        self.color_hex.insert('end', self.selected_color)

    def get_color(self):
        return self.selected_color
    
    def set_color(self, color):
        self.red_value = color[1:3]
        self.green_value = color[3:5]
        self.blue_value = color[5:7]

        self.red_slider.set(int(self.red_value, 16))
        self.green_slider.set(int(self.green_value, 16))
        self.blue_slider.set(int(self.blue_value, 16))

        self.update_color()


if __name__ == "__main__":
    app = ctk.CTk()

    cf = ColorFrame(app)
    cf.grid(column=0, row=0)

    cf.set_color("#ffffff")

    app.mainloop()