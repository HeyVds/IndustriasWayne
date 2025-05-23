import threading
import flet as ft
from app.server import create_app

flask_app = create_app()

def run_flask():
    flask_app.run(debug=False)

threading.Thread(target=run_flask, daemon=True).start()

def main_ui(page: ft.Page):
    page.title = "Indústrias Wayne - Sistema de Segurança"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    email = ft.TextField(label="Email")
    senha = ft.TextField(label="Senha", password=True, can_reveal_password=True)
    status_text = ft.Text()

    def realizar_login(e):
        import requests
        try:
            r = requests.post("http://localhost:5000/api/login", json={"email": email.value, "password": senha.value})
            if r.status_code == 200:
                token = r.json()['token']
                status_text.value = "Login realizado com sucesso!"
                page.update()
                page.controls.clear()
                dashboard_ui(page, token)
            else:
                status_text.value = "Falha no login."
        except Exception as ex:
            status_text.value = f"Erro: {ex}"
        page.update()

    login_btn = ft.ElevatedButton("Entrar", on_click=realizar_login)
    page.add(email, senha, login_btn, status_text)

def dashboard_ui(page: ft.Page, token):
    import requests
    page.controls.append(ft.Text("Dashboard de Recursos", size=30))
    recurso_list = ft.Column()

    def carregar_recursos():
        r = requests.get("http://localhost:5000/api/recursos", headers={"Authorization": f"Bearer {token}"})
        if r.status_code == 200:
            for rec in r.json():
                recurso_list.controls.append(ft.Text(f"{rec['nome']} - {rec['tipo']} - {rec['status']}"))
        else:
            recurso_list.controls.append(ft.Text("Erro ao carregar recursos"))
        page.update()

    carregar_recursos()
    page.add(recurso_list)

ft.app(target=main_ui)
