# -*- coding: iso-8859-1 -*-
from model.pesquisa.pesquisa_db import Pesquisa
from datetime import datetime


class Acoes(object):
    """Classe objeto acao."""

    def __init__(self):
        """Inicializa o objeto."""
        self._p = Pesquisa()

    def buscar_empresas(self, empresas=[]):
        """Busca as empresas disponiveis no banco."""
        return self._p.busca_empresa(empresas=empresas)

    def buscar_acoes_empresas(self, empresas=[], dt_init=None, dt_fim=None):
        """Busca as acoes das empresas solicitadas."""
        return self._p.busca_acoes(empresas=empresas, dt_init=dt_init,
                                   dt_fim=dt_fim)

    def validar_data(self, data):
        """Valida uma data e retorna como objeto Date."""
        d = None
        try:
            if data:
                d = datetime.strptime(data, '%d/%m/%Y')
        except ValueError:
            return (0, d)
        
        return (1, d)

    def validar_empresa(self, id_empresa, unique=False):
        """Valida o id_empresa e retorna uma lista de int."""
        try:
            if not unique:
                if isinstance(id_empresa, [list, tuple]):
                    return (1, [int(x) for x in id_empresa])
                else:
                    return (1, [int(x)])
            else:
                return (1, int(id_empresa))
        except:
            if not unique:
                return (0, [])
            else:
                return (0, None)

    def calcular(self, dados):
        """Recebe os dados necessarios para iniciar os calculos."""
        return


    # Codigo para fazer o calculo. Precisa ser adaptado para o funcionar
    # com o banco de dados
    # import csv

    # companies = ['PETR4','CPLE6','CIEL3']
    # #companies = ['PETR4','CIEL3']
    # emp = []
    # #temp = []
    # corrTable = []
    # corrDict = {}

    # def meanCalc(values):
    #     c = 0
    #     for value in values:
    #         c = c + value
    #     Mean = c/len(values)
    #     return Mean

    # def stdDev(values):
    #     c = 0
    #     x = meanCalc(values)
    #     for value in values:
    #         c = c + (value - x)**2
    #     SD = (c/(len(values) - 1))**(0.5) ## **(0.5) -> square root
    #     return SD

    # def covarianceCalc(values_1, values_2):
    #     c = 0
    #     m1 = meanCalc(values_1)
    #     m2 = meanCalc(values_2)
    #     ran = len(values_1)
    #     for i in range(ran):
    #         c = c +(values_1[i]-m1)*(values_2[i]-m2)
    #     cov = c/(ran-1)
    #     return cov



    # def getPricesOnly(database, date):
    #     storeValues = []
    #     i = False
    #     for item in database:
    #         if item[0] == date:
    #             i = True
    #         if i == True:
    #             storeValues.append(float(item[1]))
    #     return storeValues



    # print("Digite o ticker da empresa que deseje consultar:\n")
    # ticker = input()
    # print("Digite a data inicial no formato aaaa-mm-dd:\n")
    # data = input()

    # with open(ticker+'.SA.csv', 'r') as bvsp_file:
    #     bvsp_reader = csv.DictReader(bvsp_file)
    #     for line in bvsp_reader:
    #         emp.append([line.pop('Date'), line.pop('Adj Close')])
    #     pricesChosenCompany = getPricesOnly(emp, data) #precos da acao escolhida
    #     sdChosenCompany = stdDev(pricesChosenCompany)
    #     meanChosenStock = meanCalc(pricesChosenCompany)
    #     #print(sdChosenCompany)
    #     print(meanChosenStock)

    # for company in companies:
    #     if(company != ticker):
    #         temp = []
    #         with open(company+'.SA.csv', 'r') as comp_file:
    #             comp_reader = csv.DictReader(comp_file)
    #             for line in comp_reader:
    #                 temp.append([line.pop('Date'), line.pop('Adj Close')])
    #             pricesComparedCompany = getPricesOnly(temp, data) #precos da acao a ser comparada
    #             sdComparedCompany = stdDev(pricesComparedCompany)
    #             covPrices = covarianceCalc(pricesChosenCompany, pricesComparedCompany)
    #             corr = covPrices/(sdChosenCompany*sdComparedCompany)
    #             corrDict[ticker+'-'+company] = corr
    # print(corrDict)
