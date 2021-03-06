#!/usr/bin/env python
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import numpy as np
from matplotlib.lines import Line2D
import matplotlib as mat
import matplotlib.pyplot as plt

fontsize = 18
mat.rc('legend', fontsize=fontsize, handlelength=3)
mat.rc('axes', titlesize=fontsize)
mat.rc('axes', labelsize=25)
mat.rc('xtick', labelsize=fontsize)
mat.rc('ytick', labelsize=fontsize)
# mat.rc('text', usetex=True)
mat.rc('font', size=fontsize, family='serif', style='normal', variant='normal',stretch='normal', weight='normal')

def vs_feature(dumper_1, dumper_2, clamp_1, clamp_2, cable_1, cable_2, label1, label2, title):

    # plt.plot(dumper_1, dumper_2, ls='-', c = 'teal', alpha = 0.2, linewidth = 2.0, linestyle='-') 
    plt.scatter(dumper_1, dumper_2,color='teal', alpha = 0.8, s=50, label=u"Amortecedor de Vibrações", marker='>')

    # plt.plot(clamp_1, clamp_2, ls='-', c = 'green', alpha = 0.2, linewidth = 2.0, linestyle='-') 
    plt.scatter(clamp_1, clamp_2,color='green', alpha = 0.6, s=50, label=u"Grampo de Suspensão", marker='s')

    # plt.plot(cable_1, cable_2, ls='-', c = 'orangered', alpha = 0.2, linewidth = 2.0, linestyle='-') 
    plt.scatter(cable_1, cable_2,color='orangered', s=100, label=u"Ausência de obstáculo", alpha = 1, marker='3')

    # x_axis = [0, 510]

    # plt.xlim(0, 510)
    # plt.xticks( np.arange(min(y), max(y), 25) )
    # plt.yticks( np.arange(min(x_axis), max(x_axis), 0.02) )
    plt.xticks.labelpad = 100
    plt.yticks.labelpad = 100
    plt.xlabel(u""+label1)
    plt.ylabel(u""+label2)

    plt.title(u""+title, fontsize = 25)
    plt.legend(loc='upper center', scatterpoints = 1, bbox_to_anchor=(0.5, -0.1),  shadow=True, ncol=3)
    # plt.plot( amortecedores_area, 'b-o',label="amortecedor" )
    # Grid
    plt.grid(True)
    plt.show()


def single_feature(x,y1,y2,y3, label, title):

    # plt.plot(x, y1, ls='-', c = 'teal', alpha = 0.2, linewidth = 2.0, linestyle='-') 
    plt.scatter(x, y1,color='teal', alpha = 0.8, s=50, marker='>', label= u"Amortecedor de Vibrações")

    # plt.plot(x, y2, ls='-', c = 'green', alpha = 0.2, linewidth = 2.0, linestyle='-') 
    plt.scatter(x, y2,color='green', alpha = 0.6, s= 50, marker='s', label=u"Grampo de Suspensão")

    # plt.plot(x, y3, ls='-', c = 'orangered', alpha = 0.2, linewidth = 2.0, linestyle='-') 
    plt.scatter(x, y3,color='orangered', alpha = 1, s=100, marker='3', label=u"Ausência de obstáculo")

    x_axis = [0, 400]

    plt.xlim(0, 400)
    plt.xticks( np.arange(min(x_axis), max(x_axis), 50) )
    plt.yticks( np.arange(0, 1.1, 0.1) )
    plt.xlabel(u"Amostra")
    plt.ylabel(u""+label)

    plt.title(u""+title, fontsize = 25)
    plt.legend(loc='upper center', scatterpoints = 1, bbox_to_anchor=(0.5, -0.1),  shadow=True, ncol=3)

    # plt.plot( amortecedores_area, 'b-o',label="amortecedor" )
    # Grid
    plt.grid(True)
    plt.show()

def threeD(dumper_1, dumper_2, dumper_3, clamp_1, clamp_2, clamp_3, cable_1, cable_2, cable_3, label1, label2, label3, title):

    fig = plt.figure()
    ax = plt.axes(projection='3d')

    ax.scatter3D(dumper_1, dumper_2, dumper_3, c='teal', alpha = 0.8, s=50, marker='>', cmap='Greens', label = u"Amortecedor de Vibrações")
    ax.scatter3D(clamp_1, clamp_2, clamp_3, c='green', cmap='Greens', alpha = 0.6, s= 50, marker='s', label=u"Grampo de Suspensão")
    ax.scatter3D(cable_1, cable_2, cable_3, c='orangered', cmap='Greens', alpha = 1, s=100, marker='3', label=u"Ausência de obstáculo")
    ax.yaxis.labelpad = 25
    ax.xaxis.labelpad = 25
    ax.zaxis.labelpad = 25
    
    ax.set_xlabel(u""+label1)
    ax.set_ylabel(u""+label2)
    ax.set_zlabel(u""+label3)
    ax.set_title(u""+title, fontsize = 25)
    ax.title.set_position([.5, 1.03])
    ax.legend(loc='upper center', scatterpoints = 1, bbox_to_anchor=(0.5, -0.1),  shadow=True, ncol=3)
    # plt.plot( amortecedores_area, 'b-o',label="amortecedor" )
    # Grid
    plt.grid(True)
    plt.show()
