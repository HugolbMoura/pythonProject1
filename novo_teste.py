import tkinter as tk
from tkinter import messagebox

class Cadastro:
    def __init__(self, master):
        self.master = master
        self.master.title("Cadastro")
        
        self.label = tk.Label(self.master, text="Selecione o tipo de cadastro:")
        self.label.pack(pady=10)
        
        self.cliente_button = tk.Button(self.master, text="Cliente", command=self.cadastro_cliente)
        self.cliente_button.pack(pady=10)
        
        self.fornecedor_button = tk.Button(self.master, text="Fornecedor", command=self.cadastro_fornecedor)
        self.fornecedor_button.pack(pady=10)
        
    def cadastro_cliente(self):
        self.master.destroy()
        root = tk.Tk()
        app = App(root, "Cliente")
        root.mainloop()
        
    def cadastro_fornecedor(self):
        self.master.destroy()
        root = tk.Tk()
        app = App(root, "Fornecedor")
        root.mainloop()

class App:
    def __init__(self, master, tipo_cadastro):
        self.master = master
        self.master.title(tipo_cadastro)
        self.master.resizable(False, False)
        
        # Obtém a largura e a altura da tela
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()

        # Define a largura e a altura da janela para serem 50% da largura e altura da tela
        window_width = screen_width // 2
        window_height = screen_height // 2

        # Define a posição inicial da janela para que ela apareça no centro da tela
        start_x = screen_width // 4
        start_y = screen_height // 4

        # Configura a geometria da janela
        self.master.geometry(f'{window_width}x{window_height}+{start_x}+{start_y}')

        self.carteira_corretora = CarteiraCorretora()  # Instância da classe CarteiraCorretora

        self.create_widgets(tipo_cadastro)  # Método para criar os widgets da interface
        
         # Criação dos botões de editar e apagar
        self.editar_button = tk.Button(self.master, text="Editar", command=self.editar)
        self.apagar_button = tk.Button(self.master, text="Apagar", command=self.apagar)

        # Inicialmente, os botões são invisíveis
        self.editar_button.pack_forget()
        self.apagar_button.pack_forget()

        # Criação da lista de clientes
        self.clientes_listbox = tk.Listbox(self.master)
        self.clientes_listbox.bind('<<ListboxSelect>>', self.on_select_cliente)
        self.clientes_listbox.grid(row=1, column=1, padx=20, pady=20)
        # ... código para preencher a lista de clientes ...

    def on_select_cliente(self, event): # Quando um cliente é selecionado, os botões se tornam visíveis
        self.editar_button.grid(row=3, column=0, padx=10, pady=10)
        self.apagar_button.grid(row=4, column=0, padx=10, pady=10)

    def editar(self):  
        pass

    def apagar(self): 
        pass  

    def create_widgets(self, tipo_cadastro): # Configuração da interface para clientes ou fornecedores
        self.cliente_label = tk.Label(self.master, text=tipo_cadastro)
        self.cliente_label.grid(row=0, column=0, padx=20, pady=20)

root = tk.Tk()
cadastro = Cadastro(root)
root.mainloop()