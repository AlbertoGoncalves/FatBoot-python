from botcity.core import DesktopBot


# Uncomment the line below for integrations with BotMaestro
# Using the Maestro SDK
# from botcity.maestro import *


class Bot(DesktopBot):

    def __int__(self, opc_ext=int, opc_ext1=int):
        super().__init__()
        self.opc = opc_ext
        self.opc1 = opc_ext1

    def action(self, execution=None, opc=int, opc1=int):
        # Uncomment to silence Maestro errors when disconnected
        # if self.maestro:
        #     self.maestro.RAISE_NOT_CONNECTED = False

        # Fetch the Activity ID from the task:
        # task = self.maestro.get_task(execution.task_id)
        # activity_id = task.activity_id

        # Opens the BotCity website.

        timeWait = int(opc)
        timePressed = 5
        numScrollDown = int(opc1)
        autoPages = True

        self.execute(r"C:\AutoBoot\Atalhos\Google Chrome.lnk")
        self.wait(3000)

        while autoPages:
            self.type_keys(["Ctrl", "tab"])
            self.wait(500)
            self.type_keys(["home"])
            self.wait(2000)

            for i in range(0, numScrollDown):
                self.type_down(timePressed)
                self.wait(timeWait)

            self.type_keys(["Ctrl", "tab"])
            self.wait(500)
            self.type_keys(["home"])
            self.wait(2000)

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











