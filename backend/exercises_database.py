# -*- coding: utf-8 -*-
"""
Database of Python exercises covering basic concepts to data structures
"""

import itertools

# IDs únicos globais para todos os exercícios
_id_counter = itertools.count(1)

def _with_global_id(exlist):
    for ex in exlist:
        ex["id"] = next(_id_counter)
    return exlist

EXERCISES_DATABASE = {
    # PRINCÍPIOS BÁSICOS (1-20)
    "basic": _with_global_id([
        {
            # "id": 1,  # removido, será atribuído automaticamente
            "title": "Hello World",
            "difficulty": "beginner",
            "topic": "output",
            "instructions": "Imprima 'Hello, World!' na tela.",
            "starter_code": "# Escreva seu código aqui\nprint('Hello, World!')",
            "expected_output": "Hello, World!",
            "hints": ["Use a função print()", "Coloque o texto entre aspas"]
        },
        {
            # "id": 2,
            "title": "Variáveis Simples",
            "difficulty": "beginner",
            "topic": "variables",
            "instructions": "Crie uma variável chamada 'nome' e atribua seu nome a ela. Depois imprima a variável.",
            "starter_code": "# Crie uma variável chamada 'nome' e atribua seu nome\n# Depois imprima a variável\n",
            "expected_output": "Seu nome aqui",
            "hints": ["Use o operador de atribuição =", "Use print() para exibir a variável"]
        },
        {
            # "id": 3,
            "title": "Operações Matemáticas",
            "difficulty": "beginner",
            "topic": "operators",
            "instructions": "Crie duas variáveis com números e calcule sua soma, subtração, multiplicação e divisão.",
            "starter_code": "# Crie duas variáveis com números\n# Calcule e imprima: soma, subtração, multiplicação e divisão\n",
            "expected_output": "Soma: X\nSubtração: Y\nMultiplicação: Z\nDivisão: W",
            "hints": ["Use +, -, *, / para operações", "Use print() para cada resultado"]
        },
        {
            # "id": 4,
            "title": "Entrada do Usuário",
            "difficulty": "beginner",
            "topic": "input",
            "instructions": "Peça ao usuário para digitar seu nome e idade, depois imprima uma mensagem personalizada.",
            "starter_code": "# Use input() para receber dados do usuário\n# Imprima uma mensagem personalizada\n",
            "expected_output": "Olá [nome], você tem [idade] anos!",
            "hints": ["Use input() para receber dados", "Use f-strings ou format() para formatação"]
        },
        {
            "id": 5,
            "title": "Tipos de Dados",
            "difficulty": "beginner",
            "topic": "data_types",
            "instructions": "Crie variáveis de diferentes tipos (int, float, string, bool) e imprima seus tipos.",
            "starter_code": "# Crie variáveis de diferentes tipos\n# Use type() para verificar o tipo\n",
            "expected_output": "<class 'int'>\n<class 'float'>\n<class 'str'>\n<class 'bool'>",
            "hints": ["Use type() para verificar tipos", "Crie: número inteiro, decimal, texto, booleano"]
        },
        {
            "id": 6,
            "title": "Conversão de Tipos",
            "difficulty": "beginner",
            "topic": "type_conversion",
            "instructions": "Converta uma string numérica para int e float, depois imprima os resultados.",
            "starter_code": "# Converta a string '123' para int e float\n",
            "expected_output": "123 <class 'int'>\n123.0 <class 'float'>",
            "hints": ["Use int() e float() para conversão", "Use type() para verificar o resultado"]
        },
        {
            "id": 7,
            "title": "Formatação de Strings",
            "difficulty": "beginner",
            "topic": "string_formatting",
            "instructions": "Use f-strings para criar uma mensagem formatada com nome e idade.",
            "starter_code": "# Use f-strings para formatação\nnome = 'João'\nidade = 25\n",
            "expected_output": "Olá João, você tem 25 anos!",
            "hints": ["Use f'texto {variável}' para f-strings", "Inclua as variáveis na string"]
        },
        {
            "id": 8,
            "title": "Operadores de Comparação",
            "difficulty": "beginner",
            "topic": "comparison",
            "instructions": "Compare dois números usando operadores de comparação e imprima os resultados.",
            "starter_code": "# Compare dois números usando ==, !=, <, >, <=, >=\n",
            "expected_output": "5 == 3: False\n5 != 3: True\n5 > 3: True",
            "hints": ["Use ==, !=, <, >, <=, >=", "Imprima cada comparação"]
        },
        {
            "id": 9,
            "title": "Operadores Lógicos",
            "difficulty": "beginner",
            "topic": "logical_operators",
            "instructions": "Use operadores lógicos (and, or, not) com valores booleanos.",
            "starter_code": "# Use and, or, not com valores True e False\n",
            "expected_output": "True and False: False\nTrue or False: True\nnot True: False",
            "hints": ["Use and, or, not", "Teste com True e False"]
        },
        {
            "id": 10,
            "title": "Módulo Math",
            "difficulty": "beginner",
            "topic": "modules",
            "instructions": "Importe o módulo math e use algumas de suas funções (sqrt, pow, pi).",
            "starter_code": "# Importe o módulo math e use sqrt, pow, pi\n",
            "expected_output": "Raiz quadrada de 16: 4.0\n2 elevado a 3: 8.0\nValor de pi: 3.141592653589793",
            "hints": ["Use import math", "Use math.sqrt(), math.pow(), math.pi"]
        }
    ]),
    
    # ESTRUTURAS CONDICIONAIS (21-40)
    "conditionals": [
        {
            "id": 21,
            "title": "If Básico",
            "difficulty": "beginner",
            "topic": "if_statement",
            "instructions": "Crie um programa que verifica se um número é positivo e imprime uma mensagem.",
            "starter_code": "# Verifique se um número é positivo\nnumero = 10\n",
            "expected_output": "O número é positivo!",
            "hints": ["Use if numero > 0:", "Imprima uma mensagem dentro do if"]
        },
        {
            "id": 22,
            "title": "If-Else",
            "difficulty": "beginner",
            "topic": "if_else",
            "instructions": "Verifique se um número é par ou ímpar e imprima o resultado.",
            "starter_code": "# Verifique se um número é par ou ímpar\nnumero = 7\n",
            "expected_output": "O número é ímpar!",
            "hints": ["Use % para resto da divisão", "Use if numero % 2 == 0:"]
        },
        {
            "id": 23,
            "title": "If-Elif-Else",
            "difficulty": "beginner",
            "topic": "if_elif_else",
            "instructions": "Crie um programa que classifica uma nota (A, B, C, D, F) baseada na pontuação.",
            "starter_code": "# Classifique uma nota baseada na pontuação\nnota = 85\n",
            "expected_output": "Nota: B",
            "hints": ["Use if-elif-else", "A: 90+, B: 80-89, C: 70-79, D: 60-69, F: <60"]
        },
        {
            "id": 24,
            "title": "Operador Ternário",
            "difficulty": "intermediate",
            "topic": "ternary_operator",
            "instructions": "Use o operador ternário para determinar se um número é positivo ou negativo.",
            "starter_code": "# Use operador ternário: valor_se_verdadeiro if condição else valor_se_falso\nnumero = -5\n",
            "expected_output": "Negativo",
            "hints": ["Use: 'Positivo' if numero > 0 else 'Negativo'", "Atribua o resultado a uma variável"]
        },
        {
            "id": 25,
            "title": "Aninhamento de Ifs",
            "difficulty": "intermediate",
            "topic": "nested_if",
            "instructions": "Crie um programa que verifica se um ano é bissexto.",
            "starter_code": "# Verifique se um ano é bissexto\nano = 2024\n",
            "expected_output": "2024 é um ano bissexto!",
            "hints": ["Ano bissexto: divisível por 4, mas não por 100, exceto se divisível por 400", "Use if aninhados"]
        }
    ],
    
    # LOOPS (41-60)
    "loops": [
        {
            "id": 41,
            "title": "For Loop Básico",
            "difficulty": "beginner",
            "topic": "for_loop",
            "instructions": "Use um for loop para imprimir números de 1 a 5.",
            "starter_code": "# Use for loop com range()\n",
            "expected_output": "1\n2\n3\n4\n5",
            "hints": ["Use for i in range(1, 6):", "Use print(i) dentro do loop"]
        },
        {
            "id": 42,
            "title": "While Loop",
            "difficulty": "beginner",
            "topic": "while_loop",
            "instructions": "Use while loop para contar de 1 a 3.",
            "starter_code": "# Use while loop\ncontador = 1\n",
            "expected_output": "1\n2\n3",
            "hints": ["Use while contador <= 3:", "Incremente contador com += 1"]
        },
        {
            "id": 43,
            "title": "Loop com Lista",
            "difficulty": "beginner",
            "topic": "loop_list",
            "instructions": "Itere sobre uma lista de frutas e imprima cada uma.",
            "starter_code": "# Itere sobre uma lista\nfrutas = ['maçã', 'banana', 'laranja']\n",
            "expected_output": "maçã\nbanana\nlaranja",
            "hints": ["Use for fruta in frutas:", "Imprima cada fruta"]
        },
        {
            "id": 44,
            "title": "Break e Continue",
            "difficulty": "intermediate",
            "topic": "break_continue",
            "instructions": "Use break para parar o loop quando encontrar o número 3.",
            "starter_code": "# Use break para parar no número 3\nfor i in range(1, 6):\n",
            "expected_output": "1\n2\n3",
            "hints": ["Use if i == 3: break", "Coloque o break antes do print"]
        },
        {
            "id": 45,
            "title": "Loop Aninhado",
            "difficulty": "intermediate",
            "topic": "nested_loops",
            "instructions": "Crie um padrão de asteriscos usando loops aninhados.",
            "starter_code": "# Crie um padrão de asteriscos\n# 3 linhas, 3 colunas\n",
            "expected_output": "***\n***\n***",
            "hints": ["Use dois for loops aninhados", "Use print('*', end='') para não quebrar linha"]
        }
    ],
    
    # LISTAS (61-80)
    "lists": [
        {
            "id": 61,
            "title": "Criar Lista",
            "difficulty": "beginner",
            "topic": "create_list",
            "instructions": "Crie uma lista com números de 1 a 5 e imprima.",
            "starter_code": "# Crie uma lista com números de 1 a 5\n",
            "expected_output": "[1, 2, 3, 4, 5]",
            "hints": ["Use colchetes [] para criar lista", "Separe elementos com vírgula"]
        },
        {
            "id": 62,
            "title": "Acessar Elementos",
            "difficulty": "beginner",
            "topic": "access_elements",
            "instructions": "Acesse o primeiro, último e elemento do meio de uma lista.",
            "starter_code": "# Acesse elementos da lista\nlista = [10, 20, 30, 40, 50]\n",
            "expected_output": "Primeiro: 10\nÚltimo: 50\nMeio: 30",
            "hints": ["Use [0] para primeiro, [-1] para último", "Use [2] para o meio"]
        },
        {
            "id": 63,
            "title": "Adicionar Elementos",
            "difficulty": "beginner",
            "topic": "add_elements",
            "instructions": "Use append() e insert() para adicionar elementos à lista.",
            "starter_code": "# Use append() e insert()\nlista = [1, 2, 3]\n",
            "expected_output": "[1, 2, 3, 4]\n[0, 1, 2, 3, 4]",
            "hints": ["Use lista.append(4)", "Use lista.insert(0, 0)"]
        },
        {
            "id": 64,
            "title": "Remover Elementos",
            "difficulty": "beginner",
            "topic": "remove_elements",
            "instructions": "Use remove() e pop() para remover elementos da lista.",
            "starter_code": "# Use remove() e pop()\nlista = [1, 2, 3, 4, 5]\n",
            "expected_output": "[1, 2, 4, 5]\n[1, 2, 4]",
            "hints": ["Use lista.remove(3)", "Use lista.pop() para remover último"]
        },
        {
            "id": 65,
            "title": "Ordenar Lista",
            "difficulty": "beginner",
            "topic": "sort_list",
            "instructions": "Ordene uma lista de números em ordem crescente e decrescente.",
            "starter_code": "# Ordene a lista\nlista = [3, 1, 4, 1, 5]\n",
            "expected_output": "Crescente: [1, 1, 3, 4, 5]\nDecrescente: [5, 4, 3, 1, 1]",
            "hints": ["Use lista.sort() para crescente", "Use lista.sort(reverse=True) para decrescente"]
        }
    ],
    
    # DICIONÁRIOS (81-100)
    "dictionaries": [
        {
            "id": 81,
            "title": "Criar Dicionário",
            "difficulty": "beginner",
            "topic": "create_dict",
            "instructions": "Crie um dicionário com informações de uma pessoa.",
            "starter_code": "# Crie um dicionário com nome, idade e cidade\n",
            "expected_output": "{'nome': 'João', 'idade': 25, 'cidade': 'São Paulo'}",
            "hints": ["Use chaves {} para criar dicionário", "Use 'chave': 'valor'"]
        },
        {
            "id": 82,
            "title": "Acessar Valores",
            "difficulty": "beginner",
            "topic": "access_dict",
            "instructions": "Acesse valores do dicionário usando chaves.",
            "starter_code": "# Acesse valores do dicionário\npessoa = {'nome': 'Maria', 'idade': 30}\n",
            "expected_output": "Nome: Maria\nIdade: 30",
            "hints": ["Use dicionario['chave']", "Use print() para exibir"]
        },
        {
            "id": 83,
            "title": "Adicionar/Modificar",
            "difficulty": "beginner",
            "topic": "modify_dict",
            "instructions": "Adicione e modifique valores no dicionário.",
            "starter_code": "# Adicione e modifique valores\npessoa = {'nome': 'Ana'}\n",
            "expected_output": "{'nome': 'Ana', 'idade': 28}\n{'nome': 'Ana Silva', 'idade': 28}",
            "hints": ["Use dicionario['nova_chave'] = valor", "Modifique com dicionario['chave'] = novo_valor"]
        },
        {
            "id": 84,
            "title": "Iterar Dicionário",
            "difficulty": "intermediate",
            "topic": "iterate_dict",
            "instructions": "Itere sobre chaves, valores e itens do dicionário.",
            "starter_code": "# Itere sobre o dicionário\npessoa = {'nome': 'Carlos', 'idade': 35, 'cidade': 'Rio'}\n",
            "expected_output": "Chaves: nome, idade, cidade\nValores: Carlos, 35, Rio\nItens: nome: Carlos, idade: 35, cidade: Rio",
            "hints": ["Use .keys(), .values(), .items()", "Use for loop para iterar"]
        },
        {
            "id": 85,
            "title": "Dicionário Aninhado",
            "difficulty": "intermediate",
            "topic": "nested_dict",
            "instructions": "Crie um dicionário aninhado e acesse valores internos.",
            "starter_code": "# Crie dicionário aninhado\nempresa = {\n    'funcionario1': {'nome': 'João', 'salario': 5000},\n    'funcionario2': {'nome': 'Maria', 'salario': 6000}\n}\n",
            "expected_output": "João: R$ 5000\nMaria: R$ 6000",
            "hints": ["Use dicionario['chave']['chave_interna']", "Itere sobre os funcionários"]
        }
    ],
    
    # FUNÇÕES (101-120)
    "functions": [
        {
            "id": 101,
            "title": "Função Simples",
            "difficulty": "beginner",
            "topic": "simple_function",
            "instructions": "Crie uma função que imprime 'Olá, Mundo!' e a chame.",
            "starter_code": "# Crie uma função que imprime 'Olá, Mundo!'\n",
            "expected_output": "Olá, Mundo!",
            "hints": ["Use def nome_funcao():", "Use print() dentro da função", "Chame a função"]
        },
        {
            "id": 102,
            "title": "Função com Parâmetros",
            "difficulty": "beginner",
            "topic": "function_params",
            "instructions": "Crie uma função que recebe um nome e imprime uma saudação personalizada.",
            "starter_code": "# Crie função com parâmetro 'nome'\n",
            "expected_output": "Olá, João!",
            "hints": ["Use def saudacao(nome):", "Use f-string para formatação", "Chame com saudacao('João')"]
        },
        {
            "id": 103,
            "title": "Função com Retorno",
            "difficulty": "beginner",
            "topic": "function_return",
            "instructions": "Crie uma função que soma dois números e retorna o resultado.",
            "starter_code": "# Crie função que retorna a soma\n",
            "expected_output": "A soma é: 15",
            "hints": ["Use return para retornar valor", "Atribua o resultado a uma variável"]
        },
        {
            "id": 104,
            "title": "Função com Múltiplos Parâmetros",
            "difficulty": "intermediate",
            "topic": "multiple_params",
            "instructions": "Crie uma função que calcula a área de um retângulo.",
            "starter_code": "# Crie função que calcula área do retângulo\n",
            "expected_output": "A área do retângulo é: 20",
            "hints": ["Use def area_retangulo(largura, altura):", "Retorne largura * altura"]
        },
        {
            "id": 105,
            "title": "Função com Valor Padrão",
            "difficulty": "intermediate",
            "topic": "default_params",
            "instructions": "Crie uma função com parâmetro com valor padrão.",
            "starter_code": "# Crie função com parâmetro padrão\n",
            "expected_output": "Olá, Mundo!\nOlá, João!",
            "hints": ["Use def saudacao(nome='Mundo'):", "Chame com e sem parâmetro"]
        }
    ],
    
    # ESTRUTURAS DE DADOS AVANÇADAS (121-140)
    "advanced_data_structures": [
        {
            "id": 121,
            "title": "Tuplas",
            "difficulty": "intermediate",
            "topic": "tuples",
            "instructions": "Crie uma tupla com coordenadas (x, y) e acesse os elementos.",
            "starter_code": "# Crie uma tupla com coordenadas\n",
            "expected_output": "Coordenadas: (10, 20)\nX: 10\nY: 20",
            "hints": ["Use parênteses () para tupla", "Acesse com [0] e [1]"]
        },
        {
            "id": 122,
            "title": "Sets",
            "difficulty": "intermediate",
            "topic": "sets",
            "instructions": "Crie dois sets e faça operações de união e interseção.",
            "starter_code": "# Crie dois sets e faça operações\n",
            "expected_output": "União: {1, 2, 3, 4, 5, 6}\nInterseção: {3, 4}",
            "hints": ["Use set() para criar sets", "Use | para união, & para interseção"]
        },
        {
            "id": 123,
            "title": "List Comprehension",
            "difficulty": "intermediate",
            "topic": "list_comprehension",
            "instructions": "Use list comprehension para criar uma lista de quadrados.",
            "starter_code": "# Use list comprehension para quadrados de 1 a 5\n",
            "expected_output": "[1, 4, 9, 16, 25]",
            "hints": ["Use [x**2 for x in range(1, 6)]", "x**2 é x ao quadrado"]
        },
        {
            "id": 124,
            "title": "Dictionary Comprehension",
            "difficulty": "intermediate",
            "topic": "dict_comprehension",
            "instructions": "Use dictionary comprehension para criar um dicionário de quadrados.",
            "starter_code": "# Use dict comprehension para quadrados\n",
            "expected_output": "{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}",
            "hints": ["Use {x: x**2 for x in range(1, 6)}", "x: x**2 é chave: valor"]
        },
        {
            "id": 125,
            "title": "Lista de Listas",
            "difficulty": "intermediate",
            "topic": "list_of_lists",
            "instructions": "Crie uma matriz 3x3 e acesse elementos específicos.",
            "starter_code": "# Crie uma matriz 3x3\n",
            "expected_output": "Matriz:\n[1, 2, 3]\n[4, 5, 6]\n[7, 8, 9]\nElemento (1,1): 5",
            "hints": ["Use lista de listas", "Acesse com matriz[linha][coluna]"]
        }
    ],
    
    # ALGORITMOS BÁSICOS (141-160)
    "algorithms": [
        {
            "id": 141,
            "title": "Busca Linear",
            "difficulty": "intermediate",
            "topic": "linear_search",
            "instructions": "Implemente busca linear em uma lista.",
            "starter_code": "# Implemente busca linear\nlista = [1, 3, 5, 7, 9]\nalvo = 5\n",
            "expected_output": "Elemento 5 encontrado na posição 2",
            "hints": ["Use for loop com enumerate()", "Compare cada elemento com o alvo"]
        },
        {
            "id": 142,
            "title": "Ordenação Bubble Sort",
            "difficulty": "intermediate",
            "topic": "bubble_sort",
            "instructions": "Implemente o algoritmo Bubble Sort.",
            "starter_code": "# Implemente Bubble Sort\nlista = [64, 34, 25, 12, 22, 11, 90]\n",
            "expected_output": "Lista ordenada: [11, 12, 22, 25, 34, 64, 90]",
            "hints": ["Use loops aninhados", "Compare elementos adjacentes", "Troque se necessário"]
        },
        {
            "id": 143,
            "title": "Fatorial",
            "difficulty": "intermediate",
            "topic": "factorial",
            "instructions": "Calcule o fatorial de um número usando loop.",
            "starter_code": "# Calcule fatorial de 5\n",
            "expected_output": "Fatorial de 5 é: 120",
            "hints": ["Use for loop de 1 até n", "Multiplique acumulador por cada número"]
        },
        {
            "id": 144,
            "title": "Sequência de Fibonacci",
            "difficulty": "intermediate",
            "topic": "fibonacci",
            "instructions": "Gere os primeiros 10 números da sequência de Fibonacci.",
            "starter_code": "# Gere sequência de Fibonacci\n",
            "expected_output": "0, 1, 1, 2, 3, 5, 8, 13, 21, 34",
            "hints": ["Comece com 0 e 1", "Cada número é soma dos dois anteriores"]
        },
        {
            "id": 145,
            "title": "Verificar Palíndromo",
            "difficulty": "intermediate",
            "topic": "palindrome",
            "instructions": "Verifique se uma palavra é palíndromo.",
            "starter_code": "# Verifique se 'arara' é palíndromo\n",
            "expected_output": "arara é um palíndromo!",
            "hints": ["Compare string com string[::-1]", "Use .lower() para ignorar maiúsculas"]
        }
    ]
}

def get_exercises_by_topic(topic=None):
    """Retorna exercícios filtrados por tópico"""
    if topic and topic in EXERCISES_DATABASE:
        return EXERCISES_DATABASE[topic]
    return EXERCISES_DATABASE

def get_exercise_by_id(exercise_id):
    """Retorna um exercício específico por ID"""
    for topic_exercises in EXERCISES_DATABASE.values():
        for exercise in topic_exercises:
            if exercise['id'] == exercise_id:
                return exercise
    return None

def get_all_exercises():
    """Retorna todos os exercícios"""
    all_exercises = []
    for topic_exercises in EXERCISES_DATABASE.values():
        all_exercises.extend(topic_exercises)
    return all_exercises

def get_exercises_by_difficulty(difficulty):
    """Retorna exercícios filtrados por dificuldade"""
    all_exercises = get_all_exercises()
    return [ex for ex in all_exercises if ex['difficulty'] == difficulty]
