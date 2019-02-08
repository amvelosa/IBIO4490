# IBIO4490
This repository strictly follows the teorethical guidelines provided by the course "*IBIO4490 - Computer Vision*" at Uniandes. 
**2019**

#1.     What is the grep command?
#The grep command searches for PATTERN  in each FILE.  A FILE of “-” stands for standard input.  If no FILE is given, recurs$
#In addition, the variant programs egrep, fgrep and rgrep are the same as grep -E, grep -F, and grep -r, respectively.  Thes$

#2.     What is the meaning of #!/bin/python at the start of scripts?
#The line of code #!/bin/python  calls the language’s interpreter to run the code inside the scrip if it is executable.

#3.     Download using wget the bsds500 image segmentation database, and decompress it using tar (keep it in you hard drive
#, we will come back over this data in a few weeks).
wget http://www.eecs.berkeley.edu/Research/Projects/CS/vision/grouping/BSR/BSR_bsds500.tgz
tar -xzvf BSR
#4.     What is the disk size of the uncompressed dataset, How many images are in the directory 'BSR/BSDS500/data/images'?
du
# numero de imagenes en cada directorio 
find .-name"*.jpg" | wc -l
#74128
#5.     What are all the different resolutions? What is their format? Tip: use awk, sort, uniq
find ./BSR/BSDS500/data/images -name "*.jpg" -exec identify {} \; | awk '{print $2, $3}' | sort | uniq
# JPEG 481x321
#JPEG  321x481
#6.     How many of them are in landscape orientation (opposed to portrait)? Tip: use awk and cut
find ./BSR/BSDS500/data/images -name "*.jpg" -exec identify {} \; | awk '{print $3}'| fgrep -i '481X321' | wc -l
# 348
find ./BSR/BSDS500/data/images -name "*.jpg" -exec identify {} \; | awk '{print $3}'| fgrep -i '321X481' | wc -l
#152
#7.	Crop all images to make them square (256x256) and save them in a different folder. Tip: do not forget aboutimagemagick.
 identify -crop 256x256+0+0 2018.jpg
 #2018.jpg JPEG 321x481=>256x256 321x481+0+0 8-bit sRGB 0.000u 0:00.000

