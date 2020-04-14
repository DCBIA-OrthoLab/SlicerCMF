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
<p style="margin: 1%  ">
<a href="#ShapePopulationViewer"><b>ShapePopulationViewer</b></a>: This module allows to interact with multiple 3D surfaces at the same time. It supports visualization and comparison of 3D surfaces by displaying the associated pointwise data (scalar or vector maps) via customizable colormaps.<br><br>
<a href="#BoneTexture"><b>Bone Texture</b></a>: This module allows to interact with multiple 3D surfaces at the same time. It supports visualization and comparison of 3D surfaces by displaying the associated pointwise data (scalar or vector maps) via customizable colormaps.<br><br>
<a href="#SurfaceRegistration"><b>Surface Registration</b></a>: This module performs region based registration<br><br>
<a href="#EasyClip"><b>EasyClip</b></a>: This module is used to clip and close one or several models according to a predetermined plane. Planes can be saved and reused.<br><br>
<a href="#MeshStatistics"><b>MeshStatistics</b></a>: This module computes descriptive statistics (min, max, avg, std, 5th per, 15th per, 15th per, 75th per, 85th per and 99th per) on data fields of a model or models. The statistics can be computed over predefined regions (selected with <a href="#PickAndPaint">PickAndPaint</a>) or the entire model.<br><br>
<a href="#MeshToLabelMap"><b>MeshToLabelMap</b></a>: This module can converts a model into a binary segmentation image volume.<br><br>
<a href="#ModelToModelDistance"><b>ModelToModelDistance</b></a>: This module computes a point by point distance between two models.<br><br>
<a href="#PickAndPaint"><b>PickAndPaint</b></a>: This module selects a region of interest (ROI) in a model or models. The user selects a landmark and a number of vertices to define the size of the ROI, and this information gets propagated to the rest of the models in case of having multiple ones.<br><br>
<a href="#Q3DC"><b>Q3DC</b></a>: This module allows to perform head measurements used in craniofacial surgery (called Quantitative 3D Cephalometrics). Using placed fiducials, the module allows users to compute 2D angles: Yaw, Pitch and Roll; and decompose the 3D distance into the three different components: R-L , A-P and S-I. It is possible to compute the middle point between two fiducials and export the values.<br><br>
</p>
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
