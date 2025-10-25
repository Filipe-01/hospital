import Usuario as us

nome = input("nome: ")
dataNasc = input("data de nascimento:").strip()
dd = dataNasc[0:2]
mm = dataNasc[3:5]
aa= dataNasc[6:10]


data_formatada = "/" . join([dd,mm,aa])
qntFilhos = int(input("quantidade de filhos:"))

if (qntFilhos <0):
    raise Exception("quantidade de filhos invalida")

user01= us.Usuario(nome, data_formatada, qntFilhos)

user01.CadastrarUsuario()
user01.apresentar()

nomeBuscado = input("qual nome voce busca?").strip()
dadosEncontrados = user01.ListarUsuario(nomeBuscado)

print(dadosEncontrados)

