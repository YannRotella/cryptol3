---
title: Home
---
Cours de Licence 3 décrivant les bases de la cryptographie moderne. Cryptographie historique, cryptographie symétrique et asymétrique. Le contenu et les documents du cours sont dûs à Prof. Christina Boura (IRIF, université Paris-Cité)

## Informations pratiques

11 Cours Magistraux d'une heure 30, 11 TDs de 3 heures. Se référer à [CELCAT](https://edt.uvsq.fr/cal?vt=agendaWeek&dt=2025-01-20&et=module&fid0=LSIN603)

Les cours ont lieu globalement les jeudi matins et les TDs ont lieu Lundi après-midi, mercredi après-midi ou jeudi après-midi.

**Responsable du cours :** [Yann Rotella](https://rotella.fr/)

**Chargé de TD :** M'Foukh Dounia et Gaël Chopin et Yann Rotella

## Modélités d'évaluation

Contrôle continu, avec deux contrôles.

## Calendrier des CMs

Ici, les documents du cours (énoncés des TDs, documents des CM, challenges et résumés seront rajoutés au fur et à mesure de l'année)

#### 23 janvier (11h20 -> 15h20): Cryptographie Historique
  - [Présentation](docs/cours1.pdf)
  - Challenge 1: un code secret se cache dans ce message. Pouvez-vous le retrouver ?
  - GZOIAVXPJUKIXCOKWVWDJIMJZICYJTBTUKYBWRZCNVPZQZMDYRDDTECGJTYYJJOXWVDZXKHVGGOFONDA
  - Challenge résolu (Vigenere avec une clef de taille 5)
  - Challenge 2: des techniques de l'antiquité ont été utilisées pour chiffrer un message. Nous avons récupéré les données suivantes:
  - JHJJZINFFZXYJJZHQIDNZWVIZDJTQQNPHWRUWJHQJXTVHJKRNYJJXHXUWUSXJFJVXSYWXYNXYTIWJQYY
  - Pouvez-vous retrouver la méthode de chiffrement ainsi que la clef utilisée ?
  - Challenge résolu (substitution et transposition)

#### 30 janvier (11h20 -> 12h50): Enigma (suite) - Chiffrements à flots
  - [Enigma](docs/ENIGMA.pdf)

#### 6 février (11h20 -> 12h50):
  - Cryptographie symétrique, définitions
  - PRNGs, one-time-pad
  - chiffrements à flot, LFSRs [Notes](docs/ChiffrementAFlot.pdf)

#### 13 février (11h20 -> 12h50):
  - Théorie de Shannon (Diffusion, confusion)
  - Introduction aux chiffrements par bloc
  - Stratégies de conception (notion de tours, SPN)

#### 20 février (11h20 -> 12h50):
  - Suite chiffrements par bloc
  - Conception complète, cadencement de clefs
  - Réseaux de Feistel
  - DES
  - [Notes](docs/Cours4-5.pdf)

#### 6 mars (11h20 -> 12h50):
  - fin cryptographie symétrique
  - padding et Modes d'opération
  - Définition Cryptographie asymétrique
  - RSA - définition

#### 13 mars (11h20 -> 12h50):
  - RSA: théorie mathématique
  - RSA en pratique

#### 27 mars (11h20 -> 12h50):
  - Générations de nombres premiers
  - à quoi faut-il faire attention
  - [Notes](docs/RSA_TestsDePrimalite.pdf)
  - [IndicatriceEuler](docs/cours7_phidEuler.pdf)
  - Signatures - définitions

#### 10 avril (11h20 -> 12h50):
  - [Signatures](docs/cours8.pdf)
  - [Diffie-Hellman](docs/Diffie-Hellman.pdf)

#### 17 avril (11h20 -> 12h50):
  - Attaque de l'homme du milieu
  - [Certificats](docs/cours10.pdf)


## Modalités d'évaluation :
  - 40% CC (deux notes)
  - 60% Examen

## Nouveaux Challenges : 

### Challenge 3 (Résolu): LFSR
  - Un LFSR de longueur 64 a engendré la suite chiffrante suivante (le premier bit est le premier bit de sortie, le deuxième est le deuxième bit sortie (de gauche à droite et de haut en bas):
  - 11011110111001011010
  - 01011010010101001000
  - 01100101111000111110
  - 01111101110001101010
  - 10101000000001100001
  - 00000010011110111000
  - 11101101101100100100
  - Pouvez-vous retrouver les Coefficients de rétroaction du LFSR ? Pour vous aider on vous donne le bout de code implémentant un LFSR en C. Votre réponse doît être la valeur de poly dans le code correspondant [code](docs/mainLFSR.c) en héxadécimal !

### Challenge 4 : Generateur de Geffe (modifié)
  - On a crée un chiffrement à flot sensiblement correspondant au générateur de Geffe.
  - Pour vous aider, on vous donne le code (en C) implémentant l'algorithme [code](docs/main_geffe_mod.c)
  - La suite chiffrante suivante a été observée. Pouvez-vous retrouver les états initiaux des générateurs ? Les valeurs à renvoyer doivent être données en héxadécimal !
  - 10011100100000001011
  - 01011011111100010001
  - 01110110010111010111
  - 11100001000111110110
  - 10101000001011110100
  - 11101000101001001001
  - 00101000001101101110
  - [Lien Formulaire Réponse](https://forms.gle/p4jCVH8weYp2gVpF8)

### Challenge 5 : Meet-in-the Middle pour les chiffrements à flots
  - Afin de palier à l'attaque précédante, nous allons utiliser de 3 LFSR filtrés (une fonction est appliquée à tout l'état. La sortie de ces trois fonctions est alors combinée au moyen d'un XOR afin de générer la suite chiffrante. Le code implémentant l'algorithme est donné [ici](docs/main_mitm.c)
  - Cependant, une autre attaque est possible. Pouvez-vous retrouver les valeurs des états initiaux générant la suite chiffrante suivante ? 
  - Les trois valeurs à renvoyer doivent être données en format héxadécimal.
  - 01011101011100110101
  - 11100110110101101000
  - 00111101011000001011
  - 01100101100000111001
  - 10011010100010011100
  - [Lien Formulaire Réponse](https://forms.gle/ck9ej5hesg1caiUW9)

## Enoncés des TDs
  - [TD1 - Les chiffrements historiques](docs/td1.pdf)
  - [TD2 - Enigma](docs/td2.pdf)
  - [TD3 - Chiffrements à flot](docs/td3.pdf)
  - [TD4 - Chiffrements par bloc](docs/td4.pdf)
  - [TD5 - DES et Modes](docs/td5.pdf)
  - [DES highlevel](docs/DES-highlevel.pdf)
  - [DES specs](docs/DES2111311.pdf)
  - [TD6 - Arithmétique modulaire](docs/td6.pdf)
  - [TD7 - RSA](docs/td7.pdf)
  - [TD8 - Tests de primalité](docs/td8.pdf)
  - [TD9 - Signatures numériques](docs/td9.pdf)
  - [TD10 - Diffie Hellman](docs/td10.pdf)
  - [TD11 - openssl (si temps)](docs/td11.pdf)


## Corrections des contrôles
  - Réalisée en TDs