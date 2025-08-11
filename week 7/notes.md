<ins> What is Principal Component Analysis (PCA) </ins>

A mathematical technique for finding patterns in heavy data and reducing its dimensionality while keeping as much important information as possible (for example in images)

# week 7 discussion

> Question: Face images are high dimensional data and when modeling their appearance there may only be a few underlying hidden factors which describe most of the variability. For two different images where one has more details compared to another, if we use the same number of PCAs, how would the corresponding MSE compare?

The image with more details would have a higher mean squared error (MSE) since the ML algorithm would need to have more principal components (PCs) to be able to accurately identify the image. Whereas for the image with less details the MSE would be lower since the ML algorithm can identify the image with not that many PCs since it does not have that many details to begin with. 

If more PCs aren't given in the detailed image then more information is lost in the detailed image, which leads to a high MSE. 
