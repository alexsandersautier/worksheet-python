import openpyxl

workbook = openpyxl.Workbook()

del workbook['Sheet']

workbook.create_sheet('vagas')

sheet_vagas = workbook['vagas']

sheet_vagas.append(['Empresa','Vaga','Data da Aplicação','Retorno'])

continuar = 's'
while continuar == 's':
    empresa = input('Digite o nome da empresa: ')
    vaga = input('Digite o nome da vaga: ')
    data_aplicacao = input('Digite a data de aplicação para a vaga: ')
    retorno = input('Teve retorno esta vaga? ')
    sheet_vagas.append([empresa,vaga,data_aplicacao,retorno])
    continuar = input('Desejar preencher mais dados? (s/n): ')

workbook.save('Acompanhamento de Vagas.xlsx')