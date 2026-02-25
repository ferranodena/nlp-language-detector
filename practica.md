fer un model que donat un document en digui la llengua:

1. preprocessament: netejar text (fer el que diu al power).
   Concatenar totes les frases en dos espais, cal perque es fan trigrames i aixi no agafa un n-grama amb només espais, per distingir espais quan esta al mig d'un doc o no
2. OBLIGATÒRIAMENT TRIGRAMES, pero es poden provar d'altres
3. Smoothing. Té paràmetres -> s'haurà de justificar aquest nombre (experimentació) Vakoff, Laplace, Interpolació, Additive Smoothing (el que ja hem fet a classe) L'important és que haurem de triar i justificar, és important sobretot justificar. És un hiperparàmetre del nostre model el $\lambda$, podem fer 
   PER OPTIMITZAR LA LAMBDA, S'HA DE DIVIDR EL TRAIN SET, NO FER SERVIR EL TEST. cross validtaion. TRAIN SET PER EVITAR OVERFITTING.
4. treure el trigtrams poc comuns
5. la tasca és classificar frase a frase del test set, calcular probabilitats
6. Accuracy i matriu de confusió. L'avaluació es fa amb el test set, els canvis amb els espais també s'ha de fer. El preprocessament haurà de ser el mateix.
7. ANÀLISI DELS ERRORS!!!!! Quan s'equivoca i perquè s'equivoca. Quina és la long dels docs que falla
8. Explicar quina és la nostra estimació de B.
9. N_T és
10. fer servir la mateixa B per a totes les llengues. 