import tkinter as tk

def calculate():
    result = eval(entry.get())
    output.config(text=f"Result: {result}")

root = tk.Tk()
root.title("Calculator")

entry = tk.Entry(root, width=20)
entry.pack(pady=10)

btn = tk.Button(root, text="Calculate", command=calculate)
btn.pack()

output = tk.Label(root, text="Result:")
output.pack(pady=10)

root.mainloop()