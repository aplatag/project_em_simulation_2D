# 2D electromagnetic simulator
<div align="justify">
2D Electromagnetic Simulator for GPR Scenarios. This simulator allows for varying the relative permittivity and conductivity of the subsurface. Additionally, cylindrical objects can be added, defined by a coordinate (x, y) indicating the center of the cylinder, as well as their relative permittivity and conductivity. The simulation requires defining the location of the transmission and reception antennas, as well as the frequency of the Ricker pulse. Below is an example image showing all the parameters necessary to configure the GPR scenario.
</div>




<p align="center">
    <img src="https://raw.githubusercontent.com/aplatag/project_em_simulation_2D/main/images/escenario_GPR.png" alt="GPR-scenario" width="500" >
</p>


<div align="justify">
The default spatial discretization in this simulator is 0.01 meters for the "x" and "y" coordinates. The positions of the antennas, cylindrical objects, and the height of the subsurface are specified in terms of points. These points are calculated as follows: if the transmission antenna is to be positioned at 0.10 meters on the "x" axis and 0.5 meters on the "y" axis, this corresponds to 10 points and 50 points, respectively. This is obtained by dividing 0.10 by 0.01, resulting in 10, and 0.5 by 0.01, resulting in 50.
</div>


## Table of Contents

- [Glossary](#Glossary)
- [Installation](#installation)
- [Code Example](#code-example)
- [Create the environment](#Create-the-environment)


## Glossary
* $Dm$ = model_size_y
* $Ws$ = model_size_x
* $Ds$ = subsurface_height
* $Rx_{x}$ = RX_antenna_position_x
* $Rx_{y}$ = RX_antenna_position_y
* $Tx_{x}$ = TX_antenna_position_x
* $Tx_{y}$ = TX_antenna_position_y
* $steps$ = steps_antenna
* $\varepsilon_{rs}$ = permittivity_r (subsurface)
* $\varepsilon_{rc}$ = permittivity_r (cylinder)
* $\sigma_{s}$ = conductivity (subsurface)
* $\sigma_{c}$ = conductivity (cylinder)
* $r_{c}$ = radius (cylinder)


## Installation

Instructions on how to install the project. For example:
```bash

pip install em_simulation
```

## Code Example
For instance, the following code can be executed in Google Colab. Simply copy and paste it into a new Colab notebook.
```bash

from em_simulation.create_gpr_image import run_image
from em_simulation.visualization import graph_ez

#--------------------------------------------------------------------------------
# 1) definition of parameters for the simulation
dicc_model ={
      'name_simulation':'test_1.npy',
      'model_size_x' : 100 ,
      'model_size_y': 60,
      'TX_antenna_position_x':10,
      'TX_antenna_position_y':50,
      'RX_antenna_position_x':14,
      'RX_antenna_position_y':50,
}

dicc_simulation = {
      'steps_antenna': 60,
      'time_window': 420,
      'frecuency': 1.6e9,

}


characteristics_subsurface= { 
'permittivity_r': 5,
'conductivity': 0.005, #mS/m
'subsurface_height': 50
}

characteristics_cylinder= { 'x_position': 50,
'y_position': 35,
'conductivity': 5.81e7, #cu
'permittivity_r': 1,
'radius': 3
}

#--------------------------------------------------------------------------------
# 2) Perform simulation:
ez = run_image(dicc_model,dicc_simulation,characteristics_subsurface,characteristics_cylinder )
#--------------------------------------------------------------------------------
# 3) show result:
graph_ez(electric_field_Z)

```
## Create the environment
Create a local environment using Anaconda from an environment.yml file.

```bash
conda env create -f environment.yml
```

