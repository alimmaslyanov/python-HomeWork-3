import flet as ft
from datetime import datetime

def main(page: ft.Page):
    page.title = "Мое первое приложение"
    page.theme_mode = ft.ThemeMode.LIGHT
    greeting_text = ft.Text("Hello world")
    greeting_history = []

    history_text = ft.Text("История приветствий:", size="bodyMedium")

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
        else:
            greeting_text.value = "Имя я буду вводить? =)"

        page.update()

    name_input = ft.TextField(label="Введите имя", autofocus=True, on_submit=on_button_click)

    def clear_history(_):
        greeting_history.clear()
        history_text.value = "История приветствий: "
        page.update()

    def toggle_theme(_):
        page.theme_mode = (
            ft.ThemeMode.DARK if page.theme_mode == ft.ThemeMode.LIGHT else ft.ThemeMode.LIGHT
        )
        page.update()

    theme_button = ft.IconButton(icon=ft.icons.BRIGHTNESS_5_ROUNDED, tooltip="Сменить тему", on_click=toggle_theme)
    greet_button = ft.ElevatedButton("Поздороваться", on_click=on_button_click)
    clear_button = ft.ElevatedButton("Очистить историю", on_click=clear_history)

    page.add(
        ft.Row([theme_button, clear_button], alignment=ft.MainAxisAlignment.CENTER),
        greeting_text,
        name_input,
        greet_button,
        history_text,
    )

ft.app(main)