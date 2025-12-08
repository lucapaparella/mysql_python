# importar biblioteca
import mysql.connector

#configuração da conexão
conexao = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "escola"
)

try:
    # conexão com o banco escola
    cursor = conexao.cursor()
    
    nome = input("Digite o seu nome: ")
    email = input("Digite o seu E-mail: ")
    cpf = input("Digite o seu CPF: ")
    
    # criar a chamada SQL para inserir dados
    query = (f"insert into alunos(nome,email,cpf) values('{nome}','{email}','{cpf}')")
    
    # enviar a query para o banco de dados
    cursor.execute(query)
    
    # o commit finaliza o envio para o banco de dados
    conexao.commit()
    
    
except mysql.connector.Error as erro:
    print(f"Erro ao inserir dados no MySQL: {erro}")