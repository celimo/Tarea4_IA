function [salida]=funcObjetiva(A1, A2, A3, B1, B2, B3, C1, C2, C3, D2, F1, F2, K1, K2, K3)
  % Se define que la letra s denota la variable de la función de
  % transerencias
  s = tf('s');

  % Se definen las funciones de tranferencia ya dadas
  G1 = (A1)/(B1*s*(s + C1));
  G2 = (A2*s)/(B2*s*(s + C2/s) + D2);
  G3 = (A3*s*(s + C3))/(B3);

  H1 = K1*(F1*s + 1);
  H2 = K2*s*(1 + F2*s);
  H3 = K3*s;

  % Se obtiene la expresión del numerador y denominador para la FT
  % equivalente del sistema
  num = G1*G2*G3 + G1*H1*G3;
  den = 1 + G1*G2*G3 + G2*H2 + G2*G3*H3 + G3*H1*H3 + G1*G3*H1;

  funct = zpk(num/den);

  % Se obtienen los polos de la función de transerencia
  polos = pole(funct);

  % Se obtiene la cantidad de polos que presenta la función
  cont = length(polos);

  temp = 0;
  % Se comprueba si el sistema es estable
  for i = 1:cont
      if real(polos(i)) > 1e-4
          temp = temp + 10 + 1e4*polos(i);
      end
  end

  % Si no es estable retorna el valor de temp
  if temp > 0
      salida = temp;
  else % Si es estable obtiene el sobreimpulso y el tiempo de este
      respuesta = stepinfo(funct);
      t = respuesta.PeakTime;
      Imp = respuesta.Overshoot;
      salida = abs(t-1)+ abs(Imp/20-1);
  end
  % Caso particular donde se presenta un error al obtener el sobreimpulso
  if isnan(salida)
    salida = 1000;
  end
