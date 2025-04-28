#Importar Mysql 
import mysql.connector

#Conexão Mysql-Python
def conectar():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='Ka06041982*',
        database='bdassistidos'
    )

#Criar/Inserir
def criar_assistido(nome, cpf, endereco, raca, genero):
    conexao = conectar()
    cursor = conexao.cursor()
    comando = ''' INSERT INTO assistidos 
        (nome_assistido, cpf_assistido, endereço_assistido, raça_assistido, genero_assistido)
        VALUES (%s, %s, %s, %s, %s)'''
    cursor.execute(comando, (nome, cpf, endereco, raca, genero))
    conexao.commit() #Editar dados Mysql
    cursor.close()
    conexao.close()

#Listar
def listar_assistidos():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute('SELECT * FROM assistidos')
    resultado = cursor.fetchall()
    cursor.close()
    conexao.close()
    return resultado

#Editar assistidos 
def atualizar_assistido(id_assistidos, nome, cpf, endereco, raca, genero):
    conexao = conectar()
    cursor = conexao.cursor()
    comando = '''
        UPDATE assistidos 
        SET nome_assistido=%s, cpf_assistido=%s, endereço_assistido=%s, raça_assistido=%s, genero_assistido=%s
        WHERE id_assistidos=%s
    '''
    cursor.execute(comando, (nome, cpf, endereco, raca, genero, id_assistidos))
    conexao.commit()
    cursor.close()
    conexao.close()

#Excluir assistido
def deletar_assistido(id_assistidos):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute('DELETE FROM assistidos WHERE id_assistidos = %s', (id_assistidos,))
    conexao.commit()
    cursor.close()
    conexao.close()