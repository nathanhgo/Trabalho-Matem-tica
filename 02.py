import math
import numpy as np
import matplotlib.pyplot as plt

def circulo_trigonometrico():
    angles_degrees = np.arange(0, 361, 1)  # Ângulos de 0 a 360 graus
    angles_radians = np.radians(angles_degrees)  # Converter para radianos

    # Valores de seno e cosseno
    sin_values = np.sin(angles_radians)
    cos_values = np.cos(angles_radians)

    # Criar o gráfico do ciclo trigonométrico
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.plot(cos_values, sin_values, label='Ciclo Trigonométrico')

    # Adicionar os ângulos principais
    principal_angles = [0, 90, 180, 270, 360]
    for angle in principal_angles:
        rad = np.radians(angle)
        ax.scatter(np.cos(rad), np.sin(rad), color='red')
        ax.text(np.cos(rad) * 1.1, np.sin(rad) * 1.1, f'{angle}°', fontsize=12, ha='center')

    # Configurar o gráfico
    ax.axhline(0, color='black',linewidth=0.5)
    ax.axvline(0, color='black',linewidth=0.5)
    ax.set_xlim([-1.5, 1.5])
    ax.set_ylim([-1.5, 1.5])
    ax.set_aspect('equal')
    ax.set_xlabel('Cosseno (x)')
    ax.set_ylabel('Seno (y)')
    ax.set_title('Ciclo Trigonométrico')

    plt.grid(True)
    plt.legend()
    plt.show()

def circulo_trigonometrico2():
    angles_degrees = np.arange(0, 361, 1)  # Ângulos de 0 a 360 graus
    angles_radians = np.radians(angles_degrees)  # Converter para radianos

    # Valores de seno e cosseno
    sin_values = np.sin(angles_radians)
    cos_values = np.cos(angles_radians)

    # Criar o gráfico do ciclo trigonométrico
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.plot(cos_values, sin_values, label='Ciclo Trigonométrico')

    # Adicionar os ângulos principais
    principal_angles = [0, 30, 45, 60, 90, 120, 135, 150, 180, 210, 225, 240, 270, 300, 315, 330, 360]
    for angle in principal_angles:
        rad = np.radians(angle)
        ax.scatter(np.cos(rad), np.sin(rad), color='red')
        ax.text(np.cos(rad) * 1.1, np.sin(rad) * 1.1, f'{angle}°', fontsize=10, ha='center')

    # Configurar o gráfico
    ax.axhline(0, color='black', linewidth=0.5)  # Eixo x
    ax.axvline(0, color='black', linewidth=0.5)  # Eixo y
    ax.set_xlim([-1.5, 1.5])
    ax.set_ylim([-1.5, 1.5])
    ax.set_aspect('equal')
    ax.set_xlabel('Cosseno (x)')
    ax.set_ylabel('Seno (y)')
    ax.set_title('Ciclo Trigonométrico')

    plt.grid(True)
    plt.legend()
    plt.show()

def calc_sen_cos():    
    # Calcular o seno e cosseno
    angulo_usuario = float(input("Digite um ângulo em graus: "))
    seno = np.around(np.sin(math.radians(angulo_usuario)), decimals=2)
    cosseno = np.around(np.cos(math.radians(angulo_usuario)), decimals=2)

    # Imprimir os resultados
    print(f"Seno de {angulo_usuario}°: {seno}")
    print(f"Cosseno de {angulo_usuario}°: {cosseno}")

def funcao_seno():
    x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)  # Valores de x de 0 a 2π
    y = np.sin(x)  # Valores de y usando a função seno

    plt.plot(x, y, label='Seno(x)', color='blue')
    plt.title("Gráfico da Função Seno")
    plt.xlabel("x (radianos)")
    plt.ylabel("Seno(x)")
    plt.axhline(0, color='black',linewidth=0.5)
    plt.axvline(0, color='black',linewidth=0.5)
    plt.grid(True)
    plt.legend()
    plt.show()

def graus_para_radianos():
    angulo = float(input("Digite um número em graus: "))
    angulo_radianos = np.radians(angulo)
    print(f"{angulo} graus correspondem a {angulo_radianos} radianos")

def funcao_cosseno():
    x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)  # Valores de x de 0 a 2π
    y = np.cos(x)  # Valores de y usando a função seno

    plt.plot(x, y, label='Cosseno(x)', color='blue')
    plt.title("Gráfico da Função Cosseno")
    plt.xlabel("x (radianos)")
    plt.ylabel("Cosseno(x)")
    plt.axhline(0, color='black',linewidth=0.5)
    plt.axvline(0, color='black',linewidth=0.5)
    plt.grid(True)
    plt.legend()
    plt.show()

def exibir_opcoes():
    print("\n" + "=" * 50)
    print("[1] - Construir no gráfico o ciclo trigonométrico")
    print("[2] - Construir no gráfico a função seno")
    print("[3] - Construir no gráfico a função cosseno")
    print("[4] - Converter ângulo em graus para radianos")
    print("[5] - Calcular o seno e cosseno de um ângulo")
    print("[6] - Sair\n")
    return int(input("Escolha uma opção: "))

def menu():
    try:
        escolha = exibir_opcoes()
        print(f"\nOpção escolhida: {escolha}")
        if escolha == 1:
            circulo_trigonometrico2()
        elif escolha == 2:
            funcao_seno()
        elif escolha == 3:
            funcao_cosseno()
        elif escolha == 4:
            graus_para_radianos()
        elif escolha == 5:
            calc_sen_cos()
        elif escolha == 6:
            quit()
        else:
            print("Opção inválida. Tente novamente.")
    except ValueError:
        print("Erro: Entrada inválida. Digite um número correspondente às opções.")

def main():
    if __name__ == '__main__':
        while True:
            menu()

main()