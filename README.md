# Isolearn

A Python API for automated loading, processing and streaming of genomics data into deep learning models (Keras).
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

### Usage
Isolearn is centered around data generators, where the generator's task is to transform your sequence data (stored in a Pandas dataframe) and corresponding measurements (e.g. column in the Pandas dataframe, or RNA-Seq count matrix) into numerical input features and output targets.

A simple Keras Data Generator can built using the isolearn.keras package:
```python
import isolearn.keras as iso
import pandas as pd
import numpy as np

#Create some functional sequence data

data = pd.DataFrame(
  {
    'seq' : ['ACGTGGGCTTTCAACTCTAAAACGAGA', 'ACGTGGGCTTTCAACTCTAAAACGAGA', ...],
    'enrichment' : [3.2, -5.1, ...]
  }
)

#Construct a data generator
#The generator one-hot encodes the sequences
#It also takes the log of the enrichment targets

gen = iso.DataGenerator(
  data_ids = np.arange(len(data), dtype=np.int),
  sources = { 'data' : data },
  batch_size = 32,
  inputs = [
    {
      'id' : 'onehot',
      'source_type' : 'dataframe',
      'source' : 'data',
      'extractor' : lambda row, index: row['seq'][100: 200],
      'encoder' : iso.OneHotEncoder(seq_length=100),
      'dim' : (100, 4),
      'sparsify' : False
    }
  ],
  outputs = [
    {
      'id' : 'log_enrichment',
      'source_type' : 'dataframe',
      'source' : 'data',
      'extractor' : lambda row, index: row['enrichment'],
      'transformer' : lambda v: np.log(v)
    }
  ],
  shuffle = True
)

#Now we are all set to feed the data generator into Keras when training a model.
#We can also use the data generator directly as a batch streamer by simply indexing it:

[X], [y] = gen[13] #Generate batch 13
```

### Example Notebooks (Alternative Splicing)
These examples show how to build more complex data generators and how to integrate them into Keras or other learning algorithms. The examples are based on Alternative Splicing data from [https://github.com/Alex-Rosenberg/cell-2015](https://github.com/Alex-Rosenberg/cell-2015).

[Notebook 1a: Logistic Regression of Sequence Hexamer Counts](https://nbviewer.jupyter.org/github/johli/isolearn/blob/master/example/splicing_hexamer_regression.ipynb)<br/>
[Notebook 1b: Logistic Regression of Sequence Hexamer Counts (Multiple Cell Types)](https://nbviewer.jupyter.org/github/johli/isolearn/blob/master/example/splicing_hexamer_regression_multicell.ipynb)<br/>
[Notebook 2a: (Keras) Sequence-Convolutional Neural Network](https://nbviewer.jupyter.org/github/johli/isolearn/blob/master/example/splicing_cnn_multicell.ipynb)<br/>
[Notebook 2b: (Keras) Sequence-Convolutional Neural Network (Sampled Splice Junctions)](https://nbviewer.jupyter.org/github/johli/isolearn/blob/master/example/splicing_cnn_perturbed_multicell.ipynb)<br/>

