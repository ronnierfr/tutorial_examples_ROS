import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
from time import sleep

# New Antecedent/Consequent objects hold universe variables and membership
# functions

#input and output 
distanciaY = ctrl.Antecedent(np.arange(-10, 10, 0.005), 'distanciaY')
vAngular   = ctrl.Consequent(np.arange(-2, 2, 0.005), 'vAngular')



# Custom membership functions can be built interactively with a familiar,
# Pythonic API
distanciaY['ME'] = fuzz.trapmf(distanciaY.universe, [-10, -10,-3.0,-1.5 ]) #trapezoidal
distanciaY['E']  = fuzz.trimf(distanciaY.universe, [-3.0, -1.5, 0])
distanciaY['R']  = fuzz.trimf(distanciaY.universe, [-1.5, 0, 1.5])
distanciaY['D']  = fuzz.trimf(distanciaY.universe, [0, 1.5, 3.0])
distanciaY['MD'] = fuzz.trapmf(distanciaY.universe, [1.5, 3.0, 10, 10]) #trap	


distanciaY.view()

# Custom membership functions can be built interactively with a familiar,
# Pythonic API
vAngular['VME'] = fuzz.trapmf(vAngular.universe, [-10, -10,-1,-0.5 ]) #trapezoidal
vAngular['VE']  = fuzz.trimf(vAngular.universe, [-1, -0.5, 0])
vAngular['R']   = fuzz.trimf(vAngular.universe, [-0.5, 0, 0.5])
vAngular['VD']  = fuzz.trimf(vAngular.universe, [0, 0.5, 1])
vAngular['VMD'] = fuzz.trapmf(vAngular.universe, [0.5, 1, 10, 10]) #trapezoidal


vAngular.view()


rule1 = ctrl.Rule(distanciaY['ME'], vAngular['VD'])
rule2 = ctrl.Rule(distanciaY['E'], vAngular['VMD'])
rule3 = ctrl.Rule(distanciaY['R'], vAngular['R'])
rule4 = ctrl.Rule(distanciaY['D'], vAngular['VME'])
rule5 = ctrl.Rule(distanciaY['MD'], vAngular['VE'])


tipping_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5])

tipping = ctrl.ControlSystemSimulation(tipping_ctrl)






