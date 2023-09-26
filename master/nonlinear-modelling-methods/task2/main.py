# Justinas Lekavičius 1 k. KM 
# 2 užduotis nr. 17 – Lygtis E, Algoritmas E1, kraštinės sąlygos I

import numpy

x = 0.8  # 0 < x < 1
t = 0.7  # t > 0
h = 0.1 # pasirinkau pats
tau = 0.1 # pasirinkau pats
a = 0.7 # laisvai keičiama konstanta a
gamma = 1.8 # laisvai keičiama konstanta gama
kappa_boundary , gamma_boundary = [0, 0], [0, 0] # kraštinės sąlygos, kapa ir gama
error_thomas_test = numpy.power(10.0, -10) # Paklaida Thomas algoritmo testui
N_thomas_test = 100 # Taškai Thomas algoritmo testui

def CalculateUExact(x,t): # I kraštinių salygų pavyzdinė funkcija
    return complex(1,t) * numpy.sin(numpy.pi * x)

def FFunction(x, t): # F funkcijos skaičiavimas – išvesta iš netiesinės Kuramoto-Cuzuki lygties
    return DerivativeDuDt(x) - complex(numpy.square(a), 1) * DerivativeDSquaredDxSquared(x, t)  - complex(0, (gamma * numpy.log(1 + UAbsoluteSquared(x, t))))

def DerivativeDuDt(x): # Išvestinės du/dt skaičiavimas
    return complex(0, numpy.sin(numpy.pi * x)) # gauta iš Wolfram Alpha: https://www.wolframalpha.com/input/?i=d%2Fdt+%281+%2B+i*t%29*sin%282pi*x%29

def DerivativeDSquaredDxSquared(x, t): # Išvestinės d^2u/dx^2 skaičiavimas
    return -numpy.square(numpy.pi) * (complex(1,t)) * numpy.sin(numpy.pi * x) # gauta iš Wolfram Alpha: https://www.wolframalpha.com/input/?i=d%5E2%2Fdx%5E2+%281+%2B+i*t%29*sin%28pi*x%29

def UAbsoluteSquared(x, t): # U modulio kvadratu skaičiavimas
    return numpy.square(numpy.absolute(CalculateUExact(x,t)))

# Pirmas testas: Iš u tikslaus (sprendinio) gauname f(x,t) (sprendimą) 
def TestFirst(x, t, h, tau):
    uj = CalculateUExact(x, t)
    uj_plus_one = CalculateUExact(x + h, t)
    uj_minus_one = CalculateUExact(x - h, t)
    uj_roof_j = CalculateUExact(x, t + tau)
    uj_roof_j_plus_one = CalculateUExact(x + h, t + tau)
    uj_roof_j_minus_one = CalculateUExact(x - h, t + tau)
    f_j = FFunction(x, t)
    f_roof_j = FFunction(x, t + tau)
    # Žemiau – E1 algoritmo skaičiavimas, išskaidytas į atskiras dalis.
    E1_left_side = (uj_roof_j - uj) / tau
    E1_right_side_1 = complex(numpy.square(a), 1) * 0.5 * (((uj_roof_j_plus_one - (2 * uj_roof_j) + uj_roof_j_minus_one) / numpy.square(h)) + (((uj_plus_one - (2 * uj) + uj_minus_one) / numpy.square(h))))
    E1_right_side_2 = complex(0, gamma) * numpy.log(1 + numpy.square(numpy.absolute((uj_roof_j + uj) / 2)))
    E1_right_side_3 = (f_roof_j + f_j) / 2
    return numpy.absolute(E1_left_side - E1_right_side_1 - E1_right_side_2 - E1_right_side_3) # Skaičiuojama netiktis

print("Vykdomas pirmasis testas")
print("_____________________________________________________________")
for i in range(0, 5):
    t1 = TestFirst(x, t, (h / numpy.power(10, i)), (tau / numpy.power(10, i)))
    t2 = TestFirst(x, t, (h / numpy.power(10, i+1)), (tau / numpy.power(10, i+1)))
    print("Netiktis sumazejo: ", t1 / t2, " kartu")
    if ((t1 / t2) > 95): # Testas sėkmingas, jeigu netiktis sumažėjo daugiau nei 95 kartus.
        print("Testas sekmingas ✓")
    else:         
        print("Testas nesekmingas ✕")
print("_____________________________________________________________")

def CValue(h, tau): # Skaičiuojame kompleksinę konstantą C
    C = 2 + 2 * numpy.square(h) / (complex(numpy.square(a),1)) / tau # Išsireikšta iš E1 algoritmo supaprastinant, keliant reikšmes prie u su stogu į dešinę (C), o visa kita į kairę (F)
    return C

def FValue(x, t, h, tau): # Skaičiuojame F reikšmę
    uj = CalculateUExact(x, t)
    uj_plus_one = CalculateUExact(x + h, t)
    uj_minus_one = CalculateUExact(x - h, t)
    u_roof_j = CalculateUExact(x, t + tau)
    f_j = FFunction(x, t)
    f_roof_j = FFunction(x, t + tau)
    E1_right_side_2 = complex(0, gamma) * numpy.log(1 + numpy.square(numpy.absolute((u_roof_j + uj) / 2)))
    E1_right_side_3 = (f_roof_j + f_j) / 2
    k = 2 * (numpy.square(h)) / (complex(numpy.square(a),1))
    F = (k * (uj / tau)) + (uj_plus_one - (2 * uj) + uj_minus_one) + k * (E1_right_side_2) + k * (E1_right_side_3)
    return F

# Testuojam ar gerai išvestos F ir C reikšmės (vėliau naudojamos Thomas algoritmui)
def TestSecond(x, t, h, tau):
    u_roof_j = CalculateUExact(x, t + tau)
    u_roof_j_plus_one = CalculateUExact(x + h, t + tau)
    u_roof_j_minus_one = CalculateUExact(x - h, t + tau)
    return abs(u_roof_j_plus_one - (CValue(h, tau) * u_roof_j) +  u_roof_j_minus_one + FValue(x, t, h, tau))

print("Vykdomas antrasis testas")
print("_____________________________________________________________")
for i in range(0, 5):
    t1 = TestSecond(x,t, (h / numpy.power(10, i)), (tau / numpy.power(10, i)))
    t2 = TestSecond(x,t, (h / numpy.power(10, i + 1)), (tau / numpy.power(10, i + 1)))
    print("Netiktis sumazejo: ", t1 / t2, " kartu")
    if ((t1 / t2) > 10000): # Jeigu netiktis sumažėjo daugiau nei 10^4 kartų, testas sėkmingas.
        print("Testas sekmingas ✓")
    else:         
        print("Testas nesekmingas ✕")
print("_____________________________________________________________")

# Thomas algoritmas (perkelties metodas)
def ThomasAlgorithm(alphas_list, betas_list):
    y_thomas = numpy.full(N_thomas_test, complex(0, 0))
    for i in reversed (range (1, N_thomas_test - 1)):
        y_thomas[i] = alphas_list[i] * y_thomas[i + 1] + betas_list[i]
    return y_thomas

# Perkelties algoritmo testavimas
def TestThird():
    print("Vykdomas trečiasis testas")
    print("_____________________________________________________________")
    y_array = numpy.full(N_thomas_test, complex(0, 0))
    F_list = numpy.full(N_thomas_test, complex(0, 0))
    alphas_list = numpy.full(N_thomas_test, complex(0, 0))
    betas_list = numpy.full(N_thomas_test, complex(0, 0))
    h = 1 / N_thomas_test
    C = CValue(h, tau)
    alphas_list[0] = kappa_boundary[0] # Pagal 44 psl. studentų konspektą
    betas_list[0] = gamma_boundary[0]
    # alphas_list[1] = kappa_boundary[1]
    # betas_list[1] = gamma_boundary[1]
    for i in range (1, N_thomas_test - 1):
        y_array[i] = CalculateUExact(i, t)
        F_list[i] = -y_array[i - 1] + C * y_array[i + 1] - y_array[i + 1]
        alphas_list[i] = 1 / (C - alphas_list[i - 1])
        betas_list[i] = (F_list[i - 1] + betas_list[i - 1]) / (C - alphas_list[i - 1])
    # Testuosim Thomas algoritmą
    y_thomas = ThomasAlgorithm(alphas_list, betas_list)
    maximum_error_value = numpy.max([numpy.absolute(y_thomas[i] - y_array[i]) for i in range (0, N_thomas_test)])
    
    if (maximum_error_value <= error_thomas_test):
        print("Testas sekmingas ✓")
        print("Paklaida: ", maximum_error_value)
    else:         
        print("Testas nesekmingas ✕")
        print("Paklaida: ", maximum_error_value)

    print("_____________________________________________________________")
    
TestThird()

