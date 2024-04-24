import tkinter as tk
import tkinter.ttk as ic
from random import randint 

n_words = [
    'zzz... \u2764\uFE0F', 
    'Hər şeyim mənim \u2764\uFE0F',
    'Səni hər şeydən çox sevirəm \u2764\uFE0F',
    'Səni hər şeydən çox sevirəm dovşanım \u2764\uFE0F',
    'Dovşanım mənim \u2764\uFE0F',
    'Varlığım mənim \u2764\uFE0F',
    'Ulduz Tozum \u2764\uFE0F',
    'Nərminim \u2764\uFE0F',
    'Dünyam mənim \u2764\uFE0F',
    'Can parçam mənim \u2764\uFE0F',
    'Mələyim mənim \u2764\uFE0F',
    'Pııt \u2764\uFE0F',
    ]

RanNum = randint(0, len(n_words)-1)

def main():
    window = tk.Tk()

    window.title("Narminator Beta v2.0.2 Special For Narmin")

    window.config(bg='pink')

    icon_heart = tk.PhotoImage(file = "C:\\Program Files (x86)\\Narminator Beta v2.0\\icon.png")
    window.iconphoto(False, icon_heart)
    window_width = 700
    window_height = 430

    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)

    window.geometry(f"{window_width}x{window_height}+{x}+{y}")

    label_text = n_words[RanNum]
    label = tk.Label(window, text=label_text, bg='pink', fg='white', font=("Helvetica", 25))
    label.place(relx=0.5, rely=0.5, anchor="center")

    window.mainloop()

if __name__ == "__main__":
    main()
