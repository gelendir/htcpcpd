---
title: Difficultés rencontrée
layout: default
category: page
---

Difficultés rencontrées
=======================

Notion de base en électronique
------------------------------
Une des premières difficultés que nous avons rencontrées a été que nous n'avions
absolument aucune notion de base en électronique. Donc, lorsque venait le temps
de comprendre comment fonctionnait un circuit, c'était difficile de comprendre
les pourquoi de ce circuit. Cela a donc été une difficulté tout le long du 
projet.

Fonctionnement d'un relais
--------------------------
Une autre difficulté que nous avons eue a été de comprendre comment fonctionne
un relais. Pour cela, nous avons monté un circuit sur un kit d’expérimentation
d'électronique. Nous avons commencé en envoyant le signal au relais à l'aide
des piles et du bouton sur le kit d'expérimentation puis nous les avons 
remplacés par notre Arduino. Voici la photo du circuit sur le kit:

![ArduinoRelaiImage]({{ site.baseurl }}/photos/relay_board_2.jpg)

Fonctionnement du circuit la cafetière
--------------------------------------
Une fois que nous avions compris le fonctionnement d'un relais, nous avions
deux choix: faire fonctionner le relais de la cafetière ou remplacer le circuit 
de la cafetière par un de notre cru. Nous avons choisi la première solution.
Nous avions trois fils qui étaient reliés au relais de la cafetière: un 
envoyant du 5 volt, un qui allait à la masse du relais et un par où nous
devions envoyer le signal digital. 

Au début, nous avons essayé d'envoyer seulement le signal digital sans se 
préoccuper des deux autres, mais ça ne fonctionnait pas. Nous nous sommes 
aperçus que nous devions nous servir du courant 5 volts ainsi que de la masse du 
relais afin de fermer le circuit et de l'activer. Finalement, afin de fermer le
circuit du relais de la cafetière, nous avons dû alimenter la carte Arduino 
avec la prise DC du Arduino relié à l'alimentation 5V venant du relais et à la 
masse du relais. Voici une image de l'assemblage:

![CafetiereRelais]({{ site.baseurl }}/img/CafetiereRelais.png)

Mesure de la quantité d'eau
---------------------------
La dernière difficulté majeure que nous avons eue a été d'être capable de 
mesurer la quantité d'eau restante dans la cafetière. 

La première solution que nous avions envisagée a été de mettre des fils dans le
récipient d'eau à différentes hauteurs avec un fil de courant dans le fond de 
la cafetière, mais cette solution ne fonctionnait pas à cause que courant 
résiduel sur les entrées du Arduino. 

La deuxième solution envisagée a été de mettre des résistances en série
avec un diviseur de tension, mais il s'est avéré que la résistance de l'eau
nuisait à la capture analogique de la résistance.

La troisième et dernière solution a été de mettre une résistance en « pull-down »
et de regarder si l'entrée analogique du Arduino retournait 0 ou un autre nombre.
Cette solution s'est avérée la meilleure solution.

