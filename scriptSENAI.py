from os import system


def CalcularIRRF():
    salario = float(input('Salário Bruto: R$ '))
    dependentes = float(input('Depentes: '))
    dependentes_valor = float(dependentes * 189.59)
    inss_valor = float()

    if salario <= 1045:
        inss_valor = salario * 0.075

    elif 1045.01 < salario < 2089.6:
        inss_valor = salario * 0.09

    elif 2089.61 < salario < 3134.4:
        inss_valor = salario * 0.12

    elif 3134.41 < salario < 6101.06:
        inss_valor = salario * 0.14

    base_de_calculo = float(salario - inss_valor - dependentes_valor)
    aliquota = 0.00
    parcela_deducao = 0.00

    if 1903.99 < base_de_calculo < 2826.66:
        aliquota = 0.075
        parcela_deducao = 142.80

    if 2826.67 < base_de_calculo < 3751.06:
        aliquota = 0.15
        parcela_deducao = 354.80

    if 3751.07 < base_de_calculo < 4664.68:
        aliquota = 0.225
        parcela_deducao = 636.13

    if 4664.69 < base_de_calculo:
        aliquota = 0.275
        parcela_deducao = 869.36

    irpf = (base_de_calculo * aliquota) - parcela_deducao

    if irpf <= 0:
        irpf_valor = 'NÃO TEM'
    else:
        irpf_valor = irpf

    print('\nINSS: ', inss_valor)
    print('Aliquota: ', aliquota)
    print('Parcela de Dedução: ', parcela_deducao)
    print('Base de Calculo: ', base_de_calculo)
    print('IRPF: ', irpf_valor)
    print('=-'*30)
    input('Pressione ENTER para continuar ')
    print('=-'*30)


def CalcularHX():

    salario = float(input('Salário Bruto: R$ '))
    periculosidade = str(input('Recebe Periculosidade? s/n: '))
    insalubridade = int(input('Porcentagem de Insalubridade: %'))
    jornada = float(input('Jornada de trabalho diaria: '))
    hx100 = float(input('Horas Extras feitas à 100%: '))
    hx70 = float(input('Horas Extras feiats à 70%: '))
    hx50 = float(input('Horas Extras feitas à 50%: '))

    insalubridade_valor = float(0)
    adicional = float(0)
    periculosidade_valor = float(salario * 0.3)

    if periculosidade == 'n':
        periculosidade_valor = 0
    if periculosidade == 's':
        periculosidade_valor = float(salario * 0.3)

    if insalubridade != 0:
        if insalubridade == 10:
            insalubridade_valor = 1045 * 0.1
        if insalubridade == 20:
            insalubridade_valor = 1045 * 0.2
        if insalubridade == 30:
            insalubridade_valor = 1045 * 0.3
        if insalubridade == 40:
            insalubridade_valor = 1045 * 0.4

    if periculosidade_valor > insalubridade_valor:
        adicional = periculosidade_valor
    if insalubridade_valor > periculosidade_valor:
        adicional = insalubridade_valor

    if jornada == 8:
        jornada = 220
    if jornada == 6:
        jornada = 150
    if jornada == 12:
        jornada = 180
    if jornada == 4:
        jornada = 100

    recebe_por_hora = (salario + adicional) / jornada
    hx100_valor = recebe_por_hora * (hx100 * 2.0)
    hx50_valor = recebe_por_hora * ((hx50 * 0.5) + hx50)
    hx70_valor = recebe_por_hora * ((hx70 * 0.7) + hx70)
    totalHX = hx100_valor + hx70_valor + hx50_valor

    print('\nPericulosidade: ', periculosidade_valor)
    print('Insalubridade: ', insalubridade_valor)
    print('Adicional usado: ', adicional)
    print('Horas Extras à 100%: ', hx100_valor)
    print('Horas Extras à 70%: ', hx70_valor)
    print('Horas Extras à 50%: ', hx50_valor)
    print('Total de Horas Extras: ', totalHX)
    print('\nPara calcular o DRS ou RSR:\n'
          '( {0} / Dias Uteis ) * Domingos e Feriados'.format(totalHX))
    print('=-'*30)
    input('Pressione ENTER para continuar ')
    print('=-'*30)


def Main():

    system('cls')
    print("=-" * 30)
    print('SCRIPT FOLHA DE PAGAMENTO\nDesenvolvido por Thales Oliveira')
    print("=-" * 30)
    print('')
    print('=-'*30)
    print('[1] Calcular HORAS EXTRAS')
    print('[2] Calcular IRRF')
    print('')
    print('[0] SAIR DO PROGRAMA')
    print('=-'*30)
    opcao = int(input('\nDigite o número de acordo com a opção desejada: '))
    print('=-'*30)

    if opcao == 1:
        system('cls')
        CalcularHX()
        system('cls')
    elif opcao == 2:
        system('cls')
        CalcularIRRF()
        system('cls')
    elif opcao == 0:
        exit()
    else:
        print('OPÇÃO INVALIDA, TENTE NOVAMENTE')
        print('=-'*30)


while True:
    Main()
