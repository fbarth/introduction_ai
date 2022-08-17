# Exercícios sobre busca em espaço de estados: parte 1

Para executar esta atividade você terá que fazer o fork do projeto [https://github.com/fbarth/introduction_ai](https://github.com/fbarth/introduction_ai). 

Assim que você tiver o projeto na sua máquina, você terá que configurar o ambiente virtual: 

````bash
python3 -m virtualenv venv
source venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
````

*Sempre use o virtualenv para organizar as dependências do seu projeto. Desta forma fica mais simples a manutenção do mesmo.*

Na pasta `code` deste projeto você irá encontrar diversos arquivos `python`. São os arquivos desta pasta que você irá utilizar neste exercício. 

## Exercício: Aspirador de Pó 

Considere o exemplo do aspirador de pó. Uma possível solução está implementada no 
arquivo [code/search/VacuumWorld.py](../code/search/VacuumWorld.py). Considerando esta implementação, execute as seguintes ações:

* acesse o diretório **code/search** e execute o comando `python VacuumWorld.py`. Qual foi a resposta fornecida pelo programa? O que esta resposta representa?

* Acesse o código `VacuumWorld.py`. Quais são os métodos definidos na classe VacuumWorld? Descreve o que você acredita que cada método realiza.

* Vá até a função `main()` do arquivo `VacuumWorld.py`. Esta função faz uso de algum algoritmo de busca? Quais? 

* Altere o estado inicial e o estado objetivo descritos no arquivo `VacuumWorld.py`, execute novamente o comando `python VacuumWorld.py` e veja o que acontece. 

* Execute o comando `pytest test_VacuumWorld.py --capture=tee-sys`. O que aconteceu? Você sabe explicar? Você saberia adicionar mais uma função de teste no arquivo `test_VacuumWorld.py`?

### Espaço com 3 quartos

Vamos implementar um Aspirador de Pó com 3 quartos? Três quartos lado-a-lado (esquerda, centro e direita)? 

Para esta atividade já temos um código pré-pronto: `VacuumWorld3Room.py`. Neste código falta completar o código de alguns métodos da classe.  

* Complete os métodos da classe e execute os dois algoritmos que estão na função main(): Busca em Largura e Busca em Profundidade. Liste as soluções encontradas por ambos os algoritmos.

* O arquivo `SearchAlgorithms.py` implementa diveros algoritmos de busca, inclusive o BPI. Altere o código do arquivo `VacuumWorld3Room.py` para executar também o algoritmo de busca em profundidade iterativo (BPI). Qual foi o resultado encontrado pelo algoritmo BPI para este problema? Foi igual a outro resultado já apresentado? 

## Exercício: soma +1 e soma +2

Considere o problema onde o estado inicial é o número 1, o estado meta é o número 10. Existem duas operações de geração de sucessores: adicionar 1 ao número do estado atual; adicionar 2 ao número do estado atual. Utilizando o código disponibilizado no arquivo [code/search/PlusOneTwo.py](../code/search/PlusOneTwo.py), faça as seguintes atividades: 

* Implemente todos os métodos necessários para que o agente possa resolver este problema. Utilize o arquivo `test_PlusOneTwo.py` para orientar a sua implementação, por exemplo, para saber que nome utilizar em cada ação do agente. 

* Qual a solução apresentada pelos algoritmos de busca em
  largura, busca em profundidade e busca em profundidade interativa?
  Quais foram ótimos? Qual foi mais rápido?

* Mude a meta para 1000 e repita as
avaliações acima. Quais foram os resultados? Qual a justificativa para tal resultado? 


## Problema da banda U2

Lembra do problema 5 da lista de exercícios sobre [algoritmos de busca](./exerciciosBusca.pdf)?

*A banda U2 tem um concerto que começa daqui a 17 minutos e
  todos precisam cruzar uma ponte para chegar lá. Todos os 4
  participantes estão do mesmo lado da ponte. É noite. Só
  há uma lanterna. A ponte suporta, no máximo, duas
  pessoas. Qualquer pessoa que passe, uma ou duas, deve passar com a
  lanterna na mão. A lanterna deve ser levada de um lado para outro
  e não ser jogada. Cada membro da banda tem um tempo diferente
  para passar de um lado para o outro. O par deve andar no tempo do
  menos veloz: Bono: 1 minuto para passar; Edge: 2 minutos para
  passar; Adam: 5 minutos para passar; e Larry: 10 minutos para
  passar.

* Crie uma classe do tipo `State` para resolver este problema. Leve em consideração as perguntas e respostas do [enunciado anterior](./exerciciosBusca.pdf) para implementar: a estrutura de dados necessária para representar os estados; as operações e como elas afetam os estados; custo de cada operação, e; outros itens relevantes para a solução do problema.

* Que algoritmos de busca você pode utilizar para resolver este problema?

* A solução encontrada pela sua implementação é ótima? 


## Conjectura de Knuth

O cientista da computação Donal Knuth em 1964 conjecturou que **todo** número inteiro positivo pode ser gerado a partir do número **4** aplicando-se uma combinação de fatorial, raiz quadrada e arredondamento para baixo. Por exemplo, o número 2 pode ser gerado por `sqrt(4)`, o número 1 por `round_down(sqrt(sqrt(4)))` e o número 5 por `round_down(sqrt(sqrt(sqrt(sqrt(sqrt(factorial(factorial(4))))))))`.

* Implemente um agente autônomo (uma classe do tipo `State`) que dado um número inteiro positivo qualquer gere uma sequência de operações que transformam o número 4 no número informado. Para orientar o desenvolvimento da sua solução sugire-se utilizar o arquivo de teste `pytest test_KnuthProblem.py --capture=tee-sys`.

* A sua implementação funciona para todos os casos? 

* Quais as limitações que devem ser consideradas na sua implementação?

## Problema do cavalo no tabuleiro de xadrez 

Lembra do problema 4 da lista de exercícios sobre [algoritmos de busca](./exerciciosBusca.pdf)?

*Considerando um tabuleiro de xadrez (8 x 8) com um único cavalo, quais os movimentos que o cavalo deve fazer para percorrer todas as posições do tabuleiro uma única vez e retornar ao ponto de partida?*

* Crie uma classe do tipo `State` para resolver este problema. Leve em consideração as perguntas e respostas do [enunciado anterior](./exerciciosBusca.pdf) para implementar: a estrutura de dados necessária para representar os estados; as operações e como elas afetam os estados; custo de cada operação, e; outros itens relevantes para a solução do problema.

* No método `main()` ou no arquivo de testes (fica a seu critério implementar um arquivo de testes ou não) gere um estado aleatório inicial toda vez que for executar o algoritmo que irá procurar por uma solução. 

* Teste diferentes algoritmos de busca e documente os resultados encontrados, incluindo o tempo de processamento. 

* Você conhece o problema do caxeiro-viajante? Qual é a relação deste problema com o problema do caxeiro-viajante?

## Problema do caminho entre cidades

Vimos em sala de aula o problema do caminho entre cidades considerando o seguinte mapa:

<p align="center">
<img src="../slides/03_algoritmos_busca/figuras/mapa.png" alt="Mapa" width="400"/>
</p>

* Implemente uma classe chamada `Map.py` do tipo `Space` que consegue identificar caminhos entre cidades deste mapa. Para estes exercícios considere os arquivos [code/search/Map.py](../code/search/Map.py) e [code/search/test_Map.py](../code/search/test_Map.py). Sugere-se iniciar este exercício executando os testes primeiro e analisando o código especificado no arquivo de teste. Claro que a primeira vez que você executar o arquivo de teste vai retornar diversos erros porque o arquivo `Map.py` está bem incompleto. A ideia deste exercício é que você preencha os métodos desta classe e teste novamente. 

* Depois de testado, quais foram os resultados? As soluções encontradas são ótimas? Você percebeu alguma mudança no tempo de processamento dependendo do objetivo desejado?

* Se este mapa fosse maior? Será que seria possível utilizar os algoritmos vistos até então para resolver o problema? 

# Próximas atividades

[[Próximas atividades](./implementacoes_busca_parte2.md)]
