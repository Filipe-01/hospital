#usuario.py#
class Usuario:
    dic={}
  
    def __init__(self, nome, dtNascimento, filhos):

        self.nome = nome
        self.dtNascimento = dtNascimento
        self.filhos = filhos
        #self.dic={}#

    def apresentar(self):
     print(f"ola, meu nome é {self.nome} nasci em {self.dtNascimento}")  

    def CadastrarUsuario(self):
        self.dic[self.nome] = {"data_Nascimento":self.dtNascimento, "qntFilhos": self.filhos}   

    def ListarUsuario(self,nome):
        try:
            nomeEncontrado = self.dic[nome]
        except (KeyError):  
         print("nome nao existente")
        else:
         return nomeEncontrado
        finally:
         print("operaçao concluida")  