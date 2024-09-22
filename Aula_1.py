#Onde no código ele está extraindo uma API da GUPY

#Caminho: Junior_Zone/modules/gupy_scraper.py
#Trecho do código onde a extração ocorre: linhas 27-30

# try:
#     request = session.get(url, headers=self.headers)  # Faz a requisição para a API
#     response = request.json().get("data", [])  # Extrai os dados da resposta JSON
#     responses.append(response)  # Armazena a resposta processada

# -------------------------------------------------------------------------------------------------------------------------------------

# 1. O que é uma API?

# Uma API (Interface de Programação de Aplicações) é um conjunto de definições e protocolos usados para permitir que diferentes 
# sistemas de software se comuniquem entre si. Ela define a forma como um programa pode solicitar serviços de outro, enviar e 
# receber dados, e realizar operações sem precisar conhecer detalhes internos de como o outro sistema funciona.

# Exemplo: Quando você usa um aplicativo de previsão do tempo, ele pode usar uma API para consultar os dados do serviço de 
# meteorologia e exibir as previsões.


# 2. Importância de utilizar venv

# O venv (ambiente virtual) é uma ferramenta no Python para criar ambientes isolados. Isso é importante porque:
# Isolamento: Cada projeto pode ter suas próprias dependências (bibliotecas e versões específicas) sem interferir em outros projetos.
# Controle de dependências: Você pode manter a consistência das versões das bibliotecas que seu projeto usa, garantindo que ele funcione
# como esperado.

# Exemplo: Um projeto pode usar o Flask 1.x e outro, o Flask 2.x. Usando venv, ambos os projetos podem coexistir no mesmo sistema sem conflito.


# 3. Para que serve o Git?
# O Git é um sistema de controle de versão distribuído. Ele permite que você acompanhe as alterações feitas no código ao longo do 
# tempo e colabore com outros desenvolvedores de forma eficiente.
# Controle de versão: Com o Git, você pode criar "snapshots" do seu código em diferentes momentos, permitindo retornar a versões 
# anteriores se necessário.
# Colaboração: O Git facilita a colaboração em equipe, pois diferentes pessoas podem trabalhar no mesmo projeto simultaneamente e 
# mesclar suas alterações.

# Exemplo: Se você comete um erro no código, pode voltar para uma versão anterior que funcionava sem perder tudo que foi feito.


# 4. O que é o arquivo .gitignore?
# O .gitignore é um arquivo usado no Git para especificar quais arquivos ou diretórios devem ser ignorados pelo controle de versão.
# Motivo: Nem todos os arquivos precisam ser versionados. Arquivos como logs, dependências de bibliotecas externas (por exemplo, a pasta venv) 
# ou arquivos de configuração locais não devem ser incluídos no repositório.

# Exemplo: Você pode adicionar venv/ no .gitignore para garantir que a pasta do ambiente virtual local não seja enviada para o repositório Git.

# Esses conceitos são fundamentais para organizar seu código, controlar dependências e colaborar de forma eficiente no desenvolvimento de 
# software.
