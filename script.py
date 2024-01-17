from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
import time
import pandas as pd



def get_vagas():
    """ 
    Função principal responsável por fazer o scraping das vagas de emprego do site InfoJobs.
    
    """

    # instance of Options class allows
    # us to configure Headless Chrome

    # options = Options()

    # this parameter tells Chrome that
    # it should be run without UI (Headless)

    # options.add_argument('--headless=new')

    numero_de_interações = int(input("Digite o número de interações: "))


    for i in range(1,numero_de_interações):
        URL = f"https://www.infojobs.com.br/empregos-em-sao-paulo.aspx?page={i}"
        #driver = webdriver.Chrome(options=options)
        driver = webdriver.Chrome()
        driver.get(URL)
        driver.maximize_window() 

        time.sleep(5)
        cookies_button = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div/div[3]/button[2]")
        cookies_button.click()
        time.sleep(1)



        def get_score():
            """
            Função responsável por fazer o scraping da nota da empresa. Caso não tenha nota, retorna "Sem nota".

            """

            xpath_options = ['/html/body/main/div[2]/form/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div[1]/a/div/span[1]',
                            
                            ]

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

            try:
                primeira_vaga_avaliacoes = driver.find_element(By.XPATH, "/html/body/main/div[2]/form/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div[1]/div[2]")
                return primeira_vaga_avaliacoes.text
            except:
                return "Sem avaliações"
            

        def get_title():
            """
            Função responsável por fazer o scraping do título da vaga.

            """


            xpath_options = ['//*[@id="VacancyHeader"]/div[1]/div[1]/h2',
                            '//*[@id="VacancyHeader"]/div[2]/div/h2',
                            ]


            vaga_title = None

            for xpath_options in xpath_options:
                try:
                    time.sleep(1)
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
            # Preciso mudar essa estrutura para um código melhor.

            xpath_options = [
            "/html/body/main/div[2]/form/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div[1]/div[1]/a",
            "/html/body/main/div[2]/form/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div[1]/div[1]/a",
            "/html/body/main/div[2]/form/div/div[2]/div/div/div/div[1]/div[2]/div/div[2]/div[1]",
            "/html/body/main/div[2]/form/div/div[2]/div/div/div/div[1]/div[1]/div/div[1]/div[2]"
            ]

            vaga_empresa = None

            for xpath_options in xpath_options:
                try:
                    time.sleep(1)
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

            xpath_options = ['/html/body/main/div[2]/form/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div[2]/div[1]',
                            '//*[@id="VacancyHeader"]/div[2]/div/div[2]/div[1]',
                            ]

            vaga_localizacao = None

            for xpath_options in xpath_options:
                try:
                    time.sleep(1)
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

            xpath_options = ['/html/body/main/div[2]/form/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div[2]/div[3]', 
                            '/*[@id="VacancyHeader"]/div[2]/div/div[2]/div[3]'
                            ]

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

            xpath_options = ['/html/body/main/div[2]/form/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div[2]/div[2]',
                            '/html/body/main/div[2]/form/div/div[2]/div/div/div/div[1]/div[2]/div/div[2]/div[2]',
                            '/html/body/main/div[2]/form/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div[2]/div[2]',
                            '/html/body/main/div[2]/form/div/div[2]/div/div/div/div[1]/div[2]/div/div[2]/div[2]'
                            ]

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

            xpath_options = ['/html/body/main/div[2]/form/div/div[2]/div/div/div/div[2]',
                            '//*[@id="VacancyHeader"]/div[2]/div/div[2]/div[2]/span'
                            
                            ]

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
            
            xpath_options = ['/html/body/main/div[2]/form/div/div[2]/div/div/div/div[1]/div[3]/div[2]/a',
                             '/html/body/main/div[2]/form/div/div[2]/div/div/div/div[1]/div[3]/div[2]/a'
                             
                             ]

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

            data.to_csv('output.csv', mode='a', header=False, index=False)



        def get_element():
            
            for i in range(1, 20):
                time.sleep(1)
                element = f'/html/body/main/div[2]/form/div/div[1]/div[2]/div[{i}]'
                click_element = driver.find_element(By.XPATH, element)
                click_element.click()

                get_description()

        get_element()
        driver.quit()


get_vagas()
  