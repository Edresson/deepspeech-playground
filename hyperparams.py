# -*- coding: utf-8 -*-
class Hyperparams:
    '''Hyper parameters'''
    language = 'pt' 
    #language = 'eng' 
    text = True # use Text for train
    phoneme = False # use Phoneme for train
    logdir = "logdir/" # directory for save checkpoints
    
    model = 'QRnnModel'
    #model = 'GruModel'
    args_model = '{nodes=1000, conv_context=5, recur_layers=5}' # list config arguments for compile model
    batch_size = 10 # Batch Size