## AutoTS - Sistema de Gerenciamento de Recrutamento com IA 🤖

Este projeto é um sistema de console (CLI) em Python que atua como uma ferramenta de rastreamento de candidatos (ATS - Applicant Tracking System) simplificada.

Sua funcionalidade principal é gerenciar um banco de dados de candidatos e vagas, e utilizar a IA do Google (Gemini) para realizar uma análise inteligente, ranqueando e selecionando os candidatos mais qualificados para uma vaga específica.

## 🌍 Alinhamento com os ODS da ONU

Este projeto foi desenvolvido com foco em dois **Objetivos de Desenvolvimento Sustentável (ODS) da ONU**:

-   **🎯 ODS 10 (Redução das Desigualdades):** O núcleo do sistema busca promover a **igualdade de oportunidades** no acesso ao emprego. Ao usar a IA para uma análise de perfil baseada puramente em dados (habilidades, experiências, projetos), o sistema é projetado para ser **imparcial e justo**, mitigando vieses humanos inconscientes que podem ocorrer em processos seletivos tradicionais.
    
-   **💡 ODS 9 (Indústria, Inovação e Infraestrutura):** O projeto aplica **inovação** (Inteligência Artificial generativa) a um processo de negócios tradicional (Recursos Humanos). Ele moderniza a infraestrutura de contratação e fomenta o uso de novas tecnologias para criar soluções mais eficientes e justas na indústria.

----------

## 👥 Integrantes

| Nome                         | RM      |
|------------------------------|---------|
| Azor Tartuce                 | 563995  |
| Daniel Oliveira de Souza     | 566284  |
| Lucas de Almeida Pires       | 562757  |


Link do GitHub: https://github.com/Global-Solution-Future-At-Work/Python-AutoTS

Link do Vídeo de Demonstração: https://youtu.be/ueUEZpuMLJU

----------

## 🚀 Funcionalidades Principais

O sistema é dividido em quatro módulos principais acessíveis através do menu inicial:

### 1. Gerenciar Candidatos

Permite o gerenciamento completo (CRUD) dos perfis dos candidatos.

-   **Listar Candidatos:** Mostra um resumo de todos os candidatos cadastrados (ID, Nome, Resumo, Idiomas).
    
-   **Ver Candidato por ID:** Exibe _todos_ os detalhes de um candidato específico (habilidades, experiências, formação, projetos, etc.).
    
-   **Adicionar Candidato:** Inicia um formulário detalhado para cadastrar um novo candidato, solicitando:
    
    -   Informações básicas (nome, foto, cargo, resumo, localização).
        
    -   Habilidades Técnicas (lista).
        
    -   Soft Skills (lista).
        
    -   Experiências (lista com empresa, cargo, datas, descrição).
        
    -   Formação (lista com curso, instituição, ano).
        
    -   Projetos (lista com título, link).
        
    -   Certificações (lista).
        
    -   Idiomas (lista com idioma, nível).
        
    -   Áreas de Interesse (lista).
        
-   **Atualizar Candidato:** Permite editar todas as informações de um candidato existente, campo por campo.
    
-   **Deletar Candidato:** Remove um candidato do banco de dados.
    

### 2. Gerenciar Vagas e Empresa

Permite definir o perfil da empresa e gerenciar as vagas em aberto.

-   **Ver Dados da Empresa:** Exibe o nome e a descrição da empresa (usados como contexto para a IA).
    
-   **Definir/Atualizar Empresa:** Permite inserir ou alterar o nome e a descrição da empresa.
    
-   **Listar Vagas:** Mostra todas as vagas em aberto.
    
-   **Adicionar Vaga:** Cadastra uma nova vaga (ID, descrição/requisitos, quantidade).
    
-   **Atualizar Vaga:** Permite editar a descrição ou a quantidade de uma vaga.
    
-   **Deletar Vaga:** Remove uma vaga do sistema.
    

### 3. Iniciar Análise por IA

Este é o módulo central do sistema.

-   O usuário seleciona uma vaga em aberto pelo ID.
    
-   O sistema coleta os dados da empresa, os detalhes da vaga selecionada e os perfis de **todos** os candidatos cadastrados.
    
-   Essas informações são enviadas ao `gemini_service` (API do Gemini).
    
-   A IA processa os dados e retorna um JSON com:
    
    -   `candidatos_selecionados`: Uma lista de IDs dos candidatos mais aptos.
        
    -   `resumo_analise`: Um texto explicando o porquê da seleção.
        
-   O usuário pode **salvar o resultado** no histórico.
    
-   O usuário tem a opção de **encerrar o processo seletivo**, o que automaticamente deleta a vaga e os candidatos selecionados do sistema.
    

### 4. Histórico de Análise

Permite consultar ou limpar análises de IA anteriores.

-   **Listar Histórico:** Exibe todos os resultados salvos (ID da análise, descrição da vaga, IDs dos candidatos que foram selecionados e o resumo da IA).
    
-   **Deletar Histórico:** Remove um registro de análise específico.
    

----------

## 🏛️ Arquitetura do Projeto

O projeto é modular e busca separar as responsabilidades:

-   **`main.py` (ou arquivo similar):** Ponto de entrada da aplicação. Controla o loop principal do programa e o roteamento entre os menus (`candidatos_menu`, `empresa_vagas_menu`, etc.).
    
-   **`menu.py`:** Módulo utilitário responsável por toda a interface do console: exibir logos, opções de menu, limpar a tela e capturar entradas do usuário (validando se são números, etc.).
    
-   **`*_repository.py` (Camada de Dados):**
    
    -   `candidatos_repository.py`
        
    -   `empresa_repository.py`
        
    -   `vagas_repository.py`
        
    -   `historico_repository.py`
        
    -   Estes módulos são responsáveis pela persistência dos dados (CRUD). Eles lidam com a leitura e escrita em arquivos locais (provavelmente JSON), garantindo que os dados sejam salvos.
        
-   **`gemini_service.py`:** Contém a lógica de integração com a API do Gemini. É responsável por formatar o _prompt_ com os dados da empresa, da vaga e dos candidatos, enviar a requisição e processar a resposta da IA.
    
-   **`data_service.py`:** Utilitário que verifica se os diretórios ou arquivos de dados necessários existem ao iniciar a aplicação, criando-os se necessário.
    

----------

## 🛠️ Instalação e Configuração

### Pré-requisitos

-   **Python 3.x**
    
-   **Bibliotecas Python:** -> **requests**

### Passos para Instalação

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/Global-Solution-Future-At-Work/Python-AutoTS.git
    cd Python-AutoTS
    ```
    
2.  **Crie e ative um ambiente virtual:**
    ```bash
    # Windows
    python -m venv .venv
    .\.venv\Scripts\activate
    
    # macOS / Linux
    python3 -m venv .venv
    source .venv/bin/activate
    ```
    
3.  Instale as dependências:
    ```
    pip install requests
    ```

----------

## 🏃 Como Usar

1.  **Inicie o programa:**
    
    ```
    python main.py
    ```
    
2.  **Siga o fluxo recomendado:**
           
    -   Acesse **"1. Gerenciar Candidatos"** e cadastre pelo menos 2 ou 3 candidatos com perfis variados.
        
    -   Acesse **"2. Gerenciar Vagas e Empresa"** para definir os dados da sua empresa e criar vagas.
        
    -   Acesse **"3. Iniciar Análise por IA"**, selecione a vaga criada e aguarde o processamento.
        
	    -   Visualize o resultado e, se desejar, salve no histórico.
        
    -   Acesse **"4. Histórico de Análise"** para ver os resultados salvos.
