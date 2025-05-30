
# 📊 Company Monthly Hours Dashboard

A simple and interactive Streamlit dashboard for analyzing and visualizing employee monthly working hours across different companies and cities. This tool helps HR teams, analysts, and managers gain insights into work hour distributions using filters, summary statistics, and visual plots.

---

## 🚀 Features

- Upload CSV or Excel datasets.
- Filter data by **City** and **Company**.
- View raw and filtered data tables.
- Get **summary statistics** (mean, min, max of monthly hours).
- Visualize data with **box plots** grouped by city.

---

## 🖥️ Demo

![Screenshot](screenshot.png)  
*Example dashboard interface*

---

## 📂 File Upload Format

Your dataset should include at least the following columns:

| Column Name    | Description                            |
|----------------|----------------------------------------|
| `City`         | Name of the city                      |
| `Company`      | Name of the company                   |
| `MonthlyHours` | Monthly working hours (numerical)     |

Example:

```csv
City,Company,MonthlyHours
New York,TechCorp,160
San Francisco,HealthInc,145
````

---

## ▶️ How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/monthly-hours-dashboard.git
cd monthly-hours-dashboard
```

### 2. Install Dependencies

It's recommended to use a virtual environment:

```bash
pip install -r requirements.txt
```

### 3. Launch the App

```bash
streamlit run app.py
```

---

## 🛠️ Tech Stack

* [Streamlit](https://streamlit.io/) – for building the dashboard UI
* [Pandas](https://pandas.pydata.org/) – for data manipulation
* [Seaborn](https://seaborn.pydata.org/) – for data visualization
* [Matplotlib](https://matplotlib.org/) – for plotting

---

## 📄 License

MIT License. Feel free to use, modify, and share this project.

---

## 🤝 Contributions

Pull requests, feature suggestions, and bug reports are welcome!

---

## 📬 Contact

For questions or collaboration, please reach out at \[[gjahanvis07@gmail.com](mailto:your-email@example.com)].

