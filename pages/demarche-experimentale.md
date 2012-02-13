---
title: Démarche expérimentale
layout: default
category: page
---

Démarche expérimentale sur l'Arduino
====================================

Programmation d'un microcontrôleur
----------------------------------

Notre démarche expérimentale a commencé en apprenant comment programmer
un microcontrôleur Arduino Duemilanove. Pour ce faire, nous avons
utilisé l'IDE Arduino (à ne pas confondre avec le microcontrôleur qui
porte le même nom) fourni sur le site web du fabricant.

![ArduinoIde]({{ site.baseurl }}/img/arduinoIde.png)

L'IDE permet
de compiler du code C++ ainsi que de téléverser un programme sur la mémoire
non volatile du microcontrôleur. Cette expérience nous a permis d'apprendre
les points suivants:

 * Un programme Arduino est composé de 2 fonctions : setup() et loop().
 * La fonction setup() permet d'initialiser des variables et de configurer.
 les composantes du microcontrôleur.
 * La fonction loop() boucle continuellement lors de l'exécution d'un
 programme, un peu de la même manière que "while(true) {}".

Programmation d'une DEL
-----------------------

La 2e expérience fut d'implémenter le "hello world" des systèmes
embarqués, c'est-à-dire coder un programme minimaliste permettant de
faire une démonstration rapide des capacités d'un microcontrôleur.

![ArduinoDel]({{ site.baseurl }}/img/arduinoDel.png)

Nous avons programmé l'Arduino pour allumer et éteindre une DEL en
alternance à un intervalle d'une seconde. Cette expérience nous a permis
d'appendre les points suivants :

 * Comment configurer un port pour émettre un signal (mode OUTPUT).
 * Comment allumer et éteindre un signal sur un port digital.
 * Comment utiliser la fonction delay() pour arrêter temporairement.
 l'exécution d'un programme pendant un certain délai en millisecondes.

Communication par port série
----------------------------

L'Arduino utilise un port série émulé à travers la connexion USB pour
communiquer avec l'ordinateur externe. À fin de mieux comprendre comment
envoyer et recevoir des données à travers le port série, nous avons écrit un programme
qui renvoie une chaîne de caractères reçus. Voici un extrait du
programme : 

{% highlight c++ %}

void setup() {

    //Ouvrir le port série et ajuster le "baud-rate"
    Serial.begin(9600);
    //Avertir l'utilisateur que l'Arduino est prêt à recevoir des strings
    Serial.println("Booted");
}

String message;

void loop() {

    //Vérification si nous avons reçu des données
    while( Serial.available() ) {

        char in = Serial.read();

        //Debug, vérification des caractères reçus
        Serial.print("Character is ");
        Serial.println(in);

        //Nous utilisons le retour de chariot pour indiquer
        //la fin de la chaîne de caractères
        if( in == '\n' ) {
            Serial.println(message);
            message = "";
        } else {
            //Vu que Serial.read() retourne seulement un
            //caractère à la fois, nous avons besoin de les accumuler
            message.concat( in );
        }

    }

}

{% endhighlight %}

Ce programme nous a permis d'apprendre les points suivants:

 * Le port série fonctionne un peu de la même manière qu'un descripteur de fichier
 * Il est juste possible de lire un caractère à la fois. Il faut donc emmagasiner 
   les caractères temporairement avant de les utiliser.
 * Si Serial.begin() n'est pas appelé, l'Arduino ne démarre pas le programme.
 * L'arduino n'emmagasine pas toujours tous les caractères reçus du premier coup. 
   Il faut donc attendre la réception du '\n' avant de traiter la chaîne au complet.

Programmation d'un capteur de lumière
-------------------------------------

À fin de nous aider à comprendre la différence entre un port analogique
et un port digital, nous avons monté un circuit utilisant un capteur de
lumière. Le capteur fait varier la résistance du circuit selon la
quantité de lumière exposé. 

![ArduinoPhotocell]({{ site.baseurl }}/img/arduinoPhotocell.png)

Dans le programme, le port analogique retourne une valeur entre 0 et
1024 pour indiquer le niveau de résistance du circuit. Cette expérience
nous a permis d'appendre les points suivants : 

 * Comment configurer un port pour lire un signal (mode INPUT).
 * Comment utiliser un port analogique.
 * La différence entre un port analogique et un port digital.

Programmation d'un relais
-------------------------

La cafetière utilise un relais pour partir et éteindre l'élément
chauffant utilisé pour bouillir l'eau. À fin de mieux comprendre
son utilisation, nous avons monté un circuit avec un relais que
nous étions capables de contrôler avec l'Arduino. Voici un schéma
du circuit :

![ArduinoRelaiSchema]({{ site.baseurl }}/img/arduinoRelaySchema.jpg)

Puis voici une photo du circuit monté :

![ArduinoRelaiImage]({{ site.baseurl }}/photos/relay_board_2.jpg)

Le circuit nous a permis d'apprendre les points suivants :

 * Le principe de base du fonctionnement d'un relai
 * Comment envoyer une source de courant plus puissante à un autre
 appareil
 * Comment allumer et éteindre un relai

Programmation d'un circuit utilisant de l'eau
---------------------------------------------

Lors de notre recherche, nous avons eu besoin de déterminer quelles
approches étaient le mieux adaptées pour mesurer la quantité d'eau restant
dans la cafetière. Une des approches que nous avons essayées consistait à
utiliser l'eau pour former un circuit électrique. Vu que l'eau est
conducteur d'électricité, il serait envisageable de savoir à quel niveau
l'eau était rendue en plaçant plusieurs circuits et en mesurant lesquels
conduisait de l'électricité.  Cette expérience nous a permis d'appendre
les points suivants :

 * Cette approche pour mesurer l'eau est une solution envisageable
 * Désavantage : Il faudrait un port digital pour chaque circuit
 installé dans l'eau
 * Découverte : même après avoir retiré l'eau il reste encore de
 l'électricité résiduelle dans le circuit, ce qui peut fausser les
 résultats de lecture

Programmation d'un circuit à diviseur de tension
------------------------------------------------

La 2e approche retenue pour mesurer la quantité d'eau était d'utiliser un
circuit à diviseur de tension. Voici une image du circuit que nous avons
utilisée pour comprendre le concept :

![ArduinoVoltageDivider]({{ site.baseurl }}/img/arduinoVoltageDivider.png)

L'hypothèse était qu'en utilisant un
circuit en série, plus le niveau d'eau augmente et plus la résistance du
circuit serait élevée. De cette manière, il serait possible de mesurer la
quantité d'eau avec un port analogique et en mesurant le niveau de résistance
pour des quantités d'eau prédéterminées.

Cette expérience nous a permis d'apprendre les points suivants :

 * L'eau a une plus grande résistance que des fils de cuivre
 * La résistance de l'eau varie légèrement selon sa température
 * Après environ 8 tasses d'eau, la variation de résistance est beaucoup
 plus petite

Programmation d'un circuit avec "pull-down"
-------------------------------------------

La découverte d'électricité résiduelle dans certains circuits était un
facteur important qui faussait plusieurs de nos résultats de lecture.
Nous avons donc cherché un moyen d'éliminer ce problème. La solution
retenue fut d'utiliser un circuit de type "pull-down". Voici une image du
circuit que nous avons utilisée pour faire nos expérimentations :

![ArduinoPullDown]({{ site.baseurl }}/img/arduinoPullDown.png)

Ce circuit nous a permis d'avoir des résultats beaucoup plus précis
lorsque nous avons implémenté les divers circuits de la cafetière. 

Cette expérience nous a permis d'apprendre les points suivants : 

 * L'électricité "évacue" par le circuit pull-down lorsque le circuit
 principal est déconnecté
 * Un pull-down est souvent nécessaire pour éviter de capter
 l'électricité dans l'air ambiant et fausser les résultats, aussi connu
 sous le nom de "bruit statique"


Démarche expérimentale sur le serveur web
=========================================

Réception de données sur un port série
--------------------------------------

Le moyen de communication principale de l'Arduino est à travers un port
série. Nous avons donc eu besoin de trouver un moyen d'envoyer et de
transmettre des données dans le langage de programmation python étant
donnée que le serveur web serait codé dans ce langage.
Après quelques recherches, nous
avons décidé d'utiliser le module python-pyserial pour contrôler un port
série. Pour mieux comprendre le fonctionnement de ce module, nous avons
implémenté un petit programme similaire à celui de l'Arduino (Voir la
section [Communication par port série](#communication_par_port_srie)),
c'est-à-dire un programme qui envoie une chaîne de caractères et
affiche à l'écran le résultat reçu. Voici un extrait de code :

{% highlight python %}

import serial

#Ouvrir le port série de l'arduino
ser = serial.Serial('/dev/ttyUSB0')  

#Nous envoyons une chaîne de caractère à l'arduino
ser.write("hello world")

#L'arduino est censé nous renvoyer la même chaîne de caractère
print ser.readline()

#Fermeture du port
ser.close()

{% endhighlight %}

Ce programme nous a permis d'apprendre les points suivants :

 * Comment utiliser un port série en python
 * L'envoi et la réception de données agissent de la même manière qu'un
 descripteur de fichier (les fonctions read and write)
 * Un seul programme peut accéder au port série à la fois

Réception de requêtes BREW, GET, POST
-------------------------------------

Les spécifications du protocole HTCPCP ajoutent des verbes
d'action pour contrôler la cafetière qui ne sont pas reconnus par les
serveurs HTTP traditionnels. Nous avons donc eu besoin de trouver un
moyen d'ajouter une implémentation pour ces nouveaux verbes tout en
restant compatible avec HTTP. Après quelques recherches, nous avons
découvert que le module SimpleHTTPServer de python permet de redéfinir
les verbes d'action de manière arbitraire en redéfinissant les
fonctions do_VERBE() de manière appropriée. Voici un extrait de code :

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

    def do_BREW(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write("Ceci est une requête BREW")

httpd = SocketServer.TCPServer(("localhost", PORT), HTTPImpl)

print "Disponible sur le port ", PORT
httpd.serve_forever()_

{% endhighlight %}

Cette expérimentation nous a permis d'apprendre les points suivants :

 * Comment intercepter les requêtes web venant d'un navigateur
 * Comment envoyer une réponse au navigateur

Devis technique des outils
==========================

Voici une liste non exhaustive des outils que nous avons utilisés :

Arduino IDE
-----------

Version utilisée : 1.0

Environnement de programmation utilisé pour développer le code pour 
l'arduino ainsi que de le téléverser sur la mémoire non volatile.

Carte Arduino
-------------

Modèle : Duemilanove (2009)

Microcontrôleur à circuit imprimé qui peut être programmé avec L'IDE.
Nous a permis de vérifier nos hypothèses et de tester les circuits que 
nous avons montés.

Python
------

Version utilisée : 2.7

Langage de programmation dynamique interprété. Utilisé pour faire les
tests de communication avec le port série et implémenter le serveur web.

Le module SimpleHTTPServer est inclus par défaut avec le langage. Le module
python-pyserial est disponible sur le site web suivant : http://pyserial.sourceforge.net

Breadboard
----------

Dispositif qui permet de faire du prototypage rapide de circuits électroniques
à l'aide de branchements avec des fils de cuivre.

Capteur de lumière
------------------

Cellule photosensitive qui fait varier la résistance d'un circuit selon la 
quantité de lumière qui est exposée sur la cellule.

Autres composantes
------------------

 * Fils de cuivre de longueur variable
 * Résistances (1K, 2K, 4.7K)
 * Câble USB
 * De l'eau

Code source
===========

Voici le code source de tous les programmes que nous avons utilisés 
pour chacune de nos expérimentations :

 * [Programmation d'une DEL]({{ site.baseurl }}/examples/programmationDel.ino)
 * [Communication par port série]({{ site.baseurl }}/examples/portSerie.ino)
 * [Capteur de lumière]({{ site.baseurl }}/examples/capteurLumiere.ino)
 * [Programmation d'un relais]({{ site.baseurl }}/examples/exempleRelais.ino)
 * [Circuit utilisant de l'eau]({{ site.baseurl }}/examples/circuitEau.ino)
 * [Circuit à diviseur de tension]({{ site.baseurl }}/examples/diviseurTension.ino)
 * [Circuit pull-down]({{ site.baseurl }}/examples/pullDown.ino)
 * [Port série python]({{ site.baseurl }}/examples/portSerie.py)
 * [Requêtes HTCPCP]({{ site.baseurl }}/examples/serveurHTCPCP.py)
