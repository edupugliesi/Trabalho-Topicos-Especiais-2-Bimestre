from tkinter import *
from tkinter import ttk
import sqlite3

class BackEnd():

    #Função para conectar ao banco de dados
    def conecta_bd(self):
        self.conn = sqlite3.connect("CRUD.bd")
        self.cursor = self.conn.cursor(); print("Conectado ao banco de dados")
    
    #Função para desconectar do banco de dados
    def desconecta_bd(self):
        self.conn.close(); print("Desconectado do banco de dados")

    #Função para criar a tabela do banco de dados
    def montaTabelaCRUD(self):
        self.conecta_bd()

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS pessoas(
                pes_id INTEGER primary key,
                pes_nome char(20) NOT NULL,
                pes_idade INTEGER NOT NULL,
                pes_sexo char(10) NOT NULL,
                pes_profissao char(10) NOT NULL,
                pes_estadoCivil char(10) NOT NULL
            );
        """)

        self.conn.commit(); print("Banco de dados criado")
        self.desconecta_bd()

    #Função para adicionar dados a tabela pessoas
    def add_pessoa(self):
        self.conecta_bd()
        self.cursor.execute(""" 
            INSERT INTO pessoas (
                pes_nome, 
                pes_idade, 
                pes_sexo, 
                pes_profissao, 
                pes_estadoCivil
            )
            VALUES (?, ?, ?, ?, ?) """, (
                self.nome, 
                self.idade, 
                self.sexo, 
                self.profissao, 
                self.estadoCivil
            )
        )
        self.conn.commit()
        self.desconecta_bd()
    

class FrontEnd(BackEnd):

    #Função de inicialização do sistema
    def __init__(self):

        #Chamar funções do banco de dados
        self.montaTabelaCRUD()

        #Chamar janela
        self.janelaPrincipal()


    
    #Janela Principal
    def janelaPrincipal(self):



        #Configurações visuais e comportamentais da Janela
        root = Tk()
        self.root = root
        self.root.title("CRUD")
        self.root.configure(background = '#DDA0DD')
        self.root.geometry('1280x720')
        self.root.resizable(True, True)
        self.root.maxsize(width=1280, height=720)
        self.root.minsize(width=800, height=600)


        ### LABELS

        self.lb_apresentacaoAluno = Label(self.root, text="Eduardo Pugliesi Assis Lima - 6º ADS")
        self.lb_apresentacaoAluno.place(relx=0.35, rely=0.05, relwidth=0.3, relheight=0.1)
        self.lb_apresentacaoAluno.configure(font='Arial 12 bold' ,background='#DDA0DD', foreground='white')

        
