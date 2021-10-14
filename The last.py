import tkinter as tk
def multiplyer ():
    number = int(input_box.get())
    if number == 0:
        output_result.configure(text="อย่าเอ๋อ")
        return
    output = " "
    for i in range(1, 13):
        output += str(number) + " X " + str(i) + " = " + str(number * i) + "\n"
    output_result.configure(text=output)
window = tk.Tk()
window.title("Python Proj.")
window.minsize(width=400, height=400)

title_label = tk.Label(master=window, text="แปลรักฉันด้วยใจเทอ")
title_label.pack()

input_box = tk.Entry(master=window, width=15)
input_box.pack(pady=20)

run_button = tk.Button(master=window, text="RUN", command=multiplyer, width=15, height=2)
run_button.pack(pady=20)

output_result = tk.Label(master=window)
output_result.pack()
window.mainloop()