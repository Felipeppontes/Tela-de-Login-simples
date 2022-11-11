from tkinter import *
from tkinter import Tk, messagebox, ttk

#Paleta de cores----------------------------------------------------

co0 = "#000100" #ppreto
co1 = "#ffffff" #branco
co2 = "#295c2b" #verde exercito
co3 = "#2c5e5e" #Azul marinho
co4 = "#38576b" #Letras

#Criando janela ---------------------------------------------------

janela = Tk()
janela.title('LOGIN')
janela.geometry('310x300')
janela.configure(background=co1)
janela.resizable(width=FALSE, height=FALSE)

#Dividindo a janela -----------------------------------------------

frame_cima = Frame(janela, width=310, height=50, bg=co1,relief='flat')
frame_cima.grid(row=0, column=0, padx=0,pady=1, sticky=NSEW)

frame_baixo = Frame(janela, width=310, height=250, bg=co1,relief='flat')
frame_baixo.grid(row=1, column=0, padx=0,pady=1, sticky=NSEW)

#Configurando frame de cima--------------------------------------------

l_nome = Label(frame_cima,text='LOGIN',anchor=NE, font=('Ivy 25'), bg=co1, fg= co4)
l_nome.place(x=5,y=5)

l_linha = Label(frame_cima,text='', width=275, anchor=NW, font=('Ivy 1'), bg=co4, fg= co4)
l_linha.place(x=10,y=45)

#criando Acesso restrito -------------------------------------------------------------

#função para verificar senha
acesso = ['Felipe', '123']

def verifica_senha():
    nome = e_nome.get()
    senha = e_pass.get() 
    if nome == 'admin' and senha == 'admin':
        messagebox.showinfo('Login','seja bem-vindo ADMIN!')
    elif acesso [0] == nome and acesso [1] == senha:
        messagebox.showinfo('Login','Seja bem-vindo de volta ' +acesso[0])
        
        #apagar oque tiver no frame baixo e cima
        for widget in frame_baixo.winfo_children():
            widget.destroy()
            
        for widget in frame_cima.winfo_children():
            widget.destroy()
            nova_janela()
    else: 
        messagebox.showwarning('Erro', 'Verifique o nome e a senha')
        
#função após verificação ----------------------------------------------------------------------------

def nova_janela():
    # Configuração do frame de cima
    l_nome = Label(frame_cima,text='Usuário: ' +acesso[0],anchor=NE, font=('Ivy 20'), bg=co1, fg= co4)
    l_nome.place(x=5,y=5)
    
    l_linha = Label(frame_cima, text='', width=275, anchor=NW, font=('Ivy 1'), bg=co4, fg= co4)
    l_linha.place(x=10,y=45)
    
    l_nome = Label(frame_baixo,text='Seja bem-Vindo, ' +acesso[0],anchor=NE, font=('Ivy 20'), bg=co1, fg= co4)
    l_nome.place(x=5,y=105)

#Configurando frame de Baixo--------------------------------------------

l_nome = Label(frame_baixo,text='Nome *',anchor=NW, font=('Ivy 10'), bg=co1, fg= co0)
l_nome.place(x=10,y=20)

e_nome = Entry(frame_baixo, width=25, justify='left',font=("", 15), highlightthickness=1, relief='solid', fg=co4)
e_nome.place(x=14,y=50)

l_pass = Label(frame_baixo,text='Senha *',anchor=NW, font=('Ivy 10'), bg=co1, fg= co0)
l_pass.place(x=10,y=95)

e_pass = Entry(frame_baixo, width=25, justify='left', show='*' ,font=("", 15), highlightthickness=1, relief='solid',fg=co4)
e_pass.place(x=14,y=130)

# Criando botão
b_confirmar = Button(frame_baixo, command=verifica_senha, text='ENTRAR', width=39, height=2, font=('Ivy 8 bold'), bg=co4, fg= co0, relief= RAISED, overrelief=RIDGE)
b_confirmar.place(x=15,y=180)

janela.mainloop()