import random


class Dado:
    def __init__(self, min_vel=1, max_vel=6):
        self.min = min_vel
        self.min_original = min_vel
        self.max = max_vel
        self.max_original = max_vel

    def jogar(self, n_dados=1, separado=False):
        # Joga os dados no tabuleiro, sorteando um número entre o máximo e mínimo
        # Sorteia quando vezes for solicitado
        # Pode devolver só a soma dos sorteios ou o resultado individual de cada
        numeros = []
        result = 0
        x = 0
        while x < n_dados:
            x += 1
            numeros.append(int(random.uniform(self.min, self.max)))
        for x in numeros:
            result += x
        if not separado:
            return result
        elif separado:
            return result, numeros

    def altera_min_max(self, min_vel=0, max_vel=6):
        # Altera valor mínimo e máximo das faces
        self.min = min_vel
        self.max = max_vel

    def reseta_valores(self):
        # Reseta para valoeres originais
        self.min = self.min_original
        self.max = self.max_original


class Interacao:
    def __init__(self, dado_obj):
        self.dado = dado_obj
        self.individual = False

    def inicia(self):
        # Ao Iniciar o programa
        print('********************')
        print('*****DadoSystem*****')
        print('********************')
        print('\n')
        print('Olá, bem vindo!')

    def tratar(self, string):
        # Tenta tranformar string em um inteiro, ou deixa a string toda e low
        result = string
        try:
            result = int(string)
        except:
            result = string.lower()
        finally:
            return result

    def print_config_alteracao(self):
        # Print a explicação de como fazer a alteração dos valoeres mínimos e máximos dos dados
        print("-Em caso de dois valores separados por um espaço (' ') "
              "o primeiro será o valor mínimo e p segundo o valor máximo;")
        print("-Em caso de um único valor, esse valor será inválido;")
        print(
            f"-Para alterar o valor máximo, coloque {self.dado.min} "
            f"(que é o atual valor mínimo), espaço e o novo valor máximo;")
        print(
            f"-Para alterar o valor mínimo, coloque o novo valor mínimo, espaço e {self.dado.max} "
            f"(que é o atual valor máximo);")
        print("-Outras entradas são inválidas.\n")
        self.alterar_max_min()

    def alterar_max_min(self):
        # Altera valor mínimo e máximo das faces do dado
        result = input('Qual os valores? (e para explicação):')
        result = result.lower()
        if result == 'e':
            self.print_config_alteracao()
        else:
            result = result.split()
            result_tratado = []
            for x in result:
                x = self.tratar(x)
                if isinstance(x, int):
                    result_tratado.append(x)
                else:
                    result_tratado = 'Iválido'
            if result_tratado == 'Inválido':
                print('Inválido')
            else:
                min_vel, max_vel = self.desempacotar_alteracoes(result_tratado)
                self.dado.altera_min_max(min_vel, max_vel)
                print(f'Novo mínimo {self.dado.min}')
                print(f'Novo máximo {self.dado.max}')

    def desempacotar_alteracoes(self, vel):
        # Tenta desempacotar os valores alterados
        vel_1, vel_2 = 0, 0
        try:
            vel_1, vel_2 = vel
        except:
            print('Valore inválidos, operação falhou.')
            vel_1, vel_2 = self.dado.min, self.dado.max
        finally:
            return vel_1, vel_2

    def alterar_individual(self):
        # Altera se os valores viram separador ou não
        if not self.individual:
            self.individual = True
        elif self.individual:
            self.individual = False

    def comandos(self):
        # Printa os comando disponíveis
        print("'' ou 'j' para Jogo simples;")
        print("Número x para Jogar x vezes o dado;")
        print("'a' para alterar máximo e mínimo dos valores das faces do dado;")
        print("'i' para alterar se você quer ou não os valores individuais de cada jogada no tabuleiro;")
        print("'e' para sair;")
        print("'c' para ver os comandos.")
        self.entrada_usuario()

    def entrada_usuario(self):
        # Faz a entrada do usuário, aceita comandos
        answer = input("Deseja jogar os dados ou alterar o valores?: \n('c' para ver comandos)\n")
        answer = self.tratar(answer)

        if answer == "" or answer == "j":
            result = self.dado.jogar(separado=self.individual)
            return result
        elif isinstance(answer, int):
            result = self.dado.jogar(n_dados=answer, separado=self.individual)
            return result
        elif answer == 'a':
            self.alterar_max_min()
        elif answer == "e":
            return False
        elif answer == 'i':
            self.alterar_individual()
        elif answer == 'c':
            self.comandos()
        else:
            print('Não entendi.')


if __name__ == '__main__':
    dado = Dado()
    inter = Interacao(dado)

    inter.inicia()
    resultado = inter.entrada_usuario()
    if resultado is None:
        pass
    else:
        print(resultado)
