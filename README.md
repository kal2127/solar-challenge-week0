MoonLight Energy Solutions: Solar Investment Strategy  

📘 Project Overview  
This project aims to develop a **data-driven framework for sustainable solar investment** across three West African countries — **Benin, Togo, and Sierra Leone.**  
By analyzing solar radiation data, operational efficiency, and maintenance costs, the project identifies the most promising region for investment.  

🎯 Project Goal  
To leverage **data science methodologies** to rank three countries for optimal solar investment potential based on:  
1. **Energy Yield** – Global Horizontal Irradiance (GHI)  
2. **Operational Efficiency** – Wind Cooling Effect (Wind Mitigation)  
3. **Maintenance Costs** – Soiling Loss  

-🧭 Methodology  

1️⃣ Data Preparation  
- Cleaned and formatted hourly solar radiation data for each country.  
- Handled missing values via median imputation.  
- Removed outliers using Z-score analysis.  
- Ensured consistent column names and structure across all datasets.  

2️⃣ Exploratory Data Analysis (EDA)  
- Visualized time-series patterns for GHI, DNI, DHI, and WS.  
- Compared daily and monthly radiation trends across countries.  
- Generated descriptive statistics and correlation plots.  

3️⃣ Cross-Country Comparison  
- Combined datasets for Benin, Togo, and Sierra Leone.  
- Used boxplots and summary statistics to analyze cross-country differences.  
- Applied Kruskal–Wallis H-Test for statistical comparison.  

4️⃣ Efficiency and Soiling Analysis  
- Modeled temperature and wind effects using Multiple Linear Regression:  
  `TModA ~ GHI + Tamb + WS`  
- Quantified soiling loss as the difference between clean and dirty module power.  

5️⃣ Investment Ranking  
| Rank | Country | Rationale |
|------|----------|------------|
| 🥇 1 | **Benin** | Highest GHI and best wind cooling performance. |
| 🥈 2 | **Togo** | Balanced GHI and lowest soiling loss. |
| 🥉 3 | **Sierra Leone** | Lowest GHI and highest soiling loss. |

⚙️ Tools & Technologies  

| Category | Tools |
|-----------|--------|
| Language | Python 3.x |
| Environment | Jupyter Notebook, Streamlit |
| Libraries | Pandas, NumPy, Matplotlib, Seaborn, Statsmodels |
| Version Control | Git & GitHub |
| CI/CD | GitHub Actions |
| Deployment | Streamlit Cloud |

🧠 Key Insights  
- **Benin** shows the best investment potential with the highest solar yield.  
- **Wind speed** is a key factor in cooling solar modules and improving efficiency.  
- **Soiling loss** impacts maintenance planning and energy yield prediction.  

🧩 Streamlit Dashboard  
An interactive dashboard was developed using **Streamlit** to visualize key metrics and explore solar data files.  

Features  
- Upload CSV files and preview data.  
- Display summary statistics and column details.  
- Generate simple plots for GHI, DNI, and WS.  

#Run Locally  
`bash
streamlit run app.py

Live Deployment
👉 [Streamlit Dashboard Link](https://solarproj.streamlit.app)


Author
Kalkidan Tesfaye
27kalkidan21@gmail.com
🔗 github.com/kal2127
🌐https://solarproj.streamlit.app
