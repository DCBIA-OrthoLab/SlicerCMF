import os
import unittest
import vtk, qt, ctk, slicer
from slicer.ScriptedLoadableModule import *
import logging

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

    text = """
<br>
<u>SlicerCMF modules:</u><br>
<br>
&nbsp;  <a href="#BoneTexture"><b>Bone Texture</b></a><br><br>
&nbsp;  <a href="#SurfaceRegistration"><b>Surface Registration</b></a><br><br>
&nbsp;  <a href="#EasyClip"><b>EasyClip</b></a><br><br>
&nbsp;  <a href="#MeshStatistics"><b>MeshStatistics</b></a><br><br>
&nbsp;  <a href="#MeshToLabelMap"><b>MeshToLabelMap</b></a><br><br>
&nbsp;  <a href="#ModelToModelDistance"><b>ModelToModelDistance</b></a><br><br>
&nbsp;  <a href="#PickAndPaint"><b>PickAndPaint</b></a><br><br>
&nbsp;  <a href="#Q3DC"><b>Q3DC</b></a><br><br>
    """

    modulesTextBrowser = qt.QTextBrowser()
    modulesTextBrowser.setHtml(text)
    modulesTextBrowser.setMinimumHeight(400)
    modulesTextBrowser.connect('anchorClicked(QUrl)', self.onAnchorClicked)

    self.modulesTextBrowser = modulesTextBrowser
    self.layout.addWidget(self.modulesTextBrowser)

    # Add vertical spacer
    self.layout.addStretch(1)

  def cleanup(self):
    pass

  def onAnchorClicked(self, url):
      moduleName = url.fragment()
      slicer.util.selectModule(moduleName)
