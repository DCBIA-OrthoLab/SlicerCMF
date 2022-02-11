# SlicerCMF

SlicerCMF is the dissemination vehicle of powerful dental image analysis methodology based on 3D Slicer open-source software. SlicerCMF supports patient-specific decision making and assessment of the disease progression via registration of serial images.

For more information, see https://cmf.slicer.org/

## Dependencies

SlicerCMF extension depends on other extensions. This means that installing SlicerCMF automatically
install these.

* Click on the _Extension Name_ link to browse the extension GitHub repository and report issues
  specific to that extension.

* Click on the _Quality Assurance Dashboard_ link to learn about the extension
  build, test or packaging status.
  
* *stable* builds are published to the slicer stable release; *preview* builds are published to the preview release.

| Extension Name                   | Quality Assurance Dashboard (CDash)                               |
|----------------------------------|-------------------------------------------------------------------|
| SlicerCMF                        | [stable][cdash-SlicerCMF]    - [preview][cdash-prev-SlicerCMF]    |
| [AnglePlanes][gh-AnglePlanes]    | [stable][cdash-AnglePlanes]  - [preview][cdash-prev-AnglePlanes]  |
| [BoneTexture][gh-BoneTexture]    | [stable][cdash-BoneTexture]  - [preview][cdash-prev-BoneTexture]  |
| [CMFreg][gh-CMFreg]              | [stable][cdash-CMFreg]       - [preview][cdash-prev-CMFreg]       |
| [DatabaseInteractor][gh-DB]      | [stable][cdash-DB]           - [preview][cdash-prev-DB]           |
| [EasyClip][gh-EasyClip]          | [stable][cdash-EasyClip]     - [preview][cdash-prev-EasyClip]     |
| [MeshStatistics][gh-MeshStats]   | [stable][cdash-MeshStats]    - [preview][cdash-prev-MeshStats]    |
| [MeshToLabelMap][gh-M2LM]        | [stable][cdash-M2LM]         - [preview][cdash-prev-M2LM]         |
| [ModelToModelDistance][gh-M2MD]  | [stable][cdash-M2MD]         - [preview][cdash-prev-M2MD]         |
| [PickAndPaint][gh-PickAndPaint]  | [stable][cdash-PickAndPaint] - [preview][cdash-prev-PickAndPaint] |
| [Q3DC][gh-Q3DC]                  | [stable][cdash-Q3DC]         - [preview][cdash-prev-Q3DC]         |
| [SPHARM-PDM][gh-SPHARM-PDM]      | [stable][cdash-SPHARM-PDM]   - [preview][cdash-prev-SPHARM-PDM]   |
| [ShapePopulationViewer][gh-SPV]  | [stable][cdash-SPV]          - [preview][cdash-prev-SPV]          |
| [ShapeVariationAnalyzer][gh-SVA] | [stable][cdash-SVA]          - [preview][cdash-prev-SVA]          |

[gh-AnglePlanes]: https://github.com/DCBIA-OrthoLab/AnglePlanes-Extension
[gh-BoneTexture]: https://github.com/Kitware/BoneTextureExtension
[gh-CMFreg]: https://github.com/DCBIA-OrthoLab/CMFreg
[gh-DB]: https://github.com/DCBIA-OrthoLab/DatabaseInteractorExtension
[gh-EasyClip]: https://github.com/DCBIA-OrthoLab/EasyClip-Extension
[gh-MeshStats]: https://github.com/DCBIA-OrthoLab/MeshStatisticsExtension
[gh-M2LM]: https://github.com/NIRALUser/MeshToLabelMap
[gh-M2MD]: https://github.com/NIRALUser/3DMetricTools
[gh-PickAndPaint]: https://github.com/DCBIA-OrthoLab/PickAndPaintExtension
[gh-Q3DC]: https://github.com/DCBIA-OrthoLab/Q3DCExtension
[gh-SPHARM-PDM]: https://github.com/NIRALUser/SPHARM-PDM
[gh-SPV]: https://github.com/NIRALUser/ShapePopulationViewer
[gh-SVA]: https://github.com/DCBIA-OrthoLab/ShapeVariationAnalyzer

[cdash-SlicerCMF]: http://slicer.cdash.org/index.php?project=SlicerPreview&filtercount=1&showfilters=1&field1=buildname&compare1=63&value1=SlicerCMF
[cdash-AnglePlanes]: http://slicer.cdash.org/index.php?project=SlicerPreview&filtercount=1&showfilters=1&field1=buildname&compare1=63&value1=AnglePlanesExtension
[cdash-BoneTexture]: http://slicer.cdash.org/index.php?project=SlicerPreview&filtercount=1&showfilters=1&field1=buildname&compare1=63&value1=BoneTexture
[cdash-CMFreg]: http://slicer.cdash.org/index.php?project=SlicerPreview&filtercount=1&showfilters=1&field1=buildname&compare1=63&value1=CMFreg
[cdash-DB]: http://slicer.cdash.org/index.php?project=SlicerPreview&filtercount=1&showfilters=1&field1=buildname&compare1=63&value1=DatabaseInteractor
[cdash-EasyClip]: http://slicer.cdash.org/index.php?project=SlicerPreview&filtercount=1&showfilters=1&field1=buildname&compare1=63&value1=EasyClip
[cdash-MeshStats]: http://slicer.cdash.org/index.php?project=SlicerPreview&filtercount=1&showfilters=1&field1=buildname&compare1=63&value1=MeshStatisticsExtension
[cdash-M2LM]: http://slicer.cdash.org/index.php?project=SlicerPreview&filtercount=1&showfilters=1&field1=buildname&compare1=63&value1=MeshToLabelMap
[cdash-M2MD]: http://slicer.cdash.org/index.php?project=SlicerPreview&filtercount=1&showfilters=1&field1=buildname&compare1=63&value1=ModelToModelDistance
[cdash-PickAndPaint]: http://slicer.cdash.org/index.php?project=SlicerPreview&filtercount=1&showfilters=1&field1=buildname&compare1=63&value1=PickAndPaintExtension
[cdash-Q3DC]: http://slicer.cdash.org/index.php?project=SlicerPreview&filtercount=1&showfilters=1&field1=buildname&compare1=63&value1=Q3DC
[cdash-SPHARM-PDM]: http://slicer.cdash.org/index.php?project=SlicerPreview&filtercount=1&showfilters=1&field1=buildname&compare1=63&value1=SPHARM-PDM
[cdash-SPV]: http://slicer.cdash.org/index.php?project=SlicerPreview&filtercount=1&showfilters=1&field1=buildname&compare1=63&value1=ShapePopulationViewer
[cdash-SVA]: http://slicer.cdash.org/index.php?project=SlicerPreview&filtercount=1&showfilters=1&field1=buildname&compare1=63&value1=ShapeVariationAnalyzer

[cdash-prev-SlicerCMF]: http://slicer.cdash.org/index.php?project=SlicerPreview&filtercount=1&showfilters=1&field1=buildname&compare1=63&value1=SlicerCMF
[cdash-prev-AnglePlanes]: http://slicer.cdash.org/index.php?project=SlicerPreview&filtercount=1&showfilters=1&field1=buildname&compare1=63&value1=AnglePlanesExtension
[cdash-prev-BoneTexture]: http://slicer.cdash.org/index.php?project=SlicerPreview&filtercount=1&showfilters=1&field1=buildname&compare1=63&value1=BoneTexture
[cdash-prev-CMFreg]: http://slicer.cdash.org/index.php?project=SlicerPreview&filtercount=1&showfilters=1&field1=buildname&compare1=63&value1=CMFreg
[cdash-prev-DB]: http://slicer.cdash.org/index.php?project=SlicerPreview&filtercount=1&showfilters=1&field1=buildname&compare1=63&value1=DatabaseInteractor
[cdash-prev-EasyClip]: http://slicer.cdash.org/index.php?project=SlicerPreview&filtercount=1&showfilters=1&field1=buildname&compare1=63&value1=EasyClip
[cdash-prev-MeshStats]: http://slicer.cdash.org/index.php?project=SlicerPreview&filtercount=1&showfilters=1&field1=buildname&compare1=63&value1=MeshStatisticsExtension
[cdash-prev-M2LM]: http://slicer.cdash.org/index.php?project=SlicerPreview&filtercount=1&showfilters=1&field1=buildname&compare1=63&value1=MeshToLabelMap
[cdash-prev-M2MD]: http://slicer.cdash.org/index.php?project=SlicerPreview&filtercount=1&showfilters=1&field1=buildname&compare1=63&value1=ModelToModelDistance
[cdash-prev-PickAndPaint]: http://slicer.cdash.org/index.php?project=SlicerPreview&filtercount=1&showfilters=1&field1=buildname&compare1=63&value1=PickAndPaintExtension
[cdash-prev-Q3DC]: http://slicer.cdash.org/index.php?project=SlicerPreview&filtercount=1&showfilters=1&field1=buildname&compare1=63&value1=Q3DC
[cdash-prev-SPHARM-PDM]: http://slicer.cdash.org/index.php?project=SlicerPreview&filtercount=1&showfilters=1&field1=buildname&compare1=63&value1=SPHARM-PDM
[cdash-prev-SPV]: http://slicer.cdash.org/index.php?project=SlicerPreview&filtercount=1&showfilters=1&field1=buildname&compare1=63&value1=ShapePopulationViewer
[cdash-prev-SVA]: http://slicer.cdash.org/index.php?project=SlicerPreview&filtercount=1&showfilters=1&field1=buildname&compare1=63&value1=ShapeVariationAnalyzer
