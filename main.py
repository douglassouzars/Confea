
import os
from tkinter import *
import customtkinter as ctk
from tkinter import ttk
import tkinter as tk
from PIL import Image, ImageTk
#import tabula
import PyPDF2
import re
from tkinter.filedialog import askopenfilename
from PyPDF2 import PdfReader

root = Tk()
class App():
    def __init__(self):
        self.root = root
        self.tela()
        self.frames()
        self.logo()
        

        

    def tela(self):
        """Definição da tela e sua cor total"""
        self.root.title("Sistema Confea")
        self.root.configure(background='#e8e8e8')
        self.root.geometry("1060x600")
        self.root.resizable(False, False)
        self.root.minsize(850,600)


    
    def frames(self):
        """Header azul"""
        self.frame_1 = Frame(self.root)
        self.frame_1.configure(background='#4a8ad4')
        self.frame_1.place(relx= 0.0, rely=0.0, relwidth= 1, relheight= 0.2)
        
        """SubHeader cinza"""
        self.frame_3 = Frame(self.root)
        self.frame_3.configure(background='#adadad')
        self.frame_3.place(relx= 0.0, rely=0.2, relwidth= 1, relheight= 0.05)
        
        """nav lateral azul"""
        self.frame_2 = Frame(self.root)
        self.frame_2.configure(background='#01509b')
        self.frame_2.place(relx= 0.0, rely=0.25, relwidth= 0.055, relheight= 1)

        """Caixa AI"""
        self.frame_4 = Frame(self.root)
        self.frame_4.configure(background='#2596be')
        self.frame_4.place(relx= 0.065, rely=0.26, relwidth= 0.46, relheight= 0.2)

        """Caixa CE"""
        self.frame_5 = Frame(self.root)
        self.frame_5.configure(background='#2596be')
        self.frame_5.place(relx= 0.54, rely=0.26, relwidth= 0.45, relheight= 0.2)

        """Caixa PL"""
        self.frame_6 = Frame(self.root)
        self.frame_6.configure(background='#2596be')
        self.frame_6.place(relx= 0.065, rely=0.47, relwidth= 0.46, relheight= 0.2)

        """Caixa AR"""
        self.frame_7 = Frame(self.root)
        self.frame_7.configure(background='#2596be')
        self.frame_7.place(relx= 0.54, rely=0.47, relwidth= 0.45, relheight= 0.2)

        """Caixa RECURSO"""
        self.frame_8 = Frame(self.root)
        self.frame_8.configure(background='#2596be')
        self.frame_8.place(relx= 0.065, rely=0.68, relwidth= 0.46, relheight= 0.2)

        """CaixA ART"""
        self.frame_9 = Frame(self.root)
        self.frame_9.configure(background='#2596be')
        self.frame_9.place(relx= 0.54, rely=0.68, relwidth= 0.45, relheight= 0.2)

    def logo(self):
        logoimg = Image.open("../log.png")
        self.lg = ImageTk.PhotoImage(logoimg)
        self.lbl = tk.Label(self.frame_1, image= self.lg)
        self.lbl.place(relx=0.07,rely=0.1, relwidth=0.35,relheight=0.8)
        self.lbl.image = self.lg

        """Barra de pesquisa"""
        lb_pes = Entry(self.frame_1,text="Digite sua busca aqui")
        lb_pes.configure(background='#fff',fg='black',font='Arial 10 ')
        lb_pes.place(relx=0.60,rely=0.4,relwidth=0.25,relheight=0.25)

        """Botao pesquisar"""
        btn_pes = ctk.CTkButton(self.frame_1, text='Pesquisar', fg_color='#fff', text_color='#000',font=('Arial', 14))
        btn_pes.place(relx=0.86, rely=0.4, relwidth=0.07, relheight=0.25)

        
        btn_art1 = ctk.CTkButton(self.frame_2, text='Art 1º', fg_color='#01509b', text_color='White',font=('Arial', 14))
        btn_art1.place(relx=0, rely=0, relwidth=1, relheight=0.08)
        btn_art6 = ctk.CTkButton(self.frame_2, text='Art 6º a', fg_color='#01509b', text_color='White',font=('Arial', 14))
        btn_art6.place(relx=0, rely=0.08, relwidth=1, relheight=0.08)
        btn_art59 = ctk.CTkButton(self.frame_2, text='Art 6º e', fg_color='#01509b', text_color='White',font=('Arial', 14))
        btn_art59.place(relx=0, rely=0.16, relwidth=1, relheight=0.08)
        btn_art2 = ctk.CTkButton(self.frame_2, text='Art 59º', fg_color='#01509b', text_color='White',font=('Arial', 14))
        btn_art2.place(relx=0, rely=0.24, relwidth=1, relheight=0.08)
        #btn_art2 = ctk.CTkButton(self.frame_2, text='Art 2º', fg_color='#01509b', text_color='White',font=('Arial', 14))
        #btn_art2.place(relx=0, rely=0.32, relwidth=1, relheight=0.08)

        

        def selecionar_arquivo(): 
            file_path = askopenfilename(filetypes=[("Arquivos PDF", "*.pdf")], defaultextension=".pdf")
        # Verifica se o usuário selecionou um arquivo ou cancelou o diálogo
            if file_path:
                print("Arquivo selecionado:", file_path)
                partes = file_path.split("Downloads/")
                if len(partes) > 1:
                    depois_downloads = partes[1]
                lbl_selecionado = Label(self.frame_3)
                lbl_selecionado.config(text=depois_downloads,background='#adadad')
                lbl_selecionado.place(relx=0.45, rely=0.10, relwidth=0.15, relheight=0.80)
                # Abre o arquivo PDF em modo leitura binária
                with open(file_path, 'rb') as pdf_file:
                    # Cria um objeto PDFReader
                    pdf_reader = PdfReader(pdf_file)

                    # Itera por todas as páginas do arquivo
                    for page_num in range(len(pdf_reader.pages)):
                        # Extrai o conteúdo da página atual
                        page = pdf_reader.pages[page_num]
                        text = page.extract_text()

                        # Procura pelo termo "auto" na página atual
#                        match = re.search(r'(?=.*Redação)(?=.*República)', text)
                        match = re.search(r'Redação.*República|República.*Redação', text)

                         # Se o termo for encontrado, exibe o que vem depois dele
                        if match:
                            result = match.group(1)
                            print('Encontrado:', result)
                            lbl2_selecionado = Label(self.frame_4)
                            lbl2_selecionado.config(text=result,background='#4a8ad4')
                            lbl2_selecionado.place(relx=0.1, rely=0.10, relwidth=0.9, relheight=0.80)
                        else:
                            print("erro")
            else:
                print("Seleção de arquivo cancelada.")

        btn_selecionar = ctk.CTkButton(self.frame_3, text="Selecionar arquivo", command=selecionar_arquivo)
        btn_selecionar.place(relx=0.65, rely=0.10, relwidth=0.15, relheight=0.80)


        

       
App()
root.mainloop()