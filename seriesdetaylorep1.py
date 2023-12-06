# -*- coding: utf-8 -*-
"""SeriesDeTaylorEP1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/191XeIb7XznFAHZBIyrjpys38tiepUS9c
"""

import sympy
import math
import matplotlib.pyplot as plt
import numpy as np

#SÉRIE DE TAYLOR
g = sympy.symbols('g')
arcTangente = sympy.atan(g)
serieTaylor = sympy.series(arcTangente, g, 0, 5)
print(serieTaylor)

"""# Tabela de valores mais usados (fixos)

| x (entrada) | arctan(x) (saida) |
| :---: | :---: |
| 0 | 0 |
| 1 | π/4 |
| -1 | -π/4 |
| 1.73205 | π/3 |
| -1.73205 | -π/3 |
| ∞ | π/2 |
| -∞ | -π/2 |

# Plotando Arco Tangente

| Nome | Notação 1 | Notação 2 | Definição | Domínio como função real | Imagem (em radianos) |
| :---: | :---: | :---: | :---: | :---: | :---: |
| Arco tangente | y = arctg(x) | y = tg-1(x) | x = tg(y) | R | −π/2 < y < π/2 |
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-6, 6, 400)
y = np.arctan(x)

plt.figure(figsize=(10, 4))
plt.plot(x, y, label='Arco Tangente', color='blue')
plt.xlabel('x')
plt.ylabel('arctan(x)')
plt.title('Gráfico do Arco Tangente')
plt.legend()
plt.grid()
plt.show()

"""# Series de Taylor:

$f(x) = \sum_{n = 0}^{\infty} \frac{(-1)^{n}x^{2n+1}}{2n+1}$

# Expansão da serie com x = 0:

$f(0) = x - \frac{x^{3}}{3} + \frac{x^{7}}{7} - O(x^{7})$

#Expansão da serie com x = infinito:
$f(\infty) =  \frac{\pi }{2} - \frac{1}{x} + \frac{1}{3x^{3}} - \frac{1}{5x^{5}} + O\left ( \left ( \frac{1}{x}  \right )^{7}\right )$

#Derivadas:

$f'(x) = \frac{1}{1+x^{2}}$

$f''(x) = -\frac{2x}{(1+x^{2})^{2}}$

$f'''(x) = \frac{6x^{2}-2}{(1+x^{2})^{3}}$

$f''''(x) = -\frac{24x(x^{2}-1)}{(1+x^{2})^{4}}$

$f'''''(x) = \frac{24(5x^{4}-10x^{2}+1)}{(1+x^{2})^{5}}$

# Encontrando a serie:

$f(x) = arctan(x)$

$f'(x) = \frac{1}{1+x^{2}} = \sum_{n=0}^{\infty} (-1)^{n} x^{2n}$

$arctan(x) = \int \sum_{n=0}^{\infty} (-1)^{n} x^{2n} dx = \sum_{n=0}^{\infty} (-1)^{n}\int  x^{2n}$

$arctan(x) = \sum_{n = 0}^{\infty} \frac{(-1)^{n}x^{2n+1}}{2n+1}$

Portanto:

$arctan(x) = x - \frac{x^{3}}{3} + \frac{x^{5}}{5} - \frac{x^{7}}{7} + \frac{x^{9}}{9} ...$

Esta série é convergente para todos os valores reais de x. Em outras palavras, não há um valor de N (um número finito de termos) que represente o limite exato da série, porque a série continua indefinidamente. No entanto, à medida que você adiciona mais termos à série de Taylor, ela se aproxima cada vez mais da função real arco tangente (arctan(x)).

Portanto, para calcular uma aproximação específica de arctan(x) usando a série de Taylor, você deve escolher um valor específico de N (um número finito de termos) que forneça a precisão desejada. Quanto maior o valor de N, mais precisa será a aproximação.

# Series de Taylor Simples:
"""

import matplotlib.pyplot as plt
import numpy as np
# Arco tangente simples (4 termos)
def arco_tangente_simples(x):
    return x - (x ** 3) / 3 + (x ** 5) / 5 - (x ** 7) / 7

x = np.linspace(-2, 2, 400)
y_aproximado = arco_tangente_simples(x)
y = np.arctan(x)

plt.plot(x, y_aproximado, label=f'Aproximação', color='red')
plt.plot(x, y, label='Arco Tangente Real', color='blue')
plt.xlabel('x')
plt.ylabel('arctan(x)')
plt.title('Gráfico do Arco Tangente e sua Aproximação')
plt.legend()
plt.grid()
plt.show()

# Valores de entrada comuns
valores_de_x = [-1, -0.5, -0.1 ,0, 0.1 ,0.2 ,0.3 ,0.4 , 0.5 , 0.6, 0.7, 0.8, 0.9, 1]

# Imprimir a tabela com os resultados
print("Valor de x\tTangente Inversa Real\tTangente Inversa Aproximada")
print("-" * 60)
for x in valores_de_x:
    real_tan_inv = np.arctan(x)
    approx_tan_inv = arco_tangente_simples(x)
    print(f"{x}\t\t{real_tan_inv}\t\t{approx_tan_inv}")

"""# Definindo uma Série de Taylor com n arbitrário:"""

import numpy as np
import matplotlib.pyplot as plt
# Arco tangente com n arbitrario
def arco_tangente(x, n):
    resultado = 0
    sinal = 1

    for i in range(1, n+1):
        termo = sinal * (x ** (2 * i - 1)) / (2 * i - 1)
        resultado += termo
        sinal *= -1

    return resultado

x = 0.5 #Valor de x para arctan(x)
n = 4 #Numero de termos
# Resultado da funcao arco_tangente
resultado_aproximado = arco_tangente(x, n)
#resultado_aproximado_simples = arco_tangente_simples(x)

# Compara com o valor real do arco tangente
resultado_real = np.arctan(x)


#print(f"Valor aproximado simples: {resultado_aproximado_simples}")
print(f"Valor aproximado: {resultado_aproximado}")
print(f"Valor real: {resultado_real}")

x = np.linspace(-2, 2, 1000)
y1 = arco_tangente(x, n)
y2 = np.arctan(x)


fig, ax = plt.subplots()
fig.set_size_inches(20, 8)
ax.plot(x, y1, label='numpy.arctan', linewidth=2.0)
ax.plot(x, y2, label='arco_tangente', linewidth=2.0)
ax.grid()
ax.legend()
plt.title('Função arco tangente vs. arco_tangente')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

"""# Definindo uma Série de Taylor otimizada com n arbitrário:"""

import numpy as np

def arco_tangente_otimizado(x, numMax=20):
    arcotan = x
    term = x

    for n in range(1, numMax):
        term = -term * x * x
        arcotan += term / (2 * n + 1)

    return arcotan


# Exemplo de uso:
x = 0.5
resultado = arco_tangente_otimizado(x)
print(f'atan({x}) = {resultado}')

import timeit
import numpy as np

x = 0.5

# Medição de tempo para a função otimizada arco tangente
comeco = timeit.default_timer()
arco_tangente_otimizado_resultado = arco_tangente_otimizado(x)
time_arco_tangente_otimizado = (timeit.default_timer() - comeco) * 1000  # Tempo em milissegundos

# Medição de tempo para a função numpy.arctan
comeco_numpy = timeit.default_timer()
numpy_arco_tangente_resultado = np.arctan(x)
time_numpy_arco_tangente = (timeit.default_timer() - comeco_numpy) * 1000  # Tempo em milissegundos

# Imprimir os resultados e tempos de execução
print("arctan(0.5) - numpy:", numpy_arco_tangente_resultado)
print("arctan(0.5) - otimizado:", arco_tangente_otimizado_resultado)
print('Tempo para calcular arco tangente otimizado:', time_arco_tangente_otimizado, 'milissegundos')
print('Tempo para calcular arco tangente usando numpy:', time_numpy_arco_tangente, 'milissegundos')

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2, 2, 1000)  # Altere os limites para o seu intervalo desejado
y1 = np.arctan(x)
y2 = arco_tangente_otimizado(x)  # Certifique-se de que a função atan_otimizado esteja definida

fig, ax = plt.subplots()
fig.set_size_inches(20, 8)
ax.plot(x, y1, label='numpy.arctan', linewidth=2.0)
ax.plot(x, y2, label='arco_tangente_otimizado', linewidth=2.0)
ax.grid()
ax.legend()
plt.title('Função arco tangente vs. arco_tangente_otimizado')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

# Valores de entrada comuns
valores_de_x = [-1, -0.5, -0.1 ,0, 0.1 ,0.2 ,0.3 ,0.4 , 0.5 , 0.6, 0.7, 0.8, 0.9, 1]

# Imprimir a tabela com os resultados
print("Valor de x\tTangente Inversa Real\tTangente Inversa Aproximada")
print("-" * 60)
for x in valores_de_x:
    real_tan_inv = np.arctan(x)
    approx_tan_inv = arco_tangente_otimizado(x)
    print(f"{x}\t\t{real_tan_inv}\t\t{approx_tan_inv}")

# Valores de entrada comuns
valores_de_x = [0, np.sqrt(3)/3, 1]

# Imprimir a tabela com os resultados
print("Valor de x\tTangente Inversa Real\tTangente Inversa Aproximada")
print("-" * 60)
for x in valores_de_x:
    real_tan_inv = np.arctan(x)
    approx_tan_inv = arco_tangente_otimizado(x)
    print(f"{x}\t\t{real_tan_inv}\t\t{approx_tan_inv}")

"""Referencias:

https://www.wolframalpha.com/input?i=taylor+expansion+of+arctan%28x%29

https://www.geogebra.org/m/ZuxmRuua
"""