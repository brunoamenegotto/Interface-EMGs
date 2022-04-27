import sys
import pandas as pd

from datetime import datetime

from PySide2.QtCharts import QtCharts
from PySide2.QtCore import QPointF, Slot, QTimer
from PySide2.QtWidgets import QApplication, QMainWindow, QMessageBox

from ui_interface import *
from serialPorta import ComunicacaoSerialPorta
from Custom_Widgets.Widgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.x = 0.0

        self.setMinimumSize(850, 600)

        loadJsonStyle(self, self.ui)

        self.serialComunicacao = ComunicacaoSerialPorta()
        self.listaPortasAcessiveis()
        self.ui.cbBaudrate.addItems(self.serialComunicacao.baudrates)

        self.ui.btnRecarregar.clicked.connect(self.listaPortasAcessiveis)
        self.ui.btnConectar.clicked.connect(self.btnConectar)
        self.ui.btnDeconectar.clicked.connect(self.btnDesconectar)
        self.ui.btnReceber.clicked.connect(self.btnReceberDados)
        self.ui.btnReset.clicked.connect(self.btnResetarDados)
        self.ui.btnSalvar.clicked.connect(self.btnSalvarDados)

        self.ui.btnDeconectar.setVisible(False)
        self.ui.btnReceber.setDisabled(True)
        self.ui.btnReset.setDisabled(True)
        self.ui.btnSalvar.setDisabled(True)

        self.dadoscsvX = []
        self.dadoscsvY = []

        self.serieGrafico = QtCharts.QSplineSeries()
        self.grafico = QtCharts.QChart()

        self.grafico.addSeries(self.serieGrafico)

        self.eixoX = QtCharts.QValueAxis()
        self.eixoX.setRange(0, 5000)
        self.eixoX.setTitleText("Tempo(ms)")
        
        self.eixoY = QtCharts.QValueAxis()
        self.eixoY.setRange(0, 3.3)
        self.eixoY.setTitleText("Tensão(V)")

        self.grafico.setAxisX(self.eixoX, self.serieGrafico)
        self.grafico.setAxisY(self.eixoY, self.serieGrafico)

        self.grafico.legend().hide()
        self.grafico.setTitle("Sinal de Eletromiografia")        
        self.serieGrafico.setName("Sinal")
        self.grafico.legend().setVisible(True)
        self.grafico.legend().setAlignment(Qt.AlignRight)

        self.ui.corpoConteudo = QtCharts.QChartView(self.grafico)
        self.ui.corpoConteudo.setRenderHint(QPainter.Antialiasing)
        self.ui.corpoConteudo.chart().setTheme(QtCharts.QChart.ChartThemeDark)

        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHeightForWidth(self.ui.corpoConteudo.sizePolicy().hasHeightForWidth())
        self.ui.corpoConteudo.setSizePolicy(sizePolicy)

        self.ui.corpoConteudo.setMinimumSize(QSize(0, 300))
        self.ui.lineChartCont.addWidget(self.ui.corpoConteudo)
        self.ui.graficoV.setStyleSheet(u"background-color: transparent")

        self.show()

    def listaPortasAcessiveis(self):
        self.serialComunicacao.listarPostas()
        self.ui.cbComports.clear()
        self.ui.cbComports.addItems(self.serialComunicacao.portas)
    
    def btnConectar(self):
        porta = self.ui.cbComports.currentText()
        baud = self.ui.cbBaudrate.currentText()

        self.serialComunicacao.serialInst.port = porta
        self.serialComunicacao.serialInst.baudrate = baud

        self.serialComunicacao.conectarSerial()

        self.ui.btnConectar.setVisible(False)
        self.ui.btnDeconectar.setVisible(True)
        self.ui.btnReceber.setDisabled(False)
    
    def btnDesconectar(self):
        self.serialComunicacao.desconectarSerial()

        self.ui.btnConectar.setVisible(True)
        self.ui.btnDeconectar.setVisible(False)
        self.ui.btnReceber.setDisabled(True)
        self.ui.btnReset.setDisabled(True)
        self.ui.btnSalvar.setDisabled(True)

    def btnReceberDados(self):
        self.ui.btnDeconectar.setDisabled(True)
        self.ui.btnReset.setDisabled(True)
        self.ui.btnSalvar.setDisabled(True)

        if self.serialComunicacao.serialInst.is_open:
            self.timer = QTimer()
            self.timer.timeout.connect(self.updatePlot)
            self.timer.start()
        else:
            QMessageBox.warning(self, "Alerta", "Erro ao receber os dados!")
    
    def btnResetarDados(self):
        self.x = 0

        self.serieGrafico.clear()

        self.dadoscsvX.clear()
        self.dadoscsvY.clear()
        self.serieGrafico.append(0, 0)
        self.timer.stop()
        self.serialComunicacao.serialInst.close()

        self.ui.btnDeconectar.setVisible(False)
        self.ui.btnConectar.setVisible(True)
        self.ui.btnReceber.setDisabled(True)
        self.ui.btnReset.setDisabled(True)
        self.ui.btnSalvar.setDisabled(True)

        QMessageBox.information(self, "Informação", "Dados resetados!")

        
    def btnSalvarDados(self):
        agora = datetime.now()
        arquivo = "eletromiografia " + agora.strftime("%m%d%Y-%H %M %S") + ".csv"

        df = pd.DataFrame({'Tesao': self.dadoscsvY, 'Tempo': self.dadoscsvX})
        df.to_csv(arquivo, index=False)

        info = "Arquino salvo com sucesso! \n " + arquivo
        QMessageBox.information(self, "Informação", info)


    def updatePlot(self):
        dados = self.serialComunicacao.serialInst.readline().decode('utf-8').rstrip("\n")
        dadosFloat = float(dados)
        yDado = (dadosFloat * 3.3) / 4095
        self.x += 1
        self.serieGrafico.append(self.x, yDado)
        self.dadoscsvY.append(yDado)
        self.dadoscsvX.append(self.x)
        if self.x == 100:
            self.timer.stop()
            self.ui.btnDeconectar.setDisabled(False)
            self.ui.btnReceber.setDisabled(True)
            self.ui.btnReset.setDisabled(False)
            self.ui.btnSalvar.setDisabled(False)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())