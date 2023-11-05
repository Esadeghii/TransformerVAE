
# Automatic Feature Extraction for Silver Nanocluster Design via Variational Autoencoders




<div style="display: flex; justify-content: space-between;">
    <img src="https://upload.wikimedia.org/wikipedia/en/thumb/0/0e/University_of_California%2C_Irvine_seal.svg/150px-University_of_California%2C_Irvine_seal.svg.png" alt="University of California, Irvine Logo" width="80">
    <img src="https://www.cs.albany.edu/~petko/lab/img/logo1.png" alt="Lab Logo" width="200">
</div>
<img src="https://www.cs.albany.edu/sccepr/img/logo1.png" alt="University Logo" width="260">



## Team
- [Stacy Copp](https://copplab.eng.uci.edu/)
- [Petko Bogdanov](http://www.cs.albany.edu/~petko/lab/)
## Contents 

 - Introduction
 - Problem Formulation and Solution
 - How to Run the Project


## Introduction
DNA-stabilized silver nanoclusters (Ag𝑁-DNAs) represent a unique class of nanomaterials, composed of 10-30 silver atoms intricately bound by short synthetic DNA template strands. These Ag𝑁-DNAs exhibit immense potential as biosensors and fluorophores due to their small size, inherent compatibility with biological systems, and remarkable fluorescence properties. The DNA template sequence essentially serves as the "genome" for Ag𝑁-DNAs. Nonetheless, our current comprehension of the Ag𝑁-DNA genome remains limited. Only a minority of DNA sequences yield highly fluorescent Ag𝑁-DNAs, and the presence of bulky DNA strands and intricate DNA-silver interactions pose significant challenges for using fundamental chemical calculations to fathom and engineer Ag𝑁-DNAs.
In response to this challenge, we introduce a novel approach for Ag𝑁-DNA design by harnessing Variational Autoencoders. Our methodology employs an LSTM-based 𝛽-VAE architecture, and we apply regularization techniques to align its latent space with the desired Ag𝑁-DNA properties. This innovative model empowers us to create Ag𝑁-DNAs operating within the near-infrared spectrum, an area where relatively few Ag𝑁-DNAs have been explored so far.
Additonally, we demonstrate a method to interrogate the trained model about its predictions based on Shapley value analysis which provides insights into the learnt essential sub-sequences corresponding to properties of interest. 
Our approach demonstrates remarkable versatility in designing Ag𝑁-DNAs tailored to multiple desired properties. This advancement holds significant promise for elevating the applications of nanomaterials in  fields such as bioimaging, biosensing, and other critical technologies.
![Logo](https://imageupload.io/ib/LuxfBl1wquzLM8y_1699199518.png)





![Logo](https://imageupload.io/ib/2J254j1PUyKMeyL_1699199752.png)

## Problem Formulation and Solution
- Problem: Design DNA sequences that “code for” AgN-DNAs with specific properties. Provide explanations for what model captures.
- Solution: Train a property-regularized VAE to learn a structured latent space and sample for desired properties.
- VAE Model Architecture:

![Logo](https://imageupload.io/ib/Ke1xrj8yJHCngG2_1699200592.png)

## How to Run the Project
- `/VAE/utils/`: This directory contains code derived from the original VAE paper, with additional utilities for training the Torch model.
    - `/VAE/utils/helpers.py`: Within this file, you'll find functions designed to handle the availability of CUDA (GPU) resources, providing utility in managing GPU usage.
    - `/VAE/utils/model.py`: This file defines an abstract model that extends the capabilities of the torch.nn.Module class, offering convenient QoL helper functions for model development.
    - `/VAE/utils/trainer.py`: In this file, you'll discover an abstract trainer, which introduces mathematical utilities used within the loss function during training.
- `/VAE/genGrid.py`: This Python script serves as the entry point for conducting grid searches within your project. 
- `/VAE/plotRun.py`: This script is responsible for converting the run logs into visual plots.
- `/VAE/sampleSeqs.py`:  Here, you'll find code that generates a list of sequences using the model you've developed.
- `/VAE/sequenceDataset.py`: This file contains the code for loading the dataset, facilitating the preparation of data for the experiments.
- `/VAE/sequenceModel.py`: Within this file, you'll find the concrete implementation of the model for the AR-VAE. 
- `/VAE/kfoldrun.py`: This script is used for k-fold cross-validation, a technique that enhances model evaluation by splitting the dataset into 'k' parts for more reliable performance assessment.
- `/VAE/kfoldPlotter.py`: This Python script is designed to create plots and visualizations of the results obtained from kfoldrun.py 
- `/VAE/shapley-gaussian.py`: This script calculates the Gaussian Shapley value for a specific group, requiring the mean and standard deviation proxies of the group's data to analyze motifs or feature importance within that group.
- `/VAE/shap-plot.ipynb`: This Jupyter Notebook utilizes Shapley values to generate visualizations, including heatmaps and line graphs, to explore and analyze subsequences and their importance within the dataset.
- `/VAE/requirements.txt`: Here, you can find a list of pip requirements essential for running your project successfully.   
