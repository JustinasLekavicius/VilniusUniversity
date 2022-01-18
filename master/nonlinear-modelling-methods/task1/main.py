# Justinas Lekavicius 1 k. KM
# 1 uzduotis nr. 27

import matplotlib.pyplot
import numpy

N = 100000 # duotas parametras N
γ = 0.018 # duotas parametras gamma
σ = 0.4 # duotas parametras sigma
no_of_points = 300

def GenerateDotProcess():
    τ = numpy.zeros(N)
    t = numpy.zeros(N)
    τ[0] = 10
    t[0] = 0
    for i in range(1, N):
        ε_k = numpy.cos(2*numpy.pi*numpy.random.uniform(0,1)) *numpy.square(-2*numpy.log(numpy.random.uniform(0,1)))
        τ[i] = τ[i-1] - γ * (τ[i-1]-10) + σ*ε_k
        t[i] = t[i-1] + τ[i]
    return t

#Fano funkcijos – F(T) = (M(Z^2[m]) - (M(Z[m]))^2) / M(Z[m]) – pagal uzduoti
#Fano funkcija – F(T) = D(Z[k])/M(Z[k]) – pagal studentu konspekta.

def CalculateFanFunction(): 
    t_dots = GenerateDotProcess()
    T_min = 0.1 # Fano funkcijos pradzia
    T_max = 100000 # Fano funkcijos pabaiga
    T = numpy.zeros(no_of_points) # T intervalas (X)
    F = numpy.zeros(no_of_points) # Fano funkcija (Y)
    interval_distance = (numpy.log10(T_max) - numpy.log10(T_min)) / no_of_points # Diskretizavimo zingsnis – atstumas tarp tasku (47 psl. h)

    for i in range (0, no_of_points):
        T[i] = T_min * numpy.power(10, interval_distance * i ) # pagal (23 lygti) 47 psl, skaiciuojame diskrecias reiksmes
        # Fano funkcija:
        M = numpy.int32(numpy.floor(t_dots[N-1] - t_dots[0])/T[i]) # Gauname sekos ilgi – kiek yra T intervalu
        Z = numpy.zeros(M) # Rinkinys tasku, patenkanciu i intervala
        for k in range (0, N):
            m = numpy.int32(numpy.floor(t_dots[k]/T[i])) # ziurime i kuri T intervala pagal indeksa patenka taskas
            if (m >= M):
                break
            Z[m] = Z[m] + 1
        F[i] = numpy.var(Z)/numpy.mean(Z) # Fano funkcijos rezultatas (Y) – dispersija / aritmetinis vidurkis (studentu konspektas)
        #Fano funkcijos pabaiga

    F_min = numpy.amin(numpy.log10(F)) 
    F_max = numpy.amax(numpy.log10(F)) 
    Δ = F_max - F_min # gauname atstuma tarp didziausios ir maziausios Fano funkcjos reiksmes (Y)
    # pridedamas prieaugis (mokymo priemone, 48 psl.)
    F_max = F_min + (Δ*0.75)
    F_min = F_min + (Δ*0.25)
    # gauname maziausia ir didziausia artima reiksme i F_min ir F_max Y, kad rastume taska. Randame labiausiai panasu taska
    Y_min_index = numpy.argmin(numpy.absolute(numpy.log10(F) - F_min))
    Y_max_index = numpy.argmin(numpy.absolute(numpy.log10(F) - F_max)) 
    # Nustatome naujas X ir Y asies minimalia ir maksimalia reiksmes, kurias naudosime naujai tiesei brezti
    F_minmax = [F[Y_min_index], F[Y_max_index]]
    T_minmax = [T[Y_min_index], T[Y_max_index]]

    return T, F, numpy.log10(T_minmax), numpy.log10(F_minmax)

def DrawFanFunctionGraphLogLogScale():
    T, F, x, y = CalculateFanFunction()
    matplotlib.pyplot.loglog(T,F)
    matplotlib.pyplot.scatter(numpy.power(10, x), numpy.power(10, y))
    x_line = numpy.linspace(T[0], T[len(T)-1]) # Sugeneruojame masyva su daug iksu, kuriuos naudosime brezti tiesei
    α  = (y[1] - y[0]) / (x[1] - x[0]) # Gauname Fano konstanta (pagal studentu konspekta 30 psl)
    const = y[0] - α*x[0] 
    y_line = numpy.power(x_line,α) * numpy.power(10,const) # Sugeneruojame masyva su daug ygriku. Formule y = x^α * 10^const. Kadangi log(y) = α * log(x) + const, tai y = x^α * 10^const
    matplotlib.pyplot.loglog(x_line, y_line)
    matplotlib.pyplot.title("Fan constant: " + str(α))
    matplotlib.pyplot.xlabel("x = T")
    matplotlib.pyplot.ylabel("y = F(T)")
    matplotlib.pyplot.show()

DrawFanFunctionGraphLogLogScale()