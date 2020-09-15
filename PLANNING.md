# Avancée / Planning du cours de CAP (Compilation)
_Année 2020-2021_

* Laure Gonnord, Université Lyon 1, LIP http://laure.gonnord.org/pro/
* Page sur le portail des études ENSL : https://etudes.ens-lyon.fr/course/view.php?id=4259

# Semaine 1: 

- :book: Première Séance de Cours: Lundi 7/9/2020, 13h30. (Laure Gonnord)

	* RDV sur BBB à 13h30. 
	* [Script](https://compil-lyon.gitlabpages.inria.fr/cap20/2020_09_07_script.md) for non-french speakers (slides are in English, videos are not).
	* Introduction: [transparents](https://compil-lyon.gitlabpages.inria.fr/cap20/capmif_cours01_intro_et_archi.pdf), [vidéo 1 (intro)](https://www.youtube.com/watch?v=zGifE8MfPWA), [vidéo 2 (RISCV)](https://youtu.be/ZdElX9e_tAI?list=PLtjm-n_Ts-J-6EU1WfVIWLhl1BUUR-Sqm). 
	* Ex 4 + Ex 5 (du TP1 plus bas) pendant la séance. [Un exercice optionnel](https://compil-lyon.gitlabpages.inria.fr/cap20/riscv5_ex.pdf) si vous voulez !
	* ISA de [ref pdf RISCV](https://compil-lyon.gitlabpages.inria.fr/cap20/RISCV-ISA-2020.pdf).
	* Lexing, Parsing, [transparents](https://compil-lyon.gitlabpages.inria.fr/cap20/capmif_cours02_lexing_parsing.pdf), [vidéo 1 (lexing)](https://www.youtube.com/watch?v=UlUTSsOA9Qc), [vidéo 2(parsing)](https://www.youtube.com/watch?v=y9MrfDzrAmA).
	* [Exercice simple arbre de dérivation](https://compil-lyon.gitlabpages.inria.fr/cap20/derivtree_ex.pdf).


- :hammer: Première Séance de TP: Mardi 8/9/2020, 8h. (Paul Iannetta & Laure Gonnord) (Moitié présentiel en amphi B, distanciel sur BBB)

	* Cloner le  [git étudiant CAP](https://github.com/lauregonnord/cap-labs20).
	* Avant: les installations prévues, si vous souhaitez utiliser vos machines personnelles. Sinon, il s'agira uniquement de modifier quelques paramètres utilisateurs sur les machines de TP de l'école. Pour cela lire le [Howto](https://github.com/lauregonnord/cap-labs20/blob/master/INSTALL.md) dans le git étudiant.
	* Revisualiser une partie des transparents RISCV.
	* RDV à 8h sur BBB et la moitié en AmphiB avec Paul.
	* L'[énoncé de TP](https://compil-lyon.gitlabpages.inria.fr/cap20/cap_tp1.pdf)

	
- :book: Deuxième Séance de Cours: Jeudi 10/9/2020, 10h15. (Ludovic Henrio)

	* RDV à 10h sur	[BBBlink -externe](https://ent-services.ens-lyon.fr/entVisio/index.php) DI-M1-CAP, password = compilation
	* [transparents](https://compil-lyon.gitlabpages.inria.fr/cap20/cap_cours03b_semantics.pdf) et [Script en anglais des vidéos](https://compil-lyon.gitlabpages.inria.fr/cap20/2020_09_10_script.md).
	* Introduction:  [vidéo 1 (intro)](https://youtu.be/VGUgKBzjlIQ)
	* Sémantique opérationnelle mini-while [vidéo 2 (miniwhile)](https://youtu.be/TE8O9T4zjyE), et la [preuve de la vidéo (min48)](https://compil-lyon.gitlabpages.inria.fr/cap20/miniwhile_opsem_proofs.pdf)
	* Sémantique opérationnelle mini-ml: [vidéo 3 (miniML)](https://youtu.be/-5VAGgg2Jos)

- :rocket: Additional ressources (mainly in english)

	*  A nice YT video on [structural induction](https://www.youtube.com/watch?v=2o3EzvfgTiQ) by F. Pereira, one of our brasilian collaborators.
	* Fernando Pereira's other videos on operational semantics : [video1](https://www.youtube.com/watch?v=bOzbRhXvtlY), [video2](https://www.youtube.com/watch?v=aiBKOuM5iEA)



# Semaine 2: 

- :book: Troisième Séance de Cours: Lundi 14/09/2020, 13h30 (Laure Gonnord)

  * RDV sur [BBB "portail des études"](https://etudes.ens-lyon.fr/mod/bigbluebuttonbn/view.php?id=89490)
  * First replay the following video (summary of Lexing and Parsing phase): [from15:38](https://youtu.be/y9MrfDzrAmA?list=PLtjm-n_Ts-J-6EU1WfVIWLhl1BUUR-Sqm&t=936)
  * Sémantique et interprètes : [slides in english](https://compil-lyon.gitlabpages.inria.fr/cap20/capmif_cours03_interpreters.pdf) and [video](https://www.youtube.com/watch?v=8PYhBsgRO6g)
  * [Demo files](https://compil-lyon.gitlabpages.inria.fr/cap20/ANTLRExamples.tar.xz)
  * [Script](https://compil-lyon.gitlabpages.inria.fr/cap20/2020_09_14_script.md) for non-french speakers (slides are in English, videos are not).
  * An attribution [exercice](https://compil-lyon.gitlabpages.inria.fr/cap20/grammar_attributes_ex.pdf), 
  
- :hammer: No Lab this week, however we will make some install during the course slot
  * TODO (technically not _required_ for this week): log [on tomuss-fr](https://tomuss-fr.univ-lyon1.fr/2020/UE/CAP2021/) with your ENS account.
  * Make the first steps of [lab2](https://compil-lyon.gitlabpages.inria.fr/cap20/cap_tp2.pdf) to install and play with ANTLR.


- :book: Quatrième Séance de Cours: Jeudi 17/9/2020, 10h15. (Ludovic Henrio)
  
  * RDV sur [BBB "portail des études"](https://etudes.ens-lyon.fr/mod/bigbluebuttonbn/view.php?id=89490)
  * Fin de sémantique opérationnelle mini-ml: [vidéo (miniML)](https://youtu.be/-5VAGgg2Jos) (the script is [here](https://compil-lyon.gitlabpages.inria.fr/cap20/2020_09_10_script.md).)
  * Typage, introduction, et typage de mini-while [transparents](https://compil-lyon.gitlabpages.inria.fr/cap20/capmif_cours04_typing.pdf) [vidéo](https://youtu.be/2A-hQy_6YlE), english scripts TBD
  * Sûreté du typage de mini-while [deuxième partie de ces transparents](https://compil-lyon.gitlabpages.inria.fr/cap20/cap_cours04b_typingML_safety.pdf) [vidéo](https://youtu.be/qNhBEsKLNco) english scripts TBD
	
	
# Semaine 3 TBA


- :hammer: Deuxième Séance de TP: Lundi 21/9/2020, 13h30.
	* [pdf for lab2](https://compil-lyon.gitlabpages.inria.fr/cap20/cap_tp2.pdf)
	* All installs should be done before this session!
	

- :book: Cinquième Séance de Cours: Jeudi 24/9/2020, 10h15. (Gabriel Radanne)

