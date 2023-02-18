# Discovering Potential Skin Cancer Drugs

Abstract

Over 32.6 million people live with cancer worldwide, and 8.2 million people died from cancer in 2021. About 150,000 people are diagnosed with skin cancer every day, and many developing countries are ill-equipped to fight these diseases. Given the time-consuming and costly drug discovery process, machine learning coupled with cheminformatics provides a method to efficiently speed up the process. Molecular descriptors have especially shown immense potential to identify and predict natural products with drug properties. In this paper, I compared the accuracy of molecular descriptors from two molecular descriptor software libraries, Mordred and PaDEL, to predict and identify natural products with potential to be skin cancer drugs. I utilized the Therapeutic Target Database (TTD) to access 3,498 approved skin cancer drugs. Parsin the TTD for other randomly selected compounds, I constructed a dataset of 8,000 compounds. The dataset comprises of SMILE strings which were used to calculate the molecular descriptors using the PaDEL and Mordred software libraries. After training and testing, the best-performing model was a Random Forest with PaDEL descriptors. Using the feature importance determined by the model, I selected ten key molecular descriptors for classifying the skin cancer drugs. After tuning hyperparameters to optimize performance and limiting it to ten molecular descriptors, I utilized the model to predict whether 5,000 natural products collected from the Coconut database had the potential to be skin cancer drugs.

research notebook: https://docs.google.com/document/d/1iv_2VSPSFdsR2XIBdmccVO14nga5m-X0YSgUwNlcpgY/edit

proposal slideshow: https://docs.google.com/presentation/d/1pCz5nHR3NHXFGGUtS8lNBleQvYneREGjPiAbRQ9qoig/edit#slide=id.g1ede7390a06_0_6

Unable to upload molecular descriptors csv due to size

Email 2redrosen@gmail.com for any comments/questions
