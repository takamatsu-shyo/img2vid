import os
import cv2
import argparse
from tqdm import tqdm

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

    for i in tqdm(range(len(images))):
        image = images[i]
        video.write(cv2.imread(os.path.join(input_dir, image)))

    video.release()
    print('done')

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('input', default = '/tmp', help="directory which is keeping png files")
    parser.add_argument('output', default = '/tmp/out.avi', help='output file name for ex /tmp/out.avi')

    args = parser.parse_args()

    main(input_dir=args.input, out_filename=args.output)    
