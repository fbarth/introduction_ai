# Desenvolvendo um agente para atuar em ambiente multi-agente e competitivo

O escopo desta implementação é desenvolver um agente jogador de uma variante de Liga4 chamada *Connect4 PopOut*. O tabuleiro desta variante tem as mesmas dimensões que o Liga4 convencional, as peças continuam sendo as mesmas e o objetivo também. No entanto, durante cada jogada, o jogador pode ou adicionar um novo disco no topo ou remover um disco seu da base (o que chamamos de *pop out*). Ao fazer isto, todos os discos que estão na mesma coluna que o disco que foi removido irão descer uma linha, mudando a sua relação com os demais discos presentes no tabuleiro. Neste [vídeo](https://www.youtube.com/watch?v=Pjmysp7FzGs) é possível ver uma explicação desta variante e de outras variantes do jogo. 


Neste projeto, cada grupo de alunos (no máximo 3) irá implementar um jogador para *Connect4 PopOut* respeitando esta [interface](https://github.com/Insper/ai_code/blob/main/src/games/fourinrow_popout/Player.py):

````python
class Player(ABC): 

    @abstractmethod
    def move(self, player_code, board):
        pass

    @abstractmethod
    def name(self):
        pass
````

O método `move` retorna dois valores que indicam se o agente deve colocar o disco no topo ou remover da base e em qual coluna isto deve ser feito. Como exemplo, podemos utilizar o código do [agente aleatório](https://github.com/Insper/ai_code/blob/main/src/games/fourinrow_popout/RandomPlayer.py):

````python
    def move(self, player_code, board):
        x = randint(0,13)
        if x < 7:
            return None, x
        else:
            p = x - 7
            if self.bottomDiscExist(player_code, board, p):
                return 'p', p
            else: 
                return None, randint(0, 6)
````

Para informar que a decisão do agente é colocar um disco no topo então deve-se retornar `None, X`. Se o movimento do agente é remover um disco da base então deve-se retornar `'p', X`. **Cuidado**: você só pode remover um disco da base se este disco for seu!

## Restrições que devem ser consideradas

Ao implementar este agente você deve considerar algumas restrições:

* A duração de nenhum movimento deverá ultrapassar **10 segundos**. 

* O seu agente não deverá fazer nenhuma jogada inválida: 
    * jogar um disco em uma coluna que não existe; 
    * remover um disco que não existe; 
    * remover um disco do oponente, ou; 
    * jogar um disco em uma coluna que já está completa. 

* O seu agente **não** pode perder nenhuma partida para o jogador aleatório. 

Se o seu agente realizar qualquer um destes movimentos durante a competição então ele será desclassificado da competição. 

## Referências

Para implementar o seu agente você poderá fazer uso de diversas referências, como por exemplo: 

* [artigo do Shannon](https://archive.computerhistory.org/projects/chess/related_materials/text/2-0%20and%202-1.Programming_a_computer_for_playing_chess.shannon/2-0%20and%202-1.Programming_a_computer_for_playing_chess.shannon.062303002.pdf): neste artigo, além de discutir o uso do algoritmo min-max para Xadrez, ele também apresenta um rascunho de função de avaliação para o Xadrez. Não é uma função de avaliação para o Connect4, mas pode ajudar. 

* [Research on Different Heuristics for Minimax Algorithm Insight from Connect-4 Game](https://pdfs.semanticscholar.org/f323/3fa36a5026b42c7f331a5c98e66aad9d3e8c.pdf). Este já é um artigo bem específico para o problema do jogo Connect-4. No entanto, ele analisa funções de utilidades e heurísticas para a versão padrão do jogo. 

* [A Knowledge-Based Approach of Connect-Four](https://content.iospress.com/articles/icga-journal/icg11-4-10). O link para o texto completo está [aqui](http://www.informatik.uni-trier.de/~fernau/DSL0607/Masterthesis-Viergewinnt.pdf)

* [Checkers is solved](https://www.science.org/doi/10.1126/science.1144079). Artigo publicado na Science sobre o tema "Teoria de Jogos". O link para o texto completo está [aqui](https://www.researchgate.net/publication/231216842_Checkers_Is_Solved).

* [Verbete da Wikipedia sobre Connect4](https://en.wikipedia.org/wiki/Connect_Four).

* [Verbete da wikipedia sobre função de avaliação](https://en.wikipedia.org/wiki/Evaluation_function).

* [Documentação sobre a função de avaliação utilizada pelo stockfish](https://stockfishchess.org/blog/2020/introducing-nnue-evaluation/).

* [Material sobre como implementar um robô jogador de Connect4](http://fbarth.net.br/Connect4-Python/).

* [Implementações sobre Busca Competitiva neste repositório](./code/games/README.md).

## Entregas

Ao final do projeto, o grupo de alunos deverá entregar dois artefatos: 

* código do agente jogador pronto para participar do torneio, e;

* uma documentação que explica em alto nível as principais decisões de projeto e responde algumas perguntas conceituais. 


### Documentação e questões referentes ao projeto

1. Que algoritmo deve ser utilizado para desenvolver um agente jogador de *Connect4 PopOut* vencedor? Deve-se utilizar uma implementação de Min-Max com poda alpha-beta? Se sim, qual a profundidade que deverá ser utilizada para evitar processamentos superiores a 5 segundos por jogada? Qual a função de utilidade que deve ser utilizada? 

1. O seu jogador faz uso de alguma base de conhecimento? Se sim, como ela é utilizada durante o processo de tomada de decisão? 

1. Qual a sua expectativa com relação ao desempenho do seu agente? Você acredita que ele irá desempenhar bem na competição? Por que? Você executou testes contra outros jogadores? Qual foram os resultados? 

1. Quais foram as principais referências utilizadas para a implementação do seu jogador? 

1. Existem diferenças significativas entre um jogador de *Connect4* e um jogador de *Connect4 PopOut* em termos de árvore de busca e função de avaliação? É possível utilizar o jogador implementado para o *Connect4 PopOut* em competições de *Connect4* sem muitas modificações? 

A documentação entregue precisa responder todas as perguntas acima. As respostas para as perguntas de uma forma geral precisam ser baseadas em evidências, de preferência dados vindos de experimentos. Principalmente, as respostas para as perguntas 4 e 6.

### Rubrica da avaliação 

| Conceito | Definição |
|:---------|:----------|
| Insuficiente (I) | Não respondeu nem 50% das perguntas. |
| Em Desenvolvimento (D) | Não respondeu todas as perguntas. |
| Básico (C) | Respondeu todas as perguntas mas de forma muito supercial. |
| Esperado (B) | Respondeu todas as perguntas de forma completa, citando todas as referências, mas não apresentou dados que justificam algumas das respostas. |
| Avançado (A+) | Respondeu todas as perguntas de forma completa, citando todas as referências e apresentando todos os dados necessários para as respostas fornecidas. |


## Competição

As equipes terão até o dia **20/10/2022** para entregar a implementação dos seus jogadores e documentação. Todos os artefatos produzidos pela equipe devem ser entregues via GitHub classroom neste link: [https://classroom.github.com/a/dzylf8ZF](https://classroom.github.com/a/dzylf8ZF).

No dia **21/10/2022** (sexta-feira) o professor irá organizar as implementações e executar uma competição onde todos os jogadores irão jogar em um campeonato todos contra todos com turno e returno: `python Tournament.py`. O código fonte da lógica do torneio está [aqui](https://github.com/Insper/ai_code/blob/main/src/games/fourinrow_popout/Tournament.py).

A execução desta competição não será feita em sala de aula pois dado o número de equipes irá demorar mais que 2 horas para finalizar. O professor irá disponibilizar o log da competição para que todos os alunos possam analisar o comportamento dos seus jogadores. 

O jogador que tiver o maior número de pontos será o campeão do torneio. Abaixo segue a tabela convertendo a colocação na competição com o conceito no projeto:

| Colocação | Definição |
|:---------|:----------|
| Primeiro lugar | A+ |
| Segundo lugar  | A |
| Terceiro lugar | B |
| Demais jogadores | C |
| Jogadores que cometeram alguma infração | I | 


## Nota final do projeto

A nota final do projeto será uma média simples entre a nota da documentação e a nota da competição. 