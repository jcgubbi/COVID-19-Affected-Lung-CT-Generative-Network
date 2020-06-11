# Latent Space Explorer Widget:

### A 2-dimensional rendering of the latent space of existing lung CT scans, with trackball navigation and dynamic image display.


### To run this widget:
1. Navigate to this directory: ```CS-168-COVID/LatentSpaceWidget```
2. Start an HTTP server from your terminal: ```python -m http.server 8000```
3. Go to ```localhost:8000``` in your browser
4. Widget should be loaded!

### Things to note:
- Make sure that the folder with model information is in the same directory as the index.html file
- This code was adapted from https://douglasduhaime.com/posts/visualizing-latent-spaces.html
  - We used the same autoencoder architecture but adapted it for CT images of lungs
- The latent space is not very dense in this application because the data for lung CT scans with/without COVID is not as high in quantity or diversity as other datasets (i.e. celebrity face dataset)
- This latent space explorer can be used as a baseline to compare generated images from the GAN to real CT scans
