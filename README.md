Loja de Eletrônicos

Sistema para vendas de eletrônicos, incluindo celulares, notebooks, entre outros. Este projeto integra o framework Django com Frontend (HTML, CSS, JavaScript) e Banco de Dados para oferecer uma solução prática e eficiente para a venda de eletrônicos online.

Introdução

Este sistema foi desenvolvido para facilitar a venda de eletrônicos de forma online. O objetivo principal é proporcionar uma experiência de compra simples e sem complicações para o usuário final, com funcionalidades voltadas para:

Cadastro de clientes

Cadastro de vendedores
Realização de vendas
Emissão de relatórios
Controle de estoque
Além disso, o projeto envolve o uso de tecnologias como Django, HTML, CSS, JavaScript e Python, e permitiu o aprimoramento de nossas soft skills, trabalho em equipe e gerenciamento de tempo.

Funcionalidades

O sistema oferece as seguintes funcionalidades:

Cadastro de Clientes: Permite o cadastro de informações de clientes para realizar compras.
Cadastro de Vendedores: Cadastro dos vendedores para a realização de vendas.
Realização de Vendas: Permite o registro de vendas no sistema.
Emissão de Relatórios: Geração de relatórios para controle e análise das vendas realizadas.
Controle de Estoque: Gerenciamento do estoque de eletrônicos disponíveis para venda.
Tecnologias Utilizadas
Backend: Django (Python)
Frontend: HTML, CSS, JavaScript
Banco de Dados: SQLite (ou outro, caso configurado)
Ferramentas:
VSCode
GitHub
Instalação
Siga os passos abaixo para instalar e rodar o projeto localmente.

1. Instalar o Django
Abra o terminal no VSCode e execute o seguinte comando para instalar o Django:

bash
Copiar código
pip install django

2. Clonar o Repositório
Clone o repositório do GitHub para sua máquina:

bash
Copiar código
git clone https://github.com/caioziin/estoque.git

3. Instalar Dependências
Dentro da pasta do projeto, instale as dependências listadas no arquivo requirements.txt:

bash
Copiar código
pip install -r requirements.txt

4. Rodar o Servidor de Desenvolvimento
Execute o servidor de desenvolvimento Django:

bash
Copiar código
python manage.py runserver
O servidor será executado na URL padrão http://127.0.0.1:8000/.

5. Acessar a Aplicação
Para acessar a interface administrativa, vá até o seguinte link no seu navegador:

http://127.0.0.1:8000/admin/

Aqui você pode gerenciar os dados do sistema (clientes, vendedores, vendas, etc.). Para entrar, use as credenciais do superusuário que você criou durante o processo.

Estrutura do Projeto
O projeto está organizado da seguinte maneira:

bash
Copiar código
/estoque
  ├── /estoque      # Diretório da aplicação Django
  ├── /templates     # Arquivos HTML
  ├── /static        # Arquivos CSS e JavaScript
  ├── manage.py      # Script principal para rodar o Django
  └── requirements.txt # Dependências do projeto

Autores
Este projeto foi desenvolvido por:

Caio F Sousa Pedrosa de Albuquerque
Pedro Henrique Nascimento
Pedro Davi de Souza Monteiro

Licença
Este projeto é de código aberto e distribuído sob a licença MIT. Veja o arquivo LICENSE para mais informações.

Melhorias Possíveis
Este projeto pode ser expandido de diversas maneiras, incluindo:

Implementação de um sistema de pagamento.
Melhoria na interface de usuário (UI/UX).
Integração com sistemas de envio e rastreamento de pedidos.
Links Úteis
Protótipo do Projeto
Pauta das Reuniões
