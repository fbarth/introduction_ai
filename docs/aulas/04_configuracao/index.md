# Configuração do ambiente

Para executar esta atividade você terá que fazer o fork do projeto [https://github.com/Insper/ai_code](https://github.com/Insper/ai_code). 

Recomenda-se fortemente que todo estudante faça estas atividades em sua máquina. Os problemas podem ser discutidos em grupo, no entanto, cada aluno precisa ter a sua própria implementação. 

Na pasta `src` deste projeto você irá encontrar diversos arquivos `python`. São os arquivos desta pasta que você irá utilizar neste exercício.

## Exercício: Aspirador de Pó 

Considere o exemplo do aspirador de pó. Uma possível solução está implementada no 
arquivo [src/VacuumWorld.py](https://github.com/Insper/ai_code/blob/main/src/VacuumWorld.py). Considerando esta implementação, execute as seguintes ações:

* acesse o diretório **src** e execute o comando `python VacuumWorld.py`. Qual foi a resposta fornecida pelo programa? O que esta resposta representa? Por que as respostas são diferentes?

* Acesse o código `VacuumWorld.py`. Quais são os métodos definidos na classe VacuumWorld? Descreve o que você acredita que cada método realiza.

* Vá até a função `main()` do arquivo `VacuumWorld.py`. Esta função faz uso de algum algoritmo de busca? Quais? 

* Altere o estado inicial e o estado objetivo descritos no arquivo `VacuumWorld.py`, execute novamente o comando `python VacuumWorld.py` e veja o que acontece. 

* Execute o comando `pytest test_VacuumWorld.py --capture=tee-sys`[^1]. O que aconteceu? Você sabe explicar? Você saberia adicionar mais uma função de teste no arquivo `test_VacuumWorld.py`?

[^1]: Se `pytest test_VacuumWorld.py --capture=tee-sys` não funcionar na sua máquina, execute `pytest test_VacuumWorld.py --capture=no`.

??? warning "O que são algoritmos de busca?"

    * Algoritmo de Busca em Largura
    * Algoritmo de Busca em Profundidade
    * Algoritmo de Busca de Custo Uniforme
    * Algoritmo de Busca em Profundidade Iterativo

    Para entender melhor cada um dos algoritmos de busca, acesse o material sobre [algoritmos de busca](../../referencias/03_algoritmos_busca/busca_versaoFabricio.pdf).

## Espaço com 3 quartos

Vamos implementar um Aspirador de Pó com 3 quartos? Três quartos lado-a-lado (esquerda, centro e direita)? 

Para esta atividade já temos um código pré-pronto: `VacuumWorld3Room.py`. Neste código falta completar o código de alguns métodos da classe.  

* Complete os métodos da classe e execute os dois algoritmos que estão na função main(): Busca em Largura e Busca em Profundidade. Liste as soluções encontradas por ambos os algoritmos.

* O arquivo `SearchAlgorithms.py` implementa diversos algoritmos de busca, inclusive o BPI. Altere o código do arquivo `VacuumWorld3Room.py` para executar também o algoritmo de busca em profundidade iterativo (BPI). Qual foi o resultado encontrado pelo algoritmo BPI para este problema? Foi igual a outro resultado já apresentado? 

