from tkinter import messagebox

class CarroController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

        self.view.btn_add.config(command=self.adicionar)
        self.view.btn_update.config(command=self.atualizar)
        self.view.btn_delete.config(command=self.deletar)

        self.carregar()

    def carregar(self):
        dados = self.model.listar()
        self.view.atualizar_tabela(dados)

    def adicionar(self):
        _, marca, modelo = self.view.get_dados()

        if not marca or not modelo:
            messagebox.showwarning("Aviso", "Preencha os campos!")
            return

        self.model.adicionar(marca, modelo)
        self.view.limpar_campos()
        self.carregar()

    def atualizar(self):
        id, marca, modelo = self.view.get_dados()

        if not id:
            messagebox.showerror("Erro", "Informe o ID!")
            return

        if self.model.atualizar(int(id), marca, modelo):
            self.carregar()
        else:
            messagebox.showwarning("Aviso", "ID não encontrado!")

    def deletar(self):
        id, _, _ = self.view.get_dados()

        if not id:
            messagebox.showerror("Erro", "Informe o ID!")
            return

        if self.model.deletar(int(id)):
            self.carregar()
        else:
            messagebox.showwarning("Aviso", "ID não encontrado!")
