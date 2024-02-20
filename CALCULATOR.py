import tkinter as tk

def btn_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)

def btn_clear():
    global expression
    expression = ""
    input_text.set("")

def btn_equal():
    global expression
    try:
        result = str(eval(expression))
        input_text.set(result)
        expression = ""
    except:
        input_text.set("Error")
        expression = ""

def btn_delete():
    global expression
    expression = expression[:-1]
    input_text.set(expression)

root = tk.Tk()
root.title("Calculator")

expression = ""
input_text = tk.StringVar()

entry = tk.Entry(root, font=('Arial', 18, 'bold'), textvariable=input_text, bd=20, insertwidth=4, bg="light gray", justify='right')
entry.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('%', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('/', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('*', 3, 3),
    ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('-', 4, 3),
    ('Del', 1, 4), ('+', 2, 4)
]

for (text, row, col) in buttons:
    if text == '=':
        tk.Button(root, text=text, padx=20, pady=20, font=('Arial', 18, 'bold'), bg="blue", fg="white", command=btn_equal).grid(row=row, column=col, padx=10, pady=10)
    elif text == 'C':
        tk.Button(root, text=text, padx=20, pady=20, font=('Arial', 18, 'bold'), bg="red", fg="white", command=btn_clear).grid(row=row, column=col, padx=10, pady=10)
    elif text == 'Del':
        tk.Button(root, text=text, padx=20, pady=20, font=('Arial', 18, 'bold'), bg="orange", fg="white", command=btn_delete).grid(row=row, column=col, padx=10, pady=10)
    else:
        tk.Button(root, text=text, padx=20, pady=20, font=('Arial', 18, 'bold'), bg="gray", fg="white", command=lambda item=text: btn_click(item)).grid(row=row, column=col, padx=10, pady=10)

root.mainloop()
