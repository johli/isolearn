# Isolearn

Automated loading, processing and streaming of genomics data for use in deep learning models (Keras).
Implements Keras data generators for loading and encoding Pandas dataframes and RNA-Seq count matrices into numerical tensors.

#### When to use Isolearn
- When you want to encode DNA sequence features (e.g. hexamer counts or one-hot encodings) of large genomic datasets, for use in downstream learning algorithms.
- When you want to stream data and encode sequence features on the fly as mini batches.
- When you want seamless integration with Keras as parallelizable genomic data generators.
- When you are building a complex multi-task model composed of several data sets.

### Installation
The latest stable version of Isolearn can be installed with pip:
```sh
pip install isolearn
```

Isolearn can also be installed from the [github repository](https://github.com/johli/isolearn.git):
```sh
git clone https://github.com/johli/isolearn.git
cd isolearn
python setup.py install
```

#### Isolearn requires the following packages to be installed
- Keras >= 2.2.4
- Pandas >= 0.24.2
- Scipy >= 1.2.1
- Numpy >= 1.16.2

### Example Notebooks (Alternative Splicing)
[Notebook 1a: Logistic Regression of Sequence Hexamer Counts](https://nbviewer.jupyter.org/github/johli/isolearn/blob/master/example/splicing_hexamer_regression.ipynb)<br/>
[Notebook 1b: Logistic Regression of Sequence Hexamer Counts (Multiple Cell Types)](https://nbviewer.jupyter.org/github/johli/isolearn/blob/master/example/splicing_hexamer_regression_multicell.ipynb)<br/>
[Notebook 2a: (Keras) Sequence-Convolutional Neural Network](https://nbviewer.jupyter.org/github/johli/isolearn/blob/master/example/splicing_cnn_multicell.ipynb)<br/>
[Notebook 2b: (Keras) Sequence-Convolutional Neural Network (Sampled Splice Junctions)](https://nbviewer.jupyter.org/github/johli/isolearn/blob/master/example/splicing_cnn_perturbed_multicell.ipynb)<br/>

