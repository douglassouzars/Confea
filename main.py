from tkinter import *
import customtkinter as ctk
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk
import re
from tkinter.filedialog import askopenfilename
from PyPDF2 import PdfReader
from tkinter import font
import locale
from datetime import datetime
from tkinter import messagebox
#import mysql.connector as mysql
import requests

import mysql.connector

root = Tk()


class App():
    con = None
    crea_entry = None
    nauto_entry = None
    def __init__(self):
        self.root = root
        self.tela()
        self.variaveis()
        self.cabecalho()
        #self.texto()
        self.consulta()
        #self.frames2()
        self.funcoes()
        self.botoes()
        self.logo()
        self.conteudo()


    def tela(self):
        """Definição da tela e sua cor total"""
        self.root.title("Sistema Confea")
        self.root.configure(background='#e8e8e8')
        self.root.geometry("1900x900")
        self.root.resizable(True, True)
        self.root.minsize(1000, 600)
        #con = mysql.connect(host='localhost',user='root',password='', database='python-tkinter')

    def variaveis(self):
        result="haha"
        texto_original = """Trata-se de recurso interposto ao Confea contra a decisão do Plenário do Crea-"""+ result +"""pela pessoa , CNPJ nº , autuada mediante o Auto de Infração n° , lavrado em , por infração , ao . (fls.  e Recurso)

        A Câmara Especializada de Modalidade analisou os autos e concluiu pela manutenção da autuação, expedindo a Decisão nº, de data. (fl. Decisão)

        O recurso do(a) interessado(a) ao Plenário do Crea foi julgado mediante a Decisão nº PL-, de data, que decidiu manter a autuação. (fl. Decisão)

        O(A) interessado(a) teve ciência da decisão do Plenário do Regional em data e protocolizou, em data, no Crea-UF, recurso ao Confea. (fls. AR e Recurso)

        OU

        Embora não conste do processo a informação da data em que o interessado(a) teve ciência da Decisão do Plenário do Regional, em data, foi protocolizado pelo interessado(a)/representante do interessado(a)/nome no Crea-UF recurso ao Confea. (fls. Recurso) 

        As folhas_entry citadas neste parecer são relativas ao número da página eletrônica no SEI - XXXXX. """
        return texto_original
    def cabecalho(self, select=2):
        self.tela()
        self.variaveis()

        """Header azul"""
        self.frame_1 = Frame(self.root)
        self.frame_1.configure(background='#4a8ad4')
        self.frame_1.place(relx=0.0, rely=0.0, relwidth=1, relheight=0.2)
        self.logo()

        """SubHeader cinza"""
        self.frame_3 = Frame(self.root)
        self.frame_3.configure(background='#adadad')
        self.frame_3.place(relx=0.0, rely=0.2, relwidth=1, relheight=0.05)

        """nav lateral azul"""
        self.frame_2 = Frame(self.root)
        self.frame_2.configure(background='#01509b')
        self.frame_2.place(relx=0.0, rely=0.25, relwidth=0.055, relheight=1)
        self.botoes()

    def consulta(self):
        """Caixa AI"""
        self.caixaai = Text(self.root, bg='white', fg='black', bd=2, font=('Times New Roman', 13))
        self.caixaai.insert(tk.INSERT,"                           AUTO DE INFRAÇÃO\nNº do Processo:\nArtigo:\nAutuado(a):\nCNPJ:\nFolhas:\nNº do AI:\nMulta:\nData:\nMotivo:")
        self.caixaai.place(relx=0.065, rely=0.26, relwidth=0.46, relheight=0.25)

        """Caixa CE"""
        self.caixace = Text(self.root, bg='white', fg='black', bd=2, font=('Times New Roman', 13))
        self.caixace.insert(tk.INSERT,"                           DECISÃO DA CÂMARA ESPECIALIZADA DO CREA\nFolhas:\nDecisão nº:\nEspecialidade:\nData:\nMulta:")
        self.caixace.place(relx=0.54, rely=0.26, relwidth=0.45, relheight=0.13)

        """Caixa PL"""
        self.caixapl = Text(self.root, bg='white', fg='black', bd=2, font=('Times New Roman', 13))
        self.caixapl.insert(tk.INSERT,"                           DECISÃO PLENÁRIO DO CREA\nFolhas:\nDecisão nº:\nData:\nMulta:")
        self.caixapl.place(relx=0.065, rely=0.52, relwidth=0.46, relheight=0.11)

        """Caixa AR"""
        self.caixaar = Text(self.root, bg='white', fg='black', bd=2, font=('Times New Roman', 13))
        self.caixaar.insert(tk.INSERT, "                           AVISO DE RECEBIMENTO\nFolhas:\nData:")
        self.caixaar.place(relx=0.54, rely=0.4, relwidth=0.22, relheight=0.07)

        """Caixa Tempestividade"""
        self.caixatempestividade = Text(self.root, bg='white', fg='black', bd=2, font=('Times New Roman', 13))
        self.caixatempestividade.insert(tk.INSERT,"                           INTEMPESTIVIDADE\nDentro do prazo:\nDias:")
        self.caixatempestividade.place(relx=0.77, rely=0.4, relwidth=0.22, relheight=0.07)

        """Caixa RECURSO"""
        self.caixarecurso = Text(self.root, bg='white', fg='black', bd=2, font=('Times New Roman', 13))
        self.caixarecurso.insert(tk.INSERT,"                           RECURSO AO CONFEA\nFolhas:\nData:\nContrato:\nJustificativa 1:")
        self.caixarecurso.place(relx=0.065, rely=0.64, relwidth=0.46, relheight=0.11)

        """Caixa ART"""
        self.caixaart = Text(self.root, bg='white', fg='black', bd=2, font=('Times New Roman', 13))
        self.caixaart.insert(tk.INSERT,"                           REGULARIZAÇÃO POR ANOTAÇÃO DE RESPONSABILIDADE TÉCNICA-ART\nFolhas:\nNº da ART:\nData:")
        self.caixaart.place(relx=0.54, rely=0.48, relwidth=0.45, relheight=0.09)

        """Caixa Comprovante de Cadastro Nacional de Pessoa Juridica"""
        self.caixacnpj = Text(self.root, bg='white', fg='black', bd=2, font=('Times New Roman', 13))
        self.caixacnpj.insert(tk.INSERT,"                           COMPROVANTE DE CADASTRO NACIONAL DE PESSOA JURÍDICA\nFolhas:\nData:\nCNAE Primário:\nCNAE Secundário:")
        self.caixacnpj.place(relx=0.54, rely=0.58, relwidth=0.45, relheight=0.11)

        """Caixa Reincidência"""
        self.caixareincidencia = Text(self.root, bg='white', fg='black', bd=2, font=('Times New Roman', 13))
        self.caixareincidencia.insert(tk.INSERT, "                           REINCIDÊNCIA\nFolhas:\nData:")
        self.caixareincidencia.place(relx=0.54, rely=0.7, relwidth=0.22, relheight=0.07)

        """Caixa Procuração"""
        self.caixaprocuracao = Text(self.root, bg='white', fg='black', bd=2, font=('Times New Roman', 13))
        self.caixaprocuracao.insert(tk.INSERT, "                           PROCURAÇÃO\nFolhas:\nNome:")
        self.caixaprocuracao.place(relx=0.77, rely=0.7, relwidth=0.22, relheight=0.07)

        """Caixa Texto
        self.caixatexto = Text(self.root, bg='white', fg='black', bd=2, font=('Times New Roman', 13))
        self.caixatexto.insert(tk.INSERT, self.variaveis())
        self.caixatexto.place(relx=0.065, rely=0.78, relwidth=0.925, relheight=0.2)
        self.conteudo()"""

    def botoes(self):
        # self.frames.caixas()

        """Barra de pesquisa"""
        lb_pes = Entry(self.frame_1, text="Digite sua busca aqui")
        lb_pes.configure(background='#fff', fg='black', font='Arial 10 ')
        lb_pes.place(relx=0.60, rely=0.4, relwidth=0.25, relheight=0.25)

        """Botao pesquisar"""
        btn_pes = ctk.CTkButton(self.frame_1, text='Pesquisar', fg_color='#fff', text_color='#000', font=('Arial', 14))
        btn_pes.place(relx=0.86, rely=0.4, relwidth=0.07, relheight=0.25)
        def tela_menu():
            self.pag59.place_forget()


        """Botao Menu"""
        btn_menu = ctk.CTkButton(self.frame_2, text='Menu', fg_color='#01509b', text_color='White',font=('Arial', 14), command=tela_menu)
        btn_menu.place(relx=0, rely=0, relwidth=1, relheight=0.08)

        """Botao Artigo 1"""
        btn_art1 = ctk.CTkButton(self.frame_2, text='Art 1º', fg_color='#01509b', text_color='White',font=('Arial', 14))
        btn_art1.place(relx=0, rely=0.08, relwidth=1, relheight=0.08)

        """Botao Artigo 6 A"""
        btn_art6a = ctk.CTkButton(self.frame_2, text='Art 6º a', fg_color='#01509b', text_color='White',font=('Arial', 14))
        btn_art6a.place(relx=0, rely=0.16, relwidth=1, relheight=0.08)

        """Botao Artigo 6 E"""
        btn_art6e = ctk.CTkButton(self.frame_2, text='Art 6º e', fg_color='#01509b', text_color='White',font=('Arial', 14))
        btn_art6e.place(relx=0, rely=0.24, relwidth=1, relheight=0.08)

        """Botao Artigo 16"""
        btn_art16 = ctk.CTkButton(self.frame_2, text='Art 16º', fg_color='#01509b', text_color='White',font=('Arial', 14))
        btn_art16.place(relx=0, rely=0.32, relwidth=1, relheight=0.08)

        """Botao Artigo 59"""

        btn_art59 = ctk.CTkButton(self.frame_2, text='Art 59º', fg_color='#01509b', text_color='White',font=('Arial', 14))
        btn_art59.place(relx=0, rely=0.4, relwidth=1, relheight=0.08)

        def tela_texto():

            self.caixaai.pack_forget()
            self.caixace.pack_forget()
            self.caixapl.pack_forget()
            self.caixaar.pack_forget()
            self.caixarecurso.pack_forget()
            self.caixatempestividade.pack_forget()
            self.caixaart.pack_forget()
            self.caixareincidencia.pack_forget()
            self.caixacnpj.pack_forget()
            self.caixaprocuracao.pack_forget()
            global crea_entry
            global nsei_ai
            global artigo_ai
            global autuado_ai
            global cnpj_cpf_ai
            global folhas_ai
            global nauto_ai
            global multa_ai
            global data_ai
            global motivo_ai
            global especialidade_ce
            global folhas_ce
            global ndecisao_ce
            global data_ce
            global folhas_pl
            global ndecisao_pl
            global data_pl
            global multa_pl
            global folhas_recurso
            global data_recurso
            global justifica_recurso
            global folhas_aviso
            global data_aviso
            global prazo
            global dias
            global folhas_art
            global n_art
            global data_art
            global folhas_cnpj
            global data_cnpj
            global cnae_primeiro
            global cnae_segundo
            global folhas_reincidencia
            global data_reincidencia
            global folhas_procuracao
            global nome_procuracao
            global folhas_alteracao
            global n_alteracao
            print("a data de aviso é?",folhas_aviso)

            self.pag59 = Text(self.root, bg='white', fg='black', bd=2, font=('Times New Roman', 13))
            self.pag59.tag_configure("red", foreground="red")
            self.pag59.insert(tk.INSERT,"""Trata-se de recurso interposto ao Confea contra a decisão do Plenário do Crea-""" + str(crea_entry) + """ pela pessoa """ + str(autuado_ai) + """, CNPJ nº ***""" + str(cnpj_cpf_ai) + """***, autuada mediante o Auto de Infração n° """ + str(nauto_ai) + """, lavrado em """ + str(data_ai) + """, por infração """ + str(artigo_ai) + """, ao """ + str(motivo_ai) + """. (fls.""" + str(folhas_ai) + """  e """ + str(folhas_recurso) + """)
            A Câmara Especializada de Modalidade analisou os autos e concluiu pela manutenção da autuação, expedindo a Decisão nº """ + str(ndecisao_ce) + """, de """ + str(data_ce) + """ (fl. Decisão)
            O recurso do(a) interessado(a) ao Plenário do Crea foi julgado mediante a Decisão nº """ + str(ndecisao_pl) + """, de """ + str(data_pl) + """, que decidiu manter a autuação. (fl. Decisão)
        
            O(A) interessado(a) teve ciência da decisão do Plenário do Regional em """ + str(data_aviso) + """ e protocolizou, em """ + str(data_recurso) + """, no Crea-UF, recurso ao Confea. (fls. AR e Recurso)
            Embora não conste do processo a informação da data em que o interessado(a) teve ciência da Decisão do Plenário do Regional, em """ + str(data_recurso) + """, foi protocolizado pelo interessado(a)/representante do interessado(a)/""" + str(nome_procuracao) + """ no Crea-UF recurso ao Confea. (fls. Recurso)

            As folhas citadas neste parecer são relativas ao número da página eletrônica no SEI - XXXXX.""")

            # Aplicar a formatação em vermelho às variáveis globais
            start_index = "1.0"
            while True:
                start_index = self.pag59.search(str(crea_entry), start_index, stopindex="end", regexp=False)
                if not start_index:
                    break
                end_index = self.pag59.index(f"{start_index}+{len(str(crea_entry))}c")
                self.pag59.tag_add("red", start_index, end_index)
                start_index = end_index

            start_index = "1.0"
            while True:
                start_index = self.pag59.search(str(autuado_ai), start_index, stopindex="end", regexp=False)
                if not start_index:
                    break
                end_index = self.pag59.index(f"{start_index}+{len(str(autuado_ai))}c")
                self.pag59.tag_add("red", start_index, end_index)
                start_index = end_index
            start_index = "1.0"
            while True:
                start_index = self.pag59.search(str(cnpj_cpf_ai), start_index, stopindex="end", regexp=False)
                if not start_index:
                    break
                end_index = self.pag59.index(f"{start_index}+{len(str(cnpj_cpf_ai))}c")
                self.pag59.tag_add("red", start_index, end_index)
                start_index = end_index
            start_index = "1.0"
            while True:
                start_index = self.pag59.search(str(nauto_ai), start_index, stopindex="end", regexp=False)
                if not start_index:
                    break
                end_index = self.pag59.index(f"{start_index}+{len(str(nauto_ai))}c")
                self.pag59.tag_add("red", start_index, end_index)
                start_index = end_index
            start_index = "1.0"
            while True:
                start_index = self.pag59.search(str(data_ai), start_index, stopindex="end", regexp=False)
                if not start_index:
                    break
                end_index = self.pag59.index(f"{start_index}+{len(str(data_ai))}c")
                self.pag59.tag_add("red", start_index, end_index)
                start_index = end_index
            start_index = "1.0"
            while True:
                start_index = self.pag59.search(str(artigo_ai), start_index, stopindex="end", regexp=False)
                if not start_index:
                    break
                end_index = self.pag59.index(f"{start_index}+{len(str(artigo_ai))}c")
                self.pag59.tag_add("red", start_index, end_index)
                start_index = end_index
            start_index = "1.0"
            while True:
                start_index = self.pag59.search(str(motivo_ai), start_index, stopindex="end", regexp=False)
                if not start_index:
                    break
                end_index = self.pag59.index(f"{start_index}+{len(str(motivo_ai))}c")
                self.pag59.tag_add("red", start_index, end_index)
                start_index = end_index
            start_index = "1.0"
            while True:
                start_index = self.pag59.search(str(folhas_ai), start_index, stopindex="end", regexp=False)
                if not start_index:
                    break
                end_index = self.pag59.index(f"{start_index}+{len(str(folhas_ai))}c")
                self.pag59.tag_add("red", start_index, end_index)
                start_index = end_index
            start_index = "1.0"
            while True:
                start_index = self.pag59.search(str(folhas_recurso), start_index, stopindex="end", regexp=False)
                if not start_index:
                    break
                end_index = self.pag59.index(f"{start_index}+{len(str(folhas_recurso))}c")
                self.pag59.tag_add("red", start_index, end_index)
                start_index = end_index

            self.pag59.place(relx=0.065, rely=0.26, relwidth=0.925, relheight=0.72)
            self.conteudo()
            self.botoes()


        """Botao Texto Padrao"""
        btn_textopadrao = ctk.CTkButton(self.frame_2, text='Texto', fg_color='#01509b', text_color='White',
                                        font=('Arial', 14), command=tela_texto)
        btn_textopadrao.place(relx=0, rely=0.48, relwidth=1, relheight=0.08)

    def valBarra(self, progress):
        self.varBarra.set(progress)
        self.root.update()

    def funcoes(self):
        def valBarra(self, progress):
            self.varBarra.set(progress)
            self.root.update()

        self.varBarra = DoubleVar()
        self.varBarra.set(0)

        self.barra = ttk.Progressbar(self.root, variable=self.varBarra, maximum=100)
        self.barra.place(relx=0.80, rely=0.98, relwidth=0.2, relheight=0.02)



    def logo(self):
        """definir a logo do projeto"""
        logoimg = Image.open("log.png")
        self.lg = ImageTk.PhotoImage(logoimg)
        self.lbl = tk.Label(self.frame_1, image=self.lg)
        self.lbl.place(relx=0.07, rely=0.1, relwidth=0.35, relheight=0.8)
        self.lbl.image = self.lg

        """consulta de acordo com crea_entrys TO/BA/PR"""
        #def crea_entrys():

    """def bancodedados(self):
        nauto = self.nauto.get()
        
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="senhateste",
            database='python-tkinter'
        )

        print(mydb)"""
    def conteudo(self):
        global con
        global crea_entry
        global nauto_entry
        crea_entry = ''
        nsei_entry = ''
        nauto_entry = ''

        """artigo = ' '
        autuado = ' '
        cnpj_cpf = ' '

        nauto = ' '
        multa = ' '
        data = ' '
        motivo = ' '
        folhas_entryce = ' '
        ndecisaoce = ' '
        especialidade = ' '
        datace = ' '
        multace = ' '
        folhas_entrypl = ' '
        ndecisaopl = ' '
        datapl = ' '
        multapl = ' '
        folharecurso = ' '
        datarecurso = ' '
        justificativa = ' '
        folhaaviso = ' '
        dataaviso = ' '
        prazo = ' '
        dias = ' '
        folhas_entryart = ' '
        nart = ' '
        dataart = ' '
        folhas_entrycnpj = ' '
        datacnpj = ' '
        cnaeprimeiro = ' '
        cnaesegundo = ' '
        folhas_entryreincidencia = ' '
        datareincidencia = ' '
        folhas_entryprocuracao = ' '
        nomeprocuracao = ' '
        folhas_entryalteracao = ' '
        nalteracao = ' '"""




        """limpar dados"""
        def limpar():
            """limpa o nome do arquivo"""
            lbl_selecionado = Label(self.frame_3)
            lbl_selecionado.config(text=" ", background='#adadad')
            lbl_selecionado.place(relx=0.25, rely=0.10, relwidth=0.3, relheight=0.80)
            """limpar barra"""
            self.varBarra.set(0)
            global nauto_ai
            global multa_ai
            global nsei_ai
            global autuado_ai
            global cnpj_cpf_ai
            global artigo_ai
            global motivo_ai
            global data_ai
            global folhas_ce
            global ndecisao_ce
            global especialidade_ce
            global data_ce
            global multa_ce
            global folhas_pl
            global ndecisao_pl
            global data_pl
            global multa_pl
            global folhas_recurso
            global data_recurso
            global justifica_recurso
            global folhas_aviso
            global data_aviso
            global prazo
            global dias
            global folhas_art
            global n_art
            global data_art
            global folhas_cnpj
            global data_cnpj
            global cnae_primeiro
            global cnae_segundo
            global folhas_reincidencia
            global data_reincidencia
            global folhas_procuracao
            global nome_procuracao
            global folhas_alteracao
            global n_alteracao


            nauto_ai = None
            multa_ai = None
            nsei_ai = None
            autuado_ai = None
            cnpj_cpf_ai = None
            artigo_ai = None
            motivo_ai = None
            data_ai = None
            folhas_ce = None
            ndecisao_ce = None
            especialidade_ce = None
            data_ce = None
            multa_ce = None
            folhas_pl = None
            ndecisao_pl = None
            data_pl = None
            multa_pl = None
            folhas_recurso = None
            data_recurso = None
            justifica_recurso = None
            folhas_aviso = None
            data_aviso = None
            prazo = None
            dias = None
            folhas_art = None
            n_art = None
            data_art = None
            folhas_cnpj = None
            data_cnpj = None
            cnae_primeiro = None
            cnae_segundo = None
            folhas_reincidencia = None
            data_reincidencia = None
            folhas_procuracao = None
            nome_procuracao = None
            folhas_alteracao = None
            n_alteracao = None

            """limpa as caixas do auto"""
            self.caixaai.delete("2.15", "2.80")
            self.caixaai.delete("3.7", "3.80")
            self.caixaai.delete("4.11", "4.80")
            self.caixaai.delete("5.5", "5.80")
            self.caixaai.delete("6.7", "6.80")
            self.caixaai.delete("7.9", "7.80")
            self.caixaai.delete("9.5", "9.80")
            self.caixaai.delete("10.7", "25.80")
            self.caixaai.delete("8.6", "8.99")
            """limpa as caixas da camara"""
            self.caixace.delete("2.7", "2.80")
            self.caixace.delete("3.11", "3.99")
            self.caixace.delete("4.14", "4.99")
            self.caixace.delete("5.5", "5.80")
            self.caixace.delete("6.6", "10.80")
            """limpa as caixas do plenario"""
            self.caixapl.delete("2.7", "2.80")
            self.caixapl.delete("3.11", "3.99")
            self.caixapl.delete("4.5", "4.80")
            self.caixapl.delete("5.6", "8.80")
            """limpa caixa de aviso"""
            self.caixaar.delete("2.7", "2.80")
            self.caixaar.delete("3.5", "3.80")
            """limpa caixa de recurso"""
            self.caixarecurso.delete("2.7", "2.80")
            self.caixarecurso.delete("3.5", "3.80")
            self.caixarecurso.delete("5.16","10.80")
            """limpar intempestividade"""
            self.caixatempestividade.delete("2.16", "2.80")
            self.caixatempestividade.delete("3.5", "3.80")
            """limpar art"""
            self.caixaart.delete("2.7", "2.80")
            self.caixaart.delete("3.11", "3.80")
            self.caixaart.delete("4.5", "4.80")
            """limpar comprovante de cnpj"""
            self.caixacnpj.delete("2.7", "2.80")
            self.caixacnpj.delete("3.5", "3.80")
            self.caixacnpj.delete("4.15", "4.80")
            """limpar reincidencia"""
            self.caixareincidencia.delete("2.7","2.80")
            """limpar procuraçao"""
            self.caixaprocuracao.delete("2.7", "2.80")
            """limpar texto padrao
            self.caixatexto.delete("1.0", tk.END)  # Limpa o texto atual da caixa de texto
            self.caixatexto.insert(tk.INSERT, self.variaveis())"""

        """selecionar o arquivo"""
        def selecionar_arquivo():
            global con
            global crea_entry

            lbl2_selecionado = Label(self.frame_1)
            lbl2_selecionado.config(text="  ", background='white')
            lbl2_selecionado.place(relx=0.395, rely=0.45, relwidth=0.025, relheight=0.09)
            lbl_selecionado = Label(self.frame_3)
            lbl_selecionado.config(text="  ", background='#adadad')
            lbl_selecionado.place(relx=0.45, rely=0.10, relwidth=0.15, relheight=0.80)
            limpar()
            file_path = askopenfilename(filetypes=[("Arquivos PDF", "*.pdf")], defaultextension=".pdf")
            """Escreve o nome do arquivo"""
            if file_path:
                partes = file_path.split("Downloads/")
                if len(partes) > 1:
                    depois_downloads = partes[1]
                lbl_selecionado = Label(self.frame_3)
                lbl_selecionado.config(text=depois_downloads, background='#adadad')
                lbl_selecionado.place(relx=0.25, rely=0.10, relwidth=0.3, relheight=0.80)
                # Abre o arquivo PDF em modo leitura binária
                with open(file_path, 'rb') as pdf_file:
                    # Cria um objeto PDFReader
                    pdf_reader = PdfReader(pdf_file)
                    num_pages = len(pdf_reader.pages)
                    """Descobre qual o CREA"""
                    for page_num in range(num_pages):
                        page = pdf_reader.pages[page_num]
                        text = page.extract_text()
                        match = re.search(r'\bCREA[/_-]([a-zA-Z]{2})', text)

                        if match:
                                crea_entry_result = match.group(1)
                                crea_entry = crea_entry_result.upper()
                                lbl2_selecionado = Label(self.frame_1)
                                lbl2_selecionado.config(text=crea_entry, background='#a1a1a1')
                                fonte = font.Font(size=18)
                                lbl2_selecionado["font"] = fonte
                                lbl2_selecionado.place(relx=0.395, rely=0.45, relwidth=0.025, relheight=0.09)

                                #crea_entry["crea_entry"]=crea_entry
                                #requests.session['crea_entry'] = crea_entry
                                #salvar(crea_entry)
                            #GRUPOS CREAS
                                print("1 passo: Procura qual crea_entry")
                                self.valBarra(5)
                                if crea_entry == "TO":
                                    print("2.1 passo: Achei qual o Crea")
                                    crea_entrys(pdf_file, num_pages,crea_entry)
                                elif crea_entry == "BA":
                                    print("2.2 passo: Achei qual o Crea")
                                    crea_entrys(pdf_file, num_pages,crea_entry)
                                elif crea_entry == "RN":
                                    print("2.3 passo: Achei qual o Crea")
                                    crea_entrys(pdf_file, num_pages,crea_entry)
                                elif crea_entry == "AM":
                                    print("2.4 passo: Achei qual o Crea")
                                    crea_entrys(pdf_file, num_pages,crea_entry)
                                #GRUPO CREAS2
                                elif crea_entry == "GO":
                                    print("2.5 passo: Achei qual o Crea")
                                    crea_entrysgo(pdf_file, num_pages, crea_entry)
                                # GRUPO CREAS2
                                elif crea_entry == "RS" or crea_entry == "MT":
                                    print("2.6 passo: Achei qual o Crea")
                                    crea_entrysrs(pdf_file, num_pages, crea_entry)
                                elif crea_entry == "RJ":
                                    print("2.7 passo: Achei qual o Crea")
                                    crea_entrysrj(pdf_file, num_pages, crea_entry)
                                elif crea_entry == 'SP':
                                    print("2.8 passo: Achei qual o Crea")
                                    crea_entryssp(pdf_file, num_pages, crea_entry)
                                break
                    #salvar(crea_entry)
                return pdf_reader
##########################################################################################################
#           CREAS TO BA RN AM PR
##########################################################################################################
        """CREAS= TO/BA/RN/AM"""
        def crea_entrys(pdf_file,num_pages,crea_entry):
            global con

            global nsei_ai
            global folhas_ai
            self.valBarra(10)
            print("3 passo: Procura a pagina do AUTO DE INFRAÇÃO")
            pdf_reader = PdfReader(pdf_file)
            for page_num in range(num_pages):
                page = pdf_reader.pages[page_num]
                text = page.extract_text()
                pagautuado = re.search(r'Autuado\(a\)', text)
                pagmulta = re.search(r'Multa', text)
                result_nsei_entry = re.search(r'Nº(.*)', text)
                """Pagina do Auto de infração"""
                if (pagautuado and pagmulta) and result_nsei_entry:
                    self.valBarra(15)
                    print("4 passo: Achei a pagina do AUTO DE INFRAÇÃO")
                    folhas_ai = page_num + 1
                    #cursor = con.cursor()
                    #cursor.execute("INSERT INTO dados (folhas) VALUES (%s)", (folhas_entry,))
                    #con.commit()
                    nsei_ai = result_nsei_entry.group(1)
                    #cursor = con.cursor()
                    #cursor.execute("INSERT INTO dados (nsei) VALUES (%s)", (nsei_entry,))
                    #con.commit()
                    """Inserir numero do Processo SEI"""
                    self.caixaai.insert("2.16", nsei_ai, "red")  # Adiciona a tag "red" ao novo valor
                    self.caixaai.tag_config("red", foreground="red")
                    #salvar(nsei_entry)
                    """Inserir folha do AUTO DE INFRAÇÃO"""
                    self.caixaai.insert("6.11", folhas_ai, "red")  # Adiciona a tag "red" ao novo valor
                    self.caixaai.tag_config("red", foreground="red")  # Configura a cor vermelha para a tag "red"
                   # salvar(folhas_entry)
#                    self.caixatexto.insert("1.185", folhas_entry, "red")
#                    self.caixatexto.tag_config("red", foreground="red")
                    pagedoauto(folhas_ai, pdf_file,num_pages,crea_entry)
                    break


        """EXTRAINDO DADOS DO AUTO DE INFRAÇÃO"""
        def pagedoauto(folhas_ai, pdf_file,num_pages,crea_entry):
            self.valBarra(20)
            global nauto_ai
            global multa_ai
            global autuado_ai
            global cnpj_cpf_ai
            global artigo_ai
            global motivo_ai
            global data_ai
            print("5 passo: Procura todos os dados do AUTO DE INFRAÇÃO")
            pdf_reader = PdfReader(pdf_file)
            page = pdf_reader.pages[folhas_ai - 1]
            text = page.extract_text()
            """Extrai o artigo"""
            artigo = re.search(r'Infração:(.{39})', text)
            artigo2 = re.search(r'Infração: FALTA DE REGISTRO(.{29})', text)
            """Extrai o valor da multa"""
            multa = re.search(r'Multa de(.*)', text)

            """Extrai a data do auto"""
            data = re.search(r'em (\d{2})/(\d{2})/(\d{4})', text)
            """Extrai o NUMERO DO AUTO"""
            nauto = re.search(r'Nº(.*)', text)
            """Extrai o NOME DO AUTUADO"""
            autuado = re.search(r'(.*)Autuado\(a\)', text)
            """Extrai o CNPJ"""
            cnpj = re.search(r'\*{3}(\d+\.\d+)\*{3}', text)

            cnpj2= re.search(r'(\d{2})\.(\d{3})\.(\d{3})/(\d{4})-(\d{2})',text)
            """Extrai o motivo do AUTO"""
            desc_pos = text.find("DESCRIÇÃO")
            action_pos = text.find("Tipo de Ação Fiscalizatória")
            extracted_text = text[desc_pos + len("DESCRIÇÃO"):action_pos].strip()
            melhora_motivo = extracted_text.replace("\n", "")
            print("6 passo: Achei todos os dados do AUTO DE INFRAÇÃO")
            self.valBarra(25)
            if cnpj:
                cnpj_cpf_ai = cnpj.group(1)
                self.caixaai.insert("5.6", f"***{cnpj_cpf_ai}***", "red")
                self.caixaai.tag_config("red", foreground="red")
            elif cnpj2:
                cnpj_cpf_ai = cnpj2.group()
                self.caixaai.insert("5.6", f"***{cnpj_cpf_ai}***", "red")
                self.caixaai.tag_config("red", foreground="red")
            #
            #                    self.caixatexto.insert("1.103", f"***{result_cnpj}***", "red")
#                    self.caixatexto.tag_config("red", foreground="red")
            if data:
                configdata(data)

            if nauto:
                nauto_ai = nauto.group(1)
                self.caixaai.insert("7.10", nauto_ai, "red")  # Adiciona a tag "red" ao novo valor
                self.caixaai.tag_config("red", foreground="red")
 #                self.caixatexto.insert("1.156", str(result_nauto), "red")
#                   self.caixatexto.tag_config("red", foreground="red")
            if multa:
                multa_ai = multa.group(1)
                self.caixaai.insert("8.7", multa_ai, "red")  # Adiciona a tag "red" ao novo valor
                self.caixaai.tag_config("red", foreground="red")

#                   self.caixatexto.insert("1.360", str(result_multa), "red")
#                   self.caixatexto.tag_config("red", foreground="red")

            if autuado:
                result_autuado = autuado.group(1)
                autuado_ai = result_autuado.title()
                self.caixaai.insert("4.12", autuado_ai, "red")  # Adiciona a tag "red" ao novo valor
                self.caixaai.tag_config("red", foreground="red")
#                self.caixatexto.insert("1.93", str(result_autuado_min), "red")
#                self.caixatexto.tag_config("red", foreground="red")
            if artigo:
                result_artigo = artigo.group(1)
                if "LEIGA" in result_artigo:
                    artigo_ai = 'a alinea "a" Art. 6º da Lei Federal 5.194, de 1966'
                    self.caixaai.insert("3.8", str('a alinea "a" Art. 6º da Lei Federal 5.194, de 1966'),"red")  # Adiciona a tag "red" ao novo valor
                    self.caixaai.tag_config("red", foreground="red")
#                    self.caixatexto.insert("1.275", str('a alinea "a" Art. 6º da Lei Federal 5.194, de 1966'), "red")
#                    self.caixatexto.tag_config("red", foreground="red")
                elif "SEM REGISTRO" in result_artigo:
                    artigo_ai ="Art. 59º da Lei Federal 5.194, de 1966"
                    self.caixaai.insert("3.8", str("Art. 59º da Lei Federal 5.194, de 1966"), "red")  # Adiciona a tag "red" ao novo valor
                    self.caixaai.tag_config("red", foreground="red")
#                    self.caixatexto.insert("1.275", str("ao art. 59º da Lei Federal 5.194, de 1966"), "red")
#                    self.caixatexto.tag_config("red", foreground="red")
                elif "FALTA DE REGISTRO" in result_artigo:
                    artigo_ai="Art. 59º da Lei Federal 5.194, de 1966"
                    self.caixaai.insert("3.8", str("Art. 59º da Lei Federal 5.194, de 1966"), "red")  # Adiciona a tag "red" ao novo valor
                    self.caixaai.tag_config("red", foreground="red")
#                    self.caixatexto.insert("1.275", str("ao art. 59º da Lei Federal 5.194, de 1966"), "red")
#                    self.caixatexto.tag_config("red", foreground="red")
                elif "CANCELADO" in result_artigo:
                    artigo_ai="Art. 64º da Lei Federal 5.194, de 1966"
                    self.caixaai.insert("3.8", str("Art. 64º da Lei Federal 5.194, de 1966"), "red")  # Adiciona a tag "red" ao novo valor
                    self.caixaai.tag_config("red", foreground="red")
#                   self.caixatexto.insert("1.275", str("Art. 64º da Lei Federal 5.194, de 1966"), "red")
#                    self.caixatexto.tag_config("red", foreground="red")

            if melhora_motivo:
                motivo_ai = melhora_motivo.lower()
                self.caixaai.insert("10.10", motivo_ai, "red")
                self.caixaai.tag_config("red", foreground="red")
#                self.caixatexto.insert("1.360", melhora_motivo_min, "red")
#                self.caixatexto.tag_config("red", foreground="red")
            ce(pdf_reader,folhas_ai,crea_entry, pdf_file, num_pages)

##########################################################################################################
#           TODOS AS PAGINAS DA CAMARA ESPECIALIZADA
##########################################################################################################
        """Descobre qual a pagina da Camara Especializada"""
        def ce(pdf_reader, folhas_ai,crea_entry, pdf_file, num_pages):
            self.valBarra(30)
            global especialidade_ce
            global folhas_ce
            global ndecisao_ce
            global data_ce
            print("7 passo: Procurar a pagina da DECISAO DA CAMARA ESPECIALIZADA")

            for page_num in range(folhas_ai, len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                text2 = page.extract_text()

                pagdecisaocamarago2 = re.search(r'\bDECISÃO DE REUNIÃO\b(.*)', text2)
                pagdecisaocamara = re.search(r'\bEspecializada \b(.*?)(?:\n.*?\bdo \b)', text2)

                pagdecisaocamarago = re.search(r'A Câmara Especializada (.*)do Conselho', text2)
                pagdecisaocamaraam = re.search(r'\bA Reunião\b(.*)\bdo Conselho\b', text2)
                pagdecisaocamarasp = re.search(r'A Câmara Especializada , reunida ',text2)
                pagdecisaocamararj = re.search(r"A Câmara Especializada de (.*) - ",text2)
                self.valBarra(35)
                print(pagdecisaocamararj)

                if pagdecisaocamarasp:
                    print("8 passo: Achei a pagina da DECISAO DA CAMARA ESPECIALIZADA")
                    print("9.1 passo: Procura os dados da DECISAO DA CAMARA ESPECIALIZADA")

                    print("10.1 passo: Achei os dados da DECISAO DA CAMARA ESPECIALIZADA")
                    result_pagdecisaocamara = pagdecisaocamarasp.group(1)
                    self.caixace.insert("4.15", result_pagdecisaocamara, "red")  # Adiciona a tag "red" ao novo valor
                    self.caixace.tag_config("red", foreground="red")  # Configura a cor vermelha para a tag "red"
                    pag_ce = page_num + 1
                    # Inserir o novo valor extraído do PDF no widget Text
                    self.caixace.insert("2.8", str(pag_ce), "red")  # Adiciona a tag "red" ao novo valor
                    self.caixace.tag_config("red", foreground="red")  # Configura a cor vermelha para a tag "red"
                    page2 = pdf_reader.pages[page_num]
                    text3 = page2.extract_text()
                    ndecisaoce = re.search(r'CE\w+/SP n[O^°ººo]\s?(\d+/\s?\d+)', text2)
                    print("10.3 passo: Achei os dados da DECISAO DA CAMARA ESPECIALIZADA")
                    if ndecisaoce:
                        result_ndecisaoce = ndecisaoce.group(1)
                        self.caixace.insert("3.12", result_ndecisaoce, "red")  # Adiciona a tag "red" ao novo valor
                        self.caixace.tag_config("red", foreground="red")  # Configura a cor vermelha para a tag "red"
                    if crea_entry == "SP":
                        for page_num in range(pag_ce, len(pdf_reader.pages)):
                            page = pdf_reader.pages[page_num-1]
                            text4 = page.extract_text()
                            datato = re.search(r',[ ^]/de [A-Z][a-z]+ de (\d{4})', text4)
                            if datato:
                                result_datato = datato.group()
                                self.caixace.insert("5.6", result_datato, "red")  # Adiciona a tag "red" ao novo valor
                                self.caixace.tag_config("red", foreground="red")
                                break
                    multa(pdf_reader, pag_ce, crea_entry, pdf_file, num_pages)
                    break
                if pagdecisaocamaraam:
                    print("8 passo: Achei a pagina da DECISAO DA CAMARA ESPECIALIZADA")
                    print("9.1 passo: Procura os dados da DECISAO DA CAMARA ESPECIALIZADA")
                    pagdecisaocamara = pagdecisaocamaraam
                    print("10.1 passo: Achei os dados da DECISAO DA CAMARA ESPECIALIZADA")
                    result_pagdecisaocamara = pagdecisaocamara.group(1)
                    self.caixace.insert("4.15", result_pagdecisaocamara, "red")  # Adiciona a tag "red" ao novo valor
                    self.caixace.tag_config("red", foreground="red")  # Configura a cor vermelha para a tag "red"
                    pag_ce = page_num + 1
                    # Inserir o novo valor extraído do PDF no widget Text
                    self.caixace.insert("2.8", str(pag_ce), "red")  # Adiciona a tag "red" ao novo valor
                    self.caixace.tag_config("red", foreground="red")  # Configura a cor vermelha para a tag "red"
                    page2 = pdf_reader.pages[page_num]
                    text3 = page2.extract_text()
                    ndecisaoce = re.search(r'Decisão:(.+)', text2)
                    print("10.3 passo: Achei os dados da DECISAO DA CAMARA ESPECIALIZADA")
                    if ndecisaoce:
                        result_ndecisaoce = ndecisaoce.group(1)
                        self.caixace.insert("3.12", result_ndecisaoce, "red")  # Adiciona a tag "red" ao novo valor
                        self.caixace.tag_config("red", foreground="red")  # Configura a cor vermelha para a tag "red"
                    if crea_entry == "TO":
                        for page_num in range(pag_ce, len(pdf_reader.pages)):
                            page = pdf_reader.pages[page_num]
                            text4 = page.extract_text()
                            datato = re.search(r'\/TO, (.+)\.', text4)
                            if datato:
                                result_datato = datato.group(1)
                                self.caixace.insert("5.6", result_datato, "red")  # Adiciona a tag "red" ao novo valor
                                self.caixace.tag_config("red", foreground="red")
                                break
                    if crea_entry == "BA":
                        data3 = re.search(r', (\d{2}) de (\d{2}) de (\d{4})\.', text3)
                        if data3:
                            result_data3 = data3.group(1)
                            self.caixace.insert("5.6", result_data3, "red")  # Adiciona a tag "red" ao novo valor
                            self.caixace.tag_config("red", foreground="red")
                        data2 = re.search(r'- (\d{2})/(\d{2})/(\d{4})', text3)
                        if data2:
                            configdata2(data2)
                        multa(pdf_reader, pag_ce, crea_entry, pdf_file)
                        break
                    if crea_entry == "AM":
                        for page_num in range(pag_ce, len(pdf_reader.pages)):
                            page = pdf_reader.pages[page_num-1]
                            text4 = page.extract_text()
                            data2 = re.search(r'- (\d{2})/(\d{2})/(\d{4})', text4)
                            if data2:
                                configdata2(data2)
                                break
                    multa(pdf_reader, pag_ce, crea_entry, pdf_file, num_pages)
                    break
                if (pagdecisaocamarago or pagdecisaocamarago2 or pagdecisaocamararj) and (crea_entry == 'GO' or crea_entry == 'RJ' or crea_entry == 'BA' or crea_entry =='RN' or crea_entry =='RS'  or crea_entry =='TO'):
                    if pagdecisaocamarago2:
                        print("v1")
                        pagdecisaocamarago3 = re.search(r'A Câmara Especializada de (.*) do', text2)
                        if pagdecisaocamarago3:
                            especialidade_ce = pagdecisaocamarago3.group(1)
                            self.caixace.insert("4.15", especialidade_ce,"red")  # Adiciona a tag "red" ao novo valor
                            self.caixace.tag_config("red", foreground="red")  # Configura a cor vermelha para a tag "red"

                        pagdecisaocamarago = pagdecisaocamarago2
                    if crea_entry == "TO":
                        pag_ce = page_num + 1
                        for page_num in range(pag_ce, len(pdf_reader.pages)):
                            page = pdf_reader.pages[page_num]
                            text4 = page.extract_text()
                            datato = re.search(r'\/TO, (.+)\.', text4)
                            if datato:
                                result_datato = datato.group(1)
                                self.caixace.insert("5.6", result_datato, "red")  # Adiciona a tag "red" ao novo valor
                                self.caixace.tag_config("red", foreground="red")
                                break
                    print("8 passo: Achei a pagina da DECISAO DA CAMARA ESPECIALIZADA")
                    print("9.2 passo: Procura os dados da DECISAO DA CAMARA ESPECIALIZADA")
                    if pagdecisaocamarago:
                        print("v3")
                        especialidade_ce = pagdecisaocamarago.group(1)
                    if pagdecisaocamararj:
                        print("v2")
                        especialidade_ce = pagdecisaocamararj.group()
                    self.caixace.insert("4.15", especialidade_ce, "red")  # Adiciona a tag "red" ao novo valor
                    self.caixace.tag_config("red", foreground="red")  # Configura a cor vermelha para a tag "red"
                    folhas_ce = page_num + 1

                    self.caixace.insert("2.8", folhas_ce, "red")  # Adiciona a tag "red" ao novo valor
                    self.caixace.tag_config("red", foreground="red")  # Configura a cor vermelha para a tag "red"
                    page2 = pdf_reader.pages[page_num]
                    text3 = page2.extract_text()

                    if crea_entry == 'RJ':
                        ndecisaoce = re.search(r"CE\w+/RJ n[ººOo]\s?(\d+/\s?\d+)", text3)
                        ndecisaoce2 = re.search(r"CE\w+/RJ n° \d+/\s?\d+", text3)
                        if ndecisaoce2:
                            print(ndecisaoce2)
                            ndecisao_ce = ndecisaoce2.group()
                        elif ndecisaoce:
                            result_ndecisaoce = ndecisaoce.group(1)
                            ndecisao_ce = result_ndecisaoce

                        self.valBarra(25)
                        self.caixace.insert("3.12", ndecisao_ce,"red")  # Adiciona a tag "red" ao novo valor
                        self.caixace.tag_config("red", foreground="red")
                    ndecisaoce = re.search(r'Decisão:(.+)', text2)


                    datace = re.search(r', (\d{2}) de (.*) de (\d{4})', text3)
                    datace2= re.search(r', (\d{1})(.*) de (\d{4}).',text3)
                    if datace2:
                        print(datace2)
                        datace = datace2
                    print("10.2 passo: Achei os dados da DECISAO DA CAMARA ESPECIALIZADA")
                    if ndecisaoce:
                        result_ndecisaoce = ndecisaoce.group(1)
                        self.caixace.insert("3.12", result_ndecisaoce, "red")  # Adiciona a tag "red" ao novo valor
                        self.caixace.tag_config("red", foreground="red")
                    if datace and (crea_entry != "TO"):
                        print("nao pode")
                        result_datace = datace.group()
                        result_data_ce = re.search(r'\d.*', result_datace)
                        if result_data_ce:
                            data_ce = result_data_ce.group()
                            self.caixace.insert("5.6", data_ce, "red")  # Adiciona a tag "red" ao novo valor
                            self.caixace.tag_config("red", foreground="red")
                    multa(pdf_reader, folhas_ce, crea_entry, pdf_file,num_pages)
                    break

                if (pagdecisaocamara and (crea_entry == 'MT')):
                    print("8 passo: Achei a pagina da DECISAO DA CAMARA ESPECIALIZADA")
                    print("9.3 passo: Procura os dados da DECISAO DA CAMARA ESPECIALIZADA")
                    result_pagdecisaocamara = pagdecisaocamara.group(1)
                    self.caixace.insert("4.15", result_pagdecisaocamara, "red")  # Adiciona a tag "red" ao novo valor
                    self.caixace.tag_config("red", foreground="red")  # Configura a cor vermelha para a tag "red"
                    pag_ce = page_num + 1
                    # Inserir o novo valor extraído do PDF no widget Text
                    self.caixace.insert("2.8", str(pag_ce), "red")  # Adiciona a tag "red" ao novo valor
                    self.caixace.tag_config("red", foreground="red")  # Configura a cor vermelha para a tag "red"
                    page2 = pdf_reader.pages[page_num]
                    text3 = page2.extract_text()

                    ndecisaoce = re.search(r'Decisão:(.+)', text2)
                    ndecisaoce2 = re.search(r'Decis([^n]+n°[^ ]+)', text2)
                    print("10.3 passo: Achei os dados da DECISAO DA CAMARA ESPECIALIZADA")
                    if ndecisaoce or ndecisaoce2:
                        if ndecisaoce:
                            result_ndecisaoce = ndecisaoce.group(1)
                        if ndecisaoce2:
                            result_ndecisaoce = ndecisaoce2.group(1)
                        self.caixace.insert("3.12", result_ndecisaoce, "red")  # Adiciona a tag "red" ao novo valor
                        self.caixace.tag_config("red", foreground="red")  # Configura a cor vermelha para a tag "red"

                    if crea_entry == "BA":
                        data3 = re.search(r', (\d{2}) de (\d{2}) de (\d{4})\.', text3)
                        if data3:

                            result_data3 = data3.group(1)
                            self.caixace.insert("5.6", result_data3, "red")  # Adiciona a tag "red" ao novo valor
                            self.caixace.tag_config("red", foreground="red")
                        data2 = re.search(r'- (\d{2})/(\d{2})/(\d{4})', text3)
                        if data2:
                            configdata2(data2)
                    if crea_entry == "GO":
                        datace = re.search(r', (\d{2}) de (.*) de (\d{4})', text3)
                        result_datace = datace.group()
                        result_datace_real = result_datace[2:]
                        self.caixace.insert("5.6", result_datace_real, "red")  # Adiciona a tag "red" ao novo valor
                        self.caixace.tag_config("red", foreground="red")
                    if crea_entry == "MT":
                        datace = re.search(r'MT no dia (\d{2}) de (.*) de (\d{4})', text3)
                        result_datace = datace.group()
                        result_datace_real = result_datace[2:]
                        self.caixace.insert("5.6", result_datace_real, "red")  # Adiciona a tag "red" ao novo valor
                        self.caixace.tag_config("red", foreground="red")
                    if crea_entry == "RS":
                            decisao_desc_pos = text3.find(" - CE")
                            decisao_action_pos = text3.find("Referência")
                            extractedrs_text = text3[decisao_desc_pos + len(" - CE"):decisao_action_pos].strip()
                            melhora_decisao = extractedrs_text.replace("\n", "")
                            print("oi")
                            self.valBarra(25)
                            if melhora_decisao:
                                self.caixace.insert("3.12", "CE" + melhora_decisao, "red")  # Adiciona a tag "red" ao novo valor
                                self.caixace.tag_config("red", foreground="red")
                                for page_num in range(pag_ce, len(pdf_reader.pages)):
                                    page = pdf_reader.pages[page_num - 1]
                                    text4 = page.extract_text()
                                    datacers = re.search(r', (\d{2}) de (.*) de (\d{4})\.', text4)


                                    if datacers:
                                        result_datacers = datacers.group()
                                        result_datacers_real = result_datacers[2:]
                                        self.caixace.insert("5.6", result_datacers_real,"red")  # Adiciona a tag "red" ao novo valor
                                        self.caixace.tag_config("red", foreground="red")
                                        break


                    multa(pdf_reader, pag_ce,crea_entry,pdf_file, num_pages)
                    break


        """Descobrindo a Data"""
        def configdata2(data2):
            dia2 = data2.group(1)
            mes2 = data2.group(2)
            ano2 = data2.group(3)
            if mes2 == '01':
                mes_escrito2 = "janeiro"
                configmes2(dia2,mes_escrito2,ano2)
            elif mes2 == '02':
                mes_escrito2 = "fevereiro"
                configmes2(dia2,mes_escrito2,ano2)
            elif mes2 == '03':
                mes_escrito2 = "março"
                configmes2(dia2,mes_escrito2,ano2)
            elif mes2 == '04':
                mes_escrito2 = "abril"
                configmes2(dia2,mes_escrito2,ano2)
            elif mes2 == '05':
                mes_escrito2 = "maio"
                configmes2(dia2,mes_escrito2,ano2)
            elif mes2 == '06':
                mes_escrito2 = "junho"
                configmes2(dia2,mes_escrito2,ano2)
            elif mes2 == '07':
                mes_escrito2 = "julho"
                configmes2(dia2,mes_escrito2,ano2)
            elif mes2 == '08':
                mes_escrito2 = "agosto"
                configmes2(dia2,mes_escrito2,ano2)
            elif mes2 == '09':
                mes_escrito2 = "setembro"
                configmes2(dia2,mes_escrito2,ano2)
            elif mes2 == '10':
                mes_escrito2 = "outubro"
                configmes2(dia2,mes_escrito2,ano2)
            elif mes2 == '11':
                mes_escrito2 = "novembro"
                configmes2(dia2,mes_escrito2,ano2)
            elif mes2 == '12':
                mes_escrito2 = "dezembro"
                configmes2(dia2,mes_escrito2,ano2)
        """Exibindo a data"""
        def configmes2(dia2,mes_escrito2,ano2):
            self.valBarra(40)
            data_formatada2 = f"{dia2} de {mes_escrito2} de {ano2}"
            if data_formatada2:
                self.caixace.insert("5.6", str(data_formatada2), "red")  # Adiciona a tag "red" ao novo valor
                self.caixace.tag_config("red", foreground="red")



        def multa(pdf_reader, folhas_ce,crea_entry, pdf_file, num_pages):
            self.valBarra(45)
            global multa_ce
            if crea_entry == 'GO' or crea_entry == "AM"  or crea_entry == "BA" or crea_entry == "MT" or crea_entry == 'RN' or crea_entry == 'RJ' or crea_entry == 'SP':
                for page_num in range(folhas_ce, len(pdf_reader.pages)):
                    page = pdf_reader.pages[page_num - 1]
                    text3 = page.extract_text()

                    multacego_action_pos = text3.find("Coordenou ")
                    multacego_action_pos2 = text3.find(". Presidiu")
                    multacego_desc_pos = text3.find("DECIDIU[: ] ")
                    if multacego_action_pos != -1:
                        multacego_extracted_text = text3[multacego_desc_pos + len("DECIDIU[: ] "):multacego_action_pos].strip()
                        multacego_melhora = multacego_extracted_text.replace("\n", "")

                        if multacego_melhora:
                                if 'redução' in multacego_melhora or 'MINIMO' in multacego_melhora:
                                    multa_ce = 'reduziu'
                                    self.caixace.insert("6.6", "reduziu","red")  # Adiciona a tag "red" ao novo valor
                                    self.caixace.tag_config("red", foreground="red")
                                elif "manutenção"in multacego_melhora or "Manutenção" in multacego_melhora or "MANUTENÇÃO" in multacego_melhora:
                                    multa_ce = 'manteve'
                                    self.caixace.insert("6.6", "manteve","red")  # Adiciona a tag "red" ao novo valor
                                    self.caixace.tag_config("red", foreground="red")
                        break
                    elif multacego_action_pos2 != -1:
                        multacego_extracted_text = text3[multacego_desc_pos + len(" DECIDIU[: ] "):multacego_action_pos2].strip()
                        multacego_melhora = multacego_extracted_text.replace("\n", "")

                        if multacego_melhora:
                            if "redução" in multacego_melhora:
                                multa_ce = 'reduziu'
                                self.caixace.insert("6.6", "reduziu","red")  # Adiciona a tag "red" ao novo valor
                                self.caixace.tag_config("red", foreground="red")
                            elif "manutenção" in multacego_melhora or 'manutenção' in multacego_melhora  or "MANUTENÇÃO" in multacego_melhora:
                                multa_ce = 'manteve'
                                self.caixace.insert("6.6", "manteve","red")  # Adiciona a tag "red" ao novo valor
                                self.caixace.tag_config("red", foreground="red")
                        break
                plcrea_entry(pdf_reader, folhas_ce,crea_entry, pdf_file,num_pages)
            elif crea_entry == 'TO':
                for page_num in range(folhas_ce, len(pdf_reader.pages)):
                    page = pdf_reader.pages[page_num - 1]
                    text3 = page.extract_text()

                    multacego_action_pos = text3.find("Coordenou")
                    #multacego_action_pos2 = text3.find("")
                    multacego_desc_pos = text3.find(", voto pela ")

                    if multacego_action_pos != -1:

                        multacego_extracted_text = text3[multacego_desc_pos + len(", voto pela "):multacego_action_pos].strip()
                        multacego_melhora = multacego_extracted_text.replace("\n", "")

                        if multacego_melhora:
                            if "redução" in multacego_melhora:
                                self.caixace.insert("6.6", "reduziu para valor minimo",
                                                    "red")  # Adiciona a tag "red" ao novo valor
                                self.caixace.tag_config("red", foreground="red")
                            elif "manutenção" in multacego_melhora:
                                self.caixace.insert("6.6", "manteve o valor da multa",
                                                    "red")  # Adiciona a tag "red" ao novo valor
                                self.caixace.tag_config("red", foreground="red")
                        break

                plcrea_entry(pdf_reader, folhas_ce,crea_entry, pdf_file, num_pages)


        """Descobre qual a pagina da Decisao Plenaria"""
        def plcrea_entry(pdf_reader, folhas_ce,crea_entry, pdf_file, num_pages):
            self.valBarra(50)
            global folhas_pl
            global ndecisao_pl
            global data_pl
            print("11 passo: Procurar a pagina da DECISAO PLENARIA")
            for page_num in range(folhas_ce, len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                text3 = page.extract_text()

                pagdecisaoplenaria = re.search(r'\bO (Plen[áa]rio|Plendrio|Plenario) do Conselho Regional \b(.*)', text3)
                pagdecisaoplenariaerro = None
                if crea_entry == "RJ":
                    pagdecisaoplenariaerro = re.search(r'PL/RJ n[ººOo] (\d+/\d+)', text3)
                    if pagdecisaoplenariaerro:
                        folhas_pl = page_num + 1
                        print("hello")
                        self.caixapl.insert("2.8",folhas_pl, "red")  # Adiciona a tag "red" ao novo valor
                        self.caixapl.tag_config("red", foreground="red")
                if pagdecisaoplenaria:

                    print("12 passo: Achei a pagina da decisao do plenario")
                    page2 = pdf_reader.pages[page_num]
                    text4 = page2.extract_text()
                    folhas_pl = page_num + 1
                    if pagdecisaoplenariaerro is None:

                        print("hello2")
                        self.caixapl.insert("2.8", folhas_pl, "red")  # Adiciona a tag "red" ao novo valor
                        self.caixapl.tag_config("red", foreground="red")
                    #self.caixapl.insert("2.8", str(pag_pl), "red")  # Adiciona a tag "red" ao novo valor
                    #self.caixapl.tag_config("red", foreground="red")

                    ndecisaopl2 = re.search(r'Decisão:(.+)', text3)
                    ndecisaopl4 = re.search(r'Decisão Plenária:(.+)', text4)
                    ndecisaopl = re.search(r'Decisão Plenária\s*:\s*(?:PL/BA\s+)?Nº\s*(\d+/\d+)', text4)
                    ndecisaopl5 = re.search(r'DECISAO:(.+)', text3)
                    ndecisaopl3 = re.search(r'Decisão N\.:(.+)', text3)
                    ndecisaopl7 = re.search(r'Decisão PL/SP n[- ](.+)',text3)
                    if pagdecisaoplenariaerro is None:
                        ndecisaopl6 = re.search(r'Decisão Plenária (.+)',text4)
                    else:
                        ndecisaopl6 = pagdecisaoplenariaerro
                    print("13 passo: Procura dados da DECISAO PLENARIA")
                    if ndecisaopl:
                        print("1")
                        result_ndecisaopl = ndecisaopl.group(1)
                        self.caixapl.insert("3.12", result_ndecisaopl, "red")  # Adiciona a tag "red" ao novo valor
                        self.caixapl.tag_config("red", foreground="red")
                    elif ndecisaopl2:
                        print("2")
                        result_ndecisaopl = ndecisaopl2.group(1)
                        self.caixapl.insert("3.12", result_ndecisaopl, "red")  # Adiciona a tag "red" ao novo valor
                        self.caixapl.tag_config("red", foreground="red")
                    elif ndecisaopl3:
                        print("3")
                        result_ndecisaopl = ndecisaopl3.group(1)
                        self.caixapl.insert("3.12", result_ndecisaopl, "red")  # Adiciona a tag "red" ao novo valor
                        self.caixapl.tag_config("red", foreground="red")
                    elif ndecisaopl5:
                        print("4")
                        result_ndecisaopl = ndecisaopl5.group(1)
                        self.caixapl.insert("3.12", result_ndecisaopl, "red")  # Adiciona a tag "red" ao novo valor
                        self.caixapl.tag_config("red", foreground="red")
                    elif ndecisaopl4:
                        print("5")
                        result_ndecisaopl = ndecisaopl4.group(1)
                        self.caixapl.insert("3.12", result_ndecisaopl, "red")  # Adiciona a tag "red" ao novo valor
                        self.caixapl.tag_config("red", foreground="red")
                    elif ndecisaopl7:
                        print("6")
                        result_ndecisaopl=ndecisaopl7.group(1)

                        self.caixapl.insert("3.12", result_ndecisaopl, "red")  # Adiciona a tag "red" ao novo valor
                        self.caixapl.tag_config("red", foreground="red")
                    if crea_entry == 'RJ':

                        for page_num in range(folhas_pl, len(pdf_reader.pages)):
                            page = pdf_reader.pages[page_num - 1]
                            text5 = page.extract_text()

                            datatopl = re.search(r'([a-z]+), (\d{1,2} [\dd][ ^e][ /]([a-z]+) de \d{4})', text5)
                            datatopl2 = re.search(r', (\d{1,2}) de (.*) de (\d{4})',text5)
                            if datatopl2:
                                datatopl = datatopl2

                            print("14 passo: Achei os dados da DECISÃO PLENARIA")
                            if datatopl:
                                result_datapl = datatopl.group()
                                result_data_pl = re.search(r'\d.*', result_datapl)
                                if result_data_pl:
                                    data_pl = result_data_pl.group()
                                    self.caixapl.insert("4.6", data_pl,"red")  # Adiciona a tag "red" ao novo valor
                                    self.caixapl.tag_config("red", foreground="red")
                                    break
                        if ndecisaopl6:
                            print("6")
                            result_ndecisaopl6 = ndecisaopl6.group(1)
                            result_ndecisaopl6_real = re.search(r'\d+/\d+',result_ndecisaopl6)
                            if result_ndecisaopl6_real:
                                ndecisao_pl = result_ndecisaopl6_real.group(0)
                            self.caixapl.insert("3.12", ndecisao_pl, "red")  # Adiciona a tag "red" ao novo valor
                            self.caixapl.tag_config("red", foreground="red")
                            break
                    if crea_entry == 'GO':
                        for page_num in range(pag_pl, len(pdf_reader.pages)):
                            page = pdf_reader.pages[page_num - 1]
                            text5 = page.extract_text()
                            datatopl = re.search(r', (\d{2}) de (.*) de (\d{4})', text5)
                            print("14 passo: Achei os dados da DECISÃO PLENARIA")
                            if datatopl:
                                result_datapl = datatopl.group()
                                result_datapl_real = result_datapl[2:]
                                self.caixapl.insert("4.6", result_datapl_real, "red")  # Adiciona a tag "red" ao novo valor
                                self.caixapl.tag_config("red", foreground="red")
                                break
                    if crea_entry == 'AM' or crea_entry =='SP':
                        for page_num in range(pag_pl, len(pdf_reader.pages)):
                            page = pdf_reader.pages[page_num - 1]
                            text5 = page.extract_text()
                            datatopl = re.search(r', (\d{2}) de (.*) de (\d{4})\.', text5)
                            print("14 passo: Achei os dados da DECISÃO PLENARIA")
                            if datatopl:
                                result_datapl = datatopl.group()
                                result_datapl_real = result_datapl[2:]
                                self.caixapl.insert("4.6", result_datapl_real, "red")  # Adiciona a tag "red" ao novo valor
                                self.caixapl.tag_config("red", foreground="red")
                                break
                    if crea_entry == "MT":
                        for page_num in range(pag_pl, len(pdf_reader.pages)):
                            page = pdf_reader.pages[page_num - 1]
                            text5 = page.extract_text()
                            datatopl = re.search(r', reunido em (\d{2}) de (.*) de (\d{4})', text5)
                            print("14 passo: Achei os dados da DECISÃO PLENARIA")
                            if datatopl:
                                result_datapl = datatopl.group()
                                result_datapl_real = result_datapl[2:]
                                self.caixapl.insert("4.6", result_datapl_real, "red")  # Adiciona a tag "red" ao novo valor
                                self.caixapl.tag_config("red", foreground="red")
                                break
                    if crea_entry == 'BA':
                        for page_num in range(folhas_pl, len(pdf_reader.pages)):
                            page = pdf_reader.pages[page_num - 1]
                            text5 = page.extract_text()

                            datatopl = re.search(r',\s*(\d{1,2})\s+de\s+(\w+)\s+de\s+(\d{4})', text5)

                            print("14 passo: Achei os dados da DECISÃO PLENARIA")
                            if datatopl:
                                result_datapl = datatopl.group()
                                result_datapl_real = result_datapl[2:]
                                self.caixapl.insert("4.6", result_datapl_real, "red")  # Adiciona a tag "red" ao novo valor
                                self.caixapl.tag_config("red", foreground="red")
                                break
                    elif crea_entry == "TO":
                        for page_num in range(pag_pl, len(pdf_reader.pages)):
                            page = pdf_reader.pages[page_num]
                            text5 = page.extract_text()
                            datatopl = re.search(r'TO, (.+)\.', text5)
                            print("14 passo: Achei os dados da DECISÃO PLENARIA")
                            if datatopl:
                                result_datapl = datatopl.group(1)
                                self.caixapl.insert("4.6", result_datapl, "red")  # Adiciona a tag "red" ao novo valor
                                self.caixapl.tag_config("red", foreground="red")
                                break
                    elif  crea_entry == "RS":
                            datatopl = re.search(r'Data:(.+)\.', text3)
                            print("14 passo: Achei os dados da DECISÃO PLENARIA")
                            if datatopl:
                                result_datapl = datatopl.group(1)
                                self.caixapl.insert("4.6", result_datapl, "red")  # Adiciona a tag "red" ao novo valor
                                self.caixapl.tag_config("red", foreground="red")
                                break


            multapl(pdf_reader, folhas_pl,crea_entry, pdf_file, num_pages)

        def multapl(pdf_reader, folhas_pl,crea_entry, pdf_file, num_pages):
            self.valBarra(55)
            global multa_pl
            print("entrou na multa")
            if crea_entry == 'GO' or crea_entry == 'BA' or crea_entry =='RJ' or crea_entry == 'AM' or crea_entry =='SP':
                for page_num in range(folhas_pl, len(pdf_reader.pages)):
                    page = pdf_reader.pages[page_num-1]
                    text6 = page.extract_text()
                    multaplgo_action_pos = text6.find(". Coordenou ")
                    multaplgo_action_pos2 = text6.find(". Presidiu")
                    multaplgo_desc_pos = text6.find("[.,] DECIDIU[: ]")
                    print("procurando a multa")
                    if multaplgo_action_pos != -1:

                        ("achou a multa1")
                        multaplgo_extracted_text = text6[multaplgo_desc_pos + len(" voto "):multaplgo_action_pos].strip()
                        multaplgo_melhora = multaplgo_extracted_text.replace("\n", "")
                        if multaplgo_melhora:
                            if "redução" in multaplgo_melhora:
                                multa_pl = 'reduziu'
                                self.caixapl.insert("5.6","reduziu para valor minimo","red")  # Adiciona a tag "red" ao novo valor
                                self.caixapl.tag_config("red", foreground="red")
                            elif "manutenção" in multaplgo_melhora or "Manutenção" in multaplgo_melhora:
                                multa_pl = 'manteve'
                                self.caixapl.insert("5.6", "manteve o valor da multa do AUTO","red")  # Adiciona a tag "red" ao novo valor
                                self.caixapl.tag_config("red", foreground="red")

                        break
                    elif multaplgo_action_pos2 != -1:
                        print("achou a multa2")
                        multaplgo_extracted_text = text6[multaplgo_desc_pos + len("[.,] DECIDIU[: ]"):multaplgo_action_pos2].strip()
                        multaplgo_melhora = multaplgo_extracted_text.replace("\n", "")
                        if multaplgo_melhora:
                            if "redução" in multaplgo_melhora:
                                multa_pl = 'reduziu'
                                self.caixapl.insert("5.6", "reduziu para valor minimo","red")  # Adiciona a tag "red" ao novo valor
                                self.caixapl.tag_config("red", foreground="red")
                            elif "manutenção" in multaplgo_melhora or "MANUTENÇÃO" in multaplgo_melhora:
                                multa_pl = 'manteve'
                                self.caixapl.insert("5.6", "manteve o valor da multa do AUTO","red")  # Adiciona a tag "red" ao novo valor
                                self.caixapl.tag_config("red", foreground="red")
                        break
            if crea_entry == 'TO':
                for page_num in range(folhas_pl, len(pdf_reader.pages)):
                    page = pdf_reader.pages[page_num - 1]
                    text6 = page.extract_text()
                    multaplgo_action_pos = text6.find(". O Plenário decidiu")
                    multaplgo_desc_pos = text6.find(", voto pela ")

                    if multaplgo_action_pos != -1:
                        multaplgo_extracted_text = text6[multaplgo_desc_pos + len(", voto pela "):multaplgo_action_pos].strip()
                        multaplgo_melhora = multaplgo_extracted_text.replace("\n", "")

                        if multaplgo_melhora:
                            if "redução" in multaplgo_melhora:
                                self.caixapl.insert("5.6", "reduziu para valor minimo","red")  # Adiciona a tag "red" ao novo valor
                                self.caixapl.tag_config("red", foreground="red")
                            elif "manutenção" in multaplgo_melhora or "MANUTENÇÃO" in multaplgo_melhora:
                                self.caixapl.insert("5.6", "manteve o valor da multa do AUTO","red")  # Adiciona a tag "red" ao novo valor
                                self.caixapl.tag_config("red", foreground="red")
                        break
            elif crea_entry == 'RS':
                for page_num in range(folhas_pl, len(pdf_reader.pages)):
                    page = pdf_reader.pages[page_num - 1]
                    text6 = page.extract_text()
                    multaplrs_action_pos = text6.find(". Coordenou ")
                    multaplrs_action_pos2 = text6.find(". Presidiu")
                    multaplrs_desc_pos = text6.find(" Voto: ")
                    print("procurando a multa")
                    if multaplrs_action_pos != -1:

                        multaplrs_extracted_text = text6[multaplrs_desc_pos + len(" voto "):multaplrs_action_pos].strip()
                        multaplrs_melhora = multaplrs_extracted_text.replace("\n", "")
                        if multaplrs_melhora:
                            if "redução" in multaplrs_melhora:
                                self.caixapl.insert("5.6", "reduziu para valor minimo","red")  # Adiciona a tag "red" ao novo valor
                                self.caixapl.tag_config("red", foreground="red")
                            elif "manutenção" in multaplrs_melhora:
                                self.caixapl.insert("5.6", "manteve o valor da multa do AUTO","red")  # Adiciona a tag "red" ao novo valor
                                self.caixapl.tag_config("red", foreground="red")

                        break
                    elif multaplrs_action_pos2 != -1:
                        print("achou a multa2")
                        multaplrs_extracted_text = text6[multaplrs_desc_pos + len(". DECIDIU: "):multaplrs_action_pos2].strip()
                        multaplrs_melhora = multaplrs_extracted_text.replace("\n", "")
                        if multaplrs_melhora:
                            if "redução" in multaplrs_melhora:
                                self.caixapl.insert("5.6", "reduziu para valor minimo","red")  # Adiciona a tag "red" ao novo valor
                                self.caixapl.tag_config("red", foreground="red")
                            elif "manutenção" in multaplrs_melhora:
                                self.caixapl.insert("5.6", "manteve o valor da multa do AUTO","red")  # Adiciona a tag "red" ao novo valor
                                self.caixapl.tag_config("red", foreground="red")
                        break
            elif crea_entry == 'MT':
                for page_num in range(folhas_pl, len(pdf_reader.pages)):
                    page = pdf_reader.pages[page_num - 1]
                    text6 = page.extract_text()
                    multaplrs_action_pos = text6.find("DECIDE: ")
                    multaplrs_action_pos2 = text6.find(". Presidiu")
                    multaplrs_desc_pos = text6.find(" voto")
                    print("procurando a multa")
                    if multaplrs_action_pos != -1:

                        multaplrs_extracted_text = text6[multaplrs_desc_pos + len(" voto"):multaplrs_action_pos].strip()
                        multaplrs_melhora = multaplrs_extracted_text.replace("\n", "")
                        if multaplrs_melhora:
                            if "redução" in multaplrs_melhora or "minimo" in multaplrs_melhora:
                                self.caixapl.insert("5.6", "reduziu para valor minimo","red")  # Adiciona a tag "red" ao novo valor
                                self.caixapl.tag_config("red", foreground="red")
                            elif "manutenção" in multaplrs_melhora:
                                self.caixapl.insert("5.6", "manteve o valor da multa do AUTO","red")  # Adiciona a tag "red" ao novo valor
                                self.caixapl.tag_config("red", foreground="red")


            aviso(pdf_reader, folhas_pl, crea_entry, pdf_file, num_pages)

        def aviso(pdf_reader, folhas_pl,crea_entry, pdf_file, num_pages):
            self.valBarra(75)
            global folhas_aviso
            data1= ''
            print("15 passo: Procurar o aviso de recebimento")
            for pagina in range(folhas_pl, len(pdf_reader.pages)):
                texto_pagina = pdf_reader.pages[pagina].extract_text()

                data1 = None
                if 'AVISO DE RECEBIMENTO' in texto_pagina:
                    print("16.1 passo: Achei o aviso de recebimento")
                    folhas_aviso = pagina + 1
                    self.caixaar.insert("2.7", folhas_aviso, "red")
                    self.caixaar.tag_config("red", foreground="red")
                    break
                elif 'Aviso de Recebimento' in texto_pagina:
                    print("16.2 passo: Achei o aviso de recebimento")
                    folhas_aviso = pagina + 1
                    self.caixaar.insert("2.7", folhas_aviso, "red")
                    self.caixaar.tag_config("red", foreground="red")
                    break
                elif 'ESTINATARIO:' in texto_pagina or 'Destinatário:' in texto_pagina or 'DESTINATÁRIO' in texto_pagina:
                    print("16.3 passo: Achei o aviso de recebimento")
                    folhas_aviso = pagina + 1
                    self.caixaar.insert("2.7", folhas_aviso, "red")
                    self.caixaar.tag_config("red", foreground="red")
                    break
                elif 'Objeto entregue' in texto_pagina:
                    print("16.4 passo: Achei o aviso de recebimento")
                    data3 = re.search(r'(\d{2})/(\d{2})/(\d{4}) ', texto_pagina)
                    dia1 = int(data3.group(1))
                    mes1 = int(data3.group(2))
                    ano1 = int(data3.group(3))
                    data1 = datetime(ano1, mes1, dia1)

                    folhas_aviso = pagina + 1
                    if folhas_aviso:
                        folhas_aviso = pagina + 1

                        self.caixaar.insert("2.7", folhas_aviso, "red")
                        self.caixaar.tag_config("red", foreground="red")

                    if data3:
                        configdata3(data3)

            recurso(folhas_pl,pdf_file,pdf_reader,crea_entry,data1,num_pages)

        """Descobrindo a Data"""
        def configdata3(data3):
            dia2 = data3.group(1)
            mes2 = data3.group(2)
            ano2 = data3.group(3)
            if mes2 == '01':
                mes_escrito2 = "janeiro"
                configmes3(dia2,mes_escrito2,ano2)
            elif mes2 == '02':
                mes_escrito2 = "fevereiro"
                configmes3(dia2,mes_escrito2,ano2)
            elif mes2 == '03':
                mes_escrito2 = "março"
                configmes3(dia2,mes_escrito2,ano2)
            elif mes2 == '04':
                mes_escrito2 = "abril"
                configmes3(dia2,mes_escrito2,ano2)
            elif mes2 == '05':
                mes_escrito2 = "maio"
                configmes3(dia2,mes_escrito2,ano2)
            elif mes2 == '06':
                mes_escrito2 = "junho"
                configmes3(dia2,mes_escrito2,ano2)
            elif mes2 == '07':
                mes_escrito2 = "julho"
                configmes3(dia2,mes_escrito2,ano2)
            elif mes2 == '08':
                mes_escrito2 = "agosto"
                configmes3(dia2,mes_escrito2,ano2)
            elif mes2 == '09':
                mes_escrito2 = "setembro"
                configmes3(dia2,mes_escrito2,ano2)
            elif mes2 == '10':
                mes_escrito2 = "outubro"
                configmes3(dia2,mes_escrito2,ano2)
            elif mes2 == '11':
                mes_escrito2 = "novembro"
                configmes3(dia2,mes_escrito2,ano2)
            elif mes2 == '12':
                mes_escrito2 = "dezembro"
                configmes3(dia2,mes_escrito2,ano2)

        """Exibindo a data"""
        def configmes3(dia2,mes_escrito2,ano2):
            data_formatada2 = f"{dia2} de {mes_escrito2} de {ano2}"
            self.caixaar.insert("3.5", str(data_formatada2), "red")  # Adiciona a tag "red" ao novo valor
            self.caixaar.tag_config("red", foreground="red")

        def recurso(folhas_pl,pdf_file,pdf_reader , crea_entry,data1,num_pages):
            global folhas_recurso
            global data_recurso
            self.valBarra(80)
            print("17 passo: Procurar o recurso")
            for page_num in range(folhas_pl, len(pdf_reader.pages)):
                    page = pdf_reader.pages[page_num-1]
                    text7 = page.extract_text()
                    recurso = re.search(r'ENTRADA COM DEFESA',text7)
                    recursoba = re.search(r'ENTRADA COM RECURSO',text7)
                    recursogo = re.search(r'REQUERIMENTO PARA APRESENTAÇÃO DE DEFESA',text7)
                    recursors = re.search(r',hahq (\d{2}) de (.*) de (\d{4})',text7)

                    recursomt1 = re.search(r'CONSELHO FEDERAL DE ENGEN',text7)
                    recursomt2 = re.search(r'DEFESA',text7)
                    if recursomt1 and recursomt2 and crea_entry!='RJ':
                        pag_recurso = page_num
                        folhas_recurso = f"{pag_recurso}/{num_pages}"
                        self.caixarecurso.insert("2.7", folhas_recurso, "red")
                        self.caixarecurso.tag_config("red", foreground="red")
                    if recursomt1 and (crea_entry=='RJ' ):
                        pag_recurso = page_num

                        folhas_recurso = f"{pag_recurso}/{num_pages}"
                        if folhas_recurso:
                            self.caixarecurso.insert("2.7", folhas_recurso, "red")
                            self.caixarecurso.tag_config("red", foreground="red")
                            break
                            
                    if recurso or recursoba:

                        print("18 passo: Achei o recurso")

                        pag_recurso = page_num
                        pag_recurso_total = f"{pag_recurso}/{num_pages}"
                        self.caixarecurso.insert("2.7", pag_recurso_total, "red")
                        self.caixarecurso.tag_config("red", foreground="red")
                        datarecurso = re.search(r'(\d{2})/(\d{2})/(\d{4})', text7)
                        datarecurso2 = re.search(r'(\d{2}) de (\w+) de (\d{4})',text7)
                        if datarecurso2:
                            data_formatadare = datarecurso2.group()
                            self.caixarecurso.insert("3.5", str(data_formatadare),"red")  # Adiciona a tag "red" ao novo valor
                            self.caixarecurso.tag_config("red", foreground="red")
                        elif datarecurso:
                            diare = datarecurso.group(1)
                            mesre = datarecurso.group(2)
                            anore = datarecurso.group(3)
                            dia4 = int(datarecurso.group(1))
                            mes4 = int(datarecurso.group(2))
                            ano4 = int(datarecurso.group(3))
                            data4 = datetime(ano4, mes4, dia4)
                            if mesre == '01':
                                mes_escritore = "janeiro"
                                configmesre(diare, mes_escritore, anore)
                            elif mesre == '02':
                                mes_escritore = "fevereiro"
                                configmesre(diare, mes_escritore, anore)
                            elif mesre == '03':
                                mes_escritore = "março"
                                configmesre(diare, mes_escritore, anore)
                            elif mesre == '04':
                                mes_escritore = "abril"
                                configmesre(diare, mes_escritore, anore)
                            elif mesre == '05':
                                mes_escritore = "maio"
                                configmesre(diare, mes_escritore, anore)
                            elif mesre == '06':
                                mes_escritore = "junho"
                                configmesre(diare, mes_escritore, anore)
                            elif mesre == '07':
                                mes_escritore = "julho"
                                configmesre(diare, mes_escritore, anore)
                            elif mesre == '08':
                                mes_escritore = "agosto"
                                configmesre(diare, mes_escritore, anore)
                            elif mesre == '09':
                                mes_escritore = "setembro"
                                configmesre(diare, mes_escritore, anore)
                            elif mesre == '10':
                                mes_escritore = "outubro"
                                configmesre(diare, mes_escritore, anore)
                            elif mesre == '11':
                                mes_escritore = "novembro"
                                configmesre(diare, mes_escritore, anore)
                            elif mesre == '12':
                                mes_escritore = "dezembro"
                            configmesre(diare, mes_escritore, anore)
                            data_formatadare = f"{diare} de {mes_escritore} de {anore}"
                            self.caixarecurso.insert("3.5", str(data_formatadare),
                                                     "red")  # Adiciona a tag "red" ao novo valor
                            self.caixarecurso.tag_config("red", foreground="red")
                            if data1 is not None:
                                diferenca = (data1 - data4).days
                                if diferenca:
                                    diferenca2 = diferenca*(-1)+1
                                    self.caixatempestividade.insert("2.17", "FORA DO PRAZO", "red")
                                    self.caixatempestividade.tag_config("red", foreground="red")
                                    self.caixatempestividade.insert("3.5", diferenca2, "red")
                                    self.caixatempestividade.tag_config("red", foreground="red")
                                    tk.messagebox.showwarning("Sistema confea", "ATENÇÃO : Intempestivo segundo analise básica")
                                else:
                                    self.caixatempestividade.insert("2.17", "DENTRO DO PRAZO", "red")
                                    self.caixatempestividade.tag_config("red", foreground="red")

                        break
                        self.valBarra(85)
                    elif recursogo:
                        pag_recursogo = page_num + 1
                        folhas_recurso = f"{pag_recursogo}/{num_pages}"
                        self.caixarecurso.insert("2.7", folhas_recurso, "red")
                        self.caixarecurso.tag_config("red", foreground="red")
                        descrecursoinicio = text7.find("Descrição da Defesa:")
                        posrecursofim = text7.find("Data ")
                        justificativa = text7[descrecursoinicio + len("Descrição da Defesa:"):posrecursofim].strip()
                        melhorajustificativa = justificativa.replace("\n", "")
                        datagore = re.search(r'(\d{2}) de (.*) de (\d{4})', text7)

                        if melhorajustificativa:
                            self.caixarecurso.insert("5.17", melhorajustificativa, "red")
                            self.caixarecurso.tag_config("red", foreground="red")

                        print("18 passo: Achei o recurso")

                        if datagore:
                            result_datagore = datagore.group()
                            self.caixarecurso.insert("3.7", result_datagore, "red")
                            self.caixarecurso.tag_config("red", foreground="red")
                        self.valBarra(95)
                    elif recursors:
                        result_recursors = recursors.group()
                        #result_recursors_real =
                        pag_recursors = page_num + 1
                        pag_recursors_total = f"{pag_recursors}/{num_pages}"
                        self.caixarecurso.insert("2.7", pag_recursors_total, "red")
                        self.caixarecurso.tag_config("red", foreground="red")
                        self.caixarecurso.insert("3.5", result_recursors, "red")
                        self.caixarecurso.tag_config("red", foreground="red")
                        break
                    def configmesre(diare, mes_escritore, anore):
                        data_formatadare = f"{diare} de {mes_escritore} de {anore}"
                        self.caixarecurso.insert("3.5", str(data_formatadare), "red")  # Adiciona a tag "red" ao novo valor
                        self.caixarecurso.tag_config("red", foreground="red")

            art(pdf_reader,crea_entry)

        def art(pdf_reader, crea_entry):
            art_page = None
            reincidencia_page = None
            cnpj_page = None
            procuracao = None
            global folhas_procuracao
            global folhas_art
            global folhas_cnpj
            global folhas_reincidencia

            if crea_entry:
                for page_num, page in enumerate(pdf_reader.pages):
                    text = page.extract_text()
                    if art_page is None:
                        art_match = re.search(r'ART O', text)
                        if art_match is not None:
                            folhas_art = page_num + 1  # Número da página onde foi encontrada a correspondência
                            self.caixaart.insert("2.7", folhas_art, "red")  # Adiciona a tag "red" ao novo valor
                            self.caixaart.tag_config("red", foreground="red")


                    if cnpj_page is None:
                        cnpj_match = re.search(r'COMPROVANTE DE INSCRIÇÃO ', text)
                        cnpj_match2 = re.search(r'Comprovante de Inscri', text)
                        if cnpj_match or cnpj_match2 is not None:

                            folhas_cnpj = page_num + 1  # Número da página onde foi encontrada a correspondência
                            self.caixacnpj.insert("2.7", folhas_cnpj, "red")  # Adiciona a tag "red" ao novo valor
                            self.caixacnpj.tag_config("red", foreground="red")

                    if reincidencia_page is None:
                        reincidencia_match = re.search(r'CERTIDÃO DE TRÂNSITO EM JULGADO', text)
                        if reincidencia_match is not None:

                            folhas_reincidencia = page_num + 1  # Número da página onde foi encontrada a correspondência
                            self.caixareincidencia.insert("2.7", folhas_reincidencia, "red")  # Adiciona a tag "red" ao novo valor
                            self.caixareincidencia.tag_config("red", foreground="red")

                    if procuracao is None:
                        result_procuracao = re.search(r'PROCURAÇÃO', text)

                        if result_procuracao is not None:
                            folhas_procuracao = page_num + 1  # Número da página onde foi encontrada a correspondência
                            self.caixaprocuracao.insert("2.7", folhas_procuracao,"red")  # Adiciona a tag "red" ao novo valor
                            self.caixaprocuracao.tag_config("red", foreground="red")
                            break

                    if art_page is not None and reincidencia_page is not None:
                        break

            def salvar():
                global con
                global crea_entry
                global nsei_ai
                global artigo_ai
                global autuado_ai
                global cnpj_cpf_ai
                global folhas_ai
                global nauto_ai
                global multa_ai
                global data_ai
                global motivo_ai
                global especialidade_ce
                global folhas_ce
                global ndecisao_ce
                global data_ce
                global folhas_pl
                global ndecisao_pl
                global data_pl
                global multa_pl
                global folhas_recurso
                global data_recurso
                global justifica_recurso
                global folhas_aviso
                global data_aviso
                global prazo
                global dias
                global folhas_art
                global n_art
                global data_art
                global folhas_cnpj
                global data_cnpj
                global cnae_primeiro
                global cnae_segundo
                global folhas_reincidencia
                global data_reincidencia
                global folhas_procuracao
                global nome_procuracao
                global folhas_alteracao
                global n_alteracao
                print("CREA", crea_entry)

                # Chame a função salvar() passando os elementos da lista como argumentos separados

                if (crea_entry == ''):
                    messagebox.showinfo("Falha ao salvar", "Não pode salvar")
                else:
                    try:
                        with mysql.connector.connect(
                            host="localhost",
                            user="root",
                            password="senhateste",
                            database='python-tkinter'
                        ) as con:
                            # cursor = con.cursor("insert into dados values('"+ crea_entry+"')")
                            # cursor.execute("commit");
                            print("SALVAR 1")
                            cursor = con.cursor()
                        #if crea_entry:
                        #    cursor.execute("INSERT INTO dados (crea) VALUES (%s)", (crea_entry,))
                            if nauto_ai and crea_entry and folhas_ai:

                            #cursor.execute("INSERT INTO dados (crea,nsei,artigo,autuado,cnpj_cpf,folhas,nauto,multa,data,motivo,folhasce,ndecisaoce,especialidade,datace,multace, folhaspl, ndecisaopl,datapl,multapl,folharecurso,datarecurso,justificativa,folhaaviso,dataaviso,prazo,dias,folhasart,nart,dataart,folhascnpj,cnaeprimeiro,cnaesegundo,folhasreincidencia,datareincidencia,folhasprocuracao,nomeprocuracao,folhasalteracao,nalteracao ) VALUES (%s, %s,%s, %s, %s, %s, %s, %s,%s,%s, %s, %s,%s,%s, %s,%s,%s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (crea_entry,nsei_ai,artigo_ai,autuado_ai,cnpj_cpf_ai,folhas_ai,nauto_ai, multa_ai,data_ai,motivo_ai,folhas_ce,ndecisao_ce,especialidade_ce,data_ce,multa_ce,folhas_pl,ndecisao_pl,data_pl,multa_pl,folhas_recurso,data_recurso,justifica_recurso,folhas_aviso,data_aviso,prazo,dias,folhas_art,n_art,data_art,folhas_cnpj,data_cnpj,cnae_primeiro,cnae_segundo,folhas_reincidencia,data_reincidencia,folhas_procuracao,nome_procuracao,folhas_alteracao,n_alteracao,))
                                                                                                                            #10,                                                                                             20,                                                                                         30,                                                                                                                       38                                               10,                               20,                           30,                         39
                        # Defina as colunas em formato de lista
                                colunas = ['crea', 'nsei', 'artigo', 'autuado', 'cnpj_cpf', 'folhas', 'nauto', 'multa', 'data', 'motivo', 'folhasce', #11
                                'ndecisaoce', 'especialidade', 'datace', 'multace', 'folhaspl', 'ndecisaopl', 'datapl', 'multapl',  #8
                                'folharecurso', 'datarecurso', 'justificativa', 'folhaaviso', 'dataaviso', 'prazo', 'dias', 'folhasart',   #8
                                'nart', 'dataart', 'folhascnpj','datacnpj', 'cnaeprimeiro', 'cnaesegundo', 'folhasreincidencia', 'datareincidencia',   #8
                                'folhasprocuracao', 'nomeprocuracao', 'folhasalteracao', 'nalteracao']      #4

                        # Valores dos dados a serem inseridos
                                valores = (
                                crea_entry, nsei_ai, artigo_ai, autuado_ai, cnpj_cpf_ai, folhas_ai, nauto_ai, multa_ai, data_ai, motivo_ai, folhas_ce, #11
                                ndecisao_ce, especialidade_ce, data_ce, multa_ce, folhas_pl, ndecisao_pl, data_pl, multa_pl, folhas_recurso, #9
                                data_recurso, justifica_recurso, folhas_aviso, data_aviso, prazo, dias, folhas_art, n_art, data_art, folhas_cnpj, #10
                                data_cnpj, cnae_primeiro, cnae_segundo, folhas_reincidencia, data_reincidencia, folhas_procuracao, nome_procuracao, #7
                                folhas_alteracao, n_alteracao) #2

                        # Construa a instrução SQL com as colunas em formato de lista
                            sql = "INSERT INTO dados ({}) VALUES ({})".format(', '.join(colunas),', '.join(['%s'] * len(colunas)))
                            cursor.execute(sql, valores)

                            con.commit()
                            print("SALVAR 2")

                            print(con)
                    except mysql.connector.Error as error:
                        messagebox.showwarning("Duplicidade", f"Auto de infração duplicado ou já analisado\n {str(error)}")
            salvar()
            self.variaveis()
            self.valBarra(100)
            tk.messagebox.showinfo("Sistema confea","Finalizado")

##########################################################################################################
#           CREAS GO
##########################################################################################################
        """Descobre qual pagina do Auto de Infração"""
        def crea_entrysgo(pdf_file, num_pages, crea_entry):
            self.caixaai.delete("2.16", "2.99")
            pdf_reader = PdfReader(pdf_file)
            for page_num in range(num_pages):
                page = pdf_reader.pages[page_num]
                text = page.extract_text()
                pagautuado = re.search(r'AUTO DE INFRAÇÃO Nº(.+)', text)
                result_nsei_entry = re.search(r'Processo: (.*)Página', text)

                if pagautuado and result_nsei_entry:
                    folhas_entry = page_num + 1
                    nsei_entry = result_nsei_entry.group(1)
                    self.caixaai.insert("2.16", str(nsei_entry), "red")  # Adiciona a tag "red" ao novo valor
                    self.caixaai.tag_config("red", foreground="red")
                    #salvar(nsei_entry)
                    #salvar(folhas_entry)
                    pagdoautogo(folhas_entry, pdf_file,crea_entry, num_pages)

        """EXTRAINDO DADOS DO AUTO DE INFRAÇÃO"""
        def pagdoautogo(folhas_entry,pdf_file,crea_entry,num_pages):
            pdf_reader = PdfReader(pdf_file)
            page = pdf_reader.pages[folhas_entry - 1]
            text = page.extract_text()
            artigo = re.search(r'o\(a\) artigo(.*)da Lei', text)
            multa = re.search(r' multa no valor de(.*) \(', text)
            data = re.search(r'\-GO, (\d{2}) (.+?) (\d{4})', text)
            nauto = re.search(r'Nº(.*)', text)
            cnpj = re.search(r' \d{2}\.\d{3}\.\d{3}', text)
            desc_pos = text.find("que")
            action_pos = text.find("- C")
            extracted_text = text[desc_pos + len("que"):action_pos].strip()
            melhora = extracted_text.replace("\n","")
            desc_pos = text.find("da Infração:")
            action_pos = text.find("b)")
            extracted_text = text[desc_pos + len("da Infração:"):action_pos].strip()
            melhora_motivo = extracted_text.replace("\n", "")

            if melhora_motivo:
                melhora_motivo_min = melhora_motivo.lower()
                self.caixaai.insert("10.10", melhora_motivo_min, "red")
                self.caixaai.tag_config("red", foreground="red")
            if melhora:
                self.caixaai.insert("4.12", melhora, "red")
                self.caixaai.tag_config("red", foreground="red")
            if cnpj:
                result_cnpj = cnpj.group()
                cnpj_numeros_meio = re.search(r'\d{2}\.(\d{3}\.\d{3})', result_cnpj)
                if cnpj_numeros_meio:
                    numeros_meio = result_cnpj[5:]
                    self.caixaai.insert("5.6", f"***{numeros_meio}***", "red")
                    self.caixaai.tag_config("red", foreground="red")
            if nauto:
                # Inserir o novo valor extraído do PDF no widget Text
                self.caixaai.insert("6.11", str(folhas_entry), "red")  # Adiciona a tag "red" ao novo valor
                self.caixaai.tag_config("red", foreground="red")  # Configura a cor vermelha para a tag "red"
                result_nauto = nauto.group(1)
                self.caixaai.insert("7.10", str(result_nauto), "red")  # Adiciona a tag "red" ao novo valor
                self.caixaai.tag_config("red", foreground="red")
            if artigo:
                result_artigo = artigo.group(1)
                if "1" in result_artigo:
                    self.caixaai.insert("3.8", "artigo 1º da Lei Federal nº 6.496/77","red")  # Adiciona a tag "red" ao novo valor
                    self.caixaai.tag_config("red", foreground="red")
                if "59" in result_artigo:
                    self.caixaai.insert("3.8", "artigo 59º da Lei Federal nº 5.194/66","red")  # Adiciona a tag "red" ao novo valor
                    self.caixaai.tag_config("red", foreground="red")
            if multa:
                result_multa = multa.group(1)
                self.caixaai.insert("8.7", str(result_multa), "red")  # Adiciona a tag "red" ao novo valor
                self.caixaai.tag_config("red", foreground="red")
            if data:
                result_data = data.group()
                result_data_real = result_data[5:]
                self.caixaai.insert("9.6", result_data_real, "red")  # Adiciona a tag "red" ao novo valor
                self.caixaai.tag_config("red", foreground="red")
            ce(pdf_reader, folhas_entry, crea_entry, pdf_file,num_pages)
##########################################################################################################
#           CREAS RS
##########################################################################################################
        """CREAS= RS"""

        def crea_entrysrs(pdf_file, num_pages, crea_entry):
            self.valBarra(10)
            print("3 passo: Procura a pagina do AUTO DE INFRAÇÃO")
            pdf_reader = PdfReader(pdf_file)
            for page_num in range(num_pages):
                page = pdf_reader.pages[page_num]
                text = page.extract_text()
                pagautuado = re.search(r'AUTO DE INFRAÇÃO N', text)
                pagautuado2 = re.search(r'AUTO DE INFRACAO N', text)

                """Pagina do Auto de infração"""
                if pagautuado or pagautuado2:

                    self.valBarra(15)
                    print("4 passo: Achei a pagina do AUTO DE INFRAÇÃO")
                    folhas_entry = page_num + 1
                    #result_nsei_entry = nsei_entry.group(1)
                    """Inserir numero do Processo SEI"""
                    #self.caixaai.insert("2.16", str(result_nsei_entry), "red")  # Adiciona a tag "red" ao novo valor
                    #self.caixaai.tag_config("red", foreground="red")
                    """Inserir folha do AUTO DE INFRAÇÃO"""
                    self.caixaai.insert("6.11", str(folhas_entry), "red")  # Adiciona a tag "red" ao novo valor
                    self.caixaai.tag_config("red", foreground="red")  # Configura a cor vermelha para a tag "red"
                    #salvar(folhas_entry)
                    pagedoautors(folhas_entry, pdf_file, num_pages, crea_entry)
                    break

        """EXTRAINDO DADOS DO AUTO DE INFRAÇÃO"""
        def pagedoautors(folhas_entry, pdf_file, num_pages, crea_entry):
            self.valBarra(20)
            print("5 passo: Procura todos os dados do AUTO DE INFRAÇÃO")
            pdf_reader = PdfReader(pdf_file)
            page = pdf_reader.pages[folhas_entry - 1]
            text = page.extract_text()

            """Extrai o valor da multa"""
            multa = re.search(r'Multa:(.*)\(', text)

            """Extrai a data do auto"""
            data = re.search(r'em (\d{2})/(\d{2})/(\d{4})', text)
            #data2 = re.search(r'(\d{2}) de (.*) de (\d{4})', text)
            """Extrai o NUMERO DO AUTO"""
            nauto = re.search(r'AUTO DE INFRAÇÃO Nº(.+)', text)
            nauto2 = re.search(r'AUTO DE INFRACAO N°(.+)', text)
            """Extrai o NOME DO AUTUADO"""
            autuado = re.search(r'Nome:(.+)', text)
            """Extrai o CNPJ"""
            cnpj = re.search(r'(\d{3}).(\d{3}).(\d{3})', text)
            """Extrai o motivo do AUTO"""

            desc_pos = text.find(" detalhada:")
            action_pos = text.find("Endere",desc_pos)
            extracted_text = text[desc_pos + len(" detalhada:"):action_pos].strip()
            melhora_motivo = extracted_text.replace("\n", "")
            print("6 passo: Achei todos os dados do AUTO DE INFRAÇÃO")
            self.valBarra(25)
            if melhora_motivo:
                melhora_motivo_min = melhora_motivo.lower()
                self.caixaai.insert("10.10", melhora_motivo_min, "red")
                self.caixaai.tag_config("red", foreground="red")
                if "LEIGA" or "pf" in melhora_motivo_min:
                    self.caixaai.insert("3.8", str("Art. 6º da Lei Federal 5.194, de 1966"),"red")  # Adiciona a tag "red" ao novo valor
                    self.caixaai.tag_config("red", foreground="red")
                elif "SEM REGISTRO" in melhora_motivo_min:
                    self.caixaai.insert("3.8", str("Art. 59º da Lei Federal 5.194, de 1966"),"red")  # Adiciona a tag "red" ao novo valor
                    self.caixaai.tag_config("red", foreground="red")
                elif "FALTA DE REGISTRO" in melhora_motivo_min:
                    self.caixaai.insert("3.8", str("Art. 59º da Lei Federal 5.194, de 1966"),"red")  # Adiciona a tag "red" ao novo valor
                    self.caixaai.tag_config("red", foreground="red")
                elif "CANCELADO" in melhora_motivo_min:
                    self.caixaai.insert("3.8", str("Art. 64º da Lei Federal 5.194, de 1966"), "red")  # Adiciona a tag "red" ao novo valor
                    self.caixaai.tag_config("red", foreground="red")
                """Extrai o artigo"""
                artigo = re.search(r'Infração:(.{39})', text)
            if cnpj:
                result_cnpj = cnpj.group()
                result_cnpj_alterado = result_cnpj[5:]
                self.caixaai.insert("5.6", f"***{result_cnpj_alterado}***", "red")
                self.caixaai.tag_config("red", foreground="red")
            if autuado:
                result_autuado = autuado.group(1)
                result_autuado_min = result_autuado.title()
                self.caixaai.insert("4.12", str(result_autuado_min), "red")  # Adiciona a tag "red" ao novo valor
                self.caixaai.tag_config("red", foreground="red")
            if multa:
                result_multa = multa.group(1)
                self.caixaai.insert("8.7", str(result_multa), "red")  # Adiciona a tag "red" ao novo valor
                self.caixaai.tag_config("red", foreground="red")

            if artigo:
                result_artigo = artigo.group(1)


            if nauto or nauto2:
                if nauto:
                    result_nauto = nauto.group(1)
                elif nauto2:
                    result_nauto = nauto2.group(1)
                self.caixaai.insert("7.10", str(result_nauto), "red")  # Adiciona a tag "red" ao novo valor
                self.caixaai.tag_config("red", foreground="red")
            if  crea_entry == "RS" or crea_entry =="MT":
                for page_num in range(folhas_entry, len(pdf_reader.pages)):
                    page = pdf_reader.pages[page_num-1]
                    text2 = page.extract_text()

                    data2 = re.search(r",_(\d{1,2}) de ([A-Z]+) de (\d{4})", text2)
                    data = re.search(r', (\d{1,2} de ([A-Z]+) de \d{4})', text2)

                    if data or data2:
                        if data:
                            result_data = data.group()
                            
                        elif data2:
                            result_data = data2.group()

                        result_data_alterado = result_data[2:]
                        result_data_alterado2 = result_data_alterado.lower()
                        self.caixaai.insert("9.6", result_data_alterado2, "red")  # Adiciona a tag "red" ao novo valor
                        self.caixaai.tag_config("red", foreground="red")

                        break
            ce(pdf_reader, folhas_entry, crea_entry, pdf_file, num_pages)

        """Descobre qual a pagina da Camara Especializada"""

        #def cego(pdf_reader, folhas_entry, result, pdf_file):




        def configmes(dia,mes_escrito,ano):
            data_formatada = f"{dia} de {mes_escrito} de {ano}"
            if data_formatada:
                self.caixaai.insert("9.6", str(data_formatada), "red")  # Adiciona a tag "red" ao novo valor
                self.caixaai.tag_config("red", foreground="red")
                return data_formatada
#            self.caixatexto.insert("1.238", str(data_formatada), "red")
#            self.caixatexto.tag_config("red", foreground="red")


        def configdata(data):

            dia = data.group(1)
            mes = data.group(2)
            ano = data.group(3)
            if mes == '01':
                mes_escrito = "janeiro"
                configmes(dia,mes_escrito,ano)
            elif mes == '02':
                mes_escrito = "fevereiro"
                configmes(dia,mes_escrito,ano)
            elif mes == '03':
                mes_escrito = "março"
                configmes(dia,mes_escrito,ano)
            elif mes == '04':
                mes_escrito = "abril"
                configmes(dia,mes_escrito,ano)
            elif mes == '05':
                mes_escrito = "maio"
                configmes(dia,mes_escrito,ano)
            elif mes == '06':
                mes_escrito = "junho"
                configmes(dia,mes_escrito,ano)
            elif mes == '07':
                mes_escrito = "julho"
                configmes(dia,mes_escrito,ano)
            elif mes == '08':
                mes_escrito = "agosto"
                configmes(dia,mes_escrito,ano)
            elif mes == '09':
                mes_escrito = "setembro"
                configmes(dia,mes_escrito,ano)
            elif mes == '10':
                mes_escrito = "outubro"
                configmes(dia,mes_escrito,ano)
            elif mes == '11':
                mes_escrito = "novembro"
                configmes(dia,mes_escrito,ano)
            elif mes == '12':
                mes_escrito = "dezembro"
                configmes(dia,mes_escrito,ano)

##########################################################################################################
#           CREAS RJ
##########################################################################################################
        """Descobre qual pagina do Auto de Infração"""

        def crea_entrysrj(pdf_file, num_pages, crea_entry):
            self.valBarra(10)
            print("3 passo: Procura a pagina do AUTO DE INFRAÇÃO")
            pdf_reader = PdfReader(pdf_file)
            for page_num in range(num_pages):
                page = pdf_reader.pages[page_num]
                text = page.extract_text()
                pagautuado = re.search(r'AUTO INFRAÇÃO NÚMERO', text)


                """Pagina do Auto de infração"""
                if pagautuado:
                    self.valBarra(15)
                    print("4 passo: Achei a pagina do AUTO DE INFRAÇÃO")
                    global folhas_ai
                    folhas_ai = page_num + 1
                    # result_nsei_entry = nsei_entry.group(1)
                    """Inserir numero do Processo SEI"""
                    # self.caixaai.insert("2.16", str(result_nsei_entry), "red")  # Adiciona a tag "red" ao novo valor
                    # self.caixaai.tag_config("red", foreground="red")
                    """Inserir folha do AUTO DE INFRAÇÃO"""
                    self.caixaai.insert("6.11", str(folhas_ai), "red")  # Adiciona a tag "red" ao novo valor
                    self.caixaai.tag_config("red", foreground="red")  # Configura a cor vermelha para a tag "red"
                    #folhas_entry)
                    pagedoautorj(folhas_ai, pdf_file, num_pages, crea_entry)
                    break

        """EXTRAINDO DADOS DO AUTO DE INFRAÇÃO"""

        def pagedoautorj(folhas_ai, pdf_file, num_pages, crea_entry):
            locale.setlocale(locale.LC_TIME, 'pt_BR.utf8')
            global nauto_ai
            global multa_ai
            global nsei_ai
            global autuado_ai
            global cnpj_cpf_ai
            global artigo_ai
            global motivo_ai
            global data_ai
            self.valBarra(20)
            print("5 passo: Procura todos os dados do AUTO DE INFRAÇÃO")
            pdf_reader = PdfReader(pdf_file)
            page = pdf_reader.pages[folhas_ai - 1]
            text = page.extract_text()
            """Extrai o valor da multa"""
            multa = re.search(r'Valor da Multa(.*)\(', text)
            """Extrai a data do auto"""
            data = re.search(r'(\d{1,2} de [A-Z][a-z]+ de \d{4})', text)
            """Extrai o NUMERO DO AUTO"""
            nauto = re.search(r'AUTO INFRAÇÃO NÚMERO[;:](.+)', text)
            #nauto2 = re.search(r'AUTO DE INFRACAO N°(.+)', text)
            """Extrai o NOME DO AUTUADO"""
            autuado = re.search(r'Nome do In(.+)', text)

            """Extrai o CNPJ"""
            cnpj = re.search(r'CNPJ do Infrator(.+)', text)
            """Extrai o motivo do AUTO"""
            artigo1 = re.search(r'Enquadramento(.+)',text)


            desc_pos = text.find("Serviço Executado")
            action_pos = text.find("Contratante", desc_pos)
            extracted_text = text[desc_pos + len("Serviço Executado"):action_pos].strip()
            melhora_motivo = extracted_text.replace("\n", "")
            print("6 passo: Achei todos os dados do AUTO DE INFRAÇÃO")
            self.valBarra(25)
            if melhora_motivo:

                melhora_motivo1 = re.search(r'[:;] .+', melhora_motivo)
                if melhora_motivo1:
                    melhora_motivo2= melhora_motivo1.group()
                    melhora_motivo3 = melhora_motivo2[1:]

                    motivo_ai = melhora_motivo3.lower()
                    self.caixaai.insert("10.10", motivo_ai, "red")
                    self.caixaai.tag_config("red", foreground="red")

            if cnpj:
                result_cnpj = cnpj.group()
                cnpj_cpf_ai = result_cnpj[21:26]
                self.caixaai.insert("5.6", f"***{cnpj_cpf_ai}***", "red")
                self.caixaai.tag_config("red", foreground="red")
            if autuado:
                result_autuado = autuado.group(1)
                result_autuado_real = result_autuado[8:]
                autuado_ai = result_autuado_real.title()
                self.caixaai.insert("4.12", str(autuado_ai), "red")  # Adiciona a tag "red" ao novo valor
                self.caixaai.tag_config("red", foreground="red")
            if multa:
                result_multa = multa.group(1)
                multa_ai = result_multa[2:]
                self.caixaai.insert("8.7", str(multa_ai), "red")  # Adiciona a tag "red" ao novo valor
                self.caixaai.tag_config("red", foreground="red")

            if artigo1:
                artigo2 = artigo1.group(1)
                artigo = re.search(r'\bART.+', artigo2)
                if artigo:
                    artigo_ai = artigo.group(0).lower()
                    self.caixaai.insert("3.8", str(artigo_ai),"red")  # Adiciona a tag "red" ao novo valor
                    self.caixaai.tag_config("red", foreground="red")

            if nauto :
                nauto_ai = nauto.group(1)
                nsei_ai = nauto_ai
                self.caixaai.insert("7.10", nauto_ai, "red")  # Adiciona a tag "red" ao novo valor
                self.caixaai.tag_config("red", foreground="red")
                self.caixaai.insert("2.16", nsei_ai, "red")  # Adiciona a tag "red" ao novo valor
                self.caixaai.tag_config("red", foreground="red")
                #salvar(nauto_entry)

            if data:
                result_data = data.group(1)
                data_objeto = datetime.strptime(result_data, "%d de %B de %Y")
                data_ai = data_objeto.strftime("%Y-%m-%d")
                self.caixaai.insert("9.6", str(result_data), "red")  # Adiciona a tag "red" ao novo valor
                self.caixaai.tag_config("red", foreground="red")
            ce(pdf_reader, folhas_ai, crea_entry, pdf_file, num_pages)

        #def pagedopl(pag_pl, pdf_file):

##########################################################################################################
#           CREAS SP
##########################################################################################################
        """Descobre qual pagina do Auto de Infração"""

        def crea_entryssp(pdf_file, num_pages, crea_entry):
            self.valBarra(10)
            print("3 passo: Procura a pagina do AUTO DE INFRAÇÃO")
            pdf_reader = PdfReader(pdf_file)
            for page_num in range(num_pages):
                page = pdf_reader.pages[page_num]
                text = page.extract_text()
                pagautuado = re.search(r'AUTO DE (INFRACAO|INFRAÇÃO)', text)

                """Pagina do Auto de infração"""
                if pagautuado:
                    self.valBarra(15)
                    print("4 passo: Achei a pagina do AUTO DE INFRAÇÃO")
                    folhas_entry = page_num + 1


                    # result_nsei_entry = nsei_entry.group(1)
                    """Inserir numero do Processo SEI"""
                    # self.caixaai.insert("2.16", str(result_nsei_entry), "red")  # Adiciona a tag "red" ao novo valor
                        # self.caixaai.tag_config("red", foreground="red")
                    """Inserir folha do AUTO DE INFRAÇÃO"""
                    self.caixaai.insert("6.11", str(folhas_entry), "red")  # Adiciona a tag "red" ao novo valor
                    self.caixaai.tag_config("red", foreground="red")  # Configura a cor vermelha para a tag "red"
                    # folhas_entry)
                    pagedoautosp(folhas_entry, pdf_file, num_pages, crea_entry)
                    break


        """EXTRAINDO DADOS DO AUTO DE INFRAÇÃO"""

        def pagedoautosp(folhas_entry, pdf_file, num_pages, crea_entry):
            global nauto_entry
            self.valBarra(20)
            print("5 passo: Procura todos os dados do AUTO DE INFRAÇÃO")
            pdf_reader = PdfReader(pdf_file)
            page = pdf_reader.pages[folhas_entry - 1]
            text = page.extract_text()
            """Extrai o valor da multa"""
            """Extrai a data do auto"""
            data = re.search(r', (\d{1,2} de [A-Z][a-z]+ de \d{4}).', text)
            """Extrai o NUMERO DO AUTO"""

            nauto = re.search(r'(Número[;:]|N°)(.+) / (\d{4})', text)

            # nauto2 = re.search(r'AUTO DE INFRACAO N°(.+)', text)
            """Extrai o NOME DO AUTUADO"""
            autuado = re.search(r'nome da empresa (.*),', text)

            nsei=re.search(r'[Pp]rocesso (.*),',text)
            """Extrai o CNPJ"""
            cnpj = re.search(r'CNPJ n.°(.*), e ', text)

            """Extrai o motivo do AUTO"""
            desc_pos2 = text.find("infringindo o")
            action_pos2 = text.find(" - ", desc_pos2)
            extracted_text2 = text[desc_pos2 + len("infringindo o"):action_pos2].strip()
            artigo = extracted_text2.replace("\n", "")

            desc_pos = text.find(", vem ")
            action_pos = text.find(".", desc_pos)
            extracted_text = text[desc_pos + len(", vem "):action_pos].strip()
            melhora_motivo = extracted_text.replace("\n", "")

            desc_pos1 = text.find("R$")
            action_pos1 = text.find('incidência', desc_pos1)
            extracted_text1 = text[desc_pos1 + len("R$"):action_pos1].strip()
            multa = extracted_text1.replace("\n", "")

            print("6 passo: Achei todos os dados do AUTO DE INFRAÇÃO")
            self.valBarra(25)
            if melhora_motivo:
                melhora_motivo_min = melhora_motivo.lower()
                self.caixaai.insert("10.10", melhora_motivo_min, "red")
                self.caixaai.tag_config("red", foreground="red")
            if nsei:
                nsei_entry= nsei.group(1)
                self.caixaai.insert("2.17", nsei_entry, "red")
                self.caixaai.tag_config("red", foreground="red")
            if cnpj:
                result_cnpj = cnpj.group(1)
                self.caixaai.insert("5.6", f"***{result_cnpj}***", "red")
                self.caixaai.tag_config("red", foreground="red")
            if autuado:
                result_autuado = autuado.group(1)
                result_autuado_real = result_autuado
                result_autuado_min = result_autuado_real.title()
                self.caixaai.insert("4.12", str(result_autuado_min), "red")  # Adiciona a tag "red" ao novo valor
                self.caixaai.tag_config("red", foreground="red")
            if multa:
                self.caixaai.insert("8.7", multa, "red")  # Adiciona a tag "red" ao novo valor
                self.caixaai.tag_config("red", foreground="red")
            if artigo:
                self.caixaai.insert("3.8", artigo, "red")  # Adiciona a tag "red" ao novo valor
                self.caixaai.tag_config("red", foreground="red")

            if nauto:
                result_nauto_entry = nauto.group()
                nauto_entry = result_nauto_entry[8:]
                self.caixaai.insert("7.10", nauto_entry, "red")  # Adiciona a tag "red" ao novo valor
                self.caixaai.tag_config("red", foreground="red")
                #self.caixaai.insert("2.16", nauto_entry, "red")  # Adiciona a tag "red" ao novo valor
                #self.caixaai.tag_config("red", foreground="red")
            elif nauto is None:
                nauto2 = re.search(r'N°(\d{3})/(\d{4})', text)
                if nauto2:
                    nauto_entry= nauto2.group()
                    self.caixaai.insert("7.10", nauto_entry, "red")  # Adiciona a tag "red" ao novo valor
                    self.caixaai.tag_config("red", foreground="red")
                # salvar(nauto_entry)
            if data:
                result_data = data.group(1)
                self.caixaai.insert("9.6", str(result_data), "red")  # Adiciona a tag "red" ao novo valor
                self.caixaai.tag_config("red", foreground="red")
            ce(pdf_reader, folhas_entry, crea_entry, pdf_file, num_pages)

                # pagedoce(pag_ce, pdf_file)

        """variaveis = [nsei_entry, artigo, autuado, cnpj_cpf, folhas_entry, nauto, multa, data, motivo,
                     folhas_entryce, ndecisaoce, especialidade, datace, multace, folhas_entrypl, ndecisaopl, datapl,
                     multapl, folharecurso, datarecurso, justificativa, folhaaviso, dataaviso, prazo, dias,
                     folhas_entryart, nart, dataart, folhas_entrycnpj, datacnpj, cnaeprimeiro, cnaesegundo,
                     folhas_entryreincidencia, datareincidencia, folhas_entryprocuracao, nomeprocuracao,
                     folhas_entryalteracao, nalteracao]"""

        btn_selecionar = ctk.CTkButton(self.frame_3, text="Selecionar arquivo", command=selecionar_arquivo)
        btn_selecionar.place(relx=0.65, rely=0.10, relwidth=0.15, relheight=0.80)
    #funcoes.varBarra()

App()
root.mainloop()