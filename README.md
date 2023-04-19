# Job-Rotattion-Ribeirao-Preto

## 1) Observe o trecho de código abaixo:

> int INDICE = 13, SOMA = 0, K = 0;

> enquanto K < INDICE faça

> {

> K = K + 1;

> SOMA = SOMA + K;

> }

> imprimir(SOMA);

Ao final do processamento, qual será o valor da variável SOMA?

`R = 91`

https://github.com/borgesbsb/Job-Rotattion-Ribeirao-Preto/blob/main/q1.py




## 2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

IMPORTANTE:

Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;

https://github.com/borgesbsb/Job-Rotattion-Ribeirao-Preto/blob/main/q2.py

## 3) Descubra a lógica e complete o próximo elemento:


a) 1, 3, 5, 7, `9`

b) 2, 4, 8, 16, 32, 64, `128`

c) 0, 1, 4, 9, 16, 25, 36, `49`

d) 4, 16, 36, 64, `100`

e) 1, 1, 2, 3, 5, 8, `13`

f) 2,10, 12, 16, 17, 18, 19, `200`



## 4 - Dois veículos (um carro e um caminhão) saem respectivamente de cidades opostas pela mesma rodovia. O carro de Ribeirão Preto em direção a Franca, a uma velocidade constante de 110 km/h e o caminhão de Franca em direção a Ribeirão Preto a uma velocidade constante de 80 km/h. Quando eles se cruzarem na rodovia, qual estará mais próximo a cidade de Ribeirão Preto?

IMPORTANTE:

a) Considerar a distância de 100km entre a cidade de Ribeirão Preto <-> Franca.

b) Considerar 2 pedágios como obstáculo e que o caminhão leva 5 minutos a mais para passar em cada um deles e o carro possui tag de pedágio (Sem Parar)

c) Explique como chegou no resultado.

>Inicialmente, podemos calcular o tempo que levará para que o carro e o caminhão se cruzem na rodovia. Como a distância entre as duas cidades é de 100 km >e os veículos estão se aproximando um do outro, podemos considerar que eles percorrerão juntos essa distância. Para calcular o tempo de encontro, usamos >a seguinte fórmula:

>t = d / (v_carro + v_caminhão)

>Onde:

>t = tempo de encontro
>d = distância a percorrer (nesse caso, 100 km)
>v_carro = velocidade do carro (110 km/h)
>v_caminhão = velocidade do caminhão (80 km/h)

>Substituindo esses valores, temos:

>t = 100 / (110 + 80)
>t = 0,5 horas

>Isso significa que o encontro entre o carro e o caminhão ocorrerá após 0,5 horas (ou 30 minutos) de viagem.

>Agora, vamos considerar a questão dos pedágios. Como o carro possui tag de pedágio, ele não precisa parar nos pedágios. Já o caminhão, que não possui >essa facilidade, levará 5 minutos a mais para passar em cada um dos dois pedágios ao longo do caminho. Portanto, podemos calcular o tempo adicional que >o caminhão levará devido aos pedágios:

>tempo_pedágios = 2 * 5 minutos = 10 minutos

>Agora, precisamos saber qual a distância percorrida por cada veículo quando eles se encontrarem. Para isso, podemos usar a seguinte fórmula:

>d_veículo = v_veículo * t

>Onde:

>d_veículo = distância percorrida pelo veículo
>v_veículo = velocidade do veículo (no caso do carro, 110 km/h; no caso do caminhão, 80 km/h)
>t = tempo de encontro (0,5 horas)

>Substituindo esses valores, temos:

>d_carro = 110 * 0,5 = 55 km
>d_caminhão = 80 * 0,5 = 40 km

>Isso significa que o carro estará a 45 km de Ribeirão Preto (100 km - 55 km percorridos) e o caminhão estará a 60 km de Ribeirão Preto (100 km - 40 km >percorridos) quando eles se cruzarem.

>Portanto, concluímos que o carro estará mais próximo da cidade de Ribeirão Preto quando eles se encontrarem, já que estará a uma distância de 45 km, >enquanto o caminhão estará a uma distância de 60 km. Isso ocorre mesmo considerando o tempo adicional que o caminhão levará devido aos pedágios, pois a >diferença de distância percorrida pelos dois veículos é maior do que o tempo adicional que o caminhão levará devido aos pedágios.


## 5) Escreva um programa que inverta os caracteres de um string.

IMPORTANTE:

a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;

b) Evite usar funções prontas, como, por exemplo, reverse;

https://github.com/borgesbsb/Job-Rotattion-Ribeirao-Preto/blob/main/q5.py


