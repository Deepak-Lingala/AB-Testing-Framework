# A/B Testing Framework: E-Commerce Checkout Optimization

![Testing Status](https://img.shields.io/badge/A%2FB_Test-Completed-success)
![Data Analysis](https://img.shields.io/badge/Data_Analysis-Python%20%7C%20Pandas-blue)
![Statistics](https://img.shields.io/badge/Statistics-Hypothesis_Testing%20%7C%20SciPy-orange)

## Executive Summary
An e-commerce platform theorized that simplifying its multi-step checkout process into a single page would reduce user friction and increase the overall conversion rate. 

To evaluate this, I conducted an A/B test exposing 50% of traffic to the legacy multi-step checkout (Control) and 50% to the new one-page checkout (Treatment). 

**Key Findings:**
- The one-page checkout resulted in a **statistically significant increase in Conversion Rate (CR)**.
- The Average Order Value (AOV) remained stable, confirming the new design did not deter high-value purchases.
- The uplift was consistent across both Desktop and Mobile devices.

**Recommendation:** Full rollout of the one-page checkout to 100% of user traffic to drive scalable top-line revenue growth.

---

## Business Problem
Cart abandonment is a major issue in e-commerce. The product team designed a new, streamlined one-page checkout to combat this. The goal of this project is to rigorously test if the new design genuinely improves performance without negatively impacting the average order value (AOV).

### Metrics Defined:
*   **Primary Metric:** Conversion Rate (CR) - The percentage of sessions resulting in a completed order.
*   **Secondary Metric:** Average Order Value (AOV) - The average dollar amount spent per converted order.

---

## Methodology

### 1. Data Collection & Preprocessing
- **Dataset:** ~100,000 synthetic, user session logs over a 2-week period.
- **Data Quality:** Conducted a rigorous **Sample Ratio Mismatch (SRM)** check using a Chi-Square goodness-of-fit test to ensure the traffic allocation algorithm functioned correctly (50/50 split). Verified and cleaned missing values.

### 2. Statistical Analysis
To draw robust, actionable conclusions, I utilized the following statistical methods:
- **Two-Proportion Z-Test:** Used to analyze the primary metric (Conversion Rate). Due to the large sample size (>100k), the sampling distribution of the sample proportion approaches a normal distribution, making the Z-test highly appropriate.
- **Welch's T-Test:** Used to analyze the secondary metric (Average Order Value) specifically on converted users. Welch's t-test was chosen over Student's t-test as it does not assume equal population variances (which was validated using Levene's test).

### 3. Segmentation
- Segmented the results by **Device Type (Desktop, Mobile, Tablet)** to ensure the new checkout experience was universally beneficial and didn't introduce platform-specific usability bugs.

---

## Deep Dive into the Code
The analysis explores an end-to-end framework, from data generation to business recommendations.

1.  **`generate_data.py`**: A robust Python script that generates synthetic e-commerce traffic, realistically simulating baseline conversion rates, variance by device, and log-normal distributions for order values.
2.  **`ab_testing_analysis.ipynb`**: The core analysis notebook. Highlights include:
    *   SRM sanity checks to validate experiment integrity.
    *   Clear Data Visualizations using Seaborn/Matplotlib.
    *   Rigorous application of `statsmodels` and `scipy.stats` for hypothesis testing.
    *   Business-focused interpretation of p-values and confidence intervals.

---

## How to Run Locally

### Prerequisites
- Python 3.9+
- Jupyter Notebook

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ab-testing-framework.git
   cd ab-testing-framework
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   # On Windows:
   .\venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install pandas numpy matplotlib seaborn scipy statsmodels jupyter
   ```
4. Generate the dataset:
   ```bash
   python generate_data.py
   ```
5. Launch the analysis notebook:
   ```bash
   jupyter notebook ab_testing_analysis.ipynb
   ```

---

## About the Author
I am a Data Analyst specializing in experimentation, product analytics, and translating complex statistical findings into clear, actionable business strategies. 

If you are looking for an analyst who understands that statistical significance is only valuable when it drives business impact, let's connect!

[https://deepak-lingala.github.io/]
