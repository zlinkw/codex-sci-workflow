# Venue Canonical Names

Read this file only when auditing `journal`, `booktitle`, `publisher`, `organization`, `institution`, venue aliases, or venue capitalization.

## Selection rules

- Prefer an active template macro when its expansion is correct.
- Otherwise choose the canonical full name or standard abbreviation required by the active bst/biblatex or Typst/CSL style. Keep authoritative full-name metadata when the renderer can reliably generate the required abbreviation; check the rendered output rather than assuming CSL provides an abbreviation dictionary.
- Protect organization acronyms in literal BibTeX values; do not copy brace/escape syntax mechanically into an existing Hayagriva YAML library.
- Preserve historical branding and the exact year-specific proceedings title. The tables define casing and common aliases, not a license to rewrite historical names.
- For unlisted venues, verify the official venue and publisher spelling using the skill's metadata-authority order. Do not guess.

## Conferences

| Acronym | Canonical venue name | Protected BibTeX form | Common aliases or errors |
|---|---|---|---|
| CVPR | IEEE/CVF Conference on Computer Vision and Pattern Recognition | `{IEEE}/{CVF} Conference on Computer Vision and Pattern Recognition` | IEEE CVPR, Conference on Computer Vision and Pattern Recognition |
| ICCV | IEEE/CVF International Conference on Computer Vision | `{IEEE}/{CVF} International Conference on Computer Vision` | IEEE ICCV, International Conference on Computer Vision |
| ECCV | European Conference on Computer Vision | `European Conference on Computer Vision` | European Conf. on Computer Vision |
| WACV | IEEE/CVF Winter Conference on Applications of Computer Vision | `{IEEE}/{CVF} Winter Conference on Applications of Computer Vision` | IEEE WACV, Winter Conference on Applications of Computer Vision |
| ACCV | Asian Conference on Computer Vision | `Asian Conference on Computer Vision` | Asian Conf. on Computer Vision |
| BMVC | British Machine Vision Conference | `British Machine Vision Conference` | British Machine Vision Conf. |
| ICPR | International Conference on Pattern Recognition | `International Conference on Pattern Recognition` | Int. Conf. on Pattern Recognition |
| ICIP | IEEE International Conference on Image Processing | `{IEEE} International Conference on Image Processing` | IEEE ICIP |
| ICASSP | IEEE International Conference on Acoustics, Speech and Signal Processing | `{IEEE} International Conference on Acoustics, Speech and Signal Processing` | IEEE ICASSP |
| NeurIPS | Conference on Neural Information Processing Systems | `Conference on Neural Information Processing Systems` | NIPS, Neural Information Processing Systems; proceedings commonly use `Advances in Neural Information Processing Systems` |
| ICML | International Conference on Machine Learning | `International Conference on Machine Learning` | Int. Conf. on Machine Learning |
| ICLR | International Conference on Learning Representations | `International Conference on Learning Representations` | Int. Conf. on Learning Representations |
| AISTATS | International Conference on Artificial Intelligence and Statistics | `International Conference on Artificial Intelligence and Statistics` | AIStats, Artificial Intelligence and Statistics |
| AAAI | AAAI Conference on Artificial Intelligence | `{AAAI} Conference on Artificial Intelligence` | AAAI Conference, AAAI Conf. on Artificial Intelligence |
| IJCAI | International Joint Conference on Artificial Intelligence | `International Joint Conference on Artificial Intelligence` | Int. Joint Conf. on Artificial Intelligence |
| KDD | ACM SIGKDD Conference on Knowledge Discovery and Data Mining | `{ACM} {SIGKDD} Conference on Knowledge Discovery and Data Mining` | ACM KDD, SIGKDD, Knowledge Discovery and Data Mining |
| UAI | Conference on Uncertainty in Artificial Intelligence | `Conference on Uncertainty in Artificial Intelligence` | Uncertainty in Artificial Intelligence |
| COLT | Conference on Learning Theory | `Conference on Learning Theory` | Computational Learning Theory |
| ACM MM | ACM International Conference on Multimedia | `{ACM} International Conference on Multimedia` | ACM Multimedia, ACM MM |
| MICCAI | International Conference on Medical Image Computing and Computer-Assisted Intervention | `International Conference on Medical Image Computing and Computer-Assisted Intervention` | Medical Image Computing and Computer Assisted Intervention |
| MIDL | Medical Imaging with Deep Learning | `Medical Imaging with Deep Learning` | MIDL Conference |
| ISBI | IEEE International Symposium on Biomedical Imaging | `{IEEE} International Symposium on Biomedical Imaging` | IEEE ISBI |
| IPMI | Information Processing in Medical Imaging | `Information Processing in Medical Imaging` | IPMI Conference |
| IGARSS | IEEE International Geoscience and Remote Sensing Symposium | `{IEEE} International Geoscience and Remote Sensing Symposium` | IEEE IGARSS |

Conference `booktitle` values often include `Proceedings of`, an ordinal, a year, a volume, or a series such as Proceedings of Machine Learning Research. Preserve the official proceedings title required by the entry year and template instead of forcing the generic venue name.

## Journals

| Acronym | Canonical full name | Standard abbreviation | Common aliases or errors |
|---|---|---|---|
| TPAMI | IEEE Transactions on Pattern Analysis and Machine Intelligence | `IEEE Trans. Pattern Anal. Mach. Intell.` | IEEE TPAMI, IEEE Transactions on PAMI |
| IJCV | International Journal of Computer Vision | `Int. J. Comput. Vis.` | Intl. Journal of Computer Vision |
| TIP | IEEE Transactions on Image Processing | `IEEE Trans. Image Process.` | IEEE TIP |
| TNNLS | IEEE Transactions on Neural Networks and Learning Systems | `IEEE Trans. Neural Netw. Learn. Syst.` | IEEE TNNLS |
| TMM | IEEE Transactions on Multimedia | `IEEE Trans. Multimedia` | IEEE T-MM |
| TCSVT | IEEE Transactions on Circuits and Systems for Video Technology | `IEEE Trans. Circuits Syst. Video Technol.` | IEEE TCSVT |
| TMI | IEEE Transactions on Medical Imaging | `IEEE Trans. Med. Imaging` | IEEE TMI |
| JBHI | IEEE Journal of Biomedical and Health Informatics | `IEEE J. Biomed. Health Inform.` | IEEE JBHI |
| TGRS | IEEE Transactions on Geoscience and Remote Sensing | `IEEE Trans. Geosci. Remote Sens.` | IEEE TGRS |
| GRSL | IEEE Geoscience and Remote Sensing Letters | `IEEE Geosci. Remote Sens. Lett.` | IEEE GRSL |
| JSTARS | IEEE Journal of Selected Topics in Applied Earth Observations and Remote Sensing | `IEEE J. Sel. Topics Appl. Earth Observ. Remote Sens.` | IEEE JSTARS |
| GRSM | IEEE Geoscience and Remote Sensing Magazine | `IEEE Geosci. Remote Sens. Mag.` | IEEE GRSM |
| JMLR | Journal of Machine Learning Research | `J. Mach. Learn. Res.` | Journal of ML Research |
| MLJ | Machine Learning | `Mach. Learn.` | Machine Learning Journal |
| PR | Pattern Recognition | `Pattern Recognit.` | Pattern Recognition Journal |
| PRL | Pattern Recognition Letters | `Pattern Recognit. Lett.` | PR Letters |
| CVIU | Computer Vision and Image Understanding | `Comput. Vis. Image Underst.` | Computer Vision & Image Understanding |
| IVC | Image and Vision Computing | `Image Vis. Comput.` | Image & Vision Computing |
| NN | Neural Networks | `Neural Netw.` | Neural Network |
| NEUCOM | Neurocomputing | `Neurocomputing` | Neuro Computing |
| INFFUS | Information Fusion | `Inf. Fusion` | Information Fusion Journal |
| KBS | Knowledge-Based Systems | `Knowl.-Based Syst.` | Knowledge Based Systems |
| ESWA | Expert Systems with Applications | `Expert Syst. Appl.` | Expert Systems and Applications |
| TOMM | ACM Transactions on Multimedia Computing, Communications, and Applications | `ACM Trans. Multimedia Comput. Commun. Appl.` | ACM TOMM, TOMM |
| MedIA | Medical Image Analysis | `Med. Image Anal.` | Medical Imaging Analysis |
| CMIG | Computerized Medical Imaging and Graphics | `Comput. Med. Imaging Graph.` | Computerised Medical Imaging and Graphics |
| IJCARS | International Journal of Computer Assisted Radiology and Surgery | `Int. J. Comput. Assist. Radiol. Surg.` | International Journal of Computer-Aided Radiology and Surgery |
| ISPRS JPRS | ISPRS Journal of Photogrammetry and Remote Sensing | `ISPRS J. Photogramm. Remote Sens.` | ISPRS Journal of Photogrammetry & Remote Sensing |
| RSE | Remote Sensing of Environment | `Remote Sens. Environ.` | Remote Sensing and Environment |
| RS | Remote Sensing | `Remote Sens.` | MDPI Remote Sensing |
| IJRS | International Journal of Remote Sensing | `Int. J. Remote Sens.` | Intl. Journal of Remote Sensing |

For literal full names beginning with an organization, protect the organization token, for example `{IEEE} Transactions on Image Processing`, `{ACM} Transactions on Multimedia Computing, Communications, and Applications`, and `{ISPRS} Journal of Photogrammetry and Remote Sensing`.

## Publishers and organizations

| Canonical form | Common incorrect forms |
|---|---|
| `{IEEE}` | Ieee, IEEE Press when the publisher is only IEEE |
| `{ACM}` | Acm, Association of Computing Machinery |
| `{CVF}` | CvF, Computer Vision Foundation when the template expects CVF |
| `{AAAI} Press` | AAAI press, Aaai Press |
| `{ISPRS}` | Isprs |
| `Springer Nature` | Springer-Nature, Springer nature |
| `Springer` | springer |
| `Elsevier` | ELSEVIER, elsevier |
| `Wiley` | John Wiley when the official entry uses Wiley |
| `Taylor & Francis` | Taylor and Francis, Taylor & francis |
| `SAGE Publications` | Sage, SAGE publishing |
| `MIT Press` | The MIT Press when the template expects MIT Press |
| `PMLR` | Pmlr, Proceedings of Machine Learning Research used as publisher rather than series |
| `MDPI` | Mdpi |

Do not normalize a publisher alias without checking the official entry and the active template. Imprints and historical publisher names may be correct for their publication year.
