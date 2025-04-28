# interface.py

import customtkinter as ctk
from tkinter import messagebox
from Main import criar_assistido, listar_assistidos, atualizar_assistido, deletar_assistido

# Configurações iniciais
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Cadastro de Assistidos - Defensoria Pública")
app.geometry("700x500")

abas = ctk.CTkTabview(app)
abas.pack(fill="both", expand=True, padx=20, pady=20)

aba_cadastro = abas.add("Cadastrar")
aba_listagem = abas.add("Listar/Editar")

# Cadastro 
def cadastrar():
    nome = entry_nome.get()
    cpf = entry_cpf.get()
    endereco = entry_endereco.get()
    raca = combo_raca.get()
    genero = combo_genero.get()

    if not all([nome, cpf, endereco, raca, genero]):
        messagebox.showwarning("Atenção", "Preencha todos os campos.")
        return

    criar_assistido(nome, cpf, endereco, raca, genero)
    messagebox.showinfo("Sucesso", "Assistido cadastrado com sucesso!")
    entry_nome.delete(0, 'end')
    entry_cpf.delete(0, 'end')
    entry_endereco.delete(0, 'end')
    combo_raca.set("Raça")
    combo_genero.set("Gênero")
    carregar_assistidos()

entry_nome = ctk.CTkEntry(aba_cadastro, placeholder_text="Nome completo")
entry_nome.pack(pady=10, padx=20)
entry_cpf = ctk.CTkEntry(aba_cadastro, placeholder_text="CPF")
entry_cpf.pack(pady=10, padx=20)
entry_endereco = ctk.CTkEntry(aba_cadastro, placeholder_text="Endereço completo")
entry_endereco.pack(pady=10, padx=20)
combo_raca = ctk.CTkOptionMenu(aba_cadastro, values=["Branca", "Preta", "Parda", "Amarela", "Indígena", "Outro"])
combo_raca.set("Raça")
combo_raca.pack(pady=10, padx=20)
combo_genero = ctk.CTkOptionMenu(aba_cadastro, values=["Masculino", "Feminino", "Outro"])
combo_genero.set("Gênero")
combo_genero.pack(pady=10, padx=20)

botao_cadastrar = ctk.CTkButton(aba_cadastro, text="Cadastrar", command=cadastrar)
botao_cadastrar.pack(pady=20)

# Listar/Editar
tabela = ctk.CTkFrame(aba_listagem)
tabela.pack(fill="both", expand=True, padx=10, pady=10)

lista = ctk.CTkTextbox(tabela, height=300, width=640)
lista.pack(pady=10)

frame_editar = ctk.CTkFrame(aba_listagem)
frame_editar.pack(pady=10)

entry_id = ctk.CTkEntry(frame_editar, placeholder_text="ID")
entry_id.grid(row=0, column=0, padx=5)
entry_nome_e = ctk.CTkEntry(frame_editar, placeholder_text="Nome")
entry_nome_e.grid(row=0, column=1, padx=5)
entry_cpf_e = ctk.CTkEntry(frame_editar, placeholder_text="CPF")
entry_cpf_e.grid(row=0, column=2, padx=5)
entry_endereco_e = ctk.CTkEntry(frame_editar, placeholder_text="Endereço")
entry_endereco_e.grid(row=0, column=3, padx=5)
combo_raca_e = ctk.CTkOptionMenu(frame_editar, values=["Branca", "Preta", "Parda", "Amarela", "Indígena", "Outro"])
combo_raca_e.set("Raça")
combo_raca_e.grid(row=0, column=4, padx=5)
combo_genero_e = ctk.CTkOptionMenu(frame_editar, values=["Masculino", "Feminino", "Outro"])
combo_genero_e.set("Gênero")
combo_genero_e.grid(row=0, column=5, padx=5)

def carregar_assistidos():
    lista.delete("1.0", "end")
    dados = listar_assistidos()
    for dado in dados:
        lista.insert("end", f"ID: {dado[0]} | Nome: {dado[1]} | CPF: {dado[2]} | Endereço: {dado[3]} | Raça: {dado[4]} | Gênero: {dado[5]}\n")

def editar_assistido():
    try:
        atualizar_assistido(
            int(entry_id.get()),
            entry_nome_e.get(),
            entry_cpf_e.get(),
            entry_endereco_e.get(),
            combo_raca_e.get(),
            combo_genero_e.get()
        )
        messagebox.showinfo("Sucesso", "Assistido atualizado.")
        carregar_assistidos()
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao atualizar: {e}")

def excluir_assistido():
    try:
        id_assistido = int(entry_id.get())
        deletar_assistido(id_assistido)
        messagebox.showinfo("Sucesso", "Assistido excluído.")
        carregar_assistidos()
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao excluir: {e}")

b_editar = ctk.CTkButton(aba_listagem, text="Editar", command=editar_assistido)
b_editar.pack(side="left", padx=20)
b_excluir = ctk.CTkButton(aba_listagem, text="Excluir", command=excluir_assistido)
b_excluir.pack(side="right", padx=20)

carregar_assistidos()
app.mainloop()
