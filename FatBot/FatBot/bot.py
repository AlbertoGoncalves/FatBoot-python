import os
from pathlib import Path
import pandas as pd
from botcity.core import DesktopBot

# abrindo planilha em excel e transformando em Json
p = Path(os.getcwd())
raiz = p.parent.parent.parent.parent.parent.parent
print(raiz)
caminho = ( str(raiz) + 'AutoBoot\Arquivos\\')
print(caminho)

# Conteudo opc (1 - Incluir SC) (2 - Teams) (3 - Enviar E-Mails)
opc = 3


VldJson = False

# transformando excel em json com Pandas
if opc == 1:
    excel_data_df = pd.read_excel(caminho + 'ListSC.xlsx', sheet_name='Dados_incluir_SC')
    VldJson = True
elif opc == 2:
    excel_data_df = pd.read_excel(caminho + 'ListSC.xlsx', sheet_name='Dados_Msg_Teams')
    VldJson = True
elif opc == 3:
    excel_data_df = pd.read_excel(caminho + 'ListSC.xlsx', sheet_name='Dados_Enviar_Email')
    VldJson = True
else:
    print('Opção não disponivel')

if VldJson:
    dadosJson = excel_data_df.to_json()
    print('Excel Sheet to JSON:\n', dadosJson)




# Uncomment the line below for integrations with BotMaestro
# Using the Maestro SDK
# from botcity.maestro import *



class Bot(DesktopBot):
    def action(self, execution=None):
        # Uncomment to silence Maestro errors when disconnected
        # if self.maestro:
        #     self.maestro.RAISE_NOT_CONNECTED = False

        # Fetch the Activity ID from the task:
        # task = self.maestro.get_task(execution.task_id)
        # activity_id = task.activity_id

        # Opens the BotCity website.

        if opc == 1:

            self.browse("https://sweetfruits.e-tetris.com/")

            self.wait(2000)

            if not self.find( "logAcessar", matching=0.97, waiting_time=10000):
                self.not_found("logAcessar")
            self.click()

            self.wait(2000)

            if not self.find( "click1", matching=0.97, waiting_time=10000):
                self.not_found("click1")
            self.click()

            self.wait(1000)

            if not self.find( "clickCompras", matching=0.97, waiting_time=10000):
                self.not_found("clickCompras")
            self.click()

            self.wait(1000)

            if not self.find( "bntAcessar", matching=0.97, waiting_time=10000):
                self.not_found("bntAcessar")
            self.click()

            if not self.find( "Abrir page SC", matching=0.97, waiting_time=70000):
                self.not_found("Abrir page SC")

            if not self.find( "btIncluir", matching=0.97, waiting_time=10000):
                self.not_found("btIncluir")
            self.click()

            for i in range(0, len(dadosJson)):

                print(i)

                if i != 0:
                    if not self.find( "addNovoItem", matching=0.97, waiting_time=10000):
                        self.not_found("addNovoItem")
                    self.click()

                if not self.find( "aguardPageAdd", matching=0.97, waiting_time=10000):
                    self.not_found("aguardPageAdd")

                if not self.find( "posicioneParaTab", matching=0.97, waiting_time=10000):
                    self.not_found("posicioneParaTab")
                self.click()

                self.tab()

                self.paste(dadosJson[i]['CodProd'])

                self.wait(10000)

                self.enter()

                self.wait(1500)

                self.tab()

                self.paste(dadosJson[i]['Quant'])

                self.tab()

                self.paste(dadosJson[i]['DescObv'])

                self.tab()

                self.tab()

                self.tab()

                self.paste(dadosJson[i]['Dt'])
                # self.paste("15/01/2024")

                self.tab()

                self.paste(dadosJson[i]['Ccontabil'])

                self.wait(1500)

                self.tab()

                self.paste(dadosJson[i]['Ccusto'])

                self.wait(1500)

                self.tab()

                self.paste(dadosJson[i]['DescObvInter'])

                self.tab()

                if not self.find( "addItem", matching=0.97, waiting_time=10000):
                    self.not_found("addItem")
                self.click()

                self.wait(15000)

                print("Vou Add novo item")

            # Para incluir SC
            if not self.find( "EnvSC", matching=0.97, waiting_time=10000):
                self.not_found("EnvSC")
            self.click()
            
            if not self.find( "bntUser", matching=0.97, waiting_time=10000):
                self.not_found("bntUser")
            self.click()
            
            if not self.find( "bntSair", matching=0.97, waiting_time=10000):
                self.not_found("bntSair")
            self.click()

            if not self.find( "bntSimSair", matching=0.97, waiting_time=10000):
                self.not_found("bntSimSair")
            self.click()

        elif opc == 2:

            # BOOT TEAMS
            self.execute(r"C:\AutoBoot\Atalhos\Microsoft Teams.lnk")

            if not self.find("Pesquisar", matching=0.97, waiting_time=10000):
                self.not_found("Pesquisar")
            self.click()

            self.paste("Setor TI")

            if not self.find("GrupoTI", matching=0.97, waiting_time=10000):
                self.not_found("GrupoTI")
            self.click()

            if not self.find("caixa digit", matching=0.97, waiting_time=10000):
                self.not_found("caixa digit")
            self.click()

            self.paste(
                "Bom dia, Reunião diária hoje as 08:30, favor não ausentar-se da estão de trabalho entre 08:15 a 08:30.")

            # self.paste("Teste autoBoot")

            self.enter()

        elif opc == 3:
            self.execute(r"C:\AutoBoot\Atalhos\OUTLOOK.lnk")

            if not self.find( "pagInicial", matching=0.97, waiting_time=10000):
                self.not_found("pagInicial")
            self.click()

            for i in range(0, len(dadosJson)):
            
                if not self.find( "novoEmail", matching=0.97, waiting_time=10000):
                    self.not_found("novoEmail")
                self.click()

                self.paste(dadosJson[i]['Emails'])

                self.tab()
                self.tab()
                self.tab()

                self.paste(dadosJson[i]['Emails'])

        # Uncomment to mark this task as finished on BotMaestro
        # self.maestro.finish_task(
        #     task_id=execution.task_id,
        #     status=AutomationTaskFinishStatus.SUCCESS,
        #     message="Task Finished OK."
        # )

    def not_found(self, label):
        print(f"Element not found: {label}")


if __name__ == '__main__':
    Bot.main()













