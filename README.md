## 🩺 Projeto TDD – Módulo de Cadastro de Pacientes

Este repositório demonstra como aplicar **TDD (Test-Driven Development)** no desenvolvimento de um módulo simples de **cadastro de pacientes** em Python, utilizando a biblioteca `unittest`.



## 🧠 Objetivo

O objetivo é criar uma classe `Paciente` com validações internas, desenvolvida a partir de testes automatizados que seguem o ciclo TDD:

- 🔴 **Red** – Criar testes que inicialmente falham
- 🟢 **Green** – Escrever o código mínimo para passar os testes
- 🟡 **Refactor** – Melhorar o código mantendo os testes passando



## 📁 Estrutura do Projeto

📦 tdd_paciente/ 
- ├── paciente.py # Classe com as regras de negócio e validações 
- ├── test_paciente.py # Testes automatizados com unittest 
- └── README.md # Documentação do projeto
  
---

##  Sobre a Classe `Paciente`

A classe representa um paciente e realiza validações de dados no momento da criação do objeto.

### 📌 Atributos:
- `nome` (não pode ser vazio)
- `data_nascimento`
- `cpf` (não pode ser vazio)
- `telefone`
- `genero` (aceita: "Masculino", "Feminino", "Outro")
- `email` (deve estar em formato válido)

---

##  Testes Implementados

Os testes cobrem os seguintes cenários:

| Teste                          | Resultado Esperado              |
|-------------------------------|----------------------------------|
| Criar paciente válido          | ✅ Objeto criado com sucesso     |
| CPF vazio                      | ❌ Gera `ValueError`             |
| Email em formato inválido      | ❌ Gera `ValueError`             |

---

## ▶️ Como Executar os Testes

1. Abra o terminal na pasta do projeto
2. Execute:

```bash
python test_paciente.py
```

---

## ⚙️ Requisitos
Python 3.x instalado

Editor de código (VS Code)

## 💡 Aprendizados
- ✔️ Aplicação prática de TDD
- ✔️ Criação de testes automatizados
- ✔️ Validações em classes Python
- ✔️ Separação de responsabilidades (testes x lógica)
  
##
##   👩‍💻 By: Sarah Cantanhede/SarchDev
