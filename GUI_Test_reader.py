import glob

from PyQt5.QtCore import Qt
import gui3
import sys
import os
import serial
import numpy as np
import matplotlib.pyplot as plt
from pyqtgraph.opengl import GLViewWidget, GLGridItem
from matplotlib import cm
from matplotlib.backends.backend_qt5agg import (NavigationToolbar2QT as NavigationToolbar)
from matplotlib.ticker import LinearLocator
import matlab.engine
import time

from PyQt5 import QtCore, QtGui, QtWidgets

from reader_main import show_return_message


class GUI(QtWidgets.QMainWindow, gui3.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.Start_Button.clicked.connect(self.startbutton)
        self.Plot_Button.clicked.connect(self.plot_button)
        self.Clear_Button.clicked.connect(self.clear)

    def startbutton(self):
        k = str(self.combo_Selection.currentText())
        if k == "Ping":
            self.exec_Ping()
        elif k == "RSSI":
            self.exec_Rssi()
        elif k == "Mittelwert":
            self.mean()
        elif k == "Abstand":
            self.abstand()
        elif k == "Kathrein Reader":
            self.startButton()
        elif k == "Kathrein 2":
            self.kathrein()

    def plot_button(self):
        self.check_delete()
        filename = self.Text_Eingabe.text()
        print(str(len(filename)))
        if len(filename) > 0:
            text_file = open(str(filename) + ".txt", "r")
            f = open(str(filename) + ".txt", "r")
            #y = np.loadtxt(str(filename) + ".txt", delimiter=",")
            #z = np.arange(0, len(y), 1)

            voltage = []
            distance = []
            distance2 = []
            for row in f:
                row = row.split(',')
                voltage.append(row[0])
                distance.append(int(row[1]))
                distance2.append(int(row[2]))

            v = np.array(voltage, dtype=np.float32)
            r = np.array(distance, dtype=np.float32)
            d = np.array(distance2, dtype=np.float32)
            text_file.close()

            self.graphWidget.setLabel('left', 'Voltage', units='V')
            self.graphWidget.setLabel('bottom', 'Distance', units='m')
            self.graphWidget.plot(r, v, pen='b', symbol='x', symbolPen='b', symbolBrush=0.2, name='red')
        else:
            self.print_Box("Bitte Dateiname eingeben")


       # fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        surf = ax.scatter(r, d, v, c='r', marker='o')
        ax.set_xlabel('X Label')
        ax.set_ylabel('Y Label')
        ax.set_zlabel('Z Label')
        X = r
        Y = d
        X, Y = np.meshgrid(X, Y)
        fig.colorbar(surf, shrink=0.5, aspect=5)
        plt.show()
        self.MplWidget.canvas.axes.clear()
        self.MplWidget.canvas.axes.scatter(r, d, v)
        self.MplWidget.canvas.axes.set_title('Scatter Diagramm der Spannungen')
        self.MplWidget.canvas.axes.set_xlabel( 'Y Label')
        self.MplWidget.canvas.axes.set_ylabel( 'X Label')
        self.MplWidget.canvas.axes.set_zlabel( 'V Label')
        self.MplWidget.canvas.draw()


    def clear(self):
        self.textBrowser.clear()

    def exec_Ping(self):
        com = self.portselect(self)
        ser = serial.Serial(com, 38400, bytesize=8, parity='N', stopbits=1, timeout=None, xonxoff=0, rtscts=1)
        n = bytearray([10, 1, 44])  # 44 ist Ping
        ser.write(n)
        s = ser.read(10)
        k = str(s[0])
        p = str(s[1])
        text1 = "The length is " + k
        self.print_Box(text1)
        text2 = "The ID is " + p
        self.print_Box(text2)
        text3 = str(s)
        self.print_Box(text3)
        print(text2)
        print(text3)
        ser.close()  # close port

        a = self.checkBox.isChecked()
        b = str(a)
        if b == "True":
            filename = self.Text_Eingabe_2.text()
            text_file = open(str(filename) + ".txt", "a")
            text_file.write(text3 + ", \n")
            text_file.close()
        elif b == "False":
            print("Box ist nicht getickt")

    def exec_Rssi(self):
        m = self.spinBox_nSelection.value()  # Anzahl der Durchläufe
        j = self.spinBox_ID.value()  # ID
        t = self.spinBox_Time.value()  # ID

        com = self.portselect(self)

        for j in range(1, j + 1):  # j+1 Python würde sonst nur bis <j zählen
            ser = serial.Serial(com, 38400, bytesize=8, parity='N', stopbits=1, timeout=None, xonxoff=0, rtscts=1)

            n = bytearray([10, j, 33, m, t])
            ser.write(n)
            # wait auf PC Antwort
            s = ser.read(10)
            if s[3] == 1:  # Prüfen auf VZ
                mw = -s[2]
            else:
                mw = s[2]

            k = str(s[0])
            p = str(s[1])
            z = str(mw)
            text1 = "The length is " + k
            self.print_Box(text1)
            text2 = "The ID is " + p
            self.print_Box(text2)
            text3 = "Der RSSI ist " + z
            self.print_Box(text3)

            print("The length is " + k)
            print("The ID is " + p)
            print("Der RSSI ist " + z)
            ser.close()

            a = self.checkBox.isChecked()
            b = str(a)
            if b == "True":
                filename = self.Text_Eingabe_2.text()
                text_file = open(str(filename) + ".txt", "a")
                text_file.write(text3 + ", \n")
                text_file.close()
            elif b == "False":
                print("Box ist nicht getickt")

    def abstand(self):
        m = self.spinBox_nSelection.value()  # Anzahl der Durchläufe
        j = self.spinBox_ID.value()  # ID
        t = self.spinBox_Time.value()  # Zeit
        o = self.spinBox_Leistung_dBm.value()  # Leistung Kathrein Reader
        q = int(o)
        print(o)

        eng, obj = self.rfid_reader_init(0, q)  # mode [0, 1], power [dBm]

        rssi_offset = self.selectionOffsetRssi(self)
        voltage_offset = self.selectionOffsetVoltage(self)
        com = self.portselect(self)

        for j in range(1, j + 1):  # j+1 Python würde sonst nur bis <j zählen
            ser = serial.Serial(com, 38400, bytesize=8, parity='N', stopbits=1, timeout=None, xonxoff=0, rtscts=1)
            n = bytearray([10, j, 22, m, j, t])  # 102 = 60 s
            ser.write(n)

            # wait auf PC Antwort
            t_end = time.time() + t
            while time.time() < t_end:
                for i in range(0, 100):
                    self.rfid_scan4tags(eng, obj)
            k = self.rfid_scan4tags(eng, obj)

            self.rfid_reader_engine_disconnect(eng, obj)

            s = ser.read(10)  # liest von USB

            kon = s[2] - 69 - rssi_offset
            u = s[3] * 10 + s[4] * 0.1 + s[5] * 0.001 + voltage_offset
            format_float = "{:.3f}".format(u)
            U = str(format_float)
            self.print_Box("Der RSSI ist " + str(kon))
            self.print_Box("Die Spannung ist " + U)
            ser.close()
            P = (u / 17.2) - 69
            print(str(P))
            a = self.checkBox.isChecked()
            b = str(a)
            if b == "True":
                filename = self.Text_Eingabe_2.text()
                r = self.Text_Eingabe_3.text()
                text_file = open(str(filename) + ".txt", "a")
                text_file.write(U + ", " + r + '\n')
                text_file.close()
            elif b == "False":
                print("Box ist nicht getickt")

            if k == 0.0 or k == 10.0:
                self.print_Box('Keine Tags gefunden')
            else:
                tag_count = str(k).split(',')[1].replace('[', '').replace(']', '')
                self.print_Box('Es wurden ' + tag_count.split('.')[0] + " Tags gefunden")

    def kathrein(self):
        m = self.spinBox_nSelection.value()  # Anzahl der Durchläufe
        j = self.spinBox_ID.value()  # ID
        t = self.spinBox_Time.value()  # Zeit
        o = self.spinBox_Leistung_dBm.value()  # Leistung Kathrein Reader
        q = int(o)

        eng, obj = self.rfid_reader_init(0, q)  # mode [0, 1], power [dBm]

        rssi_offset = self.selectionOffsetRssi(self)
        voltage_offset = self.selectionOffsetVoltage(self)
        com = self.portselect(self)

        for j in range(1, j + 1):  # j+1 Python würde sonst nur bis <j zählen
            ser = serial.Serial(com, 38400, bytesize=8, parity='N', stopbits=1, timeout=None, xonxoff=0, rtscts=1)
            n = bytearray([10, j, 22, m, j, t])  # 102 = 60 s
            ser.write(n)

            t_end = time.time() + t  # in s
            while time.time() < t_end:
                for i in range(0, 100):  # alle 10 ms
                    self.rfid_scan4tags(eng, obj)
            k = self.rfid_scan4tags(eng, obj)

            self.rfid_reader_engine_disconnect(eng, obj)

            s = ser.read(10)  # liest von USB

            kon = s[2] - 69 - rssi_offset
            u = s[3] * 10 + s[4] * 0.1 + s[5] * 0.001 + voltage_offset
            format_float = "{:.3f}".format(u)
            U = str(format_float)
            self.print_Box("The length is " + str(s[0]))
            self.print_Box("The ID is " + str(s[1]))
            self.print_Box("Der RSSI ist " + str(kon))
            self.print_Box("Der RSSI ist " + str(s[3]) + "." + str(s[4]))
            self.print_Box("Die Spannung ist " + U)
            ser.close()
            print(U)
            P = (u / 17.2) - 69
            print(str(P))
            a = self.checkBox.isChecked()
            b = str(a)
            if b == "True":
                filename = self.Text_Eingabe_2.text()
                text_file = open(str(filename) + ".txt", "a")
                text_file.write(U + ", ")
                text_file.close()
            elif b == "False":
                print("Box ist nicht getickt")

            if k == 0.0 or k == 10.0:
                self.print_Box('Keine Tags gefunden')
            else:
                tag_count = str(k).split(',')[1].replace('[', '').replace(']', '')
                self.print_Box('Es wurden ' + tag_count.split('.')[0] + " Tags gefunden")

    def mean(self):
        m = self.spinBox_nSelection.value()  # Anzahl der Durchläufe
        j = self.spinBox_ID.value()  # ID
        t = self.spinBox_Time.value()  # Zeit
        o = self.spinBox_Leistung_dBm.value()  # Leistung Kathrein Reader
        q = int(o)
        print(o)

        rssi_offset = self.selectionOffsetRssi(self)
        voltage_offset = self.selectionOffsetVoltage(self)
        com = self.portselect(self)

        for j in range(1, j + 1):  # j+1 Python würde sonst nur bis <j zählen
            ser = serial.Serial(com, 38400, bytesize=8, parity='N', stopbits=1, timeout=None, xonxoff=0, rtscts=1)
            n = bytearray([10, j, 22, m, j, t])  # 102 = 60 s
            ser.write(n)
            time.sleep(t + 2)
            # wait auf PC Antwort

            s = ser.read(10)
            kon = s[2] - 69 - rssi_offset
            u = s[3] * 10 + s[4] * 0.1 + s[5] * 0.001 + voltage_offset
            format_float = "{:.3f}".format(u)
            U = str(format_float)
            self.print_Box("The length is " + str(s[0]))
            self.print_Box("The ID is " + str(s[1]))
            self.print_Box("Der RSSI ist " + str(kon))
            self.print_Box("Der RSSI ist " + str(s[3]) + "." + str(s[4]))
            self.print_Box("Die Spannung ist " + U)
            ser.close()
            print(U)
            P = (u / 17.2) - 69
            print(str(P))
            a = self.checkBox.isChecked()
            b = str(a)
            if b == "True":
                filename = self.Text_Eingabe_2.text()
                text_file = open(str(filename) + ".txt", "a")
                text_file.write(U + ", ")
                text_file.close()
            elif b == "False":
                print("Box ist nicht getickt")

    def plot(self, x, y):
        self.graphWidget.plot(x, y)

    def savebutton(self):
        a = self.checkBox.isChecked()
        b = str(a)
        if b == "True":
            filename = self.Text_Eingabe_2.text()
            text_file = open(str(filename) + ".txt", "a")
            text_file.write("Hallo World\n")
            text_file.close()
        elif b == "False":
            self.print_Box("Box ist nicht getickt")

    def print_Box(self, text):
        self.textBrowser.append(text)  # Display prompt information in the specified area
        self.cursot = self.textBrowser.textCursor()
        self.textBrowser.moveCursor(self.cursot.End)

    def save_box_check(self):
        a = self.checkBox.isChecked()
        b = str(a)
        if b == "True":
            filename = self.Text_Eingabe_2.text()
            text_file = open(str(filename) + ".txt", "a")
        elif b == "False":
            print("Box ist nicht getickt")

    def selectionOffsetRssi(self, rssi_offset):
        k = str(self.combo_Selection_2.currentText())
        if k == "SMA":
            rssi_offset = 0
        elif k == "Antenne 1":
            rssi_offset = -10
        elif k == "Monopol":
            rssi_offset = -10
        elif k == "Dipol":
            rssi_offset = -10
        return rssi_offset

    def selectionOffsetVoltage(self, voltage_offset):
        k = str(self.combo_Selection_2.currentText())
        if k == "SMA":
            voltage_offset = 0
        elif k == "Antenne 1":
            voltage_offset = -100
        elif k == "Monopol":
            voltage_offset = -0.32
        elif k == "Dipol":
            voltage_offset = -100
        return voltage_offset

    def gain_receive_antenna(self, gr):
        k = str(self.combo_Selection_2.currentText())
        if k == "SMA":
            gr = 0
        elif k == "Antenne 1":
            gr = 6.5
        elif k == "Monopol":
            gr = 4.5
        elif k == "Dipol":
            gr = 2.15
        return gr

    def gain_selection(self, gain):
        k = str(self.combo_Selection_3.currentText())
        if k == "Monopol":
            gain = 4.5
        elif k == "Dipol 1":
            gain = 2.15
        elif k == "Zirkular Polarisiert":
            gain = 8
        elif k == "Antenne 1":
            gain = 6.5
        return gain

    def check_delete(self):  # letzes Komma in txt file löschen um dann die Daten einlesen zu können
        filename = self.Text_Eingabe.text()
        with open(filename + ".txt", 'rb+') as filehandle:
            # filehandle.seek(0, os.SEEK_END)
            filehandle.seek(-2, os.SEEK_END)
            k = filehandle.read()
            filehandle.seek(-1, os.SEEK_END)
            p = filehandle.read()
            print(type(str(k)))
            print(k)
            print(p)

            if k == b' ' and p == b',':
                i = 1
                while i < 2:
                    filehandle.seek(-1, os.SEEK_END)
                    filehandle.truncate()

            elif k == b' ' or p == b',':
                filehandle.seek(-1, os.SEEK_END)
                filehandle.truncate()

            elif k == b',' or p == b' ':
                filehandle.seek(-1, os.SEEK_END)
                filehandle.truncate()

    def serial_ports(self, result):
        """ Lists serial port names

            :raises EnvironmentError:
                On unsupported or unknown platforms
            :returns:
                A list of the serial ports available on the system
        """
        if sys.platform.startswith('win'):
            ports = ['COM%s' % (i + 1) for i in range(256)]
        elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
            # this excludes your current terminal "/dev/tty"
            ports = glob.glob('/dev/tty[A-Za-z]*')
        elif sys.platform.startswith('darwin'):
            ports = glob.glob('/dev/tty.*')
        else:
            raise EnvironmentError('Unsupported platform')

        result = []
        for port in ports:
            try:
                s = serial.Serial(port)
                s.close()
                result.append(port)
            except (OSError, serial.SerialException):
                pass
            # print(result)
        return result

    def portselect(self, com):
        port = self.serial_ports(self)
        for i in range(0, len(port)):
            if len(port) == 1 and port == 'COM1':
                print("Fehler! Kein USB angeschlossen oder prüfe ob wirklich das Port 1 verwendet wurde")
            elif port[
                i] != 'COM1':  # Lehrstuhl PC zeigt immer auch Port 1 automatisch an, auch wenn nichts angeschlossen ist
                com = str(port[i])
        return com

    def show_return_message(self, flag):
        """
        Translate result flag into text message
        :param flag: returned flag to be matched with respective message
        :return:
        """
        try:
            flag_int = int(flag)
        except Exception:
            return
        result_flag_dict = {0: 'NoError',
                            1: 'NoData',
                            2: 'CRCError',
                            3: 'NoLicense',
                            4: 'OutOfRange',
                            5: 'NoStandard',
                            6: 'NoAntenna',
                            7: 'NoFrequency',
                            8: 'NoCarrier',
                            9: 'AntennaError',
                            10: 'NoTag',
                            11: 'MoreThanOneTagInField',
                            12: 'WrongLicenseKey',
                            13: 'FWRejected',
                            14: 'WrongCFM',
                            15: 'NoHandle',
                            16: 'NoProfile',
                            128: 'NonSpecified'}
        print('reader message: ' + result_flag_dict[int(flag_int)] + ' [' + str(int(flag_int)) + ']')

    def rfid_reader_init(self, mode, power):
        """
        This function starts up the matlab engine and initializes the reader
        :param mode: mode [0, 1] NormalMode = 0 (required for EPC scan) / DirectMode = 1 (for direct carrier)
        :param power: power per port in dBm
        :return obj: returns the handler instance
        """
        eng = matlab.engine.start_matlab()
        obj = eng.reader_init(mode, power)  # mode [0, 1], power in dBm
        return eng, obj

    def rfid_reader_start(self, eng, obj):
        """
        Start to emit the carrier
        :param eng: engine handler
        :param obj: instance
        :return:
        """
        result_flag = eng.reader_on(obj)
        show_return_message(result_flag)

    def rfid_reader_stop(self, eng, obj):
        """
        Deactivate the carrier
        :param eng: engine handler
        :param obj: instance
        :return:
        """
        result_flag = eng.reader_off(obj)
        show_return_message(result_flag)

    def rfid_reader_engine_disconnect(self, eng, obj):
        """
        Disconnect the reader and close matlab engine
        :param eng: engine handler
        :param obj: instance
        :return:
        """
        stat = eng.reader_disconnect(obj)
        print(stat)
        eng.quit()

    def rfid_scan4tags(self, eng, obj):
        """
        Scans for available RFID-tags (found tags are saved into txt-file)
        :param eng: engine handler
        :param obj: instance
        :return:
        """
        result_flag = eng.scan_tags(obj)
        show_return_message(result_flag)
        if result_flag == 0.0 or result_flag == 10.0:
            print('Scan4Tags: no tags found.')

        else:
            tag_count = str(result_flag).split(',')[1].replace('[', '').replace(']', '')
            print('Scan4Tags: ' + tag_count.split('.')[0] + ' tags found!')

        return result_flag

    def startButton(self):
        eng, obj = self.rfid_reader_init(0, 22)  # mode [0, 1], power [dBm]
        t_end = time.time() + 15
        while time.time() < t_end:
            self.rfid_scan4tags(eng, obj)
        self.rfid_reader_engine_disconnect(eng, obj)

    def keyPressEvent(self, event):
        key = event.key()
        if key == Qt.Key_Escape:  # exit app
            self.close()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    GUI_OBJECT = GUI()
    GUI_OBJECT.show()
    sys.exit(app.exec_())
