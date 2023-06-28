import openpyxl

def criar__planilha(empresa,vaga,data_aplicacao,retorno, continuar):

    workbook = openpyxl.Workbook()

    del workbook['Sheet']

    workbook.create_sheet('vagas')

    sheet_vagas = workbook['vagas']

    sheet_vagas.append(['Empresa','Vaga','Data da Aplicação','Retorno'])

    con = 's'
    while continuar == 's':
        emp = empresa
        vag = vaga
        dt_apli = data_aplicacao
        ret = retorno
        sheet_vagas.append([emp,vag,dt_apli,ret])
        con = continuar

    workbook.save('Acompanhamento de Vagas.xlsx')