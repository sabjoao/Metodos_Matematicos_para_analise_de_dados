# -*- coding: utf-8 -*-
# #####################################################################
#  CONSULTA PARA A PROVA - ANALISE DE DADOS (XMAC02)
#  Resumo das funcoes usadas nos notebooks (.ipynb) das aulas 1 a 13
#
#  ATENCAO: este arquivo NAO foi feito para rodar inteiro de uma vez
#  (varios blocos dependem de arquivos .csv). Copie o bloco que precisar
#  para o notebook e troque os nomes de colunas/arquivos.
# #####################################################################


# =====================================================================
# IMPORTS PADRAO (colocar sempre na primeira celula)
# =====================================================================
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statistics as st
from scipy.stats import binom, poisson, norm, expon


# =====================================================================
# AULA 2a - LISTAS
# =====================================================================

# --- Criando uma lista ---
l = []                      # lista vazia
l = [1, 2, 3, 4, 5]
l2 = [7, 2.5, 'Data']       # lista pode misturar tipos
ll = [[1, 2, 3], ["um", "dois", "tres"]]   # lista de listas
ll[1][2]                    # acessa 'tres'

# --- Acessando elementos e fatiando (sublista) ---
l[1]          # segundo elemento (indice comeca em 0)
l[-1]         # ultimo elemento
l[1:4]        # do indice 1 ate o 3 (o 4 nao entra)
l[:3]         # 3 primeiros
l[-3:]        # 3 ultimos

# --- Alterando, adicionando e removendo ---
l[1] = 'um'             # substitui elemento
l.append(6)             # adiciona no final
l.insert(0, 'abacate')  # insere na posicao 0
elem = l.pop()          # remove e retorna o ultimo
elem = l.pop(0)         # remove e retorna o do indice 0
l.remove('um')          # remove pelo VALOR

# --- Metodos uteis de lista ---
lista = [12, 8, 15, 10, 12, 6, 19, 23, 7, 8, 14, 12, 20, 4, 14, 12, 8, 25, 21, 11]
max(lista)              # maior elemento
min(lista)              # menor elemento
sum(lista)              # soma
len(lista)              # tamanho
lista.count(12)         # quantas vezes o 12 aparece
lista.sort()            # ordena (altera a propria lista)
lista.reverse()         # inverte
listaAux = lista.copy() # copia independente
frutas = ['banana', 'pera'] * 3   # repete a lista 3 vezes

# --- Elemento do meio da lista ---
meio = len(lista) // 2
lista[meio]

# --- Segundo maior elemento ---
listaAux = sorted(lista)
listaAux[-2]

# --- Trocar primeiro e ultimo elemento ---
lista[0], lista[-1] = lista[-1], lista[0]

# --- Gerando listas com range ---
list(range(10))          # 0..9
list(range(10, 20))      # 10..19
list(range(10, 100, 5))  # 10, 15, ..., 95 (passo 5)

# --- Percorrendo lista com for (lista numerada) ---
nomes = ['edu', 'gaspar', 'ana', 'maria']
for i, nome in enumerate(nomes, start=1):
    print(str(i) + '-' + nome)

# --- Separando pares e impares ---
pares, impares = [], []
for x in lista:
    if x % 2 == 0:
        pares.append(x)
    else:
        impares.append(x)


# =====================================================================
# AULA 2b - DICIONARIOS, TUPLAS E SETS
# =====================================================================

# --- Criando dicionario (chave: valor) ---
dic = {'Brasil': 'portugues', 'EUA': 'ingles', 'Egito': 'arabe'}
dic['Egito']        # acessa pelo nome da chave
dic.keys()          # todas as chaves
dic.values()        # todos os valores
dic.items()         # pares (chave, valor)
dic['Mexico'] = 'espanhol'   # adiciona nova chave

# --- Verificando se uma chave existe ---
telefones = {'Pedro': '11111 1111', 'Ana': '22222 2222'}
nome = 'Ana'
if nome in telefones:
    print('telefone: ' + telefones[nome])
else:
    print('nao existe')

# --- Tupla (lista imutavel) e Set (sem repeticao) ---
t = (1, 2, 3)
s = {1, 3, 3, 4, 5, 6}     # vira {1, 3, 4, 5, 6}


# =====================================================================
# AULA 3 (+ AULA 1) - ESTATISTICA DESCRITIVA
# =====================================================================

# --- Media, mediana, moda com o modulo statistics ---
valores = [1, 2, 3, 3]
sum(valores) / len(valores)   # media "na mao"
st.mean(valores)              # media
st.median(valores)            # mediana
st.mode(valores)              # moda

# --- Amplitude, desvio padrao e variancia ---
amplitude = max(valores) - min(valores)
st.stdev(valores)             # desvio padrao (amostral)
st.variance(valores)          # variancia (amostral)

# --- Quartis e amplitude interquartil (IQR) ---
q = st.quantiles([70, 85, 90, 98, 104, 105, 107])   # retorna [Q1, Q2, Q3]
iqr = q[2] - q[0]

# --- Estatistica de uma coluna do DataFrame (pandas) ---
df = sns.load_dataset('tips')
df['tip'].mean()        # media
df['tip'].median()      # mediana
df['tip'].mode()        # moda
df['tip'].std()         # desvio padrao
df['tip'].var()         # variancia
df['tip'].quantile([0.25, 0.5, 0.75])   # quartis
st.quantiles(df['tip'])                 # quartis com statistics

# --- Media / desvio de um grupo filtrado ---
titanic = sns.load_dataset('titanic')
titanic[titanic['sex'] == 'male']['age'].mean()
titanic[titanic['sex'] == 'female']['age'].std()

# --- Criando boxplot de uma coluna ---
df.boxplot(column='tip')
plt.show()

# --- Criando boxplot agrupado por outra coluna ---
df.boxplot(column='total_bill', by='sex')
plt.show()

# --- Boxplot com seaborn (varias categorias) ---
plt.figure(figsize=(10, 8))
sns.boxplot(data=df, x='day', y='total_bill')
plt.title('Conta por dia')
plt.show()

# --- Boxplot comparando so algumas categorias (filtro com isin) ---
# dfGen = df[df['genre'].isin(['Animation', 'Comedy', 'Drama'])]
# sns.boxplot(data=dfGen, x='genre', y='score')


# =====================================================================
# AULA 4a - NUMPY: CRIANDO ARRAYS
# =====================================================================

# --- Criando array a partir de lista ---
b = np.array([1, 2, 3])

# --- arange (como o range) ---
c = np.arange(0, 10)            # 0..9
dezenas = np.arange(0, 101, 10) # 0, 10, ..., 100

# --- linspace (inicio, fim, QUANTIDADE de itens, incluindo o fim) ---
d = np.linspace(0, 3, 31)       # 0.0, 0.1, ..., 3.0
arr = np.linspace(-3.0, 3.0, 61)

# --- Matriz (array 2D) ---
g = np.array([[1, 2, 3], [10, 20, 30]])

# --- Matriz de zeros e de uns (dimensao como tupla) ---
np.zeros((3, 4))
np.ones((4, 3))

# --- Mudando formato com reshape ---
num30 = np.arange(0, 30)
num30.shape                 # (30,)
mat = num30.reshape(3, 10)  # 3 linhas x 10 colunas
mat.reshape(-1)             # volta para 1D ("achata")


# =====================================================================
# AULA 4b - NUMPY: SELECIONANDO ELEMENTOS
# =====================================================================

arr1 = np.arange(1, 10)
arr1[4]       # elemento de indice 4
arr1[2:5]     # indices 2, 3 e 4
arr1[:4]      # 4 primeiros
arr1[-4:]     # 4 ultimos

# --- Selecionando em matriz [linha, coluna] ---
mat1 = np.arange(0, 30).reshape(3, 10)
mat1[1]            # segunda linha
mat1[2, 5]         # elemento linha 2, coluna 5 (=25)
mat1[0:3, 1:3]     # colunas 1 e 2 de todas as linhas
mat2 = np.arange(1, 41).reshape(4, 10)
mat2[1:3, 3:7]     # "miolo" da matriz

# --- Filtro por condicao (mascara booleana) ---
dezenas >= 60             # array de True/False
dezenas[dezenas >= 60]    # so os elementos >= 60


# =====================================================================
# AULA 4c - NUMPY: OPERACOES COM ARRAYS
# =====================================================================

arr1 = np.arange(0, 10)
arr2 = np.arange(10, 20)
arr1 + 10          # soma 10 em todos (sem laco)
arr1 + arr2        # soma elemento a elemento
arr1 * 2

# --- Alterando elementos ---
arr1[0] = 10       # um elemento
arr1[:5] = 20      # 5 primeiros
arr1[7:] = 30      # 3 ultimos
arr1[:] = 10       # todos

# --- CUIDADO: fatia e uma "view" (altera o original) ---
arr3 = arr2[:5]
arr3[:] = 0        # arr2 tambem muda!
arr3 = arr2[:5].copy()   # use copy() para nao alterar o original

# --- Juntando arrays ---
np.append(np.arange(0, 10), np.arange(10, 20))

# --- Numeros aleatorios inteiros ---
rng = np.random.default_rng()
rng.integers(low=1, high=101, size=20)   # 20 inteiros de 1 a 100
5 in arr1                                # verifica se valor esta no array


# =====================================================================
# AULA 5 - PROBABILIDADE (SIMULACAO)
# =====================================================================

# --- Simulando moeda com numeros aleatorios ---
np.random.rand(5)            # 5 numeros entre 0 e 1
np.random.rand(5) > 0.5      # True = cara, False = coroa
np.random.randint(0, 2, 10)  # 10 lancamentos com 0 ou 1 (o 2 nao entra)
sum(np.random.randint(0, 2, 10))   # quantas caras

# --- Simulando dado ---
np.random.randint(1, 7, 10)  # 10 lancamentos de dado (1 a 6)

# --- Grafico de contagem dos resultados ---
a = np.random.randint(1, 7, 600000)
sns.countplot(x=a)
plt.show()

# --- Probabilidade de a soma de 2 dados ser > 7 (simulacao) ---
dado1 = np.random.randint(1, 7, 1000000)
dado2 = np.random.randint(1, 7, 1000000)
soma = dado1 + dado2
sum(soma > 7) / len(soma)    # ~0.4166
np.mean(soma > 7)            # mesma coisa

# --- Uniao de eventos: P(A u B) = P(A) + P(B) - P(A n B) ---
P_A, P_B, P_AuB = 0.35, 0.46, 0.59
P_AnB = P_A + P_B - P_AuB    # probabilidade de ambos


# =====================================================================
# AULA 6 - DISTRIBUICAO BINOMIAL  binom(k, n, p)
#   k = nro de sucessos, n = nro de tentativas, p = prob. de sucesso
# =====================================================================

# --- Simulando lancamentos (np.random.binomial(n, p, qtd)) ---
np.random.binomial(1, 0.5)            # 1 moeda
np.random.binomial(2, 0.5)            # 2 moedas (nro de caras)
resultado = np.random.binomial(2, 0.5, 1000)   # 1000 jogadas de 2 moedas
sns.set_theme(style="whitegrid")
sns.countplot(x=resultado)
plt.show()

# --- Probabilidade EXATAMENTE k: pmf ---
binom.pmf(2, 20, 0.12)        # exatamente 2 defeituosas em 20, p=12%
binom.pmf(7, 10, 0.5)         # exatamente 7 caras em 10 lancamentos

# --- Probabilidade ATE k (<= k): cdf ---
binom.cdf(2, 20, 0.12)        # 2 ou menos defeituosas (= pmf(0)+pmf(1)+pmf(2))

# --- Probabilidade MAIS QUE k (> k): sf ---
binom.sf(1, 20, 0.12)         # > 1, ou seja, 2 ou mais
1 - binom.cdf(1, 20, 0.12)    # mesma coisa
binom.sf(6, 10, 0.5)          # 7 ou MAIS caras -> usar k-1 !!

# --- Media, desvio padrao e variancia ---
binom.mean(20, 0.12)          # n*p
binom.std(20, 0.12)
binom.var(20, 0.12)           # n*p*(1-p)

# --- Numero esperado (ex: 500 alunos chutando prova) ---
prob = binom.sf(8, 14, 0.25)  # 9 ou mais acertos em 14 questoes, 4 opcoes
esperado = prob * 500

# --- Grafico da distribuicao de probabilidade (pmf) ---
eixoX = np.arange(0, 21)                 # 0..20 sucessos
eixoY = binom.pmf(eixoX, 20, 0.12)
sns.barplot(x=eixoX, y=eixoY)
plt.show()

# --- Imprimindo a tabela de probabilidades formatada ---
for i in range(21):
    print(f'{i} - {eixoY[i]:.2f}')

# --- Grafico da probabilidade acumulada (cdf) ---
eixoY2 = binom.cdf(eixoX, 20, 0.12)
sns.barplot(x=eixoX, y=eixoY2)
plt.show()


# =====================================================================
# AULA 7 - DISTRIBUICAO DE POISSON  poisson(k, mu)
#   mu = media de ocorrencias NO INTERVALO pedido
# =====================================================================

# --- Simulando ---
np.random.poisson(3.6)             # 1 valor
np.random.poisson(3.6, 10)         # 10 valores
tam_fila = np.random.poisson(3.6, 1000000)
sns.countplot(x=tam_fila)
plt.show()

# --- Probabilidades ---
poisson.pmf(7, 3.6)     # EXATAMENTE 7
poisson.cdf(7, 3.6)     # 7 ou MENOS
poisson.sf(6, 4.6)      # MAIS que 6 (7 ou mais)

# --- Media, variancia, desvio (media = variancia = mu) ---
poisson.mean(3.6)
poisson.var(3.6)
poisson.std(3.6)

# --- Ajustando mu para outro intervalo (regra de 3) ---
# 1.81 meteoros a cada 30s -> em 60s mu = 1.81*2 ; em 120s mu = 1.81*4
poisson.pmf(0, 1.81 * 2)                       # nenhum em 1 minuto
intervalo = np.arange(5, 9)                    # 5, 6, 7, 8
sum(poisson.pmf(intervalo, 1.81 * 4))          # entre 5 e 8 (inclusive)
poisson.cdf(8, 7.24) - poisson.cdf(4, 7.24)    # mesma coisa

# --- Capacidade excedida (20 ou mais em 5 min, 180 chamadas/h) ---
mu = (180 / 60) * 5                # 15 chamadas em 5 min
poisson.sf(19, mu)                 # P(X >= 20)

# --- Valor minimo para garantir 99% (inverso da cdf): ppf ---
poisson.ppf(0.99, 15)              # capacidade minima

# --- Grafico pmf e cdf ---
eixo_x = np.arange(0, 15)
eixo_y = poisson.pmf(eixo_x, 3.6)
sns.barplot(x=eixo_x, y=eixo_y)
plt.show()
eixo_y = poisson.cdf(eixo_x, 3.6)
sns.barplot(x=eixo_x, y=eixo_y)
plt.show()


# =====================================================================
# AULA 8 (+ AULA 1) - PANDAS: SERIES E DATAFRAMES
# =====================================================================

# --- Criando Series (vetor com rotulos) ---
dias = ['Segunda', 'Terca', 'Quarta', 'Quinta', 'Sexta']
gastos = [44, 47, 35, 52, 60]
gastos_dia = pd.Series(gastos, dias)
gastos_dia['Terca']

# --- Criando DataFrame a partir de matriz ---
mat = np.arange(1, 10).reshape(3, 3)
df = pd.DataFrame(mat, index=['linha1', 'linha2', 'linha3'],
                  columns=['col1', 'col2', 'col3'])

# --- Criando DataFrame a partir de dicionario ---
df = pd.DataFrame({'Col A': [1, 2, 3], 'Col B': [4, 5, 6]},
                  index=['primeira', 'segunda', 'terceira'])
pd.DataFrame({'Temperatura': [28, 25, 21]}, index=['Dom', 'Seg', 'Ter'])

# --- Lendo CSV ---
# df = pd.read_csv('arquivo.csv')
# df = pd.read_csv('Piece_Dim.csv', index_col='Item_No')   # coluna como indice
# df = pd.read_csv('student-por.csv', sep=';')             # separador ;
# df = pd.read_csv('CPI_2014.csv', encoding='latin-1')     # erro de acento
df = sns.load_dataset('titanic')      # datasets prontos: titanic, tips, taxis

# --- Explorando o DataFrame ---
df.head()          # 5 primeiras linhas (df.head(10) -> 10)
df.tail()          # 5 ultimas
df.shape           # (linhas, colunas)  -> SEM parenteses
df.dtypes          # tipo de cada coluna
df.info()          # resumo (tipos + nao nulos)
df.describe()      # estatisticas de todas as colunas numericas
df.isnull().sum()  # quantidade de dados faltando por coluna
df.columns         # nomes das colunas
df['sex'].unique()         # valores distintos
df['sex'].value_counts()   # contagem de cada valor

# --- Selecionando colunas ---
df['age']                  # uma coluna (Series)
df[['age']]                # uma coluna (DataFrame)
df[['age', 'fare']]        # varias colunas

# --- Renomeando colunas ---
df.rename(columns={'age': 'Idade', 'fare': 'Tarifa'}, inplace=True)

# --- Criando nova coluna a partir de outras ---
# df['Volume'] = round(df['Comprimento'] * df['Largura'] * df['Altura'], 2)
# df['lucro'] = df['gross'] - df['budget']

# --- Removendo coluna ---
# df = df.drop('Volume', axis=1)          # axis=1 -> coluna ; axis=0 -> linha

# --- loc (pelo NOME do indice) e iloc (pela POSICAO) ---
# df.loc[['Item-1', 'Item-5']]
# df.loc[['Item-1', 'Item-5'], ['Comprimento', 'Largura']]
df.iloc[[0]]               # primeira linha
df.iloc[[0, 4], [0, 1, 2]] # linhas 0 e 4, colunas 0..2
df.iloc[:5, [0, 1, 2]]     # 5 primeiras linhas
df.iloc[:, :2]             # todas as linhas, 2 primeiras colunas

# --- Filtrando linhas por condicao ---
df = sns.load_dataset('titanic')
df[df['age'] > 30]
df[(df['age'] > 30) & (df['sex'] == 'male')]      # E  -> &
df[(df['age'] >= 60) | (df['fare'] >= 100)]       # OU -> |
df[df['embark_town'] != 'Southampton']            # diferente
df[df['class'].isin(['First', 'Second'])]         # esta na lista
df[(df['age'] > 20) & (df['age'] < 30)]           # entre dois valores
# Sempre coloque parenteses em cada condicao!

# --- Filtro + estatistica numa linha ---
df[df['sex'] == 'female']['age'].mean()

# --- Ordenando ---
df.sort_values('fare', ascending=False).head(5)       # 5 maiores
df.sort_values(by=['class', 'fare'])
df.nlargest(10, 'fare')                               # 10 maiores
df.nsmallest(10, 'fare')                              # 10 menores

# --- Busca de texto dentro da coluna (str.contains) ---
# filt = df['LanguageHaveWorkedWith'].str.contains('Python', na=False)
# df.loc[filt].shape[0]      # quantos contem 'Python'

# --- Coluna como indice + converter texto para numero ---
# dfGdp.set_index('Country', inplace=True)
# dfGdp = dfGdp.replace(',', '', regex=True)   # tira virgulas
# dfGdp = dfGdp.astype(float)
# dfGdp.loc['Brazil']                          # linha do Brasil


# =====================================================================
# AULA 9 - GRAFICOS DE PIZZA
# =====================================================================

# --- Configuracoes gerais de tamanho/estilo ---
plt.rcParams['figure.figsize'] = [8, 6]
sns.set_style('darkgrid')

# --- Criando grafico de pizza simples ---
# sierra = df[df['Countries'] == 'Sierra Leone']
# sizes = sierra['Death'] ; labels = sierra['Type']
sizes = [30, 50, 20]
labels = ['A', 'B', 'C']
plt.pie(sizes, labels=labels)
plt.title('Grafico de pizza')
plt.axis('equal')          # deixa redondo
plt.show()

# --- Pizza com porcentagem, sombra e angulo inicial ---
plt.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
plt.title('Grafico de pizza com %')
plt.axis('equal')
plt.show()

# --- Pizza a partir da contagem de uma coluna (value_counts) ---
df = sns.load_dataset('titanic')
contagem = df['class'].value_counts()
plt.figure(figsize=(8, 6))
plt.pie(contagem, labels=contagem.index, autopct='%1.1f%%')
plt.title('Porcentagem por classe')
plt.show()

# --- Pizza de sobreviventes x nao sobreviventes ---
sobrev = (df['survived'] == 1).sum()
nao_sobrev = (df['survived'] == 0).sum()
plt.pie([sobrev, nao_sobrev], labels=['Sobreviveu', 'Nao sobreviveu'],
        autopct='%1.1f%%', shadow=True, startangle=90)
plt.show()

# --- Dois graficos de pizza LADO A LADO (subplot(linhas, colunas, posicao)) ---
eua = df[df['embark_town'] == 'Southampton']
outros = df[df['embark_town'] != 'Southampton']
sizes1 = [eua.shape[0], outros.shape[0]]          # quantidade
sizes2 = [eua['fare'].sum(), outros['fare'].sum()]  # soma de valores
labels = ['Southampton', 'Outros']

plt.rcParams['figure.figsize'] = [12, 6]
plt.subplot(1, 2, 1)
plt.pie(sizes1, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
plt.title('Quantidade')
plt.subplot(1, 2, 2)
plt.pie(sizes2, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
plt.title('Valor total pago')
plt.tight_layout()
plt.show()


# =====================================================================
# AULA 9/10 - GRAFICOS DE BARRAS E DE AREA (EMPILHADOS)
# =====================================================================

# --- Criando grafico de barras direto do DataFrame ---
dfb = pd.DataFrame({'Categorias': ['A', 'B', 'C', 'D'], 'Valores': [10, 15, 20, 7]})
plt.rcParams['figure.figsize'] = [8, 6]
dfb.plot(kind='bar', x='Categorias', y='Valores', legend=False)
plt.xlabel('Categorias')
plt.ylabel('Valores')
plt.title('Grafico de barras')
plt.show()

# --- Barras horizontais ---
dfb.plot(kind='barh', x='Categorias', y='Valores')
plt.show()

# --- Barras de uma Series (ex: PIB do Brasil por ano) ---
# dfGdp.loc['Brazil'].plot(kind='bar')

# --- Top N em grafico (ex: 10 maiores e ordenados) ---
tips = sns.load_dataset('tips')
top10 = tips.nlargest(10, 'total_bill').sort_values('tip', ascending=False)
top10.plot(x='day', y='tip', kind='bar')
plt.title('Gorjeta das 10 maiores contas')
plt.show()

# --- Barras com seaborn (faz a MEDIA automaticamente) ---
sns.barplot(data=tips, x='day', y='total_bill')
plt.show()

# --- Barras agrupadas com seaborn (hue = cor por categoria) ---
sns.barplot(data=tips, x='day', y='total_bill', hue='sex')
plt.show()

# --- Barras empilhadas a partir de crosstab ---
# summary = pd.crosstab(df['Year'], df['Crime'], values=df['Rate'], aggfunc='sum')
summary = pd.crosstab(tips['day'], tips['time'], values=tips['total_bill'], aggfunc='sum')
summary.plot(kind='bar', stacked=True)
plt.title('Barras empilhadas')
plt.show()

# --- Grafico de AREA empilhada ---
summary.plot(kind='area', stacked=True)
plt.title('Area empilhada')
plt.xlabel('Dia')
plt.ylabel('Total')
plt.show()

# --- Ajustando tamanho de fonte (set_context) ---
sns.set_context("notebook", font_scale=1.2,
                rc={"font.size": 12, "axes.titlesize": 16, "axes.labelsize": 12})

# --- Barras usando ax (titulo, rotacao dos rotulos) ---
ax = tips.groupby('day')['tip'].mean().plot(kind='bar', figsize=(8, 4))
ax.set_title('Gorjeta media por dia')
ax.set_xlabel('Dia')
ax.set_ylabel('Media')
ax.tick_params(axis='x', rotation=0)   # rotulos na horizontal
plt.tight_layout()
plt.show()


# =====================================================================
# AULA 9 - GRAFICO DE DISPERSAO (SCATTER)
# =====================================================================

# --- Criando grafico de dispersao ---
plt.rcParams['figure.figsize'] = [8, 6]
sns.scatterplot(data=tips, x='total_bill', y='tip')
plt.title('Conta x Gorjeta')
plt.show()

# --- Com matplotlib ---
plt.scatter(tips['total_bill'], tips['tip'])
plt.xlabel('Conta')
plt.ylabel('Gorjeta')
plt.show()

# --- Dispersao com cor por categoria ---
sns.scatterplot(data=tips, x='total_bill', y='tip', hue='sex')
plt.show()

# --- Removendo outlier e plotando de novo ---
# df2 = df[df['Pressao'] < 220]
tips2 = tips[tips['tip'] < 8]
sns.scatterplot(data=tips2, x='total_bill', y='tip')
plt.show()


# =====================================================================
# AULA 1 / AULA 10 - HISTOGRAMAS
# =====================================================================

# --- Histograma de todas as colunas numericas ---
df = sns.load_dataset('titanic')
df.hist(figsize=(16, 8))
plt.show()

# --- Histograma de uma coluna (bins = nro de barras) ---
df.hist(column='age', bins=8)
plt.show()

# --- Histograma com seaborn + linha vertical de referencia ---
sns.displot(df['age'], kde=False, bins=15)
plt.title('Idade dos passageiros')
plt.xlabel('Idade')
plt.axvline(60, color='k', linestyle='--')   # linha vertical em x=60
plt.show()

sns.histplot(df['age'], bins=15, kde=True)   # kde=True desenha a curva
plt.show()

# --- Histograma so de um grupo (filtro antes) ---
# df2 = df[df['Continent'] == 'Europe']
# sns.displot(df2['CPI_2014'], kde=False, bins=15)

# --- DOIS histogramas LADO A LADO ---
homens = df[df['sex'] == 'male']
mulheres = df[df['sex'] == 'female']
fig, axes = plt.subplots(1, 2, figsize=(12, 5))
sns.histplot(homens['age'], bins=15, ax=axes[0])
axes[0].set_title('Homens')
sns.histplot(mulheres['age'], bins=15, ax=axes[1])
axes[1].set_title('Mulheres')
plt.tight_layout()
plt.show()

# (alternativa com plt.subplot)
plt.subplot(1, 2, 1)
plt.hist(homens['age'].dropna(), bins=15)
plt.title('Homens')
plt.subplot(1, 2, 2)
plt.hist(mulheres['age'].dropna(), bins=15)
plt.title('Mulheres')
plt.tight_layout()
plt.show()


# =====================================================================
# AULA 1 - GRAFICO DE CONTAGEM (COUNTPLOT)
# =====================================================================

# --- Contagem de uma coluna categorica ---
sns.countplot(x='alive', data=df)
plt.show()

# --- Contagem separada por outra categoria (hue) ---
sns.countplot(x='sex', hue='alive', data=df)
plt.show()
sns.countplot(x='pclass', hue='alive', data=df)
plt.show()


# =====================================================================
# AULA 10 - GRAFICO DE LINHAS
# =====================================================================

# --- Linha a partir de coluna(s) do DataFrame ---
# df[['Close TSLA', 'Close AAPL']].plot()     # evolucao de acoes (yfinance)
plt.rcParams['figure.figsize'] = [10, 8]
sns.set_style('darkgrid')
serie = tips.groupby('size')['tip'].mean()
serie.plot(kind='line', marker='o', linewidth=2, figsize=(8, 4))
plt.title('Gorjeta media por tamanho da mesa')
plt.xlabel('Pessoas na mesa')
plt.ylabel('Gorjeta media')
plt.show()

# --- Linha com seaborn ---
sns.lineplot(x=serie.index, y=serie.values)
plt.show()

# --- Barras lado a lado de duas colunas (ex: expectativa homens x mulheres) ---
# df3.head(15).plot(x='Countries', kind='bar', stacked=False)


# =====================================================================
# AULA 11 - CROSSTAB (TABELA CRUZADA)
#   pd.crosstab(linhas, colunas, values=, aggfunc=, margins=, normalize=)
# =====================================================================

dfc = pd.DataFrame({
    'gender': ['male', 'male', 'female', 'female', 'male', 'female', 'male', 'female'],
    'education_level': ['high school', 'college', 'college', 'graduate',
                        'high school', 'graduate', 'college', 'graduate'],
    'score': [75, 82, 88, 95, 69, 92, 78, 85]
})

# --- Crosstab simples (contagem) ---
ct = pd.crosstab(dfc['gender'], dfc['education_level'])   # 1o = linhas, 2o = colunas

# --- Crosstab agregando valores (media, soma...) ---
pd.crosstab(dfc['gender'], dfc['education_level'], values=dfc['score'], aggfunc='mean')
# aggfunc pode ser: 'sum', 'mean', 'max', 'min', 'median', 'std', 'var', 'count'

# --- Crosstab com totais (margins) ---
pd.crosstab(dfc['gender'], dfc['education_level'], margins=True)
pd.crosstab(dfc['gender'], dfc['education_level'], margins=True, margins_name='Total')

# --- Crosstab com nomes das linhas/colunas ---
taxis = sns.load_dataset('taxis')
pd.crosstab(taxis['payment'], taxis['pickup_borough'],
            rownames=['Payment Method'], colnames=['Locais'])

# --- Soma dos valores com total geral ---
pd.crosstab(taxis['payment'], taxis['pickup_borough'],
            values=taxis['total'], aggfunc='sum', margins=True)

# --- Normalizando (proporcoes) ---
pd.crosstab(dfc['gender'], dfc['education_level'], normalize=True)      # pelo total geral
pd.crosstab(dfc['gender'], dfc['education_level'], normalize='index')   # cada LINHA soma 1
pd.crosstab(dfc['gender'], dfc['education_level'], normalize='columns') # cada COLUNA soma 1
pd.crosstab(taxis['payment'], taxis['pickup_borough'],
            values=taxis['total'], aggfunc='sum', normalize=True)       # % dos valores

# --- Exibindo em percentual com 1 casa decimal ---
prop = pd.crosstab(dfc['gender'], dfc['education_level'], normalize='index')
perc = prop.mul(100)                     # vira porcentagem
perc.round(1).astype(str) + '%'

# --- Mapa de calor (heatmap) da crosstab ---
sns.heatmap(ct, cmap='coolwarm', annot=True)   # annot mostra os numeros
plt.show()

# --- Barras empilhadas da crosstab ---
ct.plot(kind='bar', stacked=True)
plt.show()

# --- Barras empilhadas em % (0 a 100) ---
ax = perc.plot(kind='bar', stacked=True, figsize=(9, 5))
ax.set_ylim(0, 100)
ax.legend(title='Nivel')
plt.show()

# --- Barras agrupadas (nao empilhadas), tirando a linha/coluna Total ---
tab = pd.crosstab(dfc['gender'], dfc['education_level'], margins=True, margins_name='Total')
tab_sem_total = tab.drop(index='Total', columns='Total')
ax = tab_sem_total.plot(kind='bar', figsize=(8, 4))
ax.tick_params(axis='x', rotation=0)
plt.show()


# =====================================================================
# AULA 11 - GROUPBY (AGRUPAR E AGREGAR)
# =====================================================================

dfg = pd.DataFrame({'Company': ['GOOG', 'GOOG', 'MSFT', 'MSFT', 'META', 'META'],
                    'Person': ['Sam', 'Charlie', 'Amy', 'Vanessa', 'Carl', 'Sarah'],
                    'Sales': [200, 120, 340, 124, 243, 350]})

# --- Agrupando e calculando media / soma / contagem ---
dfg.groupby('Company')[['Sales']].mean()
dfg.groupby('Company')[['Sales']].sum()
dfg.groupby('Company')['Sales'].count()
dfg.groupby('Company').describe()          # contagem, media, desvio, quartis...

# --- Agrupando por DUAS colunas + reset_index (vira DataFrame normal) ---
mean_tips = tips.groupby(['day', 'sex'])['total_bill'].mean().reset_index()
sns.barplot(x='day', y='total_bill', hue='sex', data=mean_tips)
plt.title('Valor medio da conta por dia e sexo')
plt.show()

# --- Varias medidas com nomes claros (agg) ---
resumo = tips.groupby('size').agg(
    quantidade=('tip', 'size'),
    media_gorjeta=('tip', 'mean'),
)
resumo.round(2)

# --- Trocando codigos numericos por nomes (rename com dicionario) ---
# nomes_estacoes = {1: 'Primavera', 2: 'Verao', 3: 'Outono', 4: 'Inverno'}
# media = bike_day.groupby('season')['cnt'].mean().rename(index=nomes_estacoes)
# media.plot(kind='bar')

# --- Contagem por categoria + grafico ---
# df.groupby('continent')['id'].count().plot(kind='bar')
tips.groupby('day').size().plot(kind='bar')
plt.show()


# =====================================================================
# AULA 12 - DISTRIBUICAO NORMAL  norm(x, loc=media, scale=desvio)
# =====================================================================

mu, sigma = 100, 2      # barras de aco: media 100 mm, desvio 2 mm

# --- Simulando valores ---
np.random.normal(mu, sigma)                     # 1 barra
np.round(np.random.normal(mu, sigma, 10), 2)    # 10 barras, 2 casas decimais
barras = np.random.normal(mu, sigma, 1000000)
sns.histplot(barras, bins=50)
plt.show()

# --- Regra 68 - 95 - 99.7 (verificando na simulacao) ---
np.mean((barras > mu - sigma) & (barras < mu + sigma))          # ~0.68
np.mean((barras > mu - 2*sigma) & (barras < mu + 2*sigma))      # ~0.95
np.mean((barras > mu - 3*sigma) & (barras < mu + 3*sigma))      # ~0.997

# --- Probabilidades ---
norm.cdf(153, 150, 2)                         # P(X <= 153)  (menos que)
norm.sf(153, 150, 2)                          # P(X > 153)   (mais que)
norm.cdf(152, 150, 2) - norm.cdf(148, 150, 2) # P(148 < X < 152) (ENTRE)
norm.pdf(150, 150, 2)                         # densidade no ponto (altura da curva)
# Obs: na normal (continua) P(X = valor exato) = 0.
#      Se a medida tem precisao (ex: centesimos), "64 kg" = entre 63.995 e 64.005

# --- Valor para uma porcentagem (inverso): ppf ---
norm.ppf(0.01, 8.2, 1.1)      # garantia: so 1% falha antes desse tempo
norm.ppf(0.95, 36.8, 0.35)    # temperatura acima da qual ficam so 5%

# --- Quantidade de pessoas (multiplicar pela populacao) ---
n = 500
n * (norm.cdf(77.5, 75.5, 7.5) - norm.cdf(60, 75.5, 7.5))   # entre 60 e 77.5 kg

# --- Media, variancia, desvio ---
norm.mean(150, 2)
norm.var(150, 2)
norm.std(150, 2)

# --- Grafico da curva normal (densidade) ---
eixoX = np.linspace(150 - 3*2, 150 + 3*2, 1000)    # de -3 sigma a +3 sigma
eixoY = norm.pdf(eixoX, 150, 2)
sns.lineplot(x=eixoX, y=eixoY)
plt.xlabel('Volume (ml)')
plt.ylabel('Densidade')
plt.show()

# --- Pintando a area entre dois valores ---
plt.plot(eixoX, eixoY)
faixa = (eixoX >= 148) & (eixoX <= 152)
plt.fill_between(eixoX[faixa], eixoY[faixa], alpha=0.4)
plt.show()


# =====================================================================
# AULA 13 - DISTRIBUICAO EXPONENCIAL  expon(x, scale=1/lambda)
#   lambda = taxa (eventos por unidade de tempo); media = 1/lambda
#   ATENCAO: numpy e scipy usam scale = MEDIA = 1/lambda
# =====================================================================

lamb = 3.6 / 10          # 3.6 clientes a cada 10 min -> 0.36 por minuto
media = 1 / lamb         # ~2.78 minutos entre chegadas

# --- Simulando tempos de espera ---
np.random.exponential(scale=media)              # 1 tempo
np.random.exponential(scale=media, size=10)     # 10 tempos
tempos = np.random.exponential(scale=media, size=1000)
sns.histplot(tempos, bins=30)
plt.xlabel('tempo de espera em minutos')
plt.ylabel('frequencia')
plt.show()

# --- Probabilidades ---
expon.cdf(5, scale=media)                              # P(T < 5)  (menos que)
expon.sf(5, scale=media)                               # P(T > 5)  (mais que)
expon.cdf(5, scale=media) - expon.cdf(2, scale=media)  # P(2 < T < 5) (entre)
expon.pdf(5, scale=media)                              # densidade no ponto

# --- Tempo para uma porcentagem (inverso): ppf ---
t95 = expon.ppf(0.95, scale=1/4)   # 4 req/min: tempo com 95% de chance

# --- Media, variancia, desvio ---
expon.mean(scale=media)
expon.var(scale=media)
expon.std(scale=media)

# --- Cuidado com unidades (ex: 6 chamadas por HORA, pergunta em MINUTOS) ---
lamb_min = 6 / 60                        # 0.1 chamada por minuto
expon.cdf(5, scale=1/lamb_min)           # proxima chamada em menos de 5 min

# --- Grafico da densidade (pdf) e acumulada (cdf) ---
eixoX = np.linspace(0, 15, 1000)
sns.lineplot(x=eixoX, y=expon.pdf(eixoX, scale=media))
plt.xlabel('tempo de espera em minutos')
plt.ylabel('densidade de probabilidade')
plt.show()

sns.lineplot(x=eixoX, y=expon.cdf(eixoX, scale=media))
plt.xlabel('tempo de espera em minutos')
plt.ylabel('probabilidade acumulada')
plt.show()

# --- Marcando um valor no grafico (ex: tempo t95) ---
eixoX = np.linspace(0, 2, 1000)
plt.plot(eixoX, expon.pdf(eixoX, scale=1/4))
plt.axvline(t95, color='r', linestyle='--', label=f't = {t95:.2f}')
plt.legend()
plt.show()

# --- Comparando probabilidade teorica x simulada ---
tempos = np.random.exponential(scale=media, size=100000)
pTeorica = expon.cdf(5, scale=media)
pSimulada = np.mean(tempos < 5)          # frequencia relativa observada
print(f'probabilidade teorica: {pTeorica:.4f}')
print(f'probabilidade simulada: {pSimulada:.4f}')
print(f'media simulada: {tempos.mean():.4f}  | teorica: {expon.mean(scale=media):.4f}')
print(f'desvio simulado: {tempos.std():.4f} | teorico: {expon.std(scale=media):.4f}')


# =====================================================================
# RESUMO RAPIDO - QUAL FUNCAO USAR?
# =====================================================================
#
#  Pergunta                | Binomial / Poisson (discretas) | Normal / Exponencial (continuas)
#  ------------------------|--------------------------------|---------------------------------
#  EXATAMENTE k            | pmf(k, ...)                    | (=0)  pdf da so a altura da curva
#  ATE k  (<= k)           | cdf(k, ...)                    | cdf(x, ...)
#  MENOS que k (< k)       | cdf(k-1, ...)                  | cdf(x, ...)
#  MAIS que k  (> k)       | sf(k, ...)                     | sf(x, ...)
#  k OU MAIS   (>= k)      | sf(k-1, ...)                   | sf(x, ...)
#  ENTRE a e b (inclusive) | cdf(b) - cdf(a-1)              | cdf(b) - cdf(a)
#  Valor para prob. p      | ppf(p, ...)                    | ppf(p, ...)
#  Media / Var / Desvio    | mean / var / std               | mean / var / std
#
#  Parametros:
#    binom.pmf(k, n, p)            n = tentativas, p = prob. de sucesso
#    poisson.pmf(k, mu)            mu = media no intervalo (ajustar por regra de 3)
#    norm.cdf(x, media, desvio)
#    expon.cdf(x, scale=1/lambda)  scale = media
#
#  Simulacao (numpy):
#    np.random.binomial(n, p, qtd)
#    np.random.poisson(mu, qtd)
#    np.random.normal(media, desvio, qtd)
#    np.random.exponential(scale=media, size=qtd)
#    np.random.randint(ini, fim_exclusivo, qtd)
#    np.random.rand(qtd)                          -> entre 0 e 1
#
#  Proporcao simulada:  np.mean(vetor < valor)
# =====================================================================
