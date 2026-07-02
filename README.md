# computer-vision-practice
Following Practical Computer Vision by O'Reilly 
Altered excerises to use OpenCV instead of SimpleCV

## Activate the environment
source .venv/bin/activate

## Deactivate the environment
deactivate

## Directory
### Chapter 2: Getting to know OpenCV
- hello_world.py: Takes a picture and write Hello World on it
- live_cam.py: Live camera that shows coordinates and rgb
- time_lapse.py: Takes 10 photos a second apart and saves them to photos/time_lapse
- photo_booth.py: Saves photo to photos/photo_booth every time window is left-clicked

### Chapter 3: Image sources
- img_set.py: Create an image sets
- kinect_seg.py: Use kinect data to seperate person from background
- dataset: 
    - images from: https://www.kaggle.com/datasets/bmanikan/rgbd-peoples-dataset 
    - attempted to use https://www.kaggle.com/datasets/hosseinmousavi/small-home-objects-sho-image-dataset/data, but depth and color were different sizes

### Chapter 4: Pixels and Images
- pisa.py: Playing around with shearing by straighting the leaning tower of pisa
- tv.py: Warps live feed to display on an an image of a TV
- dataset:
    - pisa.jpg source: https://stock.adobe.com/search?k=leaning+tower+pisa
    - tv.jpg source: https://www.istockphoto.com/search/2/image-film?phrase=old+tv+side+view&tracked_gsrp_landing=https%3A%2F%2Fwww.istockphoto.com%2Fphotos%2Fold-tv-side-view 

### Chapter 5: The Impact of Light
- car.py: Detect if there is a green car in the image
- dataset
    - parking_lot.jpg: https://www.wesh.com/article/backing-out-of-a-parking-space-made-easy/61803367

### Chapter 6: Image Arithmetic
- motion_det.py: Detect motion of plant growing
- hist.py: Create a histogram of the colors in a grayscale image
- blur.py: Add timelapse effect to live cam
- green_screen.py: Add pigeon to desired colors
- dataset
    - plant_one.png and plant_two.png: https://www.youtube.com/watch?v=w77zPAtVTuI 
    - pigeon.jpg: https://www.pexels.com/search/pigeon/ 

### Chapter 7: Drawing on Images
- stop_go.py: Display stop sign when flashlight shown

### Chapter 8: Basic Feature Detection
- stop_go.py: Display stop sign when flashlight shown
- dataset:
    - coins.png: https://www.reddit.com/r/mildlyinteresting/comments/1c59lha/this_the_least_amount_of_coins_you_need_to_carry/