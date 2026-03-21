import tkinter as tk
from tkinter import ttk

class CarroView:
    def __init__(self, root):
        self.root = root
        self.root.title("🚗 Sistema MVC")
        self.root.geometry("600x450")
        self.root.configure(bg="#1e1e2f")

        self.frame = tk.Frame(root, background="#1e1e2f")
        self.frame.pack(pady=10)

        tk.Label(self.frame, text="ID", background="#1e1e2f",fg="white").grid(row=0, column=0)
        self.entry_id = tk.Entry(self.frame)
        self.entry_id.grid(row=0, column=1)

        tk.Label(self.frame, text="Marca", background="#1e1e2f",fg="white").grid(row=1, column=0)
        self.entry_marca = tk.Entry(self.frame)
        self.entry_marca.grid(row=1, column=1)

        tk.Label(self.frame, text="Modelo", background="#1e1e2f",fg="white").grid(row=2, column=0)
        self.entry_modelo = tk.Entry(self.frame)
        self.entry_modelo.grid(row=2, column=1)

        self.btn_add = ttk.Button(self.frame, text="Adicionar")
        self.btn_add.grid(row=15, column=0, pady=5)

        self.btn_update = ttk.Button(self.frame, text="Atualizar")
        self.btn_update.grid(row=15, column=1)

        self.btn_delete = ttk.Button(self.frame, text="Deletar")
        self.btn_delete.grid(row=15, column=2)




        style = ttk.Style()
        style.theme_use("default")


        # Estilo da tabela
        style.configure("Treeview",
                        background="#2a2a40",
                        foreground="white",
                        rowheight=25,
                        fieldbackground="#2a2a40")
        style.map("Treeview", background=[("selected", "#4a90e2")])
        self.tabela = ttk.Treeview(root, columns=("ID", "Marca", "Modelo"), show="headings")
        self.tabela.heading("ID", text="ID")
        self.tabela.heading("Marca", text="Marca")
        self.tabela.heading("Modelo", text="Modelo")
        self.tabela.pack(fill="both", expand=True)
    

    def get_dados(self):
        return (
            self.entry_id.get(),
            self.entry_marca.get(),
            self.entry_modelo.get()
        )

    def limpar_campos(self):
        self.entry_id.delete(0, tk.END)
        self.entry_marca.delete(0, tk.END)
        self.entry_modelo.delete(0, tk.END)

    def atualizar_tabela(self, dados):
        for i in self.tabela.get_children():
            self.tabela.delete(i)
        for row in dados:
            self.tabela.insert("", "end", values=row)
