"""
Python module for external functions

WARNING: You must add all the necessary libraries here to make the function work in the main loop.

* This file includes an example with a gain function. It only scales the input with the value set in the parameter
'gain'.
"""

__version__ = "0.0.1"

import numpy as np

# Funcion principal (para la ejecución)
def myFunction(time, inputs, params):
    """
    External function 'myFunction'

    WARNING: This function needs to have the same name as the file/module that contains it, otherwise it won't work.

    :param time: Time value for the main loop.
    :param inputs: Dictionary with all the input values
    :param params: Dictionary with all the necessary parameters for the function
    :type time: float
    :type inputs: dict{numpy.darray}
    :type params: dict{str}
    :return: Dictionary with the output(s) as float or numpy vector
    :rtype: dict{numpy.darray}
    """

    return {0: np.array(params['gain'] * inputs[0])}


# Funcion para inicializar los datos y parámetros necesarios para el bloque
def _init_():
    """
    External function initialization data

    Data and parameters must be set in this function before loading it in the simulator.
    It contains 2 dictionary variables:

    * io_data: Contains the block run_ord parameter, number of inputs and outputs.
    * params: Contains all the required parameters for the function. For this example, it contains 'gain' only.
    """
    io_data = {
        'run_ord': 2,
        'inputs': 1,
        'outputs': 1,
    }
    params = {
        'gain': 1.5
    }
    return io_data, params

# cada archivo tiene 2 funciones, un ejecutable y un inicializador
# el nombre del archivo que sea igual al ejecutable o mejor al del bloque asignado (cambiar cuando se inicializa el nombre de la funcion)

# - el inicializador es unicamente para darle la información al programa de los datos ajustables para el bloque
# -- por ejemplo el nombre, el tipo, el numero de inputs y outputs

# - el ejecutable hace de funcion al momento de correr la simulacion/ejecucion
