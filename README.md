# 🅱️isualization Tool in Keras for Facial Expression Recognition


The present repo contains a Python tool-script to run a neural network visualize a facial expression recognizer in realtime.

The repo includes a pre-trained model for facial expression recognition.

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

With this, you can specify any path to any of the files to be used, or specify the resizing of the images to be processed by the neural net.

An example (using some flags) to run the pre-trained network included in this repo would be the following:
```bash
(bistek) python main.py -c "classes.txt" -rs 48 -m "./models/base_model.json" -w "./models/base_model.h5"
```


## License

**MIT License**

Copyright (c) 2018 Rodolfo Ferro

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
