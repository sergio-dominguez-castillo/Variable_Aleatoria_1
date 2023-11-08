# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 14:53:46 2023

@author: Sergio Dominguez
"""
import numpy as np
from scipy.stats import norm
from scipy.stats import percentileofscore

def distribucion_normal(columna_a_calcular_pdf):
    """
    1. Genera arreglo de valores equidistantes entre los valores mínimo y máximo
    2. Calcula el valor de la función de distribución de probabilidad normal, 
    con los parámetros dados
    
    Args:
        nombre_a_calcular_pdf (Pandas.Serie): Nombre de columna.
        
    Returns:
        x: arreglo de valores equidistantes entre los valores mínimo y máximo, utilizando linspace
        pdf: calcula el valor de la función de distribución de probabilidad normal, con los parámetros dados
    
    
    """
   
    # Calculamos la media y la desviación estándar de los datos, además de los valores máximo y mínimo para graficar.
    mu=columna_a_calcular_pdf.mean()
    sigma=columna_a_calcular_pdf.std()
    minimo=columna_a_calcular_pdf.min()
    maximo=columna_a_calcular_pdf.max()
    
    #Creamos un arreglo de valores equidistantes entre los valores mínimo y máximo, utilizando linspace
    x = np.linspace(minimo, maximo)
    
    #Creamos una función, llamada pdf, que calcula el valor de la función de distribución de probabilidad normal, con los parámetros dados
    # Notemos que "sigma" funciona como "escala"
    pdf = norm.pdf(x, loc=mu, scale=sigma)
    
    return(x,pdf)

def probabilidad_real(columna_a_calcular_pr, valor_escogido):
    """
   imprime la probabilidad real de un valor específico para el cual queremos calcular la probabilidad
    
    Args:
        nombre_a_calcular_pr (Pandas.Serie): Nombre de columna.
        
    Returns:
        none
    
    """
     # probabilidad real
    return(percentileofscore(columna_a_calcular_pr, valor_escogido).round(2))
    
def probabilidad_teorica(columna_a_calcular_pt, valor_escogido):
    """
   imprime la probabilidad teorica de un valor específico para el cual queremos calcular la probabilidad
    
    Args:
        nombre_a_calcular_pt (Pandas.Serie): Nombre del continente.
        
    Returns:
        none
    
    """
    # probabilidad teorica
    mu = np.mean(columna_a_calcular_pt)
    sigma = np.std(columna_a_calcular_pt)
        
    # Calcular la probabilidad acumulada
    return((norm.cdf(valor_escogido, loc=mu, scale=sigma)*100).round(2))

    
 
