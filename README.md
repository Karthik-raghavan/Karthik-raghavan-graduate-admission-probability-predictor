# Graduate Admission Probability Predictor

This project aims to create a Graduate Admission Probability Predictor, providing insights into important factors for university admissions, especially for competitive institutions. With a focus on making admission chances transparent, this model can aid students in understanding their chances of acceptance based on various criteria and aid organizations in crafting data-driven admissions counseling strategies.

## Project Context

Thousands of students aspire to study at top colleges worldwide, including Ivy League institutions. **Client** is dedicated to assisting students in reaching their goals through effective test prep and admissions consulting. This project simulates a tool that estimates students' chances of admission by analyzing past admissions data. The insights derived help in identifying key factors affecting admission probability and how these factors interrelate. With this knowledge, students can gain a clearer picture of what they need to focus on to strengthen their profiles.

## Objective

Our analysis explores significant factors influencing admission probability and uses **Linear Regression** to predict an applicant's chances of acceptance based on the following variables:

- GRE Scores
- TOEFL Scores
- University Rating
- Strength of Statement of Purpose and Letters of Recommendation
- Undergraduate GPA
- Research Experience

## Data Overview

The dataset used in this project includes the following columns:

- **Serial No.**: Unique row ID
- **GRE Scores**: Applicant's GRE scores (out of 340)
- **TOEFL Scores**: Applicant's TOEFL scores (out of 120)
- **University Rating**: Rating of the university (out of 5)
- **SOP/LOR Strength**: Strength of Statement of Purpose and Letter of Recommendation (out of 5)
- **Undergraduate GPA**: GPA in undergraduate studies (out of 10)
- **Research Experience**: Research experience indicator (0 for no research, 1 for research experience)
- **Chance of Admit**: Probability of admission ranging from 0 to 1

## Key Concepts

### 1. Exploratory Data Analysis (EDA)
   - Identify data distributions, outliers, and relationships between variables.
   - Visualize correlations to understand which factors impact the admission probability.

### 2. Linear Regression Model
   - Create a predictive model that estimates admission chances based on the provided variables.
   - Analyze model performance and adjust features to improve accuracy and interpretability.

## How This Helps

This analysis benefits **Client** by:

- Identifying the most impactful factors in the admission process, allowing for better guidance to applicants.
- Providing applicants with personalized insights into their admission probability.
- Assisting **Client** in refining its services for competitive exams and admission counseling.

For a more detailed walkthrough, please refer to the code and model details included in this repository.
