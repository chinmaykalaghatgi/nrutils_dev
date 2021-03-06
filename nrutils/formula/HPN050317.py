#
# Converted from Mathematica using FortranForm
# ~ L. London, londonl@cardiff.ac.uk
#

#
from numpy import pi,log,sqrt
EulerGamma = 0.57721566490153286060651209008240

'''
Delta   = -sqrt( 1-4*eta )  # NOTE the minus sign!
Xa      = 0.5 * ( X1-X2 )
Xs      = 0.5 * ( X1+X2 )
x       = (pi*f) ** (2/3)   # This is sometimes called v
'''

#
H = {}

#
H[2, 2] = lambda x,eta,Delta,Xa,Xs,X1,X2: 1 + (-2.5476190476190474 + \
(55*eta)/42.)*x + (-24*eta*1j - (107*pi)/21.0+ (34*eta*pi)/21.)*x**2.5 \
+ (eta*((14333*1j)/162. - (2495*pi)/378.) - (2173*pi)/756. + \
eta**2*((-4066*1j)/945. + (40*pi)/27.))*x**3.5 + \
x**2*(-1.437169312169312 - (1069*eta)/216. + (2047*eta**2)/1512. + \
2*eta*X1*X2) + x**1.5*(2*pi - (4*Delta*Xa)/3. + (4*(-1 + eta)*Xs)/3.) \
+ x**3*(41.78634662956092 - (20261*eta**2)/2772. + \
(114635*eta**3)/99792. - (856*EulerGamma)/105. + (428*1j*pi)/105. + \
(2*pi**2)/3. + eta*(-8.362944925444925 + (41*pi**2)/96.) - \
(428*log(16*x))/105.)
#
H[2, 1] = lambda x,eta,Delta,Xa,Xs,X1,X2: (Delta*1j*(sqrt(x) + \
(-0.6071428571428571 + (5*eta)/7.)*x**1.5 + (-0.3412698412698413 - \
(509*eta)/126. + (79*eta**2)/168.)*x**2.5 + x**2*(pi + 1j*(-0.5 - \
2*log(2))) + x**3*((-17*pi)/28. + (3*eta*pi)/14. + \
1j*(0.30357142857142855 + eta*(-11.845238095238095 - (3*log(2))/7.) + \
(17*log(2))/14.))))/3.
#
H[2, 0] = lambda x,eta,Delta,Xa,Xs,X1,X2: -5/(14.*sqrt(6))
#
H[3, 3] = lambda x,eta,Delta,Xa,Xs,X1,X2: \
(-3*sqrt(1.0714285714285714)*Delta*1j*(sqrt(x) + (-4 + 2*eta)*x**1.5 + \
(1.1181818181818182 - (1838*eta)/165. + (887*eta**2)/330.)*x**2.5 + \
x**2*(3*pi + 1j*(-4.2 + 6*log(1.5))) + x**3*(-12*pi + (9*eta*pi)/2. + \
1j*(16.8 - 24*log(1.5) + eta*(-39.59094650205761 + 9*log(1.5))))))/4.
#
H[3, 2] = lambda x,eta,Delta,Xa,Xs,X1,X2: \
(sqrt(0.7142857142857143)*((1 - 3*eta)*x + (-2.1444444444444444 + \
(145*eta)/18. - (73*eta**2)/18.)*x**2 + ((-3 + (66*eta)/5.)*1j + 2*pi \
- 6*eta*pi)*x**2.5 + (-0.3664141414141414 - (17387*eta)/3960. + \
(5557*eta**2)/220. - (5341*eta**3)/1320.)*x**3))/3.
#
H[3, 1] = lambda x,eta,Delta,Xa,Xs,X1,X2: (Delta*1j*(sqrt(x) + \
(-2.6666666666666665 - (2*eta)/3.)*x**1.5 + (3.0656565656565657 - \
(136*eta)/99. - (247*eta**2)/198.)*x**2.5 + x**2*(pi + 1j*(-1.4 - \
2*log(2))) + x**3*((-8*pi)/3. - (7*eta*pi)/6. + 1j*(3.7333333333333334 \
+ (16*log(2))/3. + eta*(-0.06666666666666667 + \
(7*log(2))/3.)))))/(12.*sqrt(14))
#
H[3, 0] = lambda x,eta,Delta,Xa,Xs,X1,X2: \
(-2*sqrt(0.8571428571428571)*eta*1j*x**2.5)/5.
#
H[4, 4] = lambda x,eta,Delta,Xa,Xs,X1,X2: \
(-8*sqrt(0.7142857142857143)*((1 - 3*eta)*x + (-5.390909090909091 + \
(1273*eta)/66. - (175*eta**2)/22.)*x**2 + (5.338016983016983 - \
(1088119*eta)/28600. + (146879*eta**2)/2340. - \
(226097*eta**3)/17160.)*x**3 + x**2.5*(4*pi - 12*eta*pi + 1j*(-8.4 + \
eta*(29.825 - 24*log(2)) + 8*log(2)))))/9.
#
H[4, 3] = lambda x,eta,Delta,Xa,Xs,X1,X2: (-9*Delta*1j*((1 - \
2*eta)*x**1.5 + (-3.5454545454545454 + (1267*eta)/132. - \
(131*eta**2)/33.)*x**2.5 + x**3*(3*pi - 6*eta*pi + 1j*(-6.4 + \
eta*(20.12469135802469 - 12*log(1.5)) + 6*log(1.5)))))/(4.*sqrt(70))
#
H[4, 2] = lambda x,eta,Delta,Xa,Xs,X1,X2: (sqrt(5)*((1 - 3*eta)*x + \
(-3.9727272727272727 + (805*eta)/66. - (19*eta**2)/22.)*x**2 + ((-4.2 \
+ (84*eta)/5.)*1j + 2*pi - 6*eta*pi)*x**2.5 + (5.18500999000999 - \
(606751*eta)/28600. + (400453*eta**2)/25740. + \
(25783*eta**3)/17160.)*x**3))/63.
#
H[4, 1] = lambda x,eta,Delta,Xa,Xs,X1,X2: (Delta*1j*((1 - \
2*eta)*x**1.5 + (-3.0606060606060606 + (337*eta)/44. - \
(83*eta**2)/33.)*x**2.5 + x**3*(pi - 2*eta*pi + \
1j*(-2.1333333333333333 - 2*log(2) + eta*(55.36666666666667 + \
4*log(2))))))/(84.*sqrt(10))
#
H[4, 0] = lambda x,eta,Delta,Xa,Xs,X1,X2: -1/(504.*sqrt(2))
#
H[5, 5] = lambda x,eta,Delta,Xa,Xs,X1,X2: (625*Delta*1j*((1 - \
2*eta)*x**1.5 + (-6.743589743589744 + (688*eta)/39. - \
(256*eta**2)/39.)*x**2.5 + x**3*(5*pi - 10*eta*pi + \
1j*(-12.928571428571429 + eta*(33.86688 - 20*log(2.5)) + \
10*log(2.5)))))/(96.*sqrt(66))
#
H[5, 4] = lambda x,eta,Delta,Xa,Xs,X1,X2: (-32*((1 - 5*eta + \
5*eta**2)*x**2 + (-4.891208791208792 + (3619*eta)/130. - \
(521*eta**2)/13. + (339*eta**3)/26.)*x**3))/(9.*sqrt(165))
#
H[5, 3] = lambda x,eta,Delta,Xa,Xs,X1,X2: \
(-9*sqrt(0.02727272727272727)*Delta*1j*((1 - 2*eta)*x**1.5 + \
(-5.3076923076923075 + (464*eta)/39. - (88*eta**2)/39.)*x**2.5 + \
x**3*(3*pi - 6*eta*pi + 1j*(-7.757142857142857 + \
eta*(22.963511659807956 - 12*log(1.5)) + 6*log(1.5)))))/32.
#
H[5, 2] = lambda x,eta,Delta,Xa,Xs,X1,X2: (2*((1 - 5*eta + \
5*eta**2)*x**2 + (-4.297802197802198 + (3079*eta)/130. - \
(413*eta**2)/13. + (231*eta**3)/26.)*x**3))/(27.*sqrt(55))
#
H[5, 1] = lambda x,eta,Delta,Xa,Xs,X1,X2: (Delta*1j*((1 - \
2*eta)*x**1.5 + (-4.589743589743589 + (352*eta)/39. - \
(4*eta**2)/39.)*x**2.5 + x**3*(pi - 2*eta*pi + 1j*(-2.585714285714286 \
- 2*log(2) + eta*(125.2 + 4*log(2))))))/(288.*sqrt(385))
#
H[5, 0] = lambda x,eta,Delta,Xa,Xs,X1,X2: 0
#
H[6, 6] = lambda x,eta,Delta,Xa,Xs,X1,X2: (54*((1 - 5*eta + \
5*eta**2)*x**2 + (-8.071428571428571 + (91*eta)/2. - 64*eta**2 + \
(39*eta**3)/2.)*x**3))/(5.*sqrt(143))
#
H[6, 5] = lambda x,eta,Delta,Xa,Xs,X1,X2: (3125*Delta*(1 - 4*eta + \
3*eta**2)*1j*x**2.5)/(504.*sqrt(429))
#
H[6, 4] = lambda x,eta,Delta,Xa,Xs,X1,X2: \
(-128*sqrt(0.05128205128205128)*((1 - 5*eta + 5*eta**2)*x**2 + \
(-6.642857142857143 + (71*eta)/2. - 44*eta**2 + \
(19*eta**3)/2.)*x**3))/495.
#
H[6, 3] = lambda x,eta,Delta,Xa,Xs,X1,X2: (-81*Delta*(1 - 4*eta + \
3*eta**2)*1j*x**2.5)/(616.*sqrt(65))
#
H[6, 2] = lambda x,eta,Delta,Xa,Xs,X1,X2: (2*((1 - 5*eta + \
5*eta**2)*x**2 + (-5.785714285714286 + (59*eta)/2. - 32*eta**2 + \
(7*eta**3)/2.)*x**3))/(297.*sqrt(65))
#
H[6, 1] = lambda x,eta,Delta,Xa,Xs,X1,X2: (Delta*(1 - 4*eta + \
3*eta**2)*1j*x**2.5)/(8316.*sqrt(26))
#
H[6, 0] = lambda x,eta,Delta,Xa,Xs,X1,X2: 0
#
H[7, 7] = lambda x,eta,Delta,Xa,Xs,X1,X2: \
(-16807*sqrt(0.008158508158508158)*Delta*(1 - 4*eta + \
3*eta**2)*1j*x**2.5)/1440.
#
H[7, 6] = lambda x,eta,Delta,Xa,Xs,X1,X2: \
(81*sqrt(0.02097902097902098)*(1 - 7*eta + 14*eta**2 - \
7*eta**3)*x**3)/35.
#
H[7, 5] = lambda x,eta,Delta,Xa,Xs,X1,X2: (15625*Delta*(1 - 4*eta + \
3*eta**2)*1j*x**2.5)/(26208.*sqrt(66))
#
H[7, 4] = lambda x,eta,Delta,Xa,Xs,X1,X2: \
(-128*sqrt(0.06060606060606061)*(1 - 7*eta + 14*eta**2 - \
7*eta**3)*x**3)/1365.
#
H[7, 3] = lambda x,eta,Delta,Xa,Xs,X1,X2: (-243*sqrt(1.5)*Delta*(1 - \
4*eta + 3*eta**2)*1j*x**2.5)/160160.
#
H[7, 2] = lambda x,eta,Delta,Xa,Xs,X1,X2: ((1 - 7*eta + 14*eta**2 - \
7*eta**3)*x**3)/(3003.*sqrt(3))
#
H[7, 1] = lambda x,eta,Delta,Xa,Xs,X1,X2: (Delta*(1 - 4*eta + \
3*eta**2)*1j*x**2.5)/(864864.*sqrt(2))
#
H[7, 0] = lambda x,eta,Delta,Xa,Xs,X1,X2: 0
#
H[8, 8] = lambda x,eta,Delta,Xa,Xs,X1,X2: \
(-16384*sqrt(0.000023505905858847036)*(1 - 7*eta + 14*eta**2 - \
7*eta**3)*x**3)/63.
#
H[8, 7] = lambda x,eta,Delta,Xa,Xs,X1,X2: 0
#
H[8, 6] = lambda x,eta,Delta,Xa,Xs,X1,X2: \
(243*sqrt(0.00017629429394135277)*(1 - 7*eta + 14*eta**2 - \
7*eta**3)*x**3)/35.
#
H[8, 5] = lambda x,eta,Delta,Xa,Xs,X1,X2: 0
#
H[8, 4] = lambda x,eta,Delta,Xa,Xs,X1,X2: \
(-128*sqrt(0.0106951871657754)*(1 - 7*eta + 14*eta**2 - \
7*eta**3)*x**3)/4095.
#
H[8, 3] = lambda x,eta,Delta,Xa,Xs,X1,X2: 0
#
H[8, 2] = lambda x,eta,Delta,Xa,Xs,X1,X2: ((1 - 7*eta + 14*eta**2 - \
7*eta**3)*x**3)/(9009.*sqrt(85))
#
H[8, 1] = lambda x,eta,Delta,Xa,Xs,X1,X2: 0
#
H[8, 0] = lambda x,eta,Delta,Xa,Xs,X1,X2: 0


#
__XdotT4__ = lambda x,m1,m2,eta,X1,X2: (-7.634928269848905e-9*(1.0- 1.*sqrt(1.0- 4.*eta))*(1.0+ 1.*sqrt(1.0- 4.*eta))*x**5*(151593.75*(1.0- 1.*sqrt(1.0- 4.*eta))**6*x**3*(2169.25*(1.0+ 1.*sqrt(1.0- 4.*eta))**2*sqrt(x) - 7896*X1)*X1 + 721.875*(1.0- 1.*sqrt(1.0- 4.*eta))**5*x**2.5*(-385985.25*(1.0+ 1.*sqrt(1.0- 4.*eta))**2*x*X1 + 2744280*sqrt(x)*X1**2 - 4.5*(1.0+ 1.*sqrt(1.0- 4.*eta))*X1*(168168 + 956307*x + 736960*sqrt(x)*X1) + 4.375*(1.0+ 1.*sqrt(1.0- 4.*eta))**3*(1121*sqrt(x) + 211164*x*X1 + 2916*x*X2)) + 360.9375*(1.0- 1.*sqrt(1.0- 4.*eta))**4*x**1.5*(4*(284256 + 738486*x + 3772435*x**2 + 1512*x**1.5*(752*pi - 375*X1))*X1 + 771970.5*(1.0+ 1.*sqrt(1.0- 4.*eta))**3*x**2*X2 + 36.*(1.0+ 1.*sqrt(1.0- 4.*eta))*x*X1*(35406 + 80119*x - 152460*sqrt(x)*X2) + 17.5*(1.0+ 1.*sqrt(1.0- 4.*eta))**4*(1121*x**1.5 + 54978*x**2*(X1 + X2)) - 0.75*(1.0+ 1.*sqrt(1.0- 4.*eta))**2*sqrt(x)*(79296 + 4036032*sqrt(x)*X1 + 8*x**1.5*(182990*pi + 3399633*X1 + 530712*X2) + 3*x*(4869 + 1702428*X1**2 + 2711352*X1*X2 + 228508*X2**2))) + 240.625*(1.0- 1.*sqrt(1.0- 4.*eta))**3*x*(1.15795575e6*(1.0+ 1.*sqrt(1.0- 4.*eta))**4*x**2.5*X1 - 12*sqrt(x)*(113400 + 174744*x + 456624*pi*x**1.5 + 644635*x**2)*X1 - 54.*(1.0+ 1.*sqrt(1.0- 4.*eta))**2*x**1.5*(152460*sqrt(x)*X1*(X1 - X2) + 35406*X2 + 80119*x*X2) + 13.125*(1.0+ 1.*sqrt(1.0- 4.*eta))**5*x**2*(1121 + 12*sqrt(x)*(243*X1 + 17597*X2)) + 0.5*(1.0+ 1.*sqrt(1.0- 4.*eta))*(598752 + 6822144*sqrt(x)*X1 + 3024*x**1.5*(1701*pi + 5861*X1) + x**2.5*(-12912300*pi + 97151928*X1 + 6613488*X2) + 108*x*(-13661 + 10206*X1**2 - 19908*X1*X2 + 10206*X2**2) + x**2*(56198689 - 2045736*pi**2 + 27288576*pi*X1 + 30746952*X1**2 + 13635864*X1*X2 + 3617892*X2**2)) - 2.25*(1.0+ 1.*sqrt(1.0- 4.*eta))**3*x*(79296 + 1009008*sqrt(x)*(X1 + X2) + 3*x*(4869 + 228508*X1**2 + 2711352*X1*X2 + 228508*X2**2) + 2*x**1.5*(731960*pi + 4991769*(X1 + X2)))) + 0.25*(1.0- 1.*sqrt(1.0- 4.*eta))**2*(-419126400 + 1247400*(743 + 462.*(1.0+ 1.*sqrt(1.0- 4.*eta))**2)*x - 23100*x**2*(34103 + 3717.*(1.0+ 1.*sqrt(1.0- 4.*eta))**4 + 91854*X1**2 - 4.5*(1.0+ 1.*sqrt(1.0- 4.*eta))**2*(-13661 + 10206*X1**2 - 19908*X1*X2 + 10206*X2**2)) - 34927200*x**1.5*(48*pi - 0.5*(1.0+ 1.*sqrt(1.0- 4.*eta))*(75*X2 + 94.*(1.0+ 1.*sqrt(1.0- 4.*eta))*(X1 + X2))) + 207900*x**2.5*(3*(4159 + 7938.*(1.0+ 1.*sqrt(1.0- 4.*eta))**2)*pi + 1.*(1.0+ 1.*sqrt(1.0- 4.*eta))*(-8851.5*(1.0+ 1.*sqrt(1.0- 4.*eta))**2*X1 + 9708*X2 - 21021.*(1.0+ 1.*sqrt(1.0- 4.*eta))**3*X2 + 20513.5*(1.0+ 1.*sqrt(1.0- 4.*eta))*(X1 + X2))) - 11550*x**3.5*(15*(-2649 + 71735.*(1.0+ 1.*sqrt(1.0- 4.*eta))**2 + 9149.5*(1.0+ 1.*sqrt(1.0- 4.*eta))**4)*pi + 1.*(1.0+ 1.*sqrt(1.0- 4.*eta))*(360535.5*(1.0+ 1.*sqrt(1.0- 4.*eta))**2*X1 - 644635*X2 + 96496.3125*(1.0+ 1.*sqrt(1.0- 4.*eta))**4*X2 - 113885.625*(1.0+ 1.*sqrt(1.0- 4.*eta))**5*X2 - 2.4373415e6*(1.0+ 1.*sqrt(1.0- 4.*eta))*(X1 + X2) + 6.75*(1.0+ 1.*sqrt(1.0- 4.*eta))**3*(58968*X1 + 377737*X2))) + x**3*(6833756160*EulerGamma + 1.6568782274499674e10*(1.0+ 1.*sqrt(1.0- 4.*eta))*X2 + 7.9241085e9*(1.0+ 1.*sqrt(1.0- 4.*eta))**3*(X1 - X2)*X2 - 3248.4375*(1.0+ 1.*sqrt(1.0- 4.*eta))**4*(4869 + 228508*X1**2 + 2711352*X1*X2 + 1702428*X2**2) - 962.5*(1.0+ 1.*sqrt(1.0- 4.*eta))**2*(-56198689 + 2045736*pi**2 - 6976422*X1**2 + 13580136*X1*X2 - 6976422*X2**2 - 6822144*pi*(X1 + X2)) - 3*(16447322263 + 745113600*pi**2 + 2321480700*X1**2 - 2277918720*log(4)))) + 0.25*(1.0- 1.*sqrt(1.0- 4.*eta))*(1.0+ 1.*sqrt(1.0- 4.*eta))*(-838252800 + 2494800*(743 + 115.5*(1.0+ 1.*sqrt(1.0- 4.*eta))**2)*x + 415800*x**2.5*(3*(4159 + 1984.5*(1.0+ 1.*sqrt(1.0- 4.*eta))**2)*pi + 4854.*(1.0+ 1.*sqrt(1.0- 4.*eta))*X1 + 20513.5*(1.0+ 1.*sqrt(1.0- 4.*eta))**2*X2 + 4425.75*(1.0+ 1.*sqrt(1.0- 4.*eta))**3*X2 - 5255.25*(1.0+ 1.*sqrt(1.0- 4.*eta))**4*X2) - 34927200*x**1.5*(96*pi - 0.5*(1.0+ 1.*sqrt(1.0- 4.*eta))*(75*X1 + 188.*(1.0+ 1.*sqrt(1.0- 4.*eta))*X2)) - 23100*x**3.5*(15*(-2649 + 17933.75*(1.0+ 1.*sqrt(1.0- 4.*eta))**2)*pi + 0.5*(1.0+ 1.*sqrt(1.0- 4.*eta))*(-((644635 + 275562.*(1.0+ 1.*sqrt(1.0- 4.*eta)))*X1) + 0.5*(-8095994 - 721071.*(1.0+ 1.*sqrt(1.0- 4.*eta)) + 2.15169075e6*(1.0+ 1.*sqrt(1.0- 4.*eta))**2)*(1.0+ 1.*sqrt(1.0- 4.*eta))*X2)) + 23100*x**2*(2.25*(1.0+ 1.*sqrt(1.0- 4.*eta))**2*(-13661 + 10206*X1**2 - 19908*X1*X2 + 10206*X2**2) - 2*(34103 + 45927*X1**2 + 45927*X2**2)) + x**3*(13667512320*EulerGamma + 1.6568782274499674e10*(1.0+ 1.*sqrt(1.0- 4.*eta))*X1 - 7.9241085e9*(1.0+ 1.*sqrt(1.0- 4.*eta))**3*X1*X2 - 9.575874e9*(1.0+ 1.*sqrt(1.0- 4.*eta))**4*X2**2 - 481.25*(1.0+ 1.*sqrt(1.0- 4.*eta))**2*(-56198689 + 2045736*pi**2 - 3617892*X1**2 - 27288576*pi*X2 - 13635864*X1*X2 - 30746952*X2**2) - 6*(16447322263 + 745113600*pi**2 + 1160740350*X1**2 + 1160740350*X2**2 - 2277918720*log(4)))) - 0.75*(1.0+ 1.*sqrt(1.0- 4.*eta))**2*(139708800 - 308939400*x + 11642400*x**1.5*(48*pi + 0.5*(75 - 94.*(1.0+ 1.*sqrt(1.0- 4.*eta)))*(1.0+ 1.*sqrt(1.0- 4.*eta))*X2) - 69300*x**2.5*(12477*pi + 1.*(-9708 + 20513.5*(1.0+ 1.*sqrt(1.0- 4.*eta)))*(1.0+ 1.*sqrt(1.0- 4.*eta))*X2) - 19250*x**3.5*(7947*pi + 1.*(-128927 + 377243.5*(1.0+ 1.*sqrt(1.0- 4.*eta)))*(1.0+ 1.*sqrt(1.0- 4.*eta))*X2) + 7700*x**2*(34103 + 91854*X2**2) + x**3*(16447322263 - 2277918720*EulerGamma + 745113600*pi**2 - 3.6575678310153805e7*(-151 + 188.*(1.0+ 1.*sqrt(1.0- 4.*eta)))*(1.0+ 1.*sqrt(1.0- 4.*eta))*X2 + 2321480700*X2**2 + 1.091475e9*(1.0+ 1.*sqrt(1.0- 4.*eta))**2*X2**2 - 2.6413695e9*(1.0+ 1.*sqrt(1.0- 4.*eta))**3*X2**2 + 1.595979e9*(1.0+ 1.*sqrt(1.0- 4.*eta))**4*X2**2 - 2277918720*log(4))) + 3416878080*(0.5*(1.0- 1.*sqrt(1.0- 4.*eta)) + 0.5*(1.0+ 1.*sqrt(1.0- 4.*eta)))**2*x**3*log(x)))/(0.5*(1.0- 1.*sqrt(1.0- 4.*eta)) + 0.5*(1.0+ 1.*sqrt(1.0- 4.*eta)))**2
