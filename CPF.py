"""
Elaborar um programa que solicite a digitação de um número de CPF no formato xxx.xxx.xxx-xx e indique se é um número válido ou inválido através da validação dos dígitos verificadores e dos caracteres de formatação.

https://dicasdeprogramacao.com.br/algoritmo-para-validar-cpf/
"""
import math

somaDigitos = 0
somaDigitos2 = 0
j = 10
c = 11

cpfOrigin = input("Digite seu CPF: ")

cpfList = list(cpfOrigin)

if cpfList ==14:
    cpfList.remove('.')
    cpfList.remove('.')
    cpfList.remove('-')

cpfNum = list(map(int, cpfList))

print("\n", cpfNum)

for i in range(0, 9, 1):
    #print(cpfNum[i], "*", j)
    soma1 = cpfNum[i] * j
    somaDigitos += soma1
    j = j - 1

resto1 = (somaDigitos * 10) % 11
resto1 = math.ceil(resto1)

for i in range(0, 10, 1):
    #print(cpfNum[i], "*", c)
    soma2 = cpfNum[i] * c
    somaDigitos2 += soma2
    c = c - 1

resto2 = (somaDigitos2 * 10) % 11
resto2 = math.ceil(resto2)

print("\nResto 01: ",resto1)
print("\nResto 02: ",resto2)

if (resto1 == cpfNum[9]) and (resto2 == cpfNum[10]):
    print("\nCPF válido")
else:
    print("\nCPF inválido")
