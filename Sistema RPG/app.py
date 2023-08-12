import tkinter as tk
import json


#função para abrir ficha já existente
def abrir_ficha_selecionada():
    ficha_selecionada = listbox_fichas.get(tk.ACTIVE)
    if ficha_selecionada:
        nome_arquivo = f"fichas/{ficha_selecionada}.json"
        with open(nome_arquivo, "r") as arquivo_json:
            dados_ficha = json.load(arquivo_json)

        #criar nova janela para exibir os dados da ficha
        janela_ficha = tk.Toplevel(janela)
        janela_ficha.title(f"Ficha: {ficha_selecionada}")
        janela_ficha.geometry("800x600")

        #exibir os detalhes da ficha na nova janela
        for chave, valor in dados_ficha.items():
            label_chave = tk.Label(janela_ficha, text=chave)
            label_chave.pack()

            label_valor = tk.Label(janela_ficha, text=valor)
            label_valor.pack()

#função para criar nova ficha
def criar_nova_ficha():
    nova_ficha = entry_nova_ficha.get()
    if nova_ficha:
        #verificar se o nome da ficha já existe:
        if f"{nova_ficha}.json" in os.listdir("fichas"): #se o nome da ficha já existe  na pasta fichas 
            label_resultado.config(text="Ficha já existe!")
        else:
            #criar um dicionário com campos vazios para a nova ficha
            dados_ficha = {
                "Nome": nova_ficha,
                "Idade": "",
                "Parentesco_divino":"",
                "Parentesco_mortal":"",
                "Alinhamento_moral":"",
                "Residência":"",
                "Classe_social":"",
                "Nível":"",
                "Pontos_de_vida":"",
                "CA":"",
            }

#criando janela principal
janela = tk.Tk()
janela.title("Sistema de RPG - Fichas")
janela.geometry("800x600")
#texto da janela
lab = tk.Label(janela, text="Personagens", font=("Times New Roman 20 bold",26))
# lab.grid(row=0, column=0, columnspan=2, sticky="ew")
# entry_nome = tk.Entry(janela)
# entry_nome.grid(row=0, column=3, columnspan=2, sticky="ew")












janela.mainloop()