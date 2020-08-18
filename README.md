# ImageTOtext-APIvision
Project built with python language using the VIsion API Image to text
Documentação para mais informações:
https://cloud.google.com/vision/docs/setup

Guia de início rápido: configurar a API Vision na Linguagem Python

#Sobre o Console do Cloud

O Console do Google Cloud é uma IU da Web usada para provisionar, configurar, gerenciar e monitorar sistemas que usam produtos do Google Cloud. Use o Console do Cloud para configurar e gerenciar recursos da Vision.

-Crie um projeto

Para usar os serviços fornecidos pelo Google Cloud, crie um projeto(Na sua linguagem desejada).
No Console do Cloud, na página do seletor de projetos, selecione ou crie um projeto do Cloud.
Acessar a página do seletor de projetos

-Ativar faturamento(Importante)

Verifique se a cobrança está ativada para o seu projeto do Google Cloud. Saiba como confirmar se a cobrança está ativada para o seu projeto.

-Ativar a API

Você precisa ativar a API Vision para seu projeto.

-Configurar a autenticação

Qualquer aplicativo cliente que usa a API precisa ser autenticado e ter acesso aos recursos solicitados. Nesta seção, você verá importantes conceitos de autenticação e etapas para a configuração. Para mais informações, consulte a Visão geral da autenticação do Google Cloud.

Crie uma Service account em credenciais, Sobre contas de serviço
Há várias opções de autenticação, mas é recomendável usar contas de serviço para autenticação e controle de acesso. 

Baixe a chave, arquivo JSON para conseguir a comunicação em sem projeto- Sobre as chaves da conta de serviço
As contas de serviço estão associadas a um ou mais pares de chaves públicas/privadas. Ao criar um novo par de chaves, você faz o download da chave privada. O SDK do Cloud usa sua chave privada para gerar credenciais ao chamar a API. Você é responsável pela segurança da chave privada e outras operações de gerenciamento, como a rotação de chaves.

#Configurando ambiente Python
baixe o SDK python
baixe o SKD do google Cloud
baixe a chave JSON do seu projeto criado no google cloud
Após todos esses processos com o arquivo Json baixado
Faça o fork do meu projeto e jogue a chave na pasta raiz(json), recomendo que cole na pasta raiz com o nome 'apikey.json' ou com o nome que quiser mas terá que alterar no código python do projeto o nome da chave que ele irá buscar. 
-Dependencias 
OK agora é a parte das dependências que iremos baixar utilizando o pip do Python(Verifique se o python foi instalado no seu sistema digite: python --version)
Para isso abra seu projeto no promp(Obs: para ver as dependências do projeto digite: 'pip list')

1° dependencia : pip install --upgrade google-cloud-vision (Biblioteca do google  cloud)
documentação: https://cloud.google.com/vision/docs/libraries
2° dependencia: pip install pandas (Manipulação de análise de dados para uso na extração do texto da imagem)
documentação: https://pandas.pydata.org/pandas-docs/stable/getting_started/install.html

-Execução
Lembre-se de baixar o plugin do python no seu Editor/IDE
Por fim a execução é feita no terminal do python eu utilizei o vs code, para entrar no terminal do python é simples digite 'python' seja no terminal do vs code ou no terminal do cmd

