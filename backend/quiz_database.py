# -*- coding: utf-8 -*-
"""
Database of Python quiz questions covering basic concepts
"""

QUIZ_QUESTIONS = [
    # CONCEITOS BÁSICOS (1-30)
    {
        "id": 1,
        "question": "Qual é a função usada para imprimir texto na tela em Python?",
        "options": ["echo()", "print()", "display()", "show()"],
        "answer": 1,
        "topic": "output",
        "difficulty": "beginner"
    },
    {
        "id": 2,
        "question": "Como se inicia um comentário em Python?",
        "options": ["//", "#", "<!--", "--"],
        "answer": 1,
        "topic": "comments",
        "difficulty": "beginner"
    },
    {
        "id": 3,
        "question": "Qual é o operador usado para atribuir um valor a uma variável?",
        "options": ["==", "=", ":=", "->"],
        "answer": 1,
        "topic": "variables",
        "difficulty": "beginner"
    },
    {
        "id": 4,
        "question": "Qual é o tipo de dados de x = 42?",
        "options": ["string", "float", "int", "boolean"],
        "answer": 2,
        "topic": "data_types",
        "difficulty": "beginner"
    },
    {
        "id": 5,
        "question": "Qual é o tipo de dados de x = 'Hello'?",
        "options": ["int", "float", "string", "boolean"],
        "answer": 2,
        "topic": "data_types",
        "difficulty": "beginner"
    },
    {
        "id": 6,
        "question": "Qual é o tipo de dados de x = 3.14?",
        "options": ["int", "float", "string", "boolean"],
        "answer": 1,
        "topic": "data_types",
        "difficulty": "beginner"
    },
    {
        "id": 7,
        "question": "Qual é o tipo de dados de x = True?",
        "options": ["int", "float", "string", "boolean"],
        "answer": 3,
        "topic": "data_types",
        "difficulty": "beginner"
    },
    {
        "id": 8,
        "question": "Qual operador é usado para adição em Python?",
        "options": ["+", "-", "*", "/"],
        "answer": 0,
        "topic": "operators",
        "difficulty": "beginner"
    },
    {
        "id": 9,
        "question": "Qual operador é usado para multiplicação em Python?",
        "options": ["+", "-", "*", "/"],
        "answer": 2,
        "topic": "operators",
        "difficulty": "beginner"
    },
    {
        "id": 10,
        "question": "Qual operador é usado para divisão em Python?",
        "options": ["+", "-", "*", "/"],
        "answer": 3,
        "topic": "operators",
        "difficulty": "beginner"
    },
    {
        "id": 11,
        "question": "Qual operador é usado para obter o resto da divisão?",
        "options": ["%", "//", "**", "&"],
        "answer": 0,
        "topic": "operators",
        "difficulty": "beginner"
    },
    {
        "id": 12,
        "question": "Qual operador é usado para exponenciação em Python?",
        "options": ["^", "**", "pow()", "exp()"],
        "answer": 1,
        "topic": "operators",
        "difficulty": "beginner"
    },
    {
        "id": 13,
        "question": "Qual função é usada para obter entrada do usuário?",
        "options": ["input()", "read()", "get()", "scan()"],
        "answer": 0,
        "topic": "input",
        "difficulty": "beginner"
    },
    {
        "id": 14,
        "question": "Qual função é usada para converter string para int?",
        "options": ["str()", "int()", "float()", "bool()"],
        "answer": 1,
        "topic": "type_conversion",
        "difficulty": "beginner"
    },
    {
        "id": 15,
        "question": "Qual função é usada para converter int para string?",
        "options": ["str()", "int()", "float()", "bool()"],
        "answer": 0,
        "topic": "type_conversion",
        "difficulty": "beginner"
    },
    {
        "id": 16,
        "question": "Qual função é usada para verificar o tipo de uma variável?",
        "options": ["type()", "typeof()", "gettype()", "checktype()"],
        "answer": 0,
        "topic": "type_conversion",
        "difficulty": "beginner"
    },
    {
        "id": 17,
        "question": "Qual é o resultado de 5 == 5?",
        "options": ["True", "False", "Error", "None"],
        "answer": 0,
        "topic": "comparison",
        "difficulty": "beginner"
    },
    {
        "id": 18,
        "question": "Qual é o resultado de 5 != 3?",
        "options": ["True", "False", "Error", "None"],
        "answer": 0,
        "topic": "comparison",
        "difficulty": "beginner"
    },
    {
        "id": 19,
        "question": "Qual é o resultado de 5 > 3?",
        "options": ["True", "False", "Error", "None"],
        "answer": 0,
        "topic": "comparison",
        "difficulty": "beginner"
    },
    {
        "id": 20,
        "question": "Qual é o resultado de 5 < 3?",
        "options": ["True", "False", "Error", "None"],
        "answer": 1,
        "topic": "comparison",
        "difficulty": "beginner"
    },
    {
        "id": 21,
        "question": "Qual operador lógico significa 'e' em Python?",
        "options": ["and", "or", "not", "&"],
        "answer": 0,
        "topic": "logical_operators",
        "difficulty": "beginner"
    },
    {
        "id": 22,
        "question": "Qual operador lógico significa 'ou' em Python?",
        "options": ["and", "or", "not", "|"],
        "answer": 1,
        "topic": "logical_operators",
        "difficulty": "beginner"
    },
    {
        "id": 23,
        "question": "Qual operador lógico significa 'não' em Python?",
        "options": ["and", "or", "not", "!"],
        "answer": 2,
        "topic": "logical_operators",
        "difficulty": "beginner"
    },
    {
        "id": 24,
        "question": "Qual é o resultado de True and False?",
        "options": ["True", "False", "Error", "None"],
        "answer": 1,
        "topic": "logical_operators",
        "difficulty": "beginner"
    },
    {
        "id": 25,
        "question": "Qual é o resultado de True or False?",
        "options": ["True", "False", "Error", "None"],
        "answer": 0,
        "topic": "logical_operators",
        "difficulty": "beginner"
    },
    {
        "id": 26,
        "question": "Qual é o resultado de not True?",
        "options": ["True", "False", "Error", "None"],
        "answer": 1,
        "topic": "logical_operators",
        "difficulty": "beginner"
    },
    {
        "id": 27,
        "question": "Qual palavra-chave é usada para criar uma condição if?",
        "options": ["if", "when", "while", "for"],
        "answer": 0,
        "topic": "conditionals",
        "difficulty": "beginner"
    },
    {
        "id": 28,
        "question": "Qual palavra-chave é usada para criar uma condição else?",
        "options": ["if", "else", "elif", "when"],
        "answer": 1,
        "topic": "conditionals",
        "difficulty": "beginner"
    },
    {
        "id": 29,
        "question": "Qual palavra-chave é usada para criar uma condição elif?",
        "options": ["if", "else", "elif", "when"],
        "answer": 2,
        "topic": "conditionals",
        "difficulty": "beginner"
    },
    {
        "id": 30,
        "question": "Qual é a indentação padrão em Python?",
        "options": ["2 espaços", "4 espaços", "8 espaços", "1 tab"],
        "answer": 1,
        "topic": "syntax",
        "difficulty": "beginner"
    },
    
    # LOOPS (31-50)
    {
        "id": 31,
        "question": "Qual palavra-chave é usada para criar um loop for?",
        "options": ["for", "while", "loop", "repeat"],
        "answer": 0,
        "topic": "loops",
        "difficulty": "beginner"
    },
    {
        "id": 32,
        "question": "Qual palavra-chave é usada para criar um loop while?",
        "options": ["for", "while", "loop", "repeat"],
        "answer": 1,
        "topic": "loops",
        "difficulty": "beginner"
    },
    {
        "id": 33,
        "question": "Qual função é usada para gerar uma sequência de números?",
        "options": ["range()", "seq()", "numbers()", "count()"],
        "answer": 0,
        "topic": "loops",
        "difficulty": "beginner"
    },
    {
        "id": 34,
        "question": "Qual palavra-chave é usada para sair de um loop?",
        "options": ["exit", "break", "stop", "quit"],
        "answer": 1,
        "topic": "loops",
        "difficulty": "beginner"
    },
    {
        "id": 35,
        "question": "Qual palavra-chave é usada para pular para a próxima iteração?",
        "options": ["skip", "continue", "next", "jump"],
        "answer": 1,
        "topic": "loops",
        "difficulty": "beginner"
    },
    {
        "id": 36,
        "question": "Qual é o resultado de range(3)?",
        "options": ["[0, 1, 2]", "[1, 2, 3]", "[0, 1, 2, 3]", "Error"],
        "answer": 0,
        "topic": "loops",
        "difficulty": "beginner"
    },
    {
        "id": 37,
        "question": "Qual é o resultado de range(1, 4)?",
        "options": ["[0, 1, 2, 3]", "[1, 2, 3]", "[1, 2, 3, 4]", "Error"],
        "answer": 1,
        "topic": "loops",
        "difficulty": "beginner"
    },
    {
        "id": 38,
        "question": "Qual é o resultado de range(0, 10, 2)?",
        "options": ["[0, 2, 4, 6, 8]", "[0, 1, 2, 3, 4]", "[2, 4, 6, 8, 10]", "Error"],
        "answer": 0,
        "topic": "loops",
        "difficulty": "beginner"
    },
    {
        "id": 39,
        "question": "Como iterar sobre uma lista em Python?",
        "options": ["for item in list:", "for list in item:", "for i in range(list):", "while list:"],
        "answer": 0,
        "topic": "loops",
        "difficulty": "beginner"
    },
    {
        "id": 40,
        "question": "Qual é a sintaxe correta para um loop while?",
        "options": ["while condition:", "while (condition):", "while condition {", "while condition do"],
        "answer": 0,
        "topic": "loops",
        "difficulty": "beginner"
    },
    
    # LISTAS (51-70)
    {
        "id": 51,
        "question": "Como criar uma lista vazia em Python?",
        "options": ["[]", "list()", "new list", "Ambos [] e list()"],
        "answer": 3,
        "topic": "lists",
        "difficulty": "beginner"
    },
    {
        "id": 52,
        "question": "Como acessar o primeiro elemento de uma lista?",
        "options": ["list[0]", "list[1]", "list.first", "list.first()"],
        "answer": 0,
        "topic": "lists",
        "difficulty": "beginner"
    },
    {
        "id": 53,
        "question": "Como acessar o último elemento de uma lista?",
        "options": ["list[-1]", "list[last]", "list.last", "list.last()"],
        "answer": 0,
        "topic": "lists",
        "difficulty": "beginner"
    },
    {
        "id": 54,
        "question": "Qual método é usado para adicionar um elemento ao final da lista?",
        "options": ["add()", "append()", "insert()", "push()"],
        "answer": 1,
        "topic": "lists",
        "difficulty": "beginner"
    },
    {
        "id": 55,
        "question": "Qual método é usado para inserir um elemento em uma posição específica?",
        "options": ["add()", "append()", "insert()", "push()"],
        "answer": 2,
        "topic": "lists",
        "difficulty": "beginner"
    },
    {
        "id": 56,
        "question": "Qual método é usado para remover um elemento da lista?",
        "options": ["remove()", "delete()", "pop()", "Ambos remove() e pop()"],
        "answer": 3,
        "topic": "lists",
        "difficulty": "beginner"
    },
    {
        "id": 57,
        "question": "Qual método é usado para ordenar uma lista?",
        "options": ["sort()", "order()", "arrange()", "sort_list()"],
        "answer": 0,
        "topic": "lists",
        "difficulty": "beginner"
    },
    {
        "id": 58,
        "question": "Qual método é usado para reverter uma lista?",
        "options": ["reverse()", "flip()", "invert()", "backwards()"],
        "answer": 0,
        "topic": "lists",
        "difficulty": "beginner"
    },
    {
        "id": 59,
        "question": "Qual método é usado para contar elementos em uma lista?",
        "options": ["count()", "length()", "size()", "len()"],
        "answer": 3,
        "topic": "lists",
        "difficulty": "beginner"
    },
    {
        "id": 60,
        "question": "Como verificar se um elemento está em uma lista?",
        "options": ["in", "contains", "has", "exists"],
        "answer": 0,
        "topic": "lists",
        "difficulty": "beginner"
    },
    
    # DICIONÁRIOS (71-90)
    {
        "id": 71,
        "question": "Como criar um dicionário vazio em Python?",
        "options": ["{}", "dict()", "new dict", "Ambos {} e dict()"],
        "answer": 3,
        "topic": "dictionaries",
        "difficulty": "beginner"
    },
    {
        "id": 72,
        "question": "Como acessar um valor em um dicionário?",
        "options": ["dict[key]", "dict.get(key)", "dict.value(key)", "Ambos dict[key] e dict.get(key)"],
        "answer": 3,
        "topic": "dictionaries",
        "difficulty": "beginner"
    },
    {
        "id": 73,
        "question": "Como adicionar um par chave-valor a um dicionário?",
        "options": ["dict[key] = value", "dict.add(key, value)", "dict.insert(key, value)", "dict.set(key, value)"],
        "answer": 0,
        "topic": "dictionaries",
        "difficulty": "beginner"
    },
    {
        "id": 74,
        "question": "Como remover um par chave-valor de um dicionário?",
        "options": ["del dict[key]", "dict.pop(key)", "dict.remove(key)", "Ambos del dict[key] e dict.pop(key)"],
        "answer": 3,
        "topic": "dictionaries",
        "difficulty": "beginner"
    },
    {
        "id": 75,
        "question": "Qual método retorna todas as chaves de um dicionário?",
        "options": ["keys()", "get_keys()", "all_keys()", "key_list()"],
        "answer": 0,
        "topic": "dictionaries",
        "difficulty": "beginner"
    },
    {
        "id": 76,
        "question": "Qual método retorna todos os valores de um dicionário?",
        "options": ["values()", "get_values()", "all_values()", "value_list()"],
        "answer": 0,
        "topic": "dictionaries",
        "difficulty": "beginner"
    },
    {
        "id": 77,
        "question": "Qual método retorna todos os pares chave-valor de um dicionário?",
        "options": ["items()", "pairs()", "entries()", "all_items()"],
        "answer": 0,
        "topic": "dictionaries",
        "difficulty": "beginner"
    },
    {
        "id": 78,
        "question": "Como verificar se uma chave existe em um dicionário?",
        "options": ["key in dict", "dict.has_key(key)", "dict.contains(key)", "dict.exists(key)"],
        "answer": 0,
        "topic": "dictionaries",
        "difficulty": "beginner"
    },
    {
        "id": 79,
        "question": "Qual método retorna o número de pares chave-valor em um dicionário?",
        "options": ["count()", "length()", "size()", "len()"],
        "answer": 3,
        "topic": "dictionaries",
        "difficulty": "beginner"
    },
    {
        "id": 80,
        "question": "Como limpar todos os elementos de um dicionário?",
        "options": ["clear()", "empty()", "reset()", "delete_all()"],
        "answer": 0,
        "topic": "dictionaries",
        "difficulty": "beginner"
    },
    
    # FUNÇÕES (91-110)
    {
        "id": 91,
        "question": "Qual palavra-chave é usada para definir uma função?",
        "options": ["def", "function", "func", "define"],
        "answer": 0,
        "topic": "functions",
        "difficulty": "beginner"
    },
    {
        "id": 92,
        "question": "Qual palavra-chave é usada para retornar um valor de uma função?",
        "options": ["return", "give", "output", "result"],
        "answer": 0,
        "topic": "functions",
        "difficulty": "beginner"
    },
    {
        "id": 93,
        "question": "Como chamar uma função em Python?",
        "options": ["function()", "call function()", "execute function()", "run function()"],
        "answer": 0,
        "topic": "functions",
        "difficulty": "beginner"
    },
    {
        "id": 94,
        "question": "Como passar argumentos para uma função?",
        "options": ["function(arg1, arg2)", "function with arg1, arg2", "function(arg1 and arg2)", "function[arg1, arg2]"],
        "answer": 0,
        "topic": "functions",
        "difficulty": "beginner"
    },
    {
        "id": 95,
        "question": "Qual é a sintaxe correta para definir uma função?",
        "options": ["def function_name():", "function function_name():", "def function_name():", "define function_name():"],
        "answer": 2,
        "topic": "functions",
        "difficulty": "beginner"
    },
    {
        "id": 96,
        "question": "Como definir uma função com parâmetros?",
        "options": ["def function(param):", "def function with param:", "function(param):", "def function[param]:"],
        "answer": 0,
        "topic": "functions",
        "difficulty": "beginner"
    },
    {
        "id": 97,
        "question": "Como definir uma função com múltiplos parâmetros?",
        "options": ["def function(param1, param2):", "def function(param1 and param2):", "def function(param1, param2):", "def function[param1, param2]:"],
        "answer": 2,
        "topic": "functions",
        "difficulty": "beginner"
    },
    {
        "id": 98,
        "question": "Como definir um valor padrão para um parâmetro?",
        "options": ["def function(param=default):", "def function(param default):", "def function(param: default):", "def function(param = default):"],
        "answer": 0,
        "topic": "functions",
        "difficulty": "beginner"
    },
    {
        "id": 99,
        "question": "Qual é o valor padrão retornado por uma função sem return?",
        "options": ["None", "0", "False", "Error"],
        "answer": 0,
        "topic": "functions",
        "difficulty": "beginner"
    },
    {
        "id": 100,
        "question": "Como documentar uma função em Python?",
        "options": ["docstring", "comment", "note", "description"],
        "answer": 0,
        "topic": "functions",
        "difficulty": "beginner"
    },
    
    # STRINGS (101-120)
    {
        "id": 101,
        "question": "Qual método é usado para converter uma string para maiúsculas?",
        "options": ["upper()", "uppercase()", "toUpper()", "capitalize()"],
        "answer": 0,
        "topic": "strings",
        "difficulty": "beginner"
    },
    {
        "id": 102,
        "question": "Qual método é usado para converter uma string para minúsculas?",
        "options": ["lower()", "lowercase()", "toLower()", "small()"],
        "answer": 0,
        "topic": "strings",
        "difficulty": "beginner"
    },
    {
        "id": 103,
        "question": "Qual método é usado para remover espaços em branco do início e fim?",
        "options": ["strip()", "trim()", "clean()", "remove_spaces()"],
        "answer": 0,
        "topic": "strings",
        "difficulty": "beginner"
    },
    {
        "id": 104,
        "question": "Qual método é usado para dividir uma string?",
        "options": ["split()", "divide()", "break()", "cut()"],
        "answer": 0,
        "topic": "strings",
        "difficulty": "beginner"
    },
    {
        "id": 105,
        "question": "Qual método é usado para juntar strings?",
        "options": ["join()", "concat()", "merge()", "combine()"],
        "answer": 0,
        "topic": "strings",
        "difficulty": "beginner"
    },
    {
        "id": 106,
        "question": "Qual método é usado para encontrar uma substring?",
        "options": ["find()", "search()", "locate()", "index()"],
        "answer": 0,
        "topic": "strings",
        "difficulty": "beginner"
    },
    {
        "id": 107,
        "question": "Qual método é usado para substituir texto em uma string?",
        "options": ["replace()", "substitute()", "change()", "swap()"],
        "answer": 0,
        "topic": "strings",
        "difficulty": "beginner"
    },
    {
        "id": 108,
        "question": "Qual método é usado para verificar se uma string começa com um texto?",
        "options": ["startswith()", "begins_with()", "starts()", "starts_with()"],
        "answer": 0,
        "topic": "strings",
        "difficulty": "beginner"
    },
    {
        "id": 109,
        "question": "Qual método é usado para verificar se uma string termina com um texto?",
        "options": ["endswith()", "ends_with()", "finishes()", "concludes()"],
        "answer": 0,
        "topic": "strings",
        "difficulty": "beginner"
    },
    {
        "id": 110,
        "question": "Qual método é usado para contar caracteres em uma string?",
        "options": ["count()", "length()", "size()", "len()"],
        "answer": 3,
        "topic": "strings",
        "difficulty": "beginner"
    },
    {
        "id": 111,
        "question": "Como concatenar duas strings?",
        "options": ["string1 + string2", "string1 & string2", "string1.concat(string2)", "string1.join(string2)"],
        "answer": 0,
        "topic": "strings",
        "difficulty": "beginner"
    },
    {
        "id": 112,
        "question": "Como repetir uma string várias vezes?",
        "options": ["string * number", "string.repeat(number)", "string * number", "repeat(string, number)"],
        "answer": 2,
        "topic": "strings",
        "difficulty": "beginner"
    },
    {
        "id": 113,
        "question": "Como acessar um caractere específico de uma string?",
        "options": ["string[index]", "string.get(index)", "string.charAt(index)", "string[index]"],
        "answer": 3,
        "topic": "strings",
        "difficulty": "beginner"
    },
    {
        "id": 114,
        "question": "Como obter uma fatia (slice) de uma string?",
        "options": ["string[start:end]", "string.slice(start, end)", "string.substring(start, end)", "string[start:end]"],
        "answer": 3,
        "topic": "strings",
        "difficulty": "beginner"
    },
    {
        "id": 115,
        "question": "Qual é o resultado de 'Hello' + 'World'?",
        "options": ["'HelloWorld'", "'Hello World'", "'Hello+World'", "Error"],
        "answer": 0,
        "topic": "strings",
        "difficulty": "beginner"
    },
    {
        "id": 116,
        "question": "Qual é o resultado de 'Hello' * 3?",
        "options": ["'HelloHelloHello'", "'Hello3'", "'Hello Hello Hello'", "Error"],
        "answer": 0,
        "topic": "strings",
        "difficulty": "beginner"
    },
    {
        "id": 117,
        "question": "Qual é o resultado de len('Python')?",
        "options": ["5", "6", "7", "Error"],
        "answer": 1,
        "topic": "strings",
        "difficulty": "beginner"
    },
    {
        "id": 118,
        "question": "Qual é o resultado de 'Python'[0]?",
        "options": ["'P'", "'p'", "'y'", "Error"],
        "answer": 0,
        "topic": "strings",
        "difficulty": "beginner"
    },
    {
        "id": 119,
        "question": "Qual é o resultado de 'Python'[-1]?",
        "options": ["'P'", "'n'", "'o'", "Error"],
        "answer": 1,
        "topic": "strings",
        "difficulty": "beginner"
    },
    {
        "id": 120,
        "question": "Qual é o resultado de 'Python'[1:4]?",
        "options": ["'yth'", "'ytho'", "'Pyth'", "'yth'"],
        "answer": 3,
        "topic": "strings",
        "difficulty": "beginner"
    },
    
    # MÓDULOS E BIBLIOTECAS (121-140)
    {
        "id": 121,
        "question": "Qual palavra-chave é usada para importar um módulo?",
        "options": ["import", "include", "require", "use"],
        "answer": 0,
        "topic": "modules",
        "difficulty": "beginner"
    },
    {
        "id": 122,
        "question": "Como importar apenas uma função específica de um módulo?",
        "options": ["from module import function", "import function from module", "module.import(function)", "import module.function"],
        "answer": 0,
        "topic": "modules",
        "difficulty": "beginner"
    },
    {
        "id": 123,
        "question": "Como importar um módulo com um alias?",
        "options": ["import module as alias", "import module alias", "alias = import module", "import alias from module"],
        "answer": 0,
        "topic": "modules",
        "difficulty": "beginner"
    },
    {
        "id": 124,
        "question": "Qual módulo é usado para operações matemáticas?",
        "options": ["math", "calc", "number", "numeric"],
        "answer": 0,
        "topic": "modules",
        "difficulty": "beginner"
    },
    {
        "id": 125,
        "question": "Qual módulo é usado para gerar números aleatórios?",
        "options": ["random", "rand", "randomize", "chance"],
        "answer": 0,
        "topic": "modules",
        "difficulty": "beginner"
    },
    {
        "id": 126,
        "question": "Qual módulo é usado para trabalhar com datas?",
        "options": ["datetime", "date", "time", "calendar"],
        "answer": 0,
        "topic": "modules",
        "difficulty": "beginner"
    },
    {
        "id": 127,
        "question": "Qual módulo é usado para trabalhar com arquivos?",
        "options": ["os", "file", "filesystem", "path"],
        "answer": 0,
        "topic": "modules",
        "difficulty": "beginner"
    },
    {
        "id": 128,
        "question": "Como usar a função sqrt do módulo math?",
        "options": ["math.sqrt()", "sqrt()", "math.sqrt()", "import sqrt from math"],
        "answer": 2,
        "topic": "modules",
        "difficulty": "beginner"
    },
    {
        "id": 129,
        "question": "Como gerar um número aleatório entre 1 e 10?",
        "options": ["random.randint(1, 10)", "random(1, 10)", "randint(1, 10)", "random.randint(1, 10)"],
        "answer": 3,
        "topic": "modules",
        "difficulty": "beginner"
    },
    {
        "id": 130,
        "question": "Qual é o valor de math.pi?",
        "options": ["3.14", "3.14159", "3.141592653589793", "3.141592653589793238"],
        "answer": 2,
        "topic": "modules",
        "difficulty": "beginner"
    },
    
    # ERROS E EXCEÇÕES (141-150)
    {
        "id": 141,
        "question": "Qual palavra-chave é usada para tratar exceções?",
        "options": ["try", "catch", "except", "Ambos try e except"],
        "answer": 3,
        "topic": "exceptions",
        "difficulty": "beginner"
    },
    {
        "id": 142,
        "question": "Qual palavra-chave é usada para capturar exceções?",
        "options": ["try", "catch", "except", "handle"],
        "answer": 2,
        "topic": "exceptions",
        "difficulty": "beginner"
    },
    {
        "id": 143,
        "question": "Qual palavra-chave é usada para executar código que sempre deve rodar?",
        "options": ["finally", "always", "ensure", "guarantee"],
        "answer": 0,
        "topic": "exceptions",
        "difficulty": "beginner"
    },
    {
        "id": 144,
        "question": "Qual palavra-chave é usada para levantar uma exceção?",
        "options": ["raise", "throw", "error", "exception"],
        "answer": 0,
        "topic": "exceptions",
        "difficulty": "beginner"
    },
    {
        "id": 145,
        "question": "Qual é a sintaxe correta para try-except?",
        "options": ["try: ... except: ...", "try { ... } catch { ... }", "try: ... catch: ...", "try: ... except: ..."],
        "answer": 3,
        "topic": "exceptions",
        "difficulty": "beginner"
    },
    {
        "id": 146,
        "question": "Como capturar uma exceção específica?",
        "options": ["except ValueError:", "except ValueError:", "catch ValueError:", "except ValueError:"],
        "answer": 1,
        "topic": "exceptions",
        "difficulty": "beginner"
    },
    {
        "id": 147,
        "question": "Como capturar qualquer exceção?",
        "options": ["except:", "except Exception:", "catch:", "Ambos except: e except Exception:"],
        "answer": 3,
        "topic": "exceptions",
        "difficulty": "beginner"
    },
    {
        "id": 148,
        "question": "Qual exceção é levantada quando uma variável não está definida?",
        "options": ["NameError", "VariableError", "UndefinedError", "NotFoundError"],
        "answer": 0,
        "topic": "exceptions",
        "difficulty": "beginner"
    },
    {
        "id": 149,
        "question": "Qual exceção é levantada quando há erro de tipo?",
        "options": ["TypeError", "TypeError", "TypeError", "TypeError"],
        "answer": 0,
        "topic": "exceptions",
        "difficulty": "beginner"
    },
    {
        "id": 150,
        "question": "Qual exceção é levantada quando há erro de valor?",
        "options": ["ValueError", "ValueError", "ValueError", "ValueError"],
        "answer": 0,
        "topic": "exceptions",
        "difficulty": "beginner"
    }
]

def get_quiz_questions(limit=50, topic=None, difficulty=None):
    """Retorna perguntas do quiz com filtros opcionais"""
    questions = QUIZ_QUESTIONS.copy()
    
    if topic:
        questions = [q for q in questions if q.get('topic') == topic]
    
    if difficulty:
        questions = [q for q in questions if q.get('difficulty') == difficulty]
    
    return questions[:limit]

def get_question_by_id(question_id):
    """Retorna uma pergunta específica por ID"""
    for question in QUIZ_QUESTIONS:
        if question['id'] == question_id:
            return question
    return None

def get_quiz_topics():
    """Retorna todos os tópicos disponíveis"""
    topics = set()
    for question in QUIZ_QUESTIONS:
        topics.add(question.get('topic', 'unknown'))
    return list(topics)

def get_quiz_difficulties():
    """Retorna todos os níveis de dificuldade"""
    difficulties = set()
    for question in QUIZ_QUESTIONS:
        difficulties.add(question.get('difficulty', 'unknown'))
    return list(difficulties)
