# Простой графический калькулятор для Windows 10 на Python с Tkinter
import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Калькулятор")
        self.root.geometry("360x500")
        self.root.resizable(False, False)
        
        # Переменная для отображения
        self.expression = ""
        self.input_text = tk.StringVar()
        
        # Создание дисплея
        input_frame = tk.Frame(self.root, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=2)
        input_frame.pack(side=tk.TOP)
        
        input_field = tk.Entry(input_frame, font=('arial', 18, 'bold'), textvariable=self.input_text, width=50, bd=0, insertwidth=4, justify='right')
        input_field.grid(row=0, column=0)
        input_field.pack(ipady=10)
        
        # Кнопки
        btns_frame = tk.Frame(self.root, bd=0)
        btns_frame.pack()
        
        # Кнопки
        buttons = [
            ('C', 1, 0), ('⌫', 1, 1), ('%', 1, 2), ('/', 1, 3),
            ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('*', 2, 3),
            ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('-', 3, 3),
            ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('+', 4, 3),
            ('0', 5, 0), ('.', 5, 1), ('=', 5, 2, 2)
        ]
        
        for btn_info in buttons:
            text = btn_info[0]
            row = btn_info[1]
            col = btn_info[2]
            colspan = btn_info[3] if len(btn_info) > 3 else 1
            
            if text == '=':
                btn = tk.Button(btns_frame, text=text, fg='white', bg='#ff9500', command=self.equalpress, height=2, width=10, font=('arial', 14, 'bold'))
                btn.grid(row=row, column=col, columnspan=colspan, padx=1, pady=1, sticky='nsew')
            elif text in ('C', '⌫', '%', '/', '*', '-', '+'):
                btn = tk.Button(btns_frame, text=text, fg='black', bg='#f2f2f2', command=lambda x=text: self.on_button_click(x), height=2, width=10, font=('arial', 14))
                btn.grid(row=row, column=col, padx=1, pady=1, sticky='nsew')
            else:
                btn = tk.Button(btns_frame, text=text, fg='black', bg='white', command=lambda x=text: self.on_button_click(x), height=2, width=10, font=('arial', 14))
                btn.grid(row=row, column=col, padx=1, pady=1, sticky='nsew')
        
        # Настройка сетки
        for i in range(6):
            btns_frame.rowconfigure(i, weight=1)
        for i in range(4):
            btns_frame.columnconfigure(i, weight=1)
        
        self.root.mainloop()
    
    def on_button_click(self, char):
        if char == 'C':
            self.expression = ""
        elif char == '⌫':
            self.expression = self.expression[:-1]
        else:
            self.expression += str(char)
        self.input_text.set(self.expression)
    
    def equalpress(self):
        try:
            result = str(eval(self.expression))
            self.input_text.set(result)
            self.expression = result
        except:
            messagebox.showerror("Ошибка", "Неверное выражение")
            self.expression = ""
            self.input_text.set("")

if __name__ == "__main__":
    Calculator()