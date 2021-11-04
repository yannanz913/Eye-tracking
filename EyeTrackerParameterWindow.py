import sys
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QLineEdit, QGridLayout, QApplication
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize, QSettings, QPoint
from PyQt5.QtGui import QIcon, QPixmap


class EyeTrackerParameterWindow(QWidget):

    def __init__(self, parent=None):
        super().__init__()
        self.initUI()
        self.UpdateClicked = False
        self.PupilParams = {"Pupil_dp": 1, "Pupil_minDist": 150, "Pupil_Param1": 12, "Pupil_Param2": 20, "Pupil_minRadius": 40, "Pupil_maxRadius": 58,
                            "Pupil_Threshold": 0}
        self.GlintsParams = {"Glints_minThreshold": 10, "Glints_maxThreshold": 255, "Glints_minArea": 10000,
                             "Glints_minCircularity": 0, "Glints_minConvexity": 0, "Glints_minInertiaRatio": 0}
        self.CamParams = {"Frame_rate": 30, "Brightness": 10, "Contrast": 10,
                             "Saturation": 10, "Hue": 10, "Gain": 10, "Exposure": 10}
        self.SetPupilParams(self.PupilParams)
        self.SetGlintsParams(self.GlintsParams)

    def initUI(self):

        self.setGeometry(800, 800, 850, 800)
        self.setWindowTitle('Input Parameters')

        label0 = QLabel("Image property adjustments:")
        frame_rate = QLabel('Frame_rate')
        brightness = QLabel('Brightness')
        contrast = QLabel('Contrast')
        saturation = QLabel('Saturation')
        hue = QLabel('Hue')
        gain = QLabel('Gain')
        exposure = QLabel('Exposure')
        y = QLabel('y')
        yh = QLabel('y+h')
        x = QLabel('x')
        xw = QLabel('x+w')

        label1 = QLabel("Enter parameters for detecting pupil:")
        dp = QLabel('Pupil_dp')
        minDist = QLabel('Pupil_minDist')
        param1 = QLabel('Pupil_Param1')
        param2 = QLabel('Pupil_Param2')
        minRadius = QLabel('Pupil_minRadius')
        maxRadius = QLabel('Pupil_maxRadius')
        Threshold = QLabel('Pupil_Threshold')

        label2 = QLabel("Enter parameters for detecting glints:")
        minThreshold = QLabel('Glints_minThreshold')
        maxThreshold = QLabel('Glints_maxThreshold')
        minArea = QLabel('Glints_minArea')
        minCircularity = QLabel('Glints_minCircularity')
        minConvexity = QLabel('Glints_minConvexity')
        minInertiaRatio = QLabel('Glints_minInertiaRatio')

        self.dpEdit = QLineEdit()
        self.minDistEdit = QLineEdit()
        self.param1Edit = QLineEdit()
        self.param2Edit = QLineEdit()
        self.minRadiusEdit = QLineEdit()
        self.maxRadiusEdit = QLineEdit()
        self.ThresholdEdit = QLineEdit()
        self.minThresholdEdit = QLineEdit()
        self.maxThresholdEdit = QLineEdit()
        self.minAreaEdit = QLineEdit()
        self.minCircularityEdit = QLineEdit()
        self.minConvexityEdit = QLineEdit()
        self.minInertiaRatioEdit = QLineEdit()
        self.minInertiaRatioEdit = QLineEdit()
        self.frame_rateEdit = QLineEdit()
        self.brightnessEdit = QLineEdit()
        self.contrastEdit = QLineEdit()
        self.exposureEdit = QLineEdit()
        self.saturationEdit = QLineEdit()
        self.hueEdit = QLineEdit()
        self.gainEdit = QLineEdit()
        self.yEdit = QLineEdit()
        self.yhEdit = QLineEdit()
        self.xEdit = QLineEdit()
        self.xwEdit = QLineEdit()



        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(label1, 0, 0)
        grid.addWidget(label2, 0, 2)
        grid.addWidget(label0, 0, 4)

        grid.addWidget(dp, 1, 0)
        grid.addWidget(self.dpEdit, 1, 1)

        grid.addWidget(minDist, 2, 0)
        grid.addWidget(self.minDistEdit, 2, 1)

        grid.addWidget(param1, 3, 0)
        grid.addWidget(self.param1Edit, 3, 1)

        grid.addWidget(param2, 4, 0)
        grid.addWidget(self.param2Edit, 4, 1)

        grid.addWidget(minRadius, 5, 0)
        grid.addWidget(self.minRadiusEdit, 5, 1)

        grid.addWidget(maxRadius, 6, 0)
        grid.addWidget(self.maxRadiusEdit, 6, 1)

        grid.addWidget(Threshold, 7, 0)
        grid.addWidget(self.ThresholdEdit, 7, 1)

        grid.addWidget(minThreshold, 1, 2)
        grid.addWidget(self.minThresholdEdit, 1, 3)

        grid.addWidget(maxThreshold, 2, 2)
        grid.addWidget(self.maxThresholdEdit, 2, 3)

        grid.addWidget(minArea, 3, 2)
        grid.addWidget(self.minAreaEdit, 3, 3)

        grid.addWidget(minCircularity, 4, 2)
        grid.addWidget(self.minCircularityEdit, 4, 3)

        grid.addWidget(minConvexity, 5, 2)
        grid.addWidget(self.minConvexityEdit, 5, 3)

        grid.addWidget(minInertiaRatio, 6, 2)
        grid.addWidget(self.minInertiaRatioEdit, 6, 3)

        grid.addWidget(frame_rate, 1, 4)
        grid.addWidget(self.frame_rateEdit, 1, 5)

        grid.addWidget(brightness, 2, 4)
        grid.addWidget(self.brightnessEdit, 2, 5)

        grid.addWidget(contrast, 3, 4)
        grid.addWidget(self.contrastEdit, 3, 5)

        grid.addWidget(exposure, 4, 4)
        grid.addWidget(self.exposureEdit, 4, 5)

        grid.addWidget(saturation, 5, 4)
        grid.addWidget(self.saturationEdit, 5, 5)

        grid.addWidget(hue, 6, 4)
        grid.addWidget(self.hueEdit, 6, 5)

        grid.addWidget(gain, 7, 4)
        grid.addWidget(self.gainEdit, 7, 5)

        grid.addWidget(y, 8, 4)
        grid.addWidget(self.yEdit, 8, 5)

        grid.addWidget(yh, 9, 4)
        grid.addWidget(self.yhEdit, 9, 5)

        grid.addWidget(x, 10, 4)
        grid.addWidget(self.xEdit, 10, 5)

        grid.addWidget(xw, 11, 4)
        grid.addWidget(self.xwEdit, 11, 5)

        self.pybutton = QPushButton('OK', self)
        grid.addWidget(self.pybutton, 12, 5)
        self.pybutton.clicked.connect(self.clickMethod_ok)

        self.setLayout(grid)

    def clickMethod_ok(self, type):
        global clicked
        if self.pybutton.isEnabled():
            p = self.getparams()
            print(p)
            self.UpdateClicked = True
        else:
            self.UpdateClicked = False

    def getparams(self):
        self.PupilParams = pupilParams = {
            "Pupil_dp": 0,
            "Pupil_minDist": 0,
            "Pupil_Param1": 0,
            "Pupil_Param2": 0,
            "Pupil_minRadius": 0,
            "Pupil_maxRadius": 0,
            "Pupil_Threshold": 0
        }
        pupilParams['Pupil_dp'] = int(self.dpEdit.text())
        pupilParams['Pupil_minDist'] = int(self.minDistEdit.text())
        pupilParams['Pupil_Param1'] = int(self.param1Edit.text());
        pupilParams['Pupil_Param2'] = int(self.param2Edit.text());
        pupilParams['Pupil_minRadius'] = int(self.minRadiusEdit.text());
        pupilParams['Pupil_maxRadius'] = int(self.maxRadiusEdit.text());
        pupilParams['Pupil_Threshold'] = int(self.ThresholdEdit.text());

        self.GlintsParams = glintsParams = {
            "Glints_minThreshold": 0,
            "Glints_maxThreshold": 0,
            "Glints_minArea": 0,
            "Glints_minCircularity": 0,
            "Glints_minConvexity": 0,
            "Glints_minInertiaRatio": 0
        }
        glintsParams['Glints_minThreshold'] = int(self.minThresholdEdit.text());
        glintsParams['Glints_maxThreshold'] = int(self.maxThresholdEdit.text());
        glintsParams['Glints_minArea'] = int(self.minAreaEdit.text());
        glintsParams['Glints_minCircularity'] = int(self.minCircularityEdit.text());
        glintsParams['Glints_minConvexity'] = int(self.minConvexityEdit.text());
        glintsParams['Glints_minInertiaRatio'] = int(self.minInertiaRatioEdit.text());

        # self.CamParams = camParams = {
        #     "Frame_rate": 0,
        #     "Brightness": 0,
        #     "Contrast": 0,
        #     "Saturation": 0,
        #     "Exposure": 0,
        #     "Hue": 0,
        #     "Gain": 0
        # }
        # camParams['Frame_rate'] = int(self.frame_rateEdit.text())
        # camParams['Brightness'] = int(self.brightnessEdit.text())
        # camParams['Contrast'] = int(self.contrastEdit.text())
        # camParams['Saturation'] = int(self.saturationEdit.text())
        # camParams['Exposure'] = int(self.exposureEdit.text())
        # camParams['Hue'] = int(self.hueEdit.text())
        # camParams['Gain'] = int(self.gainEdit.text())
        # camParams['y'] = int(self.yEdit.text())
        # camParams['y+h'] = int(self.yhEdit.text())
        # camParams['x'] = int(self.xEdit.text())
        # camParams['x+w'] = int(self.xwEdit.text())
        return (pupilParams, glintsParams)


    def SetPupilParams(self, pupilParams):
        self.PupilParams['Pupil_dp'] = pupilParams['Pupil_dp']
        self.PupilParams['Pupil_minDist'] = pupilParams['Pupil_minDist']
        self.PupilParams['Pupil_Param1'] = pupilParams['Pupil_Param1'];
        self.PupilParams['Pupil_Param2'] = pupilParams['Pupil_Param2'];
        self.PupilParams['Pupil_minRadius'] = pupilParams['Pupil_minRadius'];
        self.PupilParams['Pupil_maxRadius'] = pupilParams['Pupil_maxRadius'];
        self.PupilParams['Pupil_Threshold'] = pupilParams['Pupil_Threshold'];

        # Set the text boxes to have the parameters specified
        self.dpEdit.setText(str(self.PupilParams['Pupil_dp']))
        self.minDistEdit.setText(str(self.PupilParams['Pupil_minDist']))
        self.param1Edit.setText(str(self.PupilParams['Pupil_Param1']));
        self.param2Edit.setText(str(self.PupilParams['Pupil_Param2']));
        self.minRadiusEdit.setText(str(self.PupilParams['Pupil_minRadius']));
        self.maxRadiusEdit.setText(str(self.PupilParams['Pupil_maxRadius']));
        self.ThresholdEdit.setText(str(self.PupilParams['Pupil_Threshold']));

    def SetGlintsParams(self, glintsParams):
        self.GlintsParams['Glints_minThreshold'] = glintsParams['Glints_minThreshold'];
        self.GlintsParams['Glints_maxThreshold'] = glintsParams['Glints_maxThreshold'];
        self.GlintsParams['Glints_minArea'] = glintsParams['Glints_minArea'];
        self.GlintsParams['Glints_minCircularity'] = glintsParams['Glints_minCircularity'];
        self.GlintsParams['Glints_minConvexity'] = glintsParams['Glints_minConvexity'];
        self.GlintsParams['Glints_minInertiaRatio'] = glintsParams['Glints_minInertiaRatio'];

        self.minThresholdEdit.setText(str(self.GlintsParams['Glints_minThreshold']));
        self.maxThresholdEdit.setText(str(self.GlintsParams['Glints_maxThreshold']));
        self.minAreaEdit.setText(str(self.GlintsParams['Glints_minArea']));
        self.minCircularityEdit.setText(str(self.GlintsParams['Glints_minCircularity']));
        self.minConvexityEdit.setText(str(self.GlintsParams['Glints_minConvexity']));
        self.minInertiaRatioEdit.setText(str(self.GlintsParams['Glints_minInertiaRatio']));

    # def SetCamParams(self, camParams):
    #     self.CamParams['Frame_rate'] = camParams['Frame_rate'];
    #     self.CamParams['Brightness'] = camParams['Brightness'];
    #     self.CamParams['Contrast'] = camParams['Contrast'];
    #     self.CamParams['Saturation'] = camParams['Saturation'];
    #     self.CamParams['Exposure'] = camParams['Exposure'];
    #     self.CamParams['Hue'] = camParams['Hue'];
    #     self.CamParams['Gain'] = camParams['Gain'];
    #     self.CamParams['y'] = camParams['y'];
    #     self.CamParams['y+h'] = camParams['y+h'];
    #     self.CamParams['x'] = camParams['x'];
    #     self.CamParams['x+w'] = camParams['x+w'];
    #
    #     self.frame_rateEdit.setText(str(self.CamParams['Frame_rate']));
    #     self.brightnessEdit.setText(str(self.CamParams['Brightness']));
    #     self.contrastEdit.setText(str(self.CamParams['Contrast']));
    #     self.exposureEdit.setText(str(self.CamParams['Exposure']));
    #     self.saturationEdit.setText(str(self.CamParams['Saturation']));
    #     self.hueEdit.setText(str(self.CamParams['Hue']));
    #     self.gainEdit.setText(str(self.CamParams['Gain']));
    #     self.yEdit.setText(str(self.CamParams['y']));
    #     self.yhEdit.setText(str(self.CamParams['y+h']));
    #     self.xEdit.setText(str(self.CamParams['x']));
    #     self.xwEdit.setText(str(self.CamParams['x+w']));

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = EyeTrackerParameterWindow()
    mainWin.show()
    sys.exit(app.exec_())

    
