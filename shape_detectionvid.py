import cv2 as cv
import numpy as np

# Open webcam
cap = cv.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Apply Gaussian Blur
    blurred = cv.GaussianBlur(frame, (5, 5), 0)

    # Apply Canny Edge Detection
    edges = cv.Canny(blurred, 50, 150)

    # Find Contours
    contours, hierarchies = cv.findContours(edges, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    # Loop through each contour
    for cnt in contours:  
        # Approximate the contour
        approx = cv.approxPolyDP(cnt, 0.02 * cv.arcLength(cnt, True), True)

        # Draw the contour
        cv.drawContours(frame, [approx], 0, (0, 255, 0), 2)

        # Get coordinates for labeling
        x = approx.ravel()[0]
        y = approx.ravel()[1] - 10

        # Detect shape based on number of corners
        corners = len(approx)
        shape = "Unknown"
        if corners == 3:
            shape = "Triangle"
        elif corners == 4:
            shape = "Rectangle"  # Can add aspect ratio check for square
        elif corners > 4:
            shape = "Circle"

        # Display the shape name
        cv.putText(frame, shape, (x, y), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 2)

    # Show result
    cv.imshow("Shape Detection", frame)

    # Exit on 'x' key
    if cv.waitKey(1) & 0xFF == ord('x'):
        break

# Release resources
cap.release()
cv.destroyAllWindows()
