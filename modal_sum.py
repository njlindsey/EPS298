import numpy as np

def calc_nu(k, w, beta):
    nu = np.sqrt( (k+0j)**2 - (w/beta)**2 )
    return nu

def P_tl(nu, h):
    return np.cosh(nu*h)
    # factoring out np.exp(nu*h)
    #return 0.5 * (1.0 + np.exp(-2 * nu*h))

def P_tr(nu, h, mu):
    return (1/(nu*mu))*np.sinh((nu*h))
    # factoring out np.exp(nu*h)
    #return (1/(nu*mu)) * 0.5 * (1.0 - np.exp(-2 * nu*h))

def P_bl(nu, h, mu):
    return (nu*mu)*np.sinh(nu*h)
    #factoring out np.exp(nu*h)
    #return nu * mu * 0.5 * (1.0 - np.exp(-2 * nu*h))

def P_br(nu, h):
    return np.cosh(nu*h)
    #factoring out np.exp(nu*h)
    #return 0.5 * (1.0 + np.exp(-2 * nu*h))

def Pprecise_tl(nu, h):
    # factoring out np.exp(nu*h)
    return 0.5 * (1.0 + np.exp(-2 * nu*h))

def Pprecise_tr(nu, h, mu):
    # factoring out np.exp(nu*h)
    return (1/(nu*mu)) * 0.5 * (1.0 - np.exp(-2 * nu*h))

def Pprecise_bl(nu, h, mu):
    #factoring out np.exp(nu*h)
    return nu * mu * 0.5 * (1.0 - np.exp(-2 * nu*h))

def Pprecise_br(nu, h):
    #factoring out np.exp(nu*h)
    return 0.5 * (1.0 + np.exp(-2 * nu*h))

def amplifyP(P, nu, h):
    #at end of propagation, retrieve real amplitudes
    return np.exp(nu*h) * P

def F_bl(nu, h, mu):
    return nu*mu*np.exp(-1*nu*h)

def F_tr(nu, h, mu):
    return -1*np.exp(nu*h)

def F_br(nu, h,mu):
    return np.exp(-1*nu*h)

def F_tl(nu, h, mu):
    return nu*mu*np.exp(nu*h)
