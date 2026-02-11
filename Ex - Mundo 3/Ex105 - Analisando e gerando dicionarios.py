def notas(*num, sit=False):
    """
    ->Funcao para analisar notas e situacoes de varios alunos
    :param num: Uma ou mais notas dos alunos
    :param sit: valor opcional, indicando se deve ou nao adicionar a situacao
    :return: dicionario com varias informacoes sobre a situacao da turma
    """
    aluno = dict()
    aluno['total'] = len(num)
    aluno['maior'] = max(num)
    aluno['menor'] = min(num)
    aluno['media'] = sum(num) / len(num)
    if sit:
        if aluno['media'] >= 7:
            aluno['situacao'] = 'APROVADO'
        else:
            aluno['situacao'] = 'REPROVADO'
    return aluno


resp = notas(5.5, 2.5, 10, 6.5, sit=True)
print(resp)