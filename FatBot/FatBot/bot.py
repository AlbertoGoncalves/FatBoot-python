from botcity.core import DesktopBot

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

            # self.browse("https://sweetfruits.e-tetris.com/")
            #
            # self.wait(5000)
            #
            # if not self.find( "logAcessar", matching=0.97, waiting_time=10000):
            #     self.not_found("logAcessar")
            # self.click()
            #
            # self.wait(2000)
            #
            # if not self.find( "click1", matching=0.97, waiting_time=10000):
            #     self.not_found("click1")
            # self.click()
            #
            # self.wait(1000)
            #
            # if not self.find( "clickCompras", matching=0.97, waiting_time=10000):
            #     self.not_found("clickCompras")
            # self.click()
            #
            # self.wait(1000)
            #
            # if not self.find( "bntAcessar", matching=0.97, waiting_time=10000):
            #     self.not_found("bntAcessar")
            # self.click()

            if not self.find( "Abrir page SC", matching=0.97, waiting_time=200000):
                self.not_found("Abrir page SC")

            flial = self.dados_json[0]['Filial']

            if flial != "0101":
                self.tab()
                self.tab()
                self.enter()

                if flial == "0104":
                    for i in range(0, 3):
                        self.tab()
                elif flial == "0109":
                    for i in range(0, 5):
                        self.tab()
                elif flial == "0111":
                    for i in range(0, 6):
                        self.tab()
                elif flial == "0113":
                    for i in range(0, 7):
                        self.tab()
                elif flial == "1201":
                    for i in range(0, 13):
                        self.tab()
                elif flial == "2001":
                    for i in range(0, 14):
                        self.tab()
                elif flial == "2101":
                    for i in range(0, 15):
                        self.tab()
                elif flial == "2201":
                    for i in range(0, 16):
                        self.tab()

                self.enter()
                self.wait(10000)

                if not self.find( "Abrir page SC", matching=0.97, waiting_time=200000):
                    self.not_found("Abrir page SC")

            if not self.find( "btIncluir", matching=0.97, waiting_time=10000):
                self.not_found("btIncluir")
            self.click()

            for i in range(0, len(self.dados_json)):

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

                self.wait(15000)

                self.enter()

                self.wait(1500)

                self.tab()

                self.paste(self.dados_json[i]['Quant'])

                self.tab()

                self.paste(self.dados_json[i]['DescObv'])

                self.tab()

                self.type_up()
                self.type_up()
                self.type_up()

                if self.dados_json[i]['Tipo'] == 'Emergencial':
                    self.type_down()
                elif self.dados_json[i]['Tipo'] == 'Regularização':
                    self.type_down()
                    self.type_down()
                self.tab()

                self.tab()

                self.paste(self.dados_json[i]['Dt'])

                self.wait(3000)

                self.tab()

                self.paste(self.dados_json[i]['Ccontabil'])

                self.wait(3000)

                self.tab()

                self.paste(self.dados_json[i]['Ccusto'])

                self.wait(3000)

                self.tab()

                self.paste(self.dados_json[i]['DescObvInter'])

                self.tab()

                if not self.find( "addItem", matching=0.97, waiting_time=80000):
                    self.not_found("addItem")
                self.click()

                self.wait(15000)

            # Para incluir SC
            if not self.find( "EnvSC", matching=0.97, waiting_time=80000):
                self.not_found("EnvSC")
            self.click()

            # self.wait(70000)

            if not self.find( "Abrir page SC", matching=0.97, waiting_time=200000):
                self.not_found("Abrir page SC")

            if not self.find( "bntUser", matching=0.97, waiting_time=80000):
                self.not_found("bntUser")
            self.click()

            if not self.find( "bntSair", matching=0.97, waiting_time=80000):
                self.not_found("bntSair")
            self.click()

            if not self.find( "bntSimSair", matching=0.97, waiting_time=80000):
                self.not_found("bntSimSair")
            self.click()

        elif self.opc == 1:

            self.execute(r"C:\AutoBoot\Atalhos\Microsoft Teams.lnk")

            self.wait(2000)

            for i in range(0, len(self.dados_json)):

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

                if self.dados_json[i]['Msg'] == "":
                    self.paste(self.dados_json[i]['Msg'])

                self.type_keys(["shift", "enter"])

                self.paste(self.dados_json[i]['Msg1'])

                self.type_keys(["shift", "enter"])

                self.paste(self.dados_json[i]['Msg2'])

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

                self.enter()
                self.tab()
                self.tab()
                self.tab()

                # if CCO == True:
                #     self.tab()

                if self.dados_json[i]['Assunto'] != "txt":
                    self.paste(self.dados_json[i]['Assunto'])

                self.tab()

                if self.dados_json[i]['MSG1'] != "txt":
                    self.paste(self.dados_json[i]['MSG1'])

                self.enter()
                self.enter()

                if self.dados_json[i]['MSG2'] != "txt":
                    self.paste(self.dados_json[i]['MSG2'])

                self.enter()

                self.tab()

                if self.dados_json[i]['MSG3'] != "txt":
                    self.paste(self.dados_json[i]['MSG3'])

                self.enter()

                self.tab()

                if self.dados_json[i]['MSG4'] != "txt":
                    self.paste(self.dados_json[i]['MSG4'])

                self.enter()

                self.tab()

                if self.dados_json[i]['MSG5'] != "txt":
                    self.paste(self.dados_json[i]['MSG5'])

                self.enter()
                
                if not self.find( "enviarEmail", matching=0.97, waiting_time=10000):
                     self.not_found("enviarEmail")
                self.click()

        elif self.opc == 3:

            self.execute(r"C:\AutoBoot\Atalhos\OUTLOOK.lnk")
            
            if not self.find( "pesquisaEmail", matching=0.97, waiting_time=100000):
                self.not_found("pesquisaEmail")
            self.click()
            
            self.paste("MODELO_PROTOCOLO_COMPRAS")

            self.wait(1000)

            self.tab()
            self.tab()
            self.tab()
            self.tab()
            self.tab()

            self.enter()

            self.control_t()

            self.control_c()

            self.alt_f4()

            if not self.find( "PageIni", matching=0.97, waiting_time=10000):
                self.not_found("PageIni")
            self.click()
            

            if not self.find( "novoEmail", matching=0.97, waiting_time=20000):
                self.not_found("novoEmail")
            self.click()

            # self.paste(self.dados_json[0]['Emails'])

            self.tab()
            self.tab()
            self.tab()
            # if CCO == True:
            #     self.tab()

            # self.paste(self.dados_json[0]['Assunto'])

            self.tab()

            self.control_v()

            self.scroll_up(clicks=10)
            
            if not self.find( "A", matching=0.97, waiting_time=30000):
                self.not_found("A")
            self.click()
            
            

            self.click()
            self.click()
            self.click()

            for i in range(0, len(self.dados_json)):

                self.paste(self.dados_json[i]['Sc'])

                self.tab()

                self.paste(self.dados_json[i]['NF'])

                self.tab()

                self.paste(self.dados_json[i]['Filial'])

                self.tab()

                self.paste(self.dados_json[i]['DtEmissao'])

                self.tab()

                self.paste(self.dados_json[i]['Fornecedor'])

                self.tab()

                self.paste(self.dados_json[i]['Valor'])

                self.tab()

                self.paste(self.dados_json[i]['Vencimento'])

                self.tab()
                self.tab()

            if not self.find( "clicPara", matching=0.97, waiting_time=10000):
                self.not_found("clicPara")
            self.click()

            self.key_esc()

            self.tab()
            self.tab()
            self.tab()

            self.paste(self.dados_json[0]['Emails'])

            self.tab()
            self.tab()
            self.tab()
            # if CCO == True:
            #     self.tab()

            self.paste(self.dados_json[0]['Assunto'])

            if not self.find( "enviarEmail", matching=0.97, waiting_time=10000):
                self.not_found("enviarEmail")
            self.click()

            self.key_esc()

            self.wait(10000)

            self.alt_f4()

        elif self.opc == 4:
            timeWait = 1500
            timePressed = 5
            numScrollDown = 50
            autoPages = True

            self.execute(r"C:\AutoBoot\Atalhos\Google Chrome.lnk")
            self.wait(2000)

            while autoPages:
                self.type_keys(["home"])
                self.wait(1000)


                for i in range(0, numScrollDown):
                    self.type_down(timePressed)
                    self.wait(timeWait)


                self.type_keys(["Ctrl", "tab"])
                self.type_keys(["home"])
                self.wait(1500)

                for i in range(0, numScrollDown):
                    self.type_down(timePressed)
                    self.wait(timeWait)

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










