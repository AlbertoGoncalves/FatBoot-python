"""
WARNING:

Please make sure you install the bot with `pip install -e .` in order to get all the dependencies
on your Python environment.

Also, if you are using PyCharm or another IDE, make sure that you use the SAME Python interpreter
as your IDE.

If you get an error like:
```
ModuleNotFoundError: No module named 'botcity'
```

This means that you are likely using a different Python interpreter than the one used to install the bot.
To fix this, you can either:
- Use the same interpreter as your IDE and install your bot with `pip install -e .`
- Use the same interpreter as the one used to install the bot (`pip install -e .`)

Please refer to the documentation for more information at https://documentation.botcity.dev/
"""

from botcity.core import DesktopBot

# Uncomment the line below for integrations with BotMaestro
# Using the Maestro SDK
# from botcity.maestro import *

ListSc = [
 {
  "Filial": "0101",
  "CodProd": "0003565",
  "DescProd": "SERVICO INFORMACAO P\/INTERNET",
  "Quant": "1",
  "DescObv": "Descrição Protheus",
  "Dt": "15/08/2023",
  "Ccontabil": "8104010005",
  "Ccusto": "2150101001",
  "DescObvInter": "Descrição interna "
 },
 {
  "Filial": "0101",
  "CodProd": "0003786",
  "DescProd": "SERVICO LICENCIAMENTO OU CESSAO USO DE SOFTWARES",
  "Quant": "1",
  "DescObv": "Descrição Protheus",
  "Dt": "15/08/2023",
  "Ccontabil": "8104010005",
  "Ccusto": "2150101001",
  "DescObvInter": "Descrição interna "
 },
 {
  "Filial": "0101",
  "CodProd": "0011902",
  "DescProd": "PROCESSAMENO, ARMAZENAMENTO OU HOSPEDAGEM DE DADOS",
  "Quant": "1",
  "DescObv": "Descrição Protheus",
  "Dt": "15/08/2023",
  "Ccontabil": "8104010005",
  "Ccusto": "2150101001",
  "DescObvInter": "Descrição interna "
 }
]


class Bot(DesktopBot):
    def action(self, execution=None):
        # Uncomment to silence Maestro errors when disconnected
        # if self.maestro:
        #     self.maestro.RAISE_NOT_CONNECTED = False

        # Fetch the Activity ID from the task:
        # task = self.maestro.get_task(execution.task_id)
        # activity_id = task.activity_id

        # Opens the BotCity website.

        self.browse("https://sweetfruits.e-tetris.com/")

        if not self.find("Abrir page SC", matching=0.97, waiting_time=70000):
            self.not_found("Abrir page SC")

        if not self.find("btIncluir", matching=0.97, waiting_time=10000):
            self.not_found("btIncluir")
        self.click()

        for i in range(0, len(ListSc)):
            
            if i != 0:
                if not self.find("addNovoItem", matching=0.97, waiting_time=10000):
                    self.not_found("addNovoItem")
                self.click()

            if not self.find("aguardPageAdd", matching=0.97, waiting_time=10000):
                self.not_found("aguardPageAdd")

            if not self.find("posicioneParaTab", matching=0.97, waiting_time=10000):
                self.not_found("posicioneParaTab")
            self.click()

            self.tab()

            self.paste(ListSc[i]['CodProd'])

            self.wait(10000)

            self.enter()

            self.wait(1500)

            self.tab()

            self.paste(ListSc[i]['Quant'])

            self.tab()

            self.paste(ListSc[i]['DescObv'])

            self.tab()

            self.tab()

            self.tab()

            self.paste(ListSc[i]['Dt'])
            # self.paste("15/01/2024")

            self.tab()

            self.paste(ListSc[i]['Ccontabil'])

            self.wait(1500)

            self.tab()

            self.paste(ListSc[i]['Ccusto'])

            self.wait(1500)

            self.tab()

            self.paste(ListSc[i]['DescObvInter'])

            self.tab()

            if not self.find("addItem", matching=0.97, waiting_time=10000):
                self.not_found("addItem")
            self.click()

            self.wait(10000)

        # Para incluir SC
        if not self.find("EnvSC", matching=0.97, waiting_time=10000):
            self.not_found("EnvSC")
        self.click()

        # BOOT TEAMS
        # self.execute(r"C:\AutoBoot\Atalhos\Microsoft Teams.lnk")
        #
        # if not self.find( "Pesquisar", matching=0.97, waiting_time=10000):
        #     self.not_found("Pesquisar")
        # self.click()
        #
        # self.paste("Setor TI")
        #
        # if not self.find( "GrupoTI", matching=0.97, waiting_time=10000):
        #     self.not_found("GrupoTI")
        # self.click()
        #
        # if not self.find( "caixa digit", matching=0.97, waiting_time=10000):
        #     self.not_found("caixa digit")
        # self.click()
        #
        # self.paste("Bom dia, Reunião diária hoje as 08:30, favor não ausentar-se da estão de trabalho entre 08:15 a 08:30.")
        #
        # # self.paste("Teste autoBoot")
        #
        # self.enter()

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
