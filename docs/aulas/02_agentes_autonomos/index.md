# Agentes Autônomos

<embed src="slides.pdf" type="application/pdf" width="600" height="300">

## Exemplo do aspirador de pó

Um robô aspirador de pó deve limpar uma casa com duas posições. As operações que ele sabe executar são:

* sugar
* ir para a posição da esquerda
* ir para a posição da direita

<img src="figuras/aspirador_po.png" width="400" height="200">

Em **grupo** de 4 pessoas responda as seguintes perguntas (tempo de 15 minutos): 

* O que é relevante representar nos estados do mundo? Como os estados são estruturados (estrutura de dados) e qual o significado dela (dos campos)?
* Quais são os estados possíveis do mundo do aspirador e as suas transições?
* Quais são as consequências das ações sobre os estados? As ações são determinísticas?
* É possível desenhar o **grafo** com todos os estados e transições para este problema? 
* Apresente uma solução possível. Uma sequência de ações que fazem o robô sair do estado inicial e chegar no estado final. 

Considere como estado final a situação ilustrada abaixo: 

<img src="figuras/aspirador_po_final.png" width="400" height="200">

Prepararem-se para eventualmente apresentar as suas respostas. 

??? warning "Conceitos que devem ser explorados neste exercício"

    Representação de um problema na forma de **estado**, **transição**, **grafo**