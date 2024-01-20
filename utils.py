# config.py

xpath_options_dict = {
    'score': list(set([
        '/html/body/main/div[2]/form/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div[1]/div[2]',
        '/html/body/main/div[2]/form/div/div[2]/div/div/div/div[1]/div[2]/div/div[1]/a/div/span[1]',
        '/html/body/main/div[2]/form/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div[1]/a/div/span[1]'
    ])),

    'num_score': list(set([
        '/html/body/main/div[2]/form/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div[1]/a/div/span[1]',
        '/html/body/main/div[2]/form/div/div[2]/div/div/div/div[1]/div[1]/div/div[1]/a/div/span[1]',
        '/html/body/main/div[2]/form/div/div[1]/div[2]/div[1]/div/div[1]/div[1]/div[2]/div[1]/div/span[1]'
    ])),

    'title': list(set([
        '//*[@id="VacancyHeader"]/div[1]/div[1]/h2',
        '//*[@id="VacancyHeader"]/div[2]/div/h2',
        '/html/body/main/div[2]/form/div/div[2]/div/div/div/div[1]/div[1]/div[1]/h2',
        '/html/body/main/div[2]/form/div/div[2]/div/div/div/div[1]/div[2]/div/h2'
    ])),

    'empresa_name': list(set([
        "/html/body/main/div[2]/form/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div[1]/div[1]/a",
        "/html/body/main/div[2]/form/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div[1]/div[1]/a",
        "/html/body/main/div[2]/form/div/div[2]/div/div/div/div[1]/div[2]/div/div[2]/div[1]",
        "/html/body/main/div[2]/form/div/div[2]/div/div/div/div[1]/div[1]/div/div[1]/div[2]"
    ])),

    'localizacao': list(set([
        '/html/body/main/div[2]/form/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div[2]/div[1]',
        '//*[@id="VacancyHeader"]/div[2]/div/div[2]/div[1]',
        '/html/body/main/div[2]/form/div/div[2]/div/div/div/div[1]/div[2]/div/div[2]/div[1]'
    ])),

    'modelo': list(set([
        '/html/body/main/div[2]/form/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div[2]/div[3]',
        '/*[@id="VacancyHeader"]/div[2]/div/div[2]/div[3]',
        '/html/body/main/div[2]/form/div/div[2]/div/div/div/div[1]/div[2]/div/div[2]/div[3]'
    ])),

    'vaga_salario': list(set([
        '/html/body/main/div[2]/form/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div[2]/div[2]',
        '/html/body/main/div[2]/form/div/div[2]/div/div/div/div[1]/div[2]/div/div[2]/div[2]',
        '/html/body/main/div[2]/form/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div[2]/div[2]',
        '/html/body/main/div[2]/form/div/div[2]/div/div/div/div[1]/div[2]/div/div[2]/div[2]'
    ])),

    'vaga_descricao': list(set([
        '/html/body/main/div[2]/form/div/div[2]/div/div/div/div[2]',
        '//*[@id="VacancyHeader"]/div[2]/div/div[2]/div[2]/span'
    ])),

    'link_vaga': list(set([
        '/html/body/main/div[2]/form/div/div[2]/div/div/div/div[1]/div[3]/div[2]/a'
    ])),
}
