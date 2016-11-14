# Przybliżenie Pade, Lista 1, Metody numeryczne I.

# Importujemy niezbędne moduły. Słowo kluczowe "as" pozwala nam stosować skrócony zapis, gdy odwołujemy się do funkcji z danego modułu.
# Przykład: w celu wyrysowania funkcji z użyciem Matplotlib, zamiast matplotlib.pyplot.plot(parametry), możemy napisać plt.plot(parametry).

import numpy as np
import matplotlib.pyplot as plt
from bokeh.plotting import figure, output_notebook, show

# Wykres na podstawie x i y przy użyciu modułu Matplotlib
def plotWithMatplotlib(x, y, name):
    plt.plot(x,y)

    # Plot axis
    plt.axhline(0, color = 'k')
    plt.axvline(0, color = 'k')

    plt.ylabel(name)
    plt.xlabel('x')
    
    plt.show()
    
# Wykres na podstawie x i y przy użyciu modułu Bokeh
def plotWithBokeh(x, y, name):
    output_notebook()

    p = figure()

    p.xaxis.axis_label = "x"
    p.yaxis.axis_label_text_font_size = '20pt'
    p.xaxis.axis_label_text_font_size = '20pt'
    p.yaxis.axis_label = name
    p.line(x,y, color="blue", line_width=2)
     
    # Plot axis
    p.line([x[0], x[x.size-1]],[0,0], color="black", line_width=1)
    p.line([x[0], 0],[x[0],y[0]], color="black", line_width=1)
    
    show(p)


# N - resolution to po ang. rozdzielczość, rozdzielczość + 1 to liczba punktow na osi x,
# ktorą wykorzystamy do obliczeń (pokażę na zajęciach dlaczego tak jest)
N = 50

dx = 0.1
start = 0.
stop = start + (N + 1) * dx

# Funkcja arange generuje nam strukturę Array (trochę to lista, trochę to tablica).
# Jako argumenty podajemy punkt startowy, punkt końcowy i odstęp pomiędzy kolejnymi elementami Array (dx).
# Zmienna stop została zdefiniowana w taki sposob, żeby Array miał resolution + 1 elementow

x = np.arange(start, stop, dx)

# Wszystkie poniższe działania wykonywane są na każdym elemencie x, zmienne analyticY, pade1Y, pade2Y są także strukturami Array

analyticY = np.exp(-x)
pade1Y = (6.0 - 2.0*x)/(6.0 + 4.0*x + x*x)
pade2Y = (6.0 - 4.0*x + x*x)/(6.0 + 2.0*x)


"""plotWithMatplotlib(x, analyticY, 'analyticY')
plt.clf()
plotWithMatplotlib(x, pade1Y, 'pade1Y')
plt.clf()
plotWithMatplotlib(x, pade2Y, 'pade2Y')""""

plotWithBokeh(x, analyticY, 'analyticY')
plotWithBokeh(x, pade1Y, 'pade1Y')
plotWithBokeh(x, pade2Y, 'pade2Y')