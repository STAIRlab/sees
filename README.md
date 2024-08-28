# `sees`

<img align="left" src="https://stairlab.github.io/opensees-gallery/examples/shellframe/ShellFrame.png" width="350px" alt="SEES Logo">


**Highly efficient and portable finite element visualization framework**

<br>


<div style="align:center">

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.13367077.svg)](https://doi.org/10.5281/zenodo.13367077)
[![Latest PyPI version](https://img.shields.io/pypi/v/sees?logo=pypi&style=for-the-badge)](https://pypi.python.org/pypi/sees)

</div>

`sees` is a finite element rendering library that leverages modern 
web technologies to produce sharable, efficient, and detailed renderings.


-------------------------------------------------------------------- 

<br>

`sees` is a finite element rendering library that leverages modern 
web technologies to produce sharable, efficient, and detailed renderings.
Unlike most tools that only provide temporary visualization, `sees` generates
persistent 3D models that can be stored in files, shared with colleagues, and
viewed with any standard 3D model viewer. This means anyone can interact with
the renderings without needing to install specialized software or even Python.
Simply open the 3D object with your computer’s 3D viewer (e.g., 3D Viewer on
Windows) or load it into a free online viewer in like [gltf-viewer](https://gltf-viewer.donmccurdy.com/).

Documentation is currently under development.

## Features

- **Detailed** Render frames with extruded cross sections
- **Persistence**: Save your finite element visualizations as persistent 3D models that can be revisited and analyzed at any time.
- **Portability**: Share your models effortlessly with colleagues, enabling seamless collaboration and review.
- **Accessibility**: View and interact with the models using any standard 3D model viewer, eliminating the need for specialized software or Python installation.
- **Versatility**: A wide selection of rendering backends and output file types, including 
  optimized 3D web formats like `.glb`. Generated 3D models can be loaded directly into programs like PowerPoint and animated.
- Correctly render models that treat both `y` or `z` as the
  vertical coordinate.

-------------------------------------------------------------------- 

## Gallery


|                   |                   |
| :---------------: | :---------------: |
| ![][glry-0001]    | ![][glry-0003]    |
| ![][glry-0002]    | ![][glry-0005]    |


[glry-0001]: <https://stairlab.github.io/opensees-gallery/gallery/cablestayed02/CableStayed02.png>
[view-0001]: <https://stairlab.github.io/opensees-gallery/gallery/cablestayed02/CableStayed02.png>

[glry-0002]: <https://stairlab.github.io/opensees-gallery/examples/example7/safeway_hu11201694704832599949.png>
[view-0002]: <https://stairlab.github.io/opensees-gallery/examples/example7/safeway_hu11201694704832599949.png>

[glry-0003]: <https://stairlab.github.io/opensees-gallery/examples/shellframe/ShellFrame_hu5013315635971397841.png>
[view-0003]: <https://stairlab.github.io/opensees-gallery/examples/shellframe/ShellFrame_hu5013315635971397841.png>

[glry-0005]: <https://raw.githubusercontent.com/STAIRlab/sees/master/docs/figures/shellframe01.png>
[view-0005]: <https://raw.githubusercontent.com/STAIRlab/sees/master/docs/figures/shellframe01.png>

## Getting Started

To install `sees` run:

```shell
pip install sees
```

### Command Line Interface

To create a rendering, execute the following command from the anaconda prompt (after activating the appropriate environment):

```shell
python -m sees model.json -o model.html
```

where `model.json` is a JSON file generated from executing the following OpenSees command:

```tcl
print -JSON model.json
```

If you omit the `-o <file.html>` portion, it will plot immediately in a new
window. You can also use a `.png` extension to save a static image file, as
opposed to the interactive html.

> **Note** Printing depends on the JSON output of a model. Several materials and
> elements in the OpenSeesPy and upstream OpenSees implementations do not
> correctly print to JSON. For the most reliable results, use the
> [`opensees`](https://pypi.org/project/opensees) package.

By default, the rendering treats the $y$ coordinate as vertical.
In order to manually control this behavior, pass the option 
`--vert 3` to render model $z$ vertically, or `--vert 2` to render model $y$ vertically.

If the [`opensees`](https://pypi.org/project/opensees) package is installed,
you can directly render a Tcl script without first printing to JSON, 
by just passing a Tcl script instead of the JSON file:

```shell
python -m sees model.tcl -o model.html
```

To plot an elevation (`elev`) plan (`plan`) or section (`sect`) view, run:

```shell
python -m sees model.json --view elev
```

and add `-o <file.extension>` as appropriate.

To see the help page run

```shell
python -m sees --help
```


<br>



## Related Links

See also

- [`opensees`](https://github.com/claudioperez/opensees)
- [`osmg`](https://pypi.org/project/osmg)
- [`mdof`](https://pypi.org/project/mdof)
- [`sdof`](https://pypi.org/project/sdof)


The `sees` packages was used to generate figures for the following publications:

- *On nonlinear geometric transformations of finite elements* [doi: 10.1002/nme.7506](https://doi.org/10.1002/nme.7506)

<!-- 
Similar packages for OpenSees rendering include:

- [`vfo`](https://vfo.readthedocs.io/en/latest/)
- [`opsvis`](https://opsvis.readthedocs.io/en/latest/index.html)

Other

- [`fapp`](https://github.com/wcfrobert/fapp) 
-->

## Support

<table align="center">
<tr>

  <td>
    <a href="https://peer.berkeley.edu">
    <img src="https://raw.githubusercontent.com/claudioperez/sdof/master/docs/assets/peer-black-300.png"
         alt="PEER Logo" width="200"/>
    </a>
  </td>

  <td>
    <a href="https://dot.ca.gov/">
    <img src="https://raw.githubusercontent.com/claudioperez/sdof/master/docs/assets/Caltrans.svg.png"
         alt="Caltrans Logo" width="200"/>
    </a>
  </td>

  <td>
    <a href="https://brace2.herokuapp.com">
    <img src="https://raw.githubusercontent.com/claudioperez/sdof/master/docs/assets/stairlab.svg"
         alt="STAIRlab Logo" width="200"/>
    </a>
  </td>
 
 </tr>
</table>

