## Project Topic and Overview

Anatomy of a Blockbuster. 

This project explores a large collection of movie industry data to answer key questions about what makes a film successful:

* How do **budget levels** influence box office revenue?
* What is the relationship between **movie genre** and audience ratings?
* Do certain genres consistently outperform others in profitability?
* Have film revenues and ratings changed over time?
* Are there patterns linking **runtime**, **release year**, and success metrics?

This project performs a comprehensive analysis of the factors that shape a movie's financial and critical performance. Using movie metadata, it examines several important indicators, including:

* **Budget**
* **Revenue**
* **Genre**
* **Runtime**
* **Release_year**
* **Vote_average (rating)**
* **Profitability (revenue – budget)**

Through statistical exploration and visualization, the project uncovers hidden trends behind cinematic hits and provides insights into the formula for a blockbuster.

## Project Structure
```
ANATOMY_OF_BLOCKBUSTER/
│
├── application/                     # Web Application level: streamlit visualization 
│   ├── __init__.py
│   └── app.py
│
├── blockbuster_analysis/            # Core analysis modules
│   ├── __init__.py
│   ├── actor_popularity_vs_avg_rating_movie.py
│   ├── budget_vs_revenue.py
│   ├── genre_avg_rating.py
│   ├── genre_avg_revenue.py
│   ├── models.py
│   ├── revenue_by_year.py
│   ├── runtime_vs_revenue.py
│
├── datasets/                        # Movie datasets used for analysis
│   ├── credits_small.csv
│   ├── keywords.csv
│   ├── links_small.csv
│   ├── movies_metadata.csv
│   └── ratings_small.csv
│
├── presentation/                    # Jupyter notebooks, visuals, insights
│   └── project_analysis.ipynb
│
├── tests/                           # Unit tests for project modules
│
├── requirements.txt                 # Python dependencies
├── README.md                        # Project documentation
└── .gitignore                       # Files ignored by Git
```
## Installation

 1. Clone the Repository
```
git clone https://github.com/ely0rbek/Anatomy-of-a-Blockbuster.git
cd Anatomy-of-a-Blockbuster
```
 2. Create the virtual environment
```
python -m venv blockbuster
```
 3. Activate Virtual Environment
 4. Install Dependencies
```
pip install -r requirements.txt
```

## Running the Project
 Option 1: Run the Streamlit application
```
streamlit run application/app.py
```
 Option 2: Via Jupyter Notebook <br>
 You can see the analysis through the ```presentation/project_analysis.ipynb```.