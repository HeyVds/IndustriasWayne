import flet as ft
import requests
import jwt

def iniciar_interface():
    ft.app(target=main_ui)

def main_ui(page: ft.Page):
    page.title = "Indústrias Wayne - Sistema de Segurança"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    status_text = ft.Text()
    email = ft.TextField(label="Email", width=250)
    senha = ft.TextField(label="Senha", password=True, can_reveal_password=True, width=250)

    def realizar_login(e):
        try:
            r = requests.post("http://localhost:5000/api/login", json={
                "email": email.value,
                "password": senha.value
            })
            if r.status_code == 200:
                token = r.json()['token']
                decoded = jwt.decode(token, options={"verify_signature": False})
                nome_usuario = decoded.get('name')
                role_usuario = decoded.get('role')

                status_text.value = f"Bem-vindo, {nome_usuario}!"
                page.controls.clear()

                if role_usuario == "admin":
                    dashboard_admin(page, token, nome_usuario)
                else:
                    dashboard_funcionario(page, token, nome_usuario)

            else:
                status_text.value = "Falha no login"
        except Exception as ex:
            status_text.value = f"Erro: {ex}"
        page.update()

    login_btn = ft.ElevatedButton("Entrar", on_click=realizar_login)
    page.add(
        ft.Text("Login no Sistema", size=25),
        email,
        senha,
        login_btn,
        status_text
    )

def dashboard_funcionario(page: ft.Page, token, nome):
    def sair(e):
        page.controls.clear()
        main_ui(page)

    page.controls.append(
        ft.Row([
            ft.Text(f"Bem-vindo, {nome}", size=20, weight="bold"),
            ft.ElevatedButton("Sair", on_click=sair)
        ], alignment="spaceBetween")
    )
    page.controls.append(ft.Text("Dashboard de Recursos", size=25))
    recurso_list = ft.Column()

    nome_field = ft.TextField(label="Nome", width=200)
    tipo_field = ft.TextField(label="Tipo", width=200)
    status_field = ft.TextField(label="Status", width=200)
    id_field = ft.TextField(label="ID (para atualizar)", width=200)

    def carregar_recursos(e=None):
        recurso_list.controls.clear()
        r = requests.get("http://localhost:5000/api/recursos", headers={
            "Authorization": f"Bearer {token}"
        })
        if r.status_code == 200:
            for rec in r.json():
                recurso_list.controls.append(
                    ft.Row([
                        ft.Text(f"ID: {rec['id']}", width=50),
                        ft.Text(f"Nome: {rec['nome']}", width=200),
                        ft.Text(f"Tipo: {rec['tipo']}", width=150),
                        ft.Text(f"Status: {rec['status']}", width=150)
                    ])
                )
        else:
            recurso_list.controls.append(ft.Text("Erro ao carregar recursos"))
        page.update()

    def atualizar_recurso(e):
        recurso_id = id_field.value
        data = {
            "nome": nome_field.value,
            "tipo": tipo_field.value,
            "status": status_field.value
        }
        requests.put(f"http://localhost:5000/api/recursos/{recurso_id}", headers={
            "Authorization": f"Bearer {token}"
        }, json=data)
        limpar_campos()
        carregar_recursos()

    def limpar_campos():
        nome_field.value = ""
        tipo_field.value = ""
        status_field.value = ""
        id_field.value = ""
        page.update()

    page.add(
        ft.Row([nome_field, tipo_field, status_field]),
        ft.Row([id_field]),
        ft.Row([
            ft.ElevatedButton("Atualizar", on_click=atualizar_recurso),
            ft.ElevatedButton("Atualizar Lista", on_click=carregar_recursos),
        ]),
        ft.Container(recurso_list, padding=10)
    )

    carregar_recursos()

def dashboard_admin(page: ft.Page, token, nome):
    def sair(e):
        page.controls.clear()
        main_ui(page)

    page.controls.append(
        ft.Row([
            ft.Text(f"Bem-vindo, {nome} (Admin)", size=20, weight="bold"),
            ft.ElevatedButton("Sair", on_click=sair)
        ], alignment="spaceBetween")
    )
    page.controls.append(ft.Text("Dashboard Admin - Gestão de Recursos", size=25))
    recurso_list = ft.Column()

    nome_field = ft.TextField(label="Nome", width=200)
    tipo_field = ft.TextField(label="Tipo", width=200)
    status_field = ft.TextField(label="Status", width=200)
    id_field = ft.TextField(label="ID (para editar/deletar)", width=200)

    def carregar_recursos(e=None):
        recurso_list.controls.clear()
        r = requests.get("http://localhost:5000/api/recursos", headers={
            "Authorization": f"Bearer {token}"
        })
        if r.status_code == 200:
            for rec in r.json():
                recurso_list.controls.append(
                    ft.Row([
                        ft.Text(f"ID: {rec['id']}", width=50),
                        ft.Text(f"Nome: {rec['nome']}", width=200),
                        ft.Text(f"Tipo: {rec['tipo']}", width=150),
                        ft.Text(f"Status: {rec['status']}", width=150)
                    ])
                )
        else:
            recurso_list.controls.append(ft.Text("Erro ao carregar recursos"))
        page.update()

    def adicionar_recurso(e):
        data = {
            "nome": nome_field.value,
            "tipo": tipo_field.value,
            "status": status_field.value
        }
        requests.post("http://localhost:5000/api/recursos", headers={
            "Authorization": f"Bearer {token}"
        }, json=data)
        limpar_campos()
        carregar_recursos()

    def atualizar_recurso(e):
        recurso_id = id_field.value
        data = {
            "nome": nome_field.value,
            "tipo": tipo_field.value,
            "status": status_field.value
        }
        requests.put(f"http://localhost:5000/api/recursos/{recurso_id}", headers={
            "Authorization": f"Bearer {token}"
        }, json=data)
        limpar_campos()
        carregar_recursos()

    def deletar_recurso(e):
        recurso_id = id_field.value
        requests.delete(f"http://localhost:5000/api/recursos/{recurso_id}", headers={
            "Authorization": f"Bearer {token}"
        })
        limpar_campos()
        carregar_recursos()

    def limpar_campos():
        nome_field.value = ""
        tipo_field.value = ""
        status_field.value = ""
        id_field.value = ""
        page.update()

    page.add(
        ft.Row([nome_field, tipo_field, status_field]),
        ft.Row([id_field]),
        ft.Row([
            ft.ElevatedButton("Adicionar", on_click=adicionar_recurso),
            ft.ElevatedButton("Atualizar", on_click=atualizar_recurso),
            ft.ElevatedButton("Deletar", on_click=deletar_recurso),
            ft.ElevatedButton("Atualizar Lista", on_click=carregar_recursos),
        ]),
        ft.Container(recurso_list, padding=10)
    )

    page.controls.append(ft.Container(height=30))
    page.controls.append(ft.Text("Gestão de Usuários", size=25))
    usuario_list = ft.Column()

    nome_user = ft.TextField(label="Nome", width=200)
    email_user = ft.TextField(label="Email", width=200)
    senha_user = ft.TextField(label="Senha", width=200)
    role_user = ft.TextField(label="Role", width=200)
    id_user = ft.TextField(label="ID (para editar/deletar)", width=200)

    def carregar_usuarios(e=None):
        usuario_list.controls.clear()
        r = requests.get("http://localhost:5000/api/usuarios", headers={
            "Authorization": f"Bearer {token}"
        })
        if r.status_code == 200:
            for user in r.json():
                usuario_list.controls.append(
                    ft.Row([
                        ft.Text(f"ID: {user['id']}", width=50),
                        ft.Text(f"Nome: {user['name']}", width=150),
                        ft.Text(f"Email: {user['email']}", width=250),
                        ft.Text(f"Role: {user['role']}", width=100)
                    ])
                )
        else:
            usuario_list.controls.append(ft.Text("Erro ao carregar usuários"))
        page.update()

    def adicionar_usuario(e):
        data = {
            "name": nome_user.value,
            "email": email_user.value,
            "password": senha_user.value,
            "role": role_user.value
        }
        requests.post("http://localhost:5000/api/usuarios", headers={
            "Authorization": f"Bearer {token}"
        }, json=data)
        limpar_user()
        carregar_usuarios()

    def atualizar_usuario(e):
        usuario_id = id_user.value
        data = {
            "name": nome_user.value,
            "email": email_user.value,
            "password": senha_user.value,
            "role": role_user.value
        }
        requests.put(f"http://localhost:5000/api/usuarios/{usuario_id}", headers={
            "Authorization": f"Bearer {token}"
        }, json=data)
        limpar_user()
        carregar_usuarios()

    def deletar_usuario(e):
        usuario_id = id_user.value
        requests.delete(f"http://localhost:5000/api/usuarios/{usuario_id}", headers={
            "Authorization": f"Bearer {token}"
        })
        limpar_user()
        carregar_usuarios()

    def limpar_user():
        nome_user.value = ""
        email_user.value = ""
        senha_user.value = ""
        role_user.value = ""
        id_user.value = ""
        page.update()

    page.add(
        ft.Row([nome_user, email_user, senha_user, role_user]),
        ft.Row([id_user]),
        ft.Row([
            ft.ElevatedButton("Adicionar", on_click=adicionar_usuario),
            ft.ElevatedButton("Atualizar", on_click=atualizar_usuario),
            ft.ElevatedButton("Deletar", on_click=deletar_usuario),
            ft.ElevatedButton("Atualizar Lista", on_click=carregar_usuarios),
        ]),
        ft.Container(usuario_list, padding=10)
    )

    carregar_recursos()
    carregar_usuarios()
