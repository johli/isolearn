from __future__ import print_function
import keras

import pandas as pd
import numpy as np
import scipy.sparse as sp

import operator

from isolearn.generator import BatchEncoder, SparseBatchEncoder, SequenceEncoder, OneHotEncoder, NMerEncoder, CategoricalEncoder, IdentityEncoder
from isolearn.generator import BatchTransformer, SparseBatchTransformer, ValueTransformer, LogitTransformer, CountSumTransformer, ProportionTransformer, MultiProportionTransformer
from isolearn.generator import SequencePadder, MultiPadder
from isolearn.generator import SequenceExtractor, CountExtractor, PositionShifter, CutAlignSampler, get_bellcurve_shifter

from isolearn.generator import DataGenerator as VanillaGenerator
from isolearn.generator import MultiDataGenerator as MultiVanillaGenerator

class DataGenerator(keras.utils.Sequence) :
    
    def __init__(self, data_ids, sources, batch_size=32, inputs=None, outputs=None, randomizers=[], shuffle=True, densify_batch_matrices=False, move_outputs_to_inputs=False) :
        self.gen = VanillaGenerator(data_ids, sources, batch_size=batch_size, inputs=inputs, outputs=outputs, randomizers=randomizers, shuffle=shuffle, densify_batch_matrices=densify_batch_matrices, move_outputs_to_inputs=move_outputs_to_inputs)
        
        self.data_ids = self.gen.data_ids
        self.sources = self.gen.sources
        self.batch_size = self.gen.batch_size
        self.inputs = self.gen.inputs
        self.outputs = self.gen.outputs
        self.randomizers = self.gen.randomizers
        self.shuffle = self.gen.shuffle
        self.densify_batch_matrices = self.gen.densify_batch_matrices
        self.indexes = self.gen.indexes
        self.encoders = self.gen.encoders
        self.transformers = self.gen.transformers

    def __len__(self) :
        return self.gen.__len__()

    def __getitem__(self, index):
        return self.gen.__getitem__(index)

    def on_epoch_end(self) :
        self.gen.on_epoch_end()


class MultiDataGenerator(keras.utils.Sequence) :
    
    def __init__(self, data_gens, sampling_factors, reshuffle_flags, epoch_loss_factors, dummy_outputs=True) :
        self.gen = MultiVanillaGenerator(data_gens, sampling_factors, reshuffle_flags, epoch_loss_factors, dummy_outputs=dummy_outputs)

        self.data_gens = self.gen.data_gens
        self.dummy_outputs = self.gen.dummy_outputs
        self.lens = self.gen.lens
        self.indexes = self.gen.indexes
        self.trainable = self.gen.trainable
        self.epoch = self.gen.epoch
        self.epoch_loss_factors = self.gen.epoch_loss_factors

    def __len__(self) :
        return self.gen.__len__()

    def __getitem__(self, index):
        return self.gen.__getitem__(index)

    def on_epoch_end(self) :
        self.gen.on_epoch_end()
        self.epoch = self.gen.epoch

