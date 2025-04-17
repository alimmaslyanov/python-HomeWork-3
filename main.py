import flet as ft
from datetime import datetime

def main(page: ft.Page):
    page.title = "Мое первое приложение"
    page.theme_mode = ft.ThemeMode.LIGHT
    greeting_text = ft.Text("Hello world")
    greeting_history = []

    HISTORY_FILE = "history.txt"

    history_text = ft.Text("История приветствий:", size="bodyMedium")
    history_text.visible = True  # по умолчанию показываем

    def load_history():
        try:
            with open(HISTORY_FILE, 'r', encoding='utf-8') as file:
                lines = file.readlines()
                for line in lines:
                    name = line.strip()
                    if name:
                        greeting_history.append(name)
                history_text.value = 'История приветствий:\n' + '\n'.join(greeting_history)       
                page.update()
        except FileNotFoundError:
            pass

    def save_history():
        with open(HISTORY_FILE, 'w', encoding='utf-8') as file:
            for name in greeting_history:
                file.write(name + '\n')               

    def get_time_greeting():
        now = datetime.now()
        hour = now.hour
        if 6 <= hour < 12:
            return "Доброе утро"
        elif 12 <= hour < 18:
            return "Добрый день"
        elif 18 <= hour < 24:
            return "Добрый вечер"
        else:
            return "Доброй ночи"

    def on_button_click(_):
        name = name_input.value.strip()
        if name:
            greeting = get_time_greeting()
            greeting_text.value = f"{greeting}, {name}!"
            greet_button.text = "Поздороваться снова"
            name_input.value = ""

            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            greeting_history.append(f"{now} — {name}")
            history_text.value = "История приветствий:\n" + "\n".join(greeting_history)
            save_history()
        else:
            greeting_text.value = "Введите имя!"

        page.update()

    def clear_history(_):
        greeting_history.clear()
        history_text.value = "История приветствий: "
        save_history()
        page.update()

    def toggle_theme(_):
        page.theme_mode = (
            ft.ThemeMode.DARK if page.theme_mode == ft.ThemeMode.LIGHT else ft.ThemeMode.LIGHT
        )
        page.update()

    def toggle_history_visibility(_):
        history_text.visible = not history_text.visible
        toggle_history_button.text = "Показать историю" if not history_text.visible else "Скрыть историю"
        page.update()

    name_input = ft.TextField(label="Введите имя", autofocus=True, on_submit=on_button_click)

    theme_button = ft.IconButton(icon=ft.icons.BRIGHTNESS_5_ROUNDED, tooltip="Сменить тему", on_click=toggle_theme)
    greet_button = ft.ElevatedButton("Поздороваться", on_click=on_button_click)
    clear_button = ft.ElevatedButton("Очистить историю", on_click=clear_history)
    toggle_history_button = ft.ElevatedButton("Скрыть историю", on_click=toggle_history_visibility)

    page.add(
        ft.Row([theme_button, clear_button, toggle_history_button], alignment=ft.MainAxisAlignment.CENTER),
        greeting_text,
        name_input,
        greet_button,
        history_text,
    )

    load_history()

ft.app(main)
