
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

```
app/
├── auth.py         
├── config.py       
├── models.py       
├── resources.py    
├── server.py       
main.py             
```

---

## Como Executar o Projeto

### 1. Instale as dependências

```bash
pip install flask flask_sqlalchemy flask_jwt_extended flet psycopg2 requests
```

### 2. Configure o banco PostgreSQL

Certifique-se de que o PostgreSQL está rodando e que o banco `wayne_security` existe.

### 3. Execute a aplicação

```bash
python main.py
```

- O Flask será executado em `http://localhost:5000`
- A interface Flet será exibida automaticamente

---

## Endpoints da API

| Método | Rota                      | Protegido? | Descrição                    |
|--------|---------------------------|------------|------------------------------|
| POST   | `/api/register`           | ❌         | Cadastra um novo usuário     |
| POST   | `/api/login`              | ❌         | Realiza login e gera token   |
| GET    | `/api/recursos`           | ✅         | Lista todos os recursos      |
| POST   | `/api/recursos`           | ✅         | Cria novo recurso            |
| PUT    | `/api/recursos/<id>`      | ✅         | Atualiza recurso existente   |
| DELETE | `/api/recursos/<id>`      | ✅         | Remove um recurso            |

> As rotas protegidas exigem o token JWT no header:  
> `Authorization: Bearer <seu_token_aqui>`

---


## 👤 Autor

**Desenvolvedor:** Victor dos Santos Mafra  

---

## Licença

Este projeto foi desenvolvido para fins educacionais.
