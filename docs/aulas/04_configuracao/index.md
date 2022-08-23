# Configuração do ambiente

Para executar esta atividade você terá que fazer o fork do projeto [https://github.com/fbarth/introduction_ai](https://github.com/fbarth/introduction_ai). 

Recomenda-se fortemente que todo estudante faça estas atividades em sua máquina. Os problemas podem ser discutidos em grupo, no entanto, cada aluno precisa ter a sua própria implementação. 

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
arquivo [code/search/VacuumWorld.py](https://github.com/fbarth/introduction_ai/blob/master/code/search/VacuumWorld.py). Considerando esta implementação, execute as seguintes ações:

* acesse o diretório **code/search** e execute o comando `python VacuumWorld.py`. Qual foi a resposta fornecida pelo programa? O que esta resposta representa? Por que as respostas são diferentes?

* Acesse o código `VacuumWorld.py`. Quais são os métodos definidos na classe VacuumWorld? Descreve o que você acredita que cada método realiza.

* Vá até a função `main()` do arquivo `VacuumWorld.py`. Esta função faz uso de algum algoritmo de busca? Quais? 

* Altere o estado inicial e o estado objetivo descritos no arquivo `VacuumWorld.py`, execute novamente o comando `python VacuumWorld.py` e veja o que acontece. 

* Execute o comando `pytest test_VacuumWorld.py --capture=tee-sys`. O que aconteceu? Você sabe explicar? Você saberia adicionar mais uma função de teste no arquivo `test_VacuumWorld.py`?

??? warning "O que são algoritmos de busca?"

    * Algoritmo de Busca em Largura
    * Algoritmo de Busca em Profundidade
    * Algoritmo de Busca de Custo Uniforme
    * Algoritmo de Busca em Profundidade Iterativo

## Espaço com 3 quartos

Vamos implementar um Aspirador de Pó com 3 quartos? Três quartos lado-a-lado (esquerda, centro e direita)? 

Para esta atividade já temos um código pré-pronto: `VacuumWorld3Room.py`. Neste código falta completar o código de alguns métodos da classe.  

* Complete os métodos da classe e execute os dois algoritmos que estão na função main(): Busca em Largura e Busca em Profundidade. Liste as soluções encontradas por ambos os algoritmos.

* O arquivo `SearchAlgorithms.py` implementa diversos algoritmos de busca, inclusive o BPI. Altere o código do arquivo `VacuumWorld3Room.py` para executar também o algoritmo de busca em profundidade iterativo (BPI). Qual foi o resultado encontrado pelo algoritmo BPI para este problema? Foi igual a outro resultado já apresentado? 

## Aspirador de pó em uma casa configurável

**Que tal implementar um aspirador de pó que consegue atuar em qualquer casa retangular?** 

Utilize como exemplo o arquivo `code/search/ProblemSpecificationExample.py` para implementar a classe `VacuumWorldGeneric.py`. O método `main` da classe `VacuumWorldGeneric.py` deve receber um arquivo texto que descreve a situação do ambiente e as posições do robô como parâmetros. Por exemplo, para o seguinte ambiente: 

<img src="img/mundo_ex_1.png">

O seguinte arquivo de configuração será entregue: 

```text
L;S;S;S
L;L;L;L
S;S;S;S
```

E o seguinte comando deve ser executado:

```bash
python VacuumWorldGeneric.py configuracao.txt 0 0
``` 

As ações que o robô (agente) sabe executar são: 

* *esq*: ir para a esquerda;
* *dir*: ir para a direita;
* *baixo*: ir para baixo;
* *cima*: ir para cima;
* *limpar*: limpar o quarto onde está.

Ao executar o comando acima, o programa deverá gerar uma sequência de ações que fará com que o robô saia do **estado inicial** e chegue em um **estado final** válido. Um estado final válido é um estado onde todos os quartos (quadrados) estão limpos. 

Uma sequência de ações válida para resolver o estado acima é: 

```
esq; limpar; esq; limpar; esq; baixo; baixo; limpar; dir; limpar; dir; limpar; dir; limpar
```

### Um outro exemplo 

Considere um novo exemplo:

<img src="img/mundo_ex_2.png">

Para este exemplo o arquivo de configuração precisa ter este conteúdo:

```text
L;S;S;S
L;L;S;S
S;S;S;S
```

E a chamada para o programa: 

```bash
python VacuumWorldGeneric.py configuracao.txt 1 3
```

O programa que você irá implementar não precisa se preocupar com a validação dos dados de entrada. Assume-se que os dados de entrada estão corretos, por exemplo, a posição do robô é uma posição válida. 

**A única tarefa que o programa deve fazer é se existir solução então retornar uma sequência de ações ótima para o problema. Se não existir solução então informar que não existe solução.**
