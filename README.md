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
- **Pesquisa por municípios** com nome do município informado pelo usuário
- **Exportação de resultados** em arquivos CSV

## Estrutura e Análise do Projeto 

O projeto foi dividido em duas partes: Dois programas em python, um que executa as funções de maneira sequencial, e o outro de forma paralela. As funcionalidades executadas são as mesmas, e o programa sequencial foi adaptado como base para construção do programa paralelo. No programa paralelo, foi decidido pelo uso de 4 threads simultâneas para fins de verificar o ganho, mas este número poderia ser adaptado caso a eficiência do programa fosse priorizada ao invés da coleta de dados. Além das funções de execução de tarefas, foi também utilizada a biblioteca time para o registro de tempos de execução.

Primeiramente, foi definida uma classe **Linha** para acomodar os dados presentes nas planilhas de cada estado, com um parâmetro para cada dado da planilha, bem como métodos para o registro em terminal e nos arquivos de saída. Uma outra classe foi criada para acomodar os dados de métricas por tribunal, **Meta_tribunal**. As métricas por município foram implementadas de maneira diferente das métricas por tribunal, por opção do programador, para utilizar e testar diferentes abordagens para o processamento de dados, e portanto não utilizaram uma classe própria.

A seguir, foram implementadas diversas funções para executar as tarefas propostas. Na função abrir_arquivo(), um laço de repetição lê as linhas da planilha, converte e faz a validação dos dados para o tipo de dado correto, contando com o dado do tipo None, e adiciona os dados lidos em uma lista do objeto Linha. No programa serial, os arquivos-alvo são definidos diretamente na função e lidos todos em sequência. No programa paralelo, a lista é dividida em 4 listas menores antes de ser carregada na memória. Essas listas são responsáveis por armazenar os dados das planilhas na memória do programa, para seu posterior uso pelas demais funções. Não foi possível implementar a paralelização nessa parte do projeto, devido à dificuldades em acessar o valor de retorno das funções e parâmetros da lista quando executada por threads.

A primeira funcionalidade do programa foi criada para concatenar os dados obtidos de todas as planilhas em um único arquivo. As funções para escrever os dados em um novo arquivo recebem a lista de objetos guardada na memória e iteram sobre a lista para gravá-la no arquivo de saída. Esse processo é o mesmo para as versões paralela e serial, porém na versão paralela as listas de objetos de cada thread são unidas em uma única lista antes da gravação. A paralelização dessa etapa não evidencia muitos ganhos, visto que o arquivo de saída deve ser o mesmo, uma implementação paralela da gravação teria que implementar mecanismos para impedir o acesso simultâneo do arquivo, o que acarretaria num tempo de execução similar ao serial. Os tempos exibidos no console para o programa serial e paralelo são, respectivamente: 0.9971811771392822 segundos e 0.9104845523834229 segundos.

A segunda funcionalidade para o cálculo de metas é a com o maior tempo de execução na versão serial. A implementação utilizada requer que a função que calcula as metas itere sobre a lista inteira diversas vezes, uma para cada município, para obter uma nova lista que permite o cálculo das métricas dos municípios. O grande tempo de execução provavelmente se dá ao elevado número de municípios, na ordem dos milhares, o que implica em milhares de iterações sobre uma lista com centenas de milhares de elementos. Após os cálculos, os dados calculados são gravados em um único arquivo.

Esta é a funcionalidade que pode apresentar mais ganhos com a utilização de threads. Ao dividir a lista em listas menores, a iteração sobre as listas por cada thread pode ter um tempo de execução muito menor. A iteração sobre a lista inteira por si só não é necessária, visto que cada município pertence a apenas um estado, portanto todas as ocorrências do mesmo município ocorrerão na mesma parte da lista, e o resto da iteração se torna redundante. Essa redundância acumula cada vez mais tempo de atraso pelo vasto número de iterações. Desta forma, o uso de threads ganha tempo não apenas pela execução paralela, mas também pelo tratamento mais inteligente da lista de dados, que remove boa parte da redundância. O gargalo se torna a gravação do arquivo final, onde também se faz necessário o uso de um threading.Lock() para impedir o acesso simultâneo das threads ao arquivo de saída. O ganho no tempo de execução ainda é visível, visto que o processo de gravação do arquivo dura apenas uma fração do tempo necessário para as iterações e cálculos pela lista inteira. Os tempos exibidos no console para o programa serial e paralelo são, respectivamente: 84.35360336303711 segundos e 19.269164323806763 segundos.

A terceira funcionalidade realiza um processo similar à anterior, porém a lista é organizada por tribunais e não municípios. Aqui é possível notar ainda mais evidências de que a iteração sobre a lista toda é o processo que mais consome tempo do programa. A iteração sobre a lista é muito similar ao cálculo de metas por município, porém existem apenas 27 tribunais, se comparados aos milhares de municípios. Uma outra diferença quanto às funções anteriores é que o retorno das funções de métricas por tribunal são armazenadas como um objeto diferente do tipo Meta_tribunal, enquanto nas funções de município os dados são tratados e escritos diretamente na função. Além do cálculo das metas, outra função organiza a nova lista em ordem decrescente antes de gravar no arquivo de saída, utilizando o método sort(). Os tempos exibidos no console para o programa serial e paralelo são, respectivamente: 1.9232990741729736 segundos e 0.9416978359222412 segundos.

A última funcionalidade permite a busca por um município informado pelo usuário, e a gravação de todos os dados referentes ao município em um arquivo de mesmo nome. Esta funcionalidade não apresenta ganhos com a paralelização. Devido à forma que foi implementada, as threads realizam a busca em listas separadas. Conforme dito anteriormente, um município pertence à apenas um estado, portanto apenas uma das threads terá um retorno ao realizar a pesquisa, o que torna as outras threads reduntantes. O processo de pesquisa serial também não é particularmente demorado, pois é realizada apenas uma iteração sobre a lista procurando pelo nome do município. Uma maneira para coletar mais evidências se há ganhos reais com paralelização seria um simples aumento no volume de dados, de forma que o tempo para a pesquisa na lista inteira se torne relevante o suficiente que justifique a divisão em listas menores. Os tempos exibidos no console para o programa serial e paralelo são, respectivamente: 0.20804953575134277 segundos e 0.9712033271789551 segundos, para o município de SÃO PAULO.

## Conclusão

Com a implementação utilizada, é possível concluir que o uso de threads pode aumentar a eficiência de diversas formas, mas é primeiro necessário compreender quais são os processos do programa que requerem mais tempo, e por qual a razão. No caso atual, o processo que mais atrasa a execução do programa é a quantidade de iterações sobre uma lista de dados extensa, boa parte da qual é redundante. O uso de threads pode reduzir o atraso de forma significante, tanto por diminuir o número de iterações necessárias, quanto por abordar os dados de forma mais inteligente. 


