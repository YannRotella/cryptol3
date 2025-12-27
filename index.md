---
title: Home
---
Cours de Licence 3 décrivant les bases de la cryptographie moderne. Histoire de la cryptographie, cryptographie symétrique, théorie de Shannon (Information, Entropie), concepts et définitions de Sécurité, stratégies de conceptions, cryptanalyse, fonctions de hachage cryptographiques, modes, MACs, AEAD. Cryptographie asymétrique, Échange de clefs, chiffrements (ElGamal, RSA-OAEP), Signatures (RSA, DSA), randomisation, IND-CPA, authentification. Certificats, protocoles et notion de confiance.

## Informations pratiques

12 Cours Magistraux d'une heure 30, 12 TDs de 3 heures. Se référer à [CELCAT](https://edt.uvsq.fr/cal?vt=month&dt=2026-01-01&et=module&fid0=LSIN603)

Les cours ont lieu globalement les jeudi matins et les TDs ont lieu Lundi après-midi (TD 3), mercredi après-midi (TD 1) ou jeudi après-midi (TD 2).

**Responsable du cours :** [Yann Rotella](https://rotella.fr/)

**Chargés de TD :** [Jules Baudrin](https://baudrin-j.github.io/) (TD 1), Maxime Louvet (TD 3) et Yann Rotella (TD 2)

## Modélités d'évaluation

Contrôle Continu 40% et Examen 60%

#### CC 1:
  - Le mardi 10 mars 2026

#### CC 2:
  - Le mardi 21 avril 2026

#### CC de rattrapage
  - Le Jeudi 7 mai 2026
  - Remplace la ou les notes
  - Uniquement si ABJ

#### Examen:
  - TBA

## Programme des Cours Magistraux

#### 22 janvier (11h20 -> 15h20): Deux cours. Histoire de la Cryptographie et Théorie de Shannon
  - [Présentation du cours](docs/cours0.pdf)
  - [Histoire de la Cryptographie](docs/cours1.pdf)
  - [Théorie de Shannon](docs/cours2.pdf)

#### 12 février (11h20 -> 12h50): Définitions de sécurité, Oracles, Réductions et Définitions
  - [Définitions de Sécurité](docs/cours3.pdf)

#### 19 février (11h20 -> 12h50): Stratégies de Conception des Chiffrements par Bloc, ou comment construire des PRPs 
  - [Stratégies de Conception](docs/cours4.pdf)
  - Pour aller plus loin: le cours de C. Boura sur les [chiffrements à flots](docs/ChiffrementAFlot.pdf)

#### 26 février (11h20 -> 12h50): Cryptanalyse des Chiffrements par bloc, un critère nécessaire (mais toujours pas suffisant)
  - [Cryptanalyse des Chiffrements par bloc](docs/cours5.pdf)

#### 12 mars (11h20 -> 12h50): Fonctions de hachage cryptographiques - la primitive sans clef très utile
  - [Fonctions de hachage cryptographiques](docs/cours6.pdf)

#### 19 mars (11h20 -> 12h50): Modes opératoires et Authentification, Confidentialité, Intégrité et Authenticité
  - Retour sur le premier CC
  - [Modes opératoires et Authentification](docs/cours7.pdf)

#### 26 mars (11h20 -> 12h50): Algèbre (groupes) et Cryptographie à clef publique
  - [Algèbre et Cryptographie à Clef Publique](docs/cours8.pdf)
  - Un peu plus de détail ici: [Groupes cycliques et Diffie-Hellman](docs/Diffie-Hellman.pdf)

#### 2 avril (11h20 -> 12h50): RSA - Rivest Shamir Adleman
  - [RSA](docs/cours9.pdf)
  - Un peu plus de détail avec quelques cours de C. Boura:
  - [RSA - tests de primalités - générations des clefs](docs/RSA_TestsDePrimalite.pdf)
  - [La fonction Phi d'Euler](docs/cours7_phidEuler.pdf)

#### 9 avril (11h20 -> 12h50): Signatures Numériques, Authentification, RSA, DSA et point d'étape
  - [Signatures Numériques](docs/cours10.pdf)
  - Un document sur les signatures numériques de C. Boura: [Signatures](docs/cours8_signatures.pdf)

#### 16 avril (11h20 -> 12h50): Certificats et Infrastructures à Clefs Publiques, Cryptographie et Réalité pratique
  - [Certificats](docs/cours11.pdf)
  - Le cours de C. Boura sur les [certificats et les PKI](docs/cours10_certificatsPKI.pdf)

#### 23 avril (11h20 -> 12h50): Cryptographie avancée, un aperçu (bref)
  - [Cryptographie avancée](docs/cours12.pdf)

## Les Sujets de Travaux Dirigés

  - [Séance 1 - TD - Chiffrements historiques](docs/01_TD_chiffrementshistoriques.pdf)
  - [Séance 2 - TP - Cryptanalyse à chiffrés connus](docs/02_TP_Chiffrementshistoriques.pdf)
  - [Séance 3 - TD - Entropie, Information et Chiffrements parfaits](docs/03_TD_EntropieetReductions.pdf)
  - [Séance 4 - TD - Réductions et Définitions de sécurité](docs/04_TD_Reductions.pdf)
  - [Séance 5 - TD - Chiffrements par bloc](docs/05_TD_ChiffrementsParBloc.pdf)
  - [Séance 6 - TP - Cryptanalyse](docs/06_TP_Cryptanalyse.pdf)
  - [Séance 7 - TD - Modes, Hashage et Authentification](docs/07_TD_ModesEtAuthentification.pdf)
  - [Séance 8 - TD/TP - Arithmétique et Programmation](docs/08_TD_CryptographieAsymetrique.pdf)
  - [Séance 9 - TD - RSA](docs/09_TD_RSA.pdf)
  - [Séance 10 (et 11) - TP - Cryptanalyse des Chiffrements Asymétriques](docs/10_CryptographieAsymetriqueProg.pdf)
  - [Séance 11 et 12 - TD/TP - Signatures et Certificats](docs/11_12_TP_last_applications.pdf)

## Les liens pour les fichiers nécessaires pour certains TP

  - [TD6 - exo 1](docs/td6_exo1.py)
  - [TD6 - exo 2](docs/td6_exo2.py)
  - [TD6 - exo 3](docs/td6_exo3.py)
  - [TD12 - Certificat](docs/CACertif.pem)
  - [TD 12 - confiance 1](docs/confiance1.txt)
  - [TD 12 - confiance 2](docs/confiance2.txt)
  - [TD 12 - Req Config File](docs/req.cnf)
  - [TD 12 - signature 1](docs/sign1)
  - [TD 12 - signature 2](docs/sign2)
  - [TD 12 - Clé publique de votre enseignant](docs/publicKeyRotella.pem)

## Sujets des années précédentes

#### 2025
  - [CC1](docs/2025_cc1.pdf)
  - [CC2](docs/2025_cc2.pdf)
  - [Examen](docs/2025_exam.pdf)
  - [Rat](docs/2025_rattrapage.pdf)
