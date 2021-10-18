from PIL import Image, ImageFilter, ImageDraw
from core.resampling import *
from core.halftoning import *
from core.thresholding import *

filename = "book12.jpg"

original = Image.open("Lab1/original/" + filename)

# new_image_up = resampling(original, 6)
# new_image_up.save("Lab1/res/upsampling2_" + filename)
#
# new_image_down = resampling(original, 1/3)
# new_image_down.save("Lab1/res/downsampling2_" + filename)

new_image_re = resampling(original, 1/3)
new_image_re.save("Lab1/res/resampling" + filename)

new_image_ht = halftone(original)
new_image_ht.show()
new_image_ht.save("Lab1/res/halftone" + filename)

halftoned = halftone(new_image_re)
B = [20, 40, 80] #окно
K = [0.2, 0.6, 0.8] #коэф

for b, k in [(b, k) for b in B for k in K]:
    print(b, k)
    halftoned = halftoned.convert(mode="RGB")
    new_image = kristian_threshold(image=halftoned, b=b, k=k)
    new_image.save(f"Lab1/res/threshold_b{b}_k{k}_{filename}")
