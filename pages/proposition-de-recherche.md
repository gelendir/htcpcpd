---
title: Proposition de recherche
layout: default
category: page
---

Automatisation du contrôle d’une cafetière
==========================================

## 1 Le sujet ##
En 1999, l’IETF a publié une RFC définissant un nouveau protocole permettant de contrôler une cafetière via un service web. Ce protocole s’appelle le HTCPCP (HyperText Coffee Pot Control Protocol). Ce protocole augmente les spécifications du protocole HTTP avec nouveaux détails d’implémentation pour faciliter le contrôle d’une cafetière

Le but de cette recherche est de vérifier la faisabilité d’implémentation du protocole HTCPCP. Pour ce faire, nous aurons besoin de diviser la recherche en 2 parties. La première partie consistera à implémenter le serveur Web qui recevra les requêtes. La seconde partie consistera à vérifier si l’interfaçage avec la cafetière est possible et trouver les possibilités de contrôle de la cafetière.

Ce développement permettrait aux professeurs du département d’informatique du Cégep de Ste-Foy nécessitant du carburant le matin pour se réveiller d’automatiser la préparation du café le matin. Ainsi, apporter le bon café à la personne au bon moment.

Ce projet peut permettre d’avertir les consommateurs de café lorsque le breuvage est prêt, évitant ainsi la perte de temps dû à l’attente et à la préparation du café. De plus, lorsqu’une cafetière est utilisée par plusieurs personnes, l’organisation de la préparation du café sera simplifiée.

Nous avons des connaissances du protocole HTTP ainsi que dans l’installation de serveurs web. De plus, nous avons des connaissances avec les langages de programmation les plus utilisés pour de la programmation embarquée (C/C++). 


## 2 Les enjeux ##

Ce sujet est encore d’actualité, car la consommation de café est de plus en plus élevée dans notre société. Par ce fait, le besoin d’automatisation de ce processus est ressenti. L’automatisation permettrait d’éviter des manipulations hasardeuses de la cafetière et de réduire le temps nécessaire à la préparation du café.

Lors de cette recherche, nous aurons besoin d’acquérir des connaissances au niveau de l’électronique et de la programmation des systèmes embarqués. Nous aurons aussi besoin d’améliorer nos connaissances en programmation de processus parallèles et d’accès concurrents au niveau du serveur web et de la communication avec le système embarqué. 

Cette recherche permettra de réduire le temps nécessaire à la préparation du café permettant aux personnes de vaquer à d’autres occupations plus importantes. Elle permet aussi de simplifier le processus de préparation du café.

Les efforts de cette recherche pourront servir à de futurs projets d’automatisation des appareils ménagers et culinaires. Ainsi, nous pouvons espérer que le nombre de tâches répétitives nécessaires à la préparation des aliments sera réduit.

La motivation pour cette recherche vient du besoin d’une implémentation libre d’une spécification prometteuse, dans notre cas le protocole HTCPCP. Le web est en expansion constante et de nouveaux domaines d’application sont découverts tous les jours. L’implémentation d’un protocole supplémentaire contribuera à l’évolution du web. De plus, les défis technologiques et techniques de cette recherche nous intriguent.

## 3 Les objectifs ##

* Mettre en marche la cafetière lors de la réception d’une commande (sur demande)
* Chauffer l’eau de la cafetière
* Détecter la présence d’eau dans la cafetière, avant de la chauffer
* Détecter la présence d’un réceptacle pour le café
* Détecter la quantité d’eau restante dans la cafetière
* Détecter quand l’eau est à une température adéquate
* Procéder à l’infusion du café
* Notifier l’utilisateur lorsque le café est prêt
* Notifier l’utilisateur des étapes nécessaires pour préparer le café

## 4 L’expérimentation ##

La recherche sera menée à l’aide d’outils d’expérimentation, c’est-à-dire le développement de prototypes itératifs permettant de confirmer la faisabilité du projet. Le but de ces prototypes est d’approfondir nos connaissances du fonctionnement des systèmes embarqués. Une fois que les prototypes sont rendus à un niveau considéré comme satisfaisant, nous pourrons envisager une utilisation officielle du protocole sur internet.

### 4.1 Apprentissage ###

Un apprentissage de la programmation embarqué sur un système Arduino et de la programmation par port série seront nécessaires à la recherche. Également, une base d’électronique sera nécessaire à la mise en œuvre du projet et devra être apprise. 

La lecture de la RFC du protocole HTCPCP est aussi un préalable au projet final de la recherche étant donné que cette RFC donne les spécifications de communication réseau avec la cafetière.

### 4.2 Développement du serveur web ###

Il sera nécessaire de développer le serveur web. Ce serveur sera responsable d’implémenter le protocole HTCPCP, de l’interpréter et d’acheminer les commandes au module de gestion de la cafetière. Le serveur devra valider les requêtes HTCPCP reçues des clients pour vérifier la conformité à la spécification. Dans le cas qu’une requête s’avère invalide, le serveur web devra retourner un code d’erreur semblable à ceux utilisés par le protocole HTTP.

### 4.3 Développement du logiciel embarqué ###

Nous devons développer un logiciel embarqué sur un système embarqué de type Arduino permettant d’interagir avec les diverses composantes de la cafetière. Chacune des composantes électroniques de la cafetière devra être reliée à la carte de contrôle qui servira d’intermédiaire au module de gestion de la cafetière. De plus, il sera nécessaire de découvrir les signaux électriques à envoyer à la cafetière pour contrôler les composantes. Le système embarqué sera utilisera un algorithme d’états pour gérer la bonne préparation du café. De plus, le système devra valider certaines composantes pour chacun des états, notamment la présence d’eau, la température, etc. (Voir section 3, les objectifs)

### 4.4 API de contrôle du système embarqué ###

Un module de communication entre le serveur web et la cafetière servira d'intermédiaire pour transmettre les commandes reçues sur le web au système embarqué. Ce module devra fournir un API simple permettant de contrôler la cafetière informatiquement. Le module validera si la présence du système embarqué et la gestion des erreurs reçues.

## 5 Les limites ##

Bien que le processus de préparation du café soit simplifié, une intervention est toutefois nécessaire. L’eau et les grains de café devront être préalablement mis dans la cafetière avant la préparation. Cependant il est toujours possible de préparer la cafetière à un moment ultérieur, par exemple préparer la cafetière le soir lorsqu’on prévoit prendre du café le matin d’après. De plus, le café devra être servi à l’aide d’une intervention humaine. 

Dû à contraintes de temps, l’ajout de lait ne sera pas implémenté comme spécifié dans le protocole HTCPCP.

Seule la préparation du café sera prise en charge lors de cette recherche.

## 6 Les incertitudes ##

À ce stade de la recherche nous ne sommes pas certains de la meilleure approche pour placer tous les détecteurs comme énumérés dans la section 3 (les objectifs). Il sera nécessaire d’expérimenter plusieurs types de détecteurs et déterminer lesquelles sont le plus appropriés à notre contexte.

Il y a aussi une incertitude au niveau du fonctionnement interne d’une cafetière au niveau des composantes électroniques. Une analyse préalable des mécanismes internes de la cafetière sera nécessaire. Nous avons déjà certaines informations de disponibles sur le lien suivant : [Wikipédia: Coffeemaker](http://en.wikipedia.org/wiki/Coffeemaker)
 
## 7 Les ressources ##

Les ressources suivantes seront utilisées lors de la recherche :

* Carte embarqué Arduino (modèle Duelimanove)
* IDE Arduino version 1.0
* Compilateur C/C++ Arduino version 4.5
* Python 2, version 2.7
* Cafetière électronique
* Détecteurs optiques à résistance variable
* Fil USB pour relier l’Arduino au serveur web
* Résisteurs et fils divers pour les connexions entre l’Arduino et la cafetière

## 8 La planification de l’expérimentation ##

| Périodes | Temps prévu | Descriptions des tâches à réaliser | Responsable |
|----------|-------------|------------------------------------|-------------|
| 19 janv. | 4h          | Recherche documentaire HTCPCP, Recherche documentaire Arduino | HTCPCP : FP, Arduino : GES |
| 21 janv. | 3h | Démontage de  la cafetière, Expérimentation des senseurs | Cafetière : FP, Senseurs : GES |
| 23 janv. | 4h | Expérimentation branchage Arduino sur Cafetière| FP et GES |
| 25 janv. | 4h | Essai de contrôle de la cafetière | FP et GES |
| 26 janv. | 4h | Programmation de fonctionnalités embarquées de la cafetière | FP et GES |
| 28 janv. | 4h | Programmation de fonctionnalités embarquées de la cafetière | FP et GES |
| 30 janv. | 4h | Programmation de l’API de gestion de la cafetière | FP et GES |
| 1 fév.   | 4h | Programmation de l’API de gestion de la cafetière | FP et GES |
| 2 fév.   | 4h | Programmation de l’API de gestion de la cafetière | FP et GES |
| 4 fév.   | 4h | Programmation du Serveur Web | FP et GES |
| 6 fév.   | 4h | Programmation du Serveur Web | FP et GES |
| 8 fév.   | 4h | Mise au point du système embarqué | FP et GES |
| 9 fév.   | 4h | Validation du système | FP et GES |
| 11 fév.  | 4h | Analyse et publication des résultats | FP et GES |
| 16 fév.  | 5h | Présentation | FP et GES |
