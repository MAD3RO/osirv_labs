## Setup

- Create new directory called `images` in this directory
- Copy images from Loomen to the directory images
- Complete the git tutorial from [Try Github](https://try.github.io)

## Problem 1 - Invert

- Create a program which will load all images from `images` directory in grayscale 
- perform the invert operation and 
- save the images to `problem1/imagename_invert.png`.

## Problem 2 - Threshold

- Create a program which will load all images from `images` directory
- perform the threshold operation with the parameter values of `63`, `127`, `191`
- save the images to `problem2/imagename_parametervalue_thresh.png`

## Problem 3 - Quantisation 
Usually, the grey values in an image are represented by $`2^8 = 256`$
different grey values. In this problem, we want to quantise the image
`BoatsColor.bmp` such that it contains afterwards only $`2^q`$ different grey
values, with $`q < 8`$.

In order to reduce the number of grey values we subdivide the co-domain into
uniform intervals of size $` d = 2^{8-q} `$. All values that lie in an
interval are then mapped to the mean value of the interval: 

```math
u_{i, j} :=  \left ( \left \lfloor \frac{ u_{i,j} }{d} \right \rfloor + \frac{1}{2} \right ) * d
```

<!--![quantize]( http://latex.codecogs.com/gif.latex?u_%7Bi%2C%20j%7D%20%3A%3D%20%5Cleft%20%28%20%5Cleft%20%5Clfloor%20%5Cfrac%7B%20u_%7Bi%2Cj%7D%20%7D%7Bd%7D%20%5Cright%20%5Crfloor%20&plus;%20%5Cfrac%7B1%7D%7B2%7D%20%5Cright%20%29%20*%20d)-->

Where $` \lfloor . \rfloor `$ denotes the floor function, i.e. 
$` \lfloor x \rfloor `$ gives the largest integer number that does not exceed
$` x `$.

#### Your task: 

- Perform the quantisation on the image 
` BoatsColor.bmp` 
for all values of $` q `$ in the interval  $` [ 1, 8 ] `$ . 
- Save the images as
`.bmp` files with the filename format ` boats_q.bmp `,  where ` q ` is the
numeric value of $` q `$ used for that image.  
- Comment the visual quality of quantised images compared to original image, for
all  values of  $` q `$.

[]()


##### Hints:

If ` img ` is numpy array containing your image: 

- Load the image as grayscale ( ` cv2.CV_LOAD_IMAGE_GRAYSCALE ` )
- Convert the image to _floats_ before processing ( ` img =
img.astype(np.float32) ` ) 
- Values greater than 255 set to 255, and values lower than 0 set to 0
- `np.max(img)` returns the
maximum value in the array, `np.min(img)` returns minimum value and
`np.unique(img)` returns a list of unique values in the array.
- `np.floor(img)` returns an array with _floored_ values.
- After processing, return the image back to ` np.uint8 ` dtype.


## Problem 4 - Noise

Integrate uniformly distributed noise $` n_{i,j} `$ with zero mean and
maximal deviation of $` 0.5 `$ into the quantisation process:

```math
u_{i, j} :=  \left ( \left \lfloor \frac{ u_{i,j} }{d} + n_{i,j} \right \rfloor + \frac{1}{2} \right ) * d
```

#### Your task:

- Perform the quantisation with the added noise, according to the formula
above. Use the same image and quantisation values as in Problem 3.
- Save the images as
`.bmp` files with the filename format ` boats_qn.bmp `,  where ` q ` is the
numeric value of $` q `$ used for that image.  
- Comment the visual quality of quantised images with noise compared to
quantised images in Problem 3, for all the values of $` q `$.

##### Hint:

- For generation of uniform noise use `np.random.uniform(0,1, shape )` numpy
function (`shape` is the shape of resulting array). 
See [Numpy
documentation](http://docs.scipy.org/doc/numpy/reference/routines.random.html).

# Report

Add your report here. Details about Markdown syntax can be found on the [link](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)
