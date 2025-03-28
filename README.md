## Estrutura do Projeto

### Diretórios Principais

- **`src/`**: Raiz do projeto.

- **`builder/`**: Diretório que padroniza o desenvolvimento do código.
  - `builder/dataframebuilder/`: Aplica a esteira de tratamento da planilha até a criação do dataframe final.
  - `builder/dataframedirector/`: Executa todos os passos do PlaninhasEscolasPipelineBuilder.

- **`data/`**: Diretório para entrada e saída de dados.
  - `data/raw/`: Dados de planilhas sem tratamento.
  - `data/processed/`: Dados de planilhas tratados.

- **`repository/`**: Diretório para comunicação com serviços externos.
  - `repository/download/`: Módulo para download de arquivos.
  - `repository/raw_path/`: Módulo para encontrar e listar os arquivos em `data/raw`.

- **`service/`**: Diretório para serviços internos.
  - `service/extractor/`: Utilizado para criar máscaras e filtros para determinados elementos.
  - `service/fatiamento/`: Realiza o fatiamento (slicing) do DataFrame.
  - `service/mascaras/`: Cria máscaras específicas para um DataFrame.
  - `service/montagem/`: Realiza a montagem do DataFrame final.
  - `service/processamento/`: Realiza o processamento de cada coluna, com o objetivo de extrair as colunas desejadas.
  - `service/reader/`: Realiza a leitura das planilhas em `data/raw`.
  - `service/tratamento/`: Realiza o tratamento do DataFrame.
    - `service/tratamento/tratamento_montagem_builder/`: Tratamentos pós-extração de colunas.
    - `service/tratamento/tratamento_preprocessaento/`: Tratamentos pré-processamento de colunas.

- **`shared/`**: Diretório para constantes do programa.

- **`views/`**: Diretório da interface do usuário.
  - `views/components/`: Componentes da interface do usuário.
  - `views/pages/`: Páginas da interface do usuário.
  - `views/store/`: Controlador dos estados dos componentes.

---
