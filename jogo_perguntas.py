print()
print('Digite uma das opções e tecle enter para confirmar sua resposta em cada pergunta.')

perguntas = {
    'Pergunta 1': {
        'pergunta': 'Quanto é 2 + 2?',
        'respostas': {
            'a': '1',
            'b': '4',
            'c': '5',
            'd': '18',
        },
        'resposta_certa': 'b',
    }, 'Pergunta 2': {
        'pergunta': 'Quanto é 16 + 33?',
        'respostas': {
            'a': '44',
            'b': '45',
            'c': '49',
            'd': '40',
        },
        'resposta_certa': 'c',
    }, 'Pergunta 3': {
        'pergunta': 'Quanto é 5 * 5?',
        'respostas': {
            'a': '25',
            'b': '15',
            'c': '45',
            'd': '55',
        },
        'resposta_certa': 'a',
    }, 'Pergunta 4': {
        'pergunta': 'Quanto é 15 * 5?',
        'respostas': {
            'a': '55',
            'b': '85',
            'c': '75',
            'd': '95',
        },
        'resposta_certa': 'c',
    }, 'Pergunta 5': {
        'pergunta': 'Quanto é 12 * 5?',
        'respostas': {
            'a': '55',
            'b': '60',
            'c': '65',
            'd': '45',
        },
        'resposta_certa': 'b',
    },
}

print()
respostas_certas = 0

for pk, pv in perguntas.items():
    print(f'{pk} : {pv["pergunta"]}')

    print('Escolha uma das opções abaixo: ')
    for rk, rv in pv['respostas'].items():
        print(f'[{rk}]: {rv}')

    resposta_user = input('Digite a alternativa da sua resposta: ')

    if resposta_user == pv['resposta_certa']:
        print('Resposta correta!')
        respostas_certas += 1
    else:
        print('Resposta incorreta.')

    print()

qtd_perguntas = len(perguntas)
porcentagem_acerto = respostas_certas / qtd_perguntas * 100

print(f'Você acertou {respostas_certas} resposta(s).')
print(f'Sua porcentagem de acerto foi: {porcentagem_acerto}%.')