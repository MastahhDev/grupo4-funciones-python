from funciones.multiplicaconAndrada import multiplicar_andrada

def test_multiplicar_andrada():
    assert multiplicar_andrada(2, 3) == 6
    assert multiplicar_andrada(-1, 5) == -5
