Implémentation du protocole HTCPCP
==================================

Installation du Arduino
-----------------------
Pour installer le code Arduino, il suffit de compiler le code via l'IDE Arduino
et de le transférer à l'Arduino à l'aide de l'IDE. L'Arduino doit être en tout
temps connecté lors de la communication avec le service HTCPCPD.

Utilisation du serveur et du client
------------------------------------

### Préalable ###

Le seul préalable pour le serveur HTCPCPD et le client est d'avoir installé
l'interprétateur Python version 2.7.

### Installation ###

Pour l'installation du serveur et du client, vous devez vous rendre dans le 
répertoire htcpcpd en ligne de commande et de rentrer la commande suivante:

	python2 setup.py install

### Utilisation du serveur ###

Pour utiliser le serveur, il suffit de rentrer la commande suivante:
	
	htcpcpd -c htcpcpd.ini

où « htcpcpd.ini » est le fichier de configuration.

Le port par défaut du fichier de configuration est 8000.

La ligne « pidfile » dans le fichier de configuration indique le fichier dans 
lequel le fichier du pid du service sera mis. Il peut être utile afin de tuer
le processus pour arrêter le service.

La ligne « logfile » dans le fichier de configuration est utilisé pour mettre 
les logs du serveur HTCPCPD.

### Utilisation du client ###

Pour utiliser le client, il suffit de rentrer la commande suivante:

	htcpcp-client localhost 8000

où les deux arguments ne sont pas obligatoire. Le premier indique l'adresse du
serveur HTCPCPD et le deuxième le port du serveur.

