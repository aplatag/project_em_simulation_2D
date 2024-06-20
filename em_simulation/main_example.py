"""
the entire code of the electromagnetic propagator is executed
"""
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


import create_gpr_image as create_gpr
import visualization as vis
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++



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


caracteristicas_sub = { 
'permittivity_r': 5,
'conductivity': 0.005, #mS/m
'subsurface_height': 50
}

caracteristicas_cil= { 'x_position': 50,
'y_position': 35,
'conductivity': 5.81e7, #cu
'permittivity_r': 1,
'radius': 3
}


# main:

ez = create_gpr.run_image(dicc_model,dicc_simulation,caracteristicas_sub,caracteristicas_cil  )

vis.graph_ez(ez)