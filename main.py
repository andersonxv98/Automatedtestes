import sys

from PyQt6.QtTest import QTest
from PyQt6.QtWidgets import QWidget, QLineEdit, QApplication, QMainWindow, QVBoxLayout, QLabel, QPushButton

from ClasseTodosValores import Prima
from Reflexo import ValidaPraTeste
from pynput.mouse import Button, Controller


class TesteClass(QMainWindow):
    def __init__(self):
        super().__init__()

        self.label = QLabel('Tester')
        self.vet_campo = {
        "campo1" : QLineEdit(),
        "campo2" : QLineEdit(),
        "campo3" : QLineEdit()
        }

        self.botao = QPushButton()
        self.botao.clicked.connect(self.Enviar)

        self.layout= QVBoxLayout()

        self.layout.addWidget(self.label)
        for lb in self.vet_campo.values():
            self.layout.addWidget(lb)
        self.layout.addWidget(self.botao)


        Widget = QWidget()
        Widget.setLayout(self.layout)
        self.setCentralWidget(Widget)

        self.mouse = Controller()


    def MovimentaMouse(self):

        a = self.x()
        b = self.botao.x()
        c = self.y()
        d = self.botao.y()

        corrY = 40

        posX = (a + b) + corrY
        posY = (c + d) + corrY
        self.mouse.position = (posX, posY)
        return

    def Enviar(self):
        for tb in self.vet_campo.values():

            try:

                val =int(tb.text())
                a =Prima(val)
                b= ValidaPraTeste()
                if((a.saldo) == b.saldo):
                    print("Classe Válida")
                    print("Entrada: ", tb.text())
                else:
                    print("classe inválida")
                    print("Entrada: ", tb.text())
            except:
                print("entrada inválida")
                print("INFOrMADO: ", tb.text())


    def SetAutomatedInput(self,t):
        for tb in self.vet_campo.values():
            tb.setText(str(t))
        return

    def ClickAutomatizado(self):
        self.mouse.press(Button.left)
        self.mouse.release(Button.left)
        print("clickou")
        return

    def ExecutarTeste(self):

        vet_val = {
                "ct1":"teste1",
              "ct2": 2,
               "ct3":-1,
               "ct4":1,
              "ct5": 0
                   }

        for value in vet_val.values():
            QTest.qWait(100)
            self.MovimentaMouse()
            QTest.qWait(100)
            entrada = value
            QTest.qWait(100)
            self.SetAutomatedInput(entrada)
            QTest.qWait(100)
            self.ClickAutomatizado()

            print("ultimo item: ", value)




def main():
    app = QApplication(sys.argv)
    window = TesteClass()
    window.show()
    window.ExecutarTeste()
    app.exec()

main()

