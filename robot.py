import pypot
import time
import ikpy
import sys
import ikpy.utils.plot as plot_utils
from pypot.creatures import PoppyErgoJr
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
    

poppy = ""
my_chain = ikpy.chain.Chain.from_urdf_file("/home/cesi/Bureau/poppy-ergo-jr-master/software/poppy_ergo_jr/poppy_ergo_jr.urdf")


def robot_start():
    global poppy
    poppy = PoppyErgoJr(simulator='vrep', scene='poppy_ergo_jr_holder.ttt', camera='dummy');
    
def robot_position_initial():
    global poppy
    for m in poppy.motors:
        m.goto_position(0,5)
    return;

def robot_position_move(angles):
    global poppy
    i= 0
    for m in poppy.motors:
           m.goto_position(angles[i],7)
           i = i + 1
    return;


def robot_ikpy_test():
    
    global poppy
    
    zero = [0] * 6
    poppy.chain.end_effector
    ax = plt.figure().add_subplot(111, projection='3d')
    ax.scatter([0], [0], [0])
    
    poppy.chain.plot(poppy.chain.convert_to_ik_angles(zero), ax) 
    
    print(poppy.chain.convert_to_ik_angles(zero))
    
    poppy.chain.plot(poppy.chain.convert_to_ik_angles(zero), ax) 
    
    motors_pos = poppy.chain.inverse_kinematics([-3,-10,2])

    print(my_chain.inverse_kinematics([-3,-10,2]))
    print(poppy.chain.convert_from_ik_angles(motors_pos))
    
    motors_pos = poppy.chain.convert_from_ik_angles(motors_pos)
    
    poppy.chain.plot(poppy.chain.convert_to_ik_angles(motors_pos), ax)
    
    robot_position_move(motors_pos)
    
    
def robot_stop():
    global poppy
    poppy.stop_simulation()
    pypot.vrep.close_all_connections();
             
    
def main():
    global poppy
    robot_start();
    robot_position_initial();

if __name__ == "__main__":
    main();