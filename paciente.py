
import re

class Paciente:
    def __init__(self, nome, data_nascimento, cpf, telefone, genero, email):
        """
        Aplica validações e armazena os dados do paciente.
        """

        self.validar_nome(nome)
        self.validar_cpf(cpf)
        self.validar_email(email)

        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.telefone = telefone
        self.genero = genero
        self.email = email

    # Etapa REFACTOR: extraímos validações para métodos separados, mantendo o comportamento
    @staticmethod
    def validar_nome(nome):
        """Valida se o nome não está vazio."""
        if not nome or not nome.strip():
            raise ValueError("Nome não pode ser vazio")

    @staticmethod
    def validar_cpf(cpf):
        """Valida se o CPF não está vazio."""
        if not cpf or not cpf.strip():
            raise ValueError("CPF é obrigatório")

    @staticmethod
    def validar_email(email):
        """Valida o formato do email."""
        padrao = r"[^@]+@[^@]+\.[^@]+"
        if not re.match(padrao, email):
            raise ValueError("Email inválido")
