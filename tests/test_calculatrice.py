import pytest
from app.calculatrice import addition, soustraction, multiplication, division, puissance, modulo

from unittest.mock import patch
from app.calculatrice import calcul_complexe

def test_addition():
    assert addition(2, 3) == 5

def test_soustraction():
    assert soustraction(5, 3) == 2

def test_multiplication():
    assert multiplication(4, 3) == 12

def test_division():
    assert division(10, 2) == 5

def test_division_zero():
    with pytest.raises(ValueError):
        division(10, 0)

def test_puissance():
    assert puissance(2, 3) == 8

def test_modulo():
    assert modulo(10, 3) == 1

def test_modulo_zero():
    with pytest.raises(ValueError):
        modulo(10, 0)

def test_calcul_complexe_mock():
    with patch('app.calculatrice.puissance') as mock_puissance:
        mock_puissance.return_value = 100  # On simule que puissance renvoie 100
        resultat = calcul_complexe(2, 3)
        assert resultat == 110  # 100 + 10
        mock_puissance.assert_called_once_with(2, 3)
