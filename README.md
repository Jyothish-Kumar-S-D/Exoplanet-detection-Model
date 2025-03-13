# Exoplanet-detection-Model

## Overview
This project presents a deep learning approach for exoplanet detection based on flux time-series data. The proposed model integrates a Kalman filter for noise reduction and employs a Hybrid LSTM-Transformer architecture to effectively capture both short-term dependencies and long-range relationships within the data. The model was trained on a dataset consisting of 6000 labelled records, each comprising 4608 flux observations paired with their corresponding time data.

## Features

**Kalman Filter**: Applied to raw flux signals to reduce noise. 

**1D CNN Feature Extraction**: Extracts local patterns from input sequences.

**LSTM for Sequential Learning**:Captures temporal dependencies in time-series data.

**Transformer Encoder**: Enhances long-range dependencies for better predictions.

**Binary Classification**: Predicts whether a given signal corresponds to an exoplanet.

**PyTorch-based Implementation**: Utilizes GPU acceleration for efficient training.


## Model Architecture
The Hybrid LSTM-Transformer model consists of:

**1D Convolutional Layers**: Extracts high-level features.

**Batch Normalization & Activation Layers**: Normalizes feature maps and applies ReLU activation.

**LSTM (Bidirectional)**: Captures forward and backward dependencies.

**Transformer Encoder**: Strengthens sequence understanding.

**Fully Connected Layers**: Outputs final binary classification.


## Dataset Information
This project utilizes the **[Exoplanet Detection Dataset](https://www.kaggle.com/datasets/ronaldkroening/exoplanet-detection-dataset)** from Kaggle, which is made available under the  
[Open Data Commons Open Database License (ODbL) v1.0](https://opendatacommons.org/licenses/odbl/1-0/).

### License
The dataset is licensed under the **Open Data Commons Open Database License (ODbL) v1.0**.  

**Attribution Requirement:**  
If you use this dataset, you must provide proper credit, a link to the license,  
and indicate any changes made. Any modifications or derivative works must  
be shared under the same license.

For more details, refer to the [ODbL License](https://opendatacommons.org/licenses/odbl/1-0/).
