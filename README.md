#SEAZONE_CODE_CHALLENGE


Para o desafio desenvolvido em Python, foram utilizadas a bibliotecas:
- Pandas
- Numpy
- Matplotlib.pyplot

A seguir, um breve resumo sobre os métodos utilizados para realização das questões.

# Início
- Leitura dos dois arquivos de origem dos dados;
- Criação do dataframe unificado, para desenvolvimento das respostas;


## 1. Ordene os bairros em ordem crescente de número de listings

- Criação de dataframe com BAIRRO e ID;
- Agrupamento das informações do dataframe e ordenação crescente pelo número de anúncios;
- Ajustes estéticos;
- Resultado final
- Criação do gráfico a partir do resultado final;


## 2. Ordene os bairros em ordem crescente de faturamento médio dos listings

- Criação de dataframe com BAIRRO, ID, PREÇO, OCUPADO(FLAG);
- Filtro para imóveis ocupados;
- Agrupamento das informações do dataframe e ordenação crescente pelo valor total de faturamento;
- Ajustes estéticos;
- Resultado final
- Criação do gráfico a partir do resultado final;


## 3. Existem correlações entre as características de um anúncio e seu faturamento? Quais?

- Criação de dataframe com BAIRRO, ID, ANÚNCIO, AVALIAÇÃO, PREÇO, OCUPADO(FLAG), Nº DE QUARTOS, Nº DE BANHEIROS;
- Filtro para imóveis ocupados;
- Preenchimento e ajuste de colunas vazias;
- Agrupamento das informações do dataframe e ordenação crescente pelo valor total de faturamento para cada valor de avaliação;
- Ajustes estéticos;
- Resultado final
- Criação do gráfico a partir do resultado final;

Devido ao alto valor encontrado de anúncios sem avaliação, os sub-pontos a seguir se referem à análise complementar desse grupo.


### 3.1 Anúncios sem avaliação - Análise sobre maior faturamento do grupo

- Criação de dataframe com ID, ANÚNCIO, PREÇO, AVALIAÇÃO, OCUPADO(FLAG), Nº DE QUARTOS, Nº DE BANHEIROS;
- Filtro para imóveis ocupados;
- Preenchimento e ajuste de colunas vazias;
- Filtro para imóveis sem avaliação;
- Agrupamento das informações do dataframe e ordenação decrescente pelo valor total de faturamento;
- Soma dos três maiores resultados;
- Ajustes estéticos;
- Resultado final
- Criação do gráfico a partir do resultado final;


### 3.2 Anúncios sem avaliação - Análise sobre local e faturamento do grupo

- Criação de dataframe com ID, PREÇO, AVALIAÇÃO, OCUPADO(FLAG), Nº DE QUARTOS, Nº DE BANHEIROS;
- Filtro para imóveis ocupados;
- Preenchimento e ajuste de colunas vazias;
- Filtro para imóveis sem avaliação;
- Filtro para anúncios que mencionam as palavras MAR ou PRAIA;
- Agrupamento das informações do dataframe e para obtenção do valor total de faturamento;
- Ajustes estéticos;
- Resultado final
- Criação do gráfico a partir do resultado final;


### 3.3 Anúncios sem avaliação - Análise sobre local, estrutura e faturamento do grupo

- Criação de dataframe com ANÚNCIO, ID, PREÇO, AVALIAÇÃO, OCUPADO(FLAG), Nº DE QUARTOS, Nº DE BANHEIROS;
- Filtro para imóveis ocupados;
- Preenchimento e ajuste de colunas vazias;
- Filtro para imóveis sem avaliação;
- Filtro para anúncios que mencionam as palavras MAR ou PRAIA;
- Filtros para imóveis de até 2 quartos e até 2 banheiros;
- Agrupamento das informações do dataframe e para obtenção do valor total de faturamento;
- Ajustes estéticos;
- Resultado final
- Criação do gráfico a partir do resultado final;


### 3.4 Anúncios sem avaliação - Análise geral sobre faturamento do grupo

- Criação de dataframe com dados das últimas análises sobre o grupo de anúncios sem avaliações;
- Ajustes estéticos;
- Resultado final
- Criação do gráfico a partir do resultado final;

## 4. Qual a antecedência média das reservas? Esse número é maior ou menor para finais de semana?

- Criação de dataframe com  ID, DATA DA RESERVA, DATA DE OCUPAÇÃO, OCUPADO(FLAG);
- Filtro para imóveis ocupados;
- Filtro para imóveis ocupados que tiveram agendamento prévio;
- Tratamento de dados referentes às datas dos arquivo;
- Filtro para excluir reservas feitas no mesmo dia;
- Obtenção do resultado (em dias) da antecedência de reservas; (Resposta da primeira pergunta)
- Ajustes estéticos;
- Resultado final (Resposta da segunda pergunta)
- Criação do gráfico a partir do resultado final;
