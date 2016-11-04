import numpy as np

def calc_nu(k, w, beta):
    nu = ( k**2 - (w**2/beta**2) )**0.5
    return nu

def tl(nu, h):
    tl = np.cosh(nu*h)
    return tl

def tr(nu, h, mu):
    tr = np.sinh( (nu*h)/(nu*mu) )
    return tr

def bl(nu, h, mu):
    bl = (nu*mu)*np.sinh(nu*h)
    return bl

def br(nu, h):
    br = np.cosh(nu*h)
    return br
