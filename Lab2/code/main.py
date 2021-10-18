from PIL import Image, ImageChops
import os.path

from core.filtering import median
from core.halftoning import halftone
from core.thresholding import kristian_threshold
from core.filtering import add_salt_and_pepper

filename = "book11.jpg"
B = 20
K = 0.4
s_vs_p = 1.0
amount = 0.05
save_dir = f"../res/{filename}_svsp{s_vs_p}_amount{amount}"
threshold_name = f"{save_dir}/threshold_B{B}K{K}_{filename}"

try:
    os.mkdir(save_dir)
except OSError:
    pass

if not os.path.exists(threshold_name):
    original = Image.open("../original/" + filename)
    halftone_f2 = halftone(original).convert("RGB")
    threshold = kristian_threshold(image=halftone_f2, b=B, k=K)
    threshold.save(threshold_name)
    print("Done threshold")

original = Image.open(threshold_name)

original_with_salt = add_salt_and_pepper(original, amount, s_vs_p)
original_with_salt.save(f"{save_dir}/with_salt_{s_vs_p}_{amount}_{filename}")

plane = \
    [[1, 1, 1],
     [1, 1, 1],
     [1, 1, 1]]

cross = \
    [[0, 1, 0],
     [1, 1, 1],
     [0, 1, 0]]

x_cross = \
    [[1, 0, 1],
     [0, 1, 0],
     [1, 0, 1]]

median_x_cross = median(original_with_salt, x_cross)
median_x_cross.save(f"{save_dir}/median_x_cross_{s_vs_p}_{amount}_{filename}")
print("Done median_x_cross")

xor_x_cross = ImageChops.logical_xor(original_with_salt.convert("1"), median_x_cross.convert("1"))
xor_x_cross.save(f"{save_dir}/xor_x_cross_{s_vs_p}_{amount}_{filename}")
print("Done XOR median_x_cross")

median_cross = median(original_with_salt, cross)
median_cross.save(f"{save_dir}/median_cross_{s_vs_p}_{amount}_{filename}")
print("Done median_cross")

xor_cross = ImageChops.logical_xor(original_with_salt.convert("1"), median_cross.convert("1"))
xor_cross.save(f"{save_dir}/xor_cross_{s_vs_p}_{amount}_{filename}")
print("Done XOR median_cross")

median_plane = median(original_with_salt, plane)
median_plane.save(f"{save_dir}/median_plane_{s_vs_p}_{amount}_{filename}")
print("Done median_plane")

xor_plane = ImageChops.logical_xor(original_with_salt.convert("1"), median_plane.convert("1"))
xor_plane.save(f"{save_dir}/xor_plane_{s_vs_p}_{amount}_{filename}")
print("Done XOR median_plane")

xor_cross_x_cross = ImageChops.logical_xor(median_x_cross.convert("1"), median_cross.convert("1"))
xor_cross_x_cross.save(f"{save_dir}/xor_cross_x_cross_{s_vs_p}_{amount}_{filename}")
print("Done XOR cross_x_cross")

xor_cross_plane = ImageChops.logical_xor(median_cross.convert("1"), median_plane.convert("1"))
xor_cross_plane.save(f"{save_dir}/xor_cross_plane_{s_vs_p}_{amount}_{filename}")
print("Done XOR cross_plane")

xor_x_cross_plane = ImageChops.logical_xor(median_x_cross.convert("1"), median_plane.convert("1"))
xor_x_cross_plane.save(f"{save_dir}/xor_x_cross_plane_{s_vs_p}_{amount}_{filename}")
print("Done XOR cross_plane")