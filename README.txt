This plugin creates a mask based on values in the longest wavelength 
band available in a multispectral image. The user can set a threshold 
value. Pixels with a value below that threshold are considered to be 
water while those above are considered to be land. A connectivity 
threshold can also be set so that isolated pixels identified as water
can be eliminated. This reduces the number of shadowed areas on land 
that are misclassified as water and ensures that the pixels identified 
as water are continuous.

This plugin needs more testing and documentation before it has the 
expirimental flag turned off.
