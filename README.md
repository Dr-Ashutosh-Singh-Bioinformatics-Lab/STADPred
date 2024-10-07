# STADPred: A Tool for Identification of Stomach Adenocarcinoma using Machine Learning.
Stomach adenocarcinoma, commonly known as gastric cancer, is a malignant tumor that originates in the glandular cells lining the stomach. It often develops from chronic inflammation caused by factors like Helicobacter pylori infection, smoking, and dietary habits. Early detection is challenging due to subtle symptoms, leading to late-stage diagnosis in many cases. Identifying biomarkers is crucial for enhancing early diagnosis, guiding treatment decisions, and predicting patient outcomes. Biomarkers can help differentiate between cancerous and non-cancerous tissues, monitor disease progression, and assess treatment response. This targeted approach can significantly improve patient management and overall survival rates in stomach adenocarcinoma. Biomarkers are pivotal in this regard, providing noninvasive means for early detection, facilitating prompt treatment initiation, and potentially boosting survival rates. Hence, the recognition and validation of biomarkers are of primary importance in effectively addressing stomach adenocarcinoma.


## Introduction

STADPred is an innovative solution for identifying stomach adenocarcinoma through transcriptomic profiling. By leveraging advanced machine learning algorithms, this cutting-edge technology analyzes tissue biomarkers to deliver highly accurate prognoses for gastric cancer.

Additionally, the integration of machine learning enables continuous refinement of the predictive model’s accuracy as more data becomes available, enhancing its reliability and effectiveness over time. STADPred represents a significant breakthrough in the early detection of stomach adenocarcinoma, potentially leading to earlier interventions and improved patient outcomes.

To further strengthen our approach, we selected 40 features using a range of Feature Selection Methods. These include the Fast Correlation-Based Filter Method (FCBF), Spike and Slab ("spikeslab"), Univariate statistical tests (F-test), and wrapper methods like Boruta and Recursive Feature Elimination (RFE). Additionally, we employed embedded methods such as XGBoost, SVC linear with the SelectFromModel class from scikit-learn, Random Forest, Extra Trees with Feature Importance, and LASSO (a regularization-based embedded method). By combining Filter, Wrapper, and Embedded feature selection techniques, we used an ensemble approach to identify features present in at least five methods. These 40 features show potential as biomarkers for classifying and predicting normal versus cancerous patients.


Installation and Usage:

You can install the package using the following command:


    git clone https://github.com/GITractCancer/STADPred.git
    cd STADPred



### Predict using STADPred

    import pandas as pd
    from STADPred import predict

    df = pd.read_csv("path/to/your/data.csv")

    predict(df, model_type='svc')

    
Specify the model type you want to use Models


## Models

The following classifiers are supported:

    svc
    rf
    ab
    xgb
    dt
    et
    lr
    gnb
    knn
    mlp
