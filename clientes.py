from modulos import *
from valida import Validadores
from reports import Relatorios
from funcionalidades import Funcs

root = tix.Tk()

class App(Funcs, Relatorios, Validadores):
    def __init__(self):
        self.root = root
        self.images_base64()
        self.validaEntradas()
        self.tela()
        self.frames_da_tela()
        self.widgets_frame1()
        self.lista_frame2()
        self.monta_tabelas()
        self.select_lista()
        self.Menus()
        root.mainloop()
    def tela(self):
        self.root.title("Cadastro de Clientes")
        self.root.configure(background = "#1C1C1C")
        self.root.geometry("700x500")
        self.root.state("zoomed")
        self.root.resizable(True, True)
        self.root.minsize(width = 700, height = 500)
        self.root.iconbitmap("icocli.ico")
    def frames_da_tela(self):
        self.frame_1 = Frame(
            self.root,
            bd = 4, # Borda
            bg = "#363636", # Cor de fundo (background color)
            highlightbackground = "#836FFF",
            highlightthickness = 1)
        self.frame_1.place(
            relx = 0.01,
            rely = 0.02,
            relwidth = 0.98,
            relheight = 0.46)
        self.frame_2 = Frame(
            self.root,
            bd = 4,
            bg = "#363636",
            highlightbackground = "#836FFF",
            highlightthickness = 1)
        self.frame_2.place(
            relx=0.01,
            rely=0.5,
            relwidth=0.98,
            relheight=0.46)
    def widgets_frame1(self):
        # Abas
        self.abas = ttk.Notebook(self.frame_1)
        self.aba1 = Frame(self.abas)
        self.aba2 = Frame(self.abas)

        self.aba1.configure(background="#363636")
        self.aba2.configure(background="#363636")

        self.abas.add(self.aba1, text='Clientes')
        self.abas.add(self.aba2, text='Produtos')

        self.abas.place(relx=0, rely=0, relwidth=1, relheight=1)

        # Botão Limpar
        self.bt_limpar = Button(self.aba1, text = "Limpar", bd = 2, bg = "#808080", fg = "#363636",
            activebackground = '#A9A9A9', activeforeground = '#363636',
            font = ("verdana", "10"), command = self.limpa_tela)
        self.bt_limpar.place(relx = 0.2, rely = 0.1, relwidth = 0.1, relheight = 0.1)

        # Botão Buscar
        self.bt_buscar = Button(self.aba1, text="Buscar", bd = 2, bg = "#808080", fg = "#363636",
            activebackground='#A9A9A9', activeforeground='#363636',
            font = ("verdana", "10"), command = self.busca_cliente)
        self.bt_buscar.place(relx=0.3, rely=0.1, relwidth=0.1, relheight=0.1)

        texto_balao_buscar = 'Digite no campo nome o cliente que deseja pesquisar'
        self.balao_buscar = tix.Balloon(self.aba1)
        self.balao_buscar.bind_widget(self.bt_buscar, balloonmsg = texto_balao_buscar)

        # Botão Novo
        self.bt_novo = Button(
            self.aba1,
            text="Novo",
            bd = 2,
            bg = "#808080",
            fg = "#363636",
            activebackground='#A9A9A9',
            activeforeground='#363636',
            font = ("verdana", "10"),
            command = self.insere_cliente
        )
        self.bt_novo.place(relx=0.6, rely=0.1, relwidth=0.1, relheight=0.1)

        # Botão Alterar
        self.bt_alterar = Button(self.aba1, text="Alterar", bd = 2, bg = "#808080", fg = "#363636",
            activebackground='#A9A9A9', activeforeground='#363636',
            font = ("verdana", "10"), command = self.altera_cliente)
        self.bt_alterar.place(relx=0.7, rely=0.1, relwidth=0.1, relheight=0.1)

        # Botão Apagar
        self.bt_apagar = Button(self.aba1, text="Apagar", bd = 2, bg = "#808080", fg = "#363636",
            activebackground='#A9A9A9', activeforeground='#363636',
            font = ("verdana", "10"), command = self.deleta_cliente)
        self.bt_apagar.place(relx=0.8, rely=0.1, relwidth=0.1, relheight=0.1)

        # Criação da Label e Entrada do Código
        self.lb_codigo = Label(self.aba1, text = "Código", bg="#363636", fg = "#808080", font = ("trebouchet", "10"))
        self.lb_codigo.place(relx = 0.008, rely = 0.02)

        self.codigo_entry = Entry(self.aba1, validate="key", validatecommand=self.vcmd2)
        self.codigo_entry.place(relx = 0.008, rely = 0.11, relwidth = 0.07, relheight = 0.08)

        # Criação da Label e Entrada do Nome
        self.lb_nome = Label(self.aba1, text="Nome", bg="#363636", fg = "#808080", font = ("Trebouchet", 10))
        self.lb_nome.place(relx=0.008, rely=0.19)

        self.nome_entry = Entry(self.aba1)
        self.nome_entry.place(relx=0.008, rely=0.27, relwidth=0.46, relheight=0.08)

        # Criação da Label e Entrada do Telefone
        self.lb_telefone = Label(self.aba1, text="Telefone", bg="#363636", fg = "#808080", font = ("Trebouchet", 10))
        self.lb_telefone.place(relx=0.008, rely=0.35)

        self.telefone_entry = Entry(self.aba1)
        self.telefone_entry.place(relx=0.008, rely=0.43, relwidth=0.20, relheight=0.08)

        # Criação da Label e Entrada do Cidade
        self.lb_cidade = Label(self.aba1, text="Cidade", bg="#363636", fg = "#808080", font = ("Trebouchet", 10))
        self.lb_cidade.place(relx=0.25, rely=0.35)

        self.cidade_entry = Entry(self.aba1)
        self.cidade_entry.place(relx=0.25, rely=0.43, relwidth=0.22, relheight=0.08)

        # Menu Dropdown
        self.Tipvar = StringVar()
        self.TipV = ("Solteiro(a)", "Casado(a)", "Divorciado(a)", "Viúvo(a)")
        self.Tipvar.set("Estado civil")

        self.popupMenu = OptionMenu(self.aba2, self.Tipvar, *self.TipV)
        self.popupMenu.place(relx=0.1, rely=0.1, relwidth=0.2, relheight=0.15)
        self.estado_civil = self.Tipvar.get()
    def lista_frame2(self):
        self.listaCli = ttk.Treeview(self.frame_2, height = 3, column = ("col1", "col2", "col3", "col4"))
        self.listaCli.place(relx = 0.01, rely = 0.05, relwidth = 0.98, relheight = 0.9)
        self.listaCli.heading("#0", text = "")
        self.listaCli.heading("#1", text = "Código")
        self.listaCli.heading("#2", text = "Nome")
        self.listaCli.heading("#3", text = "Telefone")
        self.listaCli.heading("#4", text = "Cidade")

        self.listaCli.column('#0', stretch=YES, minwidth=0, width=0, anchor="center")
        self.listaCli.column('#1', stretch=YES, minwidth=40, width=50, anchor="center")
        self.listaCli.column('#2', stretch=YES, minwidth=250, width=800, anchor="nw")
        self.listaCli.column('#3', stretch=YES, minwidth=100, width=190, anchor="nw")
        self.listaCli.column('#4', stretch=YES, minwidth=120, width=250, anchor="nw")

        self.barra_de_rolagem = Scrollbar(self.frame_2, orient = "vertical")
        self.listaCli.configure(yscroll = self.barra_de_rolagem.set)
        self.barra_de_rolagem.place(relx=0.98, rely = 0.052, relheight = 0.8962)

        self.listaCli.bind("<Double-1>", self.onDoubleClick)
    def Menus(self):
        menubar = Menu(self.root)
        self.root.config(menu = menubar)
        filemenu = Menu(menubar, tearoff=0)
        filemenu2 = Menu(menubar, tearoff=0)

        def quit():
            self.root.destroy()

        menubar.add_cascade(label = "Opções", menu = filemenu)
        menubar.add_cascade(label = "Relatórios", menu = filemenu2)

        filemenu.add_command(label="Limpa Cliente", command=self.limpa_tela)
        filemenu.add_command(label = "Sair", command = quit)

        filemenu2.add_command(label="Ficha do Cliente", command=self.geraRelatCliente)
    def validaEntradas(self):
        self.vcmd2 = (self.root.register(self.validate_entry2), "%P")

# Programa Principal
App()