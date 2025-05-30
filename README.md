# Sistema de Gerenciamento de Segurança - Indústrias Wayne 🦇

Projeto final do curso **Dev Full Stack**, com o objetivo de desenvolver uma aplicação completa para controle de acesso, gestão de recursos e de usuários nas instalações da empresa fictícia **Indústrias Wayne**.

---

## Funcionalidades

- Autenticação e autorização com JWT
- Permissões por perfil:
  - **Admin:** CRUD completo de usuários e recursos
  - **Funcionário:** Visualização e atualização de recursos
- CRUD completo de:
  - **Recursos:** veículos, equipamentos e dispositivos
  - **Usuários:** funcionários, gerentes e administradores
- Dashboard gráfico e funcional utilizando **Flet**
- Banco de dados PostgreSQL
- API REST integrada e testada via Insomnia

---

## Tecnologias Utilizadas

- **Backend:** Python + Flask + Flask-JWT-Extended + SQLAlchemy
- **Frontend:** [Flet](https://flet.dev) (Framework Python para UI desktop/web)
- **Banco de Dados:** PostgreSQL
- **Testes de API:** Insomnia
- **Autenticação:** JWT Tokens

---

## Estrutura do Projeto

```md
app/
├── auth.py # Endpoints de autenticação
├── config.py # Configurações gerais
├── models.py # Modelos do banco de dados
├── resources.py # Endpoints para recursos
├── usuarios.py # Endpoints para usuários
├── server.py # Configuração e inicialização do Flask
ui.py # Interface gráfica (Flet)
main.py # Inicializa backend e frontend
```

---

## Como Executar o Projeto

### 1. Instale as dependências

```bash
pip install flask flask_sqlalchemy flask_jwt_extended flet psycopg2 requests PyJWT
```

### 2. Configure o banco PostgreSQL

- Certifique-se de que o PostgreSQL está rodando.
- Crie o banco chamado:

```sql
CREATE DATABASE wayne_security;
```

> As configurações de acesso estão no arquivo `config.py`.

### 3. Execute o projeto

```bash
python main.py
```

- O backend Flask rodará em `http://localhost:5000`.
- A interface Flet abrirá automaticamente.
- Será criado um usuário admin padrão:
  - **Email:** `bruce.wayne@batmail.com`
  - **Senha:** `bruceadmin`

---

## Endpoints da API

| Método | Rota                 | Protegido  | Descrição                    |
| ------ | -------------------- | ---------- | ---------------------------- |
| POST   | `/api/register`      | ❌         | Cadastrar novo usuário       |
| POST   | `/api/login`         | ❌         | Login e geração do token     |
| GET    | `/api/recursos`      | ✅         | Lista todos os recursos      |
| POST   | `/api/recursos`      | ✅ (Admin) | Cria um novo recurso         |
| PUT    | `/api/recursos/<id>` | ✅         | Atualiza dados de um recurso |
| DELETE | `/api/recursos/<id>` | ✅ (Admin) | Deleta um recurso            |
| GET    | `/api/usuarios`      | ✅ (Admin) | Lista todos os usuários      |
| POST   | `/api/usuarios`      | ✅ (Admin) | Adiciona um novo usuário     |
| PUT    | `/api/usuarios/<id>` | ✅ (Admin) | Atualiza dados de um usuário |
| DELETE | `/api/usuarios/<id>` | ✅ (Admin) | Deleta um usuário            |

> Rotas protegidas exigem o token JWT no header:  
> `Authorization: Bearer <seu_token_aqui>`

---

## Interface Gráfica (Flet)

- Login com autenticação JWT
- Tela específica para funcionários:
  - Visualizar e atualizar recursos
- Tela administrativa:
  - CRUD completo de recursos e usuários
- Layout organizado, inputs claros, mensagens de boas-vindas e botão de logout

---

## Autor

**Victor dos Santos Mafra**  
Desenvolvedor Full Stack em formação

---
