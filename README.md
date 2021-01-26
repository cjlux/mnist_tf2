# mnist_tf2

Hand-made digits recognition with tensorflow2

Cette activité propose la programmation, l'entraînement et l'évaluation de réseaux de neurones dédiés à la reconnaissance de chiffres écrits à la main provenant de la banque de données MNIST.

Deux TP sont proposés sous forme de notebooks jupyter 'à trous' :

- `TP1_MNIST_dense.ipynb` : présente des rappels sur des concepts de base utiles en ML (neurone artificiel, fonctions d'activations, *one-hot coding*, catégorisation des labels, entraînement du réseau, affichage de la matrice de confusion...).
Le notebook aborde ensuite la construction d'un réseau dense à 2 couches, permettant de reconnaissance les chifres MNIST avec une précision qui voisine de 98 %.

- `TP2_MNIST_convol.ipynb` : aborde la construction d'un réseau convolutionnel pour la reconnaissance des chifres MNIST qui peut atteindre 99 % de réusssite.

En cas de blocage pour compléter les notebook 'à trous', les notebooks `Sol_TP1_MNIST.ipynb` et `Sol_TP2_MNIST.ipynb` suggèrent des propositions de solution pour TP1  et TP2. Les solutions sont présentées exécutées dans les notebooks `Sol_TP1_MNIST-full.ipynb` et `Sol_TP2_MNIST-fuul.ipynb`. 

À la suite de ces TP, tu pourras créer tes propres images de chiffres écrits à la main pour tester les performances des réseaux entraînés.


## Principaux points abordés dans les TP

- neurone artificiel,
- réseau de neurones,
- fonction d'activation,
- téléchargement et visualisation des images MNIST (*handwritten digits*),
- préparation des images et des labels pour entraÎner le réseau de neurones,
- programmation d'un réseau de neurones dense puis convolutionnel avec tensorFlow-keras,
- entraînement des réseaux,
- courbes de précision et de perte,
- matrice de confusion,
- `callback` tensorflow `Early Stopping` pour éviter le sur-entraînement.
- exploitation des réseaux avec des chiffres manuscrits hors banque MNIST.
