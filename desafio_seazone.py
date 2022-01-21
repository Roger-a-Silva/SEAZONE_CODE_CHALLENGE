import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Criação do dataframe unificado, para desenvolvimento das respostas;
df_imovel = pd.read_csv('desafio_details.csv', delimiter = ',')
df_detalhes = pd.read_csv('desafio_priceav.csv', delimiter = ',')
df_unificado = df_imovel.merge(df_detalhes, on='airbnb_listing_id', how='inner').sort_values(by='occupied', ascending=False).reset_index(drop=True) 


#1. Ordene os bairros em ordem crescente de número de listings; 
df_bairro_id_anuncio = (df_unificado[['suburb','airbnb_listing_id']].reset_index(drop=True))
df_bairro_ordenado = df_bairro_id_anuncio.groupby(['suburb'], as_index=False)['airbnb_listing_id'].count().sort_values(by='airbnb_listing_id', ascending=True).reset_index(drop=True) 
df_bairro_ordenado.rename(columns = {'suburb':'BAIRRO','airbnb_listing_id':'QTD_ANUNCIO'}, inplace = True) 
#Dataframe solução 1
print("1. Ordene os bairros em ordem crescente de número de listings; \n")
display(df_bairro_ordenado)
#Gráfico solução 1
df_bairro_ordenado_graph = pd.DataFrame(df_bairro_ordenado,columns=['BAIRRO','QTD_ANUNCIO'])
df_bairro_ordenado_graph.plot(x ='BAIRRO', y='QTD_ANUNCIO', kind = 'bar')
plt.show()
input("Press Enter to continue...")


#2. Ordene os bairros em ordem crescente de faturamento médio dos listings;
df_bairro_faturamento = (df_unificado[['suburb','airbnb_listing_id','price_string','occupied']].reset_index(drop=True)).sort_values(by='occupied', ascending=True)
df_bairro_faturamento_ocupados = df_bairro_faturamento[df_bairro_faturamento['occupied'] < 1]
df_bairro_faturamento_valor = df_bairro_faturamento_ocupados.groupby(['suburb'], as_index=False)['price_string'].sum().sort_values(by='price_string', ascending=True).reset_index(drop=True) 
df_bairro_faturamento_valor_final = df_bairro_faturamento_valor.copy()
df_bairro_faturamento_valor_final['price_string'] = 'R$ ' + df_bairro_faturamento_valor_final['price_string'].astype(str)
df_bairro_faturamento_valor_final.rename(columns = {'suburb':'BAIRRO','price_string':'VALOR_TOTAL'}, inplace = True) 
#Dataframe solução 2
print("2. Ordene os bairros em ordem crescente de faturamento médio dos listings; \n")
display(df_bairro_faturamento_valor_final)
#Gráfico solução 2
df_bairro_faturamento_valor_graph = pd.DataFrame(df_bairro_faturamento_valor,columns=['suburb','price_string'])
df_bairro_faturamento_valor_graph.price_string = df_bairro_faturamento_valor_graph.price_string.astype(int)
df_bairro_faturamento_valor_graph.rename(columns = {'suburb':'BAIRRO','price_string':'VALOR_TOTAL_EM_REAIS'}, inplace = True) 
df_bairro_faturamento_valor_graph.plot(x ='BAIRRO', y='VALOR_TOTAL_EM_REAIS', kind = 'line')
plt.gcf().axes[0].yaxis.get_major_formatter().set_scientific(False)
plt.show()
input("Press Enter to continue...")


#3. Existem correlações entre as características de um anúncio e seu faturamento?
#a. Quais? Explique
df_faturamento_detalhe_uniao = (df_unificado[['suburb','ad_name','airbnb_listing_id','star_rating','is_superhost','number_of_reviews','price_string','occupied','number_of_bedrooms','number_of_bathrooms']].reset_index(drop=True)).sort_values(by='occupied', ascending=True)
df_faturamento_detalhe_ocupados = df_faturamento_detalhe_uniao[df_faturamento_detalhe_uniao['occupied'] < 1]
df_faturamento_detalhe_estrelas=df_faturamento_detalhe_ocupados.fillna(0.1)
df_faturamento_detalhe_estrelas["number_of_reviews"].replace({0.1:0}, inplace=True)
df_faturamento_detalhe_estrelas = df_faturamento_detalhe_estrelas.groupby(['star_rating'], as_index=False)['price_string'].sum().sort_values(by='price_string', ascending=False).reset_index(drop=True) 
df_faturamento_detalhe_estrelas["star_rating"].replace({0.1:"N/A"}, inplace=True)
df_faturamento_detalhe_estrelas_final = df_faturamento_detalhe_estrelas.copy()
df_faturamento_detalhe_estrelas_final['price_string'] = 'R$ ' + df_faturamento_detalhe_estrelas_final['price_string'].astype(str)
df_faturamento_detalhe_estrelas_final.rename(columns = {'star_rating':'QTD_ESTRELAS','price_string':'VALOR_TOTAL'}, inplace = True)
#Dataframe solução 3
print("3. Existem correlações entre as características de um anúncio e seu faturamento? \n")
display(df_faturamento_detalhe_estrelas_final)
####R: Sim. Existe uma relação diretamente proporcional sobre a quantidade de estrelas do anúncio e o faturamento total gerado.
#Gráfico solução 3
label_star = df_faturamento_detalhe_estrelas['star_rating']
explode = (0, 0, 0, 1, 2, 3, 4)
df_faturamento_detalhe_estrelas.rename(columns = {'star_rating':'QTD_ESTRELAS','price_string':'PERCENTUAL_DE_FATURAMENTO_POR_ESTRELA'}, inplace = True)
df_faturamento_detalhe_estrelas.plot.pie(y='PERCENTUAL_DE_FATURAMENTO_POR_ESTRELA',explode=explode,figsize=(7,7),autopct='%1.1f%%', startangle=10,labels = label_star,fontsize=15)
plt.show()
input("Press Enter to continue...")
####R: Entretanto, existe um alto valor de faturamento sobre imóveis que não apresentaram informações sobre a quantidade de estrelas do anúncio (89.210 no total com faturamento de R$31.791.356,00).
####R: Para uma análise mais profunda, temos esses anúncios como 'N/A' e iremos procurar por correlações entre outras características e faturamento dessa categoria.


df_nostar_detalhe_imovel = (df_unificado[['suburb','ad_name','airbnb_listing_id','star_rating','is_superhost','number_of_reviews','price_string','occupied','number_of_bedrooms','number_of_bathrooms']].reset_index(drop=True)).sort_values(by='occupied', ascending=True)
df_nostar_detalhe_imovel  = df_nostar_detalhe_imovel[df_nostar_detalhe_imovel['occupied'] < 1]
df_nostar_detalhe_imovel = df_nostar_detalhe_imovel.fillna(0.1)
df_nostar_detalhe_imovel["number_of_bedrooms"].replace({0.1:0}, inplace=True)
df_nostar_detalhe_imovel["number_of_bathrooms"].replace({0.1:0}, inplace=True)
df_nostar_detalhe_imovel = df_nostar_detalhe_imovel[df_nostar_detalhe_imovel.star_rating == 0.1]
df_nostar_detalhe_imovel_view = df_nostar_detalhe_imovel.groupby(['star_rating','number_of_bedrooms','number_of_bathrooms'], as_index=False)['price_string'].sum().sort_values(by='price_string', ascending=False).reset_index(drop=True) 
df_nostar_detalhe_imovel_view["star_rating"].replace({0.1:"N/A"}, inplace=True)
df_nostar_detalhe_imovel = df_nostar_detalhe_imovel_view.iloc[0:3]
df_nostar_detalhe_imovel = df_nostar_detalhe_imovel.groupby(['star_rating'], as_index=False)['price_string'].sum().reset_index(drop=True) 
df_nostar_detalhe_imovel_final = df_nostar_detalhe_imovel.copy()
df_nostar_detalhe_imovel_final['price_string'] = 'R$ ' + df_nostar_detalhe_imovel_final['price_string'].astype(str)
df_nostar_detalhe_imovel_final.rename(columns = {'star_rating':'QTD_ESTRELAS','number_of_bedrooms':'QTD_QUARTOS','number_of_bathrooms':'QTD_BANHEIROS','price_string':'VALOR_TOTAL'}, inplace = True)
#Dataframe solução 3.1
print("3.1. Valor total de imóveis que possuem entre 1/2 quartos e 1/2 banheiros sem avaliações de estrelas. \n")
display(df_nostar_detalhe_imovel_final)
####R: A maioria desses anúncios são referentes a locais pequenos (entre 1/2 quartos e 1/2 banheiros, representando aprox. 76% das locações sem informações sobre quantidade de estrelas. (R$ 24.462.936,00)
####R: Esse valor foi encontrado somando os 3 maiores faturamentos de uma lista ordenada com informações físicas do imóvel do anúncio. Essa lista pode ser acessada no dataframe: df_nostar_detalhe_imovel_view

df_nostar_detalhe_local = (df_unificado[['suburb','ad_name','airbnb_listing_id','star_rating','is_superhost','number_of_reviews','price_string','occupied','number_of_bedrooms','number_of_bathrooms']].reset_index(drop=True)).sort_values(by='occupied', ascending=True)
df_nostar_detalhe_local  = df_nostar_detalhe_local[df_nostar_detalhe_local['occupied'] < 1]
df_nostar_detalhe_local = df_nostar_detalhe_local.fillna(0.1)
df_nostar_detalhe_local["number_of_bedrooms"].replace({0.1:0}, inplace=True)
df_nostar_detalhe_local["number_of_bathrooms"].replace({0.1:0}, inplace=True)
df_nostar_detalhe_local = df_nostar_detalhe_local[df_nostar_detalhe_local.star_rating == 0.1]
df_nostar_detalhe_local_view = df_nostar_detalhe_local.loc[df_nostar_detalhe_local['ad_name'].str.contains("mar|praia", case=False)]
df_nostar_detalhe_local = df_nostar_detalhe_local_view.groupby(['star_rating'], as_index=False)['price_string'].sum().sort_values(by='price_string', ascending=False).reset_index(drop=True) 
df_nostar_detalhe_local["star_rating"].replace({0.1:"N/A"}, inplace=True)
df_nostar_detalhe_local_final = df_nostar_detalhe_local.copy()
df_nostar_detalhe_local_final['price_string'] = 'R$ ' + df_nostar_detalhe_local_final['price_string'].astype(str)
df_nostar_detalhe_local_final.rename(columns = {'star_rating':'QTD_ESTRELAS','price_string':'VALOR_TOTAL'}, inplace = True)
#Dataframe solução 3.2
print("3.2. Valor total de imóveis que fazem referência ao mar/praia no anúncio e estão sem avaliações de estrelas. \n")
display(df_nostar_detalhe_local_final)
####R: Outro valor de destaque vem de anúncios que fazem referência ao mar/praia, representando aprox. 51% das locações sem informações sobre quantidade de estrelas. (R$ 16.281.230,00)
####R: Esse valor foi encontrado após buscar uma lista de anúncios que mencionam 'mar' ou 'praia'. Essa lista pode ser acessada no dataframe: df_nostar_detalhe_local_view

df_nostar_detalhe_local_imovel= (df_unificado[['suburb','ad_name','airbnb_listing_id','star_rating','is_superhost','number_of_reviews','price_string','occupied','number_of_bedrooms','number_of_bathrooms']].reset_index(drop=True)).sort_values(by='occupied', ascending=True)
df_nostar_detalhe_local_imovel  = df_nostar_detalhe_local_imovel[df_nostar_detalhe_local_imovel['occupied'] < 1]
df_nostar_detalhe_local_imovel = df_nostar_detalhe_local_imovel.fillna(0.1)
df_nostar_detalhe_local_imovel["number_of_bedrooms"].replace({0.1:0}, inplace=True)
df_nostar_detalhe_local_imovel["number_of_bathrooms"].replace({0.1:0}, inplace=True)
df_nostar_detalhe_local_imovel = df_nostar_detalhe_local_imovel[df_nostar_detalhe_local_imovel.star_rating == 0.1]
df_nostar_detalhe_local_imovel_view = df_nostar_detalhe_local_imovel.loc[df_nostar_detalhe_local_imovel['ad_name'].str.contains("mar|praia", case=False)]
df_nostar_detalhe_local_imovel_view  = df_nostar_detalhe_local_imovel_view[df_nostar_detalhe_local_imovel_view['number_of_bedrooms'] <= 2]
df_nostar_detalhe_local_imovel_view  = df_nostar_detalhe_local_imovel_view[df_nostar_detalhe_local_imovel_view['number_of_bathrooms'] <= 2]
df_nostar_detalhe_local_imovel_view = df_nostar_detalhe_local_imovel_view.groupby(['star_rating','number_of_bedrooms','number_of_bathrooms'], as_index=False)['price_string'].sum().sort_values(by='price_string', ascending=False).reset_index(drop=True) 
df_nostar_detalhe_local_imovel = df_nostar_detalhe_local_imovel_view.groupby(['star_rating'], as_index=False)['price_string'].sum().reset_index(drop=True) 
df_nostar_detalhe_local_imovel["star_rating"].replace({0.1:"N/A"}, inplace=True)
df_nostar_detalhe_local_imovel_final = df_nostar_detalhe_local_imovel.copy()
df_nostar_detalhe_local_imovel_final['price_string'] = 'R$ ' + df_nostar_detalhe_local_imovel_final['price_string'].astype(str)
df_nostar_detalhe_local_imovel_final.rename(columns = {'star_rating':'QTD_ESTRELAS','price_string':'VALOR_TOTAL'}, inplace = True)
#Dataframe solução 3.3
print("3.3. Valor total de imóveis que possuem entre 1/2 quartos e 1/2 banheiros e fazem referência ao mar/praia no anúncio, sem avaliações de estrelas. \n")
display(df_nostar_detalhe_local_imovel_final)
####R: Imóveis de até 2 quartos e até 2 banheiros e que também mencionam 'mar' ou 'praia' no anúncio representam aprox. 40% das locações sem informações sobre quantidade de estrelas. (R$ 12.737.599,00)
####R: Esse valor foi encontrado após gerar uma lista com as citadas características. Essa lista pode ser acessada no dataframe: df_nostar_detalhe_local_imovel_view
input("Press Enter to continue...")

df_extra_1 = df_nostar_detalhe_local.copy()
df_extra_1.rename(columns = {'price_string':'VALOR_APTO_PRAIA'}, inplace = True)
df_extra_2 = df_nostar_detalhe_imovel.copy()
df_extra_2.rename(columns = {'price_string':'VALOR_APTO_PEQUENO'}, inplace = True)
df_extra_3 = df_nostar_detalhe_local_imovel.copy()
df_extra_3.rename(columns = {'price_string':'VALOR_APTO_PEQUENO_PRAIA'}, inplace = True)
df_extra_4 = df_faturamento_detalhe_estrelas.copy()
df_extra_4 =  df_extra_4[df_extra_4['QTD_ESTRELAS'] == "N/A"]
df_extra_4.rename(columns = {'PERCENTUAL_DE_FATURAMENTO_POR_ESTRELA':'VALOR_TOTAL_SEM_AVALIACAO'}, inplace = True)
df_extra_5 = [df_extra_1["VALOR_APTO_PRAIA"], df_extra_2["VALOR_APTO_PEQUENO"], df_extra_3["VALOR_APTO_PEQUENO_PRAIA"], df_extra_4["VALOR_TOTAL_SEM_AVALIACAO"]]
df_extra_5 = pd.DataFrame(df_extra_5)
df_extra_5.columns = ['VALOR_TOTAL']
df_extra_5['TIPO_VALOR'] = df_extra_5.index
df_extra_5 = df_extra_5.sort_values(by='VALOR_TOTAL', ascending=False)
df_extra_5 = df_extra_5[df_extra_5.columns[::-1]].reset_index(drop=True) 
df_extra_final = df_extra_5.copy()
representam = ['100% dos anuncios sem avaliação', '76% dos anuncios sem avaliação', '51% dos anuncios sem avaliação', '40% dos anuncios sem avaliação']
df_extra_final['PERCENTUAL_DE_FATURAMENTO'] = representam
#Dataframe solução 3.4
print("3.4. Tabela comparativa com volume de faturamento das unidades sem avaliações de estrelas. \n")
display(df_extra_final)
####R: Por fim, temos uma tabela onde podemos visualizar qual o total gasto por categoria, dentro dos anúncios sem avaliação, e o percentual de cada tipo de imóvel.
print("3.4. Gráfico comparativo com volume de faturamento das unidades sem avaliações de estrelas. \n")
#Gráfico solução 3.4
df_extra_5 = pd.DataFrame(df_extra_5,columns=['TIPO_VALOR','VALOR_TOTAL'])
df_extra_5.plot(x ='TIPO_VALOR', y='VALOR_TOTAL', kind = 'bar')
plt.gcf().axes[0].yaxis.get_major_formatter().set_scientific(False)
plt.show()
input("Press Enter to continue...")


#4. Qual a antecedência média das reservas?
#a. Esse número é maior ou menor para finais de semana?
df_reservas_view = (df_unificado[['airbnb_listing_id','booked_on','date','occupied']].reset_index(drop=True))
df_reservas_view =  df_reservas_view[df_reservas_view['occupied'] < 1]
df_reservas_view =  df_reservas_view[df_reservas_view['booked_on'] != 'blank']
df_reservas_view['booked_on'] = pd.to_datetime(df_reservas_view['booked_on'], infer_datetime_format=True)
df_reservas_view['date'] = pd.to_datetime(df_reservas_view['date'], infer_datetime_format=True)
df_reservas_view['dia_reserva'] = df_reservas_view['booked_on'].dt.day_name()
df_reservas_view['dia_ocupado'] = df_reservas_view['date'].dt.day_name()
df_reservas_view['antecedencia'] = (df_reservas_view['date'] - df_reservas_view['booked_on']).dt.days
df_reservas_view =  df_reservas_view[df_reservas_view['antecedencia'] != 0 ]
df_reservas = df_reservas_view['antecedencia'].mean()
#Resultado solução 4
print("4. Qual a antecedência média das reservas? \n")
display(df_reservas)
#R: A antecedência média das reservas é de 3.78 dias.
input("Press Enter to continue...")

df_reservas_fds = df_reservas_view.groupby(['dia_ocupado'], as_index=False)['antecedencia'].mean().sort_values(by='antecedencia', ascending=False).reset_index(drop=True) 
df_reservas_fds =  df_reservas_fds[df_reservas_fds['antecedencia'] != 0 ]
#Resultado solução 4.1
print("a. Esse número é maior ou menor para finais de semana? \n")
display(df_reservas_fds)
#R: Essa antecedência é maior para os finais de semana, sendo as médias de domingo, sábado e sexta feira as maiores dentre os dias da semana, respectivamente.
#Gráficos solução 4.1
df_reservas_fds_graph = pd.DataFrame(df_reservas_fds,columns=['dia_ocupado','antecedencia'])
df_reservas_fds_graph.plot(x ='dia_ocupado', y='antecedencia', kind = 'bar')
plt.show()
input("Press Enter to continue...")
print("Obrigado por ter chegado até aqui! Por favor, não desiste de mim! :D")









