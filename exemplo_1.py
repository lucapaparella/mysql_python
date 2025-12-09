# importar bibliotecas
import mysql.connector
import os

#configuração da conexão
conexao = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "escola"
)

# conexão com o banco escola
cursor = conexao.cursor()

while True:
    os.system("cls")
    print("1 - Novo Cadastro")
    print("2 - Atualizar Dados")
    print("3 - Apagar Cadastro")
    print("4 -Listar Cadastros")
    print("5 - Sair")
    print("*"*15)

    while True:
        opcao = int(input("Escolha uma Opção: "))
        if opcao>0 and opcao<5:
            break
    match opcao:
        case 1:
            try: 
                nome = input("Digite o seu nome: ")
                email = input("Digite o seu E-mail: ")
                cpf = input("Digite o seu CPF: ")
                
                # criar a chamada SQL para inserir dados
                query = (f"insert into alunos(nome,email,cpf) values('{nome}','{email}','{cpf}')")
                
                # enviar a query para o banco de dados
                cursor.execute(query)
                
                # o commit finaliza o envio para o banco de dados
                conexao.commit()
                
                # Resposta do servidor MYsql: 1=> deu tudo certo
                if cursor.rowcount > 0:
                    print(f"Dados gravados com sucesso!!!")
                    input("Digite ENTER para continuar...")
                
            except mysql.connector.Error as erro:
                print(f"Erro ao inserir dados no MySQL: {erro}")
                # apagar o rascunho no Mysql
                conexao.rollback()
        
        case 2:
            try:
                nome = input("Digite o seu nome: ")
                email = input("Digite o seu E-mail: ")
                cpf = input("Digite o seu CPF: ")
                
                # criar a chamada SQL para inserir dados
                query = (f"update alunos set email ='{email}', cpf = '{cpf}' where nome ='{nome}'")
                
                # enviar a query para o banco de dados
                cursor.execute(query)
                
                # o commit finaliza o envio para o banco de dados
                conexao.commit()
                
                # Resposta do servidor MYsql: 1=> deu tudo certo
                if cursor.rowcount > 0:
                    print(f"Dados atualizados com sucesso!!!")
                    input("Digite ENTER para continuar...")
                
            except mysql.connector.Error as erro:
                print(f"Erro ao inserir dados no MySQL: {erro}")
                # apagar o rascunho no Mysql
                conexao.rollback()
            
        case 3:
            try:
                nome = input("Digite o seu nome: ")
                
                # criar a chamada SQL para inserir dados
                query = (f"delete from alunos where nome = '{nome}'")
                
                # enviar a query para o banco de dados
                cursor.execute(query)
                
                # o commit finaliza o envio para o banco de dados
                conexao.commit()
                
                # Resposta do servidor MYsql: 1=> deu tudo certo
                if cursor.rowcount > 0:
                    print(f"Dados apagados com sucesso!!!")
                    input("Digite ENTER para continuar...")
                
            except mysql.connector.Error as erro:
                print(f"Erro ao inserir dados no MySQL: {erro}")
                # apagar o rascunho no Mysql
                conexao.rollback()
        case 4:
            try:
                # criar a chamada SQL para inserir dados
                query = ("select * from alunos")
                
                # enviar a query para o banco de dados
                cursor.execute(query)
                
                # variavel de dados
                resultados = cursor.fetchall()
                
                # o commit finaliza o envio para o banco de dados
                conexao.commit()
                
                # Resposta do servidor MYsql: 1=> deu tudo certo
                if cursor.rowcount > 0:
                    print(f"Dados coletados com sucesso!!!")
                    
                    
                # for resultado in resultados:
                print(f"Resultados => {resultados}")
                input("Digite ENTER para continuar...")
                    
                
            except mysql.connector.Error as erro:
                print(f"Erro ao inserir dados no MySQL: {erro}")
                # apagar o rascunho no Mysql
                conexao.rollback()
        
        case 5:
            print("Programa Encerrado com Sucesso!!!")
            break        