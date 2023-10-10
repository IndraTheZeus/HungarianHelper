# HungarianHelper
Members of group: name + neptun code
1. Indra Narayan Dutta NSN8A7

# Hungarian - English Convolutional Text Detection
1. A FCNN is trained on a database of hungarian labelled character images ( Just individual characters)
2. The FCNN is used to label an un-labelled collection of image data by iteratively going through each segment of an unlabelled image and finding maximum confidence bounding boxes. This step converts un-labelled dataset to a labelled one
3.  A CNN is trained on this new dataset to find character bounding boxes quickly in a natural scene image containing both text and natural scene objects( Some images are hand-labelled, others get labelled by the FCNN) 
4. The FCNN predicts the characters present in the CNNs output bounding box. 


