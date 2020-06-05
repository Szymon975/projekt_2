import numpy as np
import scipy import integrate


def solvr(Y,t):
    return[Y[1],sgp/(np.hypot(asteroid_vec_to_body_x, asteroid_vec_to_body_y)**3)*Y[0],Y[3],sgp/(np.hypot(asteroid_vec_to_body_x, asteroid_vec_to_body_y)**3)*Y[2]]

def main():
    a_t = np.arange(0, 25.0, 0.01)
    
'''odpowiednio przedział czasu i skok czasu'''

    asol = integrate.odeint(solvr, [asteroid_vec_to_body_x0,asteroid_vec_to_body_x0,asteroid_vec_to_body_y0,asteroid_vec_to_body_y0], a_t)
    astack = np.c_[a_t, asol[:,0], asol[:, 1],asol[:,2], asol[:, 3]]
    np.savetxt('approx.csv', astack, delimiter=',', header='t, dx,vx, dy,vy', comments='')

>>> rozwiazuje asteroid_vec_to_body_x, asteroid_vec_to_body_y od czasu dla pewnego celestial body i pewnych parametrów poczatkowych (trzeba dołozyc petle), zapisuje do pliku csv w 5 kolumn
