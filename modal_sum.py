import numpy as np

def calc_nu(k, w, beta):
    nu = np.sqrt( (k+0j)**2 - (w/beta)**2 )
    return nu

def P_tl(nu, h):
    return np.cosh(nu*h)

def P_tr(nu, h, mu):
    return np.sinh( (nu*h)/(nu*mu) )

def P_bl(nu, h, mu):
    return (nu*mu)*np.sinh(nu*h)

def P_br(nu, h):
    return np.cosh(nu*h)

def F_bl(nu, h, mu):
    return (1/(2*nu*mu))*nu*mu*np.exp(-1*nu*h)

def F_tr(nu, h, mu):
    return (1/(2*nu*mu))*-1*np.exp(nu*h)

def F_br(nu, h,mu):
    return (1/(2*nu*mu))*np.exp(-1*nu*h)

def F_tl(nu, h, mu):
    return (1/(2*nu*mu))*nu*mu*np.exp(nu*h)
