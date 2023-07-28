# Z-DNA_Generator
This repository contains an experiment aimed at generating rare DNA sequences. Z-DNA was used to test the possibility of such generation.

## Introduction
Classification of rare DNA sequences is a difficult task. DNA marking is an expensive process. Therefore, the generation of synthetic data should simplify the classification.

## Dependencies
Install the required packages using pip (settings for python3.9):
```
pip install -r requirements.txt
```
You need to download the weights of the pre-trained models:
* [DNA generation model]()
* [z-DNA generation model]()

## Model usage

## z-DNA generator validator
You need to download the pre-trained [validate DNA-BERT model](https://pages.github.com/](https://drive.google.com/file/d/1RraZTUyTTgu_R3GNNmrixOLTTMpXMhSb/view?usp=sharing)https://drive.google.com/file/d/1RraZTUyTTgu_R3GNNmrixOLTTMpXMhSb/view?usp=sharing) weights from Google drive and move the file to the "Validate" folder.
Then you need to use the validate method. The input is a list with nucleotide sequences of length 517, also the size of the batch, which affects the speed. The method returns the content of Z-DNA in sequences
```
from Validator.ZDNA_Validator import validate
accs = validate(X, 2)
```
