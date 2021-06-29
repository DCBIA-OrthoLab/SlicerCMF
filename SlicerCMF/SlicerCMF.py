import os

import qt
import slicer
from slicer.ScriptedLoadableModule import *


#
# SlicerCMF
#

class SlicerCMF(ScriptedLoadableModule):
  """Uses ScriptedLoadableModule base class, available at:
  https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/ScriptedLoadableModule.py
  """

  def __init__(self, parent):
    ScriptedLoadableModule.__init__(self, parent)
    self.parent.title = "SlicerCMF" # TODO make this more human readable by adding spaces
    self.parent.categories = ["SlicerCMF"]
    self.parent.dependencies = []
    self.parent.contributors = ["Jean-Christophe Fillion-Robin (Kitware)"] # replace with "Firstname Lastname (Organization)"
    self.parent.helpText = """
Dental image analysis to support patient-specific decision making and assessment of the disease progression via registration of serial images.
"""
    self.parent.helpText += self.getDefaultModuleDocumentationLink()
    self.parent.acknowledgementText = """
This file was originally developed by Jean-Christophe Fillion-Robin, Kitware Inc.
and was partially funded by NIH grant R01-DE024450-01A1.
""" # replace with organization, grant and thanks.

#
# SlicerCMFWidget
#

class SlicerCMFWidget(ScriptedLoadableModuleWidget):
  """Uses ScriptedLoadableModuleWidget base class, available at:
  https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/ScriptedLoadableModule.py
  """

  def setup(self):
    ScriptedLoadableModuleWidget.setup(self)

    # Instantiate and connect widgets ...

    indexPath = self.resourcePath('HTML/SlicerCMF/index.html')
    url = qt.QUrl.fromLocalFile(indexPath)

    modulesTextBrowser = qt.QTextBrowser()
    modulesTextBrowser.setSource(url)
    modulesTextBrowser.connect('anchorClicked(QUrl)', self.onAnchorClicked)

    sp = qt.QSizePolicy()
    sp.setVerticalPolicy(qt.QSizePolicy.Expanding)
    sp.setHorizontalPolicy(qt.QSizePolicy.Expanding)
    sp.setVerticalStretch(1)
    sp.setHorizontalStretch(1)

    modulesTextBrowser.setSizePolicy(sp)

    self.modulesTextBrowser = modulesTextBrowser
    self.layout.addWidget(self.modulesTextBrowser)

  def cleanup(self):
    pass

  def onAnchorClicked(self, url):
      moduleName = url.fragment()
      slicer.util.selectModule(moduleName)

  def resourcePath(self, filename):
    scriptedModulesPath = os.path.dirname(slicer.util.modulePath(self.moduleName))
    return os.path.join(scriptedModulesPath, 'Resources', filename)
