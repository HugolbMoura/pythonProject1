import tkinter as tk # Importação do módulo tkinter para criação da interface gráfica (GUI)
from tkinter import simpledialog, \
    messagebox  # Importação do módulo simpledialog para criação de diálogos de entrada de dados


# Definição da classe base Pessoa
class Pessoa:
    def __init__(self, nome, idade, endereco): # Método construtor da classe Pessoa
        self.nome = nome # Atributo nome da classe Pessoa
        self.idade = idade # Atributo idade da classe Pessoa
        self.endereco = endereco # Atributo endereço da classe Pessoa
        
    def __str__(self): # Método para retornar uma string com os dados da pessoa
        return f"Nome: {self.nome}\nIdade: {self.idade}\nEndereço: {self.endereco}"


# Definição da classe Cliente, que herda de Pessoa
class Cliente(Pessoa):
    def __init__(self, nome, idade, endereco, saldo_inicial):
        super().__init__(nome, idade, endereco) # Chamada ao método construtor da classe base Pessoa (superclasse)
        self.saldo = saldo_inicial # Atributo saldo da classe Cliente


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
        self.clientes.append(cliente)# Adiciona um cliente à lista

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

#Cria uma classe para o tamanho padrão das janelas
class TamanhoPadrao:
    def __init__(self):
        self.largura = 0
        self.altura = 0
        self.x_pos = 0
        self.y_pos = 0
        
    def set_largura(self, largura):
        self.largura = largura
        
    def set_altura(self, altura):
        self.altura = altura
        
    def set_x_pos(self, x_pos):
        self.x_pos = x_pos
        
    def set_y_pos(self, y_pos):
        self.y_pos = y_pos
        
    def get_largura(self):
        return self.largura
    
    def get_altura(self):
        return self.altura
    
    def get_x_pos(self):
        return self.x_pos
    
    def get_y_pos(self):
        return self.y_pos
    
    def get_tamanho_padrao(self):
        return f"{self.largura}x{self.altura}+{self.x_pos}+{self.y_pos}"
    
    def set_tamanho_padrao(self, largura, altura, x_pos, y_pos):
        self.set_largura(largura)
        self.set_altura(altura)
        self.set_x_pos(x_pos)
        self.set_y_pos(y_pos)
        
# Definição da classe principal App
class App: # Classe principal da aplicação
    def __init__(self, master): # Método construtor da classe App
        self.cliente_label = None # Label para exibir o texto "Clientes"
        self.master = master # Atributo master da classe App
        self.master.title("Carteira/Corretora") # Título da janela principal
        self.master.resizable(False, False)
        
        # Criação de um objeto da classe TamanhoPadrao
        self.tamanho_padrao = TamanhoPadrao()
        self.tamanho_padrao.set_tamanho_padrao(700, 500, 500, 500)
        
        # Configuração da geometria da janela principal
        self.master.geometry(self.tamanho_padrao.get_tamanho_padrao())
        
        self.carteira_corretora = CarteiraCorretora()  # Instância da classe CarteiraCorretora

        self.create_widgets()  # Método para criar os widgets da interface
        
         # Criação dos botões de editar e apagar
        self.editar_button = tk.Button(self.master, text="Editar", command=self.editar)
        self.apagar_button = tk.Button(self.master, text="Apagar", command=self.apagar)
        
        # Configuração dos eventos de seleção de cliente e fornecedor
        self.cliente_listbox.bind("<<ListboxSelect>>", self.on_select_cliente)
        self.fornecedor_listbox.bind("<<ListboxSelect>>", self.on_select_fornecedor)
        
        # Inicialmente, os botões são invisíveis
        self.editar_button.pack_forget()
        self.apagar_button.pack_forget()        
    # Quando um cliente é selecionado, os botões se tornam visíveis
    def on_select_cliente(self, event): 
        self.editar_button.grid(row=4, column=0, padx=10, pady=10)
        self.apagar_button.grid(row=4, column=1, padx=10, pady=10)
    # Quando um fornecedor é selecionado, os botões se tornam visíveis
    def on_select_fornecedor(self, event): 
        self.editar_button.grid(row=4, column=0, padx=10, pady=10)
        self.apagar_button.grid(row=4, column=1, padx=10, pady=10)

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
        
        # Criação de uma nova janela
    def adicionar_cliente(self):
        self.nova_janela_cliente = tk.Toplevel(self.master)
        
        # Obtém a altura e a largura da janela principal
        largura_janela = self.master.winfo_width()
        altura_janela = self.master.winfo_height()
        
        # Define a altura e a largura da nova janela para 50% da altura e largura da janela principal
        largura_nova_janela = int(largura_janela * 0.7)
        altura_nova_janela = int(altura_janela * 0.7)
        
        # Define a posição da nova janela para o centro da janela principal
        x_pos = int(largura_janela * 0.5 - largura_nova_janela * 0.5)
        y_pos = int(altura_janela * 0.5 - altura_nova_janela * 0.5)
        
        # Configura a altura, largura e posição da nova janela
        self.nova_janela_cliente.geometry(f"{largura_nova_janela}x{altura_nova_janela}+{x_pos}+{y_pos}")
        
        # Label para o título da janela
        self.titulo_label = tk.Label(self.nova_janela_cliente, text="Cliente")
        self.titulo_label.grid(row=0, column=1, padx=20, pady=20)
        
        # Cria widgets de entrada para o formulário do cliente
        self.nome_cliente_entry = tk.Entry(self.nova_janela_cliente)
        self.nome_cliente_entry.grid(row=1, column=1)
        self.nome_cliente_label = tk.Label(self.nova_janela_cliente, text="Nome")
        self.nome_cliente_label.grid(row=1, column=0)
        
        self.idade_cliente_entry = tk.Entry(self.nova_janela_cliente)
        self.idade_cliente_entry.grid(row=2, column=1)
        self.idade_cliente_label = tk.Label(self.nova_janela_cliente, text="Idade")
        self.idade_cliente_label.grid(row=2, column=0)
        
        self.endereco_cliente_entry = tk.Entry(self.nova_janela_cliente)
        self.endereco_cliente_entry.grid(row=3, column=1)
        self.endereco_cliente_label = tk.Label(self.nova_janela_cliente, text="Endereço")
        self.endereco_cliente_label.grid(row=3, column=0)
        
        self.saldo_cliente_entry = tk.Entry(self.nova_janela_cliente)
        self.saldo_cliente_entry.grid(row=4, column=1)
        self.saldo_cliente_label = tk.Label(self.nova_janela_cliente, text="Saldo Inicial")
        self.saldo_cliente_label.grid(row=4, column=0)
        
        # Adicionar botão para enviar os dados
        self.enviar_button = tk.Button(self.nova_janela_cliente, text="Enviar", command=self.verificar_campos_cliente)
        self.enviar_button.grid(row=5, column=1, padx=10, pady=10)
        
        # Adicionar botão para cancelar
        self.cancelar_button = tk.Button(self.nova_janela_cliente, text="Cancelar", command=self.nova_janela_cliente.destroy)
        self.cancelar_button.grid(row=5, column=2, padx=10, pady=10)
        
        # Adicione mais campos conforme necessário
        
    def verificar_campos_cliente(self):
        # Verifica se todos os campos estão preenchidos
        if self.nome_cliente_entry.get() == "":
            messagebox.showerror("Erro", "O campo Nome é obrigatório.")
            return
        # ... Verifique mais campos ...
        
        # Se todos os campos estiverem preenchidos, prossiga com a adição do cliente
        self.adicionar_cliente_db()
        #depois de atualizar a lista de clientes, mostra uma mensagem de sucesso
        messagebox.showinfo("Sucesso", "Cliente adicionado com sucesso!")
        #depois de adicionar o cliente, pergunta se quer adicionar outro
        if messagebox.askyesno("Novo Cliente", "Deseja adicionar outro cliente?"):
            self.nova_janela_cliente.destroy()
            self.adicionar_cliente()
            #se não quiser adicionar outro cliente, fecha a janela
        else:
            self.nova_janela_cliente.destroy()   
                
        
    def adicionar_fornecedor(self):
        # Cria uma nova janela
        self.nova_janela_fornecedor = tk.Toplevel(self.master)

        # Obtém a altura e a largura da janela principal
        largura_janela = self.master.winfo_width()
        altura_janela = self.master.winfo_height()

        # Define a altura e a largura da nova janela para 50% da altura e largura da janela principal
        largura_nova_janela = int(largura_janela * 0.7)
        altura_nova_janela = int(altura_janela * 0.7)

        # Define a posição da nova janela para o centro da janela principal
        x_pos = int(largura_janela * 0.5 - largura_nova_janela * 0.5)
        y_pos = int(altura_janela * 0.5 - altura_nova_janela * 0.5)

        # Configura a altura, largura e posição da nova janela
        self.nova_janela_fornecedor.geometry(f"{largura_nova_janela}x{altura_nova_janela}+{x_pos}+{y_pos}")
        
        #Label para o título da janela
        self.titulo_label = tk.Label(self.nova_janela_fornecedor, text="Fornecedor")
        self.titulo_label.grid(row=0, column=1, padx=20, pady=20)

        # Cria widgets de entrada para o formulário do fornecedor
        self.nome_fornecedor_entry = tk.Entry(self.nova_janela_fornecedor)
        self.nome_fornecedor_entry.grid(row=1, column=1)
        self.nome_fornecedor_label = tk.Label(self.nova_janela_fornecedor, text="Nome")
        self.nome_fornecedor_label.grid(row=1, column=0)
        
        self.idade_fornecedor_entry = tk.Entry(self.nova_janela_fornecedor) 
        self.idade_fornecedor_entry.grid(row=2, column=1)
        self.idade_fornecedor_label = tk.Label(self.nova_janela_fornecedor, text="Idade")
        self.idade_fornecedor_label.grid(row=2, column=0)
        
        self.endereco_fornecedor_entry = tk.Entry(self.nova_janela_fornecedor)
        self.endereco_fornecedor_entry.grid(row=3, column=1)
        self.endereco_fornecedor_label = tk.Label(self.nova_janela_fornecedor, text="Endereço")
        self.endereco_fornecedor_label.grid(row=3, column=0)
        
        self.dados_fornecidos_entry = tk.Entry(self.nova_janela_fornecedor)
        self.dados_fornecidos_entry.grid(row=4, column=1)
        self.dados_fornecidos_label = tk.Label(self.nova_janela_fornecedor, text="Dados")
        self.dados_fornecidos_label.grid(row=4, column=0)
        
        #Adicionar botáo para enviar os dados
        self.enviar_button = tk.Button(self.nova_janela_fornecedor, text="Enviar", command=self.verificar_campos_fornecedor)
        self.enviar_button.grid(row=5, column=1, padx=10, pady=10)
        
        #Adicionar botáo para cancelar
        self.cancelar_button = tk.Button(self.nova_janela_fornecedor, text="Cancelar", command=self.nova_janela_fornecedor.destroy)
        self.cancelar_button.grid(row=5, column=2, padx=10, pady=10)

        # Adicione mais campos conforme necessário

    def verificar_campos_fornecedor(self):
        # Verifica se todos os campos estão preenchidos
        if self.nome_fornecedor_entry.get() == "":
            messagebox.showerror("Erro", "O campo Nome é obrigatório.")
            return
        # ... Verifique mais campos ...
        
        # Se todos os campos estiverem preenchidos, prossiga com a adição do fornecedor
        self.adicionar_fornecedor_db()
        #depois de atualizar a lista de fornecedores, mostra uma mensagem de sucesso
        messagebox.showinfo("Sucesso", "Fornecedor adicionado com sucesso!")
        #depois de adicionar o fornecedor, pergunta se quer adicionar outro
        if messagebox.askyesno("Novo Fornecedor", "Deseja adicionar outro fornecedor?"):
            self.nova_janela_fornecedor.destroy()
            self.adicionar_fornecedor()
            #se não quiser adicionar outro fornecedor, fecha a janela
        else:
            self.nova_janela_fornecedor.destroy()            
        
    def adicionar_cliente_db(self):
        # Obtém os valores dos campos de entrada
        nome = self.nome_cliente_entry.get()
        idade = self.idade_cliente_entry.get()
        endereco = self.endereco_cliente_entry.get()
        saldo_inicial = self.saldo_cliente_entry.get()
        
        # Criação de um novo cliente e cadastramento na carteira
        novo_cliente = Cliente(nome, idade, endereco, saldo_inicial)
        self.carteira_corretora.cadastrar_cliente(novo_cliente)
        self.cliente_listbox_update()
        
    def adicionar_fornecedor_db(self):
        # Obtém os valores dos campos de entrada
        nome = self.nome_fornecedor_entry.get()
        idade = self.idade_fornecedor_entry.get()
        endereco = self.endereco_fornecedor_entry.get()
        dados_fornecidos = self.dados_fornecidos_entry.get()
        
        # Criação de um novo fornecedor e cadastramento na carteira
        novo_fornecedor = Fornecedor(nome, idade, endereco, dados_fornecidos)
        self.carteira_corretora.cadastrar_fornecedor(novo_fornecedor)
        self.fornecedor_listbox_update()


# Verificação se o script está sendo executado diretamente
if __name__ == "__main__":
    root = tk.Tk()  # Criação da janela principal
    app = App(root)  # Instância da classe App
    root.mainloop()  # Loop principal da interface gráfica
