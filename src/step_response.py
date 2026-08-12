import numpy as np
import matplotlib.pyplot as plt

# 1. Definición de Parámetros
tau = 15.0
K = 1.0
M = 57.0
tw = 20.0 # Ancho del pulso 
time = np.linspace(0, 75, 750)

def pulse_response(t, K, M, tau, tw):
    """
    Calcula la respuesta de un sistema de primer orden a un pulso rectangular.
    """
    # Respuesta escalón base (siempre activa para t > 0)
    step1 = K * M * (1 - np.exp(-t / tau))
    
    # Respuesta escalón negativo (solo activa para t >= tw)
    # np.where(condición, valor, 0) actúa como una función Heaviside [1, 15]
    step2 = np.where(t >= tw, K * M * (1 - np.exp(-(t - tw) / tau)), 0)
    
    return step1 - step2

# 2. Ejecución
y = pulse_response(time, K, M, tau, tw)

# 3. Visualización
plt.plot(time, y, label='Respuesta al Pulso')
plt.axvline(x=tw, color='r', linestyle='--', label='Fin del Pulso') # Marca tw
plt.title(f'Simulación de Proceso (tau={tau})')
plt.xlabel('Tiempo (min)')
plt.ylabel('Variable de Desviación')
plt.grid(True, alpha=0.3)
plt.legend()
plt.savefig('images/pulse_response.png', dpi=300, bbox_inches='tight')
plt.close()
