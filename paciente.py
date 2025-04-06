import re
from datetime import datetime

class Paciente:
    def __init__(self, nome, data_nascimento, cpf, telefone, genero, email):
        """
        Aplica validações e armazena os dados do paciente.
        """

        self.validar_nome(nome)
        self.validar_cpf(cpf)
        self.validar_email(email)

        if not self._validar_data(data_nascimento):
            raise ValueError("Data de nascimento inválida. Use o formato YYYY-MM-DD.")

        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.telefone = telefone
        self.genero = genero
        self.email = email

    @staticmethod
    def validar_nome(nome):
        """Valida se o nome não está vazio."""
        if not nome or not nome.strip():
            raise ValueError("Nome não pode ser vazio")

    @staticmethod
    def validar_cpf(cpf):
        """Valida se o CPF é composto por 11 dígitos numéricos."""
        if not cpf or not cpf.strip():
            raise ValueError("CPF é obrigatório")
        if not cpf.isdigit() or len(cpf) != 11:
            raise ValueError("CPF deve conter apenas números e ter 11 dígitos.")

    @staticmethod
    def validar_email(email):
        """Valida o formato do email."""
        padrao = r"[^@]+@[^@]+\.[^@]+"
        if not re.match(padrao, email):
            raise ValueError("Email inválido")

    @staticmethod
    def _validar_data(data):
        try:
            datetime.strptime(data, "%Y-%m-%d")
            return True
        except ValueError:
            return False