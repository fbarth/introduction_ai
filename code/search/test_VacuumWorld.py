from SearchAlgorithms import BuscaLargura
from SearchAlgorithms import BuscaProfundidade
from SearchAlgorithms import BuscaProfundidadeIterativa
from VacuumWorld import VacuumWorld

def test_largura():
    state = VacuumWorld('left', True, False, '')
    algorithm = BuscaLargura()
    result = algorithm.search(state)
    print(f'\nEstado inicial = {state.env()}')
    print(f'Solução = {result.show_path()}')
    assert result.show_path() == " ; Move Right ; clean ; Move Left"

def test_largura2():
    state = VacuumWorld('left', True, True, '')
    algorithm = BuscaLargura()
    result = algorithm.search(state)
    print(f'\nEstado inicial = {state.env()}')
    print(f'Solução = {result.show_path()}')
    assert result.show_path() == ""

def test_profundidade():
    state = VacuumWorld('left', True, False, '')
    algorithm = BuscaProfundidade()
    result = algorithm.search(state, 10)
    print(f'\nEstado inicial = {state.env()}')
    print(f'Solução = {result.show_path()}')
    assert result.show_path() == " ; clean ; clean ; clean ; clean ; clean ; clean ; clean ; Move Right ; clean ; Move Left"

def test_BPI():
    state = VacuumWorld('left', True, False, '')
    algorithm = BuscaProfundidadeIterativa()
    result = algorithm.search(state)
    print(f'\nEstado inicial = {state.env()}')
    print(f'Solução = {result.show_path()}')
    assert result.show_path() == " ; Move Right ; clean ; Move Left"