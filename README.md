# Impact of COVID19 on NYC Yellow Taxis Project README.md

**Research Goal:** My research goal is to analyse the impact of the late 2021 spike on the Yellow Taxi and HVFHV (High Volume For-Hire Vehicles) industry, and how passenger behaviour has changed follwing NYC's lockdowns.

**Timeline:** December 2019-February 2020 and December 2021-February 2022.

## Pipeline
To run the pipeline, please visit the `scripts` and `notebooks` directories and run the files in order:
1. `download.py`: This downloads the data into the `data` directory into its relevant sub-folders. 
2. `preprocess.ipynb`: This notebook details all preprocessing steps and outputs all data that required preprocessing to the `data/curated` directory.
3. `analysis & visualisation.ipynb`: This notebook is used to conduct analysis and visualisation on the curated data.
4. `modelling.ipynb`: This notebook is used to construct, run and generate evaluations of the models. 
