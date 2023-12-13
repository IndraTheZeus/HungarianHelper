
# HungarianHelper
Members of group: name + neptun code
1. Indra Narayan Dutta NSN8A7

# Hungarian - English Convolutional Text Detection
1. An FCNN is trained on a database of Hungarian labeled character images ( Just individual characters)

# Dataset Description
The Dataset consists of Images collected from the following sources

1. bartosgaye_ver1 - handwritten character dataset consisting of characters a to z and 6 Hungarian special characters. (Datasource: https://github.com/bartosgaye/thedataset)
2. bartosgaye_ver6 - handwritten character dataset of just 6 Hungarian special characters. (Datasource: https://github.com/bartosgaye/thedataset)
3. challenge2 - Scene text English character dataset extracted from ICDAR Robust Reading Challenge (Datasource: https://rrc.cvc.uab.es/?ch=2&com=downloads)
4. icdar2003_chars - Scene text English characters dataset extracted from ICDAR 2003 Challenge ( Datsource: http://www.iapr-tc11.org/mediawiki/index.php/ICDAR_2003_Robust_Reading_Competitions)
4. icdar2003_chars_test - Test dataset of the ICDAR 2003 challenge also added
 
When doing the train-test split using DataCombiner, we make sure to divide the test and train data have the same distribution of images from each of the sources


#Scripts
1. csvReader_bartosgye.py - Used to read the CSV files from https://github.com/bartosgaye/thedataset. The CSV files are N x 785 dimension arrays. The first index is the index of the character, and the 784 remaining positions are the image binary values (1 is foreground) for a 28 x 28 image. 
2. challenge2_chracterExtracter.py - Used to crop and extract individual characters from the ICDAR Robust Reading Challenge
3. icdar2003_charSeperator.py - Reads the XML tree provided by icdar 2003 and separates characters into individual classes
4. DataCombiner.py - Combines data across all folders from all datasets and separates them into 70 classes 

Final Dataset count:
Train: 131637 Images 
Test: 32915 Images

Dataset Link: Shared on Moodle

# Training Code
All of the Training Code as been provided in the HungarianHelper.ipynb notebook. For running the code you need to provide Training and Test Data in the following format:

'''bash
Dataset/
├── Test/                               // TEST IMAGES
│ ├── 1/               // Class Label for images  ( 1 to 70 )
│ │ ├── image1.jpg      // Each Class Label has variable number of images
│ │ ├── image2.jpg
│ │ └── ...
│ ├── 2/
│ │ ├── image1.jpg
│ │ ├── image2.jpg
│ │ └── ...
│ ├── 3/
│ │ ├── image1.jpg
│ │ ├── image2.jpg
│ │ └── ...
│ └── ...
└── Train/                               //TRAIN IMAGES
├── 1/
│ ├── image1.jpg
│ ├── image2.jpg
│ └── ...
├── 2/
│ ├── image1.jpg
│ ├── image2.jpg
│ └── ...
├── 3/
│ ├── image1.jpg
│ ├── image2.jpg
│ └── ...
└── ...
'''

No Validation Set needs to be provided since the code automatically keeps 20% of the Train set for validation

### CLASSES LABELS
| a-1  | t-20 | E-40 | Y-60 |
|------|------|------|------|
| b-2  | u-21 | F-41 | Z-61 |
| c-3  | v-22 | G-42 | Ö-62 |
| d-4  | w-23 | H-43 | Ü-63 |
| e-5  | x-24 | I-44 | Á-64 |
| f-6  | y-25 | J-45 | É-65 |
| g-7  | z-26 | K-46 | Í-66 |
| h-8  | ö-27 | L-47 | Ó-67 |
| i-9  | ü-28 | M-48 | Ő-68 |
| j-10 | á-29 | N-49 | Ú-69 |
| k-11 | é-30 | O-50 | Ű-70 |
| l-12 | í-31 | P-51 |  
| m-13 | ó-32 | Q-52 | 
| n-14 | ő-33 | R-53 | 
| o-15 | ú-34 | S-54 | 
| p-16 | ű-35 | T-55 | 
| q-17 | A-36 | U-56 | 
| r-18 | B-37 | V-57 | 
| s-19 | C-38 | W-58 | 
|      | D-39 | X-59 |  

### MODEL PARAMETERS
1. image_dims = (3,32,32) -> Sets the dimensions of the input image. The
bartosgye character dataset is a 28x28 character dataset so higher dimensions
might distort the image.
2. lr = 0.002 -> Learning rate for adam optimizer
3. epochs = 500 -> Total epochs to run training for
4. batch_size = 128 -> Batch size to feed to training


