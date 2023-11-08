
# HungarianHelper
Members of group: name + neptun code
1. Indra Narayan Dutta NSN8A7

# Hungarian - English Convolutional Text Detection
1. An FCNN is trained on a database of Hungarian labeled character images ( Just individual characters)

# Dataset Description
1. bartosgaye_ver1 - handwritten character dataset consisting of characters a to z and 6 Hungarian special characters. (Datasource: https://github.com/bartosgaye/thedataset)
2. bartosgaye_ver6 - handwritten character dataset of just 6 Hungarian special characters. (Datasource: https://github.com/bartosgaye/thedataset)
3. challenge2 - Scene text English character dataset extracted from ICDAR Robust Reading Challenge (Datasource: https://rrc.cvc.uab.es/?ch=2&com=downloads)
4. icdar2003_chars - Scene text English characters dataset extracted from ICDAR 2003 Challenge ( Datsource: http://www.iapr-tc11.org/mediawiki/index.php/ICDAR_2003_Robust_Reading_Competitions)
4. icdar2003_chars_test - Test dataset of the ICDAR 2003 challenge also added 


#Scripts
1. csvReader_bartosgye.py - Used to read the CSV files from https://github.com/bartosgaye/thedataset. The CSV files are N x 785 dimension arrays. The first index is the index of the character, and the 784 remaining positions are the image binary values (1 is foreground) for a 28 x 28 image. 
2. challenge2_chracterExtracter.py - Used to crop and extract individual characters from the ICDAR Robust Reading Challenge
3. icdar2003_charSeperator.py - Reads the XML tree provided by icdar 2003 and separates characters into individual classes
4. DataCombiner.py - Combines data across all folders from all datasets and separates them into 70 classes 

Final Dataset count:
Train: 131637 Images 
Test: 32915 Images

Dataset Link: https://drive.google.com/file/d/1zrjxe1Om-K32vI-JMaMlckJVhMOo9n2v/view?usp=sharing




