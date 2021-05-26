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
#  MFSDA_Python

#-----------------------------------------------------------------------------
# Extension dependencies
find_package(Slicer REQUIRED)
include(${Slicer_USE_FILE})
mark_as_superbuild(Slicer_DIR)

find_package(Git REQUIRED)
mark_as_superbuild(GIT_EXECUTABLE)

#-----------------------------------------------------------------------------
# Add remote extension source directories
include(FetchContent)

# GROUPS
set(extension_name "GROUPS")
set(${extension_name}_SOURCE_DIR "${CMAKE_BINARY_DIR}/${extension_name}")
FetchContent_Populate(${extension_name}
  SOURCE_DIR     ${${extension_name}_SOURCE_DIR}
  GIT_REPOSITORY ${EP_GIT_PROTOCOL}://github.com/NIRALUser/GROUPS.git
  GIT_TAG        b2bd6008416711a133fd30182f1c4a49bd0bdc46
  GIT_PROGRESS   1
  QUIET
  )
list(APPEND Slicer_EXTENSION_SOURCE_DIRS ${${extension_name}_SOURCE_DIR})

# Add CMake directory to ensure FindFortran.cmake required by External_LAPACK.cmake is fetched
add_subdirectory(${${extension_name}_SOURCE_DIR}/CMake ${CMAKE_BINARY_DIR}/GROUPS-CMake-build)
list(INSERT CMAKE_MODULE_PATH 0 "${CMAKE_BINARY_DIR}/GROUPS-CMake-build")

#-----------------------------------------------------------------------------
# SuperBuild setup
option(${EXTENSION_NAME}_SUPERBUILD "Build ${EXTENSION_NAME} and the projects it depends on." ON)
mark_as_advanced(${EXTENSION_NAME}_SUPERBUILD)
if(${EXTENSION_NAME}_SUPERBUILD)
  include("${CMAKE_CURRENT_SOURCE_DIR}/SuperBuild.cmake")
  return()
endif()

# --------------------------------------------------------------------------
# Bundle extensions adding source directories.
# --------------------------------------------------------------------------

#
# Support for bundling "SuperBuild-type" extension:
#
# * An extension is considered to be of type "SuperBuild" if a directory
#   "<extension_dir>/SuperBuild" or "<extension_dir>/Superbuild" exists.
#   Corresponding directory is appended to EXTERNAL_PROJECT_ADDITIONAL_DIRS.
#
# * If variable "<extension_name>_EXTERNAL_PROJECT_EXCLUDE_ALL" is set to TRUE, corresponding SuperBuild directory
#   is not appended to EXTERNAL_PROJECT_ADDITIONAL_DIRS.
#
# * Associated external projects are globbed using expression of the form
#   "<extension_dir>/(SuperBuild|Superbuild)/External_*.cmake".
#
# * List of external project names is extracted from the "External_<projectName>.cmake"
#   files and appended to Slicer_DEPENDENCIES. This ensures they are build before Slicer inner build.
#   Setting variable "<extension_name>_EXTERNAL_PROJECT_DEPENDENCIES" to a list of <projectName> allows
#   to override the list of <projectName> appended to Slicer_DEPENDENCIES.
#
# * Variable Slicer_BUNDLED_EXTENSION_NAMES is updated with the names of external project
#   and passed to Slicer inner build. It is then used in SlicerCPack. to package associated
#   external projects if the cache variable <extensionName>_CPACK_INSTALL_CMAKE_PROJECTS
#   was defined in the extension sources.
#
# Corresponding logic is implemented in SuperBuild.cmake
#

function(_add_extension_source_dir extension_source_dir what)
  get_filename_component(extension_source_dir ${extension_source_dir} REALPATH)
  get_filename_component(extension_source_dirname ${extension_source_dir} NAME_WE)
  message(STATUS "--------------------------------------------------")
  message(STATUS "Configuring ${what}: ${extension_source_dirname}")
  set(ExternalData_SOURCE_ROOT ${extension_source_dir})
  set(${extension_source_dirname}_SOURCE_DIR ${extension_source_dir})
  set(${extension_source_dirname}_BINARY_DIR ${extensions_build_dir}/${extension_source_dirname})
  add_subdirectory(
    ${${extension_source_dirname}_SOURCE_DIR}
    ${${extension_source_dirname}_BINARY_DIR}
    )
endfunction()

if(NOT Slicer_SOURCE_DIR)
  foreach(extension_source_dir ${Slicer_EXTENSION_SOURCE_DIRS})
    _add_extension_source_dir(${extension_source_dir} "extension directory")
  endforeach()
endif()

#-----------------------------------------------------------------------------
# Extension modules
add_subdirectory(SlicerCMF)
## NEXT_MODULE

#-----------------------------------------------------------------------------
set(EXTENSION_CPACK_INSTALL_CMAKE_PROJECTS)
if(NOT Slicer_SOURCE_DIR)
  foreach(extension_item IN LISTS Slicer_BUNDLED_EXTENSION_NAMES)
    list(APPEND EXTENSION_CPACK_INSTALL_CMAKE_PROJECTS ${${EXTENSION_NAME}_CPACK_INSTALL_CMAKE_PROJECTS})
  endforeach()
endif()
set(${EXTENSION_NAME}_CPACK_INSTALL_CMAKE_PROJECTS "${EXTENSION_CPACK_INSTALL_CMAKE_PROJECTS}" CACHE STRING "List of external projects to install" FORCE)

#-----------------------------------------------------------------------------
list(APPEND CPACK_INSTALL_CMAKE_PROJECTS "${CMAKE_BINARY_DIR};${EXTENSION_NAME};ALL;/")
list(APPEND CPACK_INSTALL_CMAKE_PROJECTS "${${EXTENSION_NAME}_CPACK_INSTALL_CMAKE_PROJECTS}")
include(${Slicer_EXTENSION_GENERATE_CONFIG})
include(${Slicer_EXTENSION_CPACK})
