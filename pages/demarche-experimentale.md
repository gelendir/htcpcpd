---
title: Démarche expérimentale
layout: default
category: page
---

Démarche expérimentale sur L'arduino
====================================

Programmation d'un microcontrôleur
----------------------------------

Notre démarche expérimentale a commencé en apprennant comment programmer
un microcontrôleur Arduino Duemilanove. Pour ce faire, nous avons
utilisé l'IDE Arduino (à ne pas confondre avec le microntrôleur qui
porte le même nom) fournit sur le site web du fabriquant.

![ArduinoIde]({{ site.baseurl }}/img/arduinoIde.png)

L'IDE permet
de compiler du code C++ ainsi que de téléverser un programme sur la mémoire
non-volatile du microcôntoleur. Cet expérience nous a permis d'apprendre
les points suivants:

 * Un programme Arduino est composé de 2 fonctions : setup() et loop().
 * La fonction setup() permet d'initialiser des variables et de configurer.
 les composantes du microcontrôleur.
 * La fonction loop() boucle continuellement lors de l'éxécution d'un
 programme, un peu de la même manière que "while(true) {}".

Programmation d'une DEL
-----------------------

La 2e expérience fût d'implémenter le "hello world" des systèmes
embarqués, c'est-à-dire coder un programme minimaliste permettant de
faire une démonstration rapide des capacités d'un microcontrôleur.

![ArduinoDel]({{ site.baseurl }}/img/arduinoDel.png)

Nous avons programmé l'Arduino pour allumer et éteindre une DEL en
alterance à un intervale d'une seconde. Cet expérience nous a permis
d'appendre les points suivants :

 * Comment configurer un port pour émettre un signal (mode OUTPUT).
 * Comment allumer et éteindre un signal sur un port digital.
 * Comment utiliser la fonction delay() pour arrêter temporairement.
 l'éxécution d'un programme pendant un certain délai en millisecondes.

Communication par port série
----------------------------

L'arduino utilise un port série émulé à travers la connection USB pour
communiquer avec l'ordinateur externe. À fin de mieux comprendre comment
envoyer et recevoir des données à travers le port série, Nous avons écrit un programme
qui renvoie une chaîne de charactères reçu. Voici un extrait du
programme : 

{% highlight c++ %}

void setup() {

    //Ouvrir le port série et ajuster le "baud-rate"
    Serial.begin(9600);
    //Avertir l'utilisateur que l'arduino est prêt à recevoir des strings
    Serial.println("Booted");
}

String message;

void loop() {

    //Vérification si nous avons reçu des données
    while( Serial.available() ) {

        char in = Serial.read();

        //Debug, vérification des charactères reçus
        Serial.print("Character is ");
        Serial.println(in);

        //Nous utilisons le retour de chariot pour indiquer
        //la fin de la chaîne de charactères
        if( in == '\n' ) {
            Serial.println(message);
            message = "";
        } else {
            //Vu que Serial.read() retourne seulement un
            //charactère à la fois, nous avons besoin de les accumuler
            message.concat( in );
        }

    }

}

{% endhighlight %}

Ce programme nous a permis d'apprendre les points suivants:

 * Le port série fonctionne un peu de la même manière qu'un descripteur de fichier
 * Il est juste possible de lire un charactère à la fois. Il faut donc emmagasiner 
   les charactères temporairement avant de les utiliser.
 * Si Serial.begin() n'est pas appelé, l'arduino ne démarre pas le programme.
 * L'arduino n'emmagasine pas toujours tout les charactères reçus du premier coup. 
   Il faut donc attendre la réception du '\n' avant de traiter la chaîne au complet.

Programmation d'un capteur de lumière
-------------------------------------

À fin de nous aider à comprendre la différence entre un port analogique
et un port digital, nous avons monté un circuit utilisant un capteur de
lumière. Le capteur fait varier la résistance du circuit selon la
quantité de lumière exposé. 

![ArduinoPhotocell]({{ site.baseurl }}/img/arduinoPhotocell.png)

Dans le programme, le port analogique retourne une valeur entre 0 et
1024 pour indiquer le niveau de résistance du circuit. Cet expérience
nous a permis d'appendre les points suivants : 

 * Comment configurer un port pour lire un signal (mode INPUT).
 * Comment utiliser un port analogique.
 * La différence entre un port analogique et un port digital.

Programmation d'un relais
-------------------------

La cafetière utilise un relais pour partir et éteindre l'élément
chauffant utilisé pour bouillir l'eau. À fin de mieux comprendre
son utilisation, nous avons monté un circuit avec un relais que
nous étions capable de contrôler avec l'arduino. Voici un schéma
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

Programmation d'un circuit avec "pull-down"
-------------------------------------------

Programmation d'un circuit à diviseur de tension
------------------------------------------------

Démarche expérimentale sur le serveur web
=========================================

Réception de données sur un port série
--------------------------------------

Réception de requêtes GET, POST
-------------------------------

