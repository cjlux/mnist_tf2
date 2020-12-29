# mnist_tf2

Hand-made digits recognition with tensorflow2

Cette activité propose la programmation, l'entraînement et l'évaluation de réseaux de neurones dédiés à la reconnaissance de chiffres écrits à la main provenant de la banque de données MNIST.

Plusieurs TP sont proposés sous forme de noetbooks jupyter, en fonction de votre expérience en *Machine Learning* (ML) :

- `TP1_MNIST_dense.ipynb` : notebook 'à trous' s'adressant plutôt à des débutants en ML avec la construction d'un réseau dense à 2 couches, permettant une précision de reconnaissance des chifres MNIST qui plafonne vers 98 %.

- `TP2_MNIST_dense_overfit.ipynb` : notebook complément au TP1 montrant comment utiliser un `callback` tensorflow `Early Stopping` pour éviter le sur-entraînement.

- `TP2_MNIST_convol.ipynb` : notebook 'à trous' pour un niveau plus avancé avec la construction d'un réseau convolutionnel pour la reconnaissance des chifres MNIST qui peut atteindre 99 % de réusssite.

En cas de blocage pour compléter les notebook 'à trous', le répertoire `solutions` contient des propositions de solution spour les notebooks du TP1  et TP2.


À la suite de ces TP, tu pourras créer un service ROS qui utilise un réseau de neurones entraîné à reconnaître les chiffres ('1' ou '2') écrits sur les cube pris en photo par la caméra du bras manipulateur utilisé.


## Principaux points abordés dans les TP

- neurone artificiel,
- réseau de neurones,
- fonction d'activation,
- téléchargement et visualisation des images MNIST (*handwritten digits*),
- préparation des images et des labels pour entraÎner le réseau de neurones,
- programmation d'un réseau de neurones dense puis convolutionnel avec tensorFlow-keras,
- entraînement des réseaux,
- courbes de précision et de perte,
- utilisation d'un `callback` tensorflow `Early Stopping` pour éviter le sur-entraînement.
- exploitation des réseaux avec des chiffres manuscrits hors banque MNIST.
