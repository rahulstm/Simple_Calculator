import tkinter as tk
from tkinter import messagebox


def button_click(item):
    current = input_text.get()
    input_text.set(current + str(item))


def button_clear():
    input_text.set("")


def button_equal():
    try:
        result = str(eval(input_text.get()))
        input_text.set(result)
    except Exception as e:
        messagebox.showerror("Error", "Invalid Input")
        input_text.set("")


window = tk.Tk()
window.title("Simple Calculator")
window.geometry("400x400")
window.resizable(0, 0)


input_text = tk.StringVar()


input_frame = tk.Frame(window, width=400, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=2)
input_frame.pack(side=tk.TOP)

input_field = tk.Entry(input_frame, textvariable=input_text, font=('arial', 18, 'bold'), width=50, bg="#eee", bd=0, justify=tk.RIGHT)
input_field.grid(row=0, column=0)
input_field.pack(ipady=10)  # internal padding


btns_frame = tk.Frame(window, width=400, height=350, bg="grey")
btns_frame.pack()


clear = tk.Button(btns_frame, text="C", fg="black", width=32, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda: button_clear()).grid(row=0, column=0, columnspan=3, padx=1, pady=1)
divide = tk.Button(btns_frame, text="/", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: button_click("/")).grid(row=0, column=3, padx=1, pady=1)

seven = tk.Button(btns_frame, text="7", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: button_click(7)).grid(row=1, column=0, padx=1, pady=1)
eight = tk.Button(btns_frame, text="8", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: button_click(8)).grid(row=1, column=1, padx=1, pady=1)
nine = tk.Button(btns_frame, text="9", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: button_click(9)).grid(row=1, column=2, padx=1, pady=1)
multiply = tk.Button(btns_frame, text="*", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: button_click("*")).grid(row=1, column=3, padx=1, pady=1)

four = tk.Button(btns_frame, text="4", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: button_click(4)).grid(row=2, column=0, padx=1, pady=1)
five = tk.Button(btns_frame, text="5", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: button_click(5)).grid(row=2, column=1, padx=1, pady=1)
six = tk.Button(btns_frame, text="6", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: button_click(6)).grid(row=2, column=2, padx=1, pady=1)
minus = tk.Button(btns_frame, text="-", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: button_click("-")).grid(row=2, column=3, padx=1, pady=1)


one = tk.Button(btns_frame, text="1", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: button_click(1)).grid(row=3, column=0, padx=1, pady=1)
two = tk.Button(btns_frame, text="2", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: button_click(2)).grid(row=3, column=1, padx=1, pady=1)
three = tk.Button(btns_frame, text="3", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: button_click(3)).grid(row=3, column=2, padx=1, pady=1)
plus = tk.Button(btns_frame, text="+", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: button_click("+")).grid(row=3, column=3, padx=1, pady=1)


zero = tk.Button(btns_frame, text="0", fg="black", width=21, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: button_click(0)).grid(row=4, column=0, columnspan=2, padx=1, pady=1)
point = tk.Button(btns_frame, text=".", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: button_click(".")).grid(row=4, column=2, padx=1, pady=1)
equals = tk.Button(btns_frame, text="=", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda: button_equal()).grid(row=4, column=3, padx=1, pady=1)

window.mainloop()
