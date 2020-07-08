# COVID-19-Affected Lung CT Image Generative Network

## A Generational Adversarial Network (GAN) to generate CT scans of lungs with COVID-19

### Premise and Motivation
- Generate images of lungs with COVID-19 to model progression of COVID-19
- Use this to expand current datasets, which are limited in quantity
- Eventually create an image-to-image model to see the progression of the disease in one set of lungs

### Major Components
- Model Definition and Training Script
- Demo of our final model, and demo of interpolation to model the progression
- Latent Space Widget for visualization
- [Academic paper where we discuss our GAN](https://github.com/brendon-ng/COVID-19-Affected-Lung-CT-Image-Generative-Network/blob/master/Modeling_COVID_19_Using_GANs_Paper.pdf)
- Generated images from the GAN
- **Project Resources** containing the dataset and our final models can be found **[here](https://drive.google.com/drive/folders/1ESqVMTe4f85d9Sk5GHlsxbI8U770WLOc?usp=sharing)**. 
  - Models (.h5 files ready to be loaded and used)
  - Data (from https://github.com/UCSD-AI4H/COVID-CT)

# Usage
## To Create/Train the COVID-19-Affected Lung CT Generative Network
### Option 1: Running Locally
- Model definition and training is located in [COVID_GAN.ipynb](https://github.com/jcgubbi/COVID-19-Affected-Lung-CT-Generative-Network/blob/master/COVID_GAN.ipynb) or [COVID_GAN.py](https://github.com/jcgubbi/COVID-19-Affected-Lung-CT-Generative-Network/blob/master/COVID_GAN.py).  
- To run, **clone this repo**, and **download the data set** available **[here](https://drive.google.com/drive/folders/1ESqVMTe4f85d9Sk5GHlsxbI8U770WLOc?usp=sharing)**.  
- Make sure the above-mentioned script and the zip file of data are in the same directory.   
- Before running, make sure all dependencies are installed by running `pip3 install -r requirements.txt` in terminal. 
- Ensure the hyperparameter `load_data_from_Google_Drive` is set to `False`.  
- The program will define a new model and train it with the data provided and hyperparameters specified and changeable in [COVID_GAN.ipynb](https://github.com/jcgubbi/COVID-19-Affected-Lung-CT-Generative-Network/blob/master/COVID_GAN.ipynb) or [COVID_GAN.py](https://github.com/jcgubbi/COVID-19-Affected-Lung-CT-Generative-Network/blob/master/COVID_GAN.py).  
- Run the program in terminal with `python3 COVID_GAN.py` or `jupyter notebook COVID_GAN.ipynb` or with any other framework of your choosing.  
- The final models will be saved in a new subdirectory called "**Saved_Models**".  
### Option 2: Running on Google Colabs
- If you would like to run the model creation/training in Google Colabs, you can make a copy of the Colab **[here](https://colab.research.google.com/drive/1pakKK8eU6wgn_2Wi_ibKGBlUGXY6dO5W?usp=sharing)**. 
- To obtain the data, go to our **[project resources](https://drive.google.com/drive/folders/1ESqVMTe4f85d9Sk5GHlsxbI8U770WLOc?usp=sharing)** and click **Add shortcut to Drive** for the whole folder.  
- Ensure the hyperparameter `load_data_from_Google_Drive` is set to `True`.  
- The program will define a new model and train it with the data provided and hyperparameters specified and changeable in the Colab after you've made a copy.  
- Run the program on Google Colabs.  
- The final models will be saved in a new directory in "My Drive" called "**COVID_GAN_Saved_Models**". 

## Demo of our final model. 
### Option 1: Running Locally. 
- Demo is located at [Demo_COVID_GAN_Progression.ipynb](https://github.com/jcgubbi/COVID-19-Affected-Lung-CT-Generative-Network/blob/master/Demo_COVID_GAN_Progression.ipynb).  
- Download both the **dataset** and `.h5` files of the **final models** are downloaded from **[project resources](https://drive.google.com/drive/folders/1ESqVMTe4f85d9Sk5GHlsxbI8U770WLOc?usp=sharing)**.  
- Ensure the zipped dataset and final models are in the same directory as `Demo_COVID_GAN.ipynb`.  
- Before running, make sure all dependencies are installed by running `pip3 install -r requirements.txt`.  
- Ensure the hyperparameter `load_data_from_Google_Drive` is set to `False`.  
- The demo will load in the pre-trained models using the `.h5` files as well as the data to run the demo.  
- Run the demo with `jupyter notebook Demo_COVID_GAN.ipynb` or with any other framework of your choosing.  
### Option 2: Running on Google Colabs. 
- If you would like to run the demo in Google Colabs, you can make a copy of the Demo Colab **[here](https://colab.research.google.com/drive/15NN5DZNQCFVkwy8P16bSpWY11iw2iv03?usp=sharing)**. 
- To obtain the data and models, go to our **[project resources](https://drive.google.com/drive/folders/1ESqVMTe4f85d9Sk5GHlsxbI8U770WLOc?usp=sharing)** and click **Add shortcut to Drive** for the whole folder.  
- Ensure the hyperparameter `load_data_from_Google_Drive` is set to `True`.  
- The program will load in the pre-trained models from project resources as well as the data to run the demo.  
- Run the program on Google Colabs.  

# Project Links
##### Linked throughout the README
[Paper](https://github.com/brendon-ng/COVID-19-Affected-Lung-CT-Image-Generative-Network/blob/master/Modeling_COVID_19_Using_GANs_Paper.pdf)  
[Model Definition and Training Script Colab](https://colab.research.google.com/drive/1pakKK8eU6wgn_2Wi_ibKGBlUGXY6dO5W?usp=sharing)  
[Demo Colab](https://colab.research.google.com/drive/15NN5DZNQCFVkwy8P16bSpWY11iw2iv03?usp=sharing)  
[Project Resources (Final Models and Data)](https://drive.google.com/drive/folders/1ESqVMTe4f85d9Sk5GHlsxbI8U770WLOc?usp=sharing)  


#### References and Helpful Links:
[1] [Age Progression/Regression by Conditional Adversarial Encoders](https://arxiv.org/pdf/1702.08423.pdf)  
[2] [Exploring GAN Latent Space](https://machinelearningmastery.com/how-to-interpolate-and-perform-vector-arithmetic-with-faces-using-a-generative-adversarial-network/)  
[3] [Deep Convolutional Neural Network Tutorial](https://www.tensorflow.org/tutorials/generative/dcgan)  
[4] [GAN Tutorial](https://towardsdatascience.com/generative-adversarial-network-gan-for-dummies-a-step-by-step-tutorial-fdefff170391)  
[5] [Visualize Autoencoders (Latent Space)](https://douglasduhaime.com/posts/visualizing-latent-spaces.html)
