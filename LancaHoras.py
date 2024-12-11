import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector

def conectar_banco():
    return mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="password",  # Insira sua senha
        database="horas"
    )

class LancaHorasApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lanca Horas")

        # Criar menu principal
        menu_bar = tk.Menu(self.root)
        self.root.config(menu=menu_bar)

        pessoa_menu = tk.Menu(menu_bar, tearoff=0)
        pessoa_menu.add_command(label="Cadastrar", command=self.cadastrar_pessoa)

        atividade_menu = tk.Menu(menu_bar, tearoff=0)
        atividade_menu.add_command(label="Cadastrar", command=self.cadastrar_atividade)

        horas_menu = tk.Menu(menu_bar, tearoff=0)
        horas_menu.add_command(label="Lançar", command=self.lancar_horas)

        menu_bar.add_cascade(label="Pessoa", menu=pessoa_menu)
        menu_bar.add_cascade(label="Atividade", menu=atividade_menu)
        menu_bar.add_cascade(label="Horas Lançadas", menu=horas_menu)

    def cadastrar_pessoa(self):
        janela = tk.Toplevel(self.root)
        janela.title("Cadastrar Pessoa")

        tk.Label(janela, text="ID Pessoa:").grid(row=0, column=0, padx=5, pady=5)
        id_pessoa = tk.Entry(janela)
        id_pessoa.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(janela, text="Nome:").grid(row=1, column=0, padx=5, pady=5)
        nome_pessoa = tk.Entry(janela)
        nome_pessoa.grid(row=1, column=1, padx=5, pady=5)

        def inserir_pessoa():
            try:
                conexao = conectar_banco()
                cursor = conexao.cursor()
                cursor.execute("INSERT INTO pessoa (idPessoa, pessoa_nome) VALUES (%s, %s)",
                               (id_pessoa.get(), nome_pessoa.get()))
                conexao.commit()
                messagebox.showinfo("Sucesso", "Pessoa cadastrada com sucesso!")
            except mysql.connector.Error as err:
                messagebox.showerror("Erro", f"Erro ao inserir pessoa: {err}")
            finally:
                cursor.close()
                conexao.close()

        tk.Button(janela, text="Salvar", command=inserir_pessoa).grid(row=2, column=0, columnspan=2, pady=10)

    def cadastrar_atividade(self):
        janela = tk.Toplevel(self.root)
        janela.title("Cadastrar Atividade")

        tk.Label(janela, text="Atividade:").grid(row=0, column=0, padx=5, pady=5)
        atividade = tk.Entry(janela)
        atividade.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(janela, text="Nome:").grid(row=1, column=0, padx=5, pady=5)
        nome_atividade = tk.Entry(janela)
        nome_atividade.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(janela, text="Tipo:").grid(row=2, column=0, padx=5, pady=5)
        tipo_atividade = tk.Entry(janela)
        tipo_atividade.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(janela, text="Descrição:").grid(row=3, column=0, padx=5, pady=5)
        descricao_atividade = tk.Entry(janela)
        descricao_atividade.grid(row=3, column=1, padx=5, pady=5)

        def inserir_atividade():
            try:
                conexao = conectar_banco()
                cursor = conexao.cursor()
                cursor.execute(
                    "INSERT INTO atividade (atividade, atividade_nome, atividade_tipo, atividade_descricao) VALUES (%s, %s, %s, %s)",
                    (atividade.get(), nome_atividade.get(), tipo_atividade.get(), descricao_atividade.get()))
                conexao.commit()
                messagebox.showinfo("Sucesso", "Atividade cadastrada com sucesso!")
            except mysql.connector.Error as err:
                messagebox.showerror("Erro", f"Erro ao inserir atividade: {err}")
            finally:
                cursor.close()
                conexao.close()

        tk.Button(janela, text="Salvar", command=inserir_atividade).grid(row=4, column=0, columnspan=2, pady=10)

    def lancar_horas(self):
        janela = tk.Toplevel(self.root)
        janela.title("Lançar Horas")

        tk.Label(janela, text="Data (AAAA-MM-DD):").grid(row=0, column=0, padx=5, pady=5)
        data = tk.Entry(janela)
        data.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(janela, text="Hora Início (HH:MM:SS):").grid(row=1, column=0, padx=5, pady=5)
        hora_inicio = tk.Entry(janela)
        hora_inicio.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(janela, text="Hora Fim (HH:MM:SS):").grid(row=2, column=0, padx=5, pady=5)
        hora_fim = tk.Entry(janela)
        hora_fim.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(janela, text="Detalhe:").grid(row=3, column=0, padx=5, pady=5)
        detalhe = tk.Entry(janela)
        detalhe.grid(row=3, column=1, padx=5, pady=5)

        tk.Label(janela, text="ID Pessoa:").grid(row=4, column=0, padx=5, pady=5)
        id_pessoa = tk.Entry(janela)
        id_pessoa.grid(row=4, column=1, padx=5, pady=5)

        tk.Label(janela, text="Atividade:").grid(row=5, column=0, padx=5, pady=5)
        atividade = tk.Entry(janela)
        atividade.grid(row=5, column=1, padx=5, pady=5)

        def inserir_horas():
            try:
                conexao = conectar_banco()
                cursor = conexao.cursor()
                cursor.execute(
                    """
                    INSERT INTO horaslancadas 
                    (hrlancto_data, hrlancto_hr_inicio, hrlancto_hr_fim, hrlancto_detalhe, Pessoa_idPessoa, Atividade_atividade) 
                    VALUES (%s, %s, %s, %s, %s, %s)
                    """,
                    (data.get(), hora_inicio.get(), hora_fim.get(), detalhe.get(), id_pessoa.get(), atividade.get())
                )
                conexao.commit()
                messagebox.showinfo("Sucesso", "Horas lançadas com sucesso!")
            except mysql.connector.Error as err:
                messagebox.showerror("Erro", f"Erro ao lançar horas: {err}")
            finally:
                cursor.close()
                conexao.close()

        tk.Button(janela, text="Salvar", command=inserir_horas).grid(row=6, column=0, columnspan=2, pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = LancaHorasApp(root)
    root.mainloop()
