# Processamento de Dados da Justiça Eleitoral

Sistema para processamento e análise de dados processuais da Justiça Eleitoral brasileira, com suporte para execução serial e paralela (multithreading).

## Descrição

Este projeto lê arquivos CSV contendo dados processuais de Tribunais Regionais Eleitorais (TREs) de todos os estados brasileiros, processa as informações e gera relatórios consolidados sobre:
- Metas de julgamento por município
- Metas de desempenho por tribunal
- Busca e exportação de dados específicos por município

## Funcionalidades

- **Leitura automatizada** de arquivos CSV de todos os TREs (27 unidades da federação)
- **Processamento serial** (modo tradicional)
- **Processamento paralelo** com threading para operações simultâneas
- **Cálculo de métricas** de desempenho (Metas 1, 2a, 2ant, 4a, 4b)
- **Exportação de resultados** em arquivos CSV

## Estrutura do Projeto
