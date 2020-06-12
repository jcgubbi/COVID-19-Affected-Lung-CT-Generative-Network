# COVID-19-Affected Lung CT Generative Network

## A Generational Adversarial Network (GAN) to generate CT scans of lungs with COVID-19

*A project for UCLA's CS 168 class taught by Professor Scalzo*

### Premise and Motivation
- Generate images of lungs with COVID-19 to model progression of COVID-19
- Use this to expand current datasets, which are limited in quantity
- Eventually create an image-to-image model to see the progression of the disease in one set of lungs

### Major Components
- Models (final and iterations -- .ipynb files)
- Data (from https://github.com/UCSD-AI4H/COVID-CT)
- Latent Space Widget for visualization
- Generated images from the GAN

# Usage
## To Create/Train the COVID-19-Affected Lung CT Generative Network
### Option 1: Running Locally
Model definition and training is located in [COVID_GAN.ipynb](https://github.com/jcgubbi/COVID-19-Affected-Lung-CT-Generative-Network/blob/master/COVID_GAN.ipynb) or [COVID_GAN.py](https://github.com/jcgubbi/COVID-19-Affected-Lung-CT-Generative-Network/blob/master/COVID_GAN.py).  
To run, **clone this repo**, and **download the data set** available **[here](https://drive.google.com/drive/folders/1ESqVMTe4f85d9Sk5GHlsxbI8U770WLOc?usp=sharing)**.  
Make sure the above-mentioned script and the zip file of data are in the same directory.   
Before running, make sure all dependencies are installed by running `pip install -r requirements.txt`.  
Run the program with `python3 COVID_GAN.py` or `jupyter notebook COVID_GAN.ipynb` or with any other framework of your choosing.  
The program will define a new model and train it with the data provided and hyperparameters specified and changeable in [COVID_GAN.ipynb](https://github.com/jcgubbi/COVID-19-Affected-Lung-CT-Generative-Network/blob/master/COVID_GAN.ipynb) or [COVID_GAN.py](https://github.com/jcgubbi/COVID-19-Affected-Lung-CT-Generative-Network/blob/master/COVID_GAN.py).  
The final models will be saved in a new subdirectory called `Saved_Models`.  
### Option 2: Running on Google Colabs
If you would like to run the model creation/training in Google Colabs, you can do so [here] (https://colab.research.google.com/drive/1pakKK8eU6wgn_2Wi_ibKGBlUGXY6dO5W?usp=sharing)
