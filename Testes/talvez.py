from src.Tete import soma, subtracao, multiplicacao

def testar_soma():
    assert soma(10, 5) == 15

def testar_subtracao():
    assert subtracao(10, 5) == 5

def testar_multiplicacao():
    assert multiplicacao(10, 5) == 50

# Executar testes manualmente
if __name__ == "__main__":
    testar_soma()
    testar_subtracao()
    testar_multiplicacao()
    print("Todos os testes passaram!!")