# Exercícios sobre busca em espaço de estados: parte 2

Neste documento estão descritos outros problemas relacionados com busca em espaço de estados 
ou versões mais complexas dos 
problemas já apresentados na [parte 1](./implementacoes_busca_parte1.md)

## Exercício soma +1 e soma +2 com heurística

Quando você mudou o objetivo para 1000, dependendo da máquina que você estava usando, ou você teve problemas de memória,
ou demorou muito para trazer um resultado ou simplesmente não retornou nenhum resultado até o momento em que você decidiu 
interromper o processo. 

Isto aconteceu porque o tamanho da árvore é muito grande e os algoritmos de busca cegos (sistemáticos) não fazem uso de nenhum
recurso para podar a árvore de busca. Por isso que para resolver este problema é necessário fazer uso de algoritmos de busca
informados. Em outras palavras, algoritmos que fazem uso de heurísticas para escolher o melhor caminho.

* Inclua uma heurística (utilize a interface Heuristica) para a resolução do
problema. Qual a solução apresentada pelo algoritmo ganancioso? Qual é a solução apresentada pelo algoritmo A*?

* Mude a meta para 1001 e repita a execução com os algoritmos ganancioso e A*. A implementação se comportou adequadamente?

* Qual foi a heurística utilizada?

## Problema do caminho entre cidades com heurística

* Quanto tempo a solução implementada para o problema do caminho entre cidades levou para encontrar uma
solução de *i* até *x*? Gastou muito mais tempo que as demais buscas? Por que?

* Será que é possível criar uma heurística admissível para este problema? Qual seria?

* O arquivo `MapHeuristics.csv` tem, de forma implícita, uma heurística codificada. Entenda o significado desta 
heurística e utilize os dados contigos neste arquivo para definir a função `h()`. 

* Quais foram os resultados encontrados? Teve alguma diferença? Por que?

## Problema do cavalo no tabuleiro de xadrez com heurística

* Quais foram os resultados encontrados, incluindo o tempo de processamento, para a 
execução com os algoritmos de busca cegos?

* Será que é possível criar uma heurística para este problema? Caso positivo, use o algoritmo A* ou ganancioso para encontrar 
respostas para este problema. 

Referências que podem ajudar no desenvolvimento da solução:

* [Verbete na Wikipedia sobre o Problema do Cavalo](https://pt.wikipedia.org/wiki/Problema_do_cavalo)
* [Costa & Sá. Heurística eficiente para o passeio aberto do cavalo a partir de casas arbitrárias em tabuleiros 
quadrados. Simpósio Brasileiro de Pesquisa Operacional. 2013](http://www.din.uem.br/sbpo/sbpo2013/pdf/arq0328.pdf)

## As oito rainhas 

Coloque *N* rainhas em um tabuleiro de xadrez (*N x N* casas), onde *4 <= N <= 10*, 
de maneira que nenhuma rainha ameace outra, i.e., as rainhas não devem compartilhar colunas, 
linhas ou diagonais do tabuleiro.

# Próximas atividades

[[Próximas atividades](./implementacoes_busca_parte3.md)]