def dV_ges_zu(A_N):
    return -0.001*A_N**2 + 1.15*A_N + 20

def dV_inf(f_inf=0.5,A_N=None,h=None,n_50=1,delta_p=None):
    if A_N is None or h is None or delta_p is None:
        raise Exception('Parameter nicht angegeben, A_N, h und delta_p müssen spezifiziert werden!')
    
    return f_inf*A_N*h*n_50*(delta_p/50)^0.667
