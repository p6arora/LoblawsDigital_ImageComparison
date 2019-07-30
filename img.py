import cv2
import csv
import time

#read from CSV file
def read_data():
    print("starting to read data")
    with open('input_test_data.csv') as input_data:
        print("opened data file")
        global line_count
        csv_reader = csv.reader(input_data, delimiter=',')
        set_of_images=[row for idx, row in enumerate(csv_reader) if idx == line_count]
        print(set_of_images)
        original_image = set_of_images[0][0]
        image_to_compare = set_of_images[0][1]
        line_count += 1
        return [original_image, image_to_compare]

# write column titles for result CSV file
def write_header():
    global line_count
    with open('result_data.csv', mode='w') as result:
        result_writer = csv.writer(result, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        result_writer.writerow(['image1', 'image2', 'similarity_ratio', 'time_elapsed'])
    print('wrote result header')
    line_count += 1

# count total number of entries in CSV file
def count_images():
    with open('input_test_data.csv') as input_data:
        print("counting number of rows in CSV file")
        csv_reader = csv.reader(input_data, delimiter=',')
        return sum(1 for row in csv_reader)


# reading images
def read_images(original_img: str, image_to_compare: str):
    original_image = cv2.imread(original_img)
    compared_image = cv2.imread(image_to_compare)
    print("Read images")
    return [original_image, compared_image]
    

# preliminary check if RGB values are same 
def check_identical(original_image , compared_image , start_time: float, image_names):
    # if images are the same shape and size - could be identical
    if original_image.shape == compared_image.shape:
        print("Images have the same size and channel")
        difference = cv2.subtract(original_image, compared_image)   # subtract RGB values between images to see difference between image organization
        b,g, r = cv2.split(difference)

        # if RGB value difference is 0 - same image
        if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
            publish_results(image_names[0], image_names[1], 0.0,  start_time)
            print("The images are completely Equal")
            return True
            
        else:
            print("The images are NOT completely Equal")
            return False

# if images are not identical:
# use OpenCV's SIFT Algorithm to find key points and features between images
def generate_keypoints(original_image: str, compared_image: str):
    sift = cv2.xfeatures2d.SIFT_create()
    key_point_image1, descriptor_image1 = sift.detectAndCompute(original_image, None)
    key_point_image2, descriptor_image2 = sift.detectAndCompute(compared_image, None)
    print("Generated keypoints for both images")
    return [key_point_image1, descriptor_image1, key_point_image2, descriptor_image2]

# FLANN - Fast Library for Approximate Neighbors
# uses Euclidean distance between common key points to judge similarity  
def compare_images(key_point_image1, descriptor_image1, key_point_image2, descriptor_image2  ):
    index_params = dict(algorithm=0, trees=5)
    search_params = dict()
    flann = cv2.FlannBasedMatcher(index_params, search_params)
    matches = flann.knnMatch(descriptor_image1, descriptor_image2, k=2)
    print("found common points in images")
    return matches
    
# SIFT algorithm has high recall, but low precision
# so a threshold ratio needs to be set to filter inacurate results
def filter_results(matches: enumerate):
    good_points = 0
    ratio = 0.6 # approximated through trial and error
    print("Matches:" + str(len(matches)))
    for m, n in matches:
            if m.distance < ratio*n.distance:
                    good_points += 1
    print("Good Matches: " + str(good_points))
    return [good_points, len(matches)]
    

# Generate Similarity Score
def generate_similarity_score(correct_matches: int, total_matches: int ):
    return 1.0 - correct_matches/total_matches   # as defined in requirements, values close to 0 is most similar, so more correct matches mean similar pictures

# Publish to CSV
def publish_results(original_img: str, image_to_compare: str, similarity_ratio , start_time):
    print("writing to CSV file...")
    with open('result_data.csv', mode='a', newline='') as result:
        result_writer = csv.writer(result, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        result_writer.writerow([original_img, image_to_compare, str(similarity_ratio), str(round(time.time() - start_time, 2))] )
        print("Write successful")

# Main Function
# reading data from CSV
print("starting program")
line_count = 0

# find number of items in CSV file to compare
total_images_to_compare = count_images()

# prepare column titles for result CSV file
write_header()

for img in range(line_count, total_images_to_compare):

    # start recording execution time
    start_time = time.time()

    # read set of images
    image_names = read_data()

    # read original image and image to compare into memory
    images = read_images(image_names[0], image_names[1])


    # determine if identical images
    if (check_identical(images[0], images[1], start_time, image_names)):
        continue
       
    print("images NOT EQUAL - starting SIFT")

    # if images are not equal - start using SIFT to generate keypoints and features of both images to measure similarity
    keypoints_descriptors = generate_keypoints(images[0], images[1])

    # Attempt at finding common points in both images
    matches = compare_images(keypoints_descriptors[0], keypoints_descriptors[1], keypoints_descriptors[2], keypoints_descriptors[3] )

    print("filtering results now...")
    # filter out outliers and mismatches
    acurate_points = filter_results(matches)

    print("generating a score...")
    # find a ratio for closely matched images are
    score = generate_similarity_score(acurate_points[0], acurate_points[1])

    # write data to CSV file
    publish_results(image_names[0], image_names[1], score, start_time)

    # increment next set of images to be compared
    img += 1















        


        

    
    
    

