1 - criar uma nova pasta com o nome: 17_arquivos.
2 - dentro dela o arquivo main.py
3 - dentro da pasta 17_arquivos, criar uma nova pasta com o nome arquivos.
4 - o Objetivo desse programa: criar um arquivo de texto, o usuário vai criar um arquivo de texto, vamos trabalhar com persistência, salvar dados, vai gravar um arquivo de texto em em um arquivo na pasta arquivos, e nunca será apagado, se o usuário sair, o arquivo vai continuar lá.
5 - vamos trabalhar com a biblioteca os.
6 - vai poder criar um texto, vai poder ler o texto dentro do programa, e sair do programa. ele pode criar um arquivo de texto 

7 - esse comando limpa o terminal: 

import os
os.system("cls" if os.name == "nt" else "clear")


8 - vamos criar um loop infinito, que o usuário escolhe quando sair:
9 - primeira informação o nome gravação do texto a ser gravado
10 - depois pede o nome do arquivo.
11 - para gravar um arquivo não é difícil, precisa apenas de identação pois é difícil,
12 - O comando with serve para gravar um texto.

13 - "w" significa: escrever with.
14 - sempre que for usar o comando de gravar arquivo usar o comando:

with open(f"17_arquivos/arquivos/{nome_arquivo}.txt", "w", encoding="utf-8") as f:

15 - ele serve para localizar a pasta que você quer localizar os arquivos, coloque dentro sempre o caminho separando as pastas por / 

"w" vai escrever no arquivo.
"r" vai ler o arquivo.

with open(f"17_arquivos/arquivos/{nome_arquivo}.txt", "w", encoding="utf-8") as f:
with open(f"17_arquivos/Arquivos/{nome_arquivo}.txt", "r", encoding="utf-8") as f:

16 - esse codigo funciona para outras extensões como .texto nativamente mas para outras extensões é preciso de outras bibliotecas.








