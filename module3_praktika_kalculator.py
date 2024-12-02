import tkinter as tk

def sum_():
    num1 = float(number1_entry.get())
    num2 = float(number2_entry.get())
    result = num1 + num2
    answer_entry.delete(0, tk.END)
    answer_entry.insert(0,str(result))

def raznost():
    num1 = float(number1_entry.get())
    num2 = float(number2_entry.get())
    result = num1 - num2
    answer_entry.delete(0, tk.END)
    answer_entry.insert(4,str(result))

def chastnost():
    num1 = float(number1_entry.get())
    num2 = float(number2_entry.get())
    result = num1 * num2
    answer_entry.delete(0, tk.END)
    answer_entry.insert(4, str(result))

def proizv():
    num1 = float(number1_entry.get())
    num2 = float(number2_entry.get())
    result = num1 / num2
    answer_entry.delete(0, tk.END)
    answer_entry.insert(4, str(result))


window = tk.Tk()
window.title('Калькулятор')
window.geometry("350x350")
window.resizable(False, False)
button_add = tk.Button(window, text="+", width=2, height=2,command=sum_)
button_add.place(x=100, y=200)
button_sub = tk.Button(window, text="-", width=2, height=2,command=raznost)
button_sub.place(x=150, y=200)
button_mul = tk.Button(window, text="*", width=2, height=2,command=chastnost)
button_mul.place(x=200, y=200)
button_div = tk.Button(window, text="/", width=2, height=2,command=proizv)
button_div.place(x=250, y=200)
number1_entry = tk.Entry(window, width=28)
number1_entry.place(x=100, y=75)
number2_entry = tk.Entry(window, width=28)
number2_entry.place(x=100, y=150)
answer_entry = tk.Entry(window, width=28)
answer_entry.place(x=100, y=300)
number1 = tk.Label(window, text="Введите первое число:")
number1.place(x=100, y=50)
number2 = tk.Label(window, text="Введите второе число:")
number2.place(x=100, y=125)
answer = tk.Label(window, text="Ответ:")
answer.place(x=100, y=275)

window.mainloop()