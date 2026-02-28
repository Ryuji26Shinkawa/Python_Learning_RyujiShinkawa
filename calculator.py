import tkinter as tk


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return None
    return a / b


class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.resizable(False, False)
        self.root.geometry("320x440")

        # UI state for display, input buffer, and selected operator.
        # 画面表示用の文字列変数
        self.display_var = tk.StringVar()
        self.input_var = tk.StringVar()
        self.operator_var = tk.StringVar()
        # 現在入力中の数字文字列
        self.current_value = ""
        # 演算子を押した時点での数値
        self.stored_value = None
        # 選択した演算子
        self.operator = None

        # 画面レイアウトを構築
        self._build_ui()

    # 画面レイアウトを構築する変数
    def _build_ui(self):
        # Top display area: current input, operator, and main display line.
        # 画面上部
        display_frame = tk.Frame(self.root, padx=10, pady=10)
        display_frame.pack(fill="x")

        input_label = tk.Label(
            display_frame,
            textvariable=self.input_var,
            anchor="e",
            font=("Segoe UI", 12),
        )
        input_label.pack(fill="x")

        operator_label = tk.Label(
            display_frame,
            textvariable=self.operator_var,
            anchor="e",
            font=("Segoe UI", 12),
        )
        operator_label.pack(fill="x")

        display_label = tk.Label(
            display_frame,
            textvariable=self.display_var,
            anchor="e",
            font=("Segoe UI", 24, "bold"),
            relief="sunken",
            padx=8,
            pady=6,
        )
        display_label.pack(fill="x", pady=(6, 0))

        # Keypad and control buttons layout.
        # 画面下部
        buttons_frame = tk.Frame(self.root, padx=10, pady=10)
        buttons_frame.pack(fill="both", expand=True)

        buttons = [
            ("7", self._append_digit),
            ("8", self._append_digit),
            ("9", self._append_digit),
            ("÷", self._set_operator),
            ("4", self._append_digit),
            ("5", self._append_digit),
            ("6", self._append_digit),
            ("×", self._set_operator),
            ("1", self._append_digit),
            ("2", self._append_digit),
            ("3", self._append_digit),
            ("-", self._set_operator),
            ("0", self._append_digit),
            (".", self._append_dot),
            ("=", self._calculate),
            ("+", self._set_operator),
            ("C", self._clear_entry),
            ("AC", self._all_clear),
        ]

        for index, (label, handler) in enumerate(buttons):
            row = index // 4
            col = index % 4
            button = tk.Button(
                buttons_frame,
                text=label,
                command=lambda value=label, fn=handler: fn(value),
                width=6,
                height=2,
                font=("Segoe UI", 12),
            )
            button.grid(row=row, column=col, padx=4, pady=4, sticky="nsew")

        # Evenly size the button grid.
        for i in range(4):
            buttons_frame.columnconfigure(i, weight=1)
        for i in range(5):
            buttons_frame.rowconfigure(i, weight=1)

    # 各ボタンの処理

    def _append_digit(self, value):
        if value == "0" and self.current_value == "0":
            return
        self.current_value += value
        self._update_display()

    def _append_dot(self, _value):
        if "." in self.current_value:
            return
        if not self.current_value:
            self.current_value = "0"
        self.current_value += "."
        self._update_display()

    def _set_operator(self, value):
        if self.current_value:
            try:
                self.stored_value = float(self.current_value)
            except ValueError:
                self.stored_value = None
            self.current_value = ""
        self.operator = value
        self.operator_var.set(value)
        self._update_display()

    def _clear_entry(self, _value):
        self.current_value = ""
        self._update_display()

    def _all_clear(self, _value):
        self.current_value = ""
        self.stored_value = None
        self.operator = None
        self.operator_var.set("")
        self.input_var.set("")
        self.display_var.set("")

    def _calculate(self, _value):
        if self.stored_value is None or not self.operator:
            return
        try:
            current = float(self.current_value) if self.current_value else 0.0
        except ValueError:
            return

        # Dispatch to the selected operator.
        result = None
        if self.operator == "+":
            result = add(self.stored_value, current)
        elif self.operator == "-":
            result = subtract(self.stored_value, current)
        elif self.operator == "×":
            result = multiply(self.stored_value, current)
        elif self.operator == "÷":
            result = divide(self.stored_value, current)

        if result is None:
            self.display_var.set("None")
        else:
            self.display_var.set(str(result))

        # Reset input while keeping the last operator visible.
        self.input_var.set("")
        self.operator_var.set(self.operator)
        self.current_value = ""
        self.stored_value = None

    def _update_display(self):
        self.input_var.set(self.current_value)
        if self.current_value:
            self.display_var.set(self.current_value)


if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
