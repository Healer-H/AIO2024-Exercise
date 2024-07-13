import numpy as np
import streamlit as st
from PIL import Image


def convert_to_grayscale_by_lightness(image):
    max_channel = image.max(axis=2)
    min_channel = image.min(axis=2)

    gray_scale = (min_channel + max_channel) / 2
    return gray_scale.astype(np.uint8)


def convert_to_grayscale_by_average(image):
    gray_scale = np.mean(image, axis=2)
    return gray_scale.astype(np.uint8)


def convert_to_grayscale_by_luminosity(image):
    gray_scale = 0.21 * image[:, :, 0] + 0.72 * \
        image[:, :, 1] + 0.07 * image[:, :, 2]
    return gray_scale.astype(np.uint8)


def main():
    st.title("Upload an Image to convert to grayscale")
    uploader_files = st.file_uploader(label="Pick some images...", type=[
                                      'png', 'jpg', 'jpeg'], accept_multiple_files=True)
    for uploader_file in uploader_files:
        if uploader_file is not None:
            original_image = Image.open(uploader_file)
            original_image = np.array(original_image)
            lightness_image = convert_to_grayscale_by_lightness(original_image)
            average_image = convert_to_grayscale_by_average(original_image)
            luminosity_image = convert_to_grayscale_by_luminosity(
                original_image)

            col1, col2, col3, col4 = st.columns(4)

            with col1:
                st.image(original_image, "Original Image",
                         use_column_width=True)
            with col2:
                st.image(lightness_image, "Lightness Image",
                         use_column_width=True, clamp=True)
            with col3:
                st.image(average_image, "Average Image",
                         use_column_width=True, clamp=True)
            with col4:
                st.image(luminosity_image, "Luminosity Image",
                         use_column_width=True, clamp=True)


if __name__ == "__main__":
    main()
