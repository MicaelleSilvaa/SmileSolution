import tkinter as tk
import customtkinter
from tkinter import PhotoImage
from tkinter import ttk, font
from tkinter import messagebox
from caixa import Banco


class ModeloTelaPrincipal():
    def __init__(self, janela):
        self.janela = janela
        self.janela.title('Acesso')
        self.janela.geometry('1000x600+450+100')
        self.janela.configure(bg='#173561')
        self.janela['bg'] = '#173561'

        self.img = PhotoImage(file='imagens/01.png')
        self.img_reduzida = self.img.subsample(5, 5)  # Reduzindo o tamanho da imagem pela metade
        self.label_imagem = tk.Label(self.janela, image=self.img_reduzida, borderwidth=0)
        self.label_imagem.place(x=460, y=0)

        self.label_clinica = customtkinter.CTkLabel(self.janela, text='SmileSolution', font=('Roboto', 40, 'bold'), text_color='#FFFFFF', fg_color='#173561')
        self.label_clinica.place(x=100, y=70)
        
        self.label_slogan = customtkinter.CTkLabel(self.janela, text='Seu sorriso, nossa paixão!', font=('Roboto', 20), text_color='#FFFFFF', fg_color='#173561')
        self.label_slogan.place(x=115, y=110)
        
        self.label_titulo = customtkinter.CTkLabel(self.janela, text='Bem-vindo!', font=('Roboto', 30, 'bold'), text_color='#FFFFFF', fg_color='#173561')
        self.label_titulo.place(x=150, y=200)
        
        self.label_titulo = customtkinter.CTkLabel(self.janela, text='Por favor selecione o seu acesso', font=('Roboto', 15), text_color='#FFFFFF', fg_color='#173561')
        self.label_titulo.place(x=115, y=230)

        self.botao_admin = customtkinter.CTkButton(self.janela, text='Administrador', font=('Roboto', 15),
                                                   text_color='#173561', fg_color='#FFFFFF', command=self.telaloginAdmin)
        self.botao_admin.place(x=160, y=300)

        self.botao_recep = customtkinter.CTkButton(self.janela, text='Recepcionista', font=('Roboto', 15),
                                                   text_color='#173561', fg_color='#FFFFFF', command=self.telaloginRecep)
        self.botao_recep.place(x=160, y=350)

        self.label_criado = customtkinter.CTkLabel(self.janela, text='Desenvolvido por Micaelle Silva ©', font=('Roboto', 15), text_color='#FFFFFF', fg_color='#173561')
        self.label_criado.place(x=120, y=570)

    def telaloginAdmin(self):
        self.janela.withdraw()  # Oculta a janela principal
        nova_janela = tk.Toplevel(self.janela)
        tela_login_admin = TelaLoginAdmin(nova_janela)
        
    def telaloginRecep(self):
        self.janela.withdraw()  # Oculta a janela principal
        nova_janela1 = tk.Toplevel(self.janela)
        tela_login_recep = TelaLoginRecep(nova_janela1)

            
       
        
#----------------------------------TELA ADMIN--------------------------------------------------

class TelaLoginAdmin():
    def __init__(self, janela):
        self.janela = janela
        self.janela.title('Login administrador')
        self.janela.geometry('1000x600+450+100')
        self.janela['bg'] = '#173561'
        
        self.label_clinica = customtkinter.CTkLabel(self.janela, text='SmileSolution', font=('Roboto', 40, 'bold'), text_color='#FFFFFF', fg_color='#173561')
        self.label_clinica.place(x=100, y=70)
        
        self.label_slogan = customtkinter.CTkLabel(self.janela, text='Seu sorriso, nossa paixão!', font=('Roboto', 20), text_color='#FFFFFF', fg_color='#173561')
        self.label_slogan.place(x=115, y=110)
        
        self.label_titulo = customtkinter.CTkLabel(self.janela, text='Bem-vindo!', font=('Roboto', 30, 'bold'), text_color='#FFFFFF', fg_color='#173561')
        self.label_titulo.place(x=150, y=200)
                
        self.img = PhotoImage(file='imagens/01.png')
        self.img_reduzida = self.img.subsample(5, 5)  # Reduzindo o tamanho da imagem pela metade
        self.label_imagem = tk.Label(self.janela, image=self.img_reduzida, borderwidth=0)
        self.label_imagem.place(x=460, y=0)

        self.label_login_admin = customtkinter.CTkLabel(self.janela, text='Código', font=('Roboto', 15), text_color='#FFFFFF', fg_color='#173561')
        self.label_login_admin.place(x=150, y=250)
        
        self.caixa_login_admin = customtkinter.CTkEntry(self.janela, placeholder_text='Digite seu código', font=('Roboto', 15), text_color='#FFFFFF', fg_color='#173561')
        self.caixa_login_admin.place(x=150, y=280)
        
        self.label_senha_admin = customtkinter.CTkLabel(self.janela, text='Senha', font=('Roboto', 15), text_color='#FFFFFF', fg_color='#173561')
        self.label_senha_admin.place(x=150, y=320)
        
        self.caixa_senha_admin = customtkinter.CTkEntry(self.janela, placeholder_text='Digite sua senha', font=('Roboto', 15), text_color='#FFFFFF', fg_color='#173561')
        self.caixa_senha_admin.place(x=150, y=350)
        
        self.botao_entrarAdmin = customtkinter.CTkButton(self.janela,text='Entrar', font=('Roboto', 12, 'bold', ), text_color='#173561', fg_color='#FFFFFF' )
        self.botao_entrarAdmin.place(x=150,y=400)
        
        self.label_criado = customtkinter.CTkLabel(self.janela, text='Desenvolvido por Micaelle Silva ©', font=('Roboto', 15), text_color='#FFFFFF', fg_color='#173561')
        self.label_criado.place(x=120, y=570)

        # Resto do código para construir a nova janela de login admin...

        self.janela.protocol("WM_DELETE_WINDOW", self.voltar_tela_principal)  # Define a ação ao fechar a janela

    def voltar_tela_principal(self):
        self.janela.destroy()  # Destroi a janela de login admin
        objeto.janela.deiconify()  # Exibe novamente a janela principal
        
        
#----------------------------------TELA RECEPCIONISTA--------------------------------------------------

        
class TelaLoginRecep():
    def __init__(self, janela1):
        self.janela1 = janela1
        self.janela1.title('Login recepcionista')
        self.janela1.geometry('1000x600+450+100')
        self.janela1['bg'] = '#173561'
        
        self.img = PhotoImage(file='imagens/01.png')
        self.img_reduzida = self.img.subsample(5, 5)  # Reduzindo o tamanho da imagem pela metade
        self.label_imagem = tk.Label(self.janela1, image=self.img_reduzida, borderwidth=0)
        self.label_imagem.place(x=460, y=0)
       
        self.label_clinica = customtkinter.CTkLabel(self.janela1, text='SmileSolution', font=('Roboto', 40, 'bold'), text_color='#FFFFFF', fg_color='#173561')
        self.label_clinica.place(x=100, y=70)
        
        self.label_slogan = customtkinter.CTkLabel(self.janela1, text='Seu sorriso, nossa paixão!', font=('Roboto', 20), text_color='#FFFFFF', fg_color='#173561')
        self.label_slogan.place(x=115, y=110)
        
        self.label_titulo = customtkinter.CTkLabel(self.janela1, text='Bem-vindo!', font=('Roboto', 30, 'bold'), text_color='#FFFFFF', fg_color='#173561')
        self.label_titulo.place(x=150, y=200)
        
        self.label_login_recep = customtkinter.CTkLabel(self.janela1, text='Código', font=('Roboto', 15), text_color='#FFFFFF', fg_color='#173561')
        self.label_login_recep.place(x=150, y=250)
        
        self.caixa_login_recep = customtkinter.CTkEntry(self.janela1, placeholder_text='Digite seu código', font=('Roboto', 15), text_color='#FFFFFF', fg_color='#173561')
        self.caixa_login_recep.place(x=150, y=280)
        
        self.label_senha_recep = customtkinter.CTkLabel(self.janela1, text='Senha', font=('Roboto', 15), text_color='#FFFFFF', fg_color='#173561')
        self.label_senha_recep.place(x=150, y=320)
        
        self.caixa_senha_recep = customtkinter.CTkEntry(self.janela1, placeholder_text='Digite sua senha', font=('Roboto', 15), text_color='#FFFFFF', fg_color='#173561')
        self.caixa_senha_recep.place(x=150, y=350)
        
        self.botao_entrarRecep = customtkinter.CTkButton(self.janela1,text='Entrar', font=('Roboto', 12, 'bold', ),
                                                         text_color='#173561', fg_color='#FFFFFF', command=self.telaacessoRecep)
        self.botao_entrarRecep.place(x=150,y=400)
        
              
        self.label_criado = customtkinter.CTkLabel(self.janela1, text='Desenvolvido por Micaelle Silva ©', font=('Roboto', 15), text_color='#FFFFFF', fg_color='#173561')
        self.label_criado.place(x=120, y=570)

    def telaacessoRecep(self):
        self.janela1.withdraw()  # Oculta a janela principal
        nova_janela2 = tk.Toplevel(self.janela1)
        tela_acesso_recep = TelaAcessoRecep(nova_janela2)

        # Resto do código para construir a nova janela de login admin...

        self.janela1.protocol("WM_DELETE_WINDOW", self.voltar_tela_principal)  # Define a ação ao fechar a janela

    def voltar_tela_principal(self):
        self.janela1.destroy()  # Destroi a janela de login admin
        objeto.janela.deiconify()  # Exibe novamente a janela principal
        
class TelaAcessoRecep():
    def __init__(self, janela2):
        self.janela2 = janela2
        self.janela2.title('Acesso recepcionista')
        self.janela2.geometry('1000x600+450+100')
        self.janela2['bg'] = '#173561'
        
        self.img = PhotoImage(file='imagens/01.png')
        self.img_reduzida = self.img.subsample(5, 5)  # Reduzindo o tamanho da imagem pela metade
        self.label_imagem = tk.Label(self.janela2, image=self.img_reduzida, borderwidth=0)
        self.label_imagem.place(x=460, y=0)
        
        self.janela2.protocol("WM_DELETE_WINDOW", self.voltar_tela_principal)  # Define a ação ao fechar a janela

#----------------------------DADOS DO CLIENTE------------------------------------------------------------------

        #self.criar_tabela()

        self.label_cadastro = customtkinter.CTkLabel(self.janela2, text='Cadastro de paciente', font=('Roboto', 20, 'bold'), text_color='#FFFFFF', fg_color='#173561')
        self.label_cadastro.place(x=120, y=60)

        self.cliente = customtkinter.CTkLabel(self.janela2, text='Nome', font=('Roboto', 15), text_color='#FFFFFF', fg_color='#173561')
        self.cliente.place(x=80, y=120)

        self.caixa_cliente = customtkinter.CTkEntry(self.janela2, placeholder_text='Digite o nome', font=('Roboto', 15), text_color='#FFFFFF', fg_color='#173561')
        self.caixa_cliente.place(x=80, y=150)

        self.cpf = customtkinter.CTkLabel(self.janela2, text='CPF', font=('Roboto', 15), text_color='#FFFFFF', fg_color='#173561')
        self.cpf.place(x=80, y=190)

        self.caixa_cpf = customtkinter.CTkEntry(self.janela2, placeholder_text='Digite o CPF', font=('Roboto', 15), text_color='#FFFFFF', fg_color='#173561')
        self.caixa_cpf.place(x=80, y=220)

        self.endereco = customtkinter.CTkLabel(self.janela2, text='Endereço', font=('Roboto', 15), text_color='#FFFFFF', fg_color='#173561')
        self.endereco.place(x=240, y=120)

        self.caixa_endereco = customtkinter.CTkEntry(self.janela2, placeholder_text='Digite o endereço', font=('Roboto', 15), text_color='#FFFFFF', fg_color='#173561')
        self.caixa_endereco.place(x=240, y=150)

        self.contato = customtkinter.CTkLabel(self.janela2, text='Contato', font=('Roboto', 15), text_color='#FFFFFF', fg_color='#173561')
        self.contato.place(x=240, y=190)

        self.caixa_contato = customtkinter.CTkEntry(self.janela2, placeholder_text='Digite o contato', font=('Roboto', 15), text_color='#FFFFFF', fg_color='#173561')
        self.caixa_contato.place(x=240, y=220)

        
        self.label_criado = customtkinter.CTkLabel(self.janela1, text='Desenvolvido por Micaelle Silva ©', font=('Roboto', 15), text_color='#FFFFFF', fg_color='#173561')
        self.label_criado.place(x=120, y=570)

#-----------------------------------BOTÕES---------------------------------
        self.botao_cadastrar = customtkinter.CTkButton(self.janela2, text='Cadastrar', font=('Roboto', 12, 'bold'), text_color='#173561', fg_color='FFFFFF',   )


    def voltar_tela_principal(self):
        self.janela2.destroy()  # Destroi a janela de login admin
        objeto.janela.deiconify()  # Exibe novamente a janela principal   

#---------------------------------------FUNÇÕES-------------------------------------------
#ARRUMAR BANCO DEPOIS
    def cadastrar(self):
        self.capturar_cliente = self.caixa_cliente.get()
        self.capturar_cpf = self.caixa_cpf.get()
        self.capturar_endereco = self.caixa_endereco.get()
        self.capturar_contato = self.caixa_endereco.get()

        self.conecta_banco()
        self.sql.execute('''INSERT INTO pacientes (nome, cpf, endereco, contato) values (?,?,?,?)''',
                        (self.capturar_cliente, self.capturar_cpf, self.capturar_endereco, self.capturar_contato))
        


        try:
            if self.capturar_cliente == '' or self.capturar_cpf == '' or self.capturar_endereco == '' or self.capturar_contato == '':
                messagebox.showerror('Sistema de cadastro', 'Preencha todos os campos!')
            else:
                self.conexao.commit()
                messagebox.showinfo('Cadastro', f'Parabéns! Dados Salvos!')
                self.desconecta_banco()

                
        except:
            messagebox.showerror('Cadastro', 'Erro no processamento do seu cadastro.')
            self.desconecta_banco()
        self.desconecta_banco()





windows = tk.Tk()
objeto = ModeloTelaPrincipal(windows)
windows.mainloop()
