import tkinter as tk
import tkinter.ttk as ic

def main():
    window = tk.Tk()

    window.title("Narminator Beta v2.0.2 Special For Narmin")

    window.config(bg='pink')

    icon_heart = tk.PhotoImage(file = "C:\\Program Files (x86)\\Narminator Beta v2.0\\icon.png")
    window.iconphoto(False, icon_heart)
    window_width = 960
    window_height = 550

    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)

    window.geometry(f"{window_width}x{window_height}+{x}+{y}")

    label_text = "Beynəlxalq 8 mart qadınlar gününü təbrik edirəm hər şeyim\u2764\uFE0F"
    label = tk.Label(window, text=label_text, bg='pink', fg='white', font=("Helvetica", 25))
    label.place(relx=0.5, rely=0.5, anchor="center")

    window.mainloop()

if __name__ == "__main__":
    main()
