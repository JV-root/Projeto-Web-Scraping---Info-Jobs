from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
import pandas as pd

from utils import xpath_options_dict


def get_vagas():
    """ 
    Função principal responsável por fazer o scraping das vagas de emprego do site InfoJobs.
    
    """

    # options = Options()
    # options.add_argument('--headless=new')

    numero_de_interações = int(input("Digite o numero de interacoes: "))

    for i in range(1,numero_de_interações):
        URL = f"https://www.infojobs.com.br/empregos-em-rio-janeiro.aspx?page={i}"
        #driver = webdriver.Chrome(options=options)
        driver = webdriver.Chrome()
        driver.get(URL)
        driver.maximize_window()

        time.sleep(2)
        cookies_button = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div/div[3]/button[2]")
        cookies_button.click()



        def get_score():
            """
            Função responsável por fazer o scraping da nota da empresa. Caso não tenha nota, retorna "Sem nota".

            """

            xpath_options = xpath_options_dict['score']

            vaga_score = None

            for xpath_options in xpath_options:
                try:
                    vaga_score = driver.find_element(By.XPATH, xpath_options).text
                    break
                except NoSuchElementException:
                    pass
            
            if vaga_score is not None:
                return vaga_score
            else:
                return "Sem nota"


        def get_num_score():
            """
            Função responsável por fazer o scraping do número de avaliações da empresa. Caso não tenha avaliações, retorna "Sem avaliações".

            """
            
            xpath_option =  xpath_options_dict['num_score']

            vaga_num_score = None

            for xpath_option in xpath_option:
                try:
                    vaga_num_score = driver.find_element(By.XPATH, xpath_option).text
                    break
                except NoSuchElementException:
                    pass

            if vaga_num_score is not None:
                return vaga_num_score
            else:
                return "Sem avaliações"
             
            

        def get_title():
            """
            Função responsável por fazer o scraping do título da vaga.

            """
            # Pega o xpath do título da vaga do arquivo utils.py
            xpath_options = xpath_options_dict['title']

            vaga_title = None

            for xpath_options in xpath_options:
                try:
                    time.sleep(0.5)
                    vaga_title = driver.find_element(By.XPATH, xpath_options).text
                    break
                except NoSuchElementException:
                    pass
            
            if vaga_title is not None:
                return vaga_title
            else:
                return "Título não encontrado"


        def get_empresa_name():
            """
            Função responsável por fazer o scraping do nome da empresa.

            """
            # 
            xpath_options = xpath_options_dict['empresa_name']

            vaga_empresa = None

            for xpath_options in xpath_options:
                try:
                    time.sleep(0.8)
                    vaga_empresa = driver.find_element(By.XPATH, xpath_options).text
                    break
                except NoSuchElementException:
                    pass

            if vaga_empresa is not None:
                return vaga_empresa
            else:
                return "Nome da empresa não encontrado"



        def get_localizacao():
            """
            Função responsável por fazer o scraping da localização da vaga.

            """

            xpath_options = xpath_options_dict['localizacao']

            vaga_localizacao = None

            for xpath_options in xpath_options:
                try:
                    time.sleep(0.5)
                    vaga_localizacao = driver.find_element(By.XPATH, xpath_options).text
                    break
                except NoSuchElementException:
                    pass
            
            if vaga_localizacao is not None:
                return vaga_localizacao
            else:
                return "Localização não encontrada"
            

        def get_modelo():
            """
            Função responsável por fazer o scraping do modelo da vaga. Caso não tenha modelo, retorna "Sem modelo".

            """

            xpath_options = xpath_options_dict['modelo']

            vaga_modelo = None

            for xpath_options in xpath_options:
                try:
                    vaga_modelo = driver.find_element(By.XPATH, xpath_options).text
                    break
                except NoSuchElementException:
                    pass

            if vaga_modelo is not None:
                return vaga_modelo
            else:
                return "Modelo de trabalho não encontrado"


        def get_vaga_salario():
            """
            Função responsável por fazer o scraping do salário da vaga.

            """

            xpath_options = xpath_options_dict['vaga_salario']

            vaga_salario = None

            for xpath_options in xpath_options:
                try:
                    time.sleep(1)
                    vaga_salario = driver.find_element(By.XPATH, xpath_options)
                    vaga_salario = vaga_salario.text
                    break
                except NoSuchElementException:
                    pass

            if vaga_salario is not None:
                return vaga_salario
            else:
                return "Salário não encontrado"
        


        def get_vaga_descricao():
            """
            Função responsável por fazer o scraping da descrição da vaga.

            """

            xpath_options = xpath_options_dict['vaga_descricao']

            vaga_descricao = None

            for xpath_options in xpath_options:
                try:
                    vaga_descricao = driver.find_element(By.XPATH, xpath_options).text
                    break
                except NoSuchElementException:
                    pass
            
            if vaga_descricao is not None:
                return vaga_descricao
            else:
                return "Descrição não encontrada."



        def get_link_vaga():
            
            xpath_options = xpath_options_dict['link_vaga']

            vaga_link = None

            for xpath_options in xpath_options:
                try:
                    vaga_link = driver.find_element(By.XPATH, xpath_options).get_attribute("data-url")
                    break
                except NoSuchElementException:
                    pass
            
            if vaga_link is not None:
                return vaga_link
            else:
                return "Link não encontrado"


        def get_description():
            """
            Função responsável por fazer o scraping da descrição da vaga.
            """

            vaga_title = get_title()
            vaga_empresa = get_empresa_name()
            vaga_localizacao = get_localizacao()
            vaga_modelo = get_modelo()
            vaga_salario = get_vaga_salario()
            # vaga_descricao = get_vaga_descricao()

            vaga_num_score = get_num_score()
            vaga_score = get_score()
            link_vaga = get_link_vaga()

            data = pd.DataFrame(columns=['Vaga', 'Empresa','Pontuacao_Empresa','Numero_Avaliacoes','Localizacao_da_Vaga', 'Modelo', 'Salario', 'Link_Vaga'], 
                                data=[[vaga_title, vaga_empresa,vaga_score,vaga_num_score, vaga_localizacao, vaga_modelo, vaga_salario, link_vaga]])
            
            # Tratamento da Localização da Vaga
            data['Localizacao_da_Vaga'] = data['Localizacao_da_Vaga'].str.split(',').str[0]

            data.to_csv('output.csv', mode='a', header=False, index=False, encoding='utf-8')


            with open('output.csv', 'r', encoding='utf-8') as file:
                    last_line = file.readlines()[-1]

            return print(last_line)



        def get_element():
            
            for i in range(1, 20):
                time.sleep(0.3)
                element = f'/html/body/main/div[2]/form/div/div[1]/div[2]/div[{i}]'
                click_element = driver.find_element(By.XPATH, element)
                click_element.click()

                get_description()

        get_element()
        driver.quit()

get_vagas()
  