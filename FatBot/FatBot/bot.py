from botcity.core import DesktopBot
from selenium.webdriver.common.keys import Keys

# Uncomment the line below for integrations with BotMaestro
# Using the Maestro SDK
# from botcity.maestro import *

class Bot(DesktopBot):

    def __int__(self, opc_ext=int, dados_json_ext=map):
        super().__init__()
        self.opc = opc_ext
        self.dados_json = dados_json_ext

    def action(self, execution=None, opc=int, dados_json=map):
        # Uncomment to silence Maestro errors when disconnected
        # if self.maestro:
        #     self.maestro.RAISE_NOT_CONNECTED = False

        # Fetch the Activity ID from the task:
        # task = self.maestro.get_task(execution.task_id)
        # activity_id = task.activity_id

        # Opens the BotCity website.
        self.opc = opc
        self.dados_json = dados_json

        if self.opc == 0:

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

            for i in range(0, len(self.dados_json)):

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

                self.paste(self.dados_json[i]['CodProd'])

                self.wait(10000)

                self.enter()

                self.wait(1500)

                self.tab()

                self.paste(self.dados_json[i]['Quant'])

                self.tab()

                self.paste(self.dados_json[i]['DescObv'])

                self.tab()

                self.tab()

                self.tab()

                self.paste(self.dados_json[i]['Dt'])
                # self.paste("15/01/2024")

                self.tab()

                self.paste(self.dados_json[i]['Ccontabil'])

                self.wait(1500)

                self.tab()

                self.paste(self.dados_json[i]['Ccusto'])

                self.wait(1500)

                self.tab()

                self.paste(self.dados_json[i]['DescObvInter'])

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

        elif self.opc == 1:

            # BOOT TEAMS
            self.execute(r"C:\AutoBoot\Atalhos\Microsoft Teams.lnk")

            self.wait(2000)

            for i in range(0, len(self.dados_json)):

                print(i)


                if not self.find( "novaConversa", matching=0.97, waiting_time=10000):
                    self.not_found("novaConversa")
                self.click()

                self.move_random(range_x=100, range_y=200)

                self.wait(500)

                self.paste(self.dados_json[i]['Destinatario'])

                self.wait(2000)

                self.tab()

                self.wait(500)

                if self.dados_json[i]['Tipo'] == "User":
                    self.tab()

                self.wait(500)

                self.paste(self.dados_json[i]['Msg'])

                self.enter()
                
            if not self.find( "fecharTeams", matching=0.97, waiting_time=10000):
                self.not_found("fecharTeams")
            self.click()
             

        elif self.opc == 2:

            self.execute(r"C:\AutoBoot\Atalhos\OUTLOOK.lnk")

            if not self.find( "pagInicial", matching=0.97, waiting_time=20000):
                self.not_found("pagInicial")
            self.click()

            for i in range(0, len(self.dados_json)):

                if not self.find( "novoEmail", matching=0.97, waiting_time=20000):
                    self.not_found("novoEmail")
                self.click()

                self.paste(self.dados_json[i]['Emails'])

                self.tab()
                self.tab()
                self.tab()

                # if CCO == True:
                #     self.tab()

                self.tab()

                self.paste(self.dados_json[i]['Assunto'])

                self.tab()

                self.paste(self.dados_json[i]['MSG1'])

                self.enter()
                self.enter()

                self.paste(self.dados_json[i]['MSG2'])

                self.enter()

                self.tab()

                self.paste(self.dados_json[i]['MSG3'])

                self.enter()

                self.tab()

                self.paste(self.dados_json[i]['MSG4'])

                self.enter()

                self.tab()

                self.paste(self.dados_json[i]['MSG5'])

                self.enter()
                
                if not self.find( "enviarEmail", matching=0.97, waiting_time=10000):
                     self.not_found("enviarEmail")
                self.click()
             

                




        # Uncomment to mark this task as finished on BotMaestro
        # self.maestro.finish_task(
        #     task_id=execution.task_id,
        #     status=AutomationTaskFinishStatus.SUCCESS,
        #     message="Task Finished OK."
        # )

    def not_found(self, label):
        print(f"Element not found: {label}")


# if __name__ == '__main__':
#     Bot.main()







