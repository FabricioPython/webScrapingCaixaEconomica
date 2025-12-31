from playwright.sync_api import sync_playwright, Playwright
import time
import pandas as pd
from bs4 import BeautifulSoup

dados = []


def test_botao(obj, op):
    b = obj.locator("#ctl00_ctl61_g_7fcd6a4b_5583_4b25_b2c4_004b6fef4036_btnVerMais")
    print(
        obj.locator(
            "#ctl00_ctl61_g_7fcd6a4b_5583_4b25_b2c4_004b6fef4036_ddlCidade"
        ).select_option(str(op))
    )
    if b.is_visible():
        # ctl00_ctl61_g_7fcd6a4b_5583_4b25_b2c4_004b6fef4036_btnVerMais
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

    # pop up
    page.click("#adopt-accept-all-button")

    page.select_option(
        "#ctl00_ctl61_g_7fcd6a4b_5583_4b25_b2c4_004b6fef4036_ddlTipo",
        value="6",
    )

    page.select_option(
        "#ctl00_ctl61_g_7fcd6a4b_5583_4b25_b2c4_004b6fef4036_ddlUf", value="RJ"
    )

    # loop pode comecar aqui
    page.locator(
        "#ctl00_ctl61_g_7fcd6a4b_5583_4b25_b2c4_004b6fef4036_ddlCidade"
    ).select_option("0")

    opcoes = page.evaluate(
        "Array.from(document.querySelectorAll('#ctl00_ctl61_g_7fcd6a4b_5583_4b25_b2c4_004b6fef4036_ddlCidade option')).map(o => o.value).filter(v => v !== '0');"
    )

    for op in opcoes:

        page.locator(
            "#ctl00_ctl61_g_7fcd6a4b_5583_4b25_b2c4_004b6fef4036_ddlCidade"
        ).select_option(str(op))
        time.sleep(1)

        page.click("#ctl00_ctl61_g_7fcd6a4b_5583_4b25_b2c4_004b6fef4036_btnBuscar")
        time.sleep(1)

        # btn = page.locator('#ctl00_ctl61_g_7fcd6a4b_5583_4b25_b2c4_004b6fef4036_btnVerMais')
        resultado = test_botao(page, op)
        print(f"Resultado do Botão de ver mais: {resultado}")

        while resultado:
            time.sleep(2)
            resultado = test_botao(page, op)

        time.sleep(1)

        # Tratamento de Dados
        html_completo = page.content()
        soup = BeautifulSoup(html_completo, "html.parser")

        itens = soup.select(".resultado-busca-item")

        for i, corr_bancario in enumerate(itens):

            fantasia = corr_bancario.select("h4.resultado-busca-titulo")[0].text.strip()
            endereco = corr_bancario.select("h4.resultado-busca-titulo + p")[0].text.strip()
            nome = corr_bancario.find("b", text="Razão Social:").next_sibling
            cnpj = corr_bancario.find("b", text="CNPJ:").next_sibling
            ag_vinculada = corr_bancario.find(
                "b", text="Agência de vinculação:"
            ).next_sibling
            email = corr_bancario.find("b", text="E-mail:").next_sibling
            atividade = corr_bancario.select("p.informacoes + p")[0].text.strip()
            # print(atividade, i)
            dados.append(
                [
                    fantasia,
                    nome,
                    endereco,
                    cnpj,
                    ag_vinculada,
                    email,
                    atividade,
                ]
            )

    print(f"dados {len(dados)}")

    df = pd.DataFrame(
        dados,
        columns=[
            "Nome Fantasia",
            "Razao Social",
            "Endereco",
            "CNPJ",
            "Agencia Vinculada",
            "E-mail",
            "Atividade",
        ],
    )

    df.to_csv("./correspondentes_bancarios_estado.csv")

    # page.wait_for_event("close")
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
