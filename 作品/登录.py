from tkinter import *
from tkinter import messagebox
import random

code = ""

def create_code():
    global code
    chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    code = "".join(random.sample(chars, 4))
    verify_label.config(text=code)

def login():
    acc = entry_user.get().strip()
    pw = entry_pwd.get().strip()
    input_code = entry_code.get().strip()

    if acc and pw and input_code.upper() == code:
        messagebox.showinfo("提示", "登录成功")
        print("用户名："+acc)
        print("密码："+pw)
    else:
        messagebox.showerror("错误", "信息不全或验证码错误")
        create_code()
        entry_code.delete(0, END)

root = Tk()
root.title("登录")
root.geometry("320x220")

Label(root, text="账号").place(x=50, y=30)
entry_user = Entry(root)
entry_user.place(x=110, y=30, width=150)

Label(root, text="密码").place(x=50, y=70)
entry_pwd = Entry(root, show="*")
entry_pwd.place(x=110, y=70, width=150)

Label(root, text="验证码").place(x=50, y=110)
entry_code = Entry(root)
entry_code.place(x=110, y=110, width=80)

verify_label = Label(root, fg="blue", font=("Arial", 12))
verify_label.place(x=200, y=110)

Button(root, text="登录", command=login).place(x=120, y=160)
Button(root, text="换一张", command=create_code).place(x=200, y=160)

create_code()
root.mainloop()
