function [y]=graficar(A1, A2, A3, B1, B2, B3, C1, C2, C3, D2, F1, F2, K1, K2, K3)
  s = tf('s');

  G1 = (A1)/(B1*s*(s + C1));
  G2 = (A2*s)/(B2*s*(s + C2/s) + D2);
  G3 = (A3*s*(s + C3))/(B3);

  H1 = K1*(F1*s + 1);
  H2 = K2*s*(1 + F2*s);
  H3 = K3*s;

  num = G1*G2*G3 + G1*H1*G3;
  den = 1 + G1*G2*G3 + G2*H2 + G2*G3*H3 + G3*H1*H3 + G1*G3*H1;

  funct = num/den;

  % Se define un espacio lineal para el tiempo
  t = linspace(0,100,1000);

  % Se obtiene la salida de la respuesta
  [y] = step(funct,t);
