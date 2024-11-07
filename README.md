# Agenda Django 
- O presente repositório se trata de um pequeno projeto desenvolvido durante meus estudos em Django.
- O projeto se trata de uma agenda de tarefas pessoais. Cada usuário tera sua agenda com suas tarefas. Há também uma admin page e toda a aplicação conta com autenticação. 



## Clonando e preparando seu ambiente de trabalho:
- Clone o repositório:
    ```bash
    git clone https://github.com/RicToni/agenda_django
    ```

- Crie um ambiente virtual:
    ```bash
    python -m venv venv
    ```
    - Após o uso do comando acima uma pasta chamada 'venv' deve ser criada no diretório do projeto. 
    - Caso seja criado um ambiente virtual com nome distinto de 'venv' ou '.venv' lembre-se de adicionar seu nome ao arquivo '.gitignore', para que o mesmo não seja carregado e salvo pelo git/github. 

- Ative o ambiente virtual:
    - Para Windows:
        ```bash
        venv\Scripts\activate
        ```
    - Para Linux/MacOS:
        ```bash
        source venv/bin/activate
        ```

- Com o ambiente virtual criado e ativo, instale o Django e todas as dependências localmente:
    ```bash
    pip install -r requirements.txt
    ```
<hr>

## Executando o servidor:
- Para rodar o servidor execute o seguinte comando no terminal:
    ```bash
    python manage.py runserver
    ```
- Caso ocorra algum erro no terminal relacionado a migração execute o seguinte comando para aplicar as migrações:
    ```bash
    python manage.py migrate
    ```
## Guias úteis para o desenvolvimento:
**1 - Migrações e alterações do banco de dados:**
  
  - Utilize o seguinte comando para criar os arquivos de migração com base nas mudanças feitas nos modelos:
     ```bash
    python manage.py makemigrations
    ```
     
  - Após o uso do referido comando o arquivo de migração será criado na pasta migrations do app onde as modificações doram realizadas. O Django automaticamente detecta as mudanças nos modelos e cria as migrações correspondentes.
    
  - Para visualizar as instruções SQL que serão executadas na migração, use o comando sqlmigrate seguido pelo nome do app e o número da migração gerada:
      ```bash
      python manage.py sqlmigrate nome_do_app numero_da_migracao
       ```
  - O número da migração se trata do número do arquivo de migração gerado pelo comando anterior.

  - Por exemplo, se a migração gerada foi 0001_initial no app meu_app, você pode visualizar as instruções SQL com:
      ```bash
      python manage.py sqlmigrate meu_app 0001
       ```
      
  - Agora, para aplicar as migrações no banco de dados, use o comando migrate:
     ```bash
    python manage.py migrate
       ```
