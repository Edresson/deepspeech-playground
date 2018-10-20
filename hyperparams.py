# -*- coding: utf-8 -*-
class Hyperparams:
    '''Hyper parameters'''
    language = 'pt' 
    #language = 'eng' 
    vocaben = "PE abcdefghijklmnopqrstuvwxyz'.?" # P: Padding, E: EOS. #english
    vocabpt = "PE abcdefghijklmnopqrstuvwxyzçãõâôêíîúûñáéó.?" # P: Padding, E: EOS. #portuguese
    text = True # use Text for train
    phoneme = False # use Phoneme for train
    logdir = "logdir/" # directory for save checkpoints
    batch_size = 35 # Batch Size

