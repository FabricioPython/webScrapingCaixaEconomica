from enum import Enum
from playwright.sync_api import sync_playwright, Playwright
import time
import pandas as pd
from bs4 import BeautifulSoup
from typing import Literal

# em desenvolvimento ***

class ElementosId(Enum):
    ID_TIPO_ATENDIMENTO = 'ctl00_ctl61_g_7fcd6a4b_5583_4b25_b2c4_004b6fef4036_ddlTipo'
    ID_UF = 'ctl00_ctl61_g_7fcd6a4b_5583_4b25_b2c4_004b6fef4036_ddlUf'
    ID_CIDADE = 'ctl00_ctl61_g_7fcd6a4b_5583_4b25_b2c4_004b6fef4036_ddlCidade'
    ID_BOTAO = 'ctl00_ctl61_g_7fcd6a4b_5583_4b25_b2c4_004b6fef4036_btnBuscar'
    ID_BTN_VER_MAIS = 'ctl00_ctl61_g_7fcd6a4b_5583_4b25_b2c4_004b6fef4036_btnVerMais'

class TipoAtendimento(Enum):
    AGENCIAS = "1"
    LOTERIAS = "2"
    CBANCARIO = "6"
    PATENDIMENTO = "8"

class Uf(Enum):
    AC="AC",
    AL="AL",
    AP="AP",
    AM="AM",
    BA="BA",
    CE="CE",
    DF="DF",
    ES="ES",
    G0="GO",
    MA="MA", 
    MT="MT",
    MS="MS",
    MG="MG",
    PA="PA",
    PB="PB",
    PR="PR",
    PE="PE",
    PI="PI",
    RJ="RJ",
    RN="RN", 
    RS="RS",
    R0="RO",
    RR="RR",
    SC="SC",
    SP="SP",
    SE="SE",
    TO="TO"


class Municipio(Enum):
    ...


class CaixaData:

    def __init__(self,*, plw: Playwright, tipo: TipoAtendimento, uf: Uf, visivel: Literal[True, False]) -> None:
        self.data = []
        self.tipo = tipo
        self.uf = uf
        self.google = plw.chromium.launch(headless=visivel)




    def buscar(self):
        self.page = self.google.new_page()
        self.page.goto("https://www.caixa.gov.br/atendimento/Paginas/encontre-a-caixa.aspx")

        ...
        return print('Finalizado!')

    

    def exportar(self,):
        ...
        # um, dois ou todos


    def ver_salvos(self,):
        ...






with sync_playwright() as plw:
    scrping_rj = CaixaData(plw=plw,tipo=TipoAtendimento.AGENCIAS, uf=Uf.RJ, visivel=False)
    scrping_rj.buscar()


with sync_playwright() as plw:
    scrping_mg = CaixaData(plw=plw,tipo=TipoAtendimento.AGENCIAS, uf=Uf.MG, visivel=False)
    scrping_mg.buscar()