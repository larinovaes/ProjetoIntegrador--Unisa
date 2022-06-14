from collections import Counter
import os

#variaveis
votos = Counter()
voto = ''
turno = True
votacaovere = True
votacaopref = True
resposta = ''
candidatos = ''
candidatoid = ''
funcao = ''
decicao = ''
opcoes = '\n  [1] - Sim\n  [2] - Não\n'
clearConsole = lambda: os.system('cls'
                                 if os.name in ('nt', 'dos') else 'clear')
continuarVotacao = ''


def computarVoto(decicao):
    if decicao == '1':
        votos.update([candidatoid])
        return False
    else:
        return True


candidatos = {
    '11': 'Diogo Enrico Cardoso',
    '12': 'Helena Alice',
    '22': 'Bernardo Benício Cardoso',
    '02733': 'Bryan Giovanni Tomás Costa',
    '02891': 'Helena Eduarda Cristiane',
    '12786': 'Theo Ryan Costa',
    '15102': 'Bernardo Matheus Isaac Farias',
    '72319': 'Analu Fernanda',
    '10233': 'Oliver Guilherme Juan Farias',
    '11928': 'Geraldo Marcos Nunes',
    '09011': 'Letícia Juliana',
    '20120': 'Emanuel Victor Nunes',
    '22283': 'Gabriel do Cunha',
    'x': 'Voto Invalidado'
}

print("BEM VINDO AS ELEICÕES 2022 \n")

resposta = input(
    "Digite [1] para imprimir zerésima: \nDigite [2] iniciar votação: \n")

clearConsole()
if (resposta == '1'):
    #exibir votos (Zerésima)
    for candidatoid in candidatos:
        votos.update([candidatoid])
        votos.subtract([candidatoid])
    print('Zerésima:\n')
    for numero, qtd_votos in votos.most_common():
        if len(numero) == 5:
            funcao = 'Vereador'
        elif len(numero) == 2:
            funcao = 'Prefeito'
        print(f'{funcao}  {candidatos[numero]}:{qtd_votos} votos')
elif (resposta == '2'):
    #iniciar votação
    while turno == True:
        print('BEM VINDO AS ELEICÕES 2022 \n\n')
        votacaovere = True
        votacaopref = True
        while votacaovere == True:
            clearConsole()
            candidatoid = input(
                "(Digite [0] para votar em branco)\nSEU VOTO PARA VEREADOR:")
            if candidatoid == '0' or len(candidatoid) != 5:
                decicao = input(f'Confirmar voto em branco?{opcoes}')
                candidatoid = 'x'
                votacaovere = computarVoto(decicao)
            #else:
            #loop
            elif candidatoid in candidatos:
                decicao = input(
                    f'{candidatos[candidatoid]}, Confirmar voto?{opcoes}')
                votacaovere = computarVoto(decicao)
            #else:
            #loop
            elif not candidatoid in candidatos:
                decicao = input(f'Candidato inválido, votar nulo?{opcoes}')
                candidatoid = 'x'
                votacaovere = computarVoto(decicao)
            #else:
            #loop
        clearConsole()

        while votacaopref == True:
            clearConsole()
            candidatoid = input(
                "(Digite [0] para votar em branco)\nSEU VOTO PARA PREFEITO:")
            if candidatoid == '0' or len(candidatoid) != 2:
                decicao = input(f'Confirmar voto em branco?{opcoes}')
                candidatoid = 'x'
                votacaopref = computarVoto(decicao)
            #else:
            #loop
            elif candidatoid in candidatos:
                decicao = input(
                    f'{candidatos[candidatoid]}, Confirmar voto?{opcoes}')
                votacaopref = computarVoto(decicao)
            #else:
            #loop
            elif not candidatoid in candidatos:
                decicao = input(f'Candidato inválido, votar nulo?{opcoes}')
                candidatoid = 'x'
                votacaopref = computarVoto(decicao)
            #else:
            #loop
        clearConsole()
        continuarVotacao = input(
            '[1] - [Finalizar] a votação ou [2] - [Continuar]?')
        if continuarVotacao == '1' or continuarVotacao == 'Finalizar':
            turno = False

    print('Resultado:')
    for numero, qtd_votos in votos.most_common():
        if candidatos[numero] == 'Voto Invalidado':
            votos_invalidos = {qtd_votos}
        else:
            print(f'{candidatos[numero]} teve {qtd_votos} votos')
    print(f'{votos_invalidos} votos foram invalidados')
