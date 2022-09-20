# Revisão sobre heurística

* As heurísticas utilizadas nas implementações do *8 puzzle* e do *Mapa* são heurísticas boas? 

* O que são heurísticas **boas**? 

    * Heurísticas admissíveis.
    * Heurísticas que não são do "*contra*". 

## Atividades: 

* Atualize o seu repositório local do projeto [AI Code](https://github.com/Insper/ai_code).

### Utilizando o arquivo `Map.py` 

* altere o algoritmo de busca que deve ser utilizado. Troque o algoritmo `AEstrela` pelo `BuscaGananciosa`. A solução retornada continua sendo ótima? Explique o comportamento da solução. 

* volte a utilizar o algoritmo `AEstrela`, mas altere a heurística implementada na solução de: 

```python
def h(self):
    return int(Map.g.edges[self.city,self.goal]['distance'])
```

para: 

```python
def h(self):
    return int(Map.g.edges[self.city,self.goal]['distance']) * 1000
```

A solução continua sendo ótima? Explique o comportamento da solução. 


### Utilizando o arquivo `Puzzle8.py`

* existem duas funções `h1()` e `h2()`. Ambas as funções implementam heurísticas para o problema dos `8 puzzles`. Que heurísticas são estas? 

* execute o arquivo `Puzzle8.py` considerando: 

```python
def h(self):
    return self.h1()
```

e depois considerando:

```python
def h(self):
    return self.h2()
```

você notou alguma diferença de tempo de processamento para resolver alguns dos problemas? 

* será que é possível combinar estas duas heurísticas em uma só? Esta combinação fornece algum ganho? 

### Utilizando o arquivo `VacuumWorldGeneric.py`

* implemente uma heurística para este problema. 

* depois de implementada a heurística e utilizando o algoritmo `AEstrela`, a solução consegue encontrar respostas para configurações que antes não conseguia? 


