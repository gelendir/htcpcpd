---
title: Acquisition de connaissance
layout: default
category: page
---

Acquisition de connaissance
===========================

Fonctionnement d'un Arduino
---------------------------
L'arduino est un microcontrôleur dont les circuits sont libres et facilement
reproduisable. Pour notre part, nous avons acheté un Arduino modèle Duemilanove.
L'alimentation du Arduino se fait par la connexion USB et elle peut se faire
par une source de 5 volt externe. 

La communication avec le microcontrôleur peut se faire par un port série que 
la connexion USB émule. De plus, notre modèle contient 5 entrées analogiques qui
nous permettent d'avoir une mesure de la tension arrivant à l'entrée. De plus,il 
y a également 13 entréess digitales qui permettent d'avoir une valeur booléenne
qui dit s'il y a du courant ou pas arrivant à l'entrée.

![ArduinoBoard]({{ site.baseurl }}/img/arduino.png)

La programmation sur l'Arduino se fait avec un langage et IDE dérivé de Wiring 
qui est un langage dérivant lui-même du C et du C++. Plusieurs API sont 
disponibles et sont faciles d'utilisations. Voici un exemple de code qui 
lit un valeur analogique et l'envoit au port série:

{% highlight c %}
void setup()
{
  Serial.begin(9600); // Initialise la connexion série
  pinMode(A0, INPUT); // Mettre l'entrée analogique 0 en lecture
}

void loop()
{
  Serial.print("A0:"); // On affiche "A0"
  Serial.println(analogRead(A0)); // On affiche la valeur de A0 et on change de ligne
}
{% endhighlight %}

Fonctionnement de relais
------------------------

Dans le cadre de notre recherche, nous avons eu à apprendre le fonctionnement
d'un relais. Un relais est une composante électronique qui agit un peu comme
un interrupteur c'est-à-dire que nous pouvons fermer ou ouvrir le circuit 
avec un signal digital. 

Comme on le voit ci-dessous, c'est le circuit nécessaire pour contrôler un relais
avec un Arduino. Dans notre cas, la cafetière comprenait déjà le relais ainsi que
le circuit nécessaire à le contrôler.

![ArduinoRelay]({{ site.baseurl }}/img/ArduinoRelay.png)
Source: [http://www.arduino.cc/cgi-bin/yabb2/YaBB.pl?num=1293881907](http://www.arduino.cc/cgi-bin/yabb2/YaBB.pl?num=1293881907)

La difficulté a été de relier ce schéma à celui de notre cafetière. Finalement, 
afin de fermer le circuit du relais de la cafetière, nous avons dû alimenter 
la carte Arduino avec la prise DC du Arduino relié à l'alimentation 5V venant
du relais et à la masse du relais. Voici un image de l'assemblage:

![CafetiereRelais]({{ site.baseurl }}/img/CafetiereRelais.png)

Pull-down
---------


Diviseur de tension
-------------------


Protocole HTCPCP
----------------


