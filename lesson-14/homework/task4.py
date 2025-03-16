import numpy as np
from PIL import Image

def flip_img_h(img_arr):
    """Flips image horizontally"""
    return img_arr[:, ::-1, :]

def flip_img_v(img_arr):
    """Flips image vertically"""
    return img_arr[::-1, :, :]

def add_noise(img_arr, mean=0, stddev=25):
    """Adds random noise"""
    noise = np.random.normal(mean, stddev, img_arr.shape).astype(np.int16)
    noisy_img = np.clip(img_arr.astype(np.int16) + noise, 0, 255).astype(np.uint8)
    return noisy_img

def brighten_channels(img_arr, value = 40):
    """Increase brightness of the channels"""
    brightened_img = np.clip(img_arr.astype(np.int16) + value, 0, 255).astype(np.uint8)
    return brightened_img

def apply_mask(img_arr, mask_size=(100, 100)):
    """Apply mask"""
    h, w, _ = img_arr.shape
    x_start = (w-mask_size[0])//2
    y_start = (h-mask_size[1])//2
    img_arr[y_start:y_start + mask_size[1], x_start:x_start + mask_size[0]] = (0, 0, 0)
    return img_arr

def main(image_path):
    """Read the image, apply transformations, and save the results"""
    with Image.open(image_path) as img:
        img_arr = np.array(img)

        flipped_h = flip_img_h(img_arr)
        flipped_v = flip_img_v(img_arr)
        added_noise = add_noise(img_arr)
        brightened = brighten_channels(img_arr)
        masked = apply_mask(img_arr.copy())

        Image.fromarray(flipped_h).save('horizontal.jpg')
        Image.fromarray(flipped_v).save('vertical.jpg')
        Image.fromarray(added_noise).save('noisy_img.jpg')
        Image.fromarray(brightened).save('brightened_img.jpg')
        Image.fromarray(masked).save('masked_img.jpg')

if __name__ == '__main__':
    main('birds.jpg')