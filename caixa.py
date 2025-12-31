from enum import StrEnum
from playwright.sync_api import sync_playwright, Playwright
import time
import pandas as pd
from bs4 import BeautifulSoup
from typing import Literal

# em desenvolvimento ***

class ElementosId(StrEnum):
    ID_TIPO_ATENDIMENTO = '#ctl00_ctl61_g_7fcd6a4b_5583_4b25_b2c4_004b6fef4036_ddlTipo'
    ID_UF = '#ctl00_ctl61_g_7fcd6a4b_5583_4b25_b2c4_004b6fef4036_ddlUf'
    ID_CIDADE = '#ctl00_ctl61_g_7fcd6a4b_5583_4b25_b2c4_004b6fef4036_ddlCidade'
    ID_BOTAO = '#ctl00_ctl61_g_7fcd6a4b_5583_4b25_b2c4_004b6fef4036_btnBuscar'
    ID_BTN_VER_MAIS = '#ctl00_ctl61_g_7fcd6a4b_5583_4b25_b2c4_004b6fef4036_btnVerMais'
    ID_POP_UP_COOKIE = '#adopt-accept-all-button'

class TipoAtendimento(StrEnum):
    AGENCIAS = "1"
    LOTERIAS = "2"
    CBANCARIO = "6"
    PATENDIMENTO = "8"

class Uf(StrEnum):
    AC="AC"
    AL="AL"
    AP="AP"
    AM="AM"
    BA="BA"
    CE="CE"
    DF="DF"
    ES="ES"
    G0="GO"
    MA="MA"
    MT="MT"
    MS="MS"
    MG="MG"
    PA="PA"
    PB="PB"
    PR="PR"
    PE="PE"
    PI="PI"
    RJ="RJ"
    RN="RN"
    RS="RS"
    R0="RO"
    RR="RR"
    SC="SC"
    SP="SP"
    SE="SE"
    TO="TO"


class Municipio(StrEnum):
    ...


class CaixaData():

    def __init__(self,*, plw: Playwright, tipo: TipoAtendimento, uf: Uf, visivel: Literal[True, False]) -> None:
        self.data = []
        self.tipo = tipo
        self.uf = uf
        self.google = plw.chromium.launch(headless=visivel)




    def buscar(self, uf: Uf):

        # Abre o navegador
        self.page = self.google.new_page()

        # Acessa o site
        self.page.goto("https://www.caixa.gov.br/atendimento/Paginas/encontre-a-caixa.aspx")

        # fecha o pop up
        self.page.click(ElementosId.ID_POP_UP_COOKIE.value)


        # seleciona o tipo de atendimento
        self.page.select_option(
            selector=ElementosId.ID_TIPO_ATENDIMENTO.value,
            value=self.tipo.value,
        )

        # seleciona a unidade federativa
        self.page.select_option(
            ElementosId.ID_UF.value, value=uf.value
            )
        
        # seleciona a cidade
        self.page.select_option(
            ElementosId.ID_CIDADE.value,
        )

        # cria lista de cidades
        self.opcoes = self.page.evaluate(
        "Array.from(document.querySelectorAll('#ctl00_ctl61_g_7fcd6a4b_5583_4b25_b2c4_004b6fef4036_ddlCidade option')).map(o => o.value).filter(v => v !== '0');"
        )

        # loop
        for cidade in self.opcoes:
            ...

            # recebe uma cidade
            self.page.locator(
            ElementosId.ID_CIDADE.value).select_option(str(cidade))
            time.sleep(1)

            # clica no botao buscar
            self.page.click(ElementosId.ID_BOTAO.value)
            time.sleep(1)

            # verifica se o resultado tem mais paginas dinamicas para serem carregadas
            status = self.test_botao(self.page, cidade)
            print(f"Resultado do Botão de ver mais: {status}")

            # loop dados
            while status:
                time.sleep(2)
                status = self.test_botao(self.page, cidade)

            time.sleep(1)
            

        



        ...
        return print('Finalizado!')

    

    def exportar(self,):
        ...
        # um, dois ou todos


    def ver_salvos(self,):
        ...

    def test_botao(self, obj, op):
        aux_b = obj.locator(ElementosId.ID_BTN_VER_MAIS.value)

        if aux_b.is_visible():
            aux_b.click()
            time.sleep(3)

            return True
        else:
            return False






with sync_playwright() as plw:
    scrping_rj = CaixaData(plw=plw,tipo=TipoAtendimento.AGENCIAS, uf=Uf.RJ, visivel=False)
    scrping_rj.buscar(uf=Uf.RJ)
    time.sleep(3)
