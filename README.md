# 🅱️isualization Tool in Keras for Facial Expression Recognition


The present repo contains a Python tool-script to run a neural network visualize a facial expression recognizer in realtime.



## Setup

The packages needed are the following:

- [SciPy](https://www.scipy.org/)
- [Numpy](http://www.numpy.org/)
- [OpenCV](https://opencv.org/)
- [Keras](https://keras.io/)

The easiest way to install them is by using the `conda env` included in this repo. To do so, just be sure to have [Anaconda](https://www.anaconda.com/download/) installed and run the following:
```bash
git clone https://github.com/RodolfoFerro/bistek-face.git
cd bistek-face
conda env create -f environment.yml
```

After this you can activate the environment by running:
```bash
source activate bistek
```

To deactivate the environment:
```bash
source deactivate
```


## Usage

You can specify the labels for each class in the [`classes.txt`](https://github.com/RodolfoFerro/bistek-face/blob/master/classes.txt), the classes will be indexed in the same order as in this file.

The main script contains a parser in which any extra required can be specified:
```bash
(bistek) python main.py -h
```

This outputs the following:
```
Using TensorFlow backend.
usage: main.py [-h] [-c CLASSES] [-hc HAAR] [-hcp HAARPATH] [-rs RESIZING]
               [-m MODEL] [-w WEIGHTS]

optional arguments:
  -h, --help            show this help message and exit
  -c CLASSES, --classes CLASSES
                        Path to custom txt file containing classes.
  -hc HAAR, --haar HAAR
                        Haar cascade to be used for face detection.
  -hcp HAARPATH, --haarpath HAARPATH
                        Path to Haar cascades for face detection.
  -rs RESIZING, --resizing RESIZING
                        Image width for resizing.
  -m MODEL, --model MODEL
                        Path to custom model in Keras' json format.
  -w WEIGHTS, --weights WEIGHTS
                        Path to custom weights in Keras' h5 format.
```


## License
