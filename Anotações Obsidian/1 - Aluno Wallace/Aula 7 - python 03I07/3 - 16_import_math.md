1 - criar uma nova pasta com o nome: 16_import_math.
2 - novo arquivo chamado: main.py.
3 - o terceiro programa da noite, o cliente pediu um programa para calcular a área de uma circunferência. 
4 - importar a biblioteca math.
5 - Para que o programa calcule a área de um circulo, o usuário precisa dar o valor do raio.
6 - segurar o alt gr e apertar o numero 2 para fazer m².
7 - comando usado para calcular a área do círculo:

area = math.pi * r ** 2      |  sem espaços.

------

- importação de biblioteca
import math
```python

import math
- tratamento de exceção:
try:
    while True:
        # Usuario informa valor do raio
        r = float(input("Informe o valor do raio: ").replace(",","."))
        
        # calcula a área do circulo
        area = math.pi*r**2

        # Imprime na tela a área do circulo
        print(f"Área do círculo: {area:.2f} m²")

        # Usuário informa se deseja continuar ou não
        print("1 - Calcular Área de outro círculo.")
        print("2 - Sair do programa.")

        opcao = input("Informe sua opção: ").strip()
        match opcao:
            case "1":
                continue
            case "2":
                break
            case _:
                print("Opção inválida.")
                continue

except Exception as e:
    print(f"Não foi possível calcular. {e}.")
    
    
```
