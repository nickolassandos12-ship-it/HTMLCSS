import tkinter as tk
from tkinter import ttk, messagebox
import os


ARQUIVO_USUARIOS = "usuarios.txt"
if not os.path.exists(ARQUIVO_USUARIOS):
    open(ARQUIVO_USUARIOS, "w").close()

produtos = []
id_contador = [1]

def pagina_inicial():
    janela_inicial = tk.Toplevel(janela)
    janela_inicial.geometry("800x400+500+100")

    # abre e redimensiona a imagem
    tk.Label(janela_inicial, text="Aqui estão os comandos que você pode usar para acessar as funcionalidades da tela principal", font=8).pack()
    img = Image.open(r"C:/Users/Felipe/Desktop/Trabalho/1.jpg")
    img = img.resize((600,400))
    imagem = ImageTk.PhotoImage(img)

    # mantém a referência dentro da janela_inicial
    janela_inicial.imagem = imagem  

    # adiciona o label com a imagem
    tk.Label(janela_inicial, image=imagem).pack(pady=20)


def estoque():
    janela_estoque = tk.Toplevel(janela)
    janela_estoque.title("Estoque")
    janela_estoque.geometry("800x500+500+100")

    frame_botoes = tk.Frame(janela_estoque)
    frame_botoes.pack(pady=10)

    tree = ttk.Treeview(janela_estoque, columns=("ID", "Nome", "Quantidade", "pdc", "pdv"), show="headings")
    tree.heading("ID", text="ID")
    tree.heading("Nome", text="Nome")
    tree.heading("Quantidade", text="Quantidade")
    tree.heading("pdc", text="Preço Compra")
    tree.heading("pdv", text="Preço Venda")
    tree.column("ID", width=80)
    tree.column("Nome", width=200)
    tree.column("Quantidade", width=150)
    tree.column("pdc", width=150)
    tree.column("pdv", width=150)
    tree.pack(fill="both", expand=True, padx=20, pady=10)

    def atualizar_tabela():
        for item in tree.get_children():
            tree.delete(item)
        for p in produtos:
            tree.insert("", "end", values=(p["id"], p["nome"], p["quantidade"], p["pdc"], p["pdv"]))

    def janela_adicionar():
        j = tk.Toplevel(janela_estoque)
        j.title("Adicionar Produto")
        j.geometry("400x300")

        tk.Label(j, text="Nome do Produto:").pack(pady=5)
        entry_nome = tk.Entry(j)
        entry_nome.pack()
        tk.Label(j, text="Quantidade:").pack(pady=5)
        entry_qtd = tk.Entry(j)
        entry_qtd.pack()
        tk.Label(j, text="Preço de Compra:").pack(pady=5)
        entry_pdc = tk.Entry(j)
        entry_pdc.pack()
        tk.Label(j, text="Preço de Venda:").pack(pady=5)
        entry_pdv = tk.Entry(j)
        entry_pdv.pack()

        def adicionar():
            nome = entry_nome.get()
            try:
                qtd = int(entry_qtd.get())
                pdc = float(entry_pdc.get())
                pdv = float(entry_pdv.get())
                if nome == "" or qtd < 0 or pdc < 0 or pdv < 0:
                    raise ValueError
            except:
                messagebox.showerror("Erro", "Insira valores válidos.", parent=j)
                return
            produto = {
                "id": id_contador[0],
                "nome": nome,
                "quantidade": qtd,
                "pdc": pdc,
                "pdv": pdv
            }
            produtos.append(produto)
            id_contador[0] += 1
            atualizar_tabela()
            j.destroy()

        tk.Button(j, text="Adicionar", command=adicionar).pack(pady=10)

    def janela_saida():
        j = tk.Toplevel(janela_estoque)
        j.title("Saída de Produto")
        j.geometry("300x200")

        tk.Label(j, text="ID do Produto:").pack(pady=5)
        entry_id = tk.Entry(j)
        entry_id.pack()
        tk.Label(j, text="Quantidade a remover:").pack(pady=5)
        entry_qtd = tk.Entry(j)
        entry_qtd.pack()

        def remover():
            try:
                id_busca = int(entry_id.get())
                qtd_saida = int(entry_qtd.get())
                if qtd_saida <= 0:
                    raise ValueError
            except:
                messagebox.showerror("Erro", "ID e quantidade devem ser válidos.", parent=j)
                return
            for produto in produtos:
                if produto["id"] == id_busca:
                    if produto["quantidade"] >= qtd_saida:
                        produto["quantidade"] -= qtd_saida
                        if produto["quantidade"] == 0:
                            messagebox.showinfo("Aviso", "Seus produtos acabaram", parent=j)
                        atualizar_tabela()
                        j.destroy()
                        return
                    else:
                        messagebox.showwarning("Aviso", "Quantidade insuficiente no estoque.", parent=j)
                        return
            messagebox.showerror("Erro", "Produto não encontrado.", parent=j)

        tk.Button(j, text="Confirmar Saída", command=remover).pack(pady=10)

    tk.Button(frame_botoes, text="Adicionar Produto", command=janela_adicionar, width=20).pack(side="left", padx=10)
    tk.Button(frame_botoes, text="Saída de Produto", command=janela_saida, width=20).pack(side="left", padx=10)

def relatorio():
    janela_relatorio = tk.Toplevel(janela)
    janela_relatorio.geometry("600x400+500+100")

    def somar_vendas():
        if not produtos:
            messagebox.showerror("Saldo", "Nenhum produto adicionado.", parent=janela_relatorio)
            return
        soma_pdc = sum(p["pdc"] * p["quantidade"] for p in produtos)
        soma_pdv = sum(p["pdv"] * p["quantidade"] for p in produtos)
        lucros = soma_pdv - soma_pdc
        messagebox.showinfo("Saldo",
            f"Total Preço Compra: R${soma_pdc:.2f}\n"
            f"Total Preço Venda: R${soma_pdv:.2f}\n"
            f"Lucros ao vender tudo: R${lucros:.2f}",
            parent=janela_relatorio)

    def mostra_max():
        if not produtos:
            messagebox.showerror("Saldo", "Nenhum produto adicionado.", parent=janela_relatorio)
            return
        maior = max(produtos, key=lambda x: x["quantidade"])
        messagebox.showinfo("Produto com mais estoque",
            f"O produto com maior quantidade é {maior['nome']} com {maior['quantidade']} unidades.",
            parent=janela_relatorio)

    def mostra_min():
        if not produtos:
            messagebox.showerror("Saldo", "Nenhum produto adicionado.", parent=janela_relatorio)
            return
        menor = min(produtos, key=lambda x: x["quantidade"])
        messagebox.showinfo("Produto com menos estoque",
            f"O produto com menor quantidade é {menor['nome']} com {menor['quantidade']} unidades.",
            parent=janela_relatorio)

    tk.Label(janela_relatorio, text="Relatório", width=18, height=1, font=1).pack(anchor="w")
    tk.Button(janela_relatorio, text="Mostrar saldo", command=somar_vendas, width=25, height=2).pack(anchor="w", padx=10, pady=5)
    tk.Button(janela_relatorio, text="Mostrar maior quantidade", command=mostra_max, width=25, height=2).pack(anchor="w", padx=10, pady=5)
    tk.Button(janela_relatorio, text="Mostrar menor quantidade", command=mostra_min, width=25, height=2).pack(anchor="w", padx=10, pady=5)

def usuario():
    messagebox.showinfo("Usuário", "Você já está logado!", parent=janela)

def precionar_tecla(event):
    tecla = event.char.lower()
    if tecla == "e":
        estoque()
    elif tecla == "r":
        relatorio()
    elif tecla == "u":
        usuario()

def abrir_janela_principal():
    global janela
    janela = tk.Tk()
    janela.title("Mercadinho")
    janela.geometry("800x400+300+100")

    tk.Label(janela, text="Stoke 0800", width=18, height=1, font=1).pack(anchor="w")
    tk.Button(janela, text="Página Inicial", command=pagina_inicial, width=20, height=2).pack(anchor="w", padx=10, pady=5)
    tk.Button(janela, text="Estoque", command=estoque, width=20, height=2).pack(anchor="w", padx=10, pady=5)
    tk.Button(janela, text="Relatório", command=relatorio, width=20, height=2).pack(anchor="w", padx=10, pady=5)
    tk.Button(janela, text="Usuário", command=usuario, width=20, height=2).pack(anchor="w", padx=10, pady=5)

    janela.bind("<Key>", precionar_tecla)
    janela.mainloop()



def iniciar_login():
    login_janela = tk.Tk()
    login_janela.title("Login de Usuário")
    login_janela.geometry("300x250+500+150")

    tk.Label(login_janela, text="Usuário").pack(pady=5)
    usuario_entry = tk.Entry(login_janela)
    usuario_entry.pack()
    tk.Label(login_janela, text="Senha").pack(pady=5)
    senha_entry = tk.Entry(login_janela, show="*")
    senha_entry.pack()

    def cadastrar():
        u = usuario_entry.get().strip()
        s = senha_entry.get().strip()
        if not u or not s:
            return messagebox.showwarning("Aviso", "Preencha todos os campos!", parent=login_janela)
        with open(ARQUIVO_USUARIOS, "r") as f:
            if any(l.split(",")[0] == u for l in f):
                return messagebox.showerror("Erro", "Usuário já existe!", parent=login_janela)
        with open(ARQUIVO_USUARIOS, "a") as f:
            f.write(f"{u},{s}\n")
        messagebox.showinfo("Sucesso", "Usuário cadastrado com sucesso!", parent=login_janela)
        usuario_entry.delete(0, tk.END)
        senha_entry.delete(0, tk.END)

    def login():
        u = usuario_entry.get().strip()
        s = senha_entry.get().strip()
        with open(ARQUIVO_USUARIOS, "r") as f:
            if any(l.strip() == f"{u},{s}" for l in f):
                messagebox.showinfo("Bem-vindo", f"Olá, {u}!", parent=login_janela)
                login_janela.destroy()
                abrir_janela_principal()
            else:
                messagebox.showerror("Erro", "Usuário ou senha incorretos.", parent=login_janela)

    tk.Button(login_janela, text="Cadastrar", command=cadastrar, width=20).pack(pady=10)
    tk.Button(login_janela, text="Login", command=login, width=20).pack()

    login_janela.mainloop()


iniciar_login()
