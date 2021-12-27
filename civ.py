#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
from matplotlib import pyplot as pl

pl.close("all")

def c_L_fun(f,w_L,p_L,i_L):
    return (f+w_L/p_L)*(1.0+i_L)

def c_F_fun(w_FW,f,p_F,i_F):
    return (f + w_FW/p_F)*(1.0+i_F)

def w_FW_fun(f,p_F,i_F):
    return f/(1.0/(1.0+i_F)-1.0/p_F)

def w_fun(u):
    return -np.log(u)*10.0

# example

# start
p_F = 1.25
pop = 1000
f = 1.0
i_F = 0.15


def g_F_calc(u,f,pop,p_F,i_F):
    n_FW = int(pop/p_F)
    e = 1.0-u
    e_FW = n_FW/pop
    w_min = w_FW_fun(f,p_F,i_F)
    w = w_fun(u)
    
    if e < e_FW:
        print("err")
        e = e_FW
        
    if w_min > w:
        print("err2")
        w = w_min
        
    cost = (e-e_FW)*w*pop
    g_F = (c_F_fun(w,f,p_F,i_F)*i_F/(1.0+i_F))*pop
    
    print("g_F",g_F,cost)
    

    
    
    

