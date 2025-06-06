class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def exibir_dados(self):
        print(f"Nome: {self.nome}, Idade: {self.idade}")

class Aluno(Pessoa):
    def __init__(self, nome, idade, matricula, curso):
        super().__init__(nome, idade)
        self.matricula = matricula
        self.curso = curso
    def exibir_dados(self):
        super().exibir_dados()  # Chama o método da classe base
        print(f"Matrícula: {self.matricula}, Curso: {self.curso}")

# Exemplo de uso
pessoa = Pessoa("Lucas", 20)
pessoa.exibir_dados()
aluno = Aluno("Kaio", 15, "2023451", "Medicina")
aluno.exibir_dados()
