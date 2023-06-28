from tkinter import *
import app

def exibir_selecao():
    valor_checkbox1 = checkbox1_var.get()
    valor_checkbox2 = checkbox2_var.get()


janela = Tk()

janela.title("Acompanhamento de Vagas")


texto = Label(janela, text="Acompanhamento de Vagas")
texto.grid(column=0, row=0, padx=5, pady=2)

label_empresa = Label(janela, text="Empresa:")
label_empresa.grid(column=0, row=1, padx=5, pady=2)
empresa = Entry(janela, text="Digite o nome da empresa")
empresa.grid(column=1, row=1, padx=5, pady=2)

label_vaga = Label(janela, text="Vaga:")
label_vaga.grid(column=0, row=2, padx=5, pady=2)
vaga = Entry(janela, text="Digite o nome da vaga")
vaga.grid(column=1, row=2, padx=5, pady=2)

label_data_aplicacao = Label(janela, text="Data Aplicação:")
label_data_aplicacao.grid(column=0, row=3, padx=5, pady=2)
data_aplicacao = Entry(janela, text="Digite o nome da empresa")
data_aplicacao.grid(column=1, row=3, padx=5, pady=2)

label_retorno = Label(janela, text="Teve Retorno?")
label_retorno.grid(column=0, row=4, padx=5, pady=2)
retorno = Entry(janela, text="Digite o nome da empresa")
retorno.grid(column=1, row=4, padx=5, pady=2)


label_checkbox1 = Label(janela, text="Cadastrar nova vaga?")
label_checkbox1.grid(column=0, row=10, padx=1, pady=1)

checkbox1_var = IntVar()
checkbox1 = Checkbutton(janela, text="Sim", variable=checkbox1_var)
checkbox1.grid(column=1, row=10, padx=1, pady=1)


checkbox2_var = IntVar()
checkbox2 = Checkbutton(janela, text="Não", variable=checkbox2_var)
checkbox2.grid(column=2, row=10, padx=1, pady=1)

botao = Button(janela, text="Exibir seleção", command=exibir_selecao)
botao.grid(column=0, row=12, padx=5, pady=2)



# botao = Button(janela, text="Buscar cotações", command=pegar_cotacoes)
# botao.grid(column=0, row=6, padx=5, pady=2)

# texto_resposta = Label(janela, text="")
# texto_resposta.grid(column=0, row=2, padx=5, pady=2)


janela.mainloop()