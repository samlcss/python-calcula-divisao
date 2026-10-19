# -*- coding: utf-8 -*-
"""
Calculadora de divisão entre dois números com tratamento
de exceções (try / except) para divisão por zero e valores inválidos.
"""

print("* * * CALCULADORA DE DIVISÃO * * *\n")

try:
    numero1 = float(input("Entre com o primeiro número: "))
    numero2 = float(input("Entre com o segundo número: "))
    resultado = numero1 / numero2
    print(f"O resultado é: {resultado}")
except ValueError:
    print("Valor inválido! Por favor, digite apenas números.")
except ZeroDivisionError:
    print("Não é possível realizar divisão por zero!")

input("\nPressione Enter para sair...")
