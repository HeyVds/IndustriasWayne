from app.server import create_app
from app.models import User, db
from ui import iniciar_interface
import threading

flask_app = create_app()

def criar_admin_inicial():
    with flask_app.app_context():
        admin_existente = User.query.filter_by(role='admin').first()
        if not admin_existente:
            print("Nenhum administrador encontrado. Criando admin padrão...")
            admin = User(
                name="Bruce Wayne",
                email="bruce.wayne@batmail.com",
                password="bruceadmin",
                role="admin"
            )
            db.session.add(admin)
            db.session.commit()
            print("Administrador criado com sucesso.")

def rodar_backend():
    flask_app.run(debug=False, use_reloader=False)

criar_admin_inicial()
threading.Thread(target=rodar_backend, daemon=True).start()
iniciar_interface()
