import unittest
from paciente import Paciente

# Etapa RED: criamos o teste antes da implementação da classe

class TestPaciente(unittest.TestCase):
    def test_criacao_paciente(self):
        paciente = Paciente(
            nome="Sarah Cantanhede",
            data_nascimento="2003-05-03",
            cpf="08596841300",
            telefone="(98)98421-0907",
            genero="Feminino",
            email="catanhedesarah@example.com"
        )
        self.assertEqual(paciente.nome, "Sarah Cantanhede")

    def test_cpf_vazio(self):
        with self.assertRaises(ValueError):
            Paciente(
                nome="João",
                data_nascimento="2000-01-01",
                cpf="",
                telefone="(11)99999-9999",
                genero="Masculino",
                email="joao@example.com"
            )

    def test_email_invalido(self):
        with self.assertRaises(ValueError):
            Paciente(
                nome="Somaycon",
                data_nascimento="1985-12-01",
                cpf="11122233344",
                telefone="(11)91111-1111",
                genero="Masculino",
                email="somay.com"
            )

    def test_nome_vazio(self):
        with self.assertRaises(ValueError):
            Paciente(
                nome="",
                data_nascimento="1990-01-01",
                cpf="22233344455",
                telefone="(11)98888-7777",
                genero="Outro",
                email="gustavo@teste.com"
            )

    def test_genero(self):
        paciente = Paciente(
            nome="igor",
            data_nascimento="2000-03-26",
            cpf="121212121",
            telefone="(98)99969-9010",
            genero="Masculino",
            email="igor@example.com"
        )
        self.assertIn(paciente.genero, ["Masculino", "Feminino", "Outro"])

if __name__ == "__main__":
    unittest.main()
