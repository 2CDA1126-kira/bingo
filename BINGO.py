import tkinter as tk
import random

number = []

def rand():
    if len(number) >= 75:
        return "終了"
    while True:
        n = random.randint(1, 75)
        if n not in number:
            number.append(n)
            return n

def hyouzi():
    n = rand()
    suuzilabel.config(text=str(n))
    label3.config(text=", ".join(map(str, number)))

def reset():
    global number
    number = []  
    suuzilabel.config(text="")
    label3.config(text="") 

# ウィンドウ設定
root = tk.Tk()
root.title("ビンゴの司会システム")
root.geometry("500x400") 

# ウィジェット
label = tk.Label(root, text="BINGO")
suuzilabel = tk.Label(root, text="", font=("Helvetica", 64))  
button = tk.Button(root, text="番号生成", command=hyouzi)
reset_button = tk.Button(root, text="リセット", command=reset)
label2 = tk.Label(root, text="履歴")
label3 = tk.Label(root, text="", wraplength=200,  borderwidth=2, relief="solid", width=30, height=10)
                    

# レイアウト
label.pack()
suuzilabel.pack()
button.pack()
reset_button.pack()
label2.pack()
label3.pack()

root.mainloop()
