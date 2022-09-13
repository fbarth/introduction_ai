# Problema dos 8-Puzzle

Considere o problema dos *8-puzzle* discutido em sala de aula. Implemente uma solução para este problema. 

<p align="center">
<img src="../../referencias/03_algoritmos_busca/figuras/fig03-04.png" alt="Grafo" width="400"/>
</p>

Implemente um agente autônomo que consegue resolver este problema. Antes de iniciar a implementação, pense na resposta para as seguintes perguntas: 

* O que é relevante representar nos estados do mundo? Como os
    estados são estruturados (estrutura de dados) e qual o significado
    dela (dos campos)?
* Mostre como ficam representados os estados inicial e final
    segundo a representação adotada.
* Quais as operações sobre os estados?
    (detalhe como cada operação irá alterar os estados e quais as
    condições para cada operação ser executada)
* Qual a estimativa do tamanho do espaço de busca (número de
    estados possíveis)?
* Que algoritmo de busca pode ser utilizado para resolver este problema considerando que
a solução apresentada precisa ser ótima? 

A entrega da sua implementação deverá ter 1 arquivo chamado `Puzzle8.py` que implementa a interface `State` e que deve passar por TODOS os testes especificados em `test_8_puzzle.py`. 

O seu agente deve ser capaz de identificar um plano para todos os estados iniciais descritos como fáceis e difícieis no arquivo de testes. Para os estados descritos como impossível o agente precisa retornar a mensagem *"Nao achou solucao"*. Deve-se considerar o estado *goal* em formato caracol, como apresentado abaixo:

| 1 | 2 | 3 |
|:-:|:-:|:-:|
| 8 |   | 4 |
| 7 | 6 | 5 |

## Formato de entrega

* Para a implementação e entrega deste exercício nós vamos utilizar o [Github Classroom](https://classroom.github.com/a/0tIfTG6H). 

* O link para o enunciado é este aqui [https://classroom.github.com/a/0tIfTG6H](https://classroom.github.com/a/0tIfTG6H). Através deste link você consegue baixar o repositório e começar a sua codificação. 

* **Prazo para a entrega**: 15/09/2022 (quinta-feira) até às 23:00 horas.
