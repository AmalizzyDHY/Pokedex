This feature focuses on image prediction and analysis using Pokémon sprites.





#### The database



Our database in /poke\_pics was gathered from : https://www.kaggle.com/datasets/divyanshusingh369/complete-pokemon-library-32k-images-and-csv, itself sourced from the PokémonDB database.



The database is composed of about 4 or 5 images for each Pokémon species, from gen 1 to 9. We therefore have ~1024 categories of Pokémon.





### Prediction test image

the prediction tests will be done on test.png. Feel free to swap it out with any other image.



test1.png is an image of a Krabby that exists within /poke\_pics.

test.png is an image of a Krabby that **does not** exists within /poke\_pics.





#### The code

##### 0 - installing dependencies



pip install numpy pandas scikit-learn plotly matplotlib opencv-python pillow tqdm torch torchvision





##### 1 - Template matching



**template\_matching.py** will compare test.png with the sprites in /poke\_pics using template matching - comparing images pixel by pixel.

It then tries to predict the pokemon in test.png, outputting its top 20 predictions.



This works well with images that are already in our database (with test1.png) but fails otherwise (with test.png).

We therefore need a more complex model.





##### 2 - Training model



We can train a Convolutional neural network model trained with resnet-18 on the sprites in /poke\_pics

**cnn\_train\_extract.py** will train the model and extract features and its auxiliairy information in pokemon\_features.npy and pokemon\_labels.npy.



**pokemon\_cnn.pt** is our trained model.



We can test this model with **predict\_test.py**. This outputs the model's top 5 predictions.





##### 3 - clustering



**clustering.py** uses pokemon\_features.npy and pokemon\_labels.npy to try and map and cluster Pokémons based on their appearance.



The script then outputs the mapping to **pokemon\_clusters\_tsne.html**, using T-SNE.



Clustering is done with k-means, and the number of clusters can be determined with the elbow method : k≈50

























