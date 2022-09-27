import numpy as np
import math
import pylab as pl
import matplotlib.pyplot as plt
r1 = 8
r2 = 3
r3 = 8
r4 = 6

if (r2 + r3 + r4 >= r1 and r2 + r3 - r4 <= r1 
    and r2 + r1 + r4 >= r3 and r2 + r1 - r4 <= r3):

    angulos =np.radians(np.array(np.linspace(-180, 180,300, endpoint=True)))

    z = np.sqrt(r1**2 + r2**2 - 2*r1*r2*np.cos(angulos))

    alfa = np.arccos((z**2 + r4**2 - r3**2)/(2*z*r4))

    beta = np.arccos((z**2 + r1**2 - r2**2)/(2*z*r1))

    theta4 = 180 - (np.degrees(alfa) + np.degrees(beta))

    angulosdeg = np.degrees(angulos)

    fig = plt.figure()

    plt.xlabel('Angulo theta2 em graus')
    plt.ylabel('Angulo theta 4')
    plt.plot(angulosdeg, theta4) 
    plt.show()

else:
    print("Os valores escolhidos não são possíveis")
