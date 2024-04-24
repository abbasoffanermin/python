import tkinter as tk
import tkinter.ttk as ic
from random import randint


bg_colors = ['pink', 
             '#FF5733', 
             '#DAF7A6', 
             '#FFC300', 
             '#2ECC71', 
             '#EA5CEF', 
             '#AC3DF8', 
             '#EAF83D', 
             '#57E9F5', 
             '#57F5CA', 
             '#CCCCFF',
             '#C0EDFF',
             ]

bg_num = len(bg_colors)
ran_num = randint(0, bg_num-1)
def main():
    window = tk.Tk()

    window.title("Narminator Beta v2.0.2 Special For Narmin")

    window.config(bg=bg_colors[ran_num])

    icon_heart = tk.PhotoImage(file = "C:\\Program Files (x86)\\Narminator Beta v2.0\\icon.png")
    window.iconphoto(False, icon_heart)
    window_width = 700
    window_height = 430

    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)

    window.geometry(f"{window_width}x{window_height}+{x}+{y}")

    label_text = "Səni çox sevirəm dovşanım\u2764\uFE0F"
    label = tk.Label(window, text=label_text, bg=bg_colors[ran_num], fg='white', font=("Helvetica", 25))
    label.place(relx=0.5, rely=0.5, anchor="center")

    window.mainloop()

if __name__ == "__main__":
    main()
