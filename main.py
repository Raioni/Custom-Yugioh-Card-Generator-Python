from PIL import Image, ImageDraw, ImageFont

#Fontes utilizadas

#Fonte Nome
fonte_nome = ImageFont.truetype('Fontes/Yu-Gi-Oh! Matrix Regular Small Caps 1.ttf',46)
#Fonte Titulo Efeito
fonte_sub = ImageFont.truetype('Fontes/Yu-Gi-Oh! Matrix Regular Small Caps 1.ttf',26)
#Fonte Descrição Efeito
fonte_desc = ImageFont.truetype('Fontes/Yu-Gi-Oh! ITC Stone Serif LT Italic.ttf',18)
#Fonte ATK e DEF
fonte_stat = ImageFont.truetype('Fontes/palatinolinotype_bold.ttf',16)

carta = Image.open('./Cartas/Normal.png')
desenhar = ImageDraw.Draw(carta)

#Inserindo Nome da Carta
desenhar.text((30,28),"Xicra Linda",fill='black',font=fonte_nome)

#Inserindo Nome do Efeito/Titulo da Carta
desenhar.text((30,460),"[Esposa mais besta do Mundo]",fill='black',font=fonte_sub)

#Inserindo Descrição do efeito da carta em uma variavél separada e criando 2 strings vazias
desc = 'Caso esta carta seja invocada e a carta "Raioni Bobo" esteja em campo de batalha, esta carta perde -300 de atk por estar besta e "Raioni Bobo" ganha +1500 de atk por estar de pinto duro'
t1 = ""
t2 = ""

#Para fazer com que o texto não ultrapasse a caixa de texto fazer mesmo processo de antes mas comparando com a width, para ajustar a fonte: diminuir ela em algum valor (1 ou 2), e entao recalcular a width e comparar para ver se ultrapassou ou não, caso ultrapasse diminuir a fonte denovo, se não tudo ok

#Percorrendo a string da descrição
for i in range(len(desc)):
  #Inserindo de 1 em 1 os elementos da descrição nas strings vazias
  t1 += desc[i]
  t2 += desc[i]
  #Comparando o comprimento da string2 em pixels com o valor em pixels da borda da caixa de texto (358 pixels)
  if fonte_desc.getlength(t2) > 358:
    #Caso seja maior inserir uma quebra de linha na string 1, e reiniciar a string 2 para que novamente seja feita a comparação nas linhas subsequentes para fazer mais quebras de linha
    t1 += "\n"
    t2 = ""
#Inserindo a string formatada com quebras de linha na Descrição do Efeito da carta
desenhar.text((30,480),t1,fill='black',font=fonte_desc)
#Inserindo ATK da carta
desenhar.text((270,564),"1800",fill='black',font=fonte_stat)
#Inserindo DEF da carta
desenhar.text((356,564),"500",fill='black',font=fonte_stat)


#Salvando a carta
carta.save('./carta.png')
