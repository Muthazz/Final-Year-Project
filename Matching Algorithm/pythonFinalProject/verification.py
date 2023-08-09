import os
import cv2  # External library called OpenCV used for match finding

# Sample image of fingerprint input is loaded here
sample = cv2.imread("SOCOFing/Altered/Altered-Medium/132__M_Right_index_finger_Obl.BMP")

best_score = 0  # Likeliness of the sample image to the original
filename = None
image = None
kp1, kp2, mp = None, None, None  # Keypoints for sample and original fingerprint image with
                                 # matchpoints linking similar keypoints together

counter = 0
for file in [file for file in os.listdir("SOCOFing/Real")][:672]:  # Size of directory containing original fingerprints
    if counter % 3 == 0:  # Calls the print file command every single time the count goes up by 3
        print(file)  # Prints the name of the file the system is currently checking for matches with
    counter += 1  # Increases the counter by 1 for every file the system checks for matches with
    fingerprint_image = cv2.imread("SOCOFing/Real/" + file)  # Searches for original fingerprint in provided directory
    sift = cv2.SIFT_create()  # Scale invariant feature transformation for image processing and extraction of features

    keypoints_1, descriptors_1 = sift.detectAndCompute(sample, None)  # Keypoints for sample and original fingerprints
    keypoints_2, descriptors_2 = sift.detectAndCompute(fingerprint_image, None)  # are assigned alongside descriptors

    # Fast library for approximate nearest neighbors is optimized for its fast search speed when using large datasets
    matches = cv2.FlannBasedMatcher({'algorithm': 1, 'trees': 10},
                                    # K-D tree algorithm used with number of trees defined
                                    # Increase of trees increases accuracy and reliability
                                    # of results but requires more processing power and
                                    # may increase the computation time

                                    {}).knnMatch(descriptors_1, descriptors_2, k=2)  # The 2 nearest neighbors of each
                                                                                     # descriptor belonging to the sample
                                                                                     # and original fingerprint image
                                                                                     # respectively is found and matched

    match_points = []

    # Match filtration process through distance ratio test filters out less reliable or ambiguous matches
    for p, q in matches:  # Defines nearest neighbors as p and q
        if p.distance < 0.1 * q.distance:  # Distance ratio threshold for match validation
            match_points.append(p)  # Adds nearest neighbor p to the match_points list if it passes the test

    # Smaller keypoint selection logic
    keypoint = 0
    if len(keypoints_1) < len(keypoints_2):
        keypoints = len(keypoints_1)
    else:
        keypoints = len(keypoints_2)

    # Results display logic
    if len(match_points) / keypoints * 100 > best_score:  # Match score calculation
        best_score = len(match_points) / keypoints * 100  # and display
        filename = file
        image = fingerprint_image
        kp1, kp2, mp = keypoints_1, keypoints_2, match_points
    if best_score == 100:
        break

# Statistical information regarding the best matching original fingerprint
if filename is not None:
    print("Best Match: " + filename)
    print("Match Score: " + str(best_score))

    # Visual representation of sample fingerprint matches with original fingerprint
    result = cv2.drawMatches(sample, kp1, image, kp2, mp, None)
    result = cv2.resize(result, None, fx=4, fy=4)
    cv2.imshow("Result", result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("No match found.")

