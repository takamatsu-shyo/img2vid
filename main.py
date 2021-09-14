import os
import cv2
import argparse

"""
1. Read all image files in a dir then put them into a list
2. Order the list 
3. Create video file
"""

def main(input_dir="/tmp", out_filename="/tmp/out.avi"):
    print('img2vid')
    print('input ',input_dir)
    print('output',out_filename)

    images = [img for img in os.listdir(input_dir) if img.endswith('png')]
    images.sort()

    if len(images) == 0:
        print('No img in ', input_dir)
        return -1

    frame = cv2.imread(os.path.join(input_dir, images[0]))
    height, width, channel = frame.shape

    video = cv2.VideoWriter(out_filename, 0, 30, (width, height))

    for image in images:
        video.write(cv2.imread(os.path.join(input_dir, image)))
        print(image)

    video.release()
    print('done')

if __name__ == "__main__":

    main()    
