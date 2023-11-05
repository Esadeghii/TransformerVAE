
# Automatic Feature Extraction for Silver Nanocluster Design via Variational Autoencoders




![Logo](https://upload.wikimedia.org/wikipedia/en/thumb/0/0e/University_of_California%2C_Irvine_seal.svg/150px-University_of_California%2C_Irvine_seal.svg.png)
![Logo](https://www.cs.albany.edu/sccepr/img/logo1.png)
![Logo](https://www.cs.albany.edu/~petko/lab/img/logo1.png)

## Team
- [Petko Bogdanov](http://www.cs.albany.edu/~petko/lab/)
- [Stacy Copp](https://copplab.eng.uci.edu/)
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
