import tkinter as tk


class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("320x420")
        self.root.resizable(0, 0)  # Prevent resizing for a fixed layout

        self.current_expression = ""

        # String variable to update the entry widget
        self.display_text = tk.StringVar()

        # Create the display frame and entry
        self.create_display()

        # Create the buttons
        self.create_buttons()

    def create_display(self):
        display_frame = tk.Frame(self.root, width=316, height=80, bg="lightgrey")
        display_frame.pack(side=tk.TOP)

        display = tk.Entry(display_frame, font=('arial', 24, 'bold'),
                           textvariable=self.display_text, width=17, bg="#eee", bd=0, justify=tk.RIGHT)
        display.grid(row=0, column=0, ipady=15, pady=10, padx=10)

    def create_buttons(self):
        button_frame = tk.Frame(self.root, width=312, height=272, bg="grey")
        button_frame.pack()

        # Button layout definition: (Text, Row, Column, Command)
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3)
        ]

        for (text, row, col) in buttons:
            self.build_button(button_frame, text, row, col)

    def build_button(self, frame, text, row, col):
        if text == 'C':
            btn = tk.Button(frame, text=text, width=6, height=2, bd=0, bg="#f44336", fg="white",
                            font=('arial', 14, 'bold'), command=self.clear)
        elif text == '=':
            btn = tk.Button(frame, text=text, width=6, height=2, bd=0, bg="#4caf50", fg="white",
                            font=('arial', 14, 'bold'), command=self.evaluate)
        elif text in ['/', '*', '-', '+']:
            btn = tk.Button(frame, text=text, width=6, height=2, bd=0, bg="#2196f3", fg="white",
                            font=('arial', 14, 'bold'), command=lambda t=text: self.click(t))
        else:
            btn = tk.Button(frame, text=text, width=6, height=2, bd=0, bg="#fff",
                            font=('arial', 14, 'bold'), command=lambda t=text: self.click(t))

        btn.grid(row=row, column=col, padx=2, pady=2)

    def click(self, item):
        self.current_expression += str(item)
        self.display_text.set(self.current_expression)

    def clear(self):
        self.current_expression = ""
        self.display_text.set("")

    def evaluate(self):
        try:
            # eval() calculates the string expression (e.g., "2+2")
            result = str(eval(self.current_expression))
            self.display_text.set(result)
            self.current_expression = result
        except Exception:
            self.display_text.set("Error")
            self.current_expression = ""


if __name__ == "__main__":
    main_window = tk.Tk()
    app = CalculatorApp(main_window)
    main_window.mainloop()