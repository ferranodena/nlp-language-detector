# Pràctica 1 PLH: Detecció d'idiomes

## 0. Taula de Continguts

- [Pràctica 1 PLH: Detecció d'idiomes](#pràctica-1-plh-detecció-didiomes)
  - [0. Taula de Continguts](#0-taula-de-continguts)
  - [1. Introducció](#1-introducció)
  - [2. Dades del problema](#2-dades-del-problema)
  - [3. Preprocessament](#3-preprocessament)
  - [4. Implementació dels models](#4-implementació-dels-models)
    - [4.1 Lidstone Smoothing](#41-lidstone-smoothing)
      - [4.1.2 Anàlisi dels resultats](#412-anàlisi-dels-resultats)
    - [4.2 Segon Smoothing](#42-segon-smoothing)
      - [4.2.2 Anàlisi dels resultats](#422-anàlisi-dels-resultats)

## 1. Introducció

## 2. Dades del problema

## 3. Preprocessament

Per a preprocessar, agafem el contingut original de cada document de text i se sotmet a un rentat de cara per uniformar-lo. Això implica treure tots els números, convertir totes les lletres a minúscules i endreçar els espais perquè no n'hi hagi de sobrers entre paraules o al principi i al final del text. A més, s'aprofita per estandarditzar la separació entre les frases, canviant els salts de línia convencionals per un format específic, un doble espai, que facilita el seu tractament posterior. Això es fa així perquè el model que es construirà més endavant treballarà amb trigrames, i aquesta forma de separar les frases permet que els trigrames no es vegin afectats per espais innecessaris, mantenint la coherència en l'anàlisi de les seqüències de caràcters.

Un cop els textos estan nets, comença la segona fase, que consisteix a repartir el material perquè el model pugui aprendre i, posteriorment, ser examinat. Per fer-ho de manera justa i representativa, el codi agafa totes les frases de cada idioma del conjunt de train, les remena a l'atzar i les talla en dos blocs: un gran que conté el vuitanta per cent de la informació i un de més petit amb el vint per cent restant. Això és així perquè en el conjunt de dades donat originalment, les dades del test estavem presents al 100% en el conjunt d'entrenament donat. Doncs per evitar que el model aprengui a reconèixer les frases del test, es fa aquesta divisió, de manera que el model només veu el bloc gran durant l'entrenament i el bloc petit es reserva per avaluar la seva capacitat de generalització.

## 4. Implementació dels models

### 4.1 Lidstone Smoothing

parlar del refinament del lambda

#### 4.1.2 Anàlisi dels resultats

### 4.2 Segon Smoothing

#### 4.2.2 Anàlisi dels resultats
