from src.Tete import soma, subtracao, multiplicacao

def testar_soma():
    assert soma(10, 5) == 15

def testar_subtracao():
    assert subtracao(10, 5) == 5

def testar_multiplicacao():
    assert multiplicacao(10, 5) == 50
