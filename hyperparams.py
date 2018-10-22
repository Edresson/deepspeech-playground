# -*- coding: utf-8 -*-
class Hyperparams:
    '''Hyper parameters'''
    language = 'pt' 
    #language = 'eng' 
    text = True # use Text for train
    phoneme = False # use Phoneme for train
    logdir = "logdir/" # directory for save checkpoints
    batch_size = 10 # Batch Size