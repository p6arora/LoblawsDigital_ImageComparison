import cv2
import numpy as np

#read from CSV file

# reading images
def read_images():
    original_image = cv2.imread("original_golden_bridge.jpg")
    compared_image = cv2.imread("images/blurred.jpg")
    print("Read images")
    
def check_identical():
    # if images are the same shape and size - could be identical
    if original_image.shape == compared_image.shape:
        print("Images have the same size and channel")
        difference = cv2.subtract(original_image, compared_image)   # subtract RGB values between images to see difference between image organization
        b,g, r = cv2.split(difference)

        # if RGB value difference is 0 - same image
        if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
            print("The images are completely Equal")
    
# if images are not identical:
# use OpenCV's SIFT Algorithm to find key points and features between images
def generate_keypoints:
    sift = cv2.xfeatures2d.SIFT_create()
    key_point_image1, descriptor_image1 = sift.detectAndCompute(original_image, None)
    key_point_image2, descriptor_image2 = sift.detectAndCompute(compared_image, None)

# FLANN - Fast Library for Approximate Neighbors
# uses Euclidean distance between common key points to judge similarity  
def compare_images():
    index_params = dict(algorithm=0, trees=5)
    search_params = dict()
    flann = cv2.FlannBasedMatcher(index_params, search_params)
    matches = flann.knnMatch(descriptor_image1, descriptor_image2, k=2)
    
# SIFT algorithm has high recall, but low precision
# so a threshold ratio needs to be set to filter inacurate results
def filter_results():
    good_points = []
    ratio = 0.6 # approximated through trial and error
    print("Matches:" + str(len(matches)))
    for m, n in matches:
            if m.distance < ratio*n.distance:
                    good_points.append(m)
    print("Good Matches: " + str(len(good_points)))
    

# Generate Similarity Score
def generate_similarity_score(correct_matches: int, total_matches: int ):
    return correct_matches/total_matches

# Publish to CSV
def publish_results(ratio: float):
    

