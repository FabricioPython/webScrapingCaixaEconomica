from playwright.sync_api import sync_playwright, Playwright
import time
import pandas as pd
from bs4 import BeautifulSoup

dados = []
def test_botao(obj, op):
    b = obj.locator('#ctl00_ctl61_g_7fcd6a4b_5583_4b25_b2c4_004b6fef4036_btnVerMais')
    print(obj.locator('#ctl00_ctl61_g_7fcd6a4b_5583_4b25_b2c4_004b6fef4036_ddlCidade').select_option(str(op)))
    if b.is_visible():
        #ctl00_ctl61_g_7fcd6a4b_5583_4b25_b2c4_004b6fef4036_btnVerMais
        b.click()
        time.sleep(3)

        return True
    else:
        return False


def run(playwright: Playwright):
    google = playwright.chromium
    browser = google.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.caixa.gov.br/atendimento/Paginas/encontre-a-caixa.aspx")

    page.click('#adopt-accept-all-button')

    page.select_option("#ctl00_ctl61_g_7fcd6a4b_5583_4b25_b2c4_004b6fef4036_ddlTipo", value="2")

    page.select_option('#ctl00_ctl61_g_7fcd6a4b_5583_4b25_b2c4_004b6fef4036_ddlUf', value='RJ')

    
    # loop pode comecar aqui
    page.locator('#ctl00_ctl61_g_7fcd6a4b_5583_4b25_b2c4_004b6fef4036_ddlCidade').select_option('0')

    opcoes = page.evaluate("Array.from(document.querySelectorAll('#ctl00_ctl61_g_7fcd6a4b_5583_4b25_b2c4_004b6fef4036_ddlCidade option')).map(o => o.value).filter(v => v !== '0');")
    
    for op in opcoes:

        page.locator('#ctl00_ctl61_g_7fcd6a4b_5583_4b25_b2c4_004b6fef4036_ddlCidade').select_option(str(op))
        time.sleep(1)

        page.click('#ctl00_ctl61_g_7fcd6a4b_5583_4b25_b2c4_004b6fef4036_btnBuscar')
        time.sleep(1)
        
        #btn = page.locator('#ctl00_ctl61_g_7fcd6a4b_5583_4b25_b2c4_004b6fef4036_btnVerMais')
        resultado = test_botao(page, op)
        print(f'Resultado do Botão de ver mais: {resultado}')

        while resultado:
            time.sleep(2)
            resultado = test_botao(page, op)



        time.sleep(1)
        # Tratamento de Dados

        
        loteria = page.locator('.resultado-busca-item').all_inner_texts()
        informacoes = page.locator('.informacoes')


        html_completo = page.content()
        soup = BeautifulSoup(html_completo, 'html.parser')

        itens = soup.select('.resultado-busca-item')

        for i, loterica in enumerate(itens):
            #aux =  loterica.replace('\t', ' ').split('\n')
            #aux.extend(informacoes[i].split('\n'))
            #dados.extend([aux])
            #print(informacoes[i].split('\n'))
            fantasia = loterica.find('h4', class_='resultado-busca-titulo').next_sibling
            nome = loterica.find('b', text='Razão Social:').next_sibling
            cnpj = loterica.find('b', text="CNPJ:").next_sibling
            ag_vinculada = loterica.find('b', text='Agência de vinculação:').next_sibling
            email = loterica.find('b', text='E-mail:').next_sibling
            #atividade = loterica.find('p', class_='informacoes').get_text()
            dados.append([nome, cnpj, ag_vinculada, email])


    

        
        
    print(f'dados {len(dados)}')
    df  = pd.DataFrame(dados) 
    df.to_csv('./lotericos_estado_rj.csv')




    #page.wait_for_event("close")
    browser.close()

with sync_playwright() as playwright:
    run(playwright)





'''
        loteria = page.locator('.resultado-busca-item').all_inner_texts()

        for loterica in loteria:
            print(loterica.replace(' ', '').split('\n'))

        informacoes = page.locator('.informacoes').all_inner_texts()

        for info in informacoes:
            print(info.replace(' ', '').split('\n'))
    '''