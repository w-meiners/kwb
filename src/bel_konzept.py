def dV_ges_zu(A_N):
    """Feststehende Formel nach DIN 1946 Teil 6"""
    return -0.001*A_N**2 + 1.15*A_N + 20

def dV_inf(f_inf=0.5,A_N=None,h=None,n_50=1,delta_p=None):
    """Feststehende Formel nach DIN 1946 Teil 6"""
    if A_N is None or h is None or delta_p is None:
        raise Exception('Parameter nicht angegeben, A_N, h und delta_p müssen spezifiziert werden!')
    
    return f_inf*A_N*h*n_50*(delta_p/50)**0.667


def norm_durchmesser(d_0):
    ''' Gibt zum Durchmesser d_0 in mm
        den zugehörigen Normdurchmesser
        in mm aus.
    '''
    import numpy as np
    
    dn = np.array([80,90,100,112,125,140,150,160,180,
          200,224,250,280,300,315,355,400,
          450,500,560,600,630,710,800,900,
          1000,1120,1250,1400,1600,1800,2000])
    return dn[np.where(d_0 <= dn)[0][0]]
