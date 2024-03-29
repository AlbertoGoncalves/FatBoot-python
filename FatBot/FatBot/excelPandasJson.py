import os
from pathlib import Path

import pandas as pd

from botcity.base.utils import find_bot_class
import FatBot.bot

klass = find_bot_class(FatBot.bot)[0]

def automacao(opc):

    # Conteudo opc (0 - Incluir SC) (1 - Teams) (2 - Enviar E-Mails)
    # print(opc)

    # abrindo planilha em excel e transformando em Json
    p = Path(os.getcwd())
    raiz = p.parent.parent.parent.parent.parent.parent
    # print(raiz)
    caminho = (str(raiz) + 'AutoBoot\Arquivos\\')
    # print(caminho)

    vld_json = False

    # transformando excel em json com Pandas
    if opc == 0:
        excel_data_df = pd.read_excel(caminho + 'ListSC.xlsx', sheet_name='Dados_incluir_SC', dtype=str)
        vld_json = True
    elif opc == 1:
        excel_data_df = pd.read_excel(caminho + 'ListSC.xlsx', sheet_name='Dados_Msg_Teams')
        vld_json = True
    elif opc == 2:
        excel_data_df = pd.read_excel(caminho + 'ListSC.xlsx', sheet_name='Dados_Enviar_Email')
        vld_json = True
    elif opc == 3:
        excel_data_df = pd.read_excel(caminho + 'ListSC.xlsx', sheet_name='Email_Protocolo_Compras', dtype=str)
        vld_json = True
    elif opc == 4:
        vld_json = False
    # else:
        # print('Opção não disponivel')

    if vld_json:
        # dados_json = excel_data_df.to_json(orient="records")
        dados_json = excel_data_df.to_dict(orient="records")
        print('Excel Sheet to JSON:\n', dados_json)
        klass.main(opc, dados_json)
    else:
        klass.main(opc, [])
