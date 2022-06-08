from tkinter import *
from tkinter import ttk
import sqlite3


#### BACK END / BANCO DE DADOS
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

        self.cursor.execute("""CREATE TABLE IF NOT EXISTS pessoas(
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

    #GETs
    def variaveis(self):
        self.nome = self.entry_nome.get()
        self.idade = self.entry_idade.get()
        self.sexo = self.entry_sexo.get()
        self.profissao = self.entry_profissao.get()
        self.estadoCivil = self.entry_estadoCivil.get()

    def limpar_campos(self):
        self.entry_pes_id.delete(0, END)
        self.entry_nome.delete(0, END)
        self.entry_idade.delete(0, END)
        self.entry_sexo.set("Selecione")
        self.entry_profissao.delete(0, END)
        self.entry_estadoCivil.set("Selecione")

    def select_lista(self):
        self.lista_pessoas.delete(* self.lista_pessoas.get_children())
        self.conecta_bd()
        lista = self.cursor.execute("""SELECT
                pes_id,
                pes_nome, 
                pes_idade, 
                pes_sexo, 
                pes_estadoCivil, 
                pes_profissao
            FROM pessoas ORDER BY pes_nome ASC; """)
        for i in lista:
            self.lista_pessoas.insert("", END, values=i)
        self.desconecta_bd()

    def duploClick(self, event):
        self.limpar_campos()
        
        self.lista_pessoas.selection()

        for n in self.lista_pessoas.selection():
            col1, col2, col3, col4, col5, col6 = self.lista_pessoas.item(n, 'values')
            self.entry_pes_id.insert(END, col1)
            self.entry_nome.insert(END, col2)
            self.entry_idade.insert(END, col3)
            self.entry_sexo.set("Selecione")
            self.entry_estadoCivil.set("Selecione")
            self.entry_profissao.insert(END, col6)

    #Função para adicionar dados a tabela pessoas
    def add_pessoa(self):
        self.variaveis()
        self.conecta_bd()
        self.cursor.execute("""INSERT INTO pessoas (
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
        self.limpar_campos()
        self.select_lista()

    def deleta_pessoa(self):

        self.conecta_bd()

        self.itemSelecionado = self.lista_pessoas.selection()[0]
        self.lista_pessoas.delete(self.itemSelecionado)

        
            
        self.pes_id = self.entry_pes_id.get()
        self.variaveis()

        self.cursor.execute("""DELETE FROM pessoas WHERE pes_id = ?""", [self.pes_id] )

        self.conn.commit()
        self.desconecta_bd()
        self.select_lista()
        self.limpar_campos()

    def edita_pessoa(self):
        self.pes_id = self.entry_pes_id.get()
        self.variaveis()
    

        self.conecta_bd()


        self.cursor.execute("""UPDATE pessoas SET 
            pes_nome = ?, 
            pes_idade = ?, 
            pes_sexo = ?, 
            pes_estadoCivil = ?, 
            pes_profissao = ?
            WHERE pes_id = ?""",
            (self.nome, self.idade, self.sexo, self.estadoCivil, self.profissao, self.pes_id))

        self.limpar_campos()
        self.conn.commit()
        self.desconecta_bd()
        self.select_lista()

    

    


#### FRONT END / JANELAS
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
        self.root.configure(background = '#363636')
        self.root.geometry('1280x720')
        self.root.resizable(True, True)
        self.root.maxsize(width=1280, height=720)
        self.root.minsize(width=800, height=600)
        

        ### LABELS


        self.lb_apresentacaoAluno = Label(self.root, text="Eduardo Pugliesi Assis Lima - 6º ADS")
        self.lb_apresentacaoAluno.place(relx=0.3, rely=0.01, relwidth=0.4, relheight=0.04)
        self.lb_apresentacaoAluno.configure(font='Arial 20 bold' ,background='#363636', foreground='white')

        self.lb_nome = Label(self.root, text="Nome")
        self.lb_nome.place(relx=0.05, rely=0.08, relwidth=0.1, relheight=0.02)
        self.lb_nome.configure(font='Arial 15 bold' ,background='#363636', foreground='white')

        self.lb_idade = Label(self.root, text="Idade")
        self.lb_idade.place(relx=0.05, rely=0.13, relwidth=0.098, relheight=0.02)
        self.lb_idade.configure(font='Arial 15 bold' ,background='#363636', foreground='white')

        self.lb_sexo = Label(self.root, text="Sexo")
        self.lb_sexo.place(relx=0.05, rely=0.18, relwidth=0.095, relheight=0.02)
        self.lb_sexo.configure(font='Arial 15 bold' ,background='#363636', foreground='white')

        self.lb_profissao = Label(self.root, text="Profissão")
        self.lb_profissao.place(relx=0.55, rely=0.13, relwidth=0.075, relheight=0.02)
        self.lb_profissao.configure(font='Arial 15 bold' ,background='#363636', foreground='white')

        self.lb_estadoCivil = Label(self.root, text="Estado Civil")
        self.lb_estadoCivil.place(relx=0.55, rely=0.08, relwidth=0.09, relheight=0.02)
        self.lb_estadoCivil.configure(font='Arial 15 bold' ,background='#363636', foreground='white')


        ### ENTRYS


        self.entry_pes_id = Entry(self.root)
        self.entry_pes_id.place(relx=0.4, rely=0.077, relwidth=0.03, relheight=0.03)
        self.entry_pes_id.configure(bg='#eeeeee')

        self.entry_nome = Entry(self.root)
        self.entry_nome.place(relx=0.13, rely=0.077, relwidth=0.26, relheight=0.03)
        self.entry_nome.configure(bg='#eeeeee')

        self.entry_idade = Entry(self.root)
        self.entry_idade.place(relx=0.13, rely=0.1277, relwidth=0.26, relheight=0.03)
        self.entry_idade.configure(bg='#eeeeee')
    
        self.entry_sexo = StringVar(self.root)
        self.entry_sexo_options = ("Masculino", "Feminino", "Outro")
        self.entry_sexo.set("Selecione")
        self.popupMenu = OptionMenu(self.root, self.entry_sexo, *self.entry_sexo_options)
        self.popupMenu.place(relx=0.13, rely=0.1777, relwidth=0.26, relheight=0.03)

        self.entry_profissao = Entry(self.root)
        self.entry_profissao.place(relx=0.645, rely=0.12777, relwidth=0.26, relheight=0.03)
        self.entry_profissao.configure(bg='#eeeeee')

        self.entry_estadoCivil = StringVar(self.root)
        self.entry_estadoCivil_options = ("Solteiro", "Casado", "Viúvo", "Divorciado", "Desistiu de viver um amor")
        self.entry_estadoCivil.set("Selecione")
        self.popupMenu = OptionMenu(self.root, self.entry_estadoCivil, *self.entry_estadoCivil_options)
        self.popupMenu.place(relx=0.645, rely=0.07777, relwidth=0.26, relheight=0.03)


        ### BUTTONS


        self.bt_cadastrar = Button(self.root, text="Cadastrar", command = self.add_pessoa)
        self.bt_cadastrar.place(relx= 0.55, rely=0.1777, relwidth=0.08, relheight=0.03)
        self.bt_cadastrar.configure(font='Arial 12 bold', bd=2, bg='#eeeeee')

        self.bt_editar = Button(self.root, text="Editar", command = self.edita_pessoa)
        self.bt_editar.place(relx= 0.645, rely=0.1777, relwidth=0.08, relheight=0.03)
        self.bt_editar.configure(font='Arial 12 bold', bd=2, bg='#eeeeee')

        self.bt_apagar = Button(self.root, text="Apagar", command = self.deleta_pessoa)
        self.bt_apagar.place(relx= 0.735, rely=0.1777, relwidth=0.08, relheight=0.03)
        self.bt_apagar.configure(font='Arial 12 bold', bd=2, bg='#eeeeee')

        self.bt_limpar = Button(self.root, text="Limpar", command = self.limpar_campos)
        self.bt_limpar.place(relx= 0.825, rely=0.1777, relwidth=0.08, relheight=0.03)
        self.bt_limpar.configure(font='Arial 12 bold', bd=2, bg='#eeeeee')


        ############################## FRAME


        self.mostraPessoas = Frame(self.root)
        self.mostraPessoas.place(relx= 0.05, rely=0.25, relwidth=0.9, relheight=0.7)


        ############################## LISTBOX


        #Criando lista dos veículos
        self.lista_pessoas = ttk.Treeview(self.mostraPessoas, height=1, columns=("col1", "col2", "col3", "col4", "col5", "col6"))

        #Atributos da Lista

        self.lista_pessoas.heading("#0", text="")
        self.lista_pessoas.column("#0", minwidth=0, width=0, stretch=NO)

        
        self.lista_pessoas.heading("#1", text="ID")
        self.lista_pessoas.column("#1", minwidth=40, width=40, stretch=NO, anchor=CENTER)

        
        self.lista_pessoas.heading("#2", text="Nome")
        self.lista_pessoas.column("#2", minwidth=310, width=310, stretch=NO, anchor=CENTER)

        
        self.lista_pessoas.heading("#3", text="Idade")
        self.lista_pessoas.column("#3", minwidth=80, width=80, stretch=NO, anchor=CENTER)

        
        self.lista_pessoas.heading("#4", text="Sexo")
        self.lista_pessoas.column("#4", minwidth=150, width=150, stretch=NO, anchor=CENTER)

        
        self.lista_pessoas.heading("#5", text="Estado Civil")
        self.lista_pessoas.column("#5", minwidth=300, width=300, stretch=NO, anchor=CENTER)

        
        self.lista_pessoas.heading("#6", text="Profissão")
        self.lista_pessoas.column("#6", minwidth=255, width=255, stretch=NO, anchor=CENTER)

  
        
        #Posicionamento da lista
        self.lista_pessoas.place(relx=0, rely=0, relwidth=1.05, relheight=1.05)


        ############################## SCROLLBAR


        self.scrolllista_pessoas = Scrollbar(self.lista_pessoas, orient='vertical')
        self.lista_pessoas.configure(yscroll=self.scrolllista_pessoas.set)
        self.scrolllista_pessoas.place(relx=0.935, rely=0, relwidth=0.02, relheight=0.96)

        self.lista_pessoas.bind("<Double-1>", self.duploClick)
        
        self.select_lista()
        root.mainloop()

        
FrontEnd()