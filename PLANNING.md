# Avancée / Planning du cours de MIF08 (Compilation)
_Année 2020-2021_

* Matthieu Moy, Université Lyon 1, LIP https://matthieu-moy.fr/
* Version : 19/08/2020

## Organisation du cours en hybride

L'organisation de l'UE en « mode COVID » est la suivante :

* Pour chaque créneau, les instructions détaillées se trouvent ci-dessous.

* Tous les CM sont à distance

* Les TD et TP sont faits en hybride, certains étudiants et enseignants à distance, d'autres en présentiel. Pour chaque créneau, vous trouverez une case sur TOMUSS indiquant la salle (si vous êtes en présentiel) ou « à distance » si vous êtes à distance. La répartition présentiel/distanciel est faite dans la mesure du possible en suivant les couleurs jAune/Bleu de TOMUSS. Pour les TP/TD à distance, rendez-vous sur le canal correspondant de chat-info (les enseignants utiliseront parfois d'autres outils, par exemple pour une explication ponctuelle en visio, mais posteront le lien vers les outils utilisés dans le canal de chat-info).

* Pour rejoindre les canaux de discussions sur chat-info, cliquez sur les liens suivants :
    - [compil-general](https://go.rocket.chat/invite?host=chat-info.univ-lyon1.fr&path=invite%2FsfzYSh) pour les discussions générales sur le cours et les CM
    - [compil-groupe-1](https://go.rocket.chat/invite?host=chat-info.univ-lyon1.fr&path=invite%2FEqiqPF) et [compil-groupe-2](https://go.rocket.chat/invite?host=chat-info.univ-lyon1.fr&path=invite%2F3Qzt5k) pour les groupes distanciels en TD
    - [compil-groupe-a](https://go.rocket.chat/invite?host=chat-info.univ-lyon1.fr&path=invite%2FtHfE7j), [compil-groupe-b](https://go.rocket.chat/invite?host=chat-info.univ-lyon1.fr&path=invite%2FqHW2MX), [compil-groupe-c](https://go.rocket.chat/invite?host=chat-info.univ-lyon1.fr&path=invite%2FsuFXKk), [compil-groupe-d](https://go.rocket.chat/invite?host=chat-info.univ-lyon1.fr&path=invite%2FkAWmMd), [compil-groupe-e](https://go.rocket.chat/invite?host=chat-info.univ-lyon1.fr&path=invite%2FcnEQ9c) pour les groupes distanciels de TP.

* Les groupes B et E sont parfois affectés à des salles de TD pour les TP. Venez avec votre ordinateur personnel pour ces séances.

## Intervenants

* Groupe A : Laure Gonnord / Joris Picot (en TD et TP)
* Groupe B : Guillaume Bouchard (+ Nicolas Louvet en TP)
* Groupe C : Élise Jeanneau (+ Thierry Excoffier en TP)
* Groupe D : Grégoire Pichon (+ Lionel Morel en TP)
* Groupe E : Matthieu Moy (+ Guillaume Salagnac en TP)

## Vidéos des CM

Toutes les vidéos sont disponibles dès maintenant :

[La playlist Youtube MIF08](https://www.youtube.com/playlist?list=PLtjm-n_Ts-J9HSZ9ahpbsC_kTQMzUZQPx)

Vous pouvez les regarder en avance si vous le souhaitez, et devez les regarder au plus tard pendant le créneau prévu dans votre emploi du temps.

Vous pouvez utiliser le canal [compil-general](https://go.rocket.chat/invite?host=chat-info.univ-lyon1.fr&path=invite%2FsfzYSh) pour poser des questions au fur et à mesure que vous regardez les vidéos. Une visio en direct aura lieu en fin de chaque créneau de CM sur [BBB (Compilation mif08)](https://classe-info.univ-lyon1.fr/moy-n6a-uip-gtj).

## Mercredi 7/10/2020

- :book: 14h: Cours 1: Introduction, machine cible (RISCV), lexing :
    - [transparents](https://compil-lyon.gitlabpages.inria.fr/mif08-20/capmif_cours01_intro_et_archi.pdf)
    - [Vidéo "teaser"](https://youtu.be/ny7HlqyuM9E)
    - [vidéo d'introduction au cours](https://www.youtube.com/watch?v=zGifE8MfPWA)
    - [vidéo sur RISCV](https://youtu.be/ZdElX9e_tAI)
    - [vidéo lexing](https://www.youtube.com/watch?v=UlUTSsOA9Qc)
    - [Extrait de la documentation RISCV](https://compil-lyon.gitlabpages.inria.fr/mif08-20/RISCV-ISA-2020.pdf)
    - chat sur [compil-general](https://go.rocket.chat/invite?host=chat-info.univ-lyon1.fr&path=invite%2FsfzYSh).
    - Visio en direct à 15h sur [BBB (Compilation mif08)](https://classe-info.univ-lyon1.fr/moy-n6a-uip-gtj).

- :book: 15h45: Cours 2:
Lexing, Parsing.
    - [transparents parsing](https://compil-lyon.gitlabpages.inria.fr/mif08-20/capmif_cours02_lexing_parsing.pdf)
    - [vidéo parsing](https://www.youtube.com/watch?v=y9MrfDzrAmA)
    - [transparents sémantique et interprète](https://compil-lyon.gitlabpages.inria.fr/mif08-20/capmif_cours03_interpreters.pdf)
    - [vidéo sémantique et interprète](https://youtu.be/8PYhBsgRO6g)
    - chat sur [compil-general](https://go.rocket.chat/invite?host=chat-info.univ-lyon1.fr&path=invite%2FsfzYSh).
    - Visio en direct à 16h45 sur [BBB (Compilation mif08)](https://classe-info.univ-lyon1.fr/moy-n6a-uip-gtj).

- :100: QCM noté sur TOMUSS, à faire avant 23:59 le jour même (7/10)

## Mercredi 14/10/2020

- :pencil2: 16h30: TD1 : Architecture RISCV, Lexing

    Votre salle est affichée sur TOMUSS, les bleus et quelques jaunes sont à distance.
    - En présentiel :
        - Nautibus TD1 (20 places) : Matthieu Moy.
        - Nautibus TD5 (24 places) : Guillaume Bouchard
        - Nautibus TD10 (24 places) : Élise Jeanneau
    - À distance :
        - groupe 1 : [compil-groupe-1](https://go.rocket.chat/invite?host=chat-info.univ-lyon1.fr&path=invite%2FEqiqPF) sur chat-info, Grégoire Pichon.
        - groupe 2 : [compil-groupe-2](https://go.rocket.chat/invite?host=chat-info.univ-lyon1.fr&path=invite%2F3Qzt5k) sur chat-info, ~~Laure Gonnord~~ Joris Picot
    - [Énoncé du TD1](https://compil-lyon.gitlabpages.inria.fr/mif08-20/td1.pdf)
    - Rappel : [Extrait de la documentation RISCV](https://compil-lyon.gitlabpages.inria.fr/mif08-20/RISCV-ISA-2020.pdf)
    - Lexing et parsing avec ANTLR en 2 slides : [slides-td1.pdf](https://compil-lyon.gitlabpages.inria.fr/mif08-20/td1-slides.pdf)

## Jeudi 15/10/2020

- :hammer: TP1,
    <!-- - Nautibus TP1 (10 places) :  -->
    Votre salle est affichée sur TOMUSS. Les bleus sont à distance, les jaunes en présentiel. Pour les quelques jaunes qui sont en distanciel sur le créneau suivant, vous pouvez aussi faire le TP en distanciel bien sûr.
    - En présentiel :
        - Nautibus TP9  (9 places)  : A1,Laure Gonnord
        - Nautibus TP10 (10 places) : A2, Laure Gonnord
        - Nautibus TP11 (9 places)  : C1, Guillaume Bouchard
        - Nautibus TP12 (9 places)  : C2, Guillaume Bouchard
        - Nautibus TP13 (10 places) : D1, Élise Jeanneau
        - Nautibus TP14 (10 places) : D2, Élise Jeanneau
        - Nautibus TD10 (24 places) : Groupe E, Grégoire Pichon
        - Nautibus TD12 (23 places) : Groupe B (repli possible en TP1 si des étudiants n'ont pas de machine), Matthieu Moy
    - À distance : 
        - Groupe A : [compil-groupe-a](https://go.rocket.chat/invite?host=chat-info.univ-lyon1.fr&path=invite%2FtHfE7j) ~~Laure Gonnord~~ Joris Picot
        - Groupe B : [compil-groupe-b](https://go.rocket.chat/invite?host=chat-info.univ-lyon1.fr&path=invite%2FqHW2MX) Nicolas Louvet
        - Groupe C : [compil-groupe-c](https://go.rocket.chat/invite?host=chat-info.univ-lyon1.fr&path=invite%2FsuFXKk) Thierry Excoffier
        - Groupe D : [compil-groupe-d](https://go.rocket.chat/invite?host=chat-info.univ-lyon1.fr&path=invite%2FkAWmMd) Lionel Morel
        - Groude E : [compil-groupe-e](https://go.rocket.chat/invite?host=chat-info.univ-lyon1.fr&path=invite%2FcnEQ9c) Guillaume Salagnac
    - Énoncé : [TP1 python/archi](https://compil-lyon.gitlabpages.inria.fr/mif08-20/tp1.pdf)
    - Fichiers du TP1 : [TP01/](TP01/).

- :pencil2: TD, Arbres abstraits, attributions, types

    Votre salle est affichée sur TOMUSS. Les bleus sont à distance et quelques jaunes sont à distance, les autres en présentiel.
    - En présentiel :
        - Nautibus TD10 (24 places) : Matthieu Moy
        - Nautibus TD11 (20 places) : Guillaume Bouchard
        - Nautibus TD1 (20 places) : Élise Jeanneau
    - À distance :
        - groupe 1 : [compil-groupe-1](https://go.rocket.chat/invite?host=chat-info.univ-lyon1.fr&path=invite%2FEqiqPF) sur chat-info, Grégoire Pichon.
        - groupe 2 : [compil-groupe-2](https://go.rocket.chat/invite?host=chat-info.univ-lyon1.fr&path=invite%2F3Qzt5k) sur chat-info, ~~Laure Gonnord~~ Joris Picot
    - [Énoncé du TD2](https://compil-lyon.gitlabpages.inria.fr/mif08-20/td2.pdf)


# TOUT CE QUI SUIT CETTE LIGNE EST UN BROUILLON QUI SERA MIS À JOUR ... BIENTÔT :-)


## Mercredi 04/11/2020

- :hammer: TP, [TP2 antlr](https://compil-lyon.gitlabpages.inria.fr/compil-lyon/MIF081920_Lyon1/mif08_tp2.pdf)

## Vendredi 13/11/2020

- :book: Cours 3, Interprètes, [transparents](https://compil-lyon.gitlabpages.inria.fr/mif08-20/capmif_cours03_interpreters.pdf), [vidéo](https://youtu.be/8PYhBsgRO6g) et typage [transparents](https://compil-lyon.gitlabpages.inria.fr/mif08-20/capmif_cours04_typing.pdf), [vidéo](https://youtu.be/2A-hQy_6YlE)
<!-- - :mag_right: Contrôle continu (papier), TODO, archi (aucun doc
    autorisé: ISA de la machine) -->

- :hammer: TP, [TP3 frontend, évaluateur](https://compil-lyon.gitlabpages.inria.fr/compil-lyon/MIF081920_Lyon1/mif08_tp3.pdf)

## Mercredi 2/12/2020

- :book: Cours 4, génération de code 3 adresses + allocation naive, [transparents](https://compil-lyon.gitlabpages.inria.fr/mif08-20/capmif_cours05_3ad_codegen.pdf), [vidéo](https://youtu.be/m2x7leFnCN4)

- :pencil2: TD, [TD3 génération de
    code](https://compil-lyon.gitlabpages.inria.fr/compil-lyon/MIF081920_Lyon1/cahier_exos_MIF08.pdf)
    (LG, GB,  MM, NL)

## Mercredi 9/12/2020

- :hammer: TP, [TP4 démo, début codegen](https://compil-lyon.gitlabpages.inria.fr/compil-lyon/MIF081920_Lyon1/mif08_tp4.pdf)

- 	- :hammer: TP, [TP5 code gen](https://compil-lyon.gitlabpages.inria.fr/compil-lyon/MIF081920_Lyon1/mif08_tp5.pdf)

## Jeudi 10/12/2020

- :book: Cours 5,
    Représentations intermédiaires, [transparents](https://compil-lyon.gitlabpages.inria.fr/mif08-20/capmif_cours06_irs.pdf) et allocation de registres, [transparents](https://compil-lyon.gitlabpages.inria.fr/mif08-20/capmif_cours07_regalloc.pdf)

## Mercredi 6/01/2021
<!-- 
- :mag_right: Contrôle continu (tp) (20 min de composition) une grammaire
    ANTLR -->

- :pencil2: TD, 8-9h30  ou 10-11h30 : [TD4
    liveness](https://compil-lyon.gitlabpages.inria.fr/compil-lyon/MIF081920_Lyon1/cahier_exos_MIF08.pdf)

## Mercredi 13/01/2021

- :pencil2: TD groupe A 8-9h30, autres 10h00 -> 11h30: [TD5
    regalloc](https://compil-lyon.gitlabpages.inria.fr/compil-lyon/MIF081920_Lyon1/cahier_exos_MIF08.pdf)

- :hammer: TP5 code gen, suite.

### Rendus Tomuss et feedback

- CC de cours : la note arrivera fin de la semaine.

- CC de tp noté : rendu mercredi 15/01 à 14h30. La correction
arrivera avant la fin de la semaine.

- Rendu de l'évaluateur juste après la démo le vendredi 17/01. Une
note "automatique" vous sera rendue durant le week-end.

- Tps de génération de code directe: rendu le mardi 21/01 à 18h - une
correction partielle sera fournie à la même heure. 

- Dernier TP : rendu le dimanche 26 à 23h59.

- Les deux dernières notes de TP vous seront fournies après l'examen.

## Pondération des notes (indicative pour l'instant)
  - CC1 (archi) 5%
  - CC2 (grammaire) 5%
  - TP évaluateur 15%
  - TPs génération de code 15%+20%
  - Examen final 40 %
