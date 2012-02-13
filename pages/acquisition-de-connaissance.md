---
title: Acquisition de connaissance
layout: default
category: page
---

Acquisition de connaissance
===========================

Fonctionnement d'un Arduino
---------------------------
L'Arduino est un microcontrôleur avec un circuit imprimé dont les spécifications
utilisent une licence libre. Pour notre part, nous avons acheté un Arduino
modèle Duemilanove. L'alimentation du Arduino se fait par la connexion USB 
et elle peut se faire par une source de 5 volts externe. 

La communication avec le microcontrôleur peut se faire par un port série que 
la connexion USB émule. De plus, notre modèle contient 5 entrées analogiques qui
nous permettent d'avoir une mesure de la tension arrivant à l'entrée. Il y a 
également 13 entrées digitales qui permettent d'avoir une valeur booléenne
qui dit s'il y a du courant ou pas arrivant à l'entrée.

![ArduinoBoard]({{ site.baseurl }}/img/arduino.png)

La programmation sur l'Arduino se fait avec un langage et IDE dérivé de Wiring 
qui est un langage dérivant lui-même du C et du C++. Plusieurs API sont 
disponibles et sont faciles d'utilisations. Voici un exemple de code qui 
lit une valeur analogique et l'envoie au port série:

{% highlight c++ %}
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

Programmation série en Python
-----------------------------
Afin de pouvoir dialoguer avec le système embarqué Arduino, il a fallu apprendre
à effectuer une connexion série en Python. Nous avons donc décidé le module
python pyserial. La programmation est très simple malgré qu'il y ait eu un 
accrochage. La classe principale de pyserial qui se nomme « Serial » a une
méthode qui se nomme « open » mais il n'est pas toujours obligatoire de
l'appeler pour ouvrir la connexion selon les arguments qui sont passés au 
constructeur. Cela nous a fait perdre un peu de temps. Voici un exemple de
code permettant d'ouvrir une connexion série, d'envoyer un message et de lire
une réponse:

{% highlight python %}
import serial
ser = serial.Serial('/dev/ttyUSB0', 9600)
ser.write('Hello world\n')
line = ser.readline()
ser.close()
{% endhighlight %}

Protocole HTCPCP
----------------
Étant donné que le protocole HTCPCP spécifiait une nouvelle méthode HTTP et 
un nouvel en-tête HTTP, il était impossible de l'implémenter avec un serveur
HTTP connu. Nous avons donc choisi SimpleHTTPServer qui est un module python
qui permet comme le dit son nom d'avoir un serveur HTTP simple. Pour s'en servir,
il suffisait d'hériter SimpleHTTPRequestHandler et d'implémenter la méthode 
HTTP voulue en créant des méthodes dont le nom commence par « do_ » suivi du
nom de la méthode HTTP. Voici un exemple de code:

{% highlight python %}
import SimpleHTTPServer
import SocketServer

PORT = 8000

class HTTPImpl(SimpleHTTPServer.SimpleHTTPRequestHandler):
	def do_GET(self):
		self.send_response(200)
		self.end_headers()
		self.wfile.write("Ceci est une requête GET")

	def do_POST(self):
		self.send_response(200)
		self.end_headers()
		self.wfile.write("Ceci est une requête POST")

httpd = SocketServer.TCPServer(("localhost", PORT), HTTPImpl)

print "Disponible sur le port ", PORT
httpd.serve_forever()
{% endhighlight %}

Fonctionnement de relais
------------------------

Dans le cadre de notre recherche, nous avons eu à apprendre le fonctionnement
d'un relais. Un relais est une composante électronique qui agit un peu comme
un interrupteur c'est-à-dire que nous pouvons fermer ou ouvrir le circuit 
avec un signal digital afin d'alimenter une autre composante nécessitant plus
de voltage.

Comme on le voit ci-dessous, c'est le circuit nécessaire pour contrôler un relais
avec un Arduino. Dans notre cas, la cafetière comprenait déjà le relais ainsi que
le circuit nécessaire pour alimenter l'élément chauffant de la cafetière.

![ArduinoRelay]({{ site.baseurl }}/img/ArduinoRelay.png)
Source: [http://www.arduino.cc/cgi-bin/yabb2/YaBB.pl?num=1293881907](http://www.arduino.cc/cgi-bin/yabb2/YaBB.pl?num=1293881907)

La difficulté a été de relier ce schéma à celui de notre cafetière. Finalement, 
afin de fermer le circuit du relais de la cafetière, nous avons dû alimenter 
la carte Arduino avec la prise DC du Arduino relié à l'alimentation 5V venant
du relais et à la masse du relais. Voici une image de l'assemblage:

![CafetiereRelais]({{ site.baseurl }}/img/CafetiereRelais.png)

Diviseur de tension
-------------------
Afin de trouver une astuce pour mesurer la quantité d'eau dans le récipient 
de la cafetière, nous avons réfléchi à plusieurs solutions. Une d'entre elles
a été de faire un diviseur de tension. Un diviseur de tension est un circuit
électronique permettant de mesurer la tension à l'endroit voulu dans le circuit
c'est-à-dire que nous pouvons mesurer l'effet qu'une résistance a sur la tension
du circuit.

Comme on peut le voir dans le schéma ci-dessous qui représente un diviseur de
tension, il faut relier l'entrée représentée ici par V<sub>out</sub> aux résistances
à mesurer et à une résistance reliée à la masse représentée par V<sub>in</sub>.

![DiviseurTension]({{ site.baseurl }}/img/Voltage_divider.png)

Source [http://it.wikipedia.org/wiki/File:Voltage_divider.svg](http://it.wikipedia.org/wiki/File:Voltage_divider.svg)

Le but était donc d'envoyer du courant dans le fond de la cafetière et de mettre
des résistances en série afin de savoir, selon la résistance mesurée, combien
d'eau il y a dans la cafetière. Les tests que nous avions faits au préalable
nous avaient démontré que cette technique fonctionnait, mais lorsque venu le temps
d'implémenter la technique, nous nous sommes aperçus que la résistance de l'eau
était trop grande pour être capable de voir une variation significative de tension
selon la hauteur de l'eau.

Pull-down
---------
Étant donné que la solution précédente était peu satisfaisante, nous avons
trouvé une autre solution. La première idée que nous avions eue avait été de
mettre des fils à différents emplacements dans l'eau et que lorsque l'eau
atteindrait ces fils, ils recevraient le courant et nous pourrions savoir que
l'eau est rendue à la hauteur du fil. Cependant, les entrées du Arduino
recevaient beaucoup trop de courant résiduel pour avoir une bonne mesure.

La dernière idée que nous avons eue s'inspire de celle-ci. Il s'agit d'employer
le principe d'une résistance « pull-down ». Ce principe part de l'idée que le
courant se dirige toujours vers le chemin le plus facile. Donc, dans le circuit
ci-dessous, lorsque le circuit est ouvert, tout le courant résiduel va dans la
masse. Et lorsque le circuit est fermé, tout le courant va dans l'entrée 
V<sub>out</sub>.

![PullDown]({{ site.baseurl }}/img/Pulldown_Resistor.png)

Source: [http://en.wikipedia.org/wiki/Pull-up_resistor](http://en.wikipedia.org/wiki/Pull-up_resistor)


