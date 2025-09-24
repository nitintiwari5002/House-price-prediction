
#  🏠 HOUSE PREDICTION MODEL
[![VS Code](https://img.shields.io/badge/VS%20Code-IDE-007ACC?logo=visual-studio-code)](https://code.visualstudio.com/) 
[![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)](https://www.python.org/)
[![Scikit-learn](https://img.shields.io/badge/Scikit--Learn-ML-F7931E?logo=scikitlearn)](https://scikit-learn.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-UI-red?logo=streamlit)](https://streamlit.io/)
[![Joblib](https://img.shields.io/badge/Joblib-Model-Purple?logo=python)](https://joblib.readthedocs.io/)
[![ChatGPT](https://img.shields.io/badge/ChatGPT-AI-00FFFF?logo=openai)](https://chat.openai.com/)
---
A machine learning project to predict house prices based on features like living area, overall quality, garage size, basement area, and number of bathrooms. The project includes a **Streamlit UI** for interactive predictions, displaying the predicted price in **Indian Rupees (₹)**.

---



## 📊 Dataset

The dataset contains the following features used for house price prediction:

| Column        | Description                           |
|---------------|---------------------------------------|
| ⭐ OverallQual   | Overall quality of the house (1–10)  |
| 🏠 GrLivArea     | Above ground living area in sq ft    |
| 🚗 GarageCars    | Number of cars the garage can hold    |
| 🏢 TotalBsmtSF   | Total basement area in sq ft          |
| 🛁 FullBath      | Number of full bathrooms              |
| 💰 SalePrice     | Target house price in USD             |


### ⚠️ If `house_prices.csv` does not exist, the script automatically generates a synthetic dataset.


## 🚀 Getting Started

#### 1️⃣ Install Dependencies

```bash
pip install -r requirements.txt

Includes: pandas, scikit-learn, joblib, streamlit.

```

#### 2️⃣ Run the Streamlit App
```bash
streamlit run house_price_app.py

```

- Enter house details using the interactive UI.

- Click Predict Price to see the value in ₹ (Rupees).

###  **Note:** ⚠️ Always use streamlit run — running with python house_price_app.py will not display the UI.

## 🔮 Features
- 🖥️ Single Python file handles training + prediction + UI.

- 💵 Converts predicted price to Indian Rupees (₹).

- 📊 Self-contained: generates synthetic dataset if none is provided.

- 🌐 Interactive Streamlit interface for easy use.

- Interactive and user-friendly Streamlit interface.

## 🔧 Future Improvements

- Use a real-world dataset for higher accuracy.

- Add more features: location, year built, neighborhood, etc.

- Experiment with advanced models: XGBoost, LightGBM, neural networks.

- Deploy the app online (Streamlit Cloud, Heroku) for public access.

## 📸 Screenshots
### Code for training the model
<img width="1919" height="571" alt="Image" src="https://github.com/user-attachments/assets/ece018f2-7641-4593-a428-db9c0c2bf410" />

### Trained the model
<img width="1918" height="766" alt="Image" src="https://github.com/user-attachments/assets/6cbbfd21-2b40-46cd-b7c7-5aba8414e556" />

### Code for predicting the model
<img width="1329" height="709" alt="Image" src="https://github.com/user-attachments/assets/79c84bdc-0a13-4813-9616-16aaf63463ab" />

### Web page 
<img width="1919" height="1066" alt="Image" src="https://github.com/user-attachments/assets/eb612310-41b6-4971-b2e0-b551e170472c" />


## 🔑 Setup & Usage
1. **Clone this repository**  
   ```bash
   git clone https://github.com/nitintiwari5002/House-price-prediction.git
   cd House-price-prediction

---

## 🤝 Contributing
Contributions are welcome! 🎉  
To contribute:  
1. **Fork** the repository  
2. **Create a new branch** (`feature-new`)  
3. **Commit your changes**  
4. **Push to the branch**  
5. Open a **Pull Request** 🚀  

---

## 👨‍💻 Author
**Nitin Tiwari**  
- GitHub: https://github.com/nitintiwari5002
- LinkedIn: https://linkedin.com/in/nitin-krishnakumar-tiwari-685557376 
