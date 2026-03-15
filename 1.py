import tkinter as tk
from tkinter import messagebox

# إنشاء النافذة الرئيسية
root = tk.Tk()
root.title("آلة حاسبة بسيطة")
root.geometry("320x450")           # حجم النافذة
root.configure(bg="#f0f0f0")       # لون الخلفية

# متغير لعرض النص
expression = ""
result_var = tk.StringVar()

# دالة لتحديث الشاشة عند الضغط على الأرقام أو العمليات
def press(num):
    global expression
    expression = expression + str(num)
    result_var.set(expression)

# دالة الحساب (تقييم التعبير)
def equalpress():
    try:
        global expression
        total = str(eval(expression))   # eval تحول النص إلى حساب رياضي
        result_var.set(total)
        expression = total              # نحدث التعبير بالنتيجة عشان نكمل الحساب
    except Exception as e:
        messagebox.showerror("خطأ", "حساب غير صحيح!")
        expression = ""
        result_var.set("")

# دالة مسح كل شيء
def clear():
    global expression
    expression = ""
    result_var.set("")

# دالة مسح آخر رقم/عملية فقط
def backspace():
    global expression
    if expression:
        expression = expression[:-1]
        result_var.set(expression)

# ────────────────────────────────────────────────
# الشاشة (Entry)
entry = tk.Entry(root, font=('Arial', 24), textvariable=result_var,
                 bd=10, insertwidth=4, width=14, borderwidth=4,
                 justify='right', bg="#ffffff")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=20, ipady=20)

# ────────────────────────────────────────────────
# الأزرار

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('C', 4, 2), ('+', 4, 3),
]

for (text, row, col) in buttons:
    if text == 'C':
        btn = tk.Button(root, text=text, font=('Arial', 18, 'bold'),
                        padx=20, pady=20, bg="#ff6b6b", fg="white",
                        command=clear)
    else:
        btn = tk.Button(root, text=text, font=('Arial', 18),
                        padx=20, pady=20, bg="#4ecdc4", fg="white",
                        command=lambda t=text: press(t))
    
    btn.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

# زر المسح الجزئي (Backspace) و زر اليساوي
btn_back = tk.Button(root, text="⌫", font=('Arial', 18),
                     padx=20, pady=20, bg="#ffa502", fg="white",
                     command=backspace)
btn_back.grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

btn_equal = tk.Button(root, text="=", font=('Arial', 18, 'bold'),
                      padx=20, pady=20, bg="#2ecc71", fg="white",
                      command=equalpress)
btn_equal.grid(row=5, column=2, columnspan=2, padx=5, pady=5, sticky="nsew")

# جعل الأزرار تتمدد مع النافذة
for i in range(6):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

# تشغيل البرنامجimport tkinter as tk
from tkinter import messagebox

# إنشاء النافذة الرئيسية
root = tk.Tk()
root.title("آلة حاسبة بسيطة")
root.geometry("320x450")           # حجم النافذة
root.configure(bg="#f0f0f0")       # لون الخلفية

# متغير لعرض النص
expression = ""
result_var = tk.StringVar()

# دالة لتحديث الشاشة عند الضغط على الأرقام أو العمليات
def press(num):
    global expression
    expression = expression + str(num)
    result_var.set(expression)

# دالة الحساب (تقييم التعبير)
def equalpress():
    try:
        global expression
        total = str(eval(expression))   # eval تحول النص إلى حساب رياضي
        result_var.set(total)
        expression = total              # نحدث التعبير بالنتيجة عشان نكمل الحساب
    except Exception as e:
        messagebox.showerror("خطأ", "حساب غير صحيح!")
        expression = ""
        result_var.set("")

# دالة مسح كل شيء
def clear():
    global expression
    expression = ""
    result_var.set("")

# دالة مسح آخر رقم/عملية فقط
def backspace():
    global expression
    if expression:
        expression = expression[:-1]
        result_var.set(expression)

# ────────────────────────────────────────────────
# الشاشة (Entry)
entry = tk.Entry(root, font=('Arial', 24), textvariable=result_var,
                 bd=10, insertwidth=4, width=14, borderwidth=4,
                 justify='right', bg="#ffffff")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=20, ipady=20)

# ────────────────────────────────────────────────
# الأزرار

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('C', 4, 2), ('+', 4, 3),
]

for (text, row, col) in buttons:
    if text == 'C':
        btn = tk.Button(root, text=text, font=('Arial', 18, 'bold'),
                        padx=20, pady=20, bg="#ff6b6b", fg="white",
                        command=clear)
    else:
        btn = tk.Button(root, text=text, font=('Arial', 18),
                        padx=20, pady=20, bg="#4ecdc4", fg="white",
                        command=lambda t=text: press(t))
    
    btn.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

# زر المسح الجزئي (Backspace) و زر اليساوي
btn_back = tk.Button(root, text="⌫", font=('Arial', 18),
                     padx=20, pady=20, bg="#ffa502", fg="white",
                     command=backspace)
btn_back.grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

btn_equal = tk.Button(root, text="=", font=('Arial', 18, 'bold'),
                      padx=20, pady=20, bg="#2ecc71", fg="white",
                      command=equalpress)
btn_equal.grid(row=5, column=2, columnspan=2, padx=5, pady=5, sticky="nsew")

# جعل الأزرار تتمدد مع النافذة
for i in range(6):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

# تشغيل البرنامج
