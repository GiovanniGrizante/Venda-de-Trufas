import math
from datetime import datetime
import os

# Medidas (em mL)
colher_sopa = 15
colher_chá = 5

# Dados do leite em pó
qtd_leite_pó_total = 400
custo_leite_pó_total = 15.9
relação_leite_pó = custo_leite_pó_total/qtd_leite_pó_total

# Dados do leite condensado
qtd_leite_cond_total = 395
custo_leite_cond_total = 5.29
relação_leite_cond = custo_leite_cond_total/qtd_leite_cond_total

# Dados creme de leite
qtd_creme_leite_total = 200
custo_creme_leite_total = 2.89
relação_creme_leite = custo_creme_leite_total/qtd_creme_leite_total

# Dados do coco
qtd_coco_total = 50
custo_coco_total = 3.99
relação_coco = custo_coco_total/qtd_coco_total

# Dados do chocolate meio amargo (casquinha)
qtd_choco_amargo_total = 1010
custo_choco_amargo_total = 25.90
relação_choco_amargo = custo_choco_amargo_total/qtd_choco_amargo_total

# Dados do chocolate ao leite (recheio tradicional)
# qtd_choco_leite_total = 1010
# custo_choco_total = 25.90
# relação_choco_leite = custo_choco_total/qtd_choco_leite_total

# Dados da manteiga
qtd_manteiga_total = 200
custo_manteiga_total = 10.99
relação_manteiga = custo_manteiga_total/qtd_manteiga_total

# Dados da embalagem
qtd_embalagem_total = 100
custo_embalagem_total = 16.7
relação_embalagem = custo_embalagem_total/qtd_embalagem_total

#########################################################################################################################

# Receita
qtd_leite_cond_receita = qtd_leite_cond_total
qtd_creme_leite_receita = qtd_creme_leite_total
qtd_manteiga_receita = 1*colher_sopa                                           # [mL]
qtd_leite_pó_receita = 13                                                      # [mL]
qtd_choco_receita = 300                                                        # [g]
qtd_coco_receita = 10                                                          # [g]

peso_trufa = 25                                                                # [g]


# Cálculos

# *NINHO*:

# Peso ideal (sem perdas)
peso_receita_ninho_ideal = (qtd_leite_cond_receita +                           # Leite condensado
                            qtd_creme_leite_receita +                          # Creme de leite
                            qtd_manteiga_receita +                             # Manteiga
                            qtd_leite_pó_receita +                             # Leite em pó
                            qtd_choco_receita)                                 # Chocolate

peso_receita_ninho_real = 375

# Custo
custo_receita_ninho =   (qtd_leite_cond_receita*relação_leite_cond +           # Leite condensado
                         qtd_creme_leite_receita*relação_creme_leite +         # Creme de leite
                         qtd_manteiga_receita*relação_manteiga +               # Manteiga
                         qtd_leite_pó_receita*relação_leite_pó +               # Leite em pó
                         qtd_choco_receita*relação_choco_amargo +              # Chocolate
                         relação_embalagem)                                    # Embalagem


# *PRESTÍGIO*:

# Peso
peso_receita_coco_ideal = (qtd_leite_cond_receita +                            # Leite condensado
                           qtd_creme_leite_receita +                           # Creme de leite
                           qtd_manteiga_receita +                              # Manteiga
                           qtd_coco_receita +                                  # Coco
                           qtd_choco_receita)                                  # Chocolate

peso_receita_coco_real = 352

# Custo
custo_receita_coco = (qtd_leite_cond_receita*relação_leite_cond +              # Leite condensado
                      qtd_creme_leite_receita*relação_creme_leite +            # Creme de leite
                      qtd_manteiga_receita*relação_manteiga +                  # Manteiga
                      qtd_coco_receita*relação_coco +                          # Coco
                      qtd_choco_receita*relação_choco_amargo +                 # Chocolate
                      relação_embalagem)                                       # Embalagem

#########################################################################################################################

# Definições finais

qtd_trufas_ninho_receita = math.trunc(peso_receita_ninho_real/peso_trufa)
sobras_trufas_ninho = ((peso_receita_ninho_real/peso_trufa) - qtd_trufas_ninho_receita)*peso_receita_ninho_real

qtd_trufas_coco_receita = math.trunc(peso_receita_coco_real/peso_trufa)
sobras_trufas_coco = ((peso_receita_coco_real/peso_trufa) - qtd_trufas_coco_receita)*peso_receita_coco_real


# Gerando arquivo de texto

dir = f'{os.path.expanduser("~")}\\Documents\\Trufas'
arquivo = f'Trufas - Dados {datetime.today().strftime("%d-%m-%Y")}.txt'

if not os.path.exists(dir):
    os.makedirs(dir)

with open(os.path.join(dir, arquivo),'w') as arq:
    arq.write(f'Dados sobre as trufas - {datetime.today().strftime("%d/%m/%Y")}\n')

    arq.write(f'\nPeso por trufa: {peso_trufa}g\n')

    arq.write('\nInformações sobre a receita de leite em pó:')
    arq.write(f'\nCusto total da receita: R${custo_receita_ninho :.2f}')
    arq.write(f'\nQuantidade de trufas por receita: {qtd_trufas_ninho_receita}')
    arq.write(f'\nPreço mínimo por trufa: R${custo_receita_ninho/qtd_trufas_ninho_receita :.2f}')
    arq.write(f'\nSobras da receita: {sobras_trufas_ninho :.1f}g')

    arq.write('\n\nInformações sobre a receita de prestígio:')
    arq.write(f'\nCusto total da receita: R${custo_receita_coco :.2f}')
    arq.write(f'\nQuantidade de trufas por receita: {qtd_trufas_coco_receita}')
    arq.write(f'\nPreço mínimo por trufa: R${custo_receita_coco/qtd_trufas_coco_receita :.2f}')
    arq.write(f'\nSobras da receita: {sobras_trufas_coco :.1f}g')

print('\nDados salvos com sucesso!')
print(f'Verificar em "{dir}"\n')