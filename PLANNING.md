# Planning of the compilation course (CAP, Compilation and Program Analysis)
_Academic "covid-19" first semester 2020-2021_

* Laure Gonnord, Université Lyon 1, LIP http://laure.gonnord.org/pro/
* Page on the "portail des études ENSL" : https://etudes.ens-lyon.fr/course/view.php?id=4259
* Discord Channel: https://discord.com/channels/691214205692542976/771392543853117460
* MCC (final grade computation) : 
```
let ccgrade = average(Lab3, Lab5, Lab_IA, Lab_futures, partial)
in (finalnote + ccgrade)/2
```
* TBA : The partial exam is this academic year replaced by a  written housework ("DM").

# Week 1: 

- :book: First Course session: Monday 7/9/2020, 13:30. (Laure Gonnord)

	* On BBB at 13:30. 
	* [Script](https://compil-lyon.gitlabpages.inria.fr/cap20/2020_09_07_script.md) for non-french speakers (slides are in English, videos are not).
	* Introduction: [transparents](https://compil-lyon.gitlabpages.inria.fr/cap20/capmif_cours01_intro_et_archi.pdf), [video 1 (intro-french)](https://www.youtube.com/watch?v=zGifE8MfPWA), [video 2 (RISCV-french)](https://youtu.be/ZdElX9e_tAI?list=PLtjm-n_Ts-J-6EU1WfVIWLhl1BUUR-Sqm). 
	* Ex 4 + Ex 5 of Lab 1 during the session. [Optional exercise](https://compil-lyon.gitlabpages.inria.fr/cap20/riscv5_ex.pdf).
	* ISA [ref pdf RISCV](https://compil-lyon.gitlabpages.inria.fr/cap20/RISCV-ISA-2020.pdf).
	* Lexing, Parsing, [slides](https://compil-lyon.gitlabpages.inria.fr/cap20/capmif_cours02_lexing_parsing.pdf), [vidéo 1 (french)](https://www.youtube.com/watch?v=UlUTSsOA9Qc), [vidéo 2(parsing, french)](https://www.youtube.com/watch?v=y9MrfDzrAmA).
	* [Derivation tree exercise](https://compil-lyon.gitlabpages.inria.fr/cap20/derivtree_ex.pdf).


- :hammer: Première Séance de TP: Mardi 8/9/2020, 8h. (Paul Iannetta & Laure Gonnord) (Moitié présentiel en amphi B, distanciel sur BBB)

	* Clone the   [git étudiant CAP](https://github.com/lauregonnord/cap-labs20).
	* **do installs before**, especially if you want to use your personal laptops. On ENS machines, this install only takes the form of a quick edit of `.bashrc`, everything is on the student git [Howto](https://github.com/lauregonnord/cap-labs20/blob/master/INSTALL.md).
	* Review RISCV slides.
	* Amphi B and BBB
	* [Lab1 (pdf)](https://compil-lyon.gitlabpages.inria.fr/cap20/cap_tp1.pdf)

	
- :book: Deuxième Course session: Thursday 10/9/2020, 10:15. (Ludovic Henrio)

	* At 10:15 sur	[BBBlink -externe](https://ent-services.ens-lyon.fr/entVisio/index.php) DI-M1-CAP, password = compilation
	* [transparents](https://compil-lyon.gitlabpages.inria.fr/cap20/cap_cours03b_semantics.pdf) et [Script en anglais des vidéos](https://compil-lyon.gitlabpages.inria.fr/cap20/2020_09_10_script.md).
	* Introduction:  [vidéo 1 (intro)](https://youtu.be/VGUgKBzjlIQ)
	* Sémantique opérationnelle mini-while [vidéo 2 (miniwhile)](https://youtu.be/TE8O9T4zjyE), et la [preuve de la vidéo (min48)](https://compil-lyon.gitlabpages.inria.fr/cap20/miniwhile_opsem_proofs.pdf)
	* Sémantique opérationnelle mini-ml: [vidéo 3 (miniML)](https://youtu.be/-5VAGgg2Jos)

- :rocket: Additional ressources (mainly in english)

	*  A nice YT video on [structural induction](https://www.youtube.com/watch?v=2o3EzvfgTiQ) by F. Pereira, one of our brasilian collaborators.
	* Fernando Pereira's other videos on operational semantics : [video1](https://www.youtube.com/watch?v=bOzbRhXvtlY), [video2](https://www.youtube.com/watch?v=aiBKOuM5iEA)



# Week 2: 

- :book: Course session #3: Monday 14/09/2020, 13:30 (Laure Gonnord)

  * On BBB.
  * First replay the following video (summary of Lexing and Parsing phase): [from15:38 (french)](https://youtu.be/y9MrfDzrAmA?list=PLtjm-n_Ts-J-6EU1WfVIWLhl1BUUR-Sqm&t=936)
  * Semantics, interpreters [slides in english](https://compil-lyon.gitlabpages.inria.fr/cap20/capmif_cours03_interpreters.pdf) and [video (fr)](https://www.youtube.com/watch?v=8PYhBsgRO6g)
  * [Demo files](https://compil-lyon.gitlabpages.inria.fr/cap20/ANTLRExamples.tar.xz)
  * [Script](https://compil-lyon.gitlabpages.inria.fr/cap20/2020_09_14_script.md) for non-french speakers (slides are in English, videos are not).
  * An attribution [exercice](https://compil-lyon.gitlabpages.inria.fr/cap20/grammar_attributes_ex.pdf), [english correction](https://compil-lyon.gitlabpages.inria.fr/cap20/grammar_attributes_ex_corr.pdf)
  
- :hammer: No Lab this week, however we will make some install during the 3rd course slot
  * TODO (technically not _required_ for this week): log [on tomuss-fr](https://tomuss-fr.univ-lyon1.fr/2020/UE/CAP2021/) with your ENS account.
  * Make the first steps of [lab2](https://compil-lyon.gitlabpages.inria.fr/cap20/cap_tp2.pdf) to install and play with ANTLR.


- :book: Course session #4: Thursday 17/9/2020, 10:15. (Ludovic Henrio)
  
  * On BBB
  * End of miniML op semantics [vidéo (miniML - french)](https://youtu.be/-5VAGgg2Jos) (the script is [here](https://compil-lyon.gitlabpages.inria.fr/cap20/2020_09_10_script.md).)
  * Intro, typing mini-while [transparents](https://compil-lyon.gitlabpages.inria.fr/cap20/capmif_cours04_typing.pdf) et [vidéo](https://youtu.be/2A-hQy_6YlE).
  * Safety of miniwhile typing on  [the second part of these slides](https://compil-lyon.gitlabpages.inria.fr/cap20/cap_cours04b_typingML_safety.pdf). The [video (fr)](https://youtu.be/qNhBEsKLNco). The proof on [paper(scanned pdf)](https://compil-lyon.gitlabpages.inria.fr/cap20/Handproofssafety.pdf)
  * [English script for these two videos](https://compil-lyon.gitlabpages.inria.fr/cap20/2020_09_17_script.md)


- :rocket: Additional ressources (mainly in english)

	* Fernando Pereira's videos (in English) for type systems: : [video1](https://www.youtube.com/watch?v=AtFH_6yzC1Y) (there are 4 of such nice videos).

	
# Week 3 (from Monday, Sept 21th)


- :hammer: Lab Session #2: Monday 21/9/2020, 13:30 (Paul Iannetta and Laure Gonnord)
    * AMPHI and  BBB.
	* [pdf for lab2](https://compil-lyon.gitlabpages.inria.fr/cap20/cap_tp2.pdf)
	* All installs should be done before this session!
    * RDV sur [BBB "portail des études"](https://etudes.ens-lyon.fr/mod/bigbluebuttonbn/view.php?id=89490) (Yes, works again!)
	* [slides: summary of the lab](https://compil-lyon.gitlabpages.inria.fr/cap20/capmif_labs.pdf)

- :book: Course session #5: Thursday 24/9/2020, 10:15. (Gabriel Radanne)
	* At 10:15 on BBB
	* Typing ML, and safety:  [transparents](https://compil-lyon.gitlabpages.inria.fr/cap20/cap_cours04b_typingML_safety.pdf) 
	* [Video 1 (french)](https://youtu.be/8LNEeffQks0), [Video 2 (french)](https://www.youtube.com/watch?v=jub4CzctrTs), [Video 3 (french)](https://youtu.be/4qHX_F5W6jo)
	* [English script](https://compil-lyon.gitlabpages.inria.fr/cap20/2020_09_24_script.md).
	* [Exercises](https://compil-lyon.gitlabpages.inria.fr/cap20/mltypes_ex.pdf)


# Week 4 (from Monday, Sept 28th)


- :book: Course session #6: Monday 28/9/2020, 13:30. (Laure Gonnord)
	* At 13:30 on  [BBB "portail des études"](https://etudes.ens-lyon.fr/mod/bigbluebuttonbn/view.php?id=89490)
	* Quick recall of where we are and Lab3's objective.
	* 3-address code generation:  [transparents (fr)](https://compil-lyon.gitlabpages.inria.fr/cap20/capmif_cours05_3ad_codegen.pdf) 
	* [Video (french)](https://youtu.be/m2x7leFnCN4)
	* [English script](https://compil-lyon.gitlabpages.inria.fr/cap20/2020_09_28_script.md).
	* [Exercises (pdf)](https://compil-lyon.gitlabpages.inria.fr/cap20/3ad_ex.pdf) and a [corrected version (pdf)](https://compil-lyon.gitlabpages.inria.fr/cap20/3ad_ex_corr.pdf)


- :hammer: Lab session #3: Thursday 01/10/2020, 10:15 (Paul Iannetta and Gabriel Radanne) 
    * TOPIC **Interpret MiniC with ANTLR**! 
	* All installs should be done before this session!
    * AMPHI B and [BBB "portail des études"](https://etudes.ens-lyon.fr/mod/bigbluebuttonbn/view.php?id=89490)
	* A quick summary **READ BEFORE** with [slides](https://compil-lyon.gitlabpages.inria.fr/cap20/capmif_labs.pdf).
	* [pdf for lab3](https://compil-lyon.gitlabpages.inria.fr/cap20/cap_tp3.pdf)
	* Lab deposit on [TOMUSS-fr](https://tomuss-fr.univ-lyon1.fr/2020/UE/CAP2021) before Oct 7, 2020, 6pm Paris time. Email deposits are **strictly forbidden** (except for pople that do not have their ENS account yet).
		

# Week 5 (from Monday, Oct 5th)

- :book: Course session #7: Monday 05/10/2020, 13:30. (Laure Gonnord)
	* At 13:30 on  [BBB "portail des études"](https://etudes.ens-lyon.fr/mod/bigbluebuttonbn/view.php?id=89490)
	* Quick recall of where we are and Lab4's objective.
	* Topic: **Intermediate Representations** (1)
	* [Slides (english)](https://compil-lyon.gitlabpages.inria.fr/cap20/capmif_cours06_irs.pdf)
	* [Video 1(french)](https://youtu.be/dD9bRhLfykM) and [Video 2(french)- instruction scheduling](https://youtu.be/Xico_JTK3XQ)
	* DAG construction example: [Video (english)](https://www.youtube.com/watch?v=PXTKWvyQUwE) 
	* Course on SSA : will be done later.
	* [English script](https://compil-lyon.gitlabpages.inria.fr/cap20/2020_10_05_script.md).
	* [Exercises (pdf)](https://compil-lyon.gitlabpages.inria.fr/cap20/IR_ex1.pdf) and  a [corrected version (pdf)](https://compil-lyon.gitlabpages.inria.fr/cap20/IR_ex1_corr.pdf).


- :hammer: Lab session #4: Thursday 08/10/2020, 10:15 (Paul Iannetta and Gabriel Radanne) 
    * TOPIC **Syntax directed code generation for MiniC**
	* All installs should be done before this session!
    * AMPHI B and [BBB "portail des études"](https://etudes.ens-lyon.fr/mod/bigbluebuttonbn/view.php?id=89490)
	* A quick summary **READ BEFORE** with [slides](https://compil-lyon.gitlabpages.inria.fr/cap20/capmif_labs.pdf).
	* [pdf for lab4](https://compil-lyon.gitlabpages.inria.fr/cap20/cap_tp4.pdf)
		


# Week 6 (from Monday, Oct 12th)


- :book: Course session #8: Monday 12/10/2020, 13:30. (Laure Gonnord)
	* At 13:30 on  [BBB "portail des études"](https://etudes.ens-lyon.fr/mod/bigbluebuttonbn/view.php?id=89490)
	* Topic: **Register Allocation/Dataflow analyses**
	* [Slides (english)](https://compil-lyon.gitlabpages.inria.fr/cap20/capmif_cours07_regalloc.pdf)
	* [Video 1(french) - register alloc (21min)](https://www.youtube.com/watch?v=9902mMgDIK8) and [Video 2(french)- dataflow UNTIL 15'10](https://www.youtube.com/watch?v=LknSDccweFw)
	* [English script](https://compil-lyon.gitlabpages.inria.fr/cap20/2020_10_12_script.md).
	* [Exercises 2+7 here (pdf)](https://compil-lyon.gitlabpages.inria.fr/cap20/DF_regalloc_ex.pdf) [and elements of solution](https://compil-lyon.gitlabpages.inria.fr/cap20/DF_regalloc_ex_corr.pdf)
	* Homework : end of Video 2 and corresponding exercice (ex 3 of the previous pdf)

- :hammer: Lab session #5: Thursday 15/10/2020, 10:15 (Paul Iannetta and Gabriel Radanne) 
    * TOPIC **Smart code generation for MiniC (1/2)**
	* All installs should be done before this session!
    * AMPHI B and [BBB "portail des études"](https://etudes.ens-lyon.fr/mod/bigbluebuttonbn/view.php?id=89490)
	* A quick summary **READ BEFORE** with [slides](https://compil-lyon.gitlabpages.inria.fr/cap20/capmif_labs.pdf).
	* [pdf for lab5](https://compil-lyon.gitlabpages.inria.fr/cap20/cap_tp5.pdf)
		

- :rocket: Additional ressources (in english)

	* Fernando Pereira's videos (in English) for register allocation : [video1](https://youtu.be/pSunR-16EgA) (there are 4 of such nice videos, with an additional nice algorithm called linear scan).


# Week 7 (from Monday, Oct 19th)


- :book: Course session #9: Monday 19/10/2020, 13:30. (Yannick Zakowski)
	* At 13:30 on  [BBB "portail des études"](https://etudes.ens-lyon.fr/mod/bigbluebuttonbn/view.php?id=89490)
	* Topic: **SSA: Static Single Assignment**
	* [slides (en)](https://compil-lyon.gitlabpages.inria.fr/cap20/ssa_cours.pdf)
    * [video 1 Intro (en)](https://www.youtube.com/watch?v=x61pjK3kGbg) and [video 2 Construction/Deconstruction (en)](https://youtu.be/ufmCopez1ys?list=PLtjm-n_Ts-J-6EU1WfVIWLhl1BUUR-Sqm) and [video 3 SSA is functional (en)](https://youtu.be/aFevTC8HzgE)
	* [exercises (en)](https://compil-lyon.gitlabpages.inria.fr/cap20/ssa_exos.pdf) [and elements of solution](https://compil-lyon.gitlabpages.inria.fr/cap20/ssa_exos_avec_corriges.pdf)

- :hammer: Lab session #6: Thursday 22/10/2020, 10:15 (Paul Iannetta and Gabriel Radanne) 
    * TOPIC **Smart code generation for MiniC (2/2)**
    * AMPHI B and [BBB "portail des études"](https://etudes.ens-lyon.fr/mod/bigbluebuttonbn/view.php?id=89490)
	* A quick summary **READ BEFORE** with [slides](https://compil-lyon.gitlabpages.inria.fr/cap20/capmif_labs.pdf).
	* [pdf for lab5](https://compil-lyon.gitlabpages.inria.fr/cap20/cap_tp5.pdf)
	* Lab deposit on [TOMUSS-fr](https://tomuss-fr.univ-lyon1.fr/2020/UE/CAP2021) before November 1st, 2020, 6pm Paris time. Email deposits are **strictly forbidden**
		

- :rocket: Additional ressources (in English)

	* Fernando Pereira's videos (in English): [SSA-based register allocation](https://www.youtube.com/watch?v=Q2tQcBxjRp8), see his YT chain for additional videos.


# Week 8 No course

- :pencil: DM on paper: [DM_2020](https://compil-lyon.gitlabpages.inria.fr/cap20/dm_cap_2020.pdf). Due on [TOMUSS-fr]((https://tomuss-fr.univ-lyon1.fr/2020/UE/CAP2021)), deadline November 7th, 2020, 6pm Paris time. **1 PDF file only** ; email deposits are **strictly forbidden** Ask questions by email with [CAP:DM] header to Laure.Gonnord and Lucdovic.Henrio (at ens-lyon.fr).


# Week 9 (from Monday, nov 2nd)


- :book: Course session #10: Monday 02/11/2020, 13:30. (Laure Gonnord)
	* At 13:30 on  [BBB "portail des études"](https://etudes.ens-lyon.fr/mod/bigbluebuttonbn/view.php?id=89490)
	* Topic: **Code generation for functions**
	* [slides (en)](https://compil-lyon.gitlabpages.inria.fr/cap20/cap_cours09b_func_codegen.pdf)
    * [video Full, fr](https://youtu.be/N2rQhJJcQls) . Timestamps in the video description to cut it into pieces. 
	* [Script](https://compil-lyon.gitlabpages.inria.fr/cap20/2020_11_02_script.md)
	* [Exercices (en)](https://compil-lyon.gitlabpages.inria.fr/cap20/functions_ex.pdf), [correction (fr/en])](https://compil-lyon.gitlabpages.inria.fr/cap20/functions_ex_corr.pdf)



- :book: Course session #11: Thursday 05/11/2020, 10h15. (Ludovic Henrio)
	* At 10h15 on  [BBB "portail des études"](https://etudes.ens-lyon.fr/mod/bigbluebuttonbn/view.php?id=89490)
	* Topic: **Semantics for functions**
   * TBD

	
- :hammer: No Lab this week.
