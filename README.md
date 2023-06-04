# mnist_tf2

<img src='./img/CC-BY-SA.jpeg' width=100 style="vertical-align:middle; float:left"> &emsp; jean-luc.charles@ensam.eu 

## Reconnaissance de chiffres écrits à la main

Cette activité propose la construction, l'entraînement et l'évaluation de réseaux de neurones dédiés à la reconnaissance de chiffres écrits à la main provenant de la banque de données MNIST.

Deux TP sont proposés sous forme de notebooks jupyter 'à trous' :

- `TP1_MNIST_dense.ipynb` : rappels sur des concepts fondamentaux en ML (neurone artificiel, fonction d'activation, *one-hot coding*, catégorisation des labels, entraînement du réseau, affichage de la matrice de confusion...).
Le notebook aborde ensuite la construction d'un réseau dense à 2 couches, et son antraînement pour la reconnaissance des chifres MNIST, avec une précision qui voisine de 98 %.

- `TP2_MNIST_convol.ipynb` : construction d'un réseau convolutionnel pour la reconnaissance des chifres MNIST qui peut atteindre 99 % de réusssite.

En cas de blocage pour compléter les notebook 'à trous', les notebooks `Sol_TP1_MNIST.ipynb` et `Sol_TP2_MNIST.ipynb` présentent des solutions pour TP1  et TP2. Les solutions sont présentées exécutées dans les notebooks `Sol_TP1_MNIST-executed.ipynb` et `Sol_TP2_MNIST-executed.ipynb`. 

À la suite de ces TP, tu pourras créer tes propres images de chiffres écrits à la main pour tester les performances des réseaux entraînés.


## Principaux points abordés dans les TP

- neurone artificiel,
- réseau de neurones,
- fonction d'activation,
- téléchargement et visualisation des images MNIST (*handwritten digits*),
- préparation des images et des labels pour entraÎner le réseau de neurones,
- construction d'un réseau de neurones dense puis convolutionnel avec tensorFlow-keras,
- entraînement des réseaux,
- courbes de précision et de perte,
- matrice de confusion,
- `callback` tensorflow `Early Stopping` pour éviter le sur-entraînement.
- exploitation des réseaux avec des chiffres manuscrits hors banque MNIST.


# Acquis d'apprentissage

À l'issue de cette activité, tu sauras :
- Télécharger les images de la banque MNIST avec le module Python keras.
- À la suite du TP1, tu sauras utiliser les modules tensorflow2 & keras pour développer et évaluer un réseau de neurone dense dédié à la reconnaissance des images MNIST.
- À la suite du TP2, tu sauras utiliser les modules tensorflow2 & keras pour développer et évaluer un réseau de neurone convolutif dédié à la reconnaissance des images MNIST.
- Utiliser tes propres images de chiffres écrits à la main pour évaluer les réponse d'un réseau de neurones entraîné avec la banque MNIST.
