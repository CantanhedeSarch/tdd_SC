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
        #deve dar erro no email
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
        #deve dar erro no nome
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
        #deve dar erro pois o paciente não possui 11 digitos
        paciente = Paciente(
            nome="igor",
            data_nascimento="2000-03-26",
            cpf="12345678901",
            telefone="(98)99969-9010",
            genero="Masculino",
            email="igor@example.com"
        )
        self.assertIn(paciente.genero, ["Masculino", "Feminino", "Outro"])

    def test_cpf_com_letras(self):
        #deve dar erro no cpf por conter letras
        with self.assertRaises(ValueError):
            Paciente(
                    nome="Roberto carlos",
                    data_nascimento="1990-05-12",
                    cpf="abc12345678",
                    telefone="98999999999",
                    genero="Masculino",
                    email="carlosroberto@gmail.com"
            )

    def test_dt_nascimento_invalida(self):
        #deve dar erro na data de nascimento por conta do formato
        with self.assertRaises(ValueError):
            Paciente(
                nome="Gerson",
                data_nascimento="20-03-1995", 
                cpf="12345678900",
                telefone="98999999999",
                genero="Masculino",
                email="gerson@gmail.com"
            )

if __name__ == "__main__":
    unittest.main()
