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
from datetime import datetime, timedelta
from tkinter import messagebox
#import mysql.connector as mysql
import requests

import mysql.connector

root = ctk.CTk()


class App():
    con = None
    crea_entry = None
    nauto_entry = None
    def __init__(self):
        self.root = root
        self.tela()
        self.variaveis()
        self.cabecalho()
        self.caixas()
        self.funcoes()
        #self.botoes()
        self.logo()
        #self.conteudo()
    def tela(self):
        """Definição da tela e sua cor total"""
        self.root.title("Sistema Confea")
        self.root.configure(fg_color='#e8e8e8')
        self.root.geometry("1900x900")
        self.root.resizable(True, True)
        self.root.minsize(1000, 600)
        self.root.iconbitmap("confea_color.ico")
        #con = mysql.connect(host='localhost',user='root',password='', database='python-tkinter')
    def variaveis(self):
        pass
    def cabecalho(self, select=2):
        self.tela()
        self.variaveis()

        """Header azul"""
        self.frame_1 = ctk.CTkFrame(self.root,fg_color='#4a89d3')
        self.frame_1.place(relx=0.0, rely=0.0, relwidth=1, relheight=0.2)
        self.logo()


        #self.botoes()
    def caixas(self):
        """Caixa AI"""
        self.caixaai = ctk.CTkTextbox(self.root, text_color='black', fg_color='white', font=('Lato Regular', 18))
        self.caixaai.insert(tk.INSERT,"                           AUTO DE INFRAÇÃO\nNº do Processo:\nArtigo:\nAutuado(a):\nCNPJ:\nFolhas:\nNº do AI:\nMulta:\nData:\nMotivo:")
        self.caixaai.place(relx=0.065, rely=0.26, relwidth=0.46, relheight=0.34)

        """Caixa CE"""
        self.caixace = ctk.CTkTextbox(self.root, text_color='black', fg_color='white', font=('Lato Bold', 18))
        self.caixace.insert(tk.INSERT,"                           DECISÃO DA CÂMARA ESPECIALIZADA DO CREA\nFolhas:\nDecisão nº:\nEspecialidade:\nData:\nMulta:")
        self.caixace.place(relx=0.54, rely=0.26, relwidth=0.45, relheight=0.16)

        """Caixa PL"""
        self.caixapl = ctk.CTkTextbox(self.root, text_color='black', fg_color='white', font=('Lato Regular', 18))
        self.caixapl.insert(tk.INSERT,"                DECISÃO PLENÁRIO DO CREA\nFolhas:\nDecisão nº:\nData:\nMulta:")
        self.caixapl.place(relx=0.065, rely=0.61, relwidth=0.23, relheight=0.14)

        """Caixa Ficha Cadastral"""
        self.caixaficha = ctk.CTkTextbox(self.root, text_color='black', fg_color='white', font=('Lato Regular', 18))
        self.caixaficha.insert(tk.INSERT,"            FICHA CADASTRAL SIMPLIFICADA\nFolhas:\nData:\nObjetivo Social:")
        self.caixaficha.place(relx=0.305, rely=0.61, relwidth=0.22, relheight=0.14)

        """Caixa Alteração"""
        self.caixaalteracao = ctk.CTkTextbox(self.root, text_color='black', fg_color='white', font=('Lato Regular', 18))
        self.caixaalteracao.insert(tk.INSERT,"ALTERAÇÃO/CONSOLIDAÇÃO CONTRATUAL\nFolhas:\nData:\nObjetivo Social:")
        self.caixaalteracao.place(relx=0.305, rely=0.76, relwidth=0.22, relheight=0.14)

        """Caixa AR"""
        self.caixaar = ctk.CTkTextbox(self.root, text_color='black', fg_color='white', font=('Lato Regular', 18))
        self.caixaar.insert(tk.INSERT, "                           AVISO DE RECEBIMENTO\nFolhas:\nData:")
        self.caixaar.place(relx=0.54, rely=0.43, relwidth=0.22, relheight=0.09)

        """Caixa Tempestividade"""
        self.caixatempestividade = ctk.CTkTextbox(self.root, text_color='black', fg_color='white', font=('Lato Regular', 18))
        self.caixatempestividade.insert(tk.INSERT,"                           INTEMPESTIVIDADE\nDentro do prazo:\nDias:")
        self.caixatempestividade.place(relx=0.77, rely=0.43, relwidth=0.22, relheight=0.09)

        """Caixa RECURSO"""
        self.caixarecurso = ctk.CTkTextbox(self.root, text_color='black', fg_color='white', font=('Lato Regular', 18))
        self.caixarecurso.insert(tk.INSERT,"                    RECURSO AO CONFEA\nFolhas:\nData:\nContrato:\nJustificativa 1:")
        self.caixarecurso.place(relx=0.065, rely=0.76, relwidth=0.23, relheight=0.14)

        """Caixa ART"""
        self.caixaart = ctk.CTkTextbox(self.root, text_color='black', fg_color='white', font=('Lato Regular', 18))
        self.caixaart.insert(tk.INSERT,"                           REGULARIZAÇÃO POR ANOTAÇÃO DE RESPONSABILIDADE TÉCNICA-ART\nFolhas:\nNº da ART:\nData:")
        self.caixaart.place(relx=0.54, rely=0.53, relwidth=0.45, relheight=0.12)

        """Caixa Comprovante de Cadastro Nacional de Pessoa Juridica"""
        self.caixacnpj = ctk.CTkTextbox(self.root, text_color='black', fg_color='white', font=('Lato Regular', 18))
        self.caixacnpj.insert(tk.INSERT,"                           COMPROVANTE DE CADASTRO NACIONAL DE PESSOA JURÍDICA\nFolhas:\nData:\nCNAE Primário:\nCNAE Secundário:")
        self.caixacnpj.place(relx=0.54, rely=0.66, relwidth=0.45, relheight=0.14)

        """Caixa Reincidência"""
        self.caixareincidencia = ctk.CTkTextbox(self.root, text_color='black', fg_color='white', font=('Lato Regular', 18))
        self.caixareincidencia.insert(tk.INSERT, "                           REINCIDÊNCIA\nFolhas:\nData:")
        self.caixareincidencia.place(relx=0.54, rely=0.81, relwidth=0.22, relheight=0.09)

        """Caixa Procuração"""
        self.caixaprocuracao = ctk.CTkTextbox(self.root, text_color='black', fg_color='white', font=('Lato Regular', 18))
        self.caixaprocuracao.insert(tk.INSERT, "                           PROCURAÇÃO\nFolhas:\nNome:")
        self.caixaprocuracao.place(relx=0.77, rely=0.81, relwidth=0.22, relheight=0.09)
    def valBarra(self, progress):
        self.varBarra.set(progress)
        self.root.update()
    def funcoes(self):
        def valBarra(self, progress):
            self.varBarra.set(progress)
            self.root.update()

        self.varBarra = DoubleVar()
        self.varBarra.set(0)

        self.barra = ctk.CTkProgressBar(self.root, variable=self.varBarra)
        self.barra.configure(fg_color="#535353",progress_color="#4a89d3")
        #self.barra = ctk.CTkProgressBar(self.root,  )
        #self.barra.start()
        self.barra.place(relx=0.43, rely=0.94, relwidth=0.2, relheight=0.02)
    def logo(self):
        self.frame_3 = ctk.CTkFrame(self.root, fg_color='#535353')
        self.frame_3.place(relx=0.0, rely=0.2, relwidth=1, relheight=0.05)
        self.frame_2 = ctk.CTkFrame(self.root,fg_color='#094c8c')
        self.frame_2.place(relx=0.0, rely=0.25, relwidth=0.06, relheight=1)

        lg= ctk.CTkImage(Image.open("log.png"),size=(300,70))
        logo=ctk.CTkLabel(self.frame_1,image=lg,text='')
        logo.place(relx=0.07, rely=0.1, relwidth=0.35, relheight=0.8)
        """consulta de acordo com crea_entrys TO/BA/PR"""
        global con
        global crea_entry
        global nauto_entry
        crea_entry = ''
        nsei_entry = ''
        nauto_entry = ''
        """limpar dados"""
        def limpar():
            """limpa o nome do arquivo"""
            lbl_selecionado = ctk.CTkLabel(self.frame_3, text='', fg_color='#535353')
            lbl_selecionado.place(relx=0.25, rely=0.10, relwidth=0.3, relheight=0.80)
            """limpar barra"""
            self.varBarra.set(0)
            self.variaveis()
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
            multa_ai = "multa do ai"
            nsei_ai = "numero do processo"
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
            data_aviso = "data do aviso"
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
            self.caixaai.delete("2.15", "2.9999")
            self.caixaai.delete("3.7", "3.99999")
            self.caixaai.delete("4.11", "4.9999")
            self.caixaai.delete("5.5", "5.9999")
            self.caixaai.delete("6.7", "6.9999")
            self.caixaai.delete("7.9", "7.9999")
            self.caixaai.delete("9.5", "9.9999")
            self.caixaai.delete("10.7", "10.9999")
            self.caixaai.delete("8.6", "8.9999")
            """limpa as caixas da camara"""
            self.caixace.delete("2.7", "2.9999")
            self.caixace.delete("3.11", "3.9999")
            self.caixace.delete("4.14", "4.9999")
            self.caixace.delete("5.5", "5.9999")
            self.caixace.delete("6.6", "6.9999")
            """limpa as caixas do plenario"""
            self.caixapl.delete("2.7", "2.9999")
            self.caixapl.delete("3.11", "3.9999")
            self.caixapl.delete("4.5", "4.9999")
            self.caixapl.delete("5.6", "8.9999")
            """limpar Ficha cadastral"""
            self.caixaficha.delete("2.7", "2.9999")
            self.caixaficha.delete("3.5", "3.9999")
            self.caixaficha.delete("4.16", "4.9999")
            """limpar Alteração"""
            self.caixaalteracao.delete("2.7", "2.9999")
            self.caixaalteracao.delete("3.5", "3.9999")
            self.caixaalteracao.delete("4.16", "4.9999")
            """limpa caixa de aviso"""
            self.caixaar.delete("2.7", "2.9999")
            self.caixaar.delete("3.5", "3.9999")
            """limpa caixa de recurso"""
            self.caixarecurso.delete("2.7", "2.9999")
            self.caixarecurso.delete("3.5", "3.9999")
            self.caixarecurso.delete("5.16","10.9999")
            """limpar intempestividade"""
            self.caixatempestividade.delete("2.16", "2.9999")
            self.caixatempestividade.delete("3.5", "3.9999")
            """limpar art"""
            self.caixaart.delete("2.7", "2.9999")
            self.caixaart.delete("3.11", "3.9999")
            self.caixaart.delete("4.5", "4.9999")
            """limpar comprovante de cnpj"""
            self.caixacnpj.delete("2.7", "2.9999")
            self.caixacnpj.delete("3.5", "3.9999")
            self.caixacnpj.delete("4.14", "4.9999")
            self.caixacnpj.delete("5.16", "10.9999")
            """limpar reincidencia"""
            self.caixareincidencia.delete("2.7","2.9999")
            """limpar procuraçao"""
            self.caixaprocuracao.delete("2.7", "2.9999")
            """limpar texto padrao
            self.caixatexto.delete("1.0", tk.END)  # Limpa o texto atual da caixa de texto
            self.caixatexto.insert(tk.INSERT, self.variaveis())"""
        """selecionar o arquivo"""
        def selecionar_arquivo():
            global con
            global crea_entry

            lbl2_selecionado = ctk.CTkLabel(self.frame_1,text="  ",fg_color="#4a89d3")
            lbl2_selecionado.place(relx=0.395, rely=0.45, relwidth=0.05, relheight=0.2)
            lbl_selecionado = ctk.CTkLabel(self.frame_3,text="  ", fg_color='#535353')
            lbl_selecionado.place(relx=0.45, rely=0.10, relwidth=0.15, relheight=0.80)
            limpar()
            file_path = askopenfilename(filetypes=[("Arquivos PDF", "*.pdf")], defaultextension=".pdf")
            """Escreve o nome do arquivo"""
            if file_path:
                partes = file_path.split("Downloads/")
                if len(partes) > 1:
                    depois_downloads = partes[1]
                lbl_selecionado = ctk.CTkLabel(self.frame_3,text=depois_downloads, fg_color='#535353')
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

                        match = re.search(r'CREA[/_-]([a-zA-Z]{2})', text)

                        print(page_num)
                        print(match)
                        if match:

                                crea_entry_result = match.group(1)
                                crea_entry = crea_entry_result.upper()
                                if crea_entry != ['TO',"BA","RN", "AM", "GO", "RS", "MT","RJ",'SP','PR','PA','MG','MS']:
                                    for page_num in range(num_pages):
                                        page = pdf_reader.pages[page_num + 2]
                                        text = page.extract_text()
                                        match2 = re.search(r'CREA[/_-]([a-zA-Z]{2})', text)
                                        if match2:
                                            print(match2)
                                            print("ae crea")
                                            crea_entry_result = match2.group(1)
                                            crea_entry = crea_entry_result.upper()
                                        break
                                lbl2_selecionado = ctk.CTkLabel(self.frame_1, text=crea_entry, fg_color='#4a89d3',text_color='black', bg_color='#094c8c',font=('Lato Regular', 30))
                                lbl2_selecionado.place(relx=0.395, rely=0.45, relwidth=0.05, relheight=0.2)
                                print("1 passo: Procura qual crea_entry")
                                self.valBarra(0.05)
                                #self.barra.set(0.05)
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

                                elif crea_entry == "GO":
                                    print("2.5 passo: Achei qual o Crea")
                                    crea_entrysgo(pdf_file, num_pages, crea_entry)

                                elif crea_entry == "RS" or crea_entry == "MT":
                                    print("2.6 passo: Achei qual o Crea")
                                    crea_entrysrs(pdf_file, num_pages, crea_entry)
                                elif crea_entry == "RJ":
                                    print("2.7 passo: Achei qual o Crea")
                                    crea_entrysrj(pdf_file, num_pages, crea_entry)
                                elif crea_entry == 'SP':
                                    print("2.8 passo: Achei qual o Crea")
                                    crea_entryssp(pdf_file, num_pages, crea_entry)
                                elif crea_entry == 'PR':
                                    print("2.9 passo: Achei qual o Crea")
                                    crea_entryspr(pdf_file, num_pages, crea_entry)
                                elif crea_entry == 'PA':
                                    print("2.10 passo: Achei qual o Crea")
                                    crea_entrys(pdf_file, num_pages, crea_entry)
                                elif crea_entry == 'MG':
                                    print("2.11 passo: Achei qual o Crea")
                                    crea_entrysmg(pdf_file, num_pages, crea_entry)
                                elif crea_entry == 'MS':
                                    print("2.12 passo: Achei qual o Crea")
                                    crea_entrysms(pdf_file, num_pages, crea_entry)
                                elif crea_entry == 'RO':
                                    print("2.13 passo: Achei qual o Crea")
                                    crea_entrysro(pdf_file, num_pages, crea_entry)
                                break
                    #salvar(crea_entry)
                return pdf_reader
##########################################################################################################
#           CREAS TO BA RN AM PA
##########################################################################################################
        """CREAS= TO/BA/RN/AM"""
        def crea_entrys(pdf_file,num_pages,crea_entry):
            global con

            global nsei_ai
            global folhas_ai
            self.valBarra(0.10)
            #self.barra.set(0.10)
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
                    self.valBarra(0.15)
                    print("4 passo: Achei a pagina do AUTO DE INFRAÇÃO")
                    folhas_ai = page_num + 1
                    nsei_ai = result_nsei_entry.group(1)
                    """Inserir numero do Processo SEI"""
                    self.caixaai.insert("2.16", nsei_ai, "red")  # Adiciona a tag "red" ao novo valor
                    self.caixaai.tag_config("red", foreground="red")
                    """Inserir folha do AUTO DE INFRAÇÃO"""
                    self.caixaai.insert("6.11", folhas_ai, "red")  # Adiciona a tag "red" ao novo valor
                    self.caixaai.tag_config("red", foreground="red")  # Configura a cor vermelha para a tag "red"
                    pagedoauto(folhas_ai, pdf_file,num_pages,crea_entry)
                    break
        """EXTRAINDO DADOS DO AUTO DE INFRAÇÃO"""
        def pagedoauto(folhas_ai, pdf_file,num_pages,crea_entry):
            self.valBarra(0.20)
            global nauto_ai
            global multa_ai
            global autuado_ai
            global cnpj_cpf_ai
            global artigo_ai
            global motivo_ai

            global data_aviso
            print("5 passo: Procura todos os dados do AUTO DE INFRAÇÃO")
            pdf_reader = PdfReader(pdf_file)
            page = pdf_reader.pages[folhas_ai - 1]
            text = page.extract_text()
            """Extrai o artigo"""
            artigo = re.search(r'Infração:(.{39})', text)
            print(artigo)
            artigo1_1 = re.search(r'Infração:(.*)', text)
            print(artigo1_1)
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
            action_pos = text.find("OBSERVAÇÃO")
            action_pos2 = text.find("Tipo de")
            if crea_entry != 'PA':
                extracted_text = text[desc_pos + len("DESCRIÇÃO"):action_pos].strip()
            elif crea_entry == 'PA':
                extracted_text = text[desc_pos + len("DESCRIÇÃO"):action_pos2].strip()
            melhora_motivo = extracted_text.replace("\n", "")
            print("6 passo: Achei todos os dados do AUTO DE INFRAÇÃO")
            self.valBarra(0.25)
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
            print(data)

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
                    artigo_ai = 'a alínea "a" Art. 6º da Lei Federal 5.194, de 1966'
                    self.caixaai.insert("3.8", str('a alínea "a" Art. 6º da Lei Federal 5.194, de 1966'),"red")  # Adiciona a tag "red" ao novo valor
                    self.caixaai.tag_config("red", foreground="red")
#                    self.caixatexto.insert("1.275", str('a alinea "a" Art. 6º da Lei Federal 5.194, de 1966'), "red")
#                    self.caixatexto.tag_config("red", foreground="red")
                elif "SEM REGISTRO" in result_artigo or 'S/REGISTRO' in result_artigo :
                    artigo_ai ="Art. 59º da Lei Federal 5.194, de 1966"
                    self.caixaai.insert("3.8", str("Art. 59º da Lei Federal 5.194, de 1966"), "red")  # Adiciona a tag "red" ao novo valor
                    self.caixaai.tag_config("red", foreground="red")
#                    self.caixatexto.insert("1.275", str("ao art. 59º da Lei Federal 5.194, de 1966"), "red")
#                    self.caixatexto.tag_config("red", foreground="red")
                elif "REGISTRO DE ART " in result_artigo:
                    artigo_ai="Art. 1º da Lei Federal 5.194, de 1966"
                    self.caixaai.insert("3.8", str("Art. 1º da Lei Federal 5.194, de 1966"), "red")  # Adiciona a tag "red" ao novo valor
                    self.caixaai.tag_config("red", foreground="red")
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
                elif "CANCELADO" in result_artigo:
                    artigo_ai="Art. 64º da Lei Federal 5.194, de 1966"
                    self.caixaai.insert("3.8", str("Art. 64º da Lei Federal 5.194, de 1966"), "red")  # Adiciona a tag "red" ao novo valor
                    self.caixaai.tag_config("red", foreground="red")
            if melhora_motivo:
                motivo_ai = melhora_motivo.lower()
                self.caixaai.insert("10.10", motivo_ai, "red")
                self.caixaai.tag_config("red", foreground="red")
#                self.caixatexto.insert("1.360", melhora_motivo_min, "red")
#                self.caixatexto.tag_config("red", foreground="red")
            ce(pdf_reader,folhas_ai,crea_entry, pdf_file, num_pages)
        def configdata(data):
            global data_ai
            print("config data")
            dia = data.group(1)
            mes = data.group(2)
            ano = data.group(3)
            if mes == '01' or mes == '1':
                mes_escrito = "janeiro"
                configmes(dia, mes_escrito, ano)
            elif mes == '02' or mes == '2':
                mes_escrito = "fevereiro"
                configmes(dia, mes_escrito, ano)
            elif mes == '03' or mes == '3':
                mes_escrito = "março"
                configmes(dia, mes_escrito, ano)
            elif mes == '04' or mes == '4':
                mes_escrito = "abril"
                configmes(dia, mes_escrito, ano)
            elif mes == '05' or mes == '5':
                mes_escrito = "maio"
                configmes(dia, mes_escrito, ano)
            elif mes == '06' or mes == '6':
                mes_escrito = "junho"
                configmes(dia, mes_escrito, ano)
            elif mes == '07' or mes == '7':
                mes_escrito = "julho"
                configmes(dia, mes_escrito, ano)
            elif mes == '08' or mes == '8':
                mes_escrito = "agosto"
                configmes(dia, mes_escrito, ano)
            elif mes == '09' or mes == '9':
                mes_escrito = "setembro"
                configmes(dia, mes_escrito, ano)
            elif mes == '10':
                mes_escrito = "outubro"
                configmes(dia, mes_escrito, ano)
            elif mes == '11':
                mes_escrito = "novembro"
                configmes(dia, mes_escrito, ano)
            elif mes == '12':
                mes_escrito = "dezembro"
                configmes(dia, mes_escrito, ano)
        def configmes(dia, mes_escrito, ano):
                global data_ai
                print("a data")
                data_ai = f"{dia} de {mes_escrito} de {ano}"

                if data_ai:
                    self.caixaai.insert("9.6", str(data_ai), "red")  # Adiciona a tag "red" ao novo valor
                    self.caixaai.tag_config("red", foreground="red")
                    return data_ai
##########################################################################################################
#           TODOS AS PAGINAS DA CAMARA ESPECIALIZADA
##########################################################################################################
        """Descobre qual a pagina da Camara Especializada"""
        def ce(pdf_reader, folhas_ai,crea_entry, pdf_file, num_pages):
            self.valBarra(0.30)
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
                pagdecisaocamarasp = re.search(r'A Câmara Especializada [Dd]e(.*), reunida ',text2)
                pagdecisaocamararj = re.search(r"A Câmara Especializada [Dd]e (.*) - ",text2)
                pagdecisaocamaramg = re.search(r"A Câmara Especializada [Dd]e (.*) deste", text2)
                pagdecisaocamararo = re.search(r"Câmara Especializada de (.*) do ", text2)
                complemento_pagdecisaocamararj = re.search(r"Decisão da(.*) - ",text2)
                complemento_pagdecisaocamaramg = re.search(r"CE\w+/MG[/ ]n[O^°ºººo]\s?(\d+/\s?\d+)", text2)

                self.valBarra(0.35)
                if (pagdecisaocamaramg or pagdecisaocamarago) and complemento_pagdecisaocamaramg :
                    print("8 passo: Achei a pagina da DECISAO DA CAMARA ESPECIALIZADA")
                    print("9.0 passo: Procura os dados da DECISAO DA CAMARA ESPECIALIZADA")

                    print("10.0 passo: Achei os dados da DECISAO DA CAMARA ESPECIALIZADA")
                    if pagdecisaocamaramg:
                        especialidade_ce = pagdecisaocamaramg.group(1)
                    elif pagdecisaocamarago:
                        especialidade_ce = pagdecisaocamarago.group(1)
                    self.caixace.insert("4.15", especialidade_ce, "red")  # Adiciona a tag "red" ao novo valor
                    self.caixace.tag_config("red", foreground="red")  # Configura a cor vermelha para a tag "red"
                    folhas_ce = page_num + 1
                    # Inserir o novo valor extraído do PDF no widget Text
                    self.caixace.insert("2.8", str(folhas_ce), "red")  # Adiciona a tag "red" ao novo valor
                    self.caixace.tag_config("red", foreground="red")  # Configura a cor vermelha para a tag "red"
                    ndecisaoce = re.search(r'CE\w+/MG[/ ]n[O^°ººo]\s?(\d+/\s?\d+)', text2)
                    complemento_datato = re.search(r'Cientifique-se e cumpra-se', text2)
                    print("10.3 passo: Achei os dados da DECISAO DA CAMARA ESPECIALIZADA")
                    if ndecisaoce:
                        ndecisao_ce = ndecisaoce.group(1)
                        self.caixace.insert("3.12", ndecisao_ce, "red")  # Adiciona a tag "red" ao novo valor
                        self.caixace.tag_config("red", foreground="red")  # Configura a cor vermelha para a tag "red"
                    if crea_entry == 'MG':
                        for page_num in range(folhas_ce, len(pdf_reader.pages)):
                            page = pdf_reader.pages[page_num-1]
                            text4_1 = page.extract_text()
                            complemento_datato = re.search(r'Cientifique-se e cumpra-se', text4_1)
                            if complemento_datato:
                                datato = re.search(r', (\d{2}) de (\w+) de (\d{4})', text4_1)

                                if datato:
                                    print("datamg", datato)
                                    data_ce = datato.group()
                                    self.caixace.insert("5.6", data_ce, "red")  # Adiciona a tag "red" ao novo valor
                                    self.caixace.tag_config("red", foreground="red")
                                    break
                        multa(pdf_reader, folhas_ce, crea_entry, pdf_file, num_pages)
                    break

                if pagdecisaocamarasp:
                    print("8 passo: Achei a pagina da DECISAO DA CAMARA ESPECIALIZADA")
                    print("9.1 passo: Procura os dados da DECISAO DA CAMARA ESPECIALIZADA")

                    print("10.1 passo: Achei os dados da DECISAO DA CAMARA ESPECIALIZADA")
                    especialidade_ce = pagdecisaocamarasp.group(1)
                    self.caixace.insert("4.15", especialidade_ce, "red")  # Adiciona a tag "red" ao novo valor
                    self.caixace.tag_config("red", foreground="red")  # Configura a cor vermelha para a tag "red"
                    folhas_ce = page_num + 1
                    # Inserir o novo valor extraído do PDF no widget Text
                    self.caixace.insert("2.8", str(folhas_ce), "red")  # Adiciona a tag "red" ao novo valor
                    self.caixace.tag_config("red", foreground="red")  # Configura a cor vermelha para a tag "red"
                    page2 = pdf_reader.pages[page_num]
                    text3 = page2.extract_text()
                    ndecisaoce = re.search(r'CE\w+/SP n[O^°ººo]\s?(\d+/\s?\d+)', text2)
                    print("10.3 passo: Achei os dados da DECISAO DA CAMARA ESPECIALIZADA")
                    if ndecisaoce:
                        ndecisao_ce = ndecisaoce.group(1)
                        self.caixace.insert("3.12", ndecisao_ce, "red")  # Adiciona a tag "red" ao novo valor
                        self.caixace.tag_config("red", foreground="red")  # Configura a cor vermelha para a tag "red"
                    elif ndecisaoce is None:
                        ndecisaoce2 = re.search(r'CE\w+/SP n.[O^°ººo]\s?(\d+/\s?\d+)', text2)
                        if ndecisaoce2:
                            ndecisao_ce = ndecisaoce2.group(1)
                            self.caixace.insert("3.12", ndecisao_ce, "red")  # Adiciona a tag "red" ao novo valor
                            self.caixace.tag_config("red", foreground="red")  # Configura a cor vermelha para a tag "red"
                    if crea_entry == "SP":
                        for page_num in range(folhas_ce, len(pdf_reader.pages)):
                            page = pdf_reader.pages[page_num-1]
                            text4_2 = page.extract_text()

                            complemento_datato = re.search(r'Cientifique-se e cumpra-se', text4_2)
                            if complemento_datato:
                                datato = re.search(r',(.*)de [A-Z][a-z]+ de (\d{4})', text4_2)
                                if datato:
                                    print("datato",datato)
                                    data_ce = datato.group()
                                    self.caixace.insert("5.6", data_ce, "red")  # Adiciona a tag "red" ao novo valor
                                    self.caixace.tag_config("red", foreground="red")
                                    break
                                elif datato is None:
                                    datato2 = re.search(r', (\d{2}) de (\w+) de (\d{4})', text4_2)
                                    datato3 = re.search(r', (.*) de (\d{4})', text4_2)
                                    if datato2:
                                        print("datato2", datato2)
                                        data_ce = datato2.group()
                                        self.caixace.insert("5.6", data_ce, "red")  # Adiciona a tag "red" ao novo valor
                                        self.caixace.tag_config("red", foreground="red")
                                        break
                                    elif datato3:
                                        print("datato3", datato3)
                                        data_ce = datato3.group()
                                        self.caixace.insert("5.6", data_ce, "red")  # Adiciona a tag "red" ao novo valor
                                        self.caixace.tag_config("red", foreground="red")
                                        break
                    multa(pdf_reader, folhas_ce, crea_entry, pdf_file, num_pages)
                    break
                if pagdecisaocamaraam:
                    print("8 passo: Achei a pagina da DECISAO DA CAMARA ESPECIALIZADA")
                    print("9.2 passo: Procura os dados da DECISAO DA CAMARA ESPECIALIZADA")
                    pagdecisaocamara = pagdecisaocamaraam
                    print("10.2 passo: Achei os dados da DECISAO DA CAMARA ESPECIALIZADA")
                    especialidade_ce = pagdecisaocamara.group(1)
                    self.caixace.insert("4.15", especialidade_ce, "red")  # Adiciona a tag "red" ao novo valor
                    self.caixace.tag_config("red", foreground="red")  # Configura a cor vermelha para a tag "red"
                    folhas_ce = page_num + 1
                    # Inserir o novo valor extraído do PDF no widget Text
                    self.caixace.insert("2.8", str(folhas_ce), "red")  # Adiciona a tag "red" ao novo valor
                    self.caixace.tag_config("red", foreground="red")  # Configura a cor vermelha para a tag "red"
                    page2 = pdf_reader.pages[page_num]
                    text3 = page2.extract_text()
                    ndecisaoce = re.search(r'Decisão:(.+)', text2)

                    if ndecisaoce:
                        ndecisao_ce = ndecisaoce.group(1)
                        self.caixace.insert("3.12", ndecisao_ce, "red")  # Adiciona a tag "red" ao novo valor
                        self.caixace.tag_config("red", foreground="red")  # Configura a cor vermelha para a tag "red"
                    if crea_entry == "TO":
                        for page_num in range(folhas_ce, len(pdf_reader.pages)):
                            page = pdf_reader.pages[page_num]
                            text4 = page.extract_text()
                            datato = re.search(r'\/TO, (.+)\.', text4)
                            if datato:
                                data_ce = datato.group(1)
                                self.caixace.insert("5.6", data_ce, "red")  # Adiciona a tag "red" ao novo valor
                                self.caixace.tag_config("red", foreground="red")
                                break
                    if crea_entry == "BA":
                        data3 = re.search(r', (\d{2}) de (\d{2}) de (\d{4})\.', text3)
                        if data3:

                            data_ce = data3.group(1)
                            self.caixace.insert("5.6", data_ce, "red")  # Adiciona a tag "red" ao novo valor
                            self.caixace.tag_config("red", foreground="red")
                        data2 = re.search(r'- (\d{2})/(\d{2})/(\d{4})', text3)
                        if data2:

                            configdata2(data2)
                        multa(pdf_reader, folhas_ce, crea_entry, pdf_file)
                        break
                    if crea_entry == "AM":
                        for page_num in range(folhas_ce, len(pdf_reader.pages)):
                            page = pdf_reader.pages[page_num-1]
                            text4 = page.extract_text()
                            data2 = re.search(r'- (\d{2})/(\d{2})/(\d{4})', text4)
                            if data2:
                                configdata2(data2)
                                break
                    multa(pdf_reader, folhas_ce, crea_entry, pdf_file, num_pages)
                    break
                if (pagdecisaocamarago or pagdecisaocamarago2 or pagdecisaocamararj) and (crea_entry == 'GO' or crea_entry == 'RJ' or crea_entry == 'BA' or crea_entry =='RN' or crea_entry =='RS'  or crea_entry =='TO' or crea_entry == 'PA'):
                    if pagdecisaocamarago2:
                        print("v1")
                        pagdecisaocamarago3 = re.search(r'A Câmara Especializada de (.*) do', text2)
                        if pagdecisaocamarago3:
                            especialidade_ce = pagdecisaocamarago3.group(1)
                            self.caixace.insert("4.15", especialidade_ce,"red")  # Adiciona a tag "red" ao novo valor
                            self.caixace.tag_config("red", foreground="red")  # Configura a cor vermelha para a tag "red"

                        pagdecisaocamarago = pagdecisaocamarago2
                    if crea_entry == "TO":
                        folhas_ce = page_num + 1
                        for page_num in range(folhas_ce, len(pdf_reader.pages)):
                            page = pdf_reader.pages[page_num]
                            text4 = page.extract_text()
                            datato = re.search(r'\/TO, (.+)\.', text4)
                            if datato:
                                data_ce = datato.group(1)
                                self.caixace.insert("5.6", data_ce, "red")  # Adiciona a tag "red" ao novo valor
                                self.caixace.tag_config("red", foreground="red")
                                break
                    print("8 passo: Achei a pagina da DECISAO DA CAMARA ESPECIALIZADA")
                    print("9.2 passo: Procura os dados da DECISAO DA CAMARA ESPECIALIZADA")
                    if pagdecisaocamarago:
                        print("v3")
                        especialidade_ce = pagdecisaocamarago.group(1).strip()
                        # Removendo a palavra "De" caso ela esteja presente
                        especialidade_ce = especialidade_ce.replace("De ", "")
                    if pagdecisaocamararj:
                        print("v2")
                        especialidade_ce = pagdecisaocamararj.group(1)
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

                        self.valBarra(0.25)
                        self.caixace.insert("3.12", ndecisao_ce,"red")  # Adiciona a tag "red" ao novo valor
                        self.caixace.tag_config("red", foreground="red")

                    ndecisaoce = re.search(r'Decisão:(.+)', text2)


                    datace = re.search(r', (\d{1,2}) de (.*) de (\d{4})', text3)
                    datace2= re.search(r', (\d{1,2})(.*) de (\d{4}).',text3)
                    datace3= re.search(r', (\d{1,2}) de (\w+) de (\d{4})\.', text3)
                    if datace3 and crea_entry =='RJ':
                        data_ce = datace3.group()
                        print(data_ce)
                        self.caixace.insert("5.6", data_ce, "red")  # Adiciona a tag "red" ao novo valor
                        self.caixace.tag_config("red", foreground="red")
                    if datace2:

                        datace = datace2
                    print("10.2 passo: Achei os dados da DECISAO DA CAMARA ESPECIALIZADA")
                    print(datace)
                    if ndecisaoce:
                        ndecisao_ce = ndecisaoce.group(1)
                        self.caixace.insert("3.12", ndecisao_ce, "red")  # Adiciona a tag "red" ao novo valor
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
                if (pagdecisaocamara and (crea_entry == 'MT' or crea_entry == 'MS')):
                    print("8 passo: Achei a pagina da DECISAO DA CAMARA ESPECIALIZADA")
                    print("9.3 passo: Procura os dados da DECISAO DA CAMARA ESPECIALIZADA")
                    especialidade_ce = pagdecisaocamara.group(1)
                    self.caixace.insert("4.15", especialidade_ce, "red")  # Adiciona a tag "red" ao novo valor
                    self.caixace.tag_config("red", foreground="red")  # Configura a cor vermelha para a tag "red"
                    folhas_ce = page_num + 1
                    # Inserir o novo valor extraído do PDF no widget Text
                    self.caixace.insert("2.8", str(folhas_ce), "red")  # Adiciona a tag "red" ao novo valor
                    self.caixace.tag_config("red", foreground="red")  # Configura a cor vermelha para a tag "red"
                    page2 = pdf_reader.pages[page_num]
                    text3 = page2.extract_text()
                    print(text3)
                    ndecisaoce = re.search(r'Decisão:(.+)', text2)
                    ndecisaoce2 = re.search(r'Decis([^n]+n°[^ ]+)', text2)
                    ndecisaoce3 = re.search(r'CE\w+/MS n[º] (\d+ /\d+)', text2)
                    print(ndecisaoce3)
                    print("10.3 passo: Achei os dados da DECISAO DA CAMARA ESPECIALIZADA")
                    if ndecisaoce or ndecisaoce2 or ndecisaoce3:
                        if ndecisaoce:
                            result_ndecisaoce = ndecisaoce.group(1)
                        if ndecisaoce2:
                            ndecisao_ce = ndecisaoce2.group(1)
                        if ndecisaoce3:
                            ndecisao_ce = ndecisaoce3.group()
                        self.caixace.insert("3.12", ndecisao_ce, "red")  # Adiciona a tag "red" ao novo valor
                        self.caixace.tag_config("red", foreground="red")  # Configura a cor vermelha para a tag "red"
                    if crea_entry == "MS":
                        data2 = re.search(r', (\d{2})/(\d{1,2})\s?/(\d{4})', text3)
                        if data2:
                            configdata2(data2)
                    if crea_entry == "BA":
                        data3 = re.search(r', (\d{2}) de (\d{2}) de (\d{4})\.', text3)
                        if data3:

                            data_ce = data3.group(1)
                            self.caixace.insert("5.6", data_ce, "red")  # Adiciona a tag "red" ao novo valor
                            self.caixace.tag_config("red", foreground="red")
                        data2 = re.search(r'- (\d{2})/(\d{2})/(\d{4})', text3)
                        if data2:
                            configdata2(data2)
                    if crea_entry == "GO":
                        datace = re.search(r', (\d{2}) de (.*) de (\d{4})', text3)
                        result_datace = datace.group()
                        data_ce = result_datace[2:]
                        self.caixace.insert("5.6", data_ce, "red")  # Adiciona a tag "red" ao novo valor
                        self.caixace.tag_config("red", foreground="red")
                    if crea_entry == "MT":
                        datace = re.search(r'MT no dia (\d{2}) de (.*) de (\d{4})', text3)
                        result_datace = datace.group()
                        data_ce = result_datace[2:]
                        self.caixace.insert("5.6", data_ce, "red")  # Adiciona a tag "red" ao novo valor
                        self.caixace.tag_config("red", foreground="red")
                    if crea_entry == "RS":
                            decisao_desc_pos = text3.find(" - CE")
                            decisao_action_pos = text3.find("Referência")
                            extractedrs_text = text3[decisao_desc_pos + len(" - CE"):decisao_action_pos].strip()
                            melhora_decisao = extractedrs_text.replace("\n", "")
                            print("oi")
                            self.valBarra(0.25)
                            if melhora_decisao:
                                self.caixace.insert("3.12", "CE" + melhora_decisao, "red")  # Adiciona a tag "red" ao novo valor
                                self.caixace.tag_config("red", foreground="red")
                                for page_num in range(folhas_ce, len(pdf_reader.pages)):
                                    page = pdf_reader.pages[page_num - 1]
                                    text4 = page.extract_text()
                                    datacers = re.search(r', (\d{2}) de (.*) de (\d{4})\.', text4)


                                    if datacers:
                                        result_datacers = datacers.group()
                                        result_datacers_real = result_datacers[2:]
                                        self.caixace.insert("5.6", result_datacers_real,"red")  # Adiciona a tag "red" ao novo valor
                                        self.caixace.tag_config("red", foreground="red")
                                        break


                    multa(pdf_reader, folhas_ce,crea_entry,pdf_file, num_pages)
                    break
                if (pagdecisaocamararo) and crea_entry == 'RO':
                    print("8 passo: Achei a pagina da DECISAO DA CAMARA ESPECIALIZADA")
                    print("9.4 passo: Procura os dados da DECISAO DA CAMARA ESPECIALIZADA")
                    especialidade_ce = pagdecisaocamararo.group(1)
                    self.caixace.insert("4.15", especialidade_ce, "red")  # Adiciona a tag "red" ao novo valor
                    self.caixace.tag_config("red", foreground="red")  # Configura a cor vermelha para a tag "red"
                    folhas_ce = page_num + 1
                    # Inserir o novo valor extraído do PDF no widget Text
                    self.caixace.insert("2.8", str(folhas_ce), "red")  # Adiciona a tag "red" ao novo valor
                    self.caixace.tag_config("red", foreground="red")  # Configura a cor vermelha para a tag "red"
                    page2 = pdf_reader.pages[page_num]
                    text3 = page2.extract_text()

                    ndecisaoce = re.search(r'Decisão C. Especializada: (.+)', text2)
                    print("10.3 passo: Achei os dados da DECISAO DA CAMARA ESPECIALIZADA")
                    if ndecisaoce:
                        ndecisao_ce = ndecisaoce.group(1)                     
                        self.caixace.insert("3.12", ndecisao_ce, "red")  # Adiciona a tag "red" ao novo valor
                        self.caixace.tag_config("red", foreground="red")  # Configura a cor vermelha para a tag "red"
                    if crea_entry == "RO":
                        data3 = re.search(r', (\d{2}) de (\w+) de (\d{4})\.', text3)
                        if data3:
                            data_ce = data3.group()
                            self.caixace.insert("5.6", data_ce, "red")  # Adiciona a tag "red" ao novo valor
                            self.caixace.tag_config("red", foreground="red")
                    multa(pdf_reader, folhas_ce, crea_entry, pdf_file, num_pages)
                    break
        """Descobrindo a Data"""
        def configdata2(data2):
            print("entrou configdata2")
            dia2 = data2.group(1)
            mes2 = data2.group(2)
            ano2 = data2.group(3)
            if mes2 == '01' or mes2 == '1':
                mes_escrito2 = "janeiro"
                configmes2(dia2,mes_escrito2,ano2)
            elif mes2 == '02' or mes2 == '2':
                mes_escrito2 = "fevereiro"
                configmes2(dia2,mes_escrito2,ano2)
            elif mes2 == '03' or mes2 == '3':
                mes_escrito2 = "março"
                configmes2(dia2,mes_escrito2,ano2)
            elif mes2 == '04' or mes2 == '4':
                mes_escrito2 = "abril"
                configmes2(dia2,mes_escrito2,ano2)
            elif mes2 == '05' or mes2 == '5':
                mes_escrito2 = "maio"
                configmes2(dia2,mes_escrito2,ano2)
            elif mes2 == '06' or  mes2 == '6':
                mes_escrito2 = "junho"
                configmes2(dia2,mes_escrito2,ano2)
            elif mes2 == '07' or mes2 == '7':
                mes_escrito2 = "julho"
                configmes2(dia2,mes_escrito2,ano2)
            elif mes2 == '08'or mes2 == '8':
                mes_escrito2 = "agosto"
                configmes2(dia2,mes_escrito2,ano2)
            elif mes2 == '09' or mes2 == '9':
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

            self.valBarra(0.40)
            data_formatada2 = f"{dia2} de {mes_escrito2} de {ano2}"
            if data_formatada2:
                self.caixace.insert("5.6", str(data_formatada2), "red")  # Adiciona a tag "red" ao novo valor
                self.caixace.tag_config("red", foreground="red")
        def multa(pdf_reader, folhas_ce,crea_entry, pdf_file, num_pages):
            self.valBarra(0.45)
            global multa_ce
            print("Multa da camara")
            if crea_entry in ['GO', 'AM', 'BA', 'MT', 'RN', 'RJ', 'SP', 'PA', 'MG', 'MS', 'RO']:

                for page_num in range(folhas_ce, len(pdf_reader.pages)):
                    page = pdf_reader.pages[page_num - 1]
                    text3 = page.extract_text()

                    multacego_action_pos = text3.find("Coordenou ")
                    multacego_action_pos2 = text3.find(". Presidiu")
                    multacego_action_pos3 = text3.find(" B) ")
                    multacego_action_pos4 = text3.find("; 2) ")
                    multacego_desc_pos = text3.find("DECIDIU[: ]")
                    if multacego_action_pos != -1:
                        print("coordenou")
                        multacego_extracted_text = text3[multacego_desc_pos + len("DECIDIU[: ]"):multacego_action_pos].strip()
                        multacego_melhora = multacego_extracted_text.replace("\n", "")

                        if multacego_melhora:
                                if 'redução' in multacego_melhora or 'MINIMO' in multacego_melhora or 'mínimo' in multacego_melhora:
                                    multa_ce = 'reduziu'
                                    self.caixace.insert("6.6", "reduziu","red")  # Adiciona a tag "red" ao novo valor
                                    self.caixace.tag_config("red", foreground="red")
                                elif "manutenção"in multacego_melhora or "Manutenção" in multacego_melhora or "MANUTENÇÃO" in multacego_melhora or "Manter"in multacego_melhora or 'máximo' in multacego_melhora:
                                    multa_ce = 'manteve'
                                    self.caixace.insert("6.6", "manteve","red")  # Adiciona a tag "red" ao novo valor
                                    self.caixace.tag_config("red", foreground="red")
                        break
                    elif multacego_action_pos2 != -1:
                        multacego_extracted_text = text3[multacego_desc_pos + len("DECIDIU[: ]"):multacego_action_pos2].strip()
                        multacego_melhora = multacego_extracted_text.replace("\n", "")
                        print("presidiu")
                        if multacego_melhora:
                            if 'redução' in multacego_melhora or 'MINIMO' in multacego_melhora or 'mínimo' in multacego_melhora:
                                multa_ce = 'reduziu'
                                self.caixace.insert("6.6", "reduziu","red")  # Adiciona a tag "red" ao novo valor
                                self.caixace.tag_config("red", foreground="red")
                            elif "manutenção" in multacego_melhora or 'manutenção' in multacego_melhora  or "MANUTENÇÃO" in multacego_melhora or "Manter"in multacego_melhora or 'máximo' in multacego_melhora:
                                multa_ce = 'manteve'
                                self.caixace.insert("6.6", "manteve","red")  # Adiciona a tag "red" ao novo valor
                                self.caixace.tag_config("red", foreground="red")
                        break
                    elif multacego_action_pos3 != -1:
                        multacego_extracted_text = text3[multacego_desc_pos + len("DECIDIU[: ]"):multacego_action_pos3].strip()
                        multacego_melhora = multacego_extracted_text.replace("\n", "")
                        print("B")
                        if multacego_melhora:
                            if "redução" in multacego_melhora:
                                multa_ce = 'reduziu'
                                self.caixace.insert("6.6", "reduziu", "red")  # Adiciona a tag "red" ao novo valor
                                self.caixace.tag_config("red", foreground="red")
                            elif "manutenção" in multacego_melhora or 'manutenção' in multacego_melhora or "MANUTENÇÃO" in multacego_melhora or "Manter" in multacego_melhora or 'máximo' in multacego_melhora:
                                multa_ce = 'manteve'
                                self.caixace.insert("6.6", "manteve", "red")  # Adiciona a tag "red" ao novo valor
                                self.caixace.tag_config("red", foreground="red")
                        break
                    elif multacego_action_pos4 != -1:
                        multacego_extracted_text = text3[multacego_desc_pos + len("DECIDIU[: ]"):multacego_action_pos4].strip()
                        multacego_melhora = multacego_extracted_text.replace("\n", "")
                        print("2)")
                        if multacego_melhora:
                            if "redução" in multacego_melhora:
                                multa_ce = 'reduziu'
                                self.caixace.insert("6.6", "reduziu", "red")  # Adiciona a tag "red" ao novo valor
                                self.caixace.tag_config("red", foreground="red")
                            elif "manutenção" in multacego_melhora or 'manutenção' in multacego_melhora or "MANUTENÇÃO" in multacego_melhora or "Manter" in multacego_melhora or 'máximo' in multacego_melhora:
                                multa_ce = 'manteve'
                                self.caixace.insert("6.6", "manteve", "red")  # Adiciona a tag "red" ao novo valor
                                self.caixace.tag_config("red", foreground="red")
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
                                multa_ce = 'reduziu'
                                self.caixace.insert("6.6", "reduziu para valor minimo",
                                                    "red")  # Adiciona a tag "red" ao novo valor
                                self.caixace.tag_config("red", foreground="red")
                            elif "manutenção" in multacego_melhora:
                                multa_ce = 'manteve'
                                self.caixace.insert("6.6", "manteve o valor da multa",
                                                    "red")  # Adiciona a tag "red" ao novo valor
                                self.caixace.tag_config("red", foreground="red")
                        break

                plcrea_entry(pdf_reader, folhas_ce,crea_entry, pdf_file, num_pages)
        """Descobre qual a pagina da Decisao Plenaria"""
        def plcrea_entry(pdf_reader, folhas_ce,crea_entry, pdf_file, num_pages):

            self.valBarra(0.50)
            global folhas_pl
            global ndecisao_pl
            global data_pl
            print("11 passo: Procurar a pagina da DECISAO PLENARIA")
            for page_num in range(folhas_ce, len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                text3 = page.extract_text()

                pagdecisaoplenaria = re.search(r'\bO (Plen[áa]rio|Plendrio|Plenario) do Conse[li]ho Regional \b(.*)', text3)
                pagdecisaoplenariaerro = None
                if crea_entry == 'RO':
                    pagdecisaoplenariaerro = re.search(r'Decisão Plenária:  PL/RO Nº. (\d+/\d+)', text3)
                    if pagdecisaoplenariaerro:
                        folhas_pl = page_num + 1
                        print("hello ro")
                        self.caixapl.insert("2.8", folhas_pl, "red")  # Adiciona a tag "red" ao novo valor
                        self.caixapl.tag_config("red", foreground="red")
                        ndecisao_pl = pagdecisaoplenariaerro.group()
                        self.caixapl.insert("3.12", ndecisao_pl, "red")  # Adiciona a tag "red" ao novo valor
                        self.caixapl.tag_config("red", foreground="red")
                        if folhas_pl:
                            print("entrou na folha")
                            for page_num in range(folhas_pl, len(pdf_reader.pages)):
                                print("entrou no for")
                                page = pdf_reader.pages[page_num - 1]
                                text5 = page.extract_text()
                                datatopl = re.search(r', (\d{2}) de (.*) de (\d{4})\.', text5)
                                print(datatopl)
                                print("14_3 passo: Achei os dados da DECISÃO PLENARIA")
                                if datatopl:
                                    print("carai de asa", datatopl)
                                    result_datapl = datatopl.group()
                                    data_pl = result_datapl[2:]
                                    self.caixapl.insert("4.6", data_pl, "red")  # Adiciona a tag "red" ao novo valor
                                    self.caixapl.tag_config("red", foreground="red")
                                    break
                        break

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
                    #self.caixapl.insert("2.8", str(folhas_pl), "red")  # Adiciona a tag "red" ao novo valor
                    #self.caixapl.tag_config("red", foreground="red")

                    ndecisaopl2 = re.search(r'Decisão:(.+)', text3)
                    ndecisaopl4 = re.search(r'Decisão Plenária:(.+)', text4)
                    ndecisaopl = re.search(r'Decisão Plenária\s*:\s*(?:PL/BA\s+)?Nº\s*(\d+/\d+)', text4)
                    ndecisaopl5 = re.search(r'DECISAO:(.+)', text3)
                    ndecisaopl3 = re.search(r'Decisão N\.:(.+)', text3)
                    ndecisaopl7 = re.search(r'Decisão PL/SP n[- °®](.+)',text3)
                    ndecisaopl7_1 = re.search(r'Decisão PL/SP (.+)',text3)
                    ndecisaopl8 = re.search(r'Decisão Plenária[]PL/MG n[o °®](.+)',text3)
                    if pagdecisaoplenariaerro is None:
                        ndecisaopl6 = re.search(r'Decisão Plenária (.+)',text4)
                    else:
                        ndecisaopl6 = pagdecisaoplenariaerro
                    print("13 passo: Procura dados da DECISAO PLENARIA")
                    if ndecisaopl:
                        print("1")
                        ndecisao_pl = ndecisaopl.group(1)
                        self.caixapl.insert("3.12", ndecisao_pl, "red")  # Adiciona a tag "red" ao novo valor
                        self.caixapl.tag_config("red", foreground="red")
                    elif ndecisaopl2:
                        print("2")
                        ndecisao_pl = ndecisaopl2.group(1)
                        self.caixapl.insert("3.12", ndecisao_pl, "red")  # Adiciona a tag "red" ao novo valor
                        self.caixapl.tag_config("red", foreground="red")
                    elif ndecisaopl3:
                        print("3")
                        ndecisao_pl = ndecisaopl3.group(1)
                        self.caixapl.insert("3.12", ndecisao_pl, "red")  # Adiciona a tag "red" ao novo valor
                        self.caixapl.tag_config("red", foreground="red")
                    elif ndecisaopl5:
                        print("4")
                        ndecisao_pl = ndecisaopl5.group(1)
                        self.caixapl.insert("3.12", ndecisao_pl, "red")  # Adiciona a tag "red" ao novo valor
                        self.caixapl.tag_config("red", foreground="red")
                    elif ndecisaopl4:
                        print("5")
                        ndecisao_pl = ndecisaopl4.group(1)
                        self.caixapl.insert("3.12", ndecisao_pl, "red")  # Adiciona a tag "red" ao novo valor
                        self.caixapl.tag_config("red", foreground="red")
                    elif ndecisaopl7:
                        print("6")
                        ndecisao_pl=ndecisaopl7.group(1)
                        self.caixapl.insert("3.12", ndecisao_pl, "red")  # Adiciona a tag "red" ao novo valor
                        self.caixapl.tag_config("red", foreground="red")
                    elif ndecisaopl7_1:
                        print("7")
                        ndecisao_pl = ndecisaopl7_1.group(1)
                        self.caixapl.insert("3.12", ndecisao_pl, "red")  # Adiciona a tag "red" ao novo valor
                        self.caixapl.tag_config("red", foreground="red")
                    elif ndecisaopl8:
                        print("8")
                        ndecisao_pl = ndecisaopl8.group(1)
                        self.caixapl.insert("3.12", ndecisao_pl, "red")  # Adiciona a tag "red" ao novo valor
                        self.caixapl.tag_config("red", foreground="red")

                    """if crea_entry == 'MG':
                        for page_num in range(folhas_pl, len(pdf_reader.pages)):
                            page = pdf_reader.pages[page_num - 1]
                            text5 = page.extract_text()
                            datatopl = re.search(r', (\d{1,2}) de (.*) de (\d{4})\.',text5)
                            if datatopl:
                                print("data", datatopl)
                                result_datapl = datatopl.group()
                                result_data_pl = re.search(r'\d.*', result_datapl)
                                if result_data_pl:
                                    data_pl = result_data_pl.group()
                                    self.caixapl.insert("4.6", data_pl, "red")  # Adiciona a tag "red" ao novo valor
                                    self.caixapl.tag_config("red", foreground="red")
                                break"""
                    if crea_entry == 'RJ':
                        for page_num in range(folhas_pl, len(pdf_reader.pages)):
                            page = pdf_reader.pages[page_num - 1]
                            text5 = page.extract_text()
                            datatopl = re.search(r'([a-z]+), (\d{1,2} [\dd][ ^e][ /]([a-z]+) de \d{4})', text5)
                            datatopl2 = re.search(r', (\d{1,2}) de (.*) de (\d{4})',text5)
                            if datatopl2:
                                datatopl = datatopl2

                            print("14_1 passo: Achei os dados da DECISÃO PLENARIA")
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
                        for page_num in range(folhas_pl, len(pdf_reader.pages)):
                            page = pdf_reader.pages[page_num - 1]
                            text5 = page.extract_text()
                            datatopl = re.search(r', (\d{2}) de (.*) de (\d{4})', text5)
                            print("14_2 passo: Achei os dados da DECISÃO PLENARIA")
                            if datatopl:
                                result_datapl = datatopl.group()
                                data_pl = result_datapl[2:]
                                self.caixapl.insert("4.6", data_pl, "red")  # Adiciona a tag "red" ao novo valor
                                self.caixapl.tag_config("red", foreground="red")
                                break
                    if crea_entry == 'AM' or crea_entry =='SP' or crea_entry == 'PA' or crea_entry=='MG':
                        print("creas aqui")
                        for page_num in range(folhas_pl, len(pdf_reader.pages)):
                            page = pdf_reader.pages[page_num - 1]
                            text5 = page.extract_text()
                            datatopl = re.search(r', (\d{2}) de (.*) de (\d{4})\.', text5)
                            print(datatopl)
                            print("14_3 passo: Achei os dados da DECISÃO PLENARIA")
                            if datatopl:
                                print("carai de asa",datatopl)
                                result_datapl = datatopl.group()
                                data_pl = result_datapl[2:]
                                self.caixapl.insert("4.6", data_pl, "red")  # Adiciona a tag "red" ao novo valor
                                self.caixapl.tag_config("red", foreground="red")
                                break
                        break
                        multapl(pdf_reader, folhas_pl, crea_entry, pdf_file, num_pages)
                    if crea_entry == "MT":
                        for page_num in range(folhas_pl, len(pdf_reader.pages)):
                            page = pdf_reader.pages[page_num - 1]
                            text5 = page.extract_text()
                            datatopl = re.search(r', reunido em (\d{2}) de (.*) de (\d{4})', text5)
                            print("14-4 passo: Achei os dados da DECISÃO PLENARIA")
                            if datatopl:
                                result_datapl = datatopl.group()
                                data_pl = result_datapl[2:]
                                self.caixapl.insert("4.6", data_pl, "red")  # Adiciona a tag "red" ao novo valor
                                self.caixapl.tag_config("red", foreground="red")
                                break
                    if crea_entry == 'BA':
                        for page_num in range(folhas_pl, len(pdf_reader.pages)):
                            page = pdf_reader.pages[page_num - 1]
                            text5 = page.extract_text()

                            datatopl = re.search(r',\s*(\d{1,2})\s+de\s+(\w+)\s+de\s+(\d{4})', text5)

                            print("14_5 passo: Achei os dados da DECISÃO PLENARIA")
                            if datatopl:
                                result_datapl = datatopl.group()
                                data_pl = result_datapl[2:]
                                self.caixapl.insert("4.6", data_pl, "red")  # Adiciona a tag "red" ao novo valor
                                self.caixapl.tag_config("red", foreground="red")
                                break
                    elif crea_entry == "TO":
                        for page_num in range(folhas_pl, len(pdf_reader.pages)):
                            page = pdf_reader.pages[page_num]
                            text5 = page.extract_text()
                            datatopl = re.search(r'TO, (.+)\.', text5)
                            print("14_6 passo: Achei os dados da DECISÃO PLENARIA")
                            if datatopl:
                                data_pl = datatopl.group(1)
                                self.caixapl.insert("4.6", data_pl, "red")  # Adiciona a tag "red" ao novo valor
                                self.caixapl.tag_config("red", foreground="red")
                                break
                    elif  crea_entry == "RS":
                            datatopl = re.search(r'Data:(.+)\.', text3)
                            print("14_7 passo: Achei os dados da DECISÃO PLENARIA")
                            if datatopl:
                                data_pl = datatopl.group(1)
                                self.caixapl.insert("4.6", data_pl, "red")  # Adiciona a tag "red" ao novo valor
                                self.caixapl.tag_config("red", foreground="red")
                                break


            multapl(pdf_reader, folhas_pl,crea_entry, pdf_file, num_pages)
        def multapl(pdf_reader, folhas_pl,crea_entry, pdf_file, num_pages):
            self.valBarra(0.55)
            global multa_pl
            print("entrou na multa")
            if crea_entry in ['GO','BA','RJ','AM','PA','MG','RO']:
                for page_num in range(folhas_pl, len(pdf_reader.pages)):
                    page = pdf_reader.pages[page_num-1]
                    text6 = page.extract_text()
                    multaplgo_action_pos = text6.find(". Coordenou ")
                    multaplgo_action_pos2 = text6.find(". Presidiu")
                    multaplgo_action_pos3 = text6.find("; 2) ")
                    multaplgo_desc_pos = text6.find("[.,;] DECIDIU[: ]")
                    print("procurando a multa")
                    if multaplgo_action_pos != -1:

                        ("achou a multa1")
                        multaplgo_extracted_text = text6[multaplgo_desc_pos + len(" voto "):multaplgo_action_pos].strip()
                        multaplgo_melhora = multaplgo_extracted_text.replace("\n", "")
                        if multaplgo_melhora:
                            if "redução" in multaplgo_melhora:
                                multa_pl = 'reduziu'
                                self.caixapl.insert("5.6","reduziu","red")  # Adiciona a tag "red" ao novo valor
                                self.caixapl.tag_config("red", foreground="red")
                            elif "manutenção" in multaplgo_melhora or "Manutenção" in multaplgo_melhora:
                                multa_pl = 'manteve'
                                self.caixapl.insert("5.6", "manteve","red")  # Adiciona a tag "red" ao novo valor
                                self.caixapl.tag_config("red", foreground="red")

                        break
                    elif multaplgo_action_pos2 != -1:
                        print("achou a multa2")
                        multaplgo_extracted_text = text6[multaplgo_desc_pos + len("[.,] DECIDIU[: ]"):multaplgo_action_pos2].strip()
                        multaplgo_melhora = multaplgo_extracted_text.replace("\n", "")
                        if multaplgo_melhora:

                            if "redução" in multaplgo_melhora:
                                multa_pl = 'reduziu'
                                self.caixapl.insert("5.6", "reduziu","red")  # Adiciona a tag "red" ao novo valor
                                self.caixapl.tag_config("red", foreground="red")
                            elif "manutenção" in multaplgo_melhora or "MANUTENÇÃO" in multaplgo_melhora:
                                multa_pl = 'manteve'
                                self.caixapl.insert("5.6", "manteve","red")  # Adiciona a tag "red" ao novo valor
                                self.caixapl.tag_config("red", foreground="red")
                        break
                    elif multaplgo_action_pos3 != -1:
                        print("achou a multa3")
                        multaplgo_extracted_text = text6[multaplgo_desc_pos + len("[.,] DECIDIU[: ]"):multaplgo_action_pos2].strip()
                        multaplgo_melhora = multaplgo_extracted_text.replace("\n", "")
                        if multaplgo_melhora:

                            if "redução" in multaplgo_melhora:
                                multa_pl = 'reduziu'
                                self.caixapl.insert("5.6", "reduziu", "red")  # Adiciona a tag "red" ao novo valor
                                self.caixapl.tag_config("red", foreground="red")
                            elif "manutenção" in multaplgo_melhora or "MANUTENÇÃO" in multaplgo_melhora:
                                multa_pl = 'manteve'
                                self.caixapl.insert("5.6", "manteve", "red")  # Adiciona a tag "red" ao novo valor
                                self.caixapl.tag_config("red", foreground="red")
            if crea_entry == 'SP':
                for page_num in range(folhas_pl, len(pdf_reader.pages)):
                    page = pdf_reader.pages[page_num - 1]
                    text6 = page.extract_text()
                    multaplsp_action_pos = text6.find("R$ ")
                    multaplsp_desc_pos = text6.find("DECIDIU pela")
                    multaplsp_desc_pos2 = text6.find("DECIDIU[: ]")
                    multaplsp_action_pos2 = text6.find("Presidiu")
                    if multaplsp_action_pos != -1:

                        multaplsp_extracted_text = text6[multaplsp_desc_pos2 + len("DECIDIU[: ]"):multaplsp_action_pos].strip()
                        multaplsp_melhora = multaplsp_extracted_text.replace("\n", "")

                        if multaplsp_melhora:
                            print(multaplsp_melhora)
                            if "redução" in multaplsp_melhora:
                                multa_pl = 'reduziu'
                                self.caixapl.insert("5.6", "reduziu","red")  # Adiciona a tag "red" ao novo valor
                                self.caixapl.tag_config("red", foreground="red")
                            elif "manutenção" in multaplsp_melhora or "MANUTENÇÃO" in multaplsp_melhora:
                                multa_pl = 'manteve'
                                self.caixapl.insert("5.6", "manteve ","red")  # Adiciona a tag "red" ao novo valor
                                self.caixapl.tag_config("red", foreground="red")
                        break
                    if multaplsp_action_pos2 != -1:
                        multaplsp_extracted_text = text6[multaplsp_desc_pos + len("DECIDIU pela"):multaplsp_action_pos2].strip()
                        multaplsp_melhora = multaplsp_extracted_text.replace("\n", "")

                        if multaplsp_melhora:
                            print(multaplsp_melhora)
                            if "redução" in multaplsp_melhora:
                                multa_pl = 'reduziu'
                                self.caixapl.insert("5.6", "reduziu ",
                                                    "red")  # Adiciona a tag "red" ao novo valor
                                self.caixapl.tag_config("red", foreground="red")
                            elif "manutenção" in multaplsp_melhora or "MANUTENÇÃO" in multaplsp_melhora:
                                multa_pl = 'manteve'
                                self.caixapl.insert("5.6", "manteve",
                                                    "red")  # Adiciona a tag "red" ao novo valor
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
                                multa_pl = 'reduziu'
                                self.caixapl.insert("5.6", "reduziu para valor minimo","red")  # Adiciona a tag "red" ao novo valor
                                self.caixapl.tag_config("red", foreground="red")
                            elif "manutenção" in multaplgo_melhora or "MANUTENÇÃO" in multaplgo_melhora:
                                multa_pl = 'manteve'
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
                                multa_pl = 'reduziu'
                                self.caixapl.insert("5.6", "reduziu para valor minimo","red")  # Adiciona a tag "red" ao novo valor
                                self.caixapl.tag_config("red", foreground="red")
                            elif "manutenção" in multaplrs_melhora:
                                multa_pl = 'manteve'
                                self.caixapl.insert("5.6", "manteve o valor da multa do AUTO","red")  # Adiciona a tag "red" ao novo valor
                                self.caixapl.tag_config("red", foreground="red")

                        break
                    elif multaplrs_action_pos2 != -1:
                        print("achou a multa2")
                        multaplrs_extracted_text = text6[multaplrs_desc_pos + len(". DECIDIU: "):multaplrs_action_pos2].strip()
                        multaplrs_melhora = multaplrs_extracted_text.replace("\n", "")
                        if multaplrs_melhora:
                            if "redução" in multaplrs_melhora:
                                multa_pl = 'reduziu'
                                self.caixapl.insert("5.6", "reduziu para valor minimo","red")  # Adiciona a tag "red" ao novo valor
                                self.caixapl.tag_config("red", foreground="red")
                            elif "manutenção" in multaplrs_melhora:
                                multa_pl = 'manteve'
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
                                multa_pl = 'reduziu'
                                self.caixapl.insert("5.6", "reduziu para valor minimo","red")  # Adiciona a tag "red" ao novo valor
                                self.caixapl.tag_config("red", foreground="red")
                            elif "manutenção" in multaplrs_melhora:
                                multa_pl = 'manteve'
                                self.caixapl.insert("5.6", "manteve o valor da multa do AUTO","red")  # Adiciona a tag "red" ao novo valor
                                self.caixapl.tag_config("red", foreground="red")


            aviso(pdf_reader, folhas_pl, crea_entry, pdf_file, num_pages)
        def aviso(pdf_reader, folhas_pl,crea_entry, pdf_file, num_pages):
            self.valBarra(0.75)
            global folhas_aviso
            global data_aviso
            data1= ''
            print("15 passo: Procurar o aviso de recebimento")
            padroes = [
                'Resposta dos correios',
                'Aviso de Recebimento',
                'ESTINATARIO:',
                'Destinatário',
                'DESTINATÁRIO',
                'DESTINAIÁRIO',
                'ASSINATURA DO RECEBEDOR'
            ]

            # Trecho de código para iterar sobre as páginas e procurar os padrões
            for pagina in range(folhas_pl, len(pdf_reader.pages)):
                texto_pagina = pdf_reader.pages[pagina].extract_text()
                if pagina == 77:
                    print(texto_pagina)
                # Procurar os padrões na página
                for padrao in padroes:
                    if padrao in texto_pagina:
                        print("Achei o padrão:", padrao)
                        folhas_aviso = pagina + 1
                        self.caixaar.insert("2.7", folhas_aviso, "red")
                        self.caixaar.tag_config("red", foreground="red")
                        break  # Parar a busca assim que um padrão for encontrado
                if 'AVISO DE RECEBIMENTO' in texto_pagina and crea_entry != 'PA':
                    print("16.1 passo: Achei o aviso de recebimento")
                    folhas_aviso = pagina + 1
                    self.caixaar.insert("2.7", folhas_aviso, "red")
                    self.caixaar.tag_config("red", foreground="red")
                    break
                elif 'Objeto entregue' in texto_pagina:
                    print("16.4 passo: Achei o aviso de recebimento")
                    data3 = re.search(r'(\d{2})/(\d{2})/(\d{4}) ', texto_pagina)

                    folhas_aviso = pagina + 1
                    if folhas_aviso:
                        folhas_aviso = pagina + 1

                        self.caixaar.insert("2.7", folhas_aviso, "red")
                        self.caixaar.tag_config("red", foreground="red")

                    if data3:
                        global data_aviso
                        dia2 = data3.group(1)
                        mes2 = data3.group(2)
                        ano2 = data3.group(3)
                        if mes2 == '01':
                            mes_escrito2 = "janeiro"
                        elif mes2 == '02':
                            mes_escrito2 = "fevereiro"
                        elif mes2 == '03':
                            mes_escrito2 = "março"
                        elif mes2 == '04':
                            mes_escrito2 = "abril"
                        elif mes2 == '05':
                            mes_escrito2 = "maio"
                        elif mes2 == '06':
                            mes_escrito2 = "junho"
                        elif mes2 == '07':
                            mes_escrito2 = "julho"
                        elif mes2 == '08':
                            mes_escrito2 = "agosto"
                        elif mes2 == '09':
                            mes_escrito2 = "setembro"
                        elif mes2 == '10':
                            mes_escrito2 = "outubro"
                        elif mes2 == '11':
                            mes_escrito2 = "novembro"
                        elif mes2 == '12':
                            mes_escrito2 = "dezembro"
                        data_aviso = f"{dia2} de {mes_escrito2} de {ano2}"
                        self.caixaar.insert("3.5", str(data_aviso), "red")  # Adiciona a tag "red" ao novo valor
                        self.caixaar.tag_config("red", foreground="red")
            """for pagina in range(folhas_pl, len(pdf_reader.pages)):
                texto_pagina = pdf_reader.pages[pagina].extract_text()

                data1 = None
                if 'AVISO DE RECEBIMENTO' in texto_pagina and crea_entry != 'PA':
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
                elif 'ESTINATARIO:' in texto_pagina or 'Destinatário' in texto_pagina or 'DESTINATÁRIO' in texto_pagina or 'DESTINAIÁRIO' in texto_pagina:
                    print("16.3 passo: Achei o aviso de recebimento")
                    folhas_aviso = pagina + 1
                    self.caixaar.insert("2.7", folhas_aviso, "red")
                    self.caixaar.tag_config("red", foreground="red")
                    break
                elif 'ASSINATURA DO RECEBEDOR' in texto_pagina:
                    print("16.5 passo: Achei o aviso de recebimento")
                    folhas_aviso = pagina + 1
                    self.caixaar.insert("2.7", folhas_aviso, "red")
                    self.caixaar.tag_config("red", foreground="red")
                    break"""


            recurso(folhas_pl,pdf_reader,crea_entry,data_aviso,num_pages)

        def recurso(folhas_pl,pdf_reader , crea_entry,data_aviso,num_pages):
            global folhas_recurso
            global data_recurso
            global justifica_recurso
            self.valBarra(0.80)
            print("17 passo: Procurar o recurso")
            for page_num in range(folhas_pl, len(pdf_reader.pages)):
                    page = pdf_reader.pages[page_num-1]
                    text7 = page.extract_text()
                    recurso = re.search(r'ENTRADA COM DEFESA',text7)
                    recursoba = re.search(r'ENTRADA COM RECURSO',text7)
                    recursogo = re.search(r'REQUERIMENTO PARA APRESENTAÇÃO DE DEFESA',text7)
                    recursors = re.search(r',hahq (\d{2}) de (.*) de (\d{4})',text7)
                    recursosp = re.search(r'FISCALIZAÇÃO - DEFESAS/RECURSOS',text7)
                    recursosp1 = re.search(r'(Recurso à decisão plenária)|(RECURSO À DECISÃO)', text7)
                    recursomt1 = re.search(r'CONSELHO FEDERAL DE ENGEN',text7)
                    recursomt2 = re.search(r'DEFESA',text7)
                    recursorj = re.search(r'RECURSO AO',text7)
                    recursorj1 = re.search(r'[Rr]ecurso [ÃAa][Oo]', text7)
                    if recursomt1 and recursomt2 and crea_entry!='RJ':
                        print("recurso1")
                        pag_recurso = page_num
                        folhas_recurso = f"{pag_recurso}/{num_pages}"
                        self.caixarecurso.insert("2.7", folhas_recurso, "red")
                        self.caixarecurso.tag_config("red", foreground="red")
                    if (recursomt1 or recursorj or recursorj1) and (crea_entry=='RJ' or crea_entry == 'PA' or crea_entry == 'MG' or crea_entry== 'RO'):
                        print("recurso2")
                        pag_recurso = page_num
                        folhas_recurso = f"{pag_recurso}/{num_pages}"
                        self.caixarecurso.insert("2.7", folhas_recurso, "red")
                        self.caixarecurso.tag_config("red", foreground="red")
                        datarecurso = re.search(r'(\d{2})/(\d{2})/(\d{4})', text7)
                        print(datarecurso)
                        if datarecurso:
                            diare = datarecurso.group(1)
                            mesre = datarecurso.group(2)
                            anore = datarecurso.group(3)
                            meses = [
                                "janeiro", "fevereiro", "março", "abril", "maio", "junho",
                                "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"
                            ]
                            mes_escritore = meses[int(mesre) - 1]  # Subtrai 1 do índice para obter o mês correto


                            data_recurso = f"{diare} de {mes_escritore} de {anore}"
                            if data_recurso:
                                print("data_recurso", data_recurso)
                                self.caixarecurso.insert("3.5", str(data_recurso),"red")  # Adiciona a tag "red" ao novo valor
                                self.caixarecurso.tag_config("red", foreground="red")
                                break
                    if recurso or recursoba or ((recursosp or recursosp1) and crea_entry == 'SP'):
                        print("recurso3")
                        print("18 passo: Achei o recurso")
                        pag_recurso = page_num
                        folhas_recurso = f"{pag_recurso}/{num_pages}"
                        self.caixarecurso.insert("2.7", folhas_recurso, "red")
                        self.caixarecurso.tag_config("red", foreground="red")
                        datarecurso = re.search(r'(\d{2})/(\d{2})/(\d{4})', text7)
                        datarecurso2 = re.search(r'(\d{2}) de (\w+) de (\d{4})',text7)
                        if datarecurso2:
                            data_recurso = datarecurso2.group()
                            self.caixarecurso.insert("3.5", str(data_recurso),"red")  # Adiciona a tag "red" ao novo valor
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

                            data_recurso = f"{diare} de {mes_escritore} de {anore}"
                            self.caixarecurso.insert("3.5", str(data_recurso),
                                                     "red")  # Adiciona a tag "red" ao novo valor
                            self.caixarecurso.tag_config("red", foreground="red")
                            if data_aviso is not None:
                                diferenca = (data_aviso - data4).days
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
                        self.valBarra(0.85)
                    elif recursogo:

                        print("recursogo")
                        pag_recursogo = page_num + 1
                        folhas_recurso = f"{pag_recursogo}/{num_pages}"
                        self.caixarecurso.insert("2.7", folhas_recurso, "red")
                        self.caixarecurso.tag_config("red", foreground="red")
                        descrecursoinicio = text7.find("Descrição da Defesa:")
                        posrecursofim = text7.find("Data ")
                        justificativa = text7[descrecursoinicio + len("Descrição da Defesa:"):posrecursofim].strip()
                        justifica_recurso = justificativa.replace("\n", "")
                        datagore = re.search(r'(\d{2}) de (.*) de (\d{4})', text7)

                        if justifica_recurso:
                            self.caixarecurso.insert("5.17", justifica_recurso, "red")
                            self.caixarecurso.tag_config("red", foreground="red")

                        print("18 passo: Achei o recurso")
                        print("18_1 GO")
                        if datagore:
                            data_recurso = datagore.group()
                            self.caixarecurso.insert("3.7", data_recurso, "red")
                            self.caixarecurso.tag_config("red", foreground="red")
                        break
                        self.valBarra(0.95)
                    elif recursors:
                        print("recursors")
                        data_recurso = recursors.group()
                        #result_recursors_real =
                        pag_recursors = page_num + 1
                        folhas_recurso = f"{pag_recursors}/{num_pages}"
                        self.caixarecurso.insert("2.7", folhas_recurso, "red")
                        self.caixarecurso.tag_config("red", foreground="red")
                        self.caixarecurso.insert("3.5", data_recurso, "red")
                        self.caixarecurso.tag_config("red", foreground="red")
                        break


            art(pdf_reader,crea_entry)
        def art(pdf_reader, crea_entry):
            print("entrou na consulta geral")
            art_page = None
            reincidencia_page = None
            cnpj_page = None
            procuracao = None
            ficha_page = None
            alteracao_page = None
            global folhas_procuracao
            global folhas_art
            global folhas_cnpj
            global folhas_reincidencia
            global cnae_primeiro
            global cnae_segundo
            global data_cnpj

            if crea_entry:

                if art_page is None:
                    print("nao achou art")
                    for page_num, page in enumerate(pdf_reader.pages):
                        text = page.extract_text()
                        art_match = re.search(r'ART O', text)
                        if art_match is not None:
                            folhas_art = page_num + 1  # Número da página onde foi encontrada a correspondência
                            self.caixaart.insert("2.7", folhas_art, "red")  # Adiciona a tag "red" ao novo valor
                            self.caixaart.tag_config("red", foreground="red")
                            break
                if alteracao_page is None:
                    print("nao achou alteraçao")
                    for page_num, page in enumerate(pdf_reader.pages):
                        text_alteracao = page.extract_text()
                        alteracao_match = re.search(r'ALTERAÇÃO CONTRATUAL', text_alteracao)
                        alteracao_match2 = re.search(r'ALTERAÇÃO DA SOCIE',  text_alteracao)
                        alteracao_match3 = re.search(r'CONTRATO DE CONSTITUIÇÃO',  text_alteracao)
                        if alteracao_match is not None or alteracao_match2 is not None or alteracao_match3 is not None:
                            folhas_alteracao = page_num + 1  # Número da página onde foi encontrada a correspondência
                            self.caixaalteracao.insert("2.7", folhas_alteracao, "red")  # Adiciona a tag "red" ao novo valor
                            self.caixaalteracao.tag_config("red", foreground="red")
                            result_alteracao_objeto = re.search(r' objeto social(.+)', text_alteracao)
                            if result_alteracao_objeto:
                                alteracao_objeto = result_alteracao_objeto.group()
                                self.caixaalteracao.insert("4.16", alteracao_objeto,"red")  # Adiciona a tag "red" ao novo valor
                                self.caixaalteracao.tag_config("red", foreground="red")
                            break
                            """alteracao_match2 = re.search(r'ALTERAÇÃO CONTRATUAL', text)
                            alteracao_match3 = re.search(r'ALTERAÇÃO DA SOCIE', text)
                            #alteracao_desc_pos = text.find("Objeto Social")
                            if alteracao_match2 or alteracao_match3:
                                ("achou a alteração")
                                ficha_extracted_text = text[ficha_desc_pos + len("Objeto Social"):ficha_action_pos].strip()
                                print(ficha_extracted_text)
                                ficha_melhora = ficha_extracted_text.replace("\n", "").lower()
                                if ficha_melhora:
                                    self.caixaficha.insert("4.18", ficha_melhora, "red")  # Adiciona a tag "red" ao novo valor
                                    self.caixaficha.tag_config("red", foreground="red")
                                    result_data_ficha = re.search(r'(\d{2})/(\d{2})/(\d{4})', text)
                                    if result_data_ficha:
                                        diaficha = result_data_ficha.group(1)
                                        mesficha = result_data_ficha.group(2)
                                        anoficha = result_data_ficha.group(3)

                                        if mesficha == '01':
                                            mes_escritof = "janeiro"
                                        elif mesficha == '02':
                                            mes_escritof = "fevereiro"
                                        elif mesficha == '03':
                                            mes_escritof = "março"
                                        elif mesficha == '04':
                                            mes_escritof = "abril"
                                        elif mesficha == '05':
                                            mes_escritof = "maio"
                                        elif mesficha == '06':
                                            mes_escritof = "junho"
                                        elif mesficha == '07':
                                            mes_escritof = "julho"
                                        elif mesficha == '08':
                                            mes_escritof = "agosto"
                                        elif mesficha == '09':
                                            mes_escritof = "setembro"
                                        elif mesficha == '10':
                                            mes_escritof = "outubro"
                                        elif mesficha == '11':
                                            mes_escritof = "novembro"
                                        elif mesficha == '12':
                                            mes_escritof = "dezembro"
                                        data_ficha= f"{diaficha} de {mes_escritof} de {anoficha}"
                                        self.caixaficha.insert("3.6", data_ficha, "red")  # Adiciona a tag "red" ao novo valor
                                        self.caixaficha.tag_config("red", foreground="red")
                                        break"""
                if ficha_page is None:
                    print("nao achou ficha")
                    for page_num, page in enumerate(pdf_reader.pages):
                        text = page.extract_text()
                        ficha_match = re.search(r'Ficha Cadastral', text)


                        if ficha_match is not None:
                            folhas_ficha = page_num + 1  # Número da página onde foi encontrada a correspondência
                            self.caixaficha.insert("2.7", folhas_ficha, "red")  # Adiciona a tag "red" ao novo valor
                            self.caixaficha.tag_config("red", foreground="red")
                            ficha_action_pos = text.find("Atividades da Empresa")
                            ficha_desc_pos = text.find("Objeto Social")
                            if ficha_desc_pos != -1:
                                ("achou a ficha")
                                ficha_extracted_text = text[ficha_desc_pos + len("Objeto Social"):ficha_action_pos].strip()
                                print(ficha_extracted_text)
                                ficha_melhora = ficha_extracted_text.replace("\n", "").lower()
                                if ficha_melhora:
                                    self.caixaficha.insert("4.18", ficha_melhora, "red")  # Adiciona a tag "red" ao novo valor
                                    self.caixaficha.tag_config("red", foreground="red")
                                    result_data_ficha = re.search(r'(\d{2})/(\d{2})/(\d{4})', text)
                                    if result_data_ficha:
                                        diaficha = result_data_ficha.group(1)
                                        mesficha = result_data_ficha.group(2)
                                        anoficha = result_data_ficha.group(3)

                                        if mesficha == '01':
                                            mes_escritof = "janeiro"
                                        elif mesficha == '02':
                                            mes_escritof = "fevereiro"
                                        elif mesficha == '03':
                                            mes_escritof = "março"
                                        elif mesficha == '04':
                                            mes_escritof = "abril"
                                        elif mesficha == '05':
                                            mes_escritof = "maio"
                                        elif mesficha == '06':
                                            mes_escritof = "junho"
                                        elif mesficha == '07':
                                            mes_escritof = "julho"
                                        elif mesficha == '08':
                                            mes_escritof = "agosto"
                                        elif mesficha == '09':
                                            mes_escritof = "setembro"
                                        elif mesficha == '10':
                                            mes_escritof = "outubro"
                                        elif mesficha == '11':
                                            mes_escritof = "novembro"
                                        elif mesficha == '12':
                                            mes_escritof = "dezembro"
                                        data_ficha= f"{diaficha} de {mes_escritof} de {anoficha}"
                                        self.caixaficha.insert("3.6", data_ficha, "red")  # Adiciona a tag "red" ao novo valor
                                        self.caixaficha.tag_config("red", foreground="red")
                                        break
                if cnpj_page is None:
                    print("nao achou cnpj")
                    for page_num, page in enumerate(pdf_reader.pages):
                        text = page.extract_text()
                        cnpj_match = re.search(r'COMPROVANTE DE INSCRIÇÃO ', text)
                        cnpj_match2 = re.search(r'Comprovante de Inscri', text)
                        result_data_cnpj = re.search(r'Emitido no dia', text)
                        if (cnpj_match is not None or cnpj_match2 is not None) and result_data_cnpj:

                            folhas_cnpj = page_num + 1  # Número da página onde foi encontrada a correspondência
                            self.caixacnpj.insert("2.7", folhas_cnpj, "red")  # Adiciona a tag "red" ao novo valor
                            self.caixacnpj.tag_config("red", foreground="red")


                            data_cnpj1 = re.search(r'Emitido no dia (\d{2})/(\d{2})/(\d{4})',text)
                            if data_cnpj1:
                                print(data_cnpj1)
                                diacnpj = data_cnpj1.group(1)
                                mescnpj = data_cnpj1.group(2)
                                anocnpj = data_cnpj1.group(3)
                                print(diacnpj)
                                if mescnpj == '01':
                                    mes_escritore = "janeiro"
                                elif mescnpj == '02':
                                    mes_escritore = "fevereiro"
                                elif mescnpj == '03':
                                    mes_escritore = "março"
                                elif mescnpj == '04':
                                    mes_escritore = "abril"
                                elif mescnpj == '05':
                                    mes_escritore = "maio"
                                elif mescnpj == '06':
                                    mes_escritore = "junho"
                                elif mescnpj == '07':
                                    mes_escritore = "julho"
                                elif mescnpj == '08':
                                    mes_escritore = "agosto"
                                elif mescnpj == '09':
                                    mes_escritore = "setembro"
                                elif mescnpj == '10':
                                    mes_escritore = "outubro"
                                elif mescnpj == '11':
                                    mes_escritore = "novembro"
                                elif mescnpj == '12':
                                    mes_escritore = "dezembro"
                                data_cnpj = f"{diacnpj} de {mes_escritore} de {anocnpj}"
                                self.caixacnpj.insert("3.5", data_cnpj,"red")  # Adiciona a tag "red" ao novo valor
                                self.caixacnpj.tag_config("red", foreground="red")
                                break
                    for page_num, page in enumerate(pdf_reader.pages):
                            text = page.extract_text()

                            inicio_primeira_atividade = text.find("PRINCIPAL")
                            fim_primeira_atividade= text.find("TIVIDADES")
                            fim_primeira_atividade2 = text.find("DESCRI")
                            fim_segunda_atividade = text.find("TUREZA")
                            data_cnpj1 = text.find("Emitido no dia ")
                            if inicio_primeira_atividade != -1 and fim_primeira_atividade != -1:
                                resultado_cnae_primeiro = text[inicio_primeira_atividade + len("PRINCIPAL"):fim_primeira_atividade].strip()
                                cnae_primeiro = resultado_cnae_primeiro.replace("\n", "")
                                if cnae_primeiro:
                                    print("cnae_primeiro=1")
                                    cnae_primeiro = cnae_primeiro[:-30]
                                    self.caixacnpj.insert("4.15", cnae_primeiro,"red")  # Adiciona a tag "red" ao novo valor
                                    self.caixacnpj.tag_config("red", foreground="red")

                            if fim_segunda_atividade != -1 and fim_primeira_atividade != -1:
                                print(data_cnpj1)
                                resultado_cnae_segundo = text[fim_primeira_atividade + len("ATIVIDADES"):fim_segunda_atividade].strip()
                                cnae_segundo = resultado_cnae_segundo.replace("\n", "")
                                if cnae_segundo:
                                    print("cnae_segundo=10")
                                    cnae_segundo = cnae_segundo[22:-25]
                                    self.caixacnpj.insert("5.17", cnae_segundo,"red")  # Adiciona a tag "red" ao novo valor
                                    self.caixacnpj.tag_config("red", foreground="red")
                                    break
                            elif inicio_primeira_atividade != -1 and fim_primeira_atividade2 != -1 :
                                resultado_cnae_primeiro = text[inicio_primeira_atividade + len("PRINCIPAL"):fim_primeira_atividade2].strip()
                                cnae_primeiro = resultado_cnae_primeiro.replace("\n", "")
                                if cnae_primeiro:
                                    print("cnae_primeiro=2")
                                    cnae_primeiro = cnae_primeiro[:-15]
                                    self.caixacnpj.insert("4.15", cnae_primeiro,
                                                          "red")  # Adiciona a tag "red" ao novo valor
                                    self.caixacnpj.tag_config("red", foreground="red")

                if reincidencia_page is None:
                    print("nao achou reincidencia")
                    for page_num, page in enumerate(pdf_reader.pages):
                        text = page.extract_text()
                        reincidencia_match = re.search(r'CERTIDÃO DE TRÂNSITO EM JULGADO', text)
                        if reincidencia_match is not None:

                            folhas_reincidencia = page_num + 1  # Número da página onde foi encontrada a correspondência
                            self.caixareincidencia.insert("2.7", folhas_reincidencia, "red")  # Adiciona a tag "red" ao novo valor
                            self.caixareincidencia.tag_config("red", foreground="red")
                            break
                if procuracao is None:
                    print("nao achou procuracao")
                    for page_num, page in enumerate(pdf_reader.pages):
                        text = page.extract_text()
                        result_procuracao = re.search(r'PROCURAÇÃO', text)

                        if result_procuracao is not None:
                            folhas_procuracao = page_num + 1  # Número da página onde foi encontrada a correspondência
                            self.caixaprocuracao.insert("2.7", folhas_procuracao,"red")  # Adiciona a tag "red" ao novo valor
                            self.caixaprocuracao.tag_config("red", foreground="red")
                            break

                """if art_page is not None and reincidencia_page is not None:
                    for page_num, page in enumerate(pdf_reader.pages):
                        text = page.extract_text()
                        break"""

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
            self.valBarra(1)
            tk.messagebox.showinfo("Sistema confea","Finalizado")

            self.valBarra(1)

##########################################################################################################
#           CREAS GO
##########################################################################################################
        """Descobre qual pagina do Auto de Infração"""
        def crea_entrysgo(pdf_file, num_pages, crea_entry):
            global nsei_ai
            global folhas_ai
            self.caixaai.delete("2.16", "2.99")
            pdf_reader = PdfReader(pdf_file)
            for page_num in range(num_pages):
                page = pdf_reader.pages[page_num]
                text = page.extract_text()
                pagautuado = re.search(r'AUTO DE INFRAÇÃO Nº(.+)', text)
                result_nsei_entry = re.search(r'Processo: (.*)Página', text)

                if pagautuado and result_nsei_entry:
                    folhas_ai = page_num + 1
                    nsei_ai = result_nsei_entry.group(1)
                    self.caixaai.insert("2.16", str(nsei_ai), "red")  # Adiciona a tag "red" ao novo valor
                    self.caixaai.tag_config("red", foreground="red")
                    #salvar(nsei_entry)
                    #salvar(folhas_entry)
                    pagdoautogo(folhas_ai, pdf_file,crea_entry, num_pages)
        """EXTRAINDO DADOS DO AUTO DE INFRAÇÃO"""
        def pagdoautogo(folhas_ai,pdf_file,crea_entry,num_pages):
            global nauto_ai
            global multa_ai
            global autuado_ai
            global cnpj_cpf_ai
            global artigo_ai
            global motivo_ai
            global data_ai
            #global folhas_ai
            pdf_reader = PdfReader(pdf_file)
            page = pdf_reader.pages[folhas_ai - 1]
            text = page.extract_text()
            artigo = re.search(r'o\(a\) artigo(.*)da Lei', text)
            multa = re.search(r' multa no valor de(.*) \(', text)
            data = re.search(r'\-GO, (\d{2}) (.+?) (\d{4})', text)
            nauto = re.search(r'Nº(.*)', text)
            cnpj = re.search(r' \d{2}\.\d{3}\.\d{3}', text)
            desc_pos = text.find("que")
            action_pos = text.find("- C")
            extracted_text = text[desc_pos + len("que"):action_pos].strip()
            autuado_ai = extracted_text.replace("\n","").title()
            desc_pos = text.find("da Infração:")
            action_pos = text.find("b)")
            extracted_text = text[desc_pos + len("da Infração:"):action_pos].strip()
            melhora_motivo = extracted_text.replace("\n", "")

            if melhora_motivo:
                motivo_ai = melhora_motivo.lower()
                self.caixaai.insert("10.10", motivo_ai, "red")
                self.caixaai.tag_config("red", foreground="red")
            if autuado_ai:
                self.caixaai.insert("4.12", autuado_ai, "red")
                self.caixaai.tag_config("red", foreground="red")
            if cnpj:
                result_cnpj = cnpj.group()
                cnpj_numeros_meio = re.search(r'\d{2}\.(\d{3}\.\d{3})', result_cnpj)
                if cnpj_numeros_meio:
                    cnpj_cpf_ai = result_cnpj[5:]
                    self.caixaai.insert("5.6", f"***{cnpj_cpf_ai}***", "red")
                    self.caixaai.tag_config("red", foreground="red")
            if nauto:
                # Inserir o novo valor extraído do PDF no widget Text
                self.caixaai.insert("6.11", str(folhas_ai), "red")  # Adiciona a tag "red" ao novo valor
                self.caixaai.tag_config("red", foreground="red")  # Configura a cor vermelha para a tag "red"
                nauto_ai = nauto.group(1)
                self.caixaai.insert("7.10", str(nauto_ai), "red")  # Adiciona a tag "red" ao novo valor
                self.caixaai.tag_config("red", foreground="red")
            if artigo:
                result_artigo = artigo.group(1)
                if "1" in result_artigo:
                    artigo_ai = "art. 1º da Lei Federal nº 6.496/77"
                    self.caixaai.insert("3.8", "art. 1º da Lei Federal nº 6.496/77","red")  # Adiciona a tag "red" ao novo valor
                    self.caixaai.tag_config("red", foreground="red")
                if "59" in result_artigo:
                    artigo_ai = "art. 59º da Lei Federal nº 5.194/66"
                    self.caixaai.insert("3.8", "art. 59º da Lei Federal nº 5.194/66","red")  # Adiciona a tag "red" ao novo valor
                    self.caixaai.tag_config("red", foreground="red")
            if multa:
                multa_ai = multa.group(1)
                self.caixaai.insert("8.7", multa_ai, "red")  # Adiciona a tag "red" ao novo valor
                self.caixaai.tag_config("red", foreground="red")
            if data:
                result_data = data.group()
                data_ai = result_data[5:]
                self.caixaai.insert("9.6", data_ai, "red")  # Adiciona a tag "red" ao novo valor
                self.caixaai.tag_config("red", foreground="red")
            ce(pdf_reader, folhas_ai, crea_entry, pdf_file,num_pages)

##########################################################################################################
#           CREAS MG
##########################################################################################################
        """Descobre qual pagina do Auto de Infração"""
        def crea_entrysmg(pdf_file, num_pages, crea_entry):
                global folhas_ai
                self.valBarra(0.10)
                print("3 passo: Procura a pagina do AUTO DE INFRAÇÃO")
                pdf_reader = PdfReader(pdf_file)
                for page_num in range(num_pages):
                    page = pdf_reader.pages[page_num]
                    text = page.extract_text()
                    pagautuado = re.search(r'AUTO DE INFRACAO', text)
                    complemento_pagautuado = re.search(r'PROCESSO N(.+)', text)
                    pagautuado1 = re.search(r'DATA DA LAVRATURA', text)
                    """Pagina do Auto de infração"""
                    if (pagautuado or pagautuado1) and complemento_pagautuado:
                        self.valBarra(0.15)

                        print("4 passo: Achei a pagina do AUTO DE INFRAÇÃO")
                        folhas_ai = page_num + 1
                        """Inserir folha do AUTO DE INFRAÇÃO"""
                        self.caixaai.insert("6.11", str(folhas_ai), "red")  # Adiciona a tag "red" ao novo valor
                        self.caixaai.tag_config("red", foreground="red")  # Configura a cor vermelha para a tag "red"

                        pagedoautomg(folhas_ai, pdf_file, num_pages, crea_entry)
                        break
        """EXTRAINDO DADOS DO AUTO DE INFRAÇÃO"""
        def pagedoautomg(folhas_ai, pdf_file, num_pages, crea_entry):
                global nauto_ai
                global multa_ai
                global nsei_ai
                global autuado_ai
                global cnpj_cpf_ai
                global artigo_ai
                global motivo_ai
                global data_ai
                self.valBarra(0.20)
                print("5 passo: Procura todos os dados do AUTO DE INFRAÇÃO")
                pdf_reader = PdfReader(pdf_file)
                page = pdf_reader.pages[folhas_ai - 1]
                text = page.extract_text()

                """Extrai o NUMERO DO AUTO"""
                nauto = re.search(r'PROCESSO N[°º°](.+)', text)


                """Extrai o NOME DO AUTUADO"""
                autuado = re.search(r'NOME/RAZ[ÃA]O SOCIAL:(.+)', text)

                """Extrai o CNPJ"""
                cnpj = re.search(r'CPF/CNPJ:(.+)', text)

                """Extrai o motivo do AUTO"""
                desc_pos2 = text.find("ATIVIDADES:")
                action_pos2 = text.find("IDENTIFICAÇÃO")
                #de_ac_pos2 = re.search(r'DESCRIÇÃO:(.+)', text)
                if desc_pos2 != -1 and action_pos2 != -1:
                    extracted_text2 = text[desc_pos2 + len("ATIVIDADES:"):action_pos2].strip()
                    extracted_text2 = extracted_text2[:-5]
                    if extracted_text2 == '':
                        desc_pos2_1 = text.find("SITUAÇÃO:")
                        action_pos2_1 = text.find("ATIVIDADES:")
                        if desc_pos2_1 != -1 and action_pos2_1 != -1:
                            extracted_text2 = text[desc_pos2_1 + len("SITUAÇÃO:"):action_pos2_1].strip()
                    #extracted_text2_1 = de_ac_pos2.group(1).strip()
                    #extracted_text2 = extracted_text + extracted_text2_1
                else:
                    extracted_text2 = ''
                melhora_motivo = extracted_text2.replace("\n", "")
                data4 = re.search(r'DATA DA LAVRAT[UO]RA: (\d{2})/(\d{2})/(\d{4})', text)
                artigo = re.search(r'ENQUADRAMENTO:(.+)', text)
                multa = re.search(r'VALOR DA MULTA:(.+)', text)

                print("6 passo: Achei todos os dados do AUTO DE INFRAÇÃO")
                self.valBarra(0.25)
                if melhora_motivo:
                    motivo_ai = melhora_motivo.lower()
                    self.caixaai.insert("10.10", str(motivo_ai), "red")
                    self.caixaai.tag_config("red", foreground="red")


                if cnpj:
                    cnpj_cpf_ai = cnpj.group(1)
                    print(cnpj_cpf_ai)
                    cnpj_cpf_ai = cnpj_cpf_ai[4:-8]
                    self.caixaai.insert("5.6", f"***{cnpj_cpf_ai}***", "red")
                    self.caixaai.tag_config("red", foreground="red")
                elif cnpj is None:
                    cnpj2 = re.search(r'CNPJ (.*), ', text)
                    if cnpj2:
                        cnpj_cpf_ai = cnpj2.group(1)

                        cnpj_cpf_ai = cnpj_cpf_ai[4:-9]
                        self.caixaai.insert("5.6", f"***{cnpj_cpf_ai}***", "red")
                        self.caixaai.tag_config("red", foreground="red")
                    elif cnpj2 is None:
                        cnpj3 = re.search(r'(\d{2}).(\d{3}).(\d{3})/(\d{4})-(\d{2})', text)
                        if cnpj3:
                            cnpj_cpf_ai = cnpj3.group()

                            cnpj_cpf_ai = cnpj_cpf_ai[4:-8]
                            self.caixaai.insert("5.6", f"***{cnpj_cpf_ai}***", "red")
                            self.caixaai.tag_config("red", foreground="red")
                        elif cnpj3 is None:
                            cnpj4 = re.search(r'CNPJ (.+)/', text)
                            if cnpj4:
                                cnpj_cpf_ai = cnpj4.group(1)

                                cnpj_cpf_ai = cnpj_cpf_ai[3:]
                                self.caixaai.insert("5.6", f"***{cnpj_cpf_ai}***", "red")
                                self.caixaai.tag_config("red", foreground="red")
                if autuado:
                    autuado = autuado.group().title()
                    autuado_ai = autuado[18:]
                    self.caixaai.insert("4.12", str(autuado_ai), "red")  # Adiciona a tag "red" ao novo valor
                    self.caixaai.tag_config("red", foreground="red")
                if multa:
                    multa = multa.group(1)
                    multa_ai = multa[3:]
                    self.caixaai.insert("8.7", str(multa_ai), "red")  # Adiciona a tag "red" ao novo valor
                    self.caixaai.tag_config("red", foreground="red")
                if artigo:
                    # artigo = artigo[:-50]
                    artigo_ai = artigo.group(1).lower()
                    self.caixaai.insert("3.8", str(artigo_ai), "red")  # Adiciona a tag "red" ao novo valor
                    self.caixaai.tag_config("red", foreground="red")
                if nauto:
                    print("n1")
                    result_nauto_entry = nauto.group(1)
                    print(result_nauto_entry)
                    result_nauto_entry = re.search(r'\d{1,10}-\d', result_nauto_entry)
                    nauto_ai = result_nauto_entry.group()
                    print(nauto_ai)
                    self.caixaai.insert("7.10", str(nauto_ai), "red")  # Adiciona a tag "red" ao novo valor
                    self.caixaai.tag_config("red", foreground="red")
                elif nauto is None:
                    nauto2 = re.search(r'N°(.*)/(\d{4})', text)
                    nauto3 = re.search(r'Número(.*)/(\d{4})', text)
                    nauto4 = re.search(r'Número;(.+)', text)
                    nauto5 = re.search(r'AUTO DE INFRAÇÃO (.+)', text)
                    if nauto2:
                        print("n2")
                        result_nauto2 = nauto2.group()
                        nauto_ai = result_nauto2[3:]
                        self.caixaai.insert("7.10", str(nauto_ai), "red")  # Adiciona a tag "red" ao novo valor
                        self.caixaai.tag_config("red", foreground="red")
                    elif nauto3:
                        result_nauto_entry = nauto3.group()
                        print("n3")
                        nauto_ai = result_nauto_entry[8:]
                        self.caixaai.insert("7.10", str(nauto_ai), "red")  # Adiciona a tag "red" ao novo valor
                        self.caixaai.tag_config("red", foreground="red")
                    elif nauto4:
                        print("n4")
                        result_nauto4 = nauto4.group()
                        nauto_ai = result_nauto4[3:]
                        self.caixaai.insert("7.10", str(nauto_ai), "red")  # Adiciona a tag "red" ao novo valor
                        self.caixaai.tag_config("red", foreground="red")
                    elif nauto5:
                        print("n5")
                        result_nauto5 = nauto5.group()
                        nauto_ai = result_nauto5[17:]
                        self.caixaai.insert("7.10", str(nauto_ai), "red")  # Adiciona a tag "red" ao novo valor
                        self.caixaai.tag_config("red", foreground="red")
                if data4:
                    print("data")
                    configdata4(data4)
                ce(pdf_reader, folhas_ai, crea_entry, pdf_file, num_pages)
        def configmes4(dia, mes_escrito, ano):
                global data_ai
                data_ai = f"{dia} de {mes_escrito} de {ano}"

                if data_ai:
                    self.caixaai.insert("9.6", str(data_ai), "red")  # Adiciona a tag "red" ao novo valor
                    self.caixaai.tag_config("red", foreground="red")
                    return data_ai
        def configdata4(data4):
                global data_ai
                dia = data4.group(1)
                mes = data4.group(2)
                ano = data4.group(3)
                if mes == '01':
                    mes_escrito = "janeiro"
                    configmes4(dia, mes_escrito, ano)
                elif mes == '02':
                    mes_escrito = "fevereiro"
                    configmes4(dia, mes_escrito, ano)
                elif mes == '03':
                    mes_escrito = "março"
                    configmes4(dia, mes_escrito, ano)
                elif mes == '04':
                    mes_escrito = "abril"
                    configmes4(dia, mes_escrito, ano)
                elif mes == '05':
                    mes_escrito = "maio"
                    configmes4(dia, mes_escrito, ano)
                elif mes == '06':
                    mes_escrito = "junho"
                    configmes4(dia, mes_escrito, ano)
                elif mes == '07':
                    mes_escrito = "julho"
                    configmes4(dia, mes_escrito, ano)
                elif mes == '08':
                    mes_escrito = "agosto"
                    configmes4(dia, mes_escrito, ano)
                elif mes == '09':
                    mes_escrito = "setembro"
                    configmes4(dia, mes_escrito, ano)
                elif mes == '10':
                    mes_escrito = "outubro"
                    configmes4(dia, mes_escrito, ano)
                elif mes == '11':
                    mes_escrito = "novembro"
                    configmes4(dia, mes_escrito, ano)
                elif mes == '12':
                    mes_escrito = "dezembro"
                    configmes4(dia, mes_escrito, ano)
##########################################################################################################
#           CREAS RS
##########################################################################################################
        """CREAS= RS"""
        def crea_entrysrs(pdf_file, num_pages, crea_entry):
            self.valBarra(0.10)
            print("3 passo: Procura a pagina do AUTO DE INFRAÇÃO")
            pdf_reader = PdfReader(pdf_file)
            for page_num in range(num_pages):
                page = pdf_reader.pages[page_num]
                text = page.extract_text()
                pagautuado = re.search(r'AUTO DE INFRAÇÃO N', text)
                pagautuado2 = re.search(r'AUTO DE INFRACAO N', text)

                """Pagina do Auto de infração"""
                if pagautuado or pagautuado2:

                    self.valBarra(0.15)
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
            self.valBarra(0.20)
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
            self.valBarra(0.25)
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
                multa_ai = multa.group(1)
                self.caixaai.insert("8.7", multa_ai, "red")  # Adiciona a tag "red" ao novo valor
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

##########################################################################################################
#           CREAS RJ
##########################################################################################################
        """Descobre qual pagina do Auto de Infração"""
        def crea_entrysrj(pdf_file, num_pages, crea_entry):
            self.valBarra(0.10)
            print("3 passo: Procura a pagina do AUTO DE INFRAÇÃO")
            pdf_reader = PdfReader(pdf_file)
            for page_num in range(num_pages):
                page = pdf_reader.pages[page_num]
                text = page.extract_text()
                pagautuado = re.search(r'AUTO INFRAÇÃO NÚMERO', text)


                """Pagina do Auto de infração"""
                if pagautuado:
                    self.valBarra(0.15)
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
            self.valBarra(0.20)
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
            artigo1 = re.search(r'((Enquadramento)|(ENQUETE))(.+)',text)
            print(artigo1)

            desc_pos = text.find("Serviço Executado")
            action_pos = text.find("Contratante", desc_pos)
            extracted_text = text[desc_pos + len("Serviço Executado"):action_pos].strip()
            melhora_motivo = extracted_text.replace("\n", "")
            print("6 passo: Achei todos os dados do AUTO DE INFRAÇÃO")
            self.valBarra(0.25)
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
                artigo2 = artigo1.group()
                print(artigo2)
                artigo = re.search(r'\bART.+', artigo2)
                if artigo:
                    artigo_ai = artigo.group(0).lower()
                    self.caixaai.insert("3.8", artigo_ai,"red")  # Adiciona a tag "red" ao novo valor
                    self.caixaai.tag_config("red", foreground="red")
                elif artigo2:
                    artigo_ai = artigo2.lower()
                    self.caixaai.insert("3.8", artigo_ai,"red")  # Adiciona a tag "red" ao novo valor
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
                data_ai = data.group()
                print("a data",data)
                self.caixaai.insert("9.6", str(data_ai), "red")  # Adiciona a tag "red" ao novo valor
                self.caixaai.tag_config("red", foreground="red")
            if data is None:
                data2 = re.search(r', (\d{1,2} de (\w+) de \d{4})', text)
                data_ai = data2.group()
                print("a data2", data2)
                self.caixaai.insert("9.6", data_ai, "red")  # Adiciona a tag "red" ao novo valor
                self.caixaai.tag_config("red", foreground="red")
            ce(pdf_reader, folhas_ai, crea_entry, pdf_file, num_pages)


##########################################################################################################
#           CREAS SP
##########################################################################################################
        """Descobre qual pagina do Auto de Infração"""
        def crea_entryssp(pdf_file, num_pages, crea_entry):
            global folhas_ai
            self.valBarra(0.10)
            print("3 passo: Procura a pagina do AUTO DE INFRAÇÃO")
            pdf_reader = PdfReader(pdf_file)
            for page_num in range(num_pages):
                page = pdf_reader.pages[page_num]
                text = page.extract_text()
                pagautuado = re.search(r'AUTO DE (INFRACAO|INFRAÇÃO)', text)
                complemento_pagautuado = re.search(r'', text)
                """Pagina do Auto de infração"""
                if pagautuado:
                    self.valBarra(0.15)
                    print("4 passo: Achei a pagina do AUTO DE INFRAÇÃO")
                    folhas_ai = page_num + 1


                    # result_nsei_entry = nsei_entry.group(1)
                    """Inserir numero do Processo SEI"""
                    # self.caixaai.insert("2.16", str(result_nsei_entry), "red")  # Adiciona a tag "red" ao novo valor
                        # self.caixaai.tag_config("red", foreground="red")
                    """Inserir folha do AUTO DE INFRAÇÃO"""
                    self.caixaai.insert("6.11", str(folhas_ai), "red")  # Adiciona a tag "red" ao novo valor
                    self.caixaai.tag_config("red", foreground="red")  # Configura a cor vermelha para a tag "red"
                    # folhas_entry)
                    pagedoautosp(folhas_ai, pdf_file, num_pages, crea_entry)
                    break
        """EXTRAINDO DADOS DO AUTO DE INFRAÇÃO"""
        def pagedoautosp(folhas_ai, pdf_file, num_pages, crea_entry):
            global nauto_ai
            global multa_ai
            global nsei_ai
            global autuado_ai
            global cnpj_cpf_ai
            global artigo_ai
            global motivo_ai
            global data_ai
            self.valBarra(0.20)
            print("5 passo: Procura todos os dados do AUTO DE INFRAÇÃO")
            pdf_reader = PdfReader(pdf_file)
            page = pdf_reader.pages[folhas_ai - 1]
            text = page.extract_text()
            """Extrai o valor da multa"""
            """Extrai a data do auto"""

            complemento_data = re.search(r'Cientifique-se e cumpra-se', text)
            """Extrai o NUMERO DO AUTO"""

            #nauto = re.search(r'((Número[;:])|N°)(.+) / (\d{4})', text)
            nauto = re.search(r'(Número[: ;] )(.+)', text)
            # nauto2 = re.search(r'AUTO DE INFRACAO N°(.+)', text)
            """Extrai o NOME DO AUTUADO"""
            desc_pos3 = text.find("nome da empresa")
            desc_pos3_1 = text.find(" em nome d")
            desc_pos3_2 = text.find(" a empresa ")
            action_pos3 = text.find(", Com", max(desc_pos3, desc_pos3_1,desc_pos3_2))
            action_pos3_1 = text.find(", com", max(desc_pos3, desc_pos3_1,desc_pos3_2))
            action_pos3_2 = text.find("CNPJ ", max(desc_pos3, desc_pos3_1, desc_pos3_2))


            if desc_pos3 != -1 and action_pos3 != -1:
                extracted_text3 = text[desc_pos3 + len("nome da empresa"):action_pos3].strip()
            elif desc_pos3 != -1 and action_pos3_1 != -1:
                extracted_text3 = text[desc_pos3 + len("nome da empresa"):action_pos3_1].strip()
            elif desc_pos3_1 != -1 and action_pos3 != -1:
                extracted_text3 = text[desc_pos3_1 + len(" em nome d"):action_pos3].strip()
            elif desc_pos3_1 != -1 and action_pos3_1 != -1:  # Add missing condition here
                extracted_text3 = text[desc_pos3_1 + len(" em nome d"):action_pos3_1].strip()
            elif desc_pos3_2 != -1 and action_pos3_1 != -1:  # Add missing condition here:
                extracted_text3 = text[desc_pos3_2 + len(" a empresa "):action_pos3_1].strip()
            elif desc_pos3_2 != -1 and action_pos3 != -1:
                extracted_text3 = text[desc_pos3_2 + len(" a empresa "):action_pos3].strip()
            elif desc_pos3_1 != -1 and action_pos3_2 != -1:
                extracted_text3 = text[desc_pos3_1 + len(" em nome d"):action_pos3_2].strip()
            else:
                extracted_text3 = "nao achei"
            autuado = extracted_text3.replace("\n", "")

            #autuado = re.search(r'nome da empresa (.*),', text)

            nsei=re.search(r'[Pp]rocesso (.*),',text)
            """Extrai o CNPJ"""
            cnpj = re.search(r'CNPJ n.° (.*), e ', text)
            print("to sim")
            """Extrai o motivo do AUTO"""
            desc_pos2 = text.find("infringindo ")
            desc_pos2_1 = text.find("infringiu")
            action_pos2 = text.find("R$")
            if desc_pos2_1 != -1 and action_pos2:
                extracted_text2 = text[desc_pos2_1 + len("infringiu"):action_pos2].strip()
            elif desc_pos2 != -1 and action_pos2:
                extracted_text2 = text[desc_pos2 + len("infringindo "):action_pos2].strip()
            artigo = extracted_text2.replace("\n", "")

            desc_pos = text.find("desenvolvendo")
            desc_pos_1 = text.find("atividades")
            action_pos = text.find(".", max(desc_pos, desc_pos_1))
            if desc_pos != -1:
                extracted_text = text[desc_pos + len("desenvolvendo"):action_pos].strip()
            elif desc_pos_1 != -1:
                extracted_text = text[desc_pos_1 + len("atividades"):action_pos].strip()
            melhora_motivo = extracted_text.replace("\n", "")

            desc_pos1 = text.find("R$")
            action_pos1 = text.find('incidência', desc_pos1)
            action_pos1_2 = text.find('), ', desc_pos1)
            action_pos1_3 = text.find(') , ', desc_pos1)
            if action_pos1 != -1:
                extracted_text1 = text[desc_pos1 + len("R$"):action_pos1].strip()
            elif action_pos1_2 != -1:
                extracted_text1 = text[desc_pos1 + len("R$"):action_pos1_2].strip()
            elif action_pos1_3 != -1:
                extracted_text1 = text[desc_pos1 + len("R$"):action_pos1_3].strip()
            multa = extracted_text1.replace("\n", "")
            print("6 passo: Achei todos os dados do AUTO DE INFRAÇÃO")
            self.valBarra(0.25)
            if melhora_motivo:
                motivo_ai = melhora_motivo.lower()
                self.caixaai.insert("10.10", motivo_ai, "red")
                self.caixaai.tag_config("red", foreground="red")
            if nsei:
                nsei_ai= nsei.group(1)
                self.caixaai.insert("2.17", nsei_ai, "red")
                self.caixaai.tag_config("red", foreground="red")
            print(cnpj)
            if cnpj:
                cnpj_cpf_ai = cnpj.group(1)
                print(cnpj_cpf_ai)
                cnpj_cpf_ai = cnpj_cpf_ai[4:-8]
                self.caixaai.insert("5.6", f"***{cnpj_cpf_ai}***", "red")
                self.caixaai.tag_config("red", foreground="red")
            elif cnpj is None:
                cnpj2 = re.search(r'CNPJ (.*), ', text)
                if cnpj2:
                    cnpj_cpf_ai = cnpj2.group(1)
                    print(cnpj_cpf_ai)
                    cnpj_cpf_ai = cnpj_cpf_ai[4:-9]
                    self.caixaai.insert("5.6", f"***{cnpj_cpf_ai}***", "red")
                    self.caixaai.tag_config("red", foreground="red")
                elif cnpj2 is None:
                    cnpj3 = re.search(r'(\d{2}).(\d{3}).(\d{3})/(\d{4})-(\d{2})', text)
                    if cnpj3:
                        cnpj_cpf_ai = cnpj3.group()
                        print(cnpj_cpf_ai)
                        cnpj_cpf_ai = cnpj_cpf_ai[4:-8]
                        self.caixaai.insert("5.6", f"***{cnpj_cpf_ai}***", "red")
                        self.caixaai.tag_config("red", foreground="red")
                    elif cnpj3 is None:
                        cnpj4 = re.search(r'CNPJ (.+)/', text)
                        if cnpj4:
                            cnpj_cpf_ai = cnpj4.group(1)
                            print(cnpj_cpf_ai)
                            cnpj_cpf_ai = cnpj_cpf_ai[3:]
                            self.caixaai.insert("5.6", f"***{cnpj_cpf_ai}***", "red")
                            self.caixaai.tag_config("red", foreground="red")
            if autuado:
                autuado_ai = autuado.lower().title()
                self.caixaai.insert("4.12", str(autuado_ai), "red")  # Adiciona a tag "red" ao novo valor
                self.caixaai.tag_config("red", foreground="red")
            if multa:
                multa_ai = multa
                self.caixaai.insert("8.7", multa_ai, "red")  # Adiciona a tag "red" ao novo valor
                self.caixaai.tag_config("red", foreground="red")
            if artigo:
                artigo= artigo[:-50]
                artigo_ai= artigo
                self.caixaai.insert("3.8", artigo_ai, "red")  # Adiciona a tag "red" ao novo valor
                self.caixaai.tag_config("red", foreground="red")
            if nauto:
                print("n1")
                result_nauto_entry = nauto.group()
                nauto_ai = result_nauto_entry[8:]
                self.caixaai.insert("7.10", nauto_ai, "red")  # Adiciona a tag "red" ao novo valor
                self.caixaai.tag_config("red", foreground="red")
            elif nauto is None:
                nauto2 = re.search(r'N°(.*)/(\d{4})', text)
                nauto3 = re.search(r'Número(.*)/(\d{4})', text)
                nauto4 = re.search(r'Número;(.+)', text)
                nauto5 = re.search(r'AUTO DE INFRAÇÃO (.+)', text)
                if nauto2:
                    print("n2")
                    result_nauto2= nauto2.group()
                    nauto_ai = result_nauto2[3:]
                    self.caixaai.insert("7.10", nauto_ai, "red")  # Adiciona a tag "red" ao novo valor
                    self.caixaai.tag_config("red", foreground="red")
                elif nauto3:
                    result_nauto_entry = nauto3.group()
                    print("n3")
                    nauto_ai = result_nauto_entry[8:]
                    self.caixaai.insert("7.10", nauto_ai, "red")  # Adiciona a tag "red" ao novo valor
                    self.caixaai.tag_config("red", foreground="red")
                elif nauto4:
                    print("n4")
                    result_nauto4 = nauto4.group()
                    nauto_ai = result_nauto4[3:]
                    self.caixaai.insert("7.10", nauto_ai, "red")  # Adiciona a tag "red" ao novo valor
                    self.caixaai.tag_config("red", foreground="red")
                elif nauto5:
                    print("n5")
                    result_nauto5 = nauto5.group()
                    nauto_ai = result_nauto5[17:]
                    self.caixaai.insert("7.10", nauto_ai, "red")  # Adiciona a tag "red" ao novo valor
                    self.caixaai.tag_config("red", foreground="red")
            if complemento_data:
                data = re.search(r', (\d{1,2} de [A-Z][a-z]+ de \d{4})', text)
                if data:
                    print("data")
                    data_ai = data.group(1)
                    self.caixaai.insert("9.6", str(data_ai), "red")  # Adiciona a tag "red" ao novo valor
                    self.caixaai.tag_config("red", foreground="red")

                elif data is None:
                    data1 = re.search(r', (\d{1,2})(.*) de (\d{4})',text)
                    if data1:
                        print("data1")
                        result_data1 = data1.group()
                        data_ai = result_data1[2:]
                        self.caixaai.insert("9.6", str(data_ai), "red")  # Adiciona a tag "red" ao novo valor
                        self.caixaai.tag_config("red", foreground="red")
                    elif data1 is None:
                        data2 = re.search(r', [ ^]de (\w+) de (\d{4})', text)
                        if data2:
                            print("data2")
                            result_data2 = data2.group()
                            data_ai = result_data2[2:]
                            self.caixaai.insert("9.6", str(data_ai), "red")  # Adiciona a tag "red" ao novo valor
                            self.caixaai.tag_config("red", foreground="red")
                        elif data2 is None:
                            data3 = re.search(r', (.*) de (\d{4})\.', text)
                            if data3:
                                print("data3")
                                result_data3 = data3.group()
                                data_ai = result_data3[2:]
                                self.caixaai.insert("9.6", str(data_ai), "red")  # Adiciona a tag "red" ao novo valor
                                self.caixaai.tag_config("red", foreground="red")
            ce(pdf_reader, folhas_ai, crea_entry, pdf_file, num_pages)
##########################################################################################################
#           CREAS PR
##########################################################################################################
        """Descobre qual pagina do Auto de Infração"""
        def crea_entryspr(pdf_file, num_pages, crea_entry):

            self.valBarra(0.10)
            print("3 passo: Procura a pagina do AUTO DE INFRAÇÃO")
            pdf_reader = PdfReader(pdf_file)
            for page_num in range(num_pages):
                page = pdf_reader.pages[page_num]
                textpr = page.extract_text()
                print(page_num)
                pagautuado = re.search(r'AUTO DE INFRAÇÃO E NOTIFICAÇÃO', textpr)
                #complemento_pagautuado = re.search(r'PROCESSO ORIGEM(.+)', textpr)
                """Pagina do Auto de infração"""
                if pagautuado:
                    global folhas_ai
                    self.valBarra(0.15)

                    print("4 passo: Achei a pagina do AUTO DE INFRAÇÃO")
                    folhas_ai = page_num + 1
                    """Inserir folha do AUTO DE INFRAÇÃO"""
                    self.caixaai.insert("6.11", str(folhas_ai), "red")  # Adiciona a tag "red" ao novo valor
                    self.caixaai.tag_config("red", foreground="red")  # Configura a cor vermelha para a tag "red"
                    # folhas_entry)
                    pagedoautopr(folhas_ai, pdf_file, num_pages, crea_entry)
                    break
        """EXTRAINDO DADOS DO AUTO DE INFRAÇÃO"""
        def pagedoautopr(folhas_ai, pdf_file, num_pages, crea_entry):
            global nauto_ai
            global multa_ai
            global nsei_ai
            global autuado_ai
            global cnpj_cpf_ai
            global artigo_ai
            global motivo_ai
            global data_ai
            self.valBarra(0.20)
            print("5 passo: Procura todos os dados do AUTO DE INFRAÇÃO")
            pdf_reader = PdfReader(pdf_file)
            page = pdf_reader.pages[folhas_ai - 1]
            text = page.extract_text()

            complemento_data = re.search(r'Cientifique-se e cumpra-se', text)
            """Extrai o NUMERO DO AUTO"""

                # nauto = re.search(r'((Número[;:])|N°)(.+) / (\d{4})', text)
            nauto = re.search(r'^(.*?)Auto:', text)
            print(nauto)
                # nauto2 = re.search(r'AUTO DE INFRACAO N°(.+)', text)
            """Extrai o NOME DO AUTUADO"""
            autuado = re.search(r'(.*?)do CREA-PR', text)
            print("o autuado",autuado)
            #nsei = re.search(r'[Pp]rocesso (.*),', text)
            """Extrai o CNPJ"""
            cnpj = re.search(r'C.P.F./C.N.P.J.:(.+)', text)
            print("to sim")
            """Extrai o motivo do AUTO"""
            desc_pos2 = text.find("Atividade:")
                #desc_pos2_1 = text.find("infringiu")
            action_pos2 = text.find("Infração:")
            if desc_pos2 != -1 and action_pos2 != -1:
                extracted_text2 = text[desc_pos2 + len("Atividade:"):action_pos2].strip()
            else:
                extracted_text2 = ""
    #            elif desc_pos2 != -1 and action_pos2:
     #               extracted_text2 = text[desc_pos2 + len("infringindo "):action_pos2].strip()
            melhora_motivo = extracted_text2.replace("\n", "")

            artigo = re.search(r'Infração:(.+)', text)
            multa = re.search(r'cujo valor (.*)(\d{1,2})\.', text)


            print("6 passo: Achei todos os dados do AUTO DE INFRAÇÃO")
            self.valBarra(0.25)
            if melhora_motivo:
                motivo_ai = melhora_motivo.lower()
                self.caixaai.insert("10.10", motivo_ai, "red")
                self.caixaai.tag_config("red", foreground="red")

            print(cnpj)
            if cnpj:
                cnpj_cpf_ai = cnpj.group(1)
                print(cnpj_cpf_ai)
                cnpj_cpf_ai = cnpj_cpf_ai[4:-8]
                self.caixaai.insert("5.6", f"***{cnpj_cpf_ai}***", "red")
                self.caixaai.tag_config("red", foreground="red")
            elif cnpj is None:
                cnpj2 = re.search(r'CNPJ (.*), ', text)
                if cnpj2:
                    cnpj_cpf_ai = cnpj2.group(1)
                    print(cnpj_cpf_ai)
                    cnpj_cpf_ai = cnpj_cpf_ai[4:-9]
                    self.caixaai.insert("5.6", f"***{cnpj_cpf_ai}***", "red")
                    self.caixaai.tag_config("red", foreground="red")
                elif cnpj2 is None:
                    cnpj3 = re.search(r'(\d{2}).(\d{3}).(\d{3})/(\d{4})-(\d{2})', text)
                    if cnpj3:
                        cnpj_cpf_ai = cnpj3.group()
                        print(cnpj_cpf_ai)
                        cnpj_cpf_ai = cnpj_cpf_ai[4:-8]
                        self.caixaai.insert("5.6", f"***{cnpj_cpf_ai}***", "red")
                        self.caixaai.tag_config("red", foreground="red")
                    elif cnpj3 is None:
                        cnpj4 = re.search(r'CNPJ (.+)/', text)
                        if cnpj4:
                            cnpj_cpf_ai = cnpj4.group(1)
                            print(cnpj_cpf_ai)
                            cnpj_cpf_ai = cnpj_cpf_ai[3:]
                            self.caixaai.insert("5.6", f"***{cnpj_cpf_ai}***", "red")
                            self.caixaai.tag_config("red", foreground="red")
            if autuado:
                autuado_ai = autuado.group(1).title()
                self.caixaai.insert("4.12", str(autuado_ai), "red")  # Adiciona a tag "red" ao novo valor
                self.caixaai.tag_config("red", foreground="red")
            if multa:
                multa_ai = multa.group()
                self.caixaai.insert("8.7", multa_ai, "red")  # Adiciona a tag "red" ao novo valor
                self.caixaai.tag_config("red", foreground="red")
            if artigo:
                artigo = artigo[:-50]
                artigo_ai = artigo
                self.caixaai.insert("3.8", artigo_ai, "red")  # Adiciona a tag "red" ao novo valor
                self.caixaai.tag_config("red", foreground="red")
            if nauto:
                print("n1")
                result_nauto_entry = nauto.group()
                nauto_ai = result_nauto_entry[8:]
                self.caixaai.insert("7.10", nauto_ai, "red")  # Adiciona a tag "red" ao novo valor
                self.caixaai.tag_config("red", foreground="red")
            elif nauto is None:
                nauto2 = re.search(r'N°(.*)/(\d{4})', text)
                nauto3 = re.search(r'Número(.*)/(\d{4})', text)
                nauto4 = re.search(r'Número;(.+)', text)
                nauto5 = re.search(r'AUTO DE INFRAÇÃO (.+)', text)
                if nauto2:
                    print("n2")
                    result_nauto2 = nauto2.group()
                    nauto_ai = result_nauto2[3:]
                    self.caixaai.insert("7.10", nauto_ai, "red")  # Adiciona a tag "red" ao novo valor
                    self.caixaai.tag_config("red", foreground="red")
                elif nauto3:
                    result_nauto_entry = nauto3.group()
                    print("n3")
                    nauto_ai = result_nauto_entry[8:]
                    self.caixaai.insert("7.10", nauto_ai, "red")  # Adiciona a tag "red" ao novo valor
                    self.caixaai.tag_config("red", foreground="red")
                elif nauto4:
                    print("n4")
                    result_nauto4 = nauto4.group()
                    nauto_ai = result_nauto4[3:]
                    self.caixaai.insert("7.10", nauto_ai, "red")  # Adiciona a tag "red" ao novo valor
                    self.caixaai.tag_config("red", foreground="red")
                elif nauto5:
                    print("n5")
                    result_nauto5 = nauto5.group()
                    nauto_ai = result_nauto5[17:]
                    self.caixaai.insert("7.10", nauto_ai, "red")  # Adiciona a tag "red" ao novo valor
                    self.caixaai.tag_config("red", foreground="red")
            if complemento_data:
                data = re.search(r', (\d{2})/(\d{2})/(\d{4})', text)
                if data:
                    print("data")
                    data_ai = data.group(1)
                    self.caixaai.insert("9.6", str(data_ai), "red")  # Adiciona a tag "red" ao novo valor
                    self.caixaai.tag_config("red", foreground="red")
                elif data is None:
                    data1 = re.search(r', (\d{2})/(\d{2})/(\d{4})', text)
                    if data1:
                        print("data1")
                        result_data1 = data1.group()
                        data_ai = result_data1[2:]
                        self.caixaai.insert("9.6", str(data_ai), "red")  # Adiciona a tag "red" ao novo valor
                        self.caixaai.tag_config("red", foreground="red")
                    elif data1 is None:
                        data2 = re.search(r', [ ^]de (\w+) de (\d{4})', text)
                        if data2:
                            print("data2")
                            result_data2 = data2.group()
                            data_ai = result_data2[2:]
                            self.caixaai.insert("9.6", str(data_ai), "red")  # Adiciona a tag "red" ao novo valor
                            self.caixaai.tag_config("red", foreground="red")
                        elif data2 is None:
                            data3 = re.search(r', (.*) de (\d{4})\.', text)
                            if data3:
                                print("data3")
                                result_data3 = data3.group()
                                data_ai = result_data3[2:]
                                self.caixaai.insert("9.6", str(data_ai),"red")  # Adiciona a tag "red" ao novo valor
                                self.caixaai.tag_config("red", foreground="red")
            ce(pdf_reader, folhas_ai, crea_entry, pdf_file, num_pages)
##########################################################################################################
#           CREAS MS
##########################################################################################################
        """Descobre qual pagina do Auto de Infração"""
        def crea_entrysms(pdf_file, num_pages, crea_entry):
                    global folhas_ai
                    self.valBarra(0.10)
                    print("3 passo: Procura a pagina do AUTO DE INFRAÇÃO")
                    pdf_reader = PdfReader(pdf_file)
                    for page_num in range(num_pages):
                        page = pdf_reader.pages[page_num]
                        text = page.extract_text()
                        pagautuado = re.search(r'AUTO DE INFRAÇÃO Nº(.+)', text)
                        complemento_pagautuado = re.search(r'Autuado', text)

                        """Pagina do Auto de infração"""
                        if pagautuado and complemento_pagautuado:
                            self.valBarra(0.15)

                            print("4 passo: Achei a pagina do AUTO DE INFRAÇÃO")
                            folhas_ai = page_num + 1

                            self.caixaai.insert("6.11", str(folhas_ai), "red")  # Adiciona a tag "red" ao novo valor
                            self.caixaai.tag_config("red",foreground="red")  # Configura a cor vermelha para a tag "red"

                            pagedoautoms(folhas_ai, pdf_file, num_pages, crea_entry)
                            break
        """EXTRAINDO DADOS DO AUTO DE INFRAÇÃO"""
        def pagedoautoms(folhas_ai, pdf_file, num_pages, crea_entry):
                    global nauto_ai
                    global multa_ai
                    global nsei_ai
                    global autuado_ai
                    global cnpj_cpf_ai
                    global artigo_ai
                    global motivo_ai
                    global data_ai
                    self.valBarra(0.20)
                    print("5 passo: Procura todos os dados do AUTO DE INFRAÇÃO")
                    pdf_reader = PdfReader(pdf_file)
                    page = pdf_reader.pages[folhas_ai - 1]
                    text = page.extract_text()

                    """Extrai o AUTUADO do AUTO"""
                    desc_autuado = text.find("Razão")
                    action_autuado = text.find("CPF",desc_autuado)
                    if desc_autuado != -1 and action_autuado != -1:
                        extracted_autuado = text[desc_autuado + len("Razão"):action_autuado].strip()
                    autuado = extracted_autuado.replace("\n", "")

                    """Extrai o CNPJ"""
                    desc_cnpj = text.find("Razão")
                    action_cnpj = text.find("Endere", desc_cnpj)
                    if desc_cnpj != -1 and action_cnpj != -1:
                        extracted_cnpj = text[desc_cnpj + len("Razão"):action_cnpj].strip()
                    else:
                        extracted_cnpj = ""
                    cnpj1 = extracted_cnpj.replace("\n", "")
                    cnpj = ''.join(filter(str.isdigit, cnpj1))


                    """Extrai o motivo do AUTO"""
                    desc_pos2 = text.find("Descrição")
                    action_pos2 = text.find("Proprietário")
                    if desc_pos2 != -1 and action_pos2 != -1:
                        extracted_text2 = text[desc_pos2 + len("Descrição"):action_pos2].strip()
                    else:
                        extracted_text2 = ""
                    melhora_motivo = extracted_text2.replace("\n", "")

                    """Extrai o DATA do AUTO"""
                    data4 = re.search(r'(\d{1,2}) de (\w+) de (\d{4})', text)

                    """Extrai o artigo do AUTO"""
                    desc_artigo = text.find("Infração")
                    action_artigo = text.find("Valor da Multa")
                    if desc_artigo != -1 and action_artigo != -1:
                        extracted_artigo = text[desc_artigo + len("Infração"):action_artigo].strip()
                    else:
                        extracted_artigo = ""
                    artigo = extracted_artigo.replace("\n", "")

                    """Extrai o multa do AUTO"""
                    desc_multa = text.find("Valor da Multa")
                    action_multa = text.find("Data da Constatação")
                    if desc_multa != -1 and action_multa != -1:
                        extracted_multa = text[desc_multa + len("Valor da Multa"):action_multa].strip()
                    else:
                        extracted_multa = ""
                    multa = extracted_multa.replace("\n", "")

                    """Extrai o nauto do AUTO"""
                    desc_nauto = text.find("AUTO DE INFRAÇÃO Nº")
                    action_nauto = text.find("Num")
                    if desc_nauto != -1 and action_nauto != -1:
                        extracted_nauto = text[desc_nauto + len("AUTO DE INFRAÇÃO Nº"):action_nauto].strip()
                    else:
                        extracted_nauto = ""
                    nauto = extracted_nauto.replace("\n", "")

                    print("6 passo: Achei todos os dados do AUTO DE INFRAÇÃO")
                    self.valBarra(0.25)
                    if nauto:
                        nauto_ai = nauto
                        self.caixaai.insert("7.10", nauto_ai, "red")  # Adiciona a tag "red" ao novo valor
                        self.caixaai.tag_config("red", foreground="red")

                    if melhora_motivo:
                        motivo_ai = melhora_motivo.lower()
                        self.caixaai.insert("10.10", motivo_ai, "red")
                        self.caixaai.tag_config("red", foreground="red")

                    if cnpj:
                        cnpj_cpf_ai = cnpj
                        print(cnpj_cpf_ai)
                        cnpj_cpf_ai = cnpj_cpf_ai[3:8]
                        self.caixaai.insert("5.6", f"***{cnpj_cpf_ai}***", "red")
                        self.caixaai.tag_config("red", foreground="red")

                    if autuado:
                        autuado_ai = autuado.title()
                        self.caixaai.insert("4.12", autuado_ai, "red")  # Adiciona a tag "red" ao novo valor
                        self.caixaai.tag_config("red", foreground="red")
                    if multa:
                        multa_ai = multa.title()

                        self.caixaai.insert("8.7", multa_ai, "red")  # Adiciona a tag "red" ao novo valor
                        self.caixaai.tag_config("red", foreground="red")
                    if artigo:
                        artigo_ai = artigo
                        self.caixaai.insert("3.8", artigo_ai, "red")  # Adiciona a tag "red" ao novo valor
                        self.caixaai.tag_config("red", foreground="red")

                    if data4:
                        data_ai = data4.group()
                        print("data")
                        self.caixaai.insert("9.6", str(data_ai), "red")  # Adiciona a tag "red" ao novo valor
                        self.caixaai.tag_config("red", foreground="red")
                    ce(pdf_reader, folhas_ai, crea_entry, pdf_file, num_pages)
##########################################################################################################
#           CREAS RO
##########################################################################################################
        """Descobre qual pagina do Auto de Infração"""
        def crea_entrysro(pdf_file, num_pages, crea_entry):
            global folhas_ai
            self.valBarra(0.10)
            print("3 passo: Procura a pagina do AUTO DE INFRAÇÃO")
            pdf_reader = PdfReader(pdf_file)
            for page_num in range(num_pages):
                page = pdf_reader.pages[page_num]
                text = page.extract_text()
                pagautuado = re.search(r'AUTO DE INFRAÇÃO(.+)', text)
                complemento_pagautuado = re.search(r'DADOS DO AUTUADO', text)

                """Pagina do Auto de infração"""
                if pagautuado and complemento_pagautuado:
                    self.valBarra(0.15)

                    print("4 passo: Achei a pagina do AUTO DE INFRAÇÃO")
                    folhas_ai = page_num + 1

                    self.caixaai.insert("6.11", str(folhas_ai), "red")  # Adiciona a tag "red" ao novo valor
                    self.caixaai.tag_config("red", foreground="red")  # Configura a cor vermelha para a tag "red"

                    pagedoautoro(folhas_ai, pdf_file, num_pages, crea_entry)
                    break
        """EXTRAINDO DADOS DO AUTO DE INFRAÇÃO"""
        def pagedoautoro(folhas_ai, pdf_file, num_pages, crea_entry):
            global nauto_ai
            global multa_ai
            global nsei_ai
            global autuado_ai
            global cnpj_cpf_ai
            global artigo_ai
            global motivo_ai
            global data_ai
            self.valBarra(0.20)
            print("5 passo: Procura todos os dados do AUTO DE INFRAÇÃO")
            pdf_reader = PdfReader(pdf_file)
            page = pdf_reader.pages[folhas_ai - 1]
            text = page.extract_text()
            print(text)
            """Extrai o AUTUADO do AUTO"""
            desc_autuado = text.find("Autuado.")
            action_autuado = text.find("Cód.", desc_autuado)
            if desc_autuado != -1 and action_autuado != -1:
                extracted_autuado = text[desc_autuado + len("Autuado."):action_autuado].strip()
            autuado = extracted_autuado.replace("\n", "")

            """Extrai o CNPJ"""
            cnpj = re.search(r'CPF/CNPJ:(.+)',text)
            """desc_cnpj = text.find("Razão")
            action_cnpj = text.find("Endere", desc_cnpj)
            if desc_cnpj != -1 and action_cnpj != -1:
                extracted_cnpj = text[desc_cnpj + len("Razão"):action_cnpj].strip()
            else:
                extracted_cnpj = ""
            cnpj1 = extracted_cnpj.replace("\n", "")
            cnpj = ''.join(filter(str.isdigit, cnpj1))"""

            """Extrai o motivo do AUTO"""
            desc_pos2 = text.find("Descrição da Irregularidade")
            action_pos2 = text.find("Infração:")
            if desc_pos2 != -1 and action_pos2 != -1:
                extracted_text2 = text[desc_pos2 + len("Descrição da Irregularidade"):action_pos2].strip()
            else:
                extracted_text2 = ""
            melhora_motivo = extracted_text2.replace("\n", "")

            """Extrai o DATA do AUTO"""
            data4 = re.search(r'Lavratura Infração (\d{2})/(\d{2})/(\d{4})', text)

            """Extrai o artigo do AUTO"""
            artigo = re.search(r'Dispositivo Legal Infrigido(.*)Minima',text)
            """desc_artigo = text.find("Infração")
            action_artigo = text.find("Valor da Multa")
            if desc_artigo != -1 and action_artigo != -1:
                extracted_artigo = text[desc_artigo + len("Infração"):action_artigo].strip()
            else:
                extracted_artigo = ""
            artigo = extracted_artigo.replace("\n", "")"""

            """Extrai o multa do AUTO"""
            multa_minimo = re.search(r'Minima(.+)',text)
            multa_maxima = re.search(r'Máxima(.+)', text)
            if multa_minimo and multa_maxima:
                result_multa_minimo = multa_minimo.group(1)
                result_multa_maxima = multa_maxima.group(1)
                multa = result_multa_minimo + "até" + result_multa_maxima
            """desc_multa = text.find("Valor da Multa")
            action_multa = text.find("Data da Constatação")
            if desc_multa != -1 and action_multa != -1:
                extracted_multa = text[desc_multa + len("Valor da Multa"):action_multa].strip()
            else:
                extracted_multa = ""
            multa = extracted_multa.replace("\n", "")"""

            """Extrai o nauto do AUTO"""
            nauto = re.search(r'Conselho Regional de Engenharia e Agronomia de Rondônia(.+)', text)
            """desc_nauto = text.find("AUTO DE INFRAÇÃO Nº")
            action_nauto = text.find("Num")
            if desc_nauto != -1 and action_nauto != -1:
                extracted_nauto = text[desc_nauto + len("AUTO DE INFRAÇÃO Nº"):action_nauto].strip()
            else:
                extracted_nauto = ""
            nauto = extracted_nauto.replace("\n", "")"""

            print("6 passo: Achei todos os dados do AUTO DE INFRAÇÃO")
            self.valBarra(0.25)
            if nauto:
                nauto_ai = nauto.group(1)
                self.caixaai.insert("7.10", nauto_ai, "red")  # Adiciona a tag "red" ao novo valor
                self.caixaai.tag_config("red", foreground="red")

            if melhora_motivo:
                motivo_ai = melhora_motivo.lower()
                self.caixaai.insert("10.10", motivo_ai, "red")
                self.caixaai.tag_config("red", foreground="red")

            if cnpj:
                cnpj_cpf_ai = cnpj.group(1)
                print(cnpj_cpf_ai)
                cnpj_cpf_ai = cnpj_cpf_ai[3:8]
                self.caixaai.insert("5.6", f"***{cnpj_cpf_ai}***", "red")
                self.caixaai.tag_config("red", foreground="red")

            if autuado:
                autuado_ai = autuado.title()
                self.caixaai.insert("4.12", autuado_ai, "red")  # Adiciona a tag "red" ao novo valor
                self.caixaai.tag_config("red", foreground="red")
            if multa:
                multa_ai = multa

                self.caixaai.insert("8.7", multa_ai, "red")  # Adiciona a tag "red" ao novo valor
                self.caixaai.tag_config("red", foreground="red")
            if artigo:
                artigo_ai = artigo.group(1)
                self.caixaai.insert("3.8", artigo_ai, "red")  # Adiciona a tag "red" ao novo valor
                self.caixaai.tag_config("red", foreground="red")

            if data4:
                data1 = data4.group()
                data = re.search(r'(\d{2})/(\d{2})/(\d{4})', data1)
                configdataro(data)
            ce(pdf_reader, folhas_ai, crea_entry, pdf_file, num_pages)
        def configmesro(dia,mes_escrito,ano):
            global data_ai
            data_ai = f"{dia} de {mes_escrito} de {ano}"

            if data_ai:
                self.caixaai.insert("9.6", str(data_ai), "red")  # Adiciona a tag "red" ao novo valor
                self.caixaai.tag_config("red", foreground="red")
                return data_ai
        def configdataro(data):
            global data_ai
            dia = data.group(1)
            mes = data.group(2)
            ano = data.group(3)
            if mes == '01':
                mes_escrito = "janeiro"
                configmesro(dia,mes_escrito,ano)
            elif mes == '02':
                mes_escrito = "fevereiro"
                configmesro(dia,mes_escrito,ano)
            elif mes == '03':
                mes_escrito = "março"
                configmesro(dia,mes_escrito,ano)
            elif mes == '04':
                mes_escrito = "abril"
                configmesro(dia,mes_escrito,ano)
            elif mes == '05':
                mes_escrito = "maio"
                configmesro(dia,mes_escrito,ano)
            elif mes == '06':
                mes_escrito = "junho"
                configmesro(dia,mes_escrito,ano)
            elif mes == '07':
                mes_escrito = "julho"
                configmesro(dia,mes_escrito,ano)
            elif mes == '08':
                mes_escrito = "agosto"
                configmesro(dia,mes_escrito,ano)
            elif mes == '09':
                mes_escrito = "setembro"
                configmesro(dia,mes_escrito,ano)
            elif mes == '10':
                mes_escrito = "outubro"
                configmesro(dia,mes_escrito,ano)
            elif mes == '11':
                mes_escrito = "novembro"
                configmesro(dia,mes_escrito,ano)
            elif mes == '12':
                mes_escrito = "dezembro"
                configmesro(dia,mes_escrito,ano)
##########################################################################################################
#           ADICIONAIS
##########################################################################################################
        """Titulo horas trabalhada"""
        lb_h = ctk.CTkLabel(self.frame_1, text='Horas Trabalhadas:',fg_color='#4a89d3',text_color='black', bg_color='#094c8c',font=('Lato Regular', 30))
        lb_h.place(relx=0.60, rely=0.1, relwidth=0.25, relheight=0.2)
        lb_inicio = ctk.CTkLabel(self.frame_1, text='Inicio:', fg_color='#4a89d3', text_color='black',bg_color='#094c8c', font=('Lato Regular', 20))
        lb_inicio.place(relx=0.60, rely=0.3, relwidth=0.05, relheight=0.2)
        lb_fim = ctk.CTkLabel(self.frame_1, text='Fim:', fg_color='#4a89d3', text_color='black',bg_color='#094c8c', font=('Lato Regular', 20))
        lb_fim.place(relx=0.60, rely=0.5, relwidth=0.05, relheight=0.2)
        lb_total = ctk.CTkLabel(self.frame_1, text='TOTAL:', fg_color='#4a89d3', text_color='black',bg_color='#094c8c', font=('Lato Regular', 20))
        lb_total.place(relx=0.58, rely=0.7, relwidth=0.07, relheight=0.2)
        horas = ''
        lb_inicio_horario = ctk.CTkLabel(self.frame_1, text=horas, fg_color='#4a89d3', text_color='white',bg_color='#094c8c', font=('Lato Regular', 20))
        lb_inicio_horario.place(relx=0.65, rely=0.3, relwidth=0.05, relheight=0.2)
        lb_fim_horario = ctk.CTkLabel(self.frame_1, text=horas, fg_color='#4a89d3', text_color='white',bg_color='#094c8c', font=('Lato Regular', 20))
        lb_fim_horario.place(relx=0.65, rely=0.5, relwidth=0.05, relheight=0.2)

        horas_inicio = ''  # Inicialize as variáveis aqui para evitar problemas de escopo
        # Crie os rótulos com as horas vazias
        lb_inicio_horario = ctk.CTkLabel(self.frame_1, text=horas_inicio, fg_color='#4a89d3', text_color='white',bg_color='#094c8c', font=('Lato Regular', 20))
        lb_inicio_horario.place(relx=0.65, rely=0.3, relwidth=0.05, relheight=0.2)

        horas_fim = ''  # Inicialize as variáveis aqui para evitar problemas de escopo
        lb_fim_horario = ctk.CTkLabel(self.frame_1, text=horas_fim, fg_color='#4a89d3', text_color='white',bg_color='#094c8c', font=('Lato Regular', 20))
        lb_fim_horario.place(relx=0.65, rely=0.5, relwidth=0.05, relheight=0.2)
        def add_horas():
            nonlocal horas_inicio, horas_fim
            if horas_inicio == '':
                horario = datetime.now()
                horas_inicio = horario.strftime("%H:%M")
                lb_inicio_horario = ctk.CTkLabel(self.frame_1, text=horas_inicio, fg_color='#4a89d3', text_color='white',bg_color='#094c8c', font=('Lato Regular', 20))
                lb_inicio_horario.place(relx=0.65, rely=0.3, relwidth=0.05, relheight=0.2)
            elif horas_fim == '':
                horario = datetime.now()
                horas_fim = horario.strftime("%H:%M")
                lb_fim_horario = ctk.CTkLabel(self.frame_1, text=horas_fim, fg_color='#4a89d3', text_color='white',bg_color='#094c8c', font=('Lato Regular', 20))
                lb_fim_horario.place(relx=0.65, rely=0.5, relwidth=0.05, relheight=0.2)
                inicio_dt = datetime.strptime(horas_inicio, "%H:%M")
                fim_dt = datetime.strptime(horas_fim, "%H:%M")
                diferenca_tempo = fim_dt - inicio_dt
                horas_total = str(diferenca_tempo).split(":")[0]
                minutos_total = str(diferenca_tempo).split(":")[1]
                lb_total_horario = ctk.CTkLabel(self.frame_1, text=f"{horas_total}:{minutos_total}", fg_color='#4a89d3', text_color='white',bg_color='#094c8c', font=('Lato Regular', 20))
                lb_total_horario.place(relx=0.65, rely=0.7, relwidth=0.05, relheight=0.2)
            else:
                print("faz nada")
        """Botao salvar horas"""
        btn_pes = ctk.CTkButton(self.frame_1, text='Salvar', fg_color='#fff', text_color='#000', font=('Lato', 14),command=add_horas)
        btn_pes.place(relx=0.86, rely=0.4, relwidth=0.07, relheight=0.2)
        def tela_menu():

            if tela_texto is not None:
                self.texto_padrao.place_forget()
                if tela_historico is not None:
                    self.canvas.place_forget()
            elif tela_historico is not None:
                self.canvas.place_forget()
                if tela_texto is not None:
                    self.texto_padrao.place_forget()
            self.logo()

        def tela_historico():
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
            x_scrollbar = ctk.CTkScrollbar(self.root)
            x_scrollbar.place(relx=0.065, rely=0.97, relwidth=0.925, relheight=0.02)
            self.canvas = ctk.CTkCanvas(self.root, xscrollcommand=x_scrollbar.set)
            scrollable_frame = ctk.CTkFrame(self.canvas)
            scrollable_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
            self.canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
            self.canvas.place(relx=0.065, rely=0.26, relwidth=0.925, relheight=0.7)  # Manter o place para a tabela

            header = ["Ações", "id", "crea", "nsei", "artigo", "autuado", "cnpj_cpf", "folhas", "nauto", "multa",
                      "data",
                      "motivo", "folhasce", "ndecisaoce", "especialidade", "datace", "multace", "folhaspl",
                      "ndecisaopl",
                      "datapl", "multapl", "folharecurso", "datarecurso", "justificativa", "folhaaviso", "dataaviso",
                      "prazo",
                      "dias", "folhasart", "nart", "dataart", "folhascnpj", "datacnpj", "cnaeprimeiro", "cnaesegundo",
                      "folhasreincidencia", "datareincidencia", "folhasprocuracao", "nomeprocuracao", "folhasalteracao",
                      "nalteracao"]

            for x, y in enumerate(header):
                entry = ctk.CTkEntry(scrollable_frame, justify='center')
                entry.insert(0, y)
                entry.configure(state='readonly')
                if y.lower() == 'phone number':
                    entry.grid(row=0, column=x, ipadx=100, pady=5)
                else:
                    entry.grid(row=0, column=x, pady=5)

            for x in range(21):
                entry = ctk.CTkEntry(scrollable_frame, justify='center')
                entry.insert(0, x)
                entry.configure(state='readonly')
                entry.grid(row=x + 3, column=0, ipadx=3, pady=0)

                button = ctk.CTkButton(scrollable_frame, text='Apagar', fg_color='red')
                button.grid(row=x + 3, column=0, pady=0)

            # Barra deslizante horizontal

            self.canvas.configure(xscrollcommand=x_scrollbar.set)
            x_scrollbar.configure(command=self.canvas.xview, fg_color='red')

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
            print(artigo_ai)

            if ('alínea "b"' in artigo_ai or "alínea 'b'" in artigo_ai):
                self.texto_padrao = ctk.CTkTextbox(self.root, text_color='black', fg_color='white', font=('Lato Regular', 18))
                self.texto_padrao.tag_config("red", foreground="red")
                self.texto_padrao.insert(tk.INSERT,
                    """ALINEA B
                    Trata-se de recurso interposto ao Confea contra a decisão do Plenário do Crea-""" + str(crea_entry) + """ pela pessoa """ + str(autuado_ai) + """, CNPJ nº ***""" + str(cnpj_cpf_ai) + """***, autuada mediante o Auto de Infração n° """ + str(nauto_ai) + """, lavrado em """ + str(data_ai) + """, por infração """ + str(artigo_ai) + """, ao encontrar-se """ + str(motivo_ai) + """. (fls.""" + str(folhas_ai) + """  e """ + str(folhas_recurso) + """)
                    A Câmara Especializada de """ + str(especialidade_ce) + """ analisou os autos e concluiu pela manutenção da autuação, expedindo a Decisão nº """ + str(ndecisao_ce) + """, de """ + str(data_ce) + """ (fl. """ + str(folhas_ce) + """)
                    O recurso do(a) interessado(a) ao Plenário do Crea foi julgado mediante a Decisão nº """ + str(ndecisao_pl) + """, de """ + str(data_pl) + """, que decidiu manter a autuação. (fl. """ + str(folhas_pl) + """)
                    O(A) interessado(a) teve ciência da decisão do Plenário do Regional em """ + str(data_aviso) + """ e protocolizou, em """ + str(data_recurso) + """, no Crea-""" + str(crea_entry) + """, recurso ao Confea. (fls. """ + str(folhas_aviso) + """ e """ + str(folhas_recurso) + """)
                    Embora não conste do processo a informação da data em que o interessado(a) teve ciência da Decisão do Plenário do Regional, em """ + str(data_recurso) + """, foi protocolizado pelo interessado(a)""" + str(nome_procuracao) + """ no Crea-""" + str(crea_entry) + """ recurso ao Confea. (fls. """ + str(folhas_recurso) + """)
                    As folhas citadas neste parecer são relativas ao número da página eletrônica no SEI - XXXXX.
1.Análise

                    A PROCURAÇÃO ESTA NA PAGINA """+ str(folhas_procuracao)+"""
                    Considerando que o comprovante do Cadastro Nacional da Pessoa Jurídica – CNPJ, emitido em """ + str(data_cnpj) + """, apresenta como atividade econômica principal da interessada o “"""+ str(cnae_primeiro)+"""” e como atividades econômicas secundárias o, entre outras, “"""+ str(cnae_segundo)+"""”; (fls. """+ str(folhas_cnpj)+""")
                    REINCIDÊNCIA ESTA CITADA NA PAGINA """+ str(folhas_reincidencia)+"""
                    A ART ESTA NA PAGINA """+ str(folhas_art)+"""










                    Considerando que a alínea “e” do art. 27 da Lei nº 5.194, de 1966, estabelece que compete ao Confea julgar em última instância os recursos sobre registros, decisões e penalidades impostas pelos Conselhos Regionais;
                    Considerando que a alínea “a” do art. 6º da Lei nº 5.194, de 1966, prevê que exerce ilegalmente a profissão de engenheiro ou engenheiro - agrônomo a pessoa física ou jurídica que realizar atos ou prestar serviços, públicos ou privados, reservados aos profissionais de que trata a lei e que não possua registro nos Conselhos Regionais;
                    Considerando que o inciso II do art. 1º da Decisão Normativa nº 74, de 27 de agosto de 2004, esclarece que pessoas físicas leigas executando atividades privativas de profissionais fiscalizados pelo Sistema Confea / Crea estarão infringindo a alínea “a” do art. 6º da Lei nº 5.194, de 1966;
                    Considerando que o(a) interessado(a), em seu recurso ao Plenário do Confea, alegou que sintetizar alegações, se necessário fazer mais considerandos;
                    Considerando que não procedem as alegações constantes do recurso apresentado, visto que contra - argumentar o recurso;
                    Considerando que, não obstante as alegações apresentadas, o(a) interessado(a) motivou a lavratura do auto de infração, uma vez que fundamentar;
                    Considerando que a infração está capitulada na alínea “a” do art. 6º da Lei n° 5.194, de 1966, cuja penalidade está prevista no art. 71, alínea “c” – multa, combinado com o art. 73, alínea “d”, dessa lei;e
                    UTILIZAR CONFORME O CASO
                    Auto lavrado no ano de 2010:
                    Considerando que a multa, à época da autuação, encontrava-se regulamentada pela Resolução nº 513, de 21 de agosto de 2009, art. 4º, alínea “d”, no valor compreendido entre R$ 238,00 (duzentos e trinta e oito reais) e R$ 801,50 (oitocentos e um reais e cinquenta centavos),
                    Auto lavrado no ano de 2011:
                    Considerando que a multa, à época da autuação, encontrava-se regulamentada pela Resolução nº 518, de 24 de setembro de 2010, art. 5º, alínea “d”, no valor compreendido entre R$ 509,50 (quinhentos e nove reais e cinquenta centavos) e R$ 844,00 (oitocentos e quarenta e quatro reais),
                    Auto lavrado no ano de 2012:
                    Considerando que a multa, à época da autuação, encontrava-se regulamentada pela Resolução nº 524, de 3 de outubro de 2011, art. 4º, alínea “d”, no valor compreendido entre R$ 752,00 (setecentos e cinquenta e dois reais) e R$ 1.504,50 (mil, quinhentos e quatro reais e cinquenta centavos),
                    Auto lavrado no ano de 2013:
                    Considerando que a multa, à época da autuação, encontrava-se regulamentada pela Resolução nº 1.043, de 28 de setembro de 2012, art. 1º, alínea “d”, no valor compreendido entre R$ 792,53 (setecentos e noventa e dois reais e cinquenta e três centavos) e R$ 1.585,59 (mil, quinhentos e oitenta e cinco reais e cinquenta e nove centavos),
                    Auto lavrado no ano de 2014:
                    Considerando que a multa, à época da autuação, encontrava-se regulamentada pela Resolução nº 1.049, de 27 de setembro de 2013, art. 1º, alínea “d”, no valor compreendido entre R$ 840,64 (oitocentos e quarenta reais e sessenta e quatro centavos) e R$ 1.681,84 (mil, seiscentos e oitenta e um reais e oitenta e quatro centavos),
                    Auto lavrado no ano de 2015:
                    Considerando que a multa, à época da autuação, encontrava-se regulamentada pela Resolução nº 1.058, de 26 de setembro de 2014, art. 1º, alínea “d”, no valor compreendido entre R$ 894,36 (oitocentos e noventa e quatro reais e trinta e seis centavos) e R$ 1.788,72 (mil, setecentos e oitenta e oito reais e setenta e dois centavos),
                    Auto lavrado no ano de 2016:
                    Considerando que a multa, à época da autuação, encontrava-se regulamentada pela Resolução nº 1.066, de 25 de setembro de 2015, art. 18, com valores atualizados pela Decisão nº PL-2041/2015, de 25 de setembro de 2015, no valor compreendido entre R$ 982,72 (novecentos e oitenta e dois reais e setenta e dois centavos) e R$ 1.965,45 (mil, novecentos e sessenta e cinco reais e quarenta e cinco centavos),
                    Auto lavrado no ano de 2017:
                    Considerando que a multa, à época da autuação, encontrava-se regulamentada pela Resolução nº 1.066, de 25 de setembro de 2015, art. 18, com valores atualizados pela Decisão nº PL-1056/2016, de 22 de setembro de 2016, no valor compreendido entre R$ 1.077,30 (mil e setenta e sete reais e trinta centavos) e R$ 2.154,60 (dois mil, cento e cinquenta e quatro reais e sessenta centavos),
                    Auto lavrado no ano de 2018:
                    Considerando que a multa, à época da autuação, encontrava-se regulamentada pela Resolução nº 1.066, de 25 de setembro de 2015, art. 18, com valores atualizados pela Decisão nº PL-1758/2017, de 28 de setembro de 2017, no valor compreendido entre R$ 1.095,96 (mil e noventa e cinco reais e noventa e seis centavos) e R$ 2.191,91 (dois mil, cento e noventa e um reais e noventa e um centavos),
                    Auto lavrado no ano de 2019:
                    Considerando que a multa, à época da autuação, encontrava-se regulamentada pela Resolução nº 1.066, de 25 de setembro de 2015, art. 18, com valores atualizados pela Decisão nº PL-1611/2018, de 28 de setembro de 2018, no valor compreendido entre R$ 1.135,87 (mil cento e trinta e cinco reais e oitenta e sete centavos) e R$ 2.271,73 (dois mil duzentos e setenta e um reais e setenta e três centavos);
                    Auto lavrado no ano de 2020:
                    Considerando que a multa, à época da autuação, encontrava-se regulamentada pela Resolução nº 1.066, de 25 de setembro de 2015, art. 18, com valores atualizados pela Decisão nº PL-1544/2019, de 26 de setembro de 2019, no valor de R$ 1.173,17 (mil cento e setenta e três reais e dezessete centavos) a R$ 2.346,33 (dois mil trezentos e quarenta e seis reais e trinta e três centavos);
                    Auto lavrado no ano de 2021: 
                    Considerando que a multa, à época da autuação, encontrava-se regulamentada pela Resolução nº 1.066, de 25 de setembro de 2015, art. 18, com valores atualizados pela Decisão nº PL-1642/2020, de 29 de setembro de 2020, no valor de R$ 1.173,17 (mil cento e setenta e três reais e dezessete centavos) a R$ 2.346,33 (dois mil trezentos e quarenta e seis reais e trinta e três centavos), 
                    Auto lavrado no ano de 2022:
                    Considerando que a multa, à época da autuação, encontrava-se regulamentada pela Resolução nº 1.066, de 25 de setembro de 2015, art. 18, com valores atualizados pela Decisão nº PL-1513/2021, de 24 de setembro de 2021, no valor de R$ 1.173,17 (mil cento e setenta e três reais e dezessete centavos) a R$ 2.346,33 (dois mil trezentos e quarenta e seis reais e trinta e três centavos), 
                    Auto lavrado no ano de 2023: 
                    Considerando que a multa, à época da autuação, encontrava-se regulamentada pela Resolução nº 1.066, de 25 de setembro de 2015, art. 18, com valores atualizados pela Decisão nº PL-1457/2022, de 30 de setembro de 2022, no valor de R$ 1.276,71 (um mil duzentos e setenta e seis reais e setenta e um centavos)  a R$ 2.553,41 (dois mil quinhentos e cinquenta e três reais e quarenta e um centavos), 
                    OU
                    NO CASO DE O CREA TER FIXADO MULTA EM VALOR FORA DAS FAIXAS DA RESOLUÇÃO
                    Considerando que apesar de o Regional ter estabelecido a multa no valor de R$ (valor por extenso), a multa, à época da autuação, encontrava-se regulamentada pela Resolução nº colocar a resolução aplicável dos parágrafos acima,
                    ACRESCENTAR, SE NECESSÁRIO:
                    HAVENDO A REGULARIZAÇÃO DO FATO QUE ENSEJOU A AUTUAÇÃO, APÓS A LAVRATURA DO A.I.
                    Considerando que o § 2° do art. 11 da Resolução n° 1.008, de 9 de dezembro de 2004, estabelece que lavrado o auto de infração, a regularização da situação não exime o(a) autuado(a) das cominações legais;
                    Considerando que o § 3º do art. 43 dessa resolução dispõe que é facultada a redução de multas pelas instâncias julgadoras do Crea e do Confea nos casos previstos nesse artigo, respeitadas as faixas de valores estabelecidas em resolução específica;
                    Considerando que o(a) interessado(a) somente providenciou a regularização após a lavratura do auto de infração, mediante a contratação do(a) profissional Título abreviado conforme Res. nº 473/2002 Nome do profissional OU o registro da ART nº NÚMERO, em data, o que motiva a aplicação da multa em seu valor mínimo, tal como dispõe o inciso V do art. 43 da Resolução nº 1.008, de 2004; e (fl. ART ou contrato)
                    SE FOR PRIMÁRIO
                    Considerando que não foi comprovada nos autos a prática, pelo(a) interessado(a), de irregularidade anterior, capitulada no mesmo dispositivo legal e transitada em julgado,
                    E/OU
                    NO CASO DE REINCIDÊNCIA OU NOVA REINCIDÊNCIA
                    Considerando que o(a) interessado(a) incorreu em reincidência OU nova reincidência, comprovada nos autos mediante apontar documento que comprova, o que motiva a aplicação do valor da multa em dobro, conforme dispõem os §§ 1° e 2º do art. 43 da Resolução n° 1.008, de 9 de dezembro de 2004,
                    E/OU
                    QUANDO A SITUAÇÃO PERMITE A APLICAÇÃO DO ART. 43 DA RESOLUÇÃO Nº 1.008, DE 2004
                    Considerando que se trata de autuado(a) primário(a), conforme informações constantes do processo, não tendo sido imputada pena anterior pelo Crea ao(à) interessado(a), por esta ou outra infração à legislação do Sistema Confea/Crea e transitada em julgado;
                    E/OU
                    Considerando que a infração não pode ser considerada de caráter grave, justificada pela pouca repercussão, tendo ficado restrita à sua atuação ilegal, perante a legislação em comento;
                    E/OU
                    Considerando que a falta cometida não trouxe prejuízos diretamente a terceiros, bem como consequências de outra natureza que possa ser considerada insanável, podendo ser facilmente reparada e corrigida a linha de condução;
                    Considerando que os três critérios atenuantes acima estão previstos nos Incisos I, III e IV do art. 43 da Resolução nº 1.008, de 9 de dezembro de 2004; (Obs.: utilizar apenas os incisos aplicáveis ao caso)
                    Considerando a necessidade de cumprimento pelo Sistema Confea/Crea da finalidade de interesse público a que se destina;
                    Considerando que o(a) autuado(a) se enquadra nas questões acima, motivos pelos quais a multa deveria ter sido fixada pelo Crea em valor proporcional e razoável, comparativamente à falta cometida;
2. Conclusão
                    Sugerimos à Comissão de Ética e Exercício Profissional – CEEP propor ao Plenário do Confea:
                    2.1. conhecer o recurso interposto pelo(a) interessado(a) para, no mérito, negar-lhe provimento; e
                    NO CASO DE MANUTENÇÃO DO VALOR DA MULTA ESTABELECIDA PELO CREA
                    2.2. manter a aplicação de multa no valor de R$ (valor por extenso), conforme estabelecido pelo Regional, sem prejuízo da regularização da falta, a ser corrigido pelo Crea na forma da lei.
                    OU
                    EM CASOS GERAIS DE REINCIDÊNCIA
                    manter a aplicação de multa no valor de R$ (valor por extenso), já dobrado em função da comprovada reincidência, sem prejuízo da regularização da falta, a ser corrigido pelo Crea na forma da lei. (valor máximo ou qualquer valor estabelecido conforme faixa)
                    NO CASO DE REINCIDÊNCIA, REGULARIZAÇÃO E REDUÇÃO DO VALOR DA MULTA PELO CONFEA
                    2.2. manter a aplicação de multa no valor de R$ (valor por extenso), reduzido em função da regularização da falta e já dobrado devido a comprovada reincidência, a ser corrigido pelo Crea na forma da lei. (valor mínimo em função da regularização).
                    OU
                    NO CASO DE REDUÇÃO DA MULTA, EM FUNÇÃO DO CONTIDO NO ART. 43 DA RESOLUÇÃO Nº 1.008, DE 2004
                    2.2 - manter a aplicação de multa e reduzir o seu valor para R$ (valor por extenso), em função dos princípios de proporcionalidade e razoabilidade, relativamente à infração cometida, sem prejuízo da regularização da falta, a ser corrigido pelo Crea na forma da lei.
                    Observação: o “conforme estabelecido pelo Regional” deve ser utilizado somente nos casos em que o valor da multa do Crea divergir do valor correto da resolução.""")
                cores()
            elif ('alínea "e"' in artigo_ai or "alínea 'e'" in artigo_ai):
                    self.texto_padrao = ctk.CTkTextbox(self.root, text_color='black', fg_color='white', font=('Lato Regular', 18))
                    self.texto_padrao.tag_config("red", foreground="red")
                    self.texto_padrao.insert(tk.INSERT,
                                      """ALINEA E
                                      Trata-se de recurso interposto ao Confea contra a decisão do Plenário do Crea-""" + str(
                                          crea_entry) + """ pela pessoa """ + str(
                                          autuado_ai) + """, CNPJ nº ***""" + str(
                                          cnpj_cpf_ai) + """***, autuada mediante o Auto de Infração n° """ + str(
                                          nauto_ai) + """, lavrado em """ + str(data_ai) + """, por infração """ + str(
                                          artigo_ai) + """, ao  encontrar-se """ + str(motivo_ai) + """. (fls.""" + str(
                                          folhas_ai) + """  e """ + str(folhas_recurso) + """)
                            A Câmara Especializada de """ + str(
                                          especialidade_ce) + """ analisou os autos e concluiu pela manutenção da autuação, expedindo a Decisão nº """ + str(
                                          ndecisao_ce) + """, de """ + str(data_ce) + """ (fl. """ + str(folhas_ce) + """)
                            O recurso do(a) interessado(a) ao Plenário do Crea foi julgado mediante a Decisão nº """ + str(
                                          ndecisao_pl) + """, de """ + str(
                                          data_pl) + """, que decidiu manter a autuação. (fl. """ + str(folhas_pl) + """)
                            O(A) interessado(a) teve ciência da decisão do Plenário do Regional em """ + str(
                                          data_aviso) + """ e protocolizou, em """ + str(
                                          data_recurso) + """, no Crea-""" + str(
                                          crea_entry) + """, recurso ao Confea. (fls. """ + str(
                                          folhas_aviso) + """ e """ + str(folhas_recurso) + """)
                            Embora não conste do processo a informação da data em que o interessado(a) teve ciência da Decisão do Plenário do Regional, em """ + str(
                                          data_recurso) + """, foi protocolizado pelo interessado(a)""" + str(
                                          nome_procuracao) + """ no Crea-""" + str(
                                          crea_entry) + """ recurso ao Confea. (fls. """ + str(folhas_recurso) + """)
                            As folhas citadas neste parecer são relativas ao número da página eletrônica no SEI - XXXXX.
        1.Análise
        
        
                    A PROCURAÇÃO ESTA NA PAGINA """+ str(folhas_procuracao)+"""
                    Considerando que o comprovante do Cadastro Nacional da Pessoa Jurídica – CNPJ, emitido em """ + str(data_cnpj) + """, apresenta como atividade econômica principal da interessada o “"""+ str(cnae_primeiro)+"""” e como atividades econômicas secundárias o, entre outras, “"""+ str(cnae_segundo)+"""”; (fls. """+ str(folhas_cnpj)+""")
                    REINCIDÊNCIA ESTA CITADA NA PAGINA """+ str(folhas_reincidencia)+"""
                    A ART ESTA NA PAGINA """+ str(folhas_art)+"""

        
        
        
        
        
        
        
        
        
                            Considerando que a alínea “e” do art. 27 da Lei nº 5.194, de 1966, estabelece que compete ao Confea julgar em última instância os recursos sobre registros, decisões e penalidades impostas pelos Conselhos Regionais;
                            Considerando que a alínea “a” do art. 6º da Lei nº 5.194, de 1966, prevê que exerce ilegalmente a profissão de engenheiro ou engenheiro - agrônomo a pessoa física ou jurídica que realizar atos ou prestar serviços, públicos ou privados, reservados aos profissionais de que trata a lei e que não possua registro nos Conselhos Regionais;
                            Considerando que o inciso II do art. 1º da Decisão Normativa nº 74, de 27 de agosto de 2004, esclarece que pessoas físicas leigas executando atividades privativas de profissionais fiscalizados pelo Sistema Confea / Crea estarão infringindo a alínea “a” do art. 6º da Lei nº 5.194, de 1966;
                            Considerando que o(a) interessado(a), em seu recurso ao Plenário do Confea, alegou que sintetizar alegações, se necessário fazer mais considerandos;
                            Considerando que não procedem as alegações constantes do recurso apresentado, visto que contra - argumentar o recurso;
                            Considerando que, não obstante as alegações apresentadas, o(a) interessado(a) motivou a lavratura do auto de infração, uma vez que fundamentar;
                            Considerando que a infração está capitulada na alínea “a” do art. 6º da Lei n° 5.194, de 1966, cuja penalidade está prevista no art. 71, alínea “c” – multa, combinado com o art. 73, alínea “d”, dessa lei;e
                            UTILIZAR CONFORME O CASO
                            Auto lavrado no ano de 2010:
                            Considerando que a multa, à época da autuação, encontrava-se regulamentada pela Resolução nº 513, de 21 de agosto de 2009, art. 4º, alínea “d”, no valor compreendido entre R$ 238,00 (duzentos e trinta e oito reais) e R$ 801,50 (oitocentos e um reais e cinquenta centavos),
                            Auto lavrado no ano de 2011:
                            Considerando que a multa, à época da autuação, encontrava-se regulamentada pela Resolução nº 518, de 24 de setembro de 2010, art. 5º, alínea “d”, no valor compreendido entre R$ 509,50 (quinhentos e nove reais e cinquenta centavos) e R$ 844,00 (oitocentos e quarenta e quatro reais),
                            Auto lavrado no ano de 2012:
                            Considerando que a multa, à época da autuação, encontrava-se regulamentada pela Resolução nº 524, de 3 de outubro de 2011, art. 4º, alínea “d”, no valor compreendido entre R$ 752,00 (setecentos e cinquenta e dois reais) e R$ 1.504,50 (mil, quinhentos e quatro reais e cinquenta centavos),
                            Auto lavrado no ano de 2013:
                            Considerando que a multa, à época da autuação, encontrava-se regulamentada pela Resolução nº 1.043, de 28 de setembro de 2012, art. 1º, alínea “d”, no valor compreendido entre R$ 792,53 (setecentos e noventa e dois reais e cinquenta e três centavos) e R$ 1.585,59 (mil, quinhentos e oitenta e cinco reais e cinquenta e nove centavos),
                            Auto lavrado no ano de 2014:
                            Considerando que a multa, à época da autuação, encontrava-se regulamentada pela Resolução nº 1.049, de 27 de setembro de 2013, art. 1º, alínea “d”, no valor compreendido entre R$ 840,64 (oitocentos e quarenta reais e sessenta e quatro centavos) e R$ 1.681,84 (mil, seiscentos e oitenta e um reais e oitenta e quatro centavos),
                            Auto lavrado no ano de 2015:
                            Considerando que a multa, à época da autuação, encontrava-se regulamentada pela Resolução nº 1.058, de 26 de setembro de 2014, art. 1º, alínea “d”, no valor compreendido entre R$ 894,36 (oitocentos e noventa e quatro reais e trinta e seis centavos) e R$ 1.788,72 (mil, setecentos e oitenta e oito reais e setenta e dois centavos),
                            Auto lavrado no ano de 2016:
                            Considerando que a multa, à época da autuação, encontrava-se regulamentada pela Resolução nº 1.066, de 25 de setembro de 2015, art. 18, com valores atualizados pela Decisão nº PL-2041/2015, de 25 de setembro de 2015, no valor compreendido entre R$ 982,72 (novecentos e oitenta e dois reais e setenta e dois centavos) e R$ 1.965,45 (mil, novecentos e sessenta e cinco reais e quarenta e cinco centavos),
                            Auto lavrado no ano de 2017:
                            Considerando que a multa, à época da autuação, encontrava-se regulamentada pela Resolução nº 1.066, de 25 de setembro de 2015, art. 18, com valores atualizados pela Decisão nº PL-1056/2016, de 22 de setembro de 2016, no valor compreendido entre R$ 1.077,30 (mil e setenta e sete reais e trinta centavos) e R$ 2.154,60 (dois mil, cento e cinquenta e quatro reais e sessenta centavos),
                            Auto lavrado no ano de 2018:
                            Considerando que a multa, à época da autuação, encontrava-se regulamentada pela Resolução nº 1.066, de 25 de setembro de 2015, art. 18, com valores atualizados pela Decisão nº PL-1758/2017, de 28 de setembro de 2017, no valor compreendido entre R$ 1.095,96 (mil e noventa e cinco reais e noventa e seis centavos) e R$ 2.191,91 (dois mil, cento e noventa e um reais e noventa e um centavos),
                            Auto lavrado no ano de 2019:
                            Considerando que a multa, à época da autuação, encontrava-se regulamentada pela Resolução nº 1.066, de 25 de setembro de 2015, art. 18, com valores atualizados pela Decisão nº PL-1611/2018, de 28 de setembro de 2018, no valor compreendido entre R$ 1.135,87 (mil cento e trinta e cinco reais e oitenta e sete centavos) e R$ 2.271,73 (dois mil duzentos e setenta e um reais e setenta e três centavos);
                            Auto lavrado no ano de 2020:
                            Considerando que a multa, à época da autuação, encontrava-se regulamentada pela Resolução nº 1.066, de 25 de setembro de 2015, art. 18, com valores atualizados pela Decisão nº PL-1544/2019, de 26 de setembro de 2019, no valor de R$ 1.173,17 (mil cento e setenta e três reais e dezessete centavos) a R$ 2.346,33 (dois mil trezentos e quarenta e seis reais e trinta e três centavos);
                            Auto lavrado no ano de 2021: 
                            Considerando que a multa, à época da autuação, encontrava-se regulamentada pela Resolução nº 1.066, de 25 de setembro de 2015, art. 18, com valores atualizados pela Decisão nº PL-1642/2020, de 29 de setembro de 2020, no valor de R$ 1.173,17 (mil cento e setenta e três reais e dezessete centavos) a R$ 2.346,33 (dois mil trezentos e quarenta e seis reais e trinta e três centavos), 
                            Auto lavrado no ano de 2022:
                            Considerando que a multa, à época da autuação, encontrava-se regulamentada pela Resolução nº 1.066, de 25 de setembro de 2015, art. 18, com valores atualizados pela Decisão nº PL-1513/2021, de 24 de setembro de 2021, no valor de R$ 1.173,17 (mil cento e setenta e três reais e dezessete centavos) a R$ 2.346,33 (dois mil trezentos e quarenta e seis reais e trinta e três centavos), 
                            Auto lavrado no ano de 2023: 
                            Considerando que a multa, à época da autuação, encontrava-se regulamentada pela Resolução nº 1.066, de 25 de setembro de 2015, art. 18, com valores atualizados pela Decisão nº PL-1457/2022, de 30 de setembro de 2022, no valor de R$ 1.276,71 (um mil duzentos e setenta e seis reais e setenta e um centavos)  a R$ 2.553,41 (dois mil quinhentos e cinquenta e três reais e quarenta e um centavos), 
                            OU
                            NO CASO DE O CREA TER FIXADO MULTA EM VALOR FORA DAS FAIXAS DA RESOLUÇÃO
                            Considerando que apesar de o Regional ter estabelecido a multa no valor de R$ (valor por extenso), a multa, à época da autuação, encontrava-se regulamentada pela Resolução nº colocar a resolução aplicável dos parágrafos acima,
                            ACRESCENTAR, SE NECESSÁRIO:
                            HAVENDO A REGULARIZAÇÃO DO FATO QUE ENSEJOU A AUTUAÇÃO, APÓS A LAVRATURA DO A.I.
                            Considerando que o § 2° do art. 11 da Resolução n° 1.008, de 9 de dezembro de 2004, estabelece que lavrado o auto de infração, a regularização da situação não exime o(a) autuado(a) das cominações legais;
                            Considerando que o § 3º do art. 43 dessa resolução dispõe que é facultada a redução de multas pelas instâncias julgadoras do Crea e do Confea nos casos previstos nesse artigo, respeitadas as faixas de valores estabelecidas em resolução específica;
                            Considerando que o(a) interessado(a) somente providenciou a regularização após a lavratura do auto de infração, mediante a contratação do(a) profissional Título abreviado conforme Res. nº 473/2002 Nome do profissional OU o registro da ART nº NÚMERO, em data, o que motiva a aplicação da multa em seu valor mínimo, tal como dispõe o inciso V do art. 43 da Resolução nº 1.008, de 2004; e (fl. ART ou contrato)
                            SE FOR PRIMÁRIO
                            Considerando que não foi comprovada nos autos a prática, pelo(a) interessado(a), de irregularidade anterior, capitulada no mesmo dispositivo legal e transitada em julgado,
                            E/OU
                            NO CASO DE REINCIDÊNCIA OU NOVA REINCIDÊNCIA
                            Considerando que o(a) interessado(a) incorreu em reincidência OU nova reincidência, comprovada nos autos mediante apontar documento que comprova, o que motiva a aplicação do valor da multa em dobro, conforme dispõem os §§ 1° e 2º do art. 43 da Resolução n° 1.008, de 9 de dezembro de 2004,
                            E/OU
                            QUANDO A SITUAÇÃO PERMITE A APLICAÇÃO DO ART. 43 DA RESOLUÇÃO Nº 1.008, DE 2004
                            Considerando que se trata de autuado(a) primário(a), conforme informações constantes do processo, não tendo sido imputada pena anterior pelo Crea ao(à) interessado(a), por esta ou outra infração à legislação do Sistema Confea/Crea e transitada em julgado;
                            E/OU
                            Considerando que a infração não pode ser considerada de caráter grave, justificada pela pouca repercussão, tendo ficado restrita à sua atuação ilegal, perante a legislação em comento;
                            E/OU
                            Considerando que a falta cometida não trouxe prejuízos diretamente a terceiros, bem como consequências de outra natureza que possa ser considerada insanável, podendo ser facilmente reparada e corrigida a linha de condução;
                            Considerando que os três critérios atenuantes acima estão previstos nos Incisos I, III e IV do art. 43 da Resolução nº 1.008, de 9 de dezembro de 2004; (Obs.: utilizar apenas os incisos aplicáveis ao caso)
                            Considerando a necessidade de cumprimento pelo Sistema Confea/Crea da finalidade de interesse público a que se destina;
                            Considerando que o(a) autuado(a) se enquadra nas questões acima, motivos pelos quais a multa deveria ter sido fixada pelo Crea em valor proporcional e razoável, comparativamente à falta cometida;
        2. Conclusão
                            Sugerimos à Comissão de Ética e Exercício Profissional – CEEP propor ao Plenário do Confea:
                            2.1. conhecer o recurso interposto pelo(a) interessado(a) para, no mérito, negar-lhe provimento; e
                            NO CASO DE MANUTENÇÃO DO VALOR DA MULTA ESTABELECIDA PELO CREA
                            2.2. manter a aplicação de multa no valor de R$ (valor por extenso), conforme estabelecido pelo Regional, sem prejuízo da regularização da falta, a ser corrigido pelo Crea na forma da lei.
                            OU
                            EM CASOS GERAIS DE REINCIDÊNCIA
                            manter a aplicação de multa no valor de R$ (valor por extenso), já dobrado em função da comprovada reincidência, sem prejuízo da regularização da falta, a ser corrigido pelo Crea na forma da lei. (valor máximo ou qualquer valor estabelecido conforme faixa)
                            NO CASO DE REINCIDÊNCIA, REGULARIZAÇÃO E REDUÇÃO DO VALOR DA MULTA PELO CONFEA
                            2.2. manter a aplicação de multa no valor de R$ (valor por extenso), reduzido em função da regularização da falta e já dobrado devido a comprovada reincidência, a ser corrigido pelo Crea na forma da lei. (valor mínimo em função da regularização).
                            OU
                            NO CASO DE REDUÇÃO DA MULTA, EM FUNÇÃO DO CONTIDO NO ART. 43 DA RESOLUÇÃO Nº 1.008, DE 2004
                            2.2 - manter a aplicação de multa e reduzir o seu valor para R$ (valor por extenso), em função dos princípios de proporcionalidade e razoabilidade, relativamente à infração cometida, sem prejuízo da regularização da falta, a ser corrigido pelo Crea na forma da lei.
                            Observação: o “conforme estabelecido pelo Regional” deve ser utilizado somente nos casos em que o valor da multa do Crea divergir do valor correto da resolução.""")
                    cores()
            elif ('alínea "a"' in artigo_ai or "alínea 'a'" in artigo_ai):
                    self.texto_padrao = ctk.CTkTextbox(self.root, text_color='black', fg_color='white', font=('Lato Regular', 18))
                    self.texto_padrao.tag_config("red", foreground="red")
                    self.texto_padrao.insert(tk.INSERT,
                                      """ALINEA A
                                      Trata-se de recurso interposto ao Confea contra a decisão do Plenário do Crea-""" + str(
                                          crea_entry) + """ pela pessoa """ + str(
                                          autuado_ai) + """, CNPJ nº ***""" + str(
                                          cnpj_cpf_ai) + """***, autuada mediante o Auto de Infração n° """ + str(
                                          nauto_ai) + """, lavrado em """ + str(data_ai) + """, por infração """ + str(
                                          artigo_ai) + """, ao  encontrar-se """ + str(motivo_ai) + """. (fls.""" + str(
                                          folhas_ai) + """  e """ + str(folhas_recurso) + """)
                            A Câmara Especializada de """ + str(
                                          especialidade_ce) + """ analisou os autos e concluiu pela manutenção da autuação, expedindo a Decisão nº """ + str(
                                          ndecisao_ce) + """, de """ + str(data_ce) + """ (fl. """ + str(folhas_ce) + """)
                            O recurso do(a) interessado(a) ao Plenário do Crea foi julgado mediante a Decisão nº """ + str(
                                          ndecisao_pl) + """, de """ + str(
                                          data_pl) + """, que decidiu manter a autuação. (fl. """ + str(folhas_pl) + """)
                            O(A) interessado(a) teve ciência da decisão do Plenário do Regional em """ + str(
                                          data_aviso) + """ e protocolizou, em """ + str(
                                          data_recurso) + """, no Crea-""" + str(
                                          crea_entry) + """, recurso ao Confea. (fls. """ + str(
                                          folhas_aviso) + """ e """ + str(folhas_recurso) + """)
                            Embora não conste do processo a informação da data em que o interessado(a) teve ciência da Decisão do Plenário do Regional, em """ + str(
                                          data_recurso) + """, foi protocolizado pelo interessado(a)""" + str(
                                          nome_procuracao) + """ no Crea-""" + str(
                                          crea_entry) + """ recurso ao Confea. (fls. """ + str(folhas_recurso) + """)
                            As folhas citadas neste parecer são relativas ao número da página eletrônica no SEI - XXXXX.
        1.Análise
        
        
                    A PROCURAÇÃO ESTA NA PAGINA """+ str(folhas_procuracao)+"""
                    Considerando que o comprovante do Cadastro Nacional da Pessoa Jurídica – CNPJ, emitido em """ + str(data_cnpj) + """, apresenta como atividade econômica principal da interessada o “"""+ str(cnae_primeiro)+"""” e como atividades econômicas secundárias o, entre outras, “"""+ str(cnae_segundo)+"""”; (fls. """+ str(folhas_cnpj)+""")
                    REINCIDÊNCIA ESTA CITADA NA PAGINA """+ str(folhas_reincidencia)+"""
                    A ART ESTA NA PAGINA """+ str(folhas_art)+"""









        
                            Considerando que a alínea “e” do art. 27 da Lei nº 5.194, de 1966, estabelece que compete ao Confea julgar em última instância os recursos sobre registros, decisões e penalidades impostas pelos Conselhos Regionais;
                            Considerando que a alínea “a” do art. 6º da Lei nº 5.194, de 1966, prevê que exerce ilegalmente a profissão de engenheiro ou engenheiro - agrônomo a pessoa física ou jurídica que realizar atos ou prestar serviços, públicos ou privados, reservados aos profissionais de que trata a lei e que não possua registro nos Conselhos Regionais;
                            Considerando que o inciso II do art. 1º da Decisão Normativa nº 74, de 27 de agosto de 2004, esclarece que pessoas físicas leigas executando atividades privativas de profissionais fiscalizados pelo Sistema Confea / Crea estarão infringindo a alínea “a” do art. 6º da Lei nº 5.194, de 1966;
                            Considerando que o(a) interessado(a), em seu recurso ao Plenário do Confea, alegou que sintetizar alegações, se necessário fazer mais considerandos;
                            Considerando que não procedem as alegações constantes do recurso apresentado, visto que contra - argumentar o recurso;
                            Considerando que, não obstante as alegações apresentadas, o(a) interessado(a) motivou a lavratura do auto de infração, uma vez que fundamentar;
                            Considerando que a infração está capitulada na alínea “a” do art. 6º da Lei n° 5.194, de 1966, cuja penalidade está prevista no art. 71, alínea “c” – multa, combinado com o art. 73, alínea “d”, dessa lei;e
                            UTILIZAR CONFORME O CASO
                            Auto lavrado no ano de 2010:
                            Considerando que a multa, à época da autuação, encontrava-se regulamentada pela Resolução nº 513, de 21 de agosto de 2009, art. 4º, alínea “d”, no valor compreendido entre R$ 238,00 (duzentos e trinta e oito reais) e R$ 801,50 (oitocentos e um reais e cinquenta centavos),
                            Auto lavrado no ano de 2011:
                            Considerando que a multa, à época da autuação, encontrava-se regulamentada pela Resolução nº 518, de 24 de setembro de 2010, art. 5º, alínea “d”, no valor compreendido entre R$ 509,50 (quinhentos e nove reais e cinquenta centavos) e R$ 844,00 (oitocentos e quarenta e quatro reais),
                            Auto lavrado no ano de 2012:
                            Considerando que a multa, à época da autuação, encontrava-se regulamentada pela Resolução nº 524, de 3 de outubro de 2011, art. 4º, alínea “d”, no valor compreendido entre R$ 752,00 (setecentos e cinquenta e dois reais) e R$ 1.504,50 (mil, quinhentos e quatro reais e cinquenta centavos),
                            Auto lavrado no ano de 2013:
                            Considerando que a multa, à época da autuação, encontrava-se regulamentada pela Resolução nº 1.043, de 28 de setembro de 2012, art. 1º, alínea “d”, no valor compreendido entre R$ 792,53 (setecentos e noventa e dois reais e cinquenta e três centavos) e R$ 1.585,59 (mil, quinhentos e oitenta e cinco reais e cinquenta e nove centavos),
                            Auto lavrado no ano de 2014:
                            Considerando que a multa, à época da autuação, encontrava-se regulamentada pela Resolução nº 1.049, de 27 de setembro de 2013, art. 1º, alínea “d”, no valor compreendido entre R$ 840,64 (oitocentos e quarenta reais e sessenta e quatro centavos) e R$ 1.681,84 (mil, seiscentos e oitenta e um reais e oitenta e quatro centavos),
                            Auto lavrado no ano de 2015:
                            Considerando que a multa, à época da autuação, encontrava-se regulamentada pela Resolução nº 1.058, de 26 de setembro de 2014, art. 1º, alínea “d”, no valor compreendido entre R$ 894,36 (oitocentos e noventa e quatro reais e trinta e seis centavos) e R$ 1.788,72 (mil, setecentos e oitenta e oito reais e setenta e dois centavos),
                            Auto lavrado no ano de 2016:
                            Considerando que a multa, à época da autuação, encontrava-se regulamentada pela Resolução nº 1.066, de 25 de setembro de 2015, art. 18, com valores atualizados pela Decisão nº PL-2041/2015, de 25 de setembro de 2015, no valor compreendido entre R$ 982,72 (novecentos e oitenta e dois reais e setenta e dois centavos) e R$ 1.965,45 (mil, novecentos e sessenta e cinco reais e quarenta e cinco centavos),
                            Auto lavrado no ano de 2017:
                            Considerando que a multa, à época da autuação, encontrava-se regulamentada pela Resolução nº 1.066, de 25 de setembro de 2015, art. 18, com valores atualizados pela Decisão nº PL-1056/2016, de 22 de setembro de 2016, no valor compreendido entre R$ 1.077,30 (mil e setenta e sete reais e trinta centavos) e R$ 2.154,60 (dois mil, cento e cinquenta e quatro reais e sessenta centavos),
                            Auto lavrado no ano de 2018:
                            Considerando que a multa, à época da autuação, encontrava-se regulamentada pela Resolução nº 1.066, de 25 de setembro de 2015, art. 18, com valores atualizados pela Decisão nº PL-1758/2017, de 28 de setembro de 2017, no valor compreendido entre R$ 1.095,96 (mil e noventa e cinco reais e noventa e seis centavos) e R$ 2.191,91 (dois mil, cento e noventa e um reais e noventa e um centavos),
                            Auto lavrado no ano de 2019:
                            Considerando que a multa, à época da autuação, encontrava-se regulamentada pela Resolução nº 1.066, de 25 de setembro de 2015, art. 18, com valores atualizados pela Decisão nº PL-1611/2018, de 28 de setembro de 2018, no valor compreendido entre R$ 1.135,87 (mil cento e trinta e cinco reais e oitenta e sete centavos) e R$ 2.271,73 (dois mil duzentos e setenta e um reais e setenta e três centavos);
                            Auto lavrado no ano de 2020:
                            Considerando que a multa, à época da autuação, encontrava-se regulamentada pela Resolução nº 1.066, de 25 de setembro de 2015, art. 18, com valores atualizados pela Decisão nº PL-1544/2019, de 26 de setembro de 2019, no valor de R$ 1.173,17 (mil cento e setenta e três reais e dezessete centavos) a R$ 2.346,33 (dois mil trezentos e quarenta e seis reais e trinta e três centavos);
                            Auto lavrado no ano de 2021: 
                            Considerando que a multa, à época da autuação, encontrava-se regulamentada pela Resolução nº 1.066, de 25 de setembro de 2015, art. 18, com valores atualizados pela Decisão nº PL-1642/2020, de 29 de setembro de 2020, no valor de R$ 1.173,17 (mil cento e setenta e três reais e dezessete centavos) a R$ 2.346,33 (dois mil trezentos e quarenta e seis reais e trinta e três centavos), 
                            Auto lavrado no ano de 2022:
                            Considerando que a multa, à época da autuação, encontrava-se regulamentada pela Resolução nº 1.066, de 25 de setembro de 2015, art. 18, com valores atualizados pela Decisão nº PL-1513/2021, de 24 de setembro de 2021, no valor de R$ 1.173,17 (mil cento e setenta e três reais e dezessete centavos) a R$ 2.346,33 (dois mil trezentos e quarenta e seis reais e trinta e três centavos), 
                            Auto lavrado no ano de 2023: 
                            Considerando que a multa, à época da autuação, encontrava-se regulamentada pela Resolução nº 1.066, de 25 de setembro de 2015, art. 18, com valores atualizados pela Decisão nº PL-1457/2022, de 30 de setembro de 2022, no valor de R$ 1.276,71 (um mil duzentos e setenta e seis reais e setenta e um centavos)  a R$ 2.553,41 (dois mil quinhentos e cinquenta e três reais e quarenta e um centavos), 
                            OU
                            NO CASO DE O CREA TER FIXADO MULTA EM VALOR FORA DAS FAIXAS DA RESOLUÇÃO
                            Considerando que apesar de o Regional ter estabelecido a multa no valor de R$ (valor por extenso), a multa, à época da autuação, encontrava-se regulamentada pela Resolução nº colocar a resolução aplicável dos parágrafos acima,
                            ACRESCENTAR, SE NECESSÁRIO:
                            HAVENDO A REGULARIZAÇÃO DO FATO QUE ENSEJOU A AUTUAÇÃO, APÓS A LAVRATURA DO A.I.
                            Considerando que o § 2° do art. 11 da Resolução n° 1.008, de 9 de dezembro de 2004, estabelece que lavrado o auto de infração, a regularização da situação não exime o(a) autuado(a) das cominações legais;
                            Considerando que o § 3º do art. 43 dessa resolução dispõe que é facultada a redução de multas pelas instâncias julgadoras do Crea e do Confea nos casos previstos nesse artigo, respeitadas as faixas de valores estabelecidas em resolução específica;
                            Considerando que o(a) interessado(a) somente providenciou a regularização após a lavratura do auto de infração, mediante a contratação do(a) profissional Título abreviado conforme Res. nº 473/2002 Nome do profissional OU o registro da ART nº NÚMERO, em data, o que motiva a aplicação da multa em seu valor mínimo, tal como dispõe o inciso V do art. 43 da Resolução nº 1.008, de 2004; e (fl. ART ou contrato)
                            SE FOR PRIMÁRIO
                            Considerando que não foi comprovada nos autos a prática, pelo(a) interessado(a), de irregularidade anterior, capitulada no mesmo dispositivo legal e transitada em julgado,
                            E/OU
                            NO CASO DE REINCIDÊNCIA OU NOVA REINCIDÊNCIA
                            Considerando que o(a) interessado(a) incorreu em reincidência OU nova reincidência, comprovada nos autos mediante apontar documento que comprova, o que motiva a aplicação do valor da multa em dobro, conforme dispõem os §§ 1° e 2º do art. 43 da Resolução n° 1.008, de 9 de dezembro de 2004,
                            E/OU
                            QUANDO A SITUAÇÃO PERMITE A APLICAÇÃO DO ART. 43 DA RESOLUÇÃO Nº 1.008, DE 2004
                            Considerando que se trata de autuado(a) primário(a), conforme informações constantes do processo, não tendo sido imputada pena anterior pelo Crea ao(à) interessado(a), por esta ou outra infração à legislação do Sistema Confea/Crea e transitada em julgado;
                            E/OU
                            Considerando que a infração não pode ser considerada de caráter grave, justificada pela pouca repercussão, tendo ficado restrita à sua atuação ilegal, perante a legislação em comento;
                            E/OU
                            Considerando que a falta cometida não trouxe prejuízos diretamente a terceiros, bem como consequências de outra natureza que possa ser considerada insanável, podendo ser facilmente reparada e corrigida a linha de condução;
                            Considerando que os três critérios atenuantes acima estão previstos nos Incisos I, III e IV do art. 43 da Resolução nº 1.008, de 9 de dezembro de 2004; (Obs.: utilizar apenas os incisos aplicáveis ao caso)
                            Considerando a necessidade de cumprimento pelo Sistema Confea/Crea da finalidade de interesse público a que se destina;
                            Considerando que o(a) autuado(a) se enquadra nas questões acima, motivos pelos quais a multa deveria ter sido fixada pelo Crea em valor proporcional e razoável, comparativamente à falta cometida;
        2. Conclusão
                            Sugerimos à Comissão de Ética e Exercício Profissional – CEEP propor ao Plenário do Confea:
                            2.1. conhecer o recurso interposto pelo(a) interessado(a) para, no mérito, negar-lhe provimento; e
                            NO CASO DE MANUTENÇÃO DO VALOR DA MULTA ESTABELECIDA PELO CREA
                            2.2. manter a aplicação de multa no valor de R$ (valor por extenso), conforme estabelecido pelo Regional, sem prejuízo da regularização da falta, a ser corrigido pelo Crea na forma da lei.
                            OU
                            EM CASOS GERAIS DE REINCIDÊNCIA
                            manter a aplicação de multa no valor de R$ (valor por extenso), já dobrado em função da comprovada reincidência, sem prejuízo da regularização da falta, a ser corrigido pelo Crea na forma da lei. (valor máximo ou qualquer valor estabelecido conforme faixa)
                            NO CASO DE REINCIDÊNCIA, REGULARIZAÇÃO E REDUÇÃO DO VALOR DA MULTA PELO CONFEA
                            2.2. manter a aplicação de multa no valor de R$ (valor por extenso), reduzido em função da regularização da falta e já dobrado devido a comprovada reincidência, a ser corrigido pelo Crea na forma da lei. (valor mínimo em função da regularização).
                            OU
                            NO CASO DE REDUÇÃO DA MULTA, EM FUNÇÃO DO CONTIDO NO ART. 43 DA RESOLUÇÃO Nº 1.008, DE 2004
                            2.2 - manter a aplicação de multa e reduzir o seu valor para R$ (valor por extenso), em função dos princípios de proporcionalidade e razoabilidade, relativamente à infração cometida, sem prejuízo da regularização da falta, a ser corrigido pelo Crea na forma da lei.
                            Observação: o “conforme estabelecido pelo Regional” deve ser utilizado somente nos casos em que o valor da multa do Crea divergir do valor correto da resolução.""")
                    cores()
            elif ("59" in artigo_ai):
                        print("artigo 59")
                        self.texto_padrao = ctk.CTkTextbox(self.root, text_color='black', fg_color='white', font=('Lato Regular', 18))
                        self.texto_padrao.tag_config("red", foreground="red")
                        self.texto_padrao.insert(tk.INSERT,
                                          """art 59
                                          Trata-se de recurso interposto ao Confea contra a decisão do Plenário do Crea-""" + str(
                                              crea_entry) + """ pela pessoa jurídica """ + str(
                                              autuado_ai) + """, CNPJ nº ***""" + str(
                                              cnpj_cpf_ai) + """***, autuada mediante o Auto de Infração n° """ + str(
                                              nauto_ai) + """, lavrado em """ + str(
                                              data_ai) + """, por infração ao art. 59 da Lei n° 5.194, ao  encontrar-se """ + str(
                                              motivo_ai) + """, sem possuir registro no Crea-""" + str(
                                              crea_entry) + """. (fls.""" + str(folhas_ai) + """  e """ + str(
                                              folhas_recurso) + """)
                            A Câmara Especializada de """ + str(
                                              especialidade_ce) + """ analisou os autos e concluiu pela manutenção da autuação, expedindo a Decisão nº """ + str(
                                              ndecisao_ce) + """, de """ + str(data_ce) + """ (fl. """ + str(
                                              folhas_ce) + """)
                            O recurso do(a) interessado(a) ao Plenário do Crea foi julgado mediante a Decisão nº """ + str(
                                              ndecisao_pl) + """, de """ + str(
                                              data_pl) + """, que decidiu manter a autuação. (fl. """ + str(folhas_pl) + """)
                            O(A) interessado(a) teve ciência da decisão do Plenário do Regional em """ + str(
                                              data_aviso) + """ e protocolizou, em """ + str(
                                              data_recurso) + """, no Crea-""" + str(
                                              crea_entry) + """, recurso ao Confea. (fls. """ + str(
                                              folhas_aviso) + """ e """ + str(folhas_recurso) + """)
                            Embora não conste do processo a informação da data em que o interessado(a) teve ciência da Decisão do Plenário do Regional, em """ + str(
                                              data_recurso) + """, foi protocolizado pelo interessado(a)""" + str(
                                              nome_procuracao) + """ no Crea-""" + str(
                                              crea_entry) + """ recurso ao Confea. (fls. """ + str(folhas_recurso) + """)
                            As folhas citadas neste parecer são relativas ao número da página eletrônica no SEI - XXXXX.
            1. Análise
            
            
                    A PROCURAÇÃO ESTA NA PAGINA """+ str(folhas_procuracao)+"""
                    Considerando que o comprovante do Cadastro Nacional da Pessoa Jurídica – CNPJ, emitido em """ + str(data_cnpj) + """, apresenta como atividade econômica principal da interessada o “"""+ str(cnae_primeiro)+"""” e como atividades econômicas secundárias o, entre outras, “"""+ str(cnae_segundo)+"""”; (fls. """+ str(folhas_cnpj)+""")
                    REINCIDÊNCIA ESTA CITADA NA PAGINA """+ str(folhas_reincidencia)+"""
                    A ART ESTA NA PAGINA """+ str(folhas_art)+"""

                        
                        
                        
                        
                        
                        
                        
                        
                        
                        Considerando que a alínea “e” do art. 27 da Lei nº 5.194, de 1966, estabelece que compete ao Confea julgar em última instância os recursos sobre registros, decisões e penalidades impostas pelos Conselhos Regionais;
                        Considerando que o art. 59 da Lei nº 5.194, de 1966, prevê que as firmas, sociedades, associações, companhias, cooperativas e empresas em geral, que se organizem para executar obras ou serviços relacionados na forma estabelecida nessa lei, só poderão iniciar suas atividades depois de promoverem o competente registro nos Conselhos Regionais, bem como o dos profissionais do seu quadro técnico;
                        Considerando que o art. 1º da Lei nº 6.839, de 30 de outubro de 1980, determina que o registro de empresas e a anotação dos profissionais legalmente habilitados, delas encarregados, serão obrigatórios nas entidades competentes para a fiscalização do exercício das diversas profissões, em razão da atividade básica ou em relação àquela pela qual prestem serviços a terceiros;
                        Considerando que o art. 3º da Resolução nº 336, de 27 de outubro de 1989, vigente à época da autuação, dispõe que o registro de pessoa jurídica é ato obrigatório de inscrição no Conselho Regional de Engenharia e Agronomia onde ela inicia suas atividades profissionais no campo técnico da Engenharia, Agronomia, Geologia, Geografia ou Meteorologia; OU
                        Considerando que os arts. 2º e 3º da Resolução nº 1.121, de 13 de dezembro de 2019, vigente à época da autuação, dispõem respectivamente que o registro é a inscrição da pessoa jurídica nos assentamentos do Crea da circunscrição onde ela inicia suas atividades envolvendo o exercício de profissões fiscalizadas pelo Sistema Confea/Crea; e o registro é obrigatório para a pessoa jurídica que possua atividade básica ou que execute efetivamente serviços para terceiros envolvendo o exercício de profissões fiscalizadas pelo Sistema Confea/Crea; 
                        Considerando que o inciso III do art. 1º da Decisão Normativa nº 74, de 27 de agosto de 2004, esclarece que pessoas jurídicas com objetivo social relacionado às atividades privativas de profissionais fiscalizados pelo Sistema Confea/Crea, sem registro no Crea, estarão infringindo o art. 59, com multa prevista na alínea “c” do art. 73 da Lei nº 5.194, de 1966;
                        PARA O CASO DE A FISCALIZAÇÃO NÃO CONSTATAR EM LOCO O EXERCÍCIO DE ATIVIDADES DE ENGENHARIA PELA PJ AUTUADA
                        Considerando, em que pese a edição da Dec. Plen. n° 0980/2022, de 8 de julho de 2022, a qual [sic] "Informa ao Crea-RN, em resposta a consulta formulada por meio do Ofício nº 436/2021-PRES (0532856), que conclui-se, que a mera constituição formal da pessoa jurídica perante o Registro de Pessoas Jurídicas sem o respectivo registro perante o Crea não é suficiente para a autuação com base no art. 59 c/c alínea "c", do art. 73, da Lei nº 5.194, de 1966 pois a caracterização da infração depende da demonstração do efetivo desempenho de atividade abrangida pelo Sistema Confea/Crea", pontuamos que a Decisão Normativa nº 74, de 2004, encontra-se em pleno vigor, motivo pelo qual o(a) Auto de Infração e Notificação n° NÚMERO, lavrado(a) em data, é pertinente;
                        PARA OS DEMAIS CASOS
                        Considerando que a interessada, em seu recurso ao Plenário do Confea, alegou que sintetizar alegações, se necessário fazer mais considerandos;
                        Considerando que o Contrato Social OU o Estatuto Social OU a Alteração do Contrato Social da pessoa jurídica estabelece em sua cláusula NÚMERO que a sociedade tem por objeto social texto objetivo social; (fls. XX)
                        E/OU
                        Considerando que o comprovante do Cadastro Nacional da Pessoa Jurídica – CNPJ, emitido em data, apresenta como atividade econômica principal da interessada o(a) “texto da certidão do CNPJ” e como atividade(s) econômica(s) secundária(s) o(a), entre outras, “texto da certidão do CNPJ”; (fls. XX OU cópia anexa)
                        SE FOR O CASO   
                        Considerando que o art. 1º da Resolução nº 417, de 27 de março de 1998, estabelece que, para efeito de registro nos Conselhos Regionais, consideram-se enquadradas nos arts. 59 e 60 da Lei nº 5.194, de 1966, as indústrias tipo de indústria (código);
                        Considerando que não procedem as alegações constantes do recurso apresentado, visto que a interessada desenvolve atividades no ramo da Engenharia OU Agronomia, razão pela qual deve possuir registro no Crea-UF e profissional(ais) registrado(s) em seu quadro técnico, com conhecimentos em processos ou atividades – VER DOCUMENTO DO GRUPO TÉCNICO DA ENGENHARIA QUÍMICA, SE FOR O CASO (Decisão PL-0577/2018), dada à responsabilidade técnica inerente ao desenvolvimento de objetivo social;
                        Considerando se for o caso, contra-argumentar outras alegações;
                        Considerando que a infração está capitulada no art. 59 da Lei n° 5.194, de 1966, cuja penalidade está prevista no art. 71, alínea “c” – multa, combinado com o art. 73, alínea “c”, dessa lei; e
                        UTILIZAR CONFORME O CASO
                        Auto lavrado no ano de 2010:
                        Considerando que a multa, à época da autuação, encontrava-se regulamentada pela Resolução nº 513, de 21 de agosto de 2009, art. 4º, alínea “c”, no valor compreendido entre R$ 238,00 (duzentos e trinta e oito reais) e R$ 484,00 (quatrocentos e oitenta e quatro reais),
                        Auto lavrado no ano de 2011:
                        Considerando que a multa, à época da autuação, encontrava-se regulamentada pela Resolução nº 518, de 24 de setembro de 2010, art. 5º, alínea “c”, no valor compreendido entre R$ 250,50 (duzentos e cinquenta reais e cinquenta centavos) e R$ 509,50 (quinhentos e nove reais e cinquenta centavos),
                        Auto lavrado no ano de 2012:
                        Considerando que a multa, à época da autuação, encontrava-se regulamentada pela Resolução nº 524, de 3 de outubro de 2011, art. 4º, alínea “c”, no valor compreendido entre R$ 752,00 (setecentos e cinquenta e dois reais) e R$ 1.504,50 (mil, quinhentos e quatro reais e cinquenta centavos),
                        Auto lavrado no ano de 2013:
                        Considerando que a multa, à época da autuação, encontrava-se regulamentada pela Resolução nº 1.043, de 28 de setembro de 2012, art. 1º, alínea “c”, no valor compreendido entre R$ 792,53 (setecentos e noventa e dois reais e cinquenta e três centavos) e R$ 1.585,59 (mil, quinhentos e oitenta e cinco reais e cinquenta e nove centavos),
                        Auto lavrado no ano de 2014:
                        Considerando que a multa, à época da autuação, encontrava-se regulamentada pela Resolução nº 1.049, de 27 de setembro de 2013, art. 1º, alínea “c”, no valor compreendido entre R$ 840,64 (oitocentos e quarenta reais e sessenta e quatro centavos) e R$ 1.681,84 (mil, seiscentos e oitenta e um reais e oitenta e quatro centavos),
                        Auto lavrado no ano de 2015:
                        Considerando que a multa, à época da autuação, encontrava-se regulamentada pela Resolução nº 1.058, de 26 de setembro de 2014, art. 1º, alínea “c”, no valor compreendido entre R$ 894,36 (oitocentos e noventa e quatro reais e trinta e seis centavos) e R$ 1.788,72 (mil, setecentos e oitenta e oito reais e setenta e dois centavos),
                        Auto lavrado no ano de 2016:
                        Considerando que a multa, à época da autuação, encontrava-se regulamentada pela Resolução nº 1.066, de 25 de setembro de 2015, art. 18, com valores atualizados pela Decisão nº PL-2041/2015, de 25 de setembro de 2015, no valor compreendido entre R$ 982,72 (novecentos e oitenta e dois reais e setenta e dois centavos) e R$ 1.965,45 (mil, novecentos e sessenta e cinco reais e quarenta e cinco centavos),
                        Auto lavrado no ano de 2017:
                        Considerando que a multa, à época da autuação, encontrava-se regulamentada pela Resolução nº 1.066, de 25 de setembro de 2015, art. 18, com valores atualizados pela Decisão nº PL-1056/2016, de 22 de setembro de 2016, no valor compreendido entre R$ 1.077,30 (mil e setenta e sete reais e trinta centavos) e R$ 2.154,60 (dois mil, cento e cinquenta e quatro reais e sessenta centavos),
                        Auto lavrado no ano de 2018:
                        Considerando que a multa, à época da autuação, encontrava-se regulamentada pela Resolução nº 1.066, de 25 de setembro de 2015, art. 18, com valores atualizados pela Decisão nº PL-1758/2017, de 28 de setembro de 2017, no valor compreendido entre R$ 1.095,96 (mil e noventa e cinco reais e noventa e seis centavos) e R$ 2.191,91 (dois mil, cento e noventa e um reais e noventa e um centavos),
                        Auto lavrado no ano de 2019:
                        Considerando que a multa, à época da autuação, encontrava-se regulamentada pela Resolução nº 1.066, de 25 de setembro de 2015, art. 18, com valores atualizados pela Decisão nº PL-1611/2018, de 28 de setembro de 2018, no valor compreendido entre R$ 1.135,87 (mil cento e trinta e cinco reais e oitenta e sete centavos) e R$ 2.271,73 (dois mil duzentos e setenta e um reais e setenta e três centavos);
                        Auto lavrado no ano de 2020: 
                        Considerando que a multa, à época da autuação, encontrava-se regulamentada pela Resolução nº 1.066, de 25 de setembro de 2015, art. 18, com valores atualizados pela Decisão nº PL-1544/2019, de 26 de setembro de 2019, no valor de R$ 1.173,17 (mil cento e setenta e três reais e dezessete centavos) e R$ 2.346,33 (dois mil trezentos e quarenta e seis reais e trinta e três centavos);
                        Auto lavrado no ano de 2021: 
                        Considerando que a multa, à época da autuação, encontrava-se regulamentada pela Resolução nº 1.066, de 25 de setembro de 2015, art. 18, com valores atualizados pela Decisão nº PL-1642/2020, de 29 de setembro de 2020, no valor de R$ 1.173,17 (mil cento e setenta e três reais e dezessete centavos) e R$ 2.346,33 (dois mil trezentos e quarenta e seis reais e trinta e três centavos);
                        Auto lavrado no ano de 2022: 
                        Considerando que a multa, à época da autuação, encontrava-se regulamentada pela Resolução nº 1.066, de 25 de setembro de 2015, art. 18, com valores atualizados pela Decisão nº PL-1513/2021, de 24 de setembro de 2021, no valor de R$ 1.173,17 (mil cento e setenta e três reais e dezessete centavos) e R$ 2.346,33 (dois mil trezentos e quarenta e seis reais e trinta e três centavos), 
                        Auto lavrado no ano de 2023: 
                        Considerando que a multa, à época da autuação, encontrava-se regulamentada pela Resolução nº 1.066, de 25 de setembro de 2015, art. 18, com valores atualizados pela Decisão nº PL-1457/2022, de 30 de setembro de 2022, no valor de R$ 1.276,71 (mil duzentos e setenta e seis reais e setenta e um centavo) a R$ 2.553,41 (dois mil quinhentos e cinquenta e três reais e quarenta e um centavos), 
                        OU
                        NO CASO DE O CREA TER FIXADO MULTA EM VALOR FORA DAS FAIXAS DA RESOLUÇÃO
                        Considerando que apesar de o Regional ter estabelecido a multa no valor de R$ (valor por extenso), a multa, à época da autuação, encontrava-se regulamentada pela Resolução nº colocar a resolução aplicável dos parágrafos acima,
                        ACRESCENTAR, SE NECESSÁRIO:
                        HAVENDO A REGULARIZAÇÃO DO FATO QUE ENSEJOU A AUTUAÇÃO, APÓS A LAVRATURA DO A.I.
                        Considerando que o § 2° do art. 11 da Resolução n° 1.008, de 9 de dezembro de 2004, estabelece que lavrado o auto de infração, a regularização da situação não exime a autuada das cominações legais;
                        Considerando que o § 3º do art. 43 dessa resolução prevê que é facultada a redução de multas pelas instâncias julgadoras do Crea e do Confea nos casos previstos nesse artigo, respeitadas as faixas de valores estabelecidas em resolução específica;
                        Considerando que a interessada somente providenciou a regularização após a lavratura do auto de infração, mediante o registro no Crea-UF, em data, o que motiva a aplicação da multa em seu valor mínimo, tal como dispõe o inciso V do art. 43 da Resolução nº 1.008, de 2004; e (fl. XX)
                        SE FOR PRIMÁRIO
                        Considerando que não foi comprovada nos autos a prática, pela interessada, de irregularidade anterior, capitulada no mesmo dispositivo legal e transitada em julgado,
                        E/OU
                        NO CASO DE REINCIDÊNCIA OU NOVA REINCIDÊNCIA
                        Considerando que a interessada incorreu em reincidência OU nova reincidência, comprovada nos autos mediante apontar documento que comprova, o que motiva a aplicação do valor da multa em dobro, conforme dispõem os §§ 1° e 2º do art. 43 da Resolução n° 1.008, de 9 de dezembro de 2004,
                        E/OU
                        QUANDO A INTERESSADA INFORMAR IMPOSSIBILIDADE DE PAGAMENTO DA MULTA – COLOCAR APENAS O CONSIDERANDO
                        Considerando que a Resolução nº 1.118, de 26 de julho de 2019, prevê a possibilidade de parcelamento de débitos, desde que atendidas as condições estipuladas na resolução, (Obs.: utilizar a partir de 1º/1/2020, data na qual se iniciam os efeitos da resolução, que revogou a Resolução nº 479, de 2003)
                        E/OU
                        QUANDO A SITUAÇÃO PERMITE A APLICAÇÃO DO ART. 43 DA RESOLUÇÃO Nº 1.008, DE 2004
                        Considerando que se trata de autuado(a) primário(a), conforme informações constantes do processo, não tendo sido imputada pena anterior pelo Crea ao(à) interessado(a), por esta ou outra infração à legislação do Sistema Confea/Crea e transitada em julgado;
                        E/OU
                        Considerando que a infração não pode ser considerada de caráter grave, justificada pela pouca repercussão, tendo ficado restrita à sua atuação ilegal, perante a legislação em comento;
                        E/OU
                        Considerando que a falta cometida não trouxe prejuízos diretamente a terceiros, bem como consequências de outra natureza que possa ser considerada insanável, podendo ser facilmente reparada e corrigida a linha de condução;
                        Considerando que os três critérios atenuantes acima estão previstos nos Incisos I, III e IV do art. 43 da Resolução nº 1.008, de 9 de dezembro de 2004; (Obs.: utilizar apenas os incisos aplicáveis ao caso)
                        Considerando a necessidade de cumprimento pelo Sistema Confea/Crea da finalidade de interesse público a que se destina;
                        Considerando que o(a) autuado(a) se enquadra nas questões acima, motivos pelos quais a multa deveria ter sido fixada pelo Crea em valor proporcional e razoável, comparativamente à falta cometida;
            2. Conclusão
                        Sugerimos à Comissão de Ética e Exercício Profissional – CEEP propor ao Plenário do Confea: 
                        2.1. conhecer o recurso interposto pelo(a) interessado(a) para, no mérito, negar-lhe provimento;    
                        NO CASO DE MANUTENÇÃO DO VALOR DA MULTA ESTABELECIDA PELO CREA
                        2.2. manter a aplicação de multa no valor de R$ (valor por extenso), conforme estabelecido pelo Regional, sem prejuízo da regularização da falta, a ser corrigido pelo Crea na forma da lei.
                        OU
                        EM CASOS GERAIS DE REINCIDÊNCIA
                        manter a aplicação de multa no valor de R$ (valor por extenso), já dobrado em função da comprovada reincidência, sem prejuízo da regularização da falta, a ser corrigido pelo Crea na forma da lei. (valor máximo ou qualquer valor estabelecido conforme faixa)
                        NO CASO DE REINCIDÊNCIA, REGULARIZAÇÃO E REDUÇÃO DO VALOR DA MULTA PELO CONFEA
                        2.2. manter a aplicação de multa no valor de R$ (valor por extenso), reduzido em função da regularização da falta e já dobrado devido a comprovada reincidência, a ser corrigido pelo Crea na forma da lei. (valor mínimo em função da regularização).
                        OU
                        NO CASO DE REDUÇÃO DA MULTA, EM FUNÇÃO DO CONTIDO NO ART. 43 DA RESOLUÇÃO Nº 1.008, DE 2004
                        2.2 - manter a aplicação de multa e reduzir o seu valor para R$ (valor por extenso), em função dos princípios de proporcionalidade e razoabilidade, relativamente à infração cometida, sem prejuízo da regularização da falta, a ser corrigido pelo Crea na forma da lei.
                        Observação: o “conforme estabelecido pelo Regional” deve ser utilizado somente nos casos em que o valor da multa do Crea divergir do valor correto da resolução.
                        OU
                        NO CASO DE REDUÇÃO DA MULTA, EM FUNÇÃO DO CONTIDO NO ART. 43 DA RESOLUÇÃO Nº 1.008, DE 2004
                        2.2 - manter a aplicação de multa e reduzir o seu valor para R$ (valor por extenso), em função da regularização da falta, a ser corrigido pelo Crea na forma da lei.""")
                        cores()
            elif ('64' in artigo_ai):

                            self.texto_padrao = ctk.CTkTextbox(self.root, text_color='black', fg_color='white', font=('Lato Regular', 18))
                            self.texto_padrao.tag_config("red", foreground="red")
                            self.texto_padrao.insert(tk.INSERT,
                                              """art 64
                                              Trata-se de recurso interposto ao Confea contra a decisão do Plenário do Crea-""" + str(
                                                  crea_entry) + """ pela pessoa """ + str(
                                                  autuado_ai) + """, CNPJ nº ***""" + str(
                                                  cnpj_cpf_ai) + """***, autuada mediante o Auto de Infração n° """ + str(
                                                  nauto_ai) + """, lavrado em """ + str(data_ai) + """, por infração """ + str(artigo_ai) + """, ao encontrar-se """ + str(
                                                  motivo_ai) + """. (fls.""" + str(folhas_ai) + """  e """ + str(
                                                  folhas_recurso) + """)
                                A Câmara Especializada de """ + str(
                                                  especialidade_ce) + """ analisou os autos e concluiu pela manutenção da autuação, expedindo a Decisão nº """ + str(
                                                  ndecisao_ce) + """, de """ + str(data_ce) + """ (fl. """ + str(
                                                  folhas_ce) + """)
                                O recurso do(a) interessado(a) ao Plenário do Crea foi julgado mediante a Decisão nº """ + str(
                                                  ndecisao_pl) + """, de """ + str(
                                                  data_pl) + """, que decidiu manter a autuação. (fl. """ + str(
                                                  folhas_pl) + """)
                                O(A) interessado(a) teve ciência da decisão do Plenário do Regional em """ + str(
                                                  data_aviso) + """ e protocolizou, em """ + str(
                                                  data_recurso) + """, no Crea-""" + str(
                                                  crea_entry) + """, recurso ao Confea. (fls. """ + str(
                                                  folhas_aviso) + """ e """ + str(folhas_recurso) + """)
                                Embora não conste do processo a informação da data em que o interessado(a) teve ciência da Decisão do Plenário do Regional, em """ + str(
                                                  data_recurso) + """, foi protocolizado pelo interessado(a)""" + str(
                                                  nome_procuracao) + """ no Crea-""" + str(
                                                  crea_entry) + """ recurso ao Confea. (fls. """ + str(folhas_recurso) + """)
                                As folhas citadas neste parecer são relativas ao número da página eletrônica no SEI - XXXXX.
            1.Análise
            
            
                    A PROCURAÇÃO ESTA NA PAGINA """+ str(folhas_procuracao)+"""
                    Considerando que o comprovante do Cadastro Nacional da Pessoa Jurídica – CNPJ, emitido em """ + str(data_cnpj) + """, apresenta como atividade econômica principal da interessada o “"""+ str(cnae_primeiro)+"""” e como atividades econômicas secundárias o, entre outras, “"""+ str(cnae_segundo)+"""”; (fls. """+ str(folhas_cnpj)+""")
                    REINCIDÊNCIA ESTA CITADA NA PAGINA """+ str(folhas_reincidencia)+"""
                    A ART ESTA NA PAGINA """+ str(folhas_art)+"""










            
                                Considerando que a alínea “e” do art. 27 da Lei nº 5.194, de 1966, estabelece que compete ao Confea julgar em última instância os recursos sobre registros, decisões e penalidades impostas pelos Conselhos Regionais;
                                Considerando que a alínea “a” do art. 6º da Lei nº 5.194, de 1966, prevê que exerce ilegalmente a profissão de engenheiro ou engenheiro - agrônomo a pessoa física ou jurídica que realizar atos ou prestar serviços, públicos ou privados, reservados aos profissionais de que trata a lei e que não possua registro nos Conselhos Regionais;
                                Considerando que o inciso II do art. 1º da Decisão Normativa nº 74, de 27 de agosto de 2004, esclarece que pessoas físicas leigas executando atividades privativas de profissionais fiscalizados pelo Sistema Confea / Crea estarão infringindo a alínea “a” do art. 6º da Lei nº 5.194, de 1966;
                                Considerando que o(a) interessado(a), em seu recurso ao Plenário do Confea, alegou que sintetizar alegações, se necessário fazer mais considerandos;
                                Considerando que não procedem as alegações constantes do recurso apresentado, visto que contra - argumentar o recurso;
                                Considerando que, não obstante as alegações apresentadas, o(a) interessado(a) motivou a lavratura do auto de infração, uma vez que fundamentar;
                                Considerando que a infração está capitulada na alínea “a” do art. 6º da Lei n° 5.194, de 1966, cuja penalidade está prevista no art. 71, alínea “c” – multa, combinado com o art. 73, alínea “d”, dessa lei;e
                                UTILIZAR CONFORME O CASO
                                Auto lavrado no ano de 2010:
                                Considerando que a multa, à época da autuação, encontrava-se regulamentada pela Resolução nº 513, de 21 de agosto de 2009, art. 4º, alínea “d”, no valor compreendido entre R$ 238,00 (duzentos e trinta e oito reais) e R$ 801,50 (oitocentos e um reais e cinquenta centavos),
                                Auto lavrado no ano de 2011:
                                Considerando que a multa, à época da autuação, encontrava-se regulamentada pela Resolução nº 518, de 24 de setembro de 2010, art. 5º, alínea “d”, no valor compreendido entre R$ 509,50 (quinhentos e nove reais e cinquenta centavos) e R$ 844,00 (oitocentos e quarenta e quatro reais),
                                Auto lavrado no ano de 2012:
                                Considerando que a multa, à época da autuação, encontrava-se regulamentada pela Resolução nº 524, de 3 de outubro de 2011, art. 4º, alínea “d”, no valor compreendido entre R$ 752,00 (setecentos e cinquenta e dois reais) e R$ 1.504,50 (mil, quinhentos e quatro reais e cinquenta centavos),
                                Auto lavrado no ano de 2013:
                                Considerando que a multa, à época da autuação, encontrava-se regulamentada pela Resolução nº 1.043, de 28 de setembro de 2012, art. 1º, alínea “d”, no valor compreendido entre R$ 792,53 (setecentos e noventa e dois reais e cinquenta e três centavos) e R$ 1.585,59 (mil, quinhentos e oitenta e cinco reais e cinquenta e nove centavos),
                                Auto lavrado no ano de 2014:
                                Considerando que a multa, à época da autuação, encontrava-se regulamentada pela Resolução nº 1.049, de 27 de setembro de 2013, art. 1º, alínea “d”, no valor compreendido entre R$ 840,64 (oitocentos e quarenta reais e sessenta e quatro centavos) e R$ 1.681,84 (mil, seiscentos e oitenta e um reais e oitenta e quatro centavos),
                                Auto lavrado no ano de 2015:
                                Considerando que a multa, à época da autuação, encontrava-se regulamentada pela Resolução nº 1.058, de 26 de setembro de 2014, art. 1º, alínea “d”, no valor compreendido entre R$ 894,36 (oitocentos e noventa e quatro reais e trinta e seis centavos) e R$ 1.788,72 (mil, setecentos e oitenta e oito reais e setenta e dois centavos),
                                Auto lavrado no ano de 2016:
                                Considerando que a multa, à época da autuação, encontrava-se regulamentada pela Resolução nº 1.066, de 25 de setembro de 2015, art. 18, com valores atualizados pela Decisão nº PL-2041/2015, de 25 de setembro de 2015, no valor compreendido entre R$ 982,72 (novecentos e oitenta e dois reais e setenta e dois centavos) e R$ 1.965,45 (mil, novecentos e sessenta e cinco reais e quarenta e cinco centavos),
                                Auto lavrado no ano de 2017:
                                Considerando que a multa, à época da autuação, encontrava-se regulamentada pela Resolução nº 1.066, de 25 de setembro de 2015, art. 18, com valores atualizados pela Decisão nº PL-1056/2016, de 22 de setembro de 2016, no valor compreendido entre R$ 1.077,30 (mil e setenta e sete reais e trinta centavos) e R$ 2.154,60 (dois mil, cento e cinquenta e quatro reais e sessenta centavos),
                                Auto lavrado no ano de 2018:
                                Considerando que a multa, à época da autuação, encontrava-se regulamentada pela Resolução nº 1.066, de 25 de setembro de 2015, art. 18, com valores atualizados pela Decisão nº PL-1758/2017, de 28 de setembro de 2017, no valor compreendido entre R$ 1.095,96 (mil e noventa e cinco reais e noventa e seis centavos) e R$ 2.191,91 (dois mil, cento e noventa e um reais e noventa e um centavos),
                                Auto lavrado no ano de 2019:
                                Considerando que a multa, à época da autuação, encontrava-se regulamentada pela Resolução nº 1.066, de 25 de setembro de 2015, art. 18, com valores atualizados pela Decisão nº PL-1611/2018, de 28 de setembro de 2018, no valor compreendido entre R$ 1.135,87 (mil cento e trinta e cinco reais e oitenta e sete centavos) e R$ 2.271,73 (dois mil duzentos e setenta e um reais e setenta e três centavos);
                                Auto lavrado no ano de 2020:
                                Considerando que a multa, à época da autuação, encontrava-se regulamentada pela Resolução nº 1.066, de 25 de setembro de 2015, art. 18, com valores atualizados pela Decisão nº PL-1544/2019, de 26 de setembro de 2019, no valor de R$ 1.173,17 (mil cento e setenta e três reais e dezessete centavos) a R$ 2.346,33 (dois mil trezentos e quarenta e seis reais e trinta e três centavos);
                                Auto lavrado no ano de 2021: 
                                Considerando que a multa, à época da autuação, encontrava-se regulamentada pela Resolução nº 1.066, de 25 de setembro de 2015, art. 18, com valores atualizados pela Decisão nº PL-1642/2020, de 29 de setembro de 2020, no valor de R$ 1.173,17 (mil cento e setenta e três reais e dezessete centavos) a R$ 2.346,33 (dois mil trezentos e quarenta e seis reais e trinta e três centavos), 
                                Auto lavrado no ano de 2022:
                                Considerando que a multa, à época da autuação, encontrava-se regulamentada pela Resolução nº 1.066, de 25 de setembro de 2015, art. 18, com valores atualizados pela Decisão nº PL-1513/2021, de 24 de setembro de 2021, no valor de R$ 1.173,17 (mil cento e setenta e três reais e dezessete centavos) a R$ 2.346,33 (dois mil trezentos e quarenta e seis reais e trinta e três centavos), 
                                Auto lavrado no ano de 2023: 
                                Considerando que a multa, à época da autuação, encontrava-se regulamentada pela Resolução nº 1.066, de 25 de setembro de 2015, art. 18, com valores atualizados pela Decisão nº PL-1457/2022, de 30 de setembro de 2022, no valor de R$ 1.276,71 (um mil duzentos e setenta e seis reais e setenta e um centavos)  a R$ 2.553,41 (dois mil quinhentos e cinquenta e três reais e quarenta e um centavos), 
                                OU
                                NO CASO DE O CREA TER FIXADO MULTA EM VALOR FORA DAS FAIXAS DA RESOLUÇÃO
                                Considerando que apesar de o Regional ter estabelecido a multa no valor de R$ (valor por extenso), a multa, à época da autuação, encontrava-se regulamentada pela Resolução nº colocar a resolução aplicável dos parágrafos acima,
                                ACRESCENTAR, SE NECESSÁRIO:
                                HAVENDO A REGULARIZAÇÃO DO FATO QUE ENSEJOU A AUTUAÇÃO, APÓS A LAVRATURA DO A.I.
                                Considerando que o § 2° do art. 11 da Resolução n° 1.008, de 9 de dezembro de 2004, estabelece que lavrado o auto de infração, a regularização da situação não exime o(a) autuado(a) das cominações legais;
                                Considerando que o § 3º do art. 43 dessa resolução dispõe que é facultada a redução de multas pelas instâncias julgadoras do Crea e do Confea nos casos previstos nesse artigo, respeitadas as faixas de valores estabelecidas em resolução específica;
                                Considerando que o(a) interessado(a) somente providenciou a regularização após a lavratura do auto de infração, mediante a contratação do(a) profissional Título abreviado conforme Res. nº 473/2002 Nome do profissional OU o registro da ART nº NÚMERO, em data, o que motiva a aplicação da multa em seu valor mínimo, tal como dispõe o inciso V do art. 43 da Resolução nº 1.008, de 2004; e (fl. ART ou contrato)
                                SE FOR PRIMÁRIO
                                Considerando que não foi comprovada nos autos a prática, pelo(a) interessado(a), de irregularidade anterior, capitulada no mesmo dispositivo legal e transitada em julgado,
                                E/OU
                                NO CASO DE REINCIDÊNCIA OU NOVA REINCIDÊNCIA
                                Considerando que o(a) interessado(a) incorreu em reincidência OU nova reincidência, comprovada nos autos mediante apontar documento que comprova, o que motiva a aplicação do valor da multa em dobro, conforme dispõem os §§ 1° e 2º do art. 43 da Resolução n° 1.008, de 9 de dezembro de 2004,
                                E/OU
                                QUANDO A SITUAÇÃO PERMITE A APLICAÇÃO DO ART. 43 DA RESOLUÇÃO Nº 1.008, DE 2004
                                Considerando que se trata de autuado(a) primário(a), conforme informações constantes do processo, não tendo sido imputada pena anterior pelo Crea ao(à) interessado(a), por esta ou outra infração à legislação do Sistema Confea/Crea e transitada em julgado;
                                E/OU
                                Considerando que a infração não pode ser considerada de caráter grave, justificada pela pouca repercussão, tendo ficado restrita à sua atuação ilegal, perante a legislação em comento;
                                E/OU
                                Considerando que a falta cometida não trouxe prejuízos diretamente a terceiros, bem como consequências de outra natureza que possa ser considerada insanável, podendo ser facilmente reparada e corrigida a linha de condução;
                                Considerando que os três critérios atenuantes acima estão previstos nos Incisos I, III e IV do art. 43 da Resolução nº 1.008, de 9 de dezembro de 2004; (Obs.: utilizar apenas os incisos aplicáveis ao caso)
                                Considerando a necessidade de cumprimento pelo Sistema Confea/Crea da finalidade de interesse público a que se destina;
                                Considerando que o(a) autuado(a) se enquadra nas questões acima, motivos pelos quais a multa deveria ter sido fixada pelo Crea em valor proporcional e razoável, comparativamente à falta cometida;
            2. Conclusão
                                Sugerimos à Comissão de Ética e Exercício Profissional – CEEP propor ao Plenário do Confea:
                                2.1. conhecer o recurso interposto pelo(a) interessado(a) para, no mérito, negar-lhe provimento; e
                                NO CASO DE MANUTENÇÃO DO VALOR DA MULTA ESTABELECIDA PELO CREA
                                2.2. manter a aplicação de multa no valor de R$ (valor por extenso), conforme estabelecido pelo Regional, sem prejuízo da regularização da falta, a ser corrigido pelo Crea na forma da lei.
                                OU
                                EM CASOS GERAIS DE REINCIDÊNCIA
                                manter a aplicação de multa no valor de R$ (valor por extenso), já dobrado em função da comprovada reincidência, sem prejuízo da regularização da falta, a ser corrigido pelo Crea na forma da lei. (valor máximo ou qualquer valor estabelecido conforme faixa)
                                NO CASO DE REINCIDÊNCIA, REGULARIZAÇÃO E REDUÇÃO DO VALOR DA MULTA PELO CONFEA
                                2.2. manter a aplicação de multa no valor de R$ (valor por extenso), reduzido em função da regularização da falta e já dobrado devido a comprovada reincidência, a ser corrigido pelo Crea na forma da lei. (valor mínimo em função da regularização).
                                OU
                                NO CASO DE REDUÇÃO DA MULTA, EM FUNÇÃO DO CONTIDO NO ART. 43 DA RESOLUÇÃO Nº 1.008, DE 2004
                                2.2 - manter a aplicação de multa e reduzir o seu valor para R$ (valor por extenso), em função dos princípios de proporcionalidade e razoabilidade, relativamente à infração cometida, sem prejuízo da regularização da falta, a ser corrigido pelo Crea na forma da lei.
                                Observação: o “conforme estabelecido pelo Regional” deve ser utilizado somente nos casos em que o valor da multa do Crea divergir do valor correto da resolução.""")
                            cores()
            elif ('art. 1' in artigo_ai or 'Art. 1' in artigo_ai or 'art 1'in artigo_ai or 'artigo 1º' in artigo_ai):
                print("é 111")
                self.texto_padrao = ctk.CTkTextbox(self.root, text_color='black', fg_color='white',
                                                   font=('Lato Regular', 18))
                self.texto_padrao.tag_config("red", foreground="red")
                self.texto_padrao.insert(tk.INSERT,
                                         """art 64
                                         Trata-se de recurso interposto ao Confea contra a decisão do Plenário do Crea-""" + str(
                                             crea_entry) + """ pela pessoa """ + str(
                                             autuado_ai) + """, CNPJ nº ***""" + str(
                                             cnpj_cpf_ai) + """***, autuada mediante o Auto de Infração n° """ + str(
                                             nauto_ai) + """, lavrado em """ + str(
                                             data_ai) + """, por infração """ + str(
                                             artigo_ai) + """, ao encontrar-se """ + str(
                                             motivo_ai) + """. (fls.""" + str(folhas_ai) + """  e """ + str(
                                             folhas_recurso) + """)
                                                A Câmara Especializada de """ + str(
                                             especialidade_ce) + """ analisou os autos e concluiu pela manutenção da autuação, expedindo a Decisão nº """ + str(
                                             ndecisao_ce) + """, de """ + str(data_ce) + """ (fl. """ + str(
                                             folhas_ce) + """)
                                                O recurso do(a) interessado(a) ao Plenário do Crea foi julgado mediante a Decisão nº """ + str(
                                             ndecisao_pl) + """, de """ + str(
                                             data_pl) + """, que decidiu manter a autuação. (fl. """ + str(
                                             folhas_pl) + """)
                                                O(A) interessado(a) teve ciência da decisão do Plenário do Regional em """ + str(
                                             data_aviso) + """ e protocolizou, em """ + str(
                                             data_recurso) + """, no Crea-""" + str(
                                             crea_entry) + """, recurso ao Confea. (fls. """ + str(
                                             folhas_aviso) + """ e """ + str(folhas_recurso) + """)
                                                Embora não conste do processo a informação da data em que o interessado(a) teve ciência da Decisão do Plenário do Regional, em """ + str(
                                             data_recurso) + """, foi protocolizado pelo interessado(a)""" + str(
                                             nome_procuracao) + """ no Crea-""" + str(
                                             crea_entry) + """ recurso ao Confea. (fls. """ + str(folhas_recurso) + """)
                                                As folhas citadas neste parecer são relativas ao número da página eletrônica no SEI - XXXXX.
                            1.Análise


                                    A PROCURAÇÃO ESTA NA PAGINA """ + str(folhas_procuracao) + """
                                    Considerando que o comprovante do Cadastro Nacional da Pessoa Jurídica – CNPJ, emitido em """ + str(
                                             data_cnpj) + """, apresenta como atividade econômica principal da interessada o “""" + str(
                                             cnae_primeiro) + """” e como atividades econômicas secundárias o, entre outras, “""" + str(
                                             cnae_segundo) + """”; (fls. """ + str(folhas_cnpj) + """)
                                    REINCIDÊNCIA ESTA CITADA NA PAGINA """ + str(folhas_reincidencia) + """
                                    A ART ESTA NA PAGINA """ + str(folhas_art) + """











                                                Considerando que a alínea “e” do art. 27 da Lei nº 5.194, de 1966, estabelece que compete ao Confea julgar em última instância os recursos sobre registros, decisões e penalidades impostas pelos Conselhos Regionais;
                                                Considerando que a alínea “a” do art. 6º da Lei nº 5.194, de 1966, prevê que exerce ilegalmente a profissão de engenheiro ou engenheiro - agrônomo a pessoa física ou jurídica que realizar atos ou prestar serviços, públicos ou privados, reservados aos profissionais de que trata a lei e que não possua registro nos Conselhos Regionais;
                                                Considerando que o inciso II do art. 1º da Decisão Normativa nº 74, de 27 de agosto de 2004, esclarece que pessoas físicas leigas executando atividades privativas de profissionais fiscalizados pelo Sistema Confea / Crea estarão infringindo a alínea “a” do art. 6º da Lei nº 5.194, de 1966;
                                                Considerando que o(a) interessado(a), em seu recurso ao Plenário do Confea, alegou que sintetizar alegações, se necessário fazer mais considerandos;
                                                Considerando que não procedem as alegações constantes do recurso apresentado, visto que contra - argumentar o recurso;
                                                Considerando que, não obstante as alegações apresentadas, o(a) interessado(a) motivou a lavratura do auto de infração, uma vez que fundamentar;
                                                Considerando que a infração está capitulada na alínea “a” do art. 6º da Lei n° 5.194, de 1966, cuja penalidade está prevista no art. 71, alínea “c” – multa, combinado com o art. 73, alínea “d”, dessa lei;e
                                                UTILIZAR CONFORME O CASO
                                                Auto lavrado no ano de 2010:
                                                Considerando que a multa, à época da autuação, encontrava-se regulamentada pela Resolução nº 513, de 21 de agosto de 2009, art. 4º, alínea “d”, no valor compreendido entre R$ 238,00 (duzentos e trinta e oito reais) e R$ 801,50 (oitocentos e um reais e cinquenta centavos),
                                                Auto lavrado no ano de 2011:
                                                Considerando que a multa, à época da autuação, encontrava-se regulamentada pela Resolução nº 518, de 24 de setembro de 2010, art. 5º, alínea “d”, no valor compreendido entre R$ 509,50 (quinhentos e nove reais e cinquenta centavos) e R$ 844,00 (oitocentos e quarenta e quatro reais),
                                                Auto lavrado no ano de 2012:
                                                Considerando que a multa, à época da autuação, encontrava-se regulamentada pela Resolução nº 524, de 3 de outubro de 2011, art. 4º, alínea “d”, no valor compreendido entre R$ 752,00 (setecentos e cinquenta e dois reais) e R$ 1.504,50 (mil, quinhentos e quatro reais e cinquenta centavos),
                                                Auto lavrado no ano de 2013:
                                                Considerando que a multa, à época da autuação, encontrava-se regulamentada pela Resolução nº 1.043, de 28 de setembro de 2012, art. 1º, alínea “d”, no valor compreendido entre R$ 792,53 (setecentos e noventa e dois reais e cinquenta e três centavos) e R$ 1.585,59 (mil, quinhentos e oitenta e cinco reais e cinquenta e nove centavos),
                                                Auto lavrado no ano de 2014:
                                                Considerando que a multa, à época da autuação, encontrava-se regulamentada pela Resolução nº 1.049, de 27 de setembro de 2013, art. 1º, alínea “d”, no valor compreendido entre R$ 840,64 (oitocentos e quarenta reais e sessenta e quatro centavos) e R$ 1.681,84 (mil, seiscentos e oitenta e um reais e oitenta e quatro centavos),
                                                Auto lavrado no ano de 2015:
                                                Considerando que a multa, à época da autuação, encontrava-se regulamentada pela Resolução nº 1.058, de 26 de setembro de 2014, art. 1º, alínea “d”, no valor compreendido entre R$ 894,36 (oitocentos e noventa e quatro reais e trinta e seis centavos) e R$ 1.788,72 (mil, setecentos e oitenta e oito reais e setenta e dois centavos),
                                                Auto lavrado no ano de 2016:
                                                Considerando que a multa, à época da autuação, encontrava-se regulamentada pela Resolução nº 1.066, de 25 de setembro de 2015, art. 18, com valores atualizados pela Decisão nº PL-2041/2015, de 25 de setembro de 2015, no valor compreendido entre R$ 982,72 (novecentos e oitenta e dois reais e setenta e dois centavos) e R$ 1.965,45 (mil, novecentos e sessenta e cinco reais e quarenta e cinco centavos),
                                                Auto lavrado no ano de 2017:
                                                Considerando que a multa, à época da autuação, encontrava-se regulamentada pela Resolução nº 1.066, de 25 de setembro de 2015, art. 18, com valores atualizados pela Decisão nº PL-1056/2016, de 22 de setembro de 2016, no valor compreendido entre R$ 1.077,30 (mil e setenta e sete reais e trinta centavos) e R$ 2.154,60 (dois mil, cento e cinquenta e quatro reais e sessenta centavos),
                                                Auto lavrado no ano de 2018:
                                                Considerando que a multa, à época da autuação, encontrava-se regulamentada pela Resolução nº 1.066, de 25 de setembro de 2015, art. 18, com valores atualizados pela Decisão nº PL-1758/2017, de 28 de setembro de 2017, no valor compreendido entre R$ 1.095,96 (mil e noventa e cinco reais e noventa e seis centavos) e R$ 2.191,91 (dois mil, cento e noventa e um reais e noventa e um centavos),
                                                Auto lavrado no ano de 2019:
                                                Considerando que a multa, à época da autuação, encontrava-se regulamentada pela Resolução nº 1.066, de 25 de setembro de 2015, art. 18, com valores atualizados pela Decisão nº PL-1611/2018, de 28 de setembro de 2018, no valor compreendido entre R$ 1.135,87 (mil cento e trinta e cinco reais e oitenta e sete centavos) e R$ 2.271,73 (dois mil duzentos e setenta e um reais e setenta e três centavos);
                                                Auto lavrado no ano de 2020:
                                                Considerando que a multa, à época da autuação, encontrava-se regulamentada pela Resolução nº 1.066, de 25 de setembro de 2015, art. 18, com valores atualizados pela Decisão nº PL-1544/2019, de 26 de setembro de 2019, no valor de R$ 1.173,17 (mil cento e setenta e três reais e dezessete centavos) a R$ 2.346,33 (dois mil trezentos e quarenta e seis reais e trinta e três centavos);
                                                Auto lavrado no ano de 2021: 
                                                Considerando que a multa, à época da autuação, encontrava-se regulamentada pela Resolução nº 1.066, de 25 de setembro de 2015, art. 18, com valores atualizados pela Decisão nº PL-1642/2020, de 29 de setembro de 2020, no valor de R$ 1.173,17 (mil cento e setenta e três reais e dezessete centavos) a R$ 2.346,33 (dois mil trezentos e quarenta e seis reais e trinta e três centavos), 
                                                Auto lavrado no ano de 2022:
                                                Considerando que a multa, à época da autuação, encontrava-se regulamentada pela Resolução nº 1.066, de 25 de setembro de 2015, art. 18, com valores atualizados pela Decisão nº PL-1513/2021, de 24 de setembro de 2021, no valor de R$ 1.173,17 (mil cento e setenta e três reais e dezessete centavos) a R$ 2.346,33 (dois mil trezentos e quarenta e seis reais e trinta e três centavos), 
                                                Auto lavrado no ano de 2023: 
                                                Considerando que a multa, à época da autuação, encontrava-se regulamentada pela Resolução nº 1.066, de 25 de setembro de 2015, art. 18, com valores atualizados pela Decisão nº PL-1457/2022, de 30 de setembro de 2022, no valor de R$ 1.276,71 (um mil duzentos e setenta e seis reais e setenta e um centavos)  a R$ 2.553,41 (dois mil quinhentos e cinquenta e três reais e quarenta e um centavos), 
                                                OU
                                                NO CASO DE O CREA TER FIXADO MULTA EM VALOR FORA DAS FAIXAS DA RESOLUÇÃO
                                                Considerando que apesar de o Regional ter estabelecido a multa no valor de R$ (valor por extenso), a multa, à época da autuação, encontrava-se regulamentada pela Resolução nº colocar a resolução aplicável dos parágrafos acima,
                                                ACRESCENTAR, SE NECESSÁRIO:
                                                HAVENDO A REGULARIZAÇÃO DO FATO QUE ENSEJOU A AUTUAÇÃO, APÓS A LAVRATURA DO A.I.
                                                Considerando que o § 2° do art. 11 da Resolução n° 1.008, de 9 de dezembro de 2004, estabelece que lavrado o auto de infração, a regularização da situação não exime o(a) autuado(a) das cominações legais;
                                                Considerando que o § 3º do art. 43 dessa resolução dispõe que é facultada a redução de multas pelas instâncias julgadoras do Crea e do Confea nos casos previstos nesse artigo, respeitadas as faixas de valores estabelecidas em resolução específica;
                                                Considerando que o(a) interessado(a) somente providenciou a regularização após a lavratura do auto de infração, mediante a contratação do(a) profissional Título abreviado conforme Res. nº 473/2002 Nome do profissional OU o registro da ART nº NÚMERO, em data, o que motiva a aplicação da multa em seu valor mínimo, tal como dispõe o inciso V do art. 43 da Resolução nº 1.008, de 2004; e (fl. ART ou contrato)
                                                SE FOR PRIMÁRIO
                                                Considerando que não foi comprovada nos autos a prática, pelo(a) interessado(a), de irregularidade anterior, capitulada no mesmo dispositivo legal e transitada em julgado,
                                                E/OU
                                                NO CASO DE REINCIDÊNCIA OU NOVA REINCIDÊNCIA
                                                Considerando que o(a) interessado(a) incorreu em reincidência OU nova reincidência, comprovada nos autos mediante apontar documento que comprova, o que motiva a aplicação do valor da multa em dobro, conforme dispõem os §§ 1° e 2º do art. 43 da Resolução n° 1.008, de 9 de dezembro de 2004,
                                                E/OU
                                                QUANDO A SITUAÇÃO PERMITE A APLICAÇÃO DO ART. 43 DA RESOLUÇÃO Nº 1.008, DE 2004
                                                Considerando que se trata de autuado(a) primário(a), conforme informações constantes do processo, não tendo sido imputada pena anterior pelo Crea ao(à) interessado(a), por esta ou outra infração à legislação do Sistema Confea/Crea e transitada em julgado;
                                                E/OU
                                                Considerando que a infração não pode ser considerada de caráter grave, justificada pela pouca repercussão, tendo ficado restrita à sua atuação ilegal, perante a legislação em comento;
                                                E/OU
                                                Considerando que a falta cometida não trouxe prejuízos diretamente a terceiros, bem como consequências de outra natureza que possa ser considerada insanável, podendo ser facilmente reparada e corrigida a linha de condução;
                                                Considerando que os três critérios atenuantes acima estão previstos nos Incisos I, III e IV do art. 43 da Resolução nº 1.008, de 9 de dezembro de 2004; (Obs.: utilizar apenas os incisos aplicáveis ao caso)
                                                Considerando a necessidade de cumprimento pelo Sistema Confea/Crea da finalidade de interesse público a que se destina;
                                                Considerando que o(a) autuado(a) se enquadra nas questões acima, motivos pelos quais a multa deveria ter sido fixada pelo Crea em valor proporcional e razoável, comparativamente à falta cometida;
                            2. Conclusão
                                                Sugerimos à Comissão de Ética e Exercício Profissional – CEEP propor ao Plenário do Confea:
                                                2.1. conhecer o recurso interposto pelo(a) interessado(a) para, no mérito, negar-lhe provimento; e
                                                NO CASO DE MANUTENÇÃO DO VALOR DA MULTA ESTABELECIDA PELO CREA
                                                2.2. manter a aplicação de multa no valor de R$ (valor por extenso), conforme estabelecido pelo Regional, sem prejuízo da regularização da falta, a ser corrigido pelo Crea na forma da lei.
                                                OU
                                                EM CASOS GERAIS DE REINCIDÊNCIA
                                                manter a aplicação de multa no valor de R$ (valor por extenso), já dobrado em função da comprovada reincidência, sem prejuízo da regularização da falta, a ser corrigido pelo Crea na forma da lei. (valor máximo ou qualquer valor estabelecido conforme faixa)
                                                NO CASO DE REINCIDÊNCIA, REGULARIZAÇÃO E REDUÇÃO DO VALOR DA MULTA PELO CONFEA
                                                2.2. manter a aplicação de multa no valor de R$ (valor por extenso), reduzido em função da regularização da falta e já dobrado devido a comprovada reincidência, a ser corrigido pelo Crea na forma da lei. (valor mínimo em função da regularização).
                                                OU
                                                NO CASO DE REDUÇÃO DA MULTA, EM FUNÇÃO DO CONTIDO NO ART. 43 DA RESOLUÇÃO Nº 1.008, DE 2004
                                                2.2 - manter a aplicação de multa e reduzir o seu valor para R$ (valor por extenso), em função dos princípios de proporcionalidade e razoabilidade, relativamente à infração cometida, sem prejuízo da regularização da falta, a ser corrigido pelo Crea na forma da lei.
                                                Observação: o “conforme estabelecido pelo Regional” deve ser utilizado somente nos casos em que o valor da multa do Crea divergir do valor correto da resolução.""")
                cores()
        def cores():
            start_index = "1.0"
            while True:
                start_index = self.texto_padrao.search(str(crea_entry), start_index, stopindex="end", regexp=False)
                if not start_index:
                    break
                end_index = self.texto_padrao.index(f"{start_index}+{len(str(crea_entry))}c")
                self.texto_padrao.tag_add("red", start_index, end_index)
                start_index = end_index

            start_index = "1.0"
            while True:
                start_index = self.texto_padrao.search(str(autuado_ai), start_index, stopindex="end", regexp=False)
                if not start_index:
                    break
                end_index = self.texto_padrao.index(f"{start_index}+{len(str(autuado_ai))}c")
                self.texto_padrao.tag_add("red", start_index, end_index)
                start_index = end_index
            start_index = "1.0"
            while True:
                start_index = self.texto_padrao.search(str(cnpj_cpf_ai), start_index, stopindex="end", regexp=False)
                if not start_index:
                    break
                end_index = self.texto_padrao.index(f"{start_index}+{len(str(cnpj_cpf_ai))}c")
                self.texto_padrao.tag_add("red", start_index, end_index)
                start_index = end_index
            start_index = "1.0"
            while True:
                start_index = self.texto_padrao.search(str(nauto_ai), start_index, stopindex="end", regexp=False)
                if not start_index:
                    break
                end_index = self.texto_padrao.index(f"{start_index}+{len(str(nauto_ai))}c")
                self.texto_padrao.tag_add("red", start_index, end_index)
                start_index = end_index
            start_index = "1.0"
            while True:
                start_index = self.texto_padrao.search(str(data_ai), start_index, stopindex="end", regexp=False)
                if not start_index:
                    break
                end_index = self.texto_padrao.index(f"{start_index}+{len(str(data_ai))}c")
                self.texto_padrao.tag_add("red", start_index, end_index)
                start_index = end_index
            start_index = "1.0"
            while True:
                start_index = self.texto_padrao.search(str(artigo_ai), start_index, stopindex="end", regexp=False)
                if not start_index:
                    break
                end_index = self.texto_padrao.index(f"{start_index}+{len(str(artigo_ai))}c")
                self.texto_padrao.tag_add("red", start_index, end_index)
                start_index = end_index
            start_index = "1.0"
            while True:
                start_index = self.texto_padrao.search(str(motivo_ai), start_index, stopindex="end", regexp=False)
                if not start_index:
                    break
                end_index = self.texto_padrao.index(f"{start_index}+{len(str(motivo_ai))}c")
                self.texto_padrao.tag_add("red", start_index, end_index)
                start_index = end_index
            start_index = "1.0"
            while True:
                start_index = self.texto_padrao.search(str(folhas_ai), start_index, stopindex="end", regexp=False)
                if not start_index:
                    break
                end_index = self.texto_padrao.index(f"{start_index}+{len(str(folhas_ai))}c")
                self.texto_padrao.tag_add("red", start_index, end_index)
                start_index = end_index
            start_index = "1.0"
            while True:
                start_index = self.texto_padrao.search(str(folhas_recurso), start_index, stopindex="end", regexp=False)
                if not start_index:
                    break
                end_index = self.texto_padrao.index(f"{start_index}+{len(str(folhas_recurso))}c")
                self.texto_padrao.tag_add("red", start_index, end_index)
                start_index = end_index
            start_index = "1.0"
            while True:
                start_index = self.texto_padrao.search(str(folhas_ce), start_index, stopindex="end", regexp=False)
                if not start_index:
                    break
                end_index = self.texto_padrao.index(f"{start_index}+{len(str(folhas_ce))}c")
                self.texto_padrao.tag_add("red", start_index, end_index)
                start_index = end_index
            start_index = "1.0"
            while True:
                start_index = self.texto_padrao.search(str(folhas_pl), start_index, stopindex="end", regexp=False)
                if not start_index:
                    break
                end_index = self.texto_padrao.index(f"{start_index}+{len(str(folhas_pl))}c")
                self.texto_padrao.tag_add("red", start_index, end_index)
                start_index = end_index
            start_index = "1.0"
            while True:
                start_index = self.texto_padrao.search(str(especialidade_ce), start_index, stopindex="end", regexp=False)
                if not start_index:
                    break
                end_index = self.texto_padrao.index(f"{start_index}+{len(str(especialidade_ce))}c")
                self.texto_padrao.tag_add("red", start_index, end_index)
                start_index = end_index
            start_index = "1.0"
            while True:
                start_index = self.texto_padrao.search(str(data_ce), start_index, stopindex="end", regexp=False)
                if not start_index:
                    break
                end_index = self.texto_padrao.index(f"{start_index}+{len(str(data_ce))}c")
                self.texto_padrao.tag_add("red", start_index, end_index)
                start_index = end_index
            start_index = "1.0"
            while True:
                start_index = self.texto_padrao.search(str(ndecisao_pl), start_index, stopindex="end", regexp=False)
                if not start_index:
                    break
                end_index = self.texto_padrao.index(f"{start_index}+{len(str(ndecisao_pl))}c")
                self.texto_padrao.tag_add("red", start_index, end_index)
                start_index = end_index
            start_index = "1.0"
            while True:
                start_index = self.texto_padrao.search(str(data_pl), start_index, stopindex="end", regexp=False)
                if not start_index:
                    break
                end_index = self.texto_padrao.index(f"{start_index}+{len(str(data_pl))}c")
                self.texto_padrao.tag_add("red", start_index, end_index)
                start_index = end_index
            start_index = "1.0"
            while True:
                start_index = self.texto_padrao.search(str(folhas_aviso), start_index, stopindex="end", regexp=False)
                if not start_index:
                    break
                end_index = self.texto_padrao.index(f"{start_index}+{len(str(folhas_aviso))}c")
                self.texto_padrao.tag_add("red", start_index, end_index)
                start_index = end_index
            start_index = "1.0"
            while True:
                start_index = self.texto_padrao.search(str(data_aviso), start_index, stopindex="end", regexp=False)
                if not start_index:
                    break
                end_index = self.texto_padrao.index(f"{start_index}+{len(str(data_aviso))}c")
                self.texto_padrao.tag_add("red", start_index, end_index)
                start_index = end_index
            start_index = "1.0"
            while True:
                start_index = self.texto_padrao.search(str(data_recurso), start_index, stopindex="end", regexp=False)
                if not start_index:
                    break
                end_index = self.texto_padrao.index(f"{start_index}+{len(str(data_recurso))}c")
                self.texto_padrao.tag_add("red", start_index, end_index)
                start_index = end_index
            start_index = "1.0"
            while True:
                start_index = self.texto_padrao.search(str(ndecisao_ce), start_index, stopindex="end", regexp=False)
                if not start_index:
                    break
                end_index = self.texto_padrao.index(f"{start_index}+{len(str(ndecisao_ce))}c")
                self.texto_padrao.tag_add("red", start_index, end_index)
                start_index = end_index
            start_index = "1.0"
            while True:
                start_index = self.texto_padrao.search(str(data_cnpj), start_index, stopindex="end", regexp=False)
                if not start_index:
                    break
                end_index = self.texto_padrao.index(f"{start_index}+{len(str(data_cnpj))}c")
                self.texto_padrao.tag_add("red", start_index, end_index)
                start_index = end_index
            start_index = "1.0"
            while True:
                start_index = self.texto_padrao.search(str(cnae_primeiro), start_index, stopindex="end", regexp=False)
                if not start_index:
                    break
                end_index = self.texto_padrao.index(f"{start_index}+{len(str(cnae_primeiro))}c")
                self.texto_padrao.tag_add("red", start_index, end_index)
                start_index = end_index
            start_index = "1.0"
            while True:
                start_index = self.texto_padrao.search(str(cnae_segundo), start_index, stopindex="end", regexp=False)
                if not start_index:
                    break
                end_index = self.texto_padrao.index(f"{start_index}+{len(str(cnae_segundo))}c")
                self.texto_padrao.tag_add("red", start_index, end_index)
                start_index = end_index
            start_index = "1.0"
            while True:
                start_index = self.texto_padrao.search(str(folhas_cnpj), start_index, stopindex="end", regexp=False)
                if not start_index:
                    break
                end_index = self.texto_padrao.index(f"{start_index}+{len(str(folhas_cnpj))}c")
                self.texto_padrao.tag_add("red", start_index, end_index)
                start_index = end_index
            self.texto_padrao.place(relx=0.065, rely=0.26, relwidth=0.925, relheight=0.72)
            #self.conteudo()
            #self.botoes()
        """selecionar arquivos"""
        btn_selecionar = ctk.CTkButton(self.frame_3,fg_color='#094c8c',text="Selecionar arquivo", command=selecionar_arquivo)
        btn_selecionar.place(relx=0.65, rely=0.10, relwidth=0.15, relheight=0.75)
        """Botao Menu"""
        btn_menu = ctk.CTkButton(self.frame_2, text='Menu', fg_color='#094c8c', text_color='White',font=('Lato', 14), command=tela_menu)
        btn_menu.place(relx=0, rely=0, relwidth=1, relheight=0.08)
        """Botao Artigo 1"""
        btn_art1 = ctk.CTkButton(self.frame_2, text='Art 1º', fg_color='#094c8c', text_color='White',font=('Lato', 14))
        btn_art1.place(relx=0, rely=0.08, relwidth=1, relheight=0.08)
        """Botao Artigo 6 A"""
        btn_art6a = ctk.CTkButton(self.frame_2, text='Art 6º a', fg_color='#094c8c', text_color='White',font=('Lato', 14))
        btn_art6a.place(relx=0, rely=0.16, relwidth=1, relheight=0.08)
        """Botao Artigo 6 E"""
        btn_art6e = ctk.CTkButton(self.frame_2, text='Art 6º e', fg_color='#094c8c', text_color='White',font=('Lato', 14))
        btn_art6e.place(relx=0, rely=0.24, relwidth=1, relheight=0.08)
        """Botao Artigo 16"""
        btn_art16 = ctk.CTkButton(self.frame_2, text='Art 16º', fg_color='#094c8c', text_color='White',font=('Lato', 14))
        btn_art16.place(relx=0, rely=0.32, relwidth=1, relheight=0.08)
        """Botao Artigo 59"""
        btn_art59 = ctk.CTkButton(self.frame_2, text='Art 59º', fg_color='#094c8c', text_color='White',font=('Lato', 14))
        btn_art59.place(relx=0, rely=0.4, relwidth=1, relheight=0.08)
        """Botao Texto Padrao"""
        btn_textopadrao = ctk.CTkButton(self.frame_2, text='Texto', fg_color='#094c8c', text_color='White',font=('Lato', 14), command=tela_texto)
        btn_textopadrao.place(relx=0, rely=0.48, relwidth=1, relheight=0.08)
        """Botao Historico"""
        btn_textopadrao = ctk.CTkButton(self.frame_2, text='Historico', fg_color='#094c8c', text_color='White',font=('Lato', 14))#, command=tela_historico)
        btn_textopadrao.place(relx=0, rely=0.56, relwidth=1, relheight=0.08)


App()
root.mainloop()