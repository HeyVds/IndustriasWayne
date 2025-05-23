# Sistema de Gerenciamento de Segurança - Indústrias Wayne

Projeto final do curso **Dev Full Stack**, com o objetivo de desenvolver uma aplicação web para controle de acesso, gestão de recursos e visualização de dados internos da empresa fictícia **Indústrias Wayne**.

## Funcionalidades

- ✅ Cadastro e login de usuários com autenticação JWT
- ✅ Controle de acesso com base em permissões (funcionário, gerente, administrador)
- ✅ CRUD completo para gerenciamento de recursos (equipamentos, veículos, dispositivos)
- ✅ Dashboard visual integrado via [Flet](https://flet.dev)
- ✅ Backend com Flask e banco de dados PostgreSQL
- ✅ Testes de API via Insomnia (prints no relatório/documentação)

---

## Tecnologias Utilizadas

- **Backend:** Python + Flask + Flask-JWT-Extended + SQLAlchemy
- **Frontend:** Flet (Framework Python para UI)
- **Banco de Dados:** PostgreSQL
- **Testes de API:** Insomnia
- **Autenticação:** JWT Tokens

---

## Estrutura do Projeto

app/
├── auth.py # Rotas de autenticação
├── config.py # Configurações do projeto
├── models.py # Modelos do banco de dados (User, Recurso)
├── resources.py # Rotas protegidas de CRUD dos recursos
├── server.py # Instância e configuração do app Flask
main.py # Integração entre Flask e Flet

---

## 🚀 Como Executar o Projeto

### 1. Instale as dependências

```bash
pip install flask flask_sqlalchemy flask_jwt_extended flet psycopg2 requests
```

## Configure o banco PostgreSQL

Certifique-se de que o PostgreSQL está rodando e que o banco wayne_security existe.

## Execute a aplicação

```bash
python main.py
```

### Autor

Victor dos santos mafra
