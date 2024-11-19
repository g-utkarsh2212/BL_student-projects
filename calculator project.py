import tkinter as tk
import math

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")
        master.geometry("400x600")

        self.display = tk.Entry(master, font=("Arial", 24), bd=10, insertwidth=2, width=14, borderwidth=4)
        self.display.grid(row=0, column=0, columnspan=4)

        self.create_buttons()

    def create_buttons(self):
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+',
            'sin', 'cos', 'tan', 'sqrt',
            'Backspace', '^' , '+/-' # Added Power button
        ]

        row_val = 1
        col_val = 0

        for button in buttons:
            tk.Button(self.master, text=button, padx=20, pady=20, font=("Arial", 18),
                      width=5, command=lambda b=button: self.on_button_click(b)).grid(row=row_val, column=col_val, sticky='nsew')
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

        # Configure grid weights to make buttons expand equally
        for i in range(5):  # 5 rows
            self.master.grid_rowconfigure(i, weight=1)
        for j in range(4):  # 4 columns
            self.master.grid_columnconfigure(j, weight=1)

    def on_button_click(self, button):
        if button == '=':
            try:
                result = eval(self.display.get())
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except Exception as e:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
        elif button in ['sin', 'cos', 'tan', 'sqrt']:
            try:
                value = float(self.display.get())
                if button == 'sin':
                    result = math.sin(math.radians(value))
                elif button == 'cos':
                    result = math.cos(math.radians(value))
                elif button == 'tan':
                    result = math.tan(math.radians(value))
                elif button == 'sqrt':
                    result = math.sqrt(value)
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except Exception as e:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
        elif button == 'Backspace':
            current_text = self.display.get()
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, current_text[:-1])  # Remove the last character
        elif button == '^':
            self.display.insert(tk.END, '**')  # Use Python's exponentiation operator
        else:
            self.display.insert(tk.END, button)

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
    

    