pizzas = {
    'Calabresa': {
        'ingredientes': ['molho', 'queijo', 'calabresa'],
        'custo': 0.20
    },
    'Calabresa com Catupiry': {  # Nome corrigido (estava duplicado como 'Calabresa')
        'ingredientes': ['molho', 'queijo', 'calabresa', 'Catupiry'],
        'custo': 0.23  # Vírgula substituída por ponto decimal
    },
    'Frango com Catupiry': {
        'ingredientes': ['molho', 'queijo', 'frango', 'Catupiry'],
        'custo': 0.25
    },
    'Mista Tradicional': {
        'ingredientes': ['molho', 'queijo', 'presunto', 'tomate'],
        'custo': 0.30
    },
    'Toscana': {
        'ingredientes': ['molho', 'queijo', 'presunto', 'calabresa', 'Frango'],
        'custo': 0.27
    },
    'Presunto e Catupiry': {
        'ingredientes': ['molho', 'queijo', 'presunto', 'frango', 'catupiry'],
        'custo': 0.24
    }
}


bordas = {'sem' : 0.00,
          'catupiry' : 1.20,
          'cheddar' : 1.00,
          'mussarela' : 00.70,
          'chocolate' : 2.00
          }

refri = {'sem refri' : 0.00,
         'coca-cola' : 6.50,
         'guarana' : 5.00,
         'sprite' : 6.00,
         'pepsi' : 5.60}

tamanhos = {'Pequena' : 625, 
            'Media': 900, 
            'Grande' : 1.225,
            'Familia' : 1.600}