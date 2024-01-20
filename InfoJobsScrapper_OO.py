from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
import pandas as pd

class InfoJobsScraper:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.base_url = "https://www.infojobs.com.br/empregos-em-sao-paulo.aspx"
        self.output_file = 'output.csv'

    def close_cookies_popup(self):
        try:
            cookies_button = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div/div[3]/button[2]")
            cookies_button.click()
            time.sleep(1)
        except NoSuchElementException:
            pass

    def get_element_text(self, xpath_options):
        for xpath_option in xpath_options:
            try:
                element = self.driver.find_element(By.XPATH, xpath_option)
                return element.text
            except NoSuchElementException:
                pass
        return None

    def get_vaga_score(self):
        xpath_options = ['/html/body/main/div[2]/form/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div[1]/a/div/span[1]']
        return self.get_element_text(xpath_options) or "Sem nota"

    def get_num_score(self):
        try:
            element = self.driver.find_element(By.XPATH, "/html/body/main/div[2]/form/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div[1]/div[2]")
            return element.text
        except NoSuchElementException:
            return "Sem avaliações"

    def get_title(self):
        xpath_options = ['//*[@id="VacancyHeader"]/div[1]/div[1]/h2', '//*[@id="VacancyHeader"]/div[2]/div/h2']
        return self.get_element_text(xpath_options) or "Título não encontrado"

    def get_empresa_name(self):
        xpath_options = [
            "/html/body/main/div[2]/form/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div[1]/div[1]/a",
            "/html/body/main/div[2]/form/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div[1]/div[1]/a",
            "/html/body/main/div[2]/form/div/div/2/div/div/div/div[1]/div[2]/div/div[2]/div[1]",
            "/html/body/main/div[2]/form/div/div[2]/div/div/div/div[1]/div[1]/div/div[1]/div[2]"
        ]
        return self.get_element_text(xpath_options) or "Nome da empresa não encontrado"

    def get_localizacao(self):
        xpath_options = [
            '/html/body/main/div[2]/form/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div[2]/div[1]',
            '//*[@id="VacancyHeader"]/div[2]/div/div[2]/div[1]'
        ]
        return self.get_element_text(xpath_options) or "Localização não encontrada"

    def get_modelo(self):
        xpath_options = [
            '/html/body/main/div[2]/form/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div[2]/div[3]',
            '/*[@id="VacancyHeader"]/div[2]/div/div[2]/div[3]'
        ]
        return self.get_element_text(xpath_options) or "Modelo de trabalho não encontrado"

    def get_vaga_salario(self):
        xpath_options = [
            '/html/body/main/div[2]/form/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div[2]/div[2]',
            '/html/body/main/div[2]/form/div/div[2]/div/div/div/div[1]/div[2]/div/div[2]/div[2]',
            '/html/body/main/div[2]/form/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div[2]/div[2]',
            '/html/body/main/div[2]/form/div/div[2]/div/div/div/div[1]/div[2]/div/div[2]/div[2]'
        ]
        element = self.get_element_text(xpath_options)
        return element.text if element else "Salário não encontrado"

    def get_vaga_descricao(self):
        xpath_options = ['/html/body/main/div[2]/form/div/div[2]/div/div/div/div[2]', '//*[@id="VacancyHeader"]/div[2]/div/div[2]/div[2]/span']
        return self.get_element_text(xpath_options) or "Descrição não encontrada"

    def get_link_vaga(self):
        xpath_options = [
            '/html/body/main/div[2]/form/div/div[2]/div/div/div/div[1]/div[3]/div[2]/a',
            '/html/body/main/div[2]/form/div/div[2]/div/div/div/div[1]/div[3]/div[2]/a'
        ]
        element = self.get_element_text(xpath_options)
        return element.get_attribute("data-url") if element else "Link não encontrado"

    def get_description(self):
        vaga_title = self.get_title()
        vaga_empresa = self.get_empresa_name()
        vaga_localizacao = self.get_localizacao()
        vaga_modelo = self.get_modelo()
        vaga_salario = self.get_vaga_salario()
        vaga_descricao = self.get_vaga_descricao()

        vaga_num_score = self.get_num_score()
        vaga_score = self.get_vaga_score()
        link_vaga = self.get_link_vaga()

        data = pd.DataFrame(columns=['Vaga', 'Empresa', 'Pontuacao_Empresa', 'Numero_Avaliacoes', 'Localizacao_da_Vaga', 'Modelo', 'Salario', 'Link_Vaga'],
                            data=[[vaga_title, vaga_empresa, vaga_score, vaga_num_score, vaga_localizacao, vaga_modelo, vaga_salario, link_vaga]])

        data.to_csv(self.output_file, mode='a', header=False, index=False, encoding='utf-8')

    def get_element(self):
        for i in range(1, 20):
            time.sleep(1)
            element_xpath = f'/html/body/main/div[2]/form/div/div[1]/div[2]/div[{i}]'
            click_element = self.driver.find_element(By.XPATH, element_xpath)
            click_element.click()
            self.get_description()

    def scrape_vagas(self, numero_de_interacoes):
        for i in range(1, numero_de_interacoes):
            URL = f"{self.base_url}?page={i}"
            self.driver.get(URL)
            self.driver.maximize_window()
            time.sleep(5)
            self.close_cookies_popup()
            self.get_element()

    def quit_driver(self):
        self.driver.quit()


def main():
    numero_de_interacoes = int(input("Digite o numero de interacoes: "))
    scraper = InfoJobsScraper()
    scraper.scrape_vagas(numero_de_interacoes)
    scraper.quit_driver()


if __name__ == "__main__":
    main()
