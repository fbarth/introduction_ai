# Agentes Autônomos

<embed src="slides.pdf" type="application/pdf" width="600" height="300">

## Exemplo do aspirador de pó

Um robô aspirador de pó deve limpar uma casa com duas posições. As operações que ele sabe executar são:

* sugar
* ir para a posição da esquerda
* ir para a posição da direita

Em grupo responda as seguintes perguntas: 

* Quais os estados possíveis do mundo do aspirador e as transições? 
* Apresente uma solução possível. Uma sequência de ações que fazem o robô sair do estado inicial e chegar no estado final. 

## Exercício: Aspirador de Pó 

Considere o exemplo do aspirador de pó. Uma possível solução está implementada no 
arquivo [code/search/VacuumWorld.py](../code/search/VacuumWorld.py). Considerando esta implementação, execute as seguintes ações:

* acesse o diretório **code/search** e execute o comando `python VacuumWorld.py`. Qual foi a resposta fornecida pelo programa? O que esta resposta representa? Por que as respostas são diferentes?

* Acesse o código `VacuumWorld.py`. Quais são os métodos definidos na classe VacuumWorld? Descreve o que você acredita que cada método realiza.

* Vá até a função `main()` do arquivo `VacuumWorld.py`. Esta função faz uso de algum algoritmo de busca? Quais? 

* Altere o estado inicial e o estado objetivo descritos no arquivo `VacuumWorld.py`, execute novamente o comando `python VacuumWorld.py` e veja o que acontece. 

* Execute o comando `pytest test_VacuumWorld.py --capture=tee-sys`. O que aconteceu? Você sabe explicar? Você saberia adicionar mais uma função de teste no arquivo `test_VacuumWorld.py`?
