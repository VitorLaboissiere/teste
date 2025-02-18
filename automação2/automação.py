import xmltodict #passar xml para a biblioteca python
import os # manuziar arquivos
import pandas as pd

# json para formatar o dicionario para ficar melhor de visualizar 

def get_info(name_arq,valores):
    #fazendo com que o arquivo xml se torne um dicionário python
    
    with open(f'nfs/{name_arq}','rb') as arq_xml:
        dic_arquivo = xmltodict.parse(arq_xml)
        if 'NFe' in dic_arquivo:
            info_nota = dic_arquivo['NFe']['infNFe']
        else:
            info_nota = dic_arquivo['nfeProc']['NFe']['infNFe']    
        number_not = info_nota['@Id'] 
        empresa_emi= info_nota['emit']['xNome']
        name_clien= info_nota['dest']['xNome']
        adress = info_nota['dest']['enderDest']
        if 'vol' in info_nota ['transp']:
            pesoB = info_nota['transp']['vol']['pesoB']
        else:
             pesoB = 'não informado'
        valores.append([number_not,empresa_emi,name_clien,adress,pesoB]) 
    
lista_arq = os.listdir("nfs")
colunas = ["numero_nota","Empresa_emissora","Nome_cliente", "Endereço","Peso_Bruto"]
valores = []
       
for arq in lista_arq:
    get_info(arq,   valores)
tabela = pd.DataFrame(columns=colunas, data =valores)
tabela.to_excel("NotasFiscais.xlsx",index=False) # no Exel já tem contadores de linhas

    
                                                    