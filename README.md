
# Automatic Feature Extraction for Silver Nanocluster Design via Variational Autoencoders




![Logo](https://upload.wikimedia.org/wikipedia/en/thumb/0/0e/University_of_California%2C_Irvine_seal.svg/150px-University_of_California%2C_Irvine_seal.svg.png)
![Logo](https://www.cs.albany.edu/sccepr/img/logo1.png)
![Logo](https://www.cs.albany.edu/~petko/lab/img/logo1.png)


## Contents 

 - Introduction
 - Problem Formulation and Solution
 - How to Run the Project


## Introduction
DNA-stabilized silver nanoclusters (Ag𝑁 -DNAs) are a class of nanomaterials comprised of 10-30 silver atoms held together by short synthetic DNA template strands. Ag𝑁 -DNAs are promising biosensors and fluorophores due to their small sizes, natural compatibility, and bright fluorescence. The sequence of the DNA template acts as a "genome" for Ag𝑁 -DNAs. However, current understanding of the Ag𝑁 -DNA genome is limited. Only a minority of DNA sequences produce highly fluorescent Ag𝑁 -DNAs, and the bulky DNA strands and complex DNA-silver interactions make it challenging to use first principles chemical calculations to understand and design Ag𝑁 -DNAs.
We present an approach to design Ag𝑁 -DNAs by employing Variational Autoencoders. We employ an LSTM-based 𝛽-VAE architecture and regularize its latent space to correlate with Ag𝑁 -DNA properties. We employ our model for designing Ag𝑁 -DNAs in the near-infrared band, where relatively few Ag𝑁 -DNAs have been observed to date. We demonstrate a method to interrogate the trained model about its predictions based on Shapley Value analysis. The model is well-suited for designing Ag𝑁 -DNAs with multiple targeted properties with significant potential to advance the promising applications of nanomaterials for bioimaging, biosensing, and other critical technologies.
![Logo](https://imageupload.io/ib/LuxfBl1wquzLM8y_1699199518.png)


![Logo](https://imageupload.io/ib/2J254j1PUyKMeyL_1699199752.png)

## Problem Formulation and Solution
- Problem: Design DNA sequences that “code for” AgN-DNAs with specific properties. Provide explanations for what model captures.
- Solution: Train a property-regularized VAE to learn a structured latent space and sample for desired properties.
- VAE Model Architecture:

![Logo](https://imageupload.io/ib/Ke1xrj8yJHCngG2_1699200592.png)

## How to Run the Project
- `/VAE/utils/`: 
    - `/VAE/utils/helpers.py`:
    - `/VAE/utils/model.py`:
    - `/VAE/utils/trainer.py`:
- `/VAE/genGrid.py`: 
- `/VAE/plotRun.py`: 
- `/VAE/sampleSeqs.py`: 
- `/VAE/sequenceDataset.py`: 
- `/VAE/sequenceModel.py`: 
- `/VAE/kfoldDataset.py`: 
- `/VAE/kfoldPlotter.py`: 
- `/VAE/pcaVisualization.py`: 
- `/VAE/shapley-gaussian.py`: 
- `/VAE/shap-plot.ipynb`: 
- `/VAE/violinWavProxy.py`: 
- `/VAE/requirements.txt`:     
