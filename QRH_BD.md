% QRH : Base de données
% Damien GABRIEL
% Version : 1 | Juillet 2016

[![Built with Spacemacs](https://cdn.rawgit.com/syl20bnr/spacemacs/442d025779da2f62fc86c2082703697714db6514/assets/spacemacs-badge.svg)](http://github.com/syl20bnr/spacemacs)

***
# Installation de PostgreSQL / PostGIS #

## Linux (Manjaro) ##

Pour installer PostgreSQL et PostGIS sur Manjaro, il faut installer :

~~~ {include="./fichiers/bash/postgresql_install.txt" .bash}
Fichier d'installation pour PostgreSQL / PostGIS sur Manjaro
~~~

On peut aussi installer les paquets suivants pour améliorer le travail avec les bases de données :

~~~ {include="./fichiers/bash/postgresql_install_opt.txt" .bash}
Fichier d'installation pour PostgreSQL / PostGIS sur Manjaro (Paquets optionnels conseillés)
~~~


### Initialisation du Cluster ###

```bash
sudo -i -u postgres
initdb --local $LANG -E UTF8 -D '/var/lib/postgres/data'
```

### Démarrage et arrêt de PostgreSQL ###

```bash
systemctl start postgresql
systemctl stop postgresql
```

Pour que PostgreSQL soit actif à tous les redemarrages on peut aussi utiliser :

```bash
systemctl enable postgresql
```


## Ajout des utilisateurs ##

Par défaut, l'installation de PostgreSQL n'a que l'utilisateur *postgres*. C'est le seul utilisateur qui peut se connecter a *psql*.

La première étape pour véritablement utiliser PostgreSQL est donc de créer de nouveau utilisateur.

Ici on va créer un utilisateur *lambda* autorisé à créer des bases.

On commence par se connecter à psql : [^4]

```bash
su - postgres
psql
```

[^4]: La démarche peut être légèrement différente en fonction des *OS* utilisés. Sous Windows, je pense qu'il suffit de taper directement *psql*

Une fois dans le shell de psql :

```shell
CREATE USER lambda;
ALTER ROLE lambda WITH CREATEDB;
ALTER ROLE lambda WITH ENCRYPTED PASSWORD 'omega';
```

### Création d'une base de donnée ###

Pour créer une base de donnée on utilise :

``` bash
created *nom_de_la_base*
```

On peut alors ce connecter avec l'utilisateur *lambda* à la base *db* en utilisant :

``` bash
psql -U lambda -d bd
```

Le shell de PostgreSQL doit affcher sur la première ligne le nom de la base, donc ici *db*.

# Utilisation de PostgreSQL et PostGIS #

## Création du base de données spatiale ##

Pour créer une base de données spatiale avec PostGIS il faut utiliser les types *geography* si on veut faire des calculs précis (ie sur le geoïde en WGS84).

**Pour utiliser PostGIS il faut créer l'extension *postgis* dans la base de données**

~~~ {include="./fichiers/SQL/create_spatial_db.sql" .sql}
Commandes SQL pour créer une base de données spatiale avec PostgreSQL et PostGIS
~~~

## Insertion de données ##

~~~ {include="./fichiers/SQL/insert_spatial_db.sql" .sql}
Commandes SQL pour créer une base de données spatiale avec PostgreSQL et PostGIS
~~~

**ATTENTION** Comme le montre les commandes au-dessus, l'ordre des coordonnées doit d'abord être **E/W** PUIS **N/S** 

## Calcul de navigation ##

La fonction **ST_AZIMUTH** permet de calculer des caps en dégrés.

La fonction **ST_DISTANCE** permet de calculer des distances en **mètres**.

Dans tous les cas il faut **faire attention aux modèles utilisés !**. Par exemple, pour de la navigation aérienne il est nécessaire d'être en WGS84 (modèle du GPS).

~~~ {include="./fichiers/SQL/hdg_distance_spatial_db.sql" .sql}
Commandes SQL pour créer une base de données spatiale avec PostgreSQL et PostGIS
~~~

Ci-dessous le résultat de la requête précédente :

```shell
  Distance (km)  |       Cap        
-----------------+------------------
 627.09856039227 | 340.544493840961
(1 row)
```
Dans l'autre sens Paris Orly (LFPO) vers Marseille Provence (LFML) on obtient bien le réciproque :

```shell
  Distance (km)  |       Cap       
-----------------+-----------------
 627.09856039227 | 158.49973504052
(1 row)
```


## Requête spatiales ##

### Affichage des coordonnées sous forme de texte ###

~~~ {include="./fichiers/SQL/show_coordo_text.sql" .sql}
Commandes SQL pour créer une base de données spatiale avec PostgreSQL et PostGIS
~~~

Le résultat de la requête est :
```shell
        st_astext        
-------------------------
 POINT(1.52389 48.45889)
(1 row)
```

### Trouver les points les plus proches d'un point d'intérêt ###

~~~ {include="./fichiers/SQL/nearest_point.sql" .sql}
Commandes SQL pour créer une base de données spatiale avec PostgreSQL et PostGIS
~~~

Le résultat de la requête est :

```shell
 nom  |       coordonnees       |   distance_km   
------+-------------------------+-----------------
 LFML | POINT(5.215 43.43667)   | 310.09213298947
 LFOR | POINT(1.52389 48.45889) | 386.22555702069
(2 rows)
```
