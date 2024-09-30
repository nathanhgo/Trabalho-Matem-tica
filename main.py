import math
import numpy as np
import matplotlib.pyplot as plt

def circulo_trigonometrico():
    angulos_grau = list(range(0, 360))
    angulos_rad = []
    for angulo in angulos_grau:
        angulos_rad.append(graus_para_radianos(angulos_grau[angulo]))

    # Valores de seno e cosseno
    valor_sen, valor_cos = [], []
    for angulo in angulos_grau:
        valor_sen.append(calc_sen(angulos_grau[angulo]))
        valor_cos.append(calc_cos(angulos_grau[angulo]))

    # Criar o gráfico do ciclo trigonométrico
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.plot(valor_cos, valor_sen, label='Ciclo Trigonométrico')

    # Adicionar os ângulos principais
    angulos_principais = [0, 30, 45, 60, 90, 120, 135, 150, 180, 210, 225, 240, 270, 300, 315, 330, 360]
    for angulo in angulos_principais:
        ax.scatter(calc_cos(angulo), calc_sen(angulo), color='red')
        ax.text(calc_cos(angulo) * 1.1, calc_sen(angulo) * 1.1, f'{angulo}°', fontsize=10, ha='center')

    # Configurar o gráfico
    ax.axhline(color='black', linewidth=0.5)  # Eixo x
    ax.axvline(color='black', linewidth=1)  # Eixo y
    ax.set_xlim([-1.5, 1.5])
    ax.set_ylim([-1.5, 1.5])
    ax.set_aspect('equal')
    ax.set_xlabel('Cosseno (x)')
    ax.set_ylabel('Seno (y)')
    ax.set_title('Ciclo Trigonométrico')

    plt.grid(True)
    plt.legend()
    plt.show()

def calc_sen(angulo_usuario):    
    return math.sin(graus_para_radianos(angulo_usuario))

def calc_cos(angulo_usuario):
    return math.cos(graus_para_radianos(angulo_usuario))

def graus_para_radianos(angulo):
    return angulo * math.pi / 180

def main():
    print('-='*10, 'CÍRCULO TRIGONOMÉTRICO' ,'-='*10)

    escolha = int(input("Deseja ver o círculo trigonométrico ou calcular o seno/cosseno de um ângulo? (1 ou 2): "))
    match escolha:
        case 1:
            print('Círculo trigonométrico aberto.')
            circulo_trigonometrico()
        case 2:
            angulo = float(input("Digite um número em graus: "))
            print('Angulo em Radianos: ', round(graus_para_radianos(angulo), 5))
            print('Seno: ', round(calc_sen(angulo), 2))
            print('Cosseno: ', round(calc_cos(angulo), 2))

main()