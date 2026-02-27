<style>
/* Estils globals del document */
body {
  font-family: Helvetica, Arial, sans-serif;
  font-size: 9pt;
  text-align: justify;
  line-height: 1.4;
}

/* Paràgrafs justificats */
p {
  text-align: justify;
  font-size: 9pt;
}

/* Estils per a les llistes amb la mateixa mida que el text normal */
ul, ol, code {
  font-size: 9pt;
  line-height: 1.4;
}

li {
  font-size: 9pt;
  line-height: 1.4;
}

/* Títols més petits */
h1 {
  font-size: 13pt;
  text-align: left;
}

h2 {
  font-size: 12pt;
  text-align: left;
  font-weight: bold;
}

h3 {
  font-size: 11pt;
  text-align: left;
  font-weight: bold;
}

h4 {
  font-size: 9pt;
  text-align: left;
}

h5{
  font-size: 9pt;
  text-align: left;
  text-decoration: underline;
}

/* CORRECCIONS PER A BLOCS DE CODI */
pre {
  max-width: 100%;
  overflow-x: auto;
  white-space: pre-wrap;
  word-wrap: break-word;
  overflow-wrap: break-word;
  background-color: #f5f5f5;
  padding: 0.5rem;
  border: 1px solid #ddd;
  border-radius: 3px;
  font-size: 8pt;
  line-height: 1.4;
  min-width: 0;
}

code {
  overflow-wrap: break-word;
  word-wrap: break-word;
  word-break: break-word;
  white-space: pre-wrap;
}

/* Contenidor principal */
.image-row {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 1rem;       /* Espai entre imatges */
  margin-top: 1rem;
  margin-bottom: 1rem;
  align-items: flex-start;
  width: 100%;
}

/* MODIFICAT: Reduïm la base (flex-basis) a 180px perquè hi capiguin 3 en una fila */
.image-column {
  flex: 1 1 180px; /* Abans 280px. Amb 180px, 3 imatges sumen ~540px + marges, que hi cap perfecte */
  max-width: 320px; /* Mida màxima per evitar que es facin gegants si n'hi ha poques */
  display: flex;
  flex-direction: column;
  align-items: center;
  box-sizing: border-box;
}

/* Regla específica: Si només hi ha UNA imatge, la deixem ser més gran */
.image-row:has(.image-column:only-child) .image-column {
  max-width: 480px;
  flex: 0 1 auto;
}

/* Imatges */
.image-column img {
  width: 100%;
  max-height: 280px; /* Limitem l'alçada */
  height: auto;
  display: block;
  object-fit: contain;
}

/* Peu de foto */
.image-column .caption {
  margin-top: 0.5rem;
  font-size: 8pt;
  text-align: center;
  color: #555;
  width: 100%;
}

/* ============================================
    CONTENIDOR GRID 2x2 PER A IMATGES
    ============================================ */
.image-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 0.8rem;
  margin-top: 1rem;
  margin-bottom: 1rem;
  width: 100%;
  max-width: 720px;
  margin-left: auto;
  margin-right: auto;
}

/* Cada cel·la del grid */
.image-grid .grid-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  box-sizing: border-box;
}

/* Imatges dins del grid 2x2 */
.image-grid .grid-item img {
  width: 100%;
  max-width: 360px;
  max-height: 320px;
  height: auto;
  display: block;
  object-fit: contain;
}

/* Peu de foto per a cada imatge del grid */
.image-grid .grid-item .caption {
  margin-top: 0.5rem;
  font-size: 8pt;
  text-align: center;
  color: #555;
  width: 100%;
}

/* Peu de figura general (opcional, per sota de tot el grid) */
.image-grid-caption {
  margin-top: 0.8rem;
  font-size: 8pt;
  text-align: center;
  color: #555;
  font-style: italic;
}

/* Estil per a la separació de pàgines en PDF */
.page-break {
  page-break-before: always;
  break-before: page;
}

/* Bloc imatge-esquerra / text-dreta */
.media-row {
  display: flex;
  gap: 1.5rem;
  align-items: flex-start;
  margin: 1rem 0;
  min-width: 0;
}

.media-image {
  flex: 0 0 38%;
  max-width: 240px;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.media-image img {
  width: 100%;
  height: auto;
  display: block;
}

.media-image .caption {
  margin-top: 0.5rem;
  font-size: 8pt;
  text-align: center;
  color: #555;
}

.media-text {
  flex: 1 1 0;
  min-width: 240px;
}

/* ============================================
    CONTENIDOR DE TAULES AMB PEU DE TAULA
    ============================================ */
.table-container {
  width: 100%;
  margin: 1.5rem 0;
  overflow-x: auto;
  page-break-inside: avoid;
}

/* Estils per a les taules */
.table-container table {
  width: 100%;
  max-width: 100%;
  border-collapse: collapse;
  font-size: 7pt;
  margin: 0 auto;
  background-color: #fff;
}

/* Capçalera de taula */
.table-container thead {
  background-color: #e0e0e0;
  font-weight: bold;
}

.table-container th {
  padding: 8px 6px;
  text-align: center;
  border: 1px solid #888;
  font-size: 7pt;
}

/* Files de dades */
.table-container td {
  padding: 6px 5px;
  text-align: center;
  border: 1px solid #aaa;
  font-size: 7pt;
}

.table-container td code {
  font-size: 7pt;
}

/* Files alternades (zebra striping) */
.table-container tbody tr:nth-child(even) {
  background-color: #f5f5f5;
}

/* Peu de taula (caption) */
.table-container .table-caption {
  margin-top: 0.5rem;
  font-size: 8pt;
  text-align: center;
  color: #555;
  font-style: italic;
}

/* Estil alternatiu: caption sobre la taula */
.table-container .table-title {
  margin-bottom: 0.5rem;
  font-size: 9pt;
  text-align: center;
  font-weight: bold;
  color: #333;
}

/* Millores per a impressió/PDF */
@media print {
  .table-container {
    page-break-inside: avoid;
  }

  .table-container table {
    border: 1px solid #000;
  }

  .table-container th,
  .table-container td {
    border: 1px solid #666;
  }

  .image-column {
    page-break-inside: avoid;
  }

  /* Límits més restrictius per a PDF */
  .image-column img {
    max-height: 280px;
  }

  .image-row:has(.image-column:only-child) .image-column img {
    max-height: 360px;
  }

  /* Grid 2x2 en impressió */
  .image-grid {
    page-break-inside: avoid;
  }

  .image-grid .grid-item img {
    max-height: 280px;
  }

  pre {
    page-break-inside: avoid;
    overflow: visible;
    white-space: pre-wrap;
  }
}

@page {
  @bottom-center {
    content: "Pàgina " counter(page) " de " counter(pages);
    font-size: 8pt;
    color: #555;
    font-family: Helvetica, Arial, sans-serif;
  }
}
</style>

# Pràctica 1 PLH: Detecció d'idiomes

## 0. Taula de Continguts

- [Pràctica 1 PLH: Detecció d'idiomes](#pràctica-1-plh-detecció-didiomes)
  - [0. Taula de Continguts](#0-taula-de-continguts)
  - [1. Introducció](#1-introducció)
  - [2. Dades del problema](#2-dades-del-problema)
  - [3. Preprocessament](#3-preprocessament)
  - [4. Implementació dels models](#4-implementació-dels-models)
    - [4.1 Lidstone Smoothing](#41-lidstone-smoothing)
      - [4.1.1 Implementació](#411-implementació)
      - [4.1.2 Refinament del paràmetre $\\lambda$](#412-refinament-del-paràmetre-lambda)
      - [4.1.2 Anàlisi dels resultats i error](#412-anàlisi-dels-resultats-i-error)
    - [4.2 Segon Smoothing](#42-segon-smoothing)
      - [4.2.2 Anàlisi dels resultats](#422-anàlisi-dels-resultats)

## 1. Introducció

## 2. Dades del problema

## 3. Preprocessament

Per a preprocessar, agafem el contingut original de cada document de text i se sotmet a un rentat de cara per uniformar-lo. Això implica treure tots els números, convertir totes les lletres a minúscules i endreçar els espais perquè no n'hi hagi de sobrers entre paraules o al principi i al final del text. A més, s'aprofita per estandarditzar la separació entre les frases, canviant els salts de línia convencionals per un format específic, un doble espai, que facilita el seu tractament posterior. Això es fa així perquè el model que es construirà més endavant treballarà amb trigrames, i aquesta forma de separar les frases permet que els trigrames no es vegin afectats per espais innecessaris, mantenint la coherència en l'anàlisi de les seqüències de caràcters.

Un cop els textos estan nets, comença la segona fase, que consisteix a repartir el material perquè el model pugui aprendre i, posteriorment, ser examinat. Per fer-ho de manera justa i representativa, el codi agafa totes les frases de cada idioma del conjunt de train, les remena a l'atzar i les talla en dos blocs: un gran que conté el vuitanta per cent de la informació i un de més petit amb el vint per cent restant. Això és així perquè en el conjunt de dades donat originalment, les dades del test estavem presents al 100% en el conjunt d'entrenament donat. Doncs per evitar que el model aprengui a reconèixer les frases del test, es fa aquesta divisió, de manera que el model només veu el bloc gran durant l'entrenament i el bloc petit es reserva per avaluar la seva capacitat de generalització.

## 4. Implementació dels models

### 4.1 Lidstone Smoothing

El Lidstone Smoothing és una tècnica d'estimació de probabilitats que s'utilitza per evitar problemes de zero probabilitat en models de llenguatge. Aquesta tècnica consisteix a afegir un petit valor, anomenat $\lambda$, a les freqüències observades dels trigrames, assegurant que cap trigram no tingui una probabilitat de zero, fins i tot si no s'ha observat en el conjunt d'entrenament. Això permet que el model pugui generalitzar millor a dades noves i desconegudes, millorant així la seva capacitat de predicció.

#### 4.1.1 Implementació

B per cada idioma, com es calcula

Pel que fa els aspectes tècnincs...:

!!! La implementació del Lidstone Smoothing ha sigut a través d'una classe `LidstoneModel`, que encapsula tota la lògica necessària per a entrenar el model, refinar el paràmetre $\lambda$ i avaluar el rendiment del model. Aquesta classe inclou mètodes per a:

- `__init__`: Inicialitza el model amb un valor de $\lambda$ i una llista de llengües.
- `fit`: Entrena el model amb les dades d'entrenament, calculant els trigrames i les seves freqüències, així com els paràmetres $B$ i $N_t$.
- `load_model`: Carrega un model preentrenat des d'un fitxer `.json`.
- `predict_model`: Realitza la predicció de la llengua d'un document de test, calculant les probabilitats per a cada llengua i seleccionant la que té la probabilitat més alta.
- `refining_lambda`: Realitza una validació creuada per a refinar el valor de $\lambda$, provant diferents valors i seleccionant aquell que maximitza l'accuracy del model.
- `evaluate_model`: Avalua el rendiment del model amb les dades de test, calculant l'accuracy i la matriu de confusió.

#### 4.1.2 Refinament del paràmetre $\lambda$

#### 4.1.2 Anàlisi dels resultats i error

### 4.2 Segon Smoothing

#### 4.2.2 Anàlisi dels resultats
