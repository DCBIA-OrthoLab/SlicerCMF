cmake_minimum_required(VERSION 3.13.4)

project(SlicerCMF)

#-----------------------------------------------------------------------------
# Extension meta-information
set(EXTENSION_HOMEPAGE "https://cmf.slicer.org/")
set(EXTENSION_CATEGORY "SlicerCMF")
set(EXTENSION_CONTRIBUTORS "Lucia Cevidanes (University of Michigan), Beatriz Paniagua (Kitware), Jean-Christophe Fillion-Robin (Kitware)")
set(EXTENSION_DESCRIPTION "SlicerCMF is a 3D Slicer extension providing registration, segmentation and quantification modules for dental images analysis that may support patient-specific decision making and assessment in the context of disease progression.")
set(EXTENSION_ICONURL "https://raw.githubusercontent.com/DCBIA-OrthoLab/SlicerCMF/master/SlicerCMF.png")
set(EXTENSION_SCREENSHOTURLS "https://raw.githubusercontent.com/slicercmf/slicercmf.github.io/master/images/slicercmf-angles-between-craniofacial-structures.png")
set(EXTENSION_DEPENDS
  AnglePlanesExtension
  BoneTextureExtension
  CMFreg
  DatabaseInteractor
  EasyClip
  MeshStatisticsExtension
  MeshToLabelMap
  ModelToModelDistance
  PickAndPaintExtension
  Q3DC
  SPHARM-PDM
  ShapePopulationViewer
  ShapeVariationAnalyzer
  ) # Specified as a list or 'NA' if any
set(EXTENSION_BUILD_SUBDIRECTORY inner-build)

set(SUPERBUILD_TOPLEVEL_PROJECT inner)

# Not available as extension:
#  GROUPS
#  MFSDA_Python

#-----------------------------------------------------------------------------
# Extension dependencies
find_package(Slicer REQUIRED)
include(${Slicer_USE_FILE})
mark_as_superbuild(Slicer_DIR)

find_package(Git REQUIRED)
mark_as_superbuild(GIT_EXECUTABLE)

#-----------------------------------------------------------------------------
# SuperBuild setup
option(${EXTENSION_NAME}_SUPERBUILD "Build ${EXTENSION_NAME} and the projects it depends on." ON)
mark_as_advanced(${EXTENSION_NAME}_SUPERBUILD)
if(${EXTENSION_NAME}_SUPERBUILD)
  include("${CMAKE_CURRENT_SOURCE_DIR}/SuperBuild.cmake")
  return()
endif()

#-----------------------------------------------------------------------------
# Extension modules
add_subdirectory(SlicerCMF)
## NEXT_MODULE

#-----------------------------------------------------------------------------
set(EXTENSION_CPACK_INSTALL_CMAKE_PROJECTS)
#list(APPEND EXTENSION_CPACK_INSTALL_CMAKE_PROJECTS "${Foo_DIR};Foo;RuntimeLibraries;/")
set(${EXTENSION_NAME}_CPACK_INSTALL_CMAKE_PROJECTS "${EXTENSION_CPACK_INSTALL_CMAKE_PROJECTS}" CACHE STRING "List of external projects to install" FORCE)

#-----------------------------------------------------------------------------
list(APPEND CPACK_INSTALL_CMAKE_PROJECTS "${CMAKE_BINARY_DIR};${EXTENSION_NAME};ALL;/")
list(APPEND CPACK_INSTALL_CMAKE_PROJECTS "${${EXTENSION_NAME}_CPACK_INSTALL_CMAKE_PROJECTS}")
include(${Slicer_EXTENSION_GENERATE_CONFIG})
include(${Slicer_EXTENSION_CPACK})
