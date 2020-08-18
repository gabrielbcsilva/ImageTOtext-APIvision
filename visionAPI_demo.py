import io
import os
# Essa API retira o texto de qualquer imagem 
# Importação da biblioteca cliente do Google Cloud
from google.cloud import vision
from google.cloud.vision import types
#Importação da library pandas que é uma biblioteca de software criada para a linguagem Python para manipulação e análise de dados.
import pandas as pd 
#Autenticação conforme a documentação no Google Cloud. 
# Com Seu Token escolha o melhor local para inseri-lo, coloquei o meu na pasta raiz do projeto
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'apikey.json'

client = vision.ImageAnnotatorClient()


#EXEMPLO DE COM IMAGEM REMOTA LOCAL
# Inserir o nome do arquivo e sua pasta 
FILE_NAME = 'plate.jpg'
FOLDER_PATH = r'C:\Users\55639\python\projetoIA\image'
with io.open(os.path.join(FOLDER_PATH, FILE_NAME), 'rb') as image_file:
     content = image_file.read()
#Construindo a instância da Imagem 
image = vision.types.Image(content=content) # pylint: disable=maybe-no-member
#Anotando a responsta da Imagem "Image response"
response = client.text_detection(image=image) # pylint: disable=maybe-no-member
df = pd.DataFrame(columns=['locale', 'description'])
#obs: esse pylint é um corretor de bugs as vezes ele não reconhece a dependência então adicionei uma exeção para essa linha
texts = response.text_annotations
#Bom a varíavel df está retirando a localização e a descrição da imagem ela vem em formato de <List>
for text in texts:
       df = df.append(
            dict(
               locale=text.locale,
               description=text.description
           ),
           ignore_index=True
       )
#printando só a lista de nomes mas se você quiser vizualizar o objeto é só digitar 'df' no terminal
print(df['description'][0])


#EXEMPLO DE COM IMAGEM REMOTA
# OU voce pode pegar na internet passando a the image url(Rode somente esse trecho para frente)

#img_url = 'https://cdn.pensador.com/img/imagens/en/qu/enquanto_deus_for_meu_chao_nao_ha_quem_me_derrube.jpg'
#image = vision.types.Image()  # pylint: disable=maybe-no-member
#image.source.image_uri = img_url
#response = client.text_detection(image=image)  # pylint: disable=maybe-no-member
#texts = response.text_annotations

#df = pd.DataFrame(columns=['locale','description'])
#for text in texts:
#       df = df.append(
#            dict(
#               locale=text.locale,
#               description=text.description
#           ),
#           ignore_index=True
#       )

#digite 'df' ou print no terminal python e veja o objeto capturado