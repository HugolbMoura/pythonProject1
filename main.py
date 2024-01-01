import tkinter as tk # Importação do módulo tkinter para criação da interface gráfica (GUI)
from tkinter import simpledialog # Importação do módulo simpledialog para criação de diálogos de entrada de dados


# Definição da classe base Pessoa
class Pessoa:
    def __init__(self, nome, idade, endereco): # Método construtor da classe Pessoa
        self.nome = nome # Atributo nome da classe Pessoa
        self.idade = idade # Atributo idade da classe Pessoa
        self.endereco = endereco # Atributo endereço da classe Pessoa


# Definição da classe Cliente, que herda de Pessoa
class Cliente(Pessoa):
    def __init__(self, nome, idade, endereco, saldo_inicial):
        super().__init__(nome, idade, endereco) # Chamada ao método construtor da classe base Pessoa (superclasse)
        self.saldo = saldo_inicial


# Definição da classe Fornecedor, que herda de Pessoa
class Fornecedor(Pessoa):
    def __init__(self, nome, idade, endereco, dados_fornecidos):
        super().__init__(nome, idade, endereco)
        self.dados_fornecidos = dados_fornecidos # Atributo dados_fornecidos da classe Fornecedor


# Definição da classe CarteiraCorretora
class CarteiraCorretora:
    def __init__(self):
        self.clientes = []  # Lista para armazenar clientes
        self.fornecedores = []  # Lista para armazenar fornecedores

    def cadastrar_cliente(self, cliente):
        self.clientes.append(cliente)  # Adiciona um cliente à lista

    def excluir_cliente(self, cliente):
        self.clientes.remove(cliente)  # Remove um cliente da lista

    def editar_cliente(self, cliente_antigo, cliente_novo):
        index = self.clientes.index(cliente_antigo)  # Encontra o índice do cliente antigo na lista
        self.clientes[index] = cliente_novo  # Substitui o cliente antigo pelo novo cliente na lista

    def cadastrar_fornecedor(self, fornecedor):
        self.fornecedores.append(fornecedor)  # Adiciona um fornecedor à lista

    def excluir_fornecedor(self, fornecedor):
        self.fornecedores.remove(fornecedor)  # Remove um fornecedor da lista

    def editar_fornecedor(self, fornecedor_antigo, fornecedor_novo):
        index = self.fornecedores.index(fornecedor_antigo)  # Encontra o índice do fornecedor antigo na lista
        self.fornecedores[index] = fornecedor_novo  # Substitui o fornecedor antigo pelo novo fornecedor na lista

    def listar_clientes(self):
        return [cliente.nome for cliente in self.clientes]  # Retorna uma lista de nomes de clientes

    def listar_fornecedores(self):
        return [fornecedor.nome for fornecedor in self.fornecedores]  # Retorna uma lista de nomes de fornecedores


# Definição da classe principal App
class App: # Classe principal da aplicação
    def __init__(self, master): # Método construtor da classe App
        self.cliente_label = None # Label para exibir o texto "Clientes"
        self.master = master # Atributo master da classe App
        self.master.title("Carteira/Corretora") # Título da janela principal
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

        self.create_widgets()  # Método para criar os widgets da interface
        
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

    def create_widgets(self): # Configuração da interface para clientes
        self.cliente_label = tk.Label(self.master, text="Clientes")
        self.cliente_label.grid(row=0, column=0, padx=20, pady=20)

        self.cliente_listbox = tk.Listbox(self.master, selectmode=tk.SINGLE)
        self.cliente_listbox.grid(row=1, column=0, padx=20, pady=20)

        self.cliente_listbox_update()

        self.adicionar_cliente_button = tk.Button(self.master, text="Adicionar Cliente", command=self.adicionar_cliente)
        self.adicionar_cliente_button.grid(row=2, column=0, padx=10, pady=10)

        # Configuração da interface para fornecedores
        self.fornecedor_label = tk.Label(self.master, text="Fornecedores")
        self.fornecedor_label.grid(row=0, column=1, padx=30, pady=30)

        self.fornecedor_listbox = tk.Listbox(self.master, selectmode=tk.SINGLE)
        self.fornecedor_listbox.grid(row=1, column=1, padx=10, pady=10)

        self.fornecedor_listbox_update()

        self.adicionar_fornecedor_button = tk.Button(self.master, text="Adicionar Fornecedor",
                                                     command=self.adicionar_fornecedor)
        self.adicionar_fornecedor_button.grid(row=2, column=1, padx=10, pady=10)

    def cliente_listbox_update(self):
        self.cliente_listbox.delete(0, tk.END)
        for cliente in self.carteira_corretora.listar_clientes():
            self.cliente_listbox.insert(tk.END, cliente)

    def fornecedor_listbox_update(self):
        self.fornecedor_listbox.delete(0, tk.END)
        for fornecedor in self.carteira_corretora.listar_fornecedores():
            self.fornecedor_listbox.insert(tk.END, fornecedor)

    def adicionar_cliente(self):
        # Cria uma nova janela
        self.nova_janela = tk.Toplevel(self.master)

        # Obtém a altura e a largura da janela principal
        largura_janela = self.master.winfo_width()
        altura_janela = self.master.winfo_height()

        # Define a altura e a largura da nova janela para 50% da altura e largura da janela principal
        largura_nova_janela = int(largura_janela * 0.5)
        altura_nova_janela = int(altura_janela * 0.5)

        # Define a posição da nova janela para o centro da janela principal
        x_pos = int(largura_janela * 0.5 - largura_nova_janela * 0.5)
        y_pos = int(altura_janela * 0.5 - altura_nova_janela * 0.5)

        # Configura a altura, largura e posição da nova janela
        self.nova_janela.geometry(f"{largura_nova_janela}x{altura_nova_janela}+{x_pos}+{y_pos}")

        # Cria widgets de entrada para o formulário
        self.nome_entry = tk.Entry(self.nova_janela)
        self.nome_entry.grid(row=0, column=1)
        self.nome_label = tk.Label(self.nova_janela, text="Nome")
        self.nome_label.grid(row=0, column=0)

        self.idade_entry = tk.Entry(self.nova_janela)
        self.idade_entry.grid(row=1, column=1)
        self.idade_label = tk.Label(self.nova_janela, text="Idade")
        self.idade_label.grid(row=1, column=0)
        
        self.endereco_entry = tk.Entry(self.nova_janela)
        self.endereco_entry.grid(row=2, column=1)
        self.endereco_label = tk.Label(self.nova_janela, text="Endereço")
        self.endereco_label.grid(row=2, column=0)
        
        self.saldo_entry = tk.Entry(self.nova_janela)
        self.saldo_entry.grid(row=3, column=1)
        self.saldo_label = tk.Label(self.nova_janela, text="Saldo Inicial")
        self.saldo_label.grid(row=3, column=0)
        
        #Adicionar botáo para enviar os dados
        self.enviar_button = tk.Button(self.nova_janela, text="Enviar", command=self.verificar_campos)
        self.enviar_button.grid(row=4, column=0, padx=10, pady=10)
        
        #Adicionar botáo para cancelar
        self.cancelar_button = tk.Button(self.nova_janela, text="Cancelar", command=self.nova_janela.destroy)
        self.cancelar_button.grid(row=4, column=1, padx=10, pady=10)
                
        def verificar_campos(self):
            # Verifica se todos os campos estão preenchidos
            if self.nome_entry.get() == "":
                messagebox.showerror("Erro", "O campo Nome é obrigatório.")
                return
        # ... Verifique mais campos ...

        # Se todos os campos estiverem preenchidos, prossiga com a adição do cliente
            self.adicionar_cliente_db()

    def adicionar_fornecedor(self):
        # Diálogo para obter dados do fornecedor
        nome = simpledialog.askstring("Input", "Nome do Fornecedor:")
        idade = simpledialog.askinteger("Input", "Idade do Fornecedor:")
        endereco = simpledialog.askstring("Input", "Endereço do Fornecedor:")
        dados_fornecidos = simpledialog.askstring("Input", "Dados Fornecidos pelo Fornecedor:")

        # Criação de um novo fornecedor e cadastramento na carteira
        novo_fornecedor = Fornecedor(nome, idade, endereco, dados_fornecidos)
        self.carteira_corretora.cadastrar_fornecedor(novo_fornecedor)
        self.fornecedor_listbox_update()


# Verificação se o script está sendo executado diretamente
if __name__ == "__main__":
    root = tk.Tk()  # Criação da janela principal
    app = App(root)  # Instância da classe App
    root.mainloop()  # Loop principal da interface gráfica
