import numpy as np
import cv2
import streamlit as st
from PIL import Image
def compute_difference(background, object):
    difference = object - background
    print(f"Background: {background}")
    print(f"Object: {object}")
    print(f"Difference: {difference}")
    return difference

def compute_binary_mask(differnce, threshold=15):
    mask = np.where(differnce > threshold, 1, 0)
    return mask

def replace_background(background, object, target):
    difference = compute_difference(background, object)
    mask = compute_binary_mask(difference)
    output = np.where(mask == 1, object, target)
    
    return output

def main():
    st.title("Background Subtraction and Replacement")

    col1, col2 = st.columns(2)

    with col1:
        st.header("Input Images")

        background_file = st.file_uploader("Upload Original Background Image", type=["jpg", "png", "jpeg"], key="background")
        object_file = st.file_uploader("Upload Object Image", type=["jpg", "png", "jpeg"], key="object")
        target_file = st.file_uploader("Upload Target Background Image", type=["jpg", "png", "jpeg"], key="target")

        if background_file and object_file and target_file:
            background = Image.open(background_file)
            object_img = Image.open(object_file)
            target = Image.open(target_file)

            background_np = np.array(background)
            object_np = np.array(object_img)
            target_np = np.array(target)
            
            
            background_np = cv2.cvtColor(background_np, cv2.COLOR_BGRA2BGR)
            object_np = cv2.cvtColor(object_np, cv2.COLOR_BGRA2BGR)
            
            print(f"background shape: {background_np.shape}")
            print(f"object shape: {object_np.shape}")
            print(f"target shape: {target_np.shape}")

            shape = (678, 381)
            background_np = cv2.resize(background_np, shape)
            object_np = cv2.resize(object_np, shape)
            target_np = cv2.resize(target_np, shape)

            st.image(background, caption="Original Background", use_column_width=True)
            st.image(object_img, caption="Object Image", use_column_width=True)
            st.image(target, caption="Target Background", use_column_width=True)

    with col2:
        st.header("Output Image")

        if background_file and object_file and target_file:
            output_np = replace_background(background_np, object_np, target_np)
            output_img = Image.fromarray(output_np.astype('uint8'))

            st.image(output_img, caption="Output Image", use_column_width=True)


if __name__ == "__main__":
    main()