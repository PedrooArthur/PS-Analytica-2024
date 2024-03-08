# -*- coding: utf-8 -*-
"""ScriptsDadosAnalytica2024PedroArthurSantosGama

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vpdGodVasw3f6uvfKx-QQEwGWGy_CB28
"""

pip install pandas matplotlib

#####SCRIPT DOS GRÁFICOS

import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.float_format', lambda x: '%.2f' % x)


dados = pd.read_csv('InvestimentoMacrorregioes.csv')


mapeamento_macrorregioes = {
    'Norte': ['AC', 'AP', 'AM', 'PA', 'RO', 'RR', 'TO'],
    'Nordeste': ['AL', 'BA', 'CE', 'MA', 'PB', 'PE', 'PI', 'RN', 'SE'],
    'Sudeste': ['ES', 'MG', 'RJ', 'SP'],
    'Sul': ['PR', 'RS', 'SC'],
    'Centro-Oeste': ['DF', 'GO', 'MT', 'MS']
}


dados['macrorregiao'] = dados['sigla_uf'].apply(lambda x: next(regiao for regiao, sigla_uf in mapeamento_macrorregioes.items() if x in sigla_uf))



dados_agrupados = dados.groupby(['macrorregiao', 'ano'])['GASTOS'].sum().reset_index()



macrorregiao = 'Centro-Oeste'
dados_macrorregiao_escolhida = dados_agrupados[dados_agrupados['macrorregiao'] == macrorregiao]


plt.ticklabel_format(style='plain', axis='y')
plt.plot(dados_macrorregiao_escolhida['ano'], dados_macrorregiao_escolhida['GASTOS'], marker='o', label=macrorregiao)
plt.xlabel('Ano')
plt.ylabel('Gastos em Educação')
plt.title(f'Evolução dos Gastos em Educação na Macrorregião {macrorregiao}')
plt.legend()
plt.show()

######SCRIPTS DAS CONSULTAS SQL UTLIZADAS NO BIG QUERY STUDIO



SELECT ano, sigla_uf, conta, estagio_bd, SUM(valor) AS GASTOS FROM `basedosdados.br_me_siconfi.municipio_despesas_funcao` where conta like ('%Ensino Fundamental%') and estagio_bd like 'Despesas Empenhadas' GROUP BY ano, sigla_uf, conta,estagio_bd ORDER BY ano

SELECT ano, sigla_uf, indice_escolaridade, prop_ocupados_fundamental,taxa_dom_sem_fund,taxa_dom_vulner_sem_fund, prop_ocupados_medio, taxa_criancas_fora_escola_4_5, taxa_criancas_fora_escola_6_14, pea_10_14, pea_15_17, pia_10_14, pia_15_17, (pea_10_14/ pia_10_14) * 100 AS porcentagem	 FROM `basedosdados.mundo_onu_adh.uf`

SELECT ano, sigla_uf, taxa_criancas_fora_escola_4_5, taxa_criancas_fora_escola_6_14, pea_10_14, pea_15_17, pia_10_14, pia_15_17, (pea_10_14/ pia_10_14) * 100 AS PorcPeaPia10_14, (pea_15_17/ pia_15_17) * 100 AS PorcPeaPia15_17	 FROM `basedosdados.mundo_onu_adh.uf` where sigla_uf in ('MS','MT','GO') and ano = 2000

SELECT ano, sigla_uf, taxa_criancas_fora_escola_4_5, taxa_criancas_fora_escola_6_14, pea_10_14, pea_15_17, pia_10_14, pia_15_17, (pea_10_14/ pia_10_14) * 100 AS PorcPeaPia10_14, (pea_15_17/ pia_15_17) * 100 AS PorcPeaPia15_17	 FROM `basedosdados.mundo_onu_adh.uf` where sigla_uf in ('RJ','SP','ES', 'MG') and ano = 2000

SELECT ano, sigla_uf, taxa_criancas_fora_escola_4_5, taxa_criancas_fora_escola_6_14, pea_10_14, pea_15_17, pia_10_14, pia_15_17, (pea_10_14/ pia_10_14) * 100 AS PorcPeaPia10_14, (pea_15_17/ pia_15_17) * 100 AS PorcPeaPia15_17	 FROM `basedosdados.mundo_onu_adh.uf` where sigla_uf in ('AC','AM','PA','RR','RO','AP','TO') and ano = 2000

SELECT ano, sigla_uf, taxa_criancas_fora_escola_4_5, taxa_criancas_fora_escola_6_14, pea_10_14, pea_15_17, pia_10_14, pia_15_17, (pea_10_14/ pia_10_14) * 100 AS PorcPeaPia10_14, (pea_15_17/ pia_15_17) * 100 AS PorcPeaPia15_17	 FROM `basedosdados.mundo_onu_adh.uf` where sigla_uf in ('SC','PR','RS') and ano = 2000

SELECT ano, sigla_uf, taxa_criancas_fora_escola_4_5, taxa_criancas_fora_escola_6_14, pea_10_14, pea_15_17, pia_10_14, pia_15_17, (pea_10_14/ pia_10_14) * 100 AS PorcPeaPia10_14, (pea_15_17/ pia_15_17) * 100 AS PorcPeaPia15_17	 FROM `basedosdados.mundo_onu_adh.uf` where sigla_uf in ('AL','BA','CE','MA','PA','PB','PI','RN','SE') and ano = 2000

SELECT ano, sigla_uf, taxa_criancas_fora_escola_4_5, taxa_criancas_fora_escola_6_14, pea_10_14, pea_15_17, pia_10_14, pia_15_17, (pea_10_14/ pia_10_14) * 100 AS PorcPeaPia10_14, (pea_15_17/ pia_15_17) * 100 AS PorcPeaPia15_17	 FROM `basedosdados.mundo_onu_adh.uf` where sigla_uf in ('MS','MT','GO') and ano = 2010

SELECT ano, sigla_uf, taxa_criancas_fora_escola_4_5, taxa_criancas_fora_escola_6_14, pea_10_14, pea_15_17, pia_10_14, pia_15_17, (pea_10_14/ pia_10_14) * 100 AS PorcPeaPia10_14, (pea_15_17/ pia_15_17) * 100 AS PorcPeaPia15_17	 FROM `basedosdados.mundo_onu_adh.uf` where sigla_uf in ('RJ','SP','ES', 'MG') and ano = 2010

SELECT ano, sigla_uf, taxa_criancas_fora_escola_4_5, taxa_criancas_fora_escola_6_14, pea_10_14, pea_15_17, pia_10_14, pia_15_17, (pea_10_14/ pia_10_14) * 100 AS PorcPeaPia10_14, (pea_15_17/ pia_15_17) * 100 AS PorcPeaPia15_17	 FROM `basedosdados.mundo_onu_adh.uf` where sigla_uf in ('AC','AM','PA','RR','RO','AP','TO') and ano = 2010

SELECT ano, sigla_uf, taxa_criancas_fora_escola_4_5, taxa_criancas_fora_escola_6_14, pea_10_14, pea_15_17, pia_10_14, pia_15_17, (pea_10_14/ pia_10_14) * 100 AS PorcPeaPia10_14, (pea_15_17/ pia_15_17) * 100 AS PorcPeaPia15_17	 FROM `basedosdados.mundo_onu_adh.uf` where sigla_uf in ('SC','PR','RS') and ano = 2010

SELECT ano, sigla_uf, taxa_criancas_fora_escola_4_5, taxa_criancas_fora_escola_6_14, pea_10_14, pea_15_17, pia_10_14, pia_15_17, (pea_10_14/ pia_10_14) * 100 AS PorcPeaPia10_14, (pea_15_17/ pia_15_17) * 100 AS PorcPeaPia15_17	 FROM `basedosdados.mundo_onu_adh.uf` where sigla_uf in ('AL','BA','CE','MA','PA','PB','PI','RN','SE') and ano = 2010