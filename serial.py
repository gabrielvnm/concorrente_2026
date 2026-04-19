import os
import time

# objeto com os atributos do arquivo
class Linha:
    def __init__(self, sigla_tribunal,procedimento,ramo_justica,sigla_grau,uf_oj,municipio_oj,id_ultimo_oj,nome,mesano_cnm1,mesano_sent,casos_novos_2026,julgados_2026,prim_sent2026,suspensos_2026,dessobrestados_2026,cumprimento_meta1,distm2_a,julgm2_a,suspm2_a,cumprimento_meta2a,distm2_ant,julgm2_ant,suspm2_ant,desom2_ant,cumprimento_meta2ant,distm4_a,julgm4_a,suspm4_a,cumprimento_meta4a,distm4_b,julgm4_b,suspm4_b,cumprimento_meta4b):
        self.sigla_tribunal = sigla_tribunal 
        self.procedimento = procedimento
        self.ramo_justica = ramo_justica
        self.sigla_grau = sigla_grau
        self.uf_oj = uf_oj
        self.municipio_oj = municipio_oj
        self.id_ultimo_oj = id_ultimo_oj
        self.nome = nome
        self.mesano_cnm1 = mesano_cnm1
        self.mesano_sent = mesano_sent
        self.casos_novos_2026 = int(casos_novos_2026)
        self.julgados_2026 = int(julgados_2026)
        self.prim_sent2026 = int(prim_sent2026)
        self.suspensos_2026 = int(suspensos_2026)
        self.dessobrestados_2026 = int(dessobrestados_2026)
        self.cumprimento_meta1 = float(cumprimento_meta1)
        self.distm2_a = int(distm2_a)
        self.julgm2_a = int(julgm2_a)
        self.suspm2_a = int(suspm2_a)
        self.cumprimento_meta2a = float(cumprimento_meta2a)
        self.distm2_ant = int(distm2_ant)
        self.julgm2_ant = int(julgm2_ant)
        self.suspm2_ant = int(suspm2_ant)
        self.desom2_ant = int(desom2_ant)
        self.cumprimento_meta2ant = float(cumprimento_meta2ant)
        self.distm4_a = int(distm4_a)
        self.julgm4_a = int(julgm4_a)
        self.suspm4_a = int(suspm4_a)
        self.cumprimento_meta4a = int(cumprimento_meta4a)
        self.distm4_b = int(distm4_b)
        self.julgm4_b = int(julgm4_b)
        self.suspm4_b = int(suspm4_b)
        self.cumprimento_meta4b = float(cumprimento_meta4b)

#metodos pra imprimir o objeto
    def __str__(self):
        return f"{self.sigla_tribunal,self.procedimento, self.ramo_justica, self.sigla_grau,
                            self.uf_oj, self.municipio_oj,
                            self.id_ultimo_oj,self.nome,
                            self.mesano_cnm1,self.mesano_sent,
                            self.casos_novos_2026,self.julgados_2026,
                            self.prim_sent2026,self.suspensos_2026,
                            self.dessobrestados_2026,self.cumprimento_meta1,
                            self.distm2_a,self.julgm2_a,self.suspm2_a,
                            self.cumprimento_meta2a,self.distm2_ant,
                            self.julgm2_ant,self.suspm2_ant,self.desom2_ant,
                            self.cumprimento_meta2ant,self.distm4_a,
                            self.julgm4_a,self.suspm4_a,self.cumprimento_meta4a,
                            self.distm4_b, self.julgm4_b, self.suspm4_b,
                            self.cumprimento_meta4b}"

    def __repr__(self):
        return self.__str__()
#objeto pra calcular as metas por sigla do tribunal
class Meta_tribunal:
    def __init__(self, sigla_tribunal, meta1, meta2a, meta2ant, meta4a, meta4b):
        self.sigla_tribunal = sigla_tribunal
        self.meta1 = meta1
        self.meta2a = meta2a
        self.meta2ant = meta2ant
        self.meta4a = meta4a
        self.meta4b = meta4b

# Funçao abrir um arquivo e salvar na memoria como um objeto
def abrir_arquivo(nome_arquivo):
    linhas = []
    with open(nome_arquivo, 'r', encoding='utf-8') as file:
        header = file.readline() #pula o cabeçalho

        for line in file:
            line = line.strip()
            if not line:
                continue
        
            parts = line.split(',')
            if len(parts) == 33:
                linha = Linha(parts[0] if parts[0] else 0,
                              parts[1] if parts[1] else 0, 
                              parts[2] if parts[2] else 0,
                              parts[3] if parts[3] else 0,
                              parts[4] if parts[4] else 0,
                              parts[5] if parts[5] else 0,
                              parts[6] if parts[6] else 0,
                              parts[7] if parts[7] else 0,
                              parts[8] if parts[8] else 0,
                              parts[9] if parts[9] else 0,
                              parts[10] if parts[10] else 0,
                              parts[11] if parts[11] else 0,
                              parts[12] if parts[12] else 0,
                              parts[13] if parts[13] else 0,
                              parts[14] if parts[14] else 0,
                              parts[15] if parts[15] else 0,
                              parts[16] if parts[16] else 0,
                              parts[17] if parts[17] else 0,
                              parts[18] if parts[18] else 0,
                              parts[19] if parts[19] else 0,
                              parts[20] if parts[20] else 0,
                              parts[21] if parts[21] else 0,
                              parts[22] if parts[22] else 0,
                              parts[23] if parts[23] else 0,
                              parts[24] if parts[24] else 0,
                              parts[25] if parts[25] else 0,
                              parts[26] if parts[26] else 0,
                              parts[27] if parts[27] else 0,
                              parts[28] if parts[28] else 0,
                              parts[29] if parts[29] else 0,
                              parts[30] if parts[30] else 0,
                              parts[31] if parts[31] else 0,
                              parts[32] if parts[32] else 0)
                linhas.append(linha)

    return linhas
# Obter todos os dados e colocar na memoria
def concatenar_arquivos():

    nome_arquivo = "Base de Dados/teste_TRE-AC.csv"
    linhas = abrir_arquivo(nome_arquivo)
    nome_arquivo = "Base de Dados/teste_TRE-AL.csv"
    linhas = linhas + abrir_arquivo(nome_arquivo)
    nome_arquivo = "Base de Dados/teste_TRE-AM.csv"
    linhas = linhas + abrir_arquivo(nome_arquivo)
    nome_arquivo = "Base de Dados/teste_TRE-AP.csv"
    linhas = linhas + abrir_arquivo(nome_arquivo)
    nome_arquivo = "Base de Dados/teste_TRE-BA.csv"
    linhas = linhas + abrir_arquivo(nome_arquivo)
    nome_arquivo = "Base de Dados/teste_TRE-CE.csv"
    linhas = linhas + abrir_arquivo(nome_arquivo)
    nome_arquivo = "Base de Dados/teste_TRE-DF.csv"
    linhas = linhas + abrir_arquivo(nome_arquivo)
    nome_arquivo = "Base de Dados/teste_TRE-ES.csv"
    linhas = linhas + abrir_arquivo(nome_arquivo)
    nome_arquivo = "Base de Dados/teste_TRE-GO.csv"
    linhas = linhas + abrir_arquivo(nome_arquivo)
    nome_arquivo = "Base de Dados/teste_TRE-MA.csv"
    linhas = linhas + abrir_arquivo(nome_arquivo)
    nome_arquivo = "Base de Dados/teste_TRE-MG.csv"
    linhas = linhas + abrir_arquivo(nome_arquivo)
    nome_arquivo = "Base de Dados/teste_TRE-MS.csv"
    linhas = linhas + abrir_arquivo(nome_arquivo)
    nome_arquivo = "Base de Dados/teste_TRE-MT.csv"
    linhas = linhas + abrir_arquivo(nome_arquivo)
    nome_arquivo = "Base de Dados/teste_TRE-PA.csv"
    linhas = linhas + abrir_arquivo(nome_arquivo)
    nome_arquivo = "Base de Dados/teste_TRE-PB.csv"
    linhas = linhas + abrir_arquivo(nome_arquivo)
    nome_arquivo = "Base de Dados/teste_TRE-PE.csv"
    linhas = linhas + abrir_arquivo(nome_arquivo)
    nome_arquivo = "Base de Dados/teste_TRE-PI.csv"
    linhas = linhas + abrir_arquivo(nome_arquivo)
    nome_arquivo = "Base de Dados/teste_TRE-PR.csv"
    linhas = linhas + abrir_arquivo(nome_arquivo)
    nome_arquivo = "Base de Dados/teste_TRE-RJ.csv"
    linhas = linhas + abrir_arquivo(nome_arquivo)
    nome_arquivo = "Base de Dados/teste_TRE-RN.csv"
    linhas = linhas + abrir_arquivo(nome_arquivo)
    nome_arquivo = "Base de Dados/teste_TRE-RO.csv"
    linhas = linhas + abrir_arquivo(nome_arquivo)
    nome_arquivo = "Base de Dados/teste_TRE-RR.csv"
    linhas = linhas + abrir_arquivo(nome_arquivo)
    nome_arquivo = "Base de Dados/teste_TRE-RS.csv"
    linhas = linhas + abrir_arquivo(nome_arquivo)
    nome_arquivo = "Base de Dados/teste_TRE-SC.csv"
    linhas = linhas + abrir_arquivo(nome_arquivo)
    nome_arquivo = "Base de Dados/teste_TRE-SE.csv"
    linhas = linhas + abrir_arquivo(nome_arquivo)
    nome_arquivo = "Base de Dados/teste_TRE-SP.csv"
    linhas = linhas + abrir_arquivo(nome_arquivo)
    nome_arquivo = "Base de Dados/teste_TRE-TO.csv"
    linhas = linhas + abrir_arquivo(nome_arquivo)
    
    return linhas

# Escrever a lista inteira com todos os dados em um único arquivo
def escrever_arquivo_inteiro(linhas):
    with open('lista_completa.csv', 'a', encoding='utf-8') as file:
        for linha in linhas:
          #achei mais facil colocar os atributos assim pra formatar direito no arquivo
            file.write(f"{linha.sigla_tribunal},{linha.procedimento},{linha.ramo_justica},{linha.sigla_grau},{linha.uf_oj},{linha.municipio_oj},{linha.id_ultimo_oj},{linha.nome},{linha.mesano_cnm1},{linha.mesano_sent},{linha.casos_novos_2026},{linha.julgados_2026},{linha.prim_sent2026},{linha.suspensos_2026},{linha.dessobrestados_2026},{linha.cumprimento_meta1},{linha.distm2_a},{linha.julgm2_a},{linha.suspm2_a},{linha.cumprimento_meta2a},{linha.distm2_ant},{linha.julgm2_ant},{linha.suspm2_ant},{linha.desom2_ant},{linha.cumprimento_meta2ant},{linha.distm4_a},{linha.julgm4_a},{linha.suspm4_a},{linha.cumprimento_meta4a},{linha.distm4_b},{linha.julgm4_b},{linha.suspm4_b},{linha.cumprimento_meta4b}\n")
    print("Arquivo escrito com sucesso!")
    return
#gravar um arquivo com nome inserido pelo usuario
def escrever_municipios(linhas,nome_municipio):
    nome_arquivo = nome_municipio + ".csv"
    with open(nome_arquivo, 'a', encoding='utf-8') as file:
        for linha in linhas:
            file.write(f"{linha.sigla_tribunal},{linha.procedimento},{linha.ramo_justica},{linha.sigla_grau},{linha.uf_oj},{linha.municipio_oj},{linha.id_ultimo_oj},{linha.nome},{linha.mesano_cnm1},{linha.mesano_sent},{linha.casos_novos_2026},{linha.julgados_2026},{linha.prim_sent2026},{linha.suspensos_2026},{linha.dessobrestados_2026},{linha.cumprimento_meta1},{linha.distm2_a},{linha.julgm2_a},{linha.suspm2_a},{linha.cumprimento_meta2a},{linha.distm2_ant},{linha.julgm2_ant},{linha.suspm2_ant},{linha.desom2_ant},{linha.cumprimento_meta2ant},{linha.distm4_a},{linha.julgm4_a},{linha.suspm4_a},{linha.cumprimento_meta4a},{linha.distm4_b},{linha.julgm4_b},{linha.suspm4_b},{linha.cumprimento_meta4b}\n")
    print("Arquivo escrito com sucesso!")
    return

# função pra abrir um arquivo menor para teste
def arquivo_teste():
    nome_arquivo = "D:/code/concorrente/teste1.txt"
    linhas = abrir_arquivo(nome_arquivo)

    return linhas


# Separar a lista por municipio, calcular as metas e escrever num arquivo
def metas_resumo_municipio(linhas):
    # escreve a primeira linha no arquivo
    with open('metas_municipio.csv', 'a', encoding='utf-8') as file: 
        file.write(f"Municipio,Meta1,Meta2a,Meta2ant,Meta4a,Meta4b\n")
    for i in linhas:

        if linhas: #checa se a lista nao esta vazia
            
            indice_zero = linhas[0].municipio_oj # obtem nome do municipio
            linhas_municipio = [linha for linha in linhas if linha.municipio_oj == indice_zero] # coloca todas as ocorrencias do municipio em outra lista
            print(indice_zero)
            # formulas com os dados da lista
            sum_julgados_2026 = sum(linha.julgados_2026 for linha in linhas_municipio)
            sum_casos_novos_2026 = sum(linha.casos_novos_2026 for linha in linhas_municipio)
            sum_dessobrestados_2026 = sum(linha.dessobrestados_2026 for linha in linhas_municipio)
            sum_suspensos_2026 = sum(linha.suspensos_2026 for linha in linhas_municipio)
            
            if (sum_casos_novos_2026 + sum_dessobrestados_2026 - sum_suspensos_2026) == 0: #verificação pra nao dividir por zero
                meta1_var = 0
            else: 
                meta1_var = sum_julgados_2026/(sum_casos_novos_2026 + sum_dessobrestados_2026 - sum_suspensos_2026) 
            
            sum_julgm2_a = sum(linha.julgm2_a for linha in linhas_municipio)
            sum_distm2_a = sum(linha.distm2_a for linha in linhas_municipio)
            sum_suspm2_a = sum(linha.suspm2_a for linha in linhas_municipio)

            if (sum_distm2_a-sum_suspm2_a) == 0:
                meta2a_var = 0
            else:
                meta2a_var = sum_julgm2_a/(sum_distm2_a-sum_suspm2_a)

            sum_julgm2_ant = sum(linha.julgm2_ant for linha in linhas_municipio)
            sum_distm2_ant = sum(linha.distm2_ant for linha in linhas_municipio)
            sum_suspm2_ant = sum(linha.suspm2_ant for linha in linhas_municipio)
            sum_desom2_ant = sum(linha.desom2_ant for linha in linhas_municipio)

            if (sum_distm2_ant-sum_suspm2_ant-sum_desom2_ant) == 0:
                meta2ant_var = 0
            else:
                meta2ant_var = sum_julgm2_ant/(sum_distm2_ant-sum_suspm2_ant-sum_desom2_ant)

            sum_julgm4_a = sum(linha.julgm4_a for linha in linhas_municipio)
            sum_distm4_a = sum(linha.distm4_a for linha in linhas_municipio)
            sum_suspm4_a = sum(linha.suspm4_a for linha in linhas_municipio)

            if (sum_distm4_a-sum_suspm4_a) == 0:
                meta4a_var = 0
            else:
                meta4a_var = sum_julgm4_a/(sum_distm4_a-sum_suspm4_a)

            sum_julgm4_b = sum(linha.julgm4_b for linha in linhas_municipio)
            sum_distm4_b = sum(linha.distm4_a for linha in linhas_municipio)
            sum_suspm4_b = sum(linha.suspm4_b for linha in linhas_municipio)

            if (sum_distm4_b-sum_suspm4_b) == 0:
                meta4b_var = 0
            else:
                meta4b_var = sum_julgm4_b/(sum_distm4_b-sum_suspm4_b)

            meta1_var = meta1_var *100
            meta2a_var = meta2a_var*1000/7
            meta2ant_var = meta2ant_var*100
            meta4a_var = meta4a_var*100
            meta4b_var = meta4b_var*100

            # escrever o resultado no arquivo
            with open('metas_municipio.csv', 'a', encoding='utf-8') as file: 
                file.write(f"{indice_zero},{meta1_var:.2f},{meta2a_var:.2f},{meta2ant_var:.2f},{meta4a_var:.2f},{meta4b_var:.2f}\n")

            linhas = [linha for linha in linhas if linha.municipio_oj != indice_zero] # apaga as ocorrencias do nome do municipio da lista principal

    print("Arquivo escrito com sucesso!")

# calcula as metas de cada tribunal e retorna um objeto com as metas
def metas_tribunal_fun(linhas):
    linhas_temp = []

    for i in linhas:

        if linhas:
            sigla_tribunal = linhas[0].sigla_tribunal
            linhas_tribunal = [linha for linha in linhas if linha.sigla_tribunal == sigla_tribunal]

            #calculo de metas
            sum_julgados_2026 = sum(linha.julgados_2026 for linha in linhas_tribunal)
            sum_casos_novos_2026 = sum(linha.casos_novos_2026 for linha in linhas_tribunal)
            sum_dessobrestados_2026 = sum(linha.dessobrestados_2026 for linha in linhas_tribunal)
            sum_suspensos_2026 = sum(linha.suspensos_2026 for linha in linhas_tribunal)
            
            if (sum_casos_novos_2026 + sum_dessobrestados_2026 - sum_suspensos_2026) == 0:
                meta1_var = 0
            else: 
                meta1_var = sum_julgados_2026/(sum_casos_novos_2026 + sum_dessobrestados_2026 - sum_suspensos_2026)

            sum_julgm2_a = sum(linha.julgm2_a for linha in linhas_tribunal)
            sum_distm2_a = sum(linha.distm2_a for linha in linhas_tribunal)
            sum_suspm2_a = sum(linha.suspm2_a for linha in linhas_tribunal)

            if (sum_distm2_a-sum_suspm2_a) == 0:
                meta2a_var = 0
            else:
                meta2a_var = sum_julgm2_a/(sum_distm2_a-sum_suspm2_a)

            sum_julgm2_ant = sum(linha.julgm2_ant for linha in linhas_tribunal)
            sum_distm2_ant = sum(linha.distm2_ant for linha in linhas_tribunal)
            sum_suspm2_ant = sum(linha.suspm2_ant for linha in linhas_tribunal)
            sum_desom2_ant = sum(linha.desom2_ant for linha in linhas_tribunal)

            if (sum_distm2_ant-sum_suspm2_ant-sum_desom2_ant) == 0:
                meta2ant_var = 0
            else:
                meta2ant_var = sum_julgm2_ant/(sum_distm2_ant-sum_suspm2_ant-sum_desom2_ant)

            sum_julgm4_a = sum(linha.julgm4_a for linha in linhas_tribunal)
            sum_distm4_a = sum(linha.distm4_a for linha in linhas_tribunal)
            sum_suspm4_a = sum(linha.suspm4_a for linha in linhas_tribunal)

            if (sum_distm4_a-sum_suspm4_a) == 0:
                meta4a_var = 0
            else:
                meta4a_var = sum_julgm4_a/(sum_distm4_a-sum_suspm4_a)

            sum_julgm4_b = sum(linha.julgm4_b for linha in linhas_tribunal)
            sum_distm4_b = sum(linha.distm4_a for linha in linhas_tribunal)
            sum_suspm4_b = sum(linha.suspm4_b for linha in linhas_tribunal)

            if (sum_distm4_b-sum_suspm4_b) == 0:
                meta4b_var = 0
            else:
                meta4b_var = sum_julgm4_b/(sum_distm4_b-sum_suspm4_b)

            meta1_var = meta1_var *100
            meta2a_var = meta2a_var*1000/7
            meta2ant_var = meta2ant_var*100
            meta4a_var = meta4a_var*100
            meta4b_var = meta4b_var*100

            metas_tribunal = Meta_tribunal(sigla_tribunal,meta1_var,meta2a_var,meta2ant_var,meta4a_var,meta4b_var)
            linhas_temp.append(metas_tribunal)
            linhas = [linha for linha in linhas if linha.sigla_tribunal != sigla_tribunal] #apagar o tribunal da primeira lista

    return linhas_temp

def busca_municipio(linhas,nome_municipio):
    linhas_municipio = [linha for linha in linhas if linha.municipio_oj == nome_municipio] # coloca todas as ocorrencias do municipio em outra lista
    return linhas_municipio

def resumo_tribunal(linhas):    
  #organiza a lista pra agrupar os nomes de tribunal
    linhas = sorted(linhas, key=lambda p: p.sigla_tribunal)
    tribunal_metas = metas_tribunal_fun(linhas) #obtem asmetas por nome de tribunal
    tribunal_metas = sorted(tribunal_metas, key=lambda x: x.meta1, reverse=True) #coloca a lista em ordem decrescente
    
    with open('tribunal_metas.csv', 'a', encoding='utf-8') as file:
        file.write(f"sigla_tribunal,meta1,meta2a,meta2ant,meta4a,meta4b\n")
        for metas_tribunal in tribunal_metas:
            file.write(f"{metas_tribunal.sigla_tribunal},{metas_tribunal.meta1:.2f},{metas_tribunal.meta2a:.2f},{metas_tribunal.meta2ant:.2f},{metas_tribunal.meta4a:.2f},{metas_tribunal.meta4b:.2f}\n")

# --------------- função principal -------------------

#current_dir = os.getcwd()
#print(f"Diretorio atual: {current_dir}, para garantir o funcionamento do programa, certifique-se que existe uma pasta Banco de Dados contendo os arquivos a serem lidos neste diretório!\n")
linhas = concatenar_arquivos()
print("1: Concatenar arquivos\n2: Resumo por município\n3: Resumo por tribunal\n4: Buscar município\n")
op = input("Digite uma opção:")
# -------- menu ----------
match op:
    case "1":
        escrever_arquivo_inteiro(linhas)
    
    case "2":
        metas_resumo_municipio(linhas)

    case "3":
        resumo_tribunal(linhas)
    case "4":
        nome_municipio = input("Digite o nome de uma cidade: ")
        linhas = busca_municipio(linhas,nome_municipio)
        escrever_municipios(linhas,nome_municipio)
    case _:
        print("Opção inválida!")
