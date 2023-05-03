Retour d'expérience sur la mise en place d'une application de consultation d'offres d'emploi

Introduction :
Dans ce retour d'expérience, je vais décrire le processus de mise en place d'une application permettant de consulter des offres d'emploi stockées dans une base de données. J'ai utilisé FileZilla pour la gestion de fichiers, Python pour la manipulation des données, et Streamlit pour la visualisation.

1. Mise en place du serveur FTP avec FileZilla :
J'ai commencé par installer et configurer un serveur FTP utilisant FileZilla. FileZilla est un outil performant et simple à utiliser, qui permet de mettre en place et de gérer un serveur FTP. Le serveur FTP devait permettre d’y déposer des offres d’emplois sous format CSV, n’ayant pas reçu de maquette j’ai dû en créer une et imaginer les différents items.

2. Récupération des fichiers CSV et transformation en DataFrames :
Après avoir configuré le serveur FTP, j'ai utilisé Python pour récupérer les fichiers CSV et les transformer en DataFrames. La bibliothèque Pandas a été essentielle pour cette étape, car elle offre des fonctionnalités puissantes pour manipuler et analyser les données tabulaires. Une fois les fichiers CSV convertis en DataFrames, j'ai pu explorer et nettoyer les données au besoin, par exemple trier les offres n’étant plus d’actualité en filtrant les « date de fin » qui était une des colonnes à traiter sous requête du commanditaire.

3. Stockage des données dans une base de données WampServer :
Une fois les DataFrames prêts, j'ai procédé à leur stockage dans une base de données MySQL sur WampServer. J'ai utilisé la bibliothèque SQLAlchemy pour faciliter la connexion et l'interaction avec la base de données. Cette étape a permis de conserver les données de manière structurée et accessible pour les étapes ultérieures.

4. Récupération des données et affichage avec Streamlit :
Enfin, j'ai utilisé Streamlit, une bibliothèque Python dédiée à la création d'applications web, pour afficher les données stockées dans la base de données. J'ai écrit un script Python pour récupérer les données de la base de données et les présenter dans un format facile à consulter et filtrables. Streamlit a rendu cette étape relativement simple, grâce à sa syntaxe intuitive et à ses nombreux composants intégrés pour la visualisation de données.


Conclusion :
En résumé, la mise en place de cette application de consultation d'offres d'emploi a été un processus enrichissant et éducatif. J'ai pu explorer différentes technologies et bibliothèques, telles que FileZilla, Python, Pandas, WampServer et Streamlit, pour créer une solution complète et fonctionnelle. Ce projet m'a également permis de renforcer mes compétences en manipulation de données, gestion de bases de données et développement d'applications web et même si pour le projet dans sa globalité il y a eu des soucis, pour ma partie tout s’est plutôt bien déroulé une fois la partie consultation via des bornes dans le metaverse mis de coté et la mise à disposition des offres consultables via une page web jugé suffisant.
