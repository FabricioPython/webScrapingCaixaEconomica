<div align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Playwright-2EAD33?style=for-the-badge&logo=playwright&logoColor=white" />
  <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" />
  <img src="https://img.shields.io/badge/BeautifulSoup-FF9900?style=for-the-badge&logo=python&logoColor=white" />
</div>

<h1 align="center" style="color: #005CA9;">🏦 Web Scraping Caixa Econômica</h1>

<p align="center" style="color: #555555; font-size: 1.2em;">
  Automação inteligente para mapeamento de Agências, Loterias e Correspondentes Bancários da Caixa Econômica Federal.
</p>

---

## 🎯 Sobre o Projeto

Este projeto tem como objetivo **compreender e mapear a cobertura de postos de atendimento** da Caixa Econômica Federal. Utilizando automação web, o script coleta dados diretamente do site oficial e os organiza em bases de dados estruturadas, facilitando análises demográficas, de negócio ou de expansão.

O sistema navega pelas páginas de busca, interage com menus dinâmicos (selecionando Tipo, Estado e Município), clica automaticamente em botões de "Ver Mais" para carregar todos os resultados dinâmicos da página e, por fim, exporta os dados limpos para arquivos CSV.

---

## ⚙️ Como Funciona

O script principal `caixa.py` possui uma estrutura orientada a objetos (`CaixaData`) que é o coração da automação. Ele suporta a extração de quatro tipos de atendimento:
1. 🏢 **Agências**
2. 🍀 **Loterias**
3. 🤝 **Correspondentes Bancários**
4. 📍 **Postos de Atendimento**

### 📊 Estrutura dos Relatórios Exportados
Os arquivos gerados são organizados e variam de acordo com o tipo de local extraído. Geralmente incluem:
- **Nome Fantasia / Razão Social**
- **CNPJ / CGC**
- **Endereço Completo**
- **Agência Vinculada**
- **E-mail** e **Atividade**

Os dados são salvos em formato `.csv` e automaticamente divididos em pastas respectivas (ex: `Agencias/`, `Loterias/`, `Correspondente_Bancario/`).

---

## 🛠️ Tecnologias e Bibliotecas

O desenvolvimento desta ferramenta foi feito utilizando tecnologias consolidadas no ecossistema Python para Automação Web e Engenharia de Dados. Escolhemos as cores oficiais da Caixa (Azul e Laranja) como inspiração!

- **[Python 3](https://www.python.org/)** 🟦 *(#3776AB)*
- **[Playwright](https://playwright.dev/python/)**: Automação e controle de navegador de forma robusta e silenciosa (*headless*). 🟩 *(#2EAD33)*
- **[BeautifulSoup 4](https://www.crummy.com/software/BeautifulSoup/)**: Parseamento avançado do HTML da página para a extração veloz dos dados. 🟧 *(#FF9900)*
- **[Pandas](https://pandas.pydata.org/)**: Estruturação dos dados extraídos em DataFrames e exportação otimizada. 🟪 *(#150458)*
- **[clean-text](https://pypi.org/project/clean-text/)**: Limpeza de caracteres e normalização dos endereços extraídos do HTML.

---

## 🚀 Como Executar

Siga as instruções abaixo para rodar a automação em sua máquina local.

### 1. Pré-requisitos
Certifique-se de ter o **Python** instalado em sua máquina. Recomendamos também o uso de um ambiente virtual (`venv`).

### 2. Instalação
Navegue até o diretório do projeto e instale as dependências:
```bash
# Navegue até a pasta
cd "Caixa economica/scripts_playwr"

# Instale as bibliotecas necessárias
pip install playwright pandas beautifulsoup4 clean-text

# Baixe os binários dos navegadores do Playwright
playwright install chromium
```

### 3. Execução
Por padrão, o script (no fim do arquivo `caixa.py`) está configurado para testar e baixar Agências do Estado de PE. Para executar a raspagem:
```bash
python caixa.py
```
*Acompanhe pelo terminal. O script fará a busca, varredura das páginas dinâmicas e salvará os `.csv` nas pastas específicas.*

---

## 👨‍💻 Autores

- [FabricioPython](https://github.com/FabricioPython)

<div align="center">
  <p>Desenvolvido para automatizar e estruturar dados com precisão. 📊</p>
</div>
