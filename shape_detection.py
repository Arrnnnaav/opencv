# shape detection using canny and contours
import cv2 as cv
import numpy as np
# Load image
img = cv.imread('images/bit4.png', 0)  

# Apply Gaussian Blur
blurred = cv.GaussianBlur(img, (5, 5), 0)

# Apply Canny Edge Detection
edges = cv.Canny(blurred, 50, 150)

# Find Contours from edges
contours, hierarchies = cv.findContours(edges, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

# Draw all contours
for cnt in contours:
    # Get the approximated polygon of the contour
    approx = cv.approxPolyDP(cnt, 0.02 * cv.arcLength(cnt, True), True)

    # Draw contours
    cv.drawContours(img, [approx], 0, (0, 255, 0), 2)

    # Get coordinates for labeling
    x = approx.ravel()[0]
    y = approx.ravel()[1] - 10

    # Detect basic shape by number of corners
    shape = "Unknown"
    corners = len(approx)
    if corners == 3:
        shape = "Triangle"
    elif corners == 4:
        shape = "Rectangle"  # could also be square
    elif corners > 4:
        shape = "Circle"

    # Put text on image
    cv.putText(img, shape, (x, y), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 2)

# Show results
cv.imshow("Detected Shapes", img)
cv.imshow("Edges", edges)
cv.waitKey(0)
cv.destroyAllWindows()
