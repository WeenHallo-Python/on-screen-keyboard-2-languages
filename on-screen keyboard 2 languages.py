from tkinter import *

window = Tk()
window.title("Экранная клавиатура")

# Глобальная переменная для хранения ввода
entry_text = StringVar()

# Глобальная переменная для отслеживания раскладки
current_layout = "ru"  # Начальная раскладка - русская

# Функция для добавления символа в поле ввода
def add_to_entry(symbol):
    current_text = entry_text.get()
    entry_text.set(current_text + symbol)

# Функция для очистки поля ввода
def clear_entry():
    entry_text.set("")

# Функция для удаления последнего символа
def backspace():
    current_text = entry_text.get()
    entry_text.set(current_text[:-1])

# Функция для переключения раскладки
def toggle_layout():
    global current_layout
    current_layout = "en" if current_layout == "ru" else "ru"
    update_keyboard_buttons()

# Функция для обновления кнопок в зависимости от раскладки
def update_keyboard_buttons():
    if current_layout == "ru":
        rows = [
            ['Ё', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'Backspace'],
            ['Tab', 'Й', 'Ц', 'У', 'К', 'Е', 'Н', 'Г', 'Ш', 'Щ', 'З', 'Х', 'Ъ'],
            ['Caps Lock', 'Ф', 'Ы', 'В', 'А', 'П', 'Р', 'О', 'Л', 'Д', 'Ж', 'Э', 'Enter'],
            ['Shift', 'Я', 'Ч', 'С', 'М', 'И', 'Т', 'Ь', 'Б', 'Ю', '/,.?', 'Shift'],
            ['Ctrl', 'Win', 'Alt', 'Space', 'Alt', 'FN', 'Empty', 'Ctrl']
        ]
    else:
        rows = [
            ['`', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'Backspace'],
            ['Tab', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', '[', ']'],
            ['Caps Lock', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ';', "'", 'Enter'],
            ['Shift', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', ',', '.', '/', 'Shift'],
            ['Ctrl', 'Win', 'Alt', 'Space', 'Alt', 'FN', 'Empty', 'Ctrl']
        ]

    # Очищаем все кнопки перед обновлением
    for widget in window.winfo_children():
        if isinstance(widget, Button):
            widget.destroy()

    # Создаем поле ввода
    Entry(window, width=40, textvariable=entry_text, font=("Arial", 14)).grid(row=0, column=0, columnspan=15, pady=10)

    # Создаем кнопки для каждой строки
    for row_index, row in enumerate(rows):
        for col_index, key in enumerate(row):
            if key == 'Space':
                # Кнопка Space с увеличенной шириной
                Button(window, text=key, height=2, width=20, command=lambda: add_to_entry(' ')).grid(row=row_index + 1, column=col_index, columnspan=4)
            elif key in ['Ctrl', 'Win', 'Alt', 'FN', 'Tab', 'Caps Lock', 'Empty', 'Enter', 'Shift']:
                # Кнопки, которые ничего не делают
                Button(window, text=key, height=2, width=5, command=lambda: None).grid(row=row_index + 1, column=col_index)
            elif key == 'Backspace':
                # Кнопка Backspace
                Button(window, text=key, height=2, width=5, command=backspace).grid(row=row_index + 1, column=col_index)
            else:
                # Остальные кнопки
                Button(window, text=key, height=2, width=5, command=lambda k=key: add_to_entry(k)).grid(row=row_index + 1, column=col_index)

    # Кнопка переключения раскладки
    Button(window, text="EN/RU", height=2, width=5, command=toggle_layout).grid(row=1, column=12, columnspan=15)

# Инициализация клавиатуры
update_keyboard_buttons()

# Запускаем главный цикл
window.mainloop()
