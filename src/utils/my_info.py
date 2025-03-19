
# my_default_prompt="""navigate to the website from the additional information. Create a account from the using email address "kinwong.ds@gmail.com" and password of "G1ttingOffers1nWA!". Task is completed after account is created"""

my_default_prompt="""Initiate the job application process from the job application links. If a user account is required, try to singin using my account_info, if no account exist, create one using my personal information. If a resume upload is necessary, pause the process and prompt me to upload it from my computer. If the application is successfully completed, pause before submitting the final application, allowing me to review it."""


with open('src/utils/job_apps_links.yaml', 'r') as f:
    lines = f.readlines()
job_apps_links = [line.strip() for line in lines]

my_add_infos=f"""
Job application links: {job_apps_links}

account_info (for creating account also):
  username: kinwongds
  email_address: kinwong.ds@gmail.com
  password: G1ttingOffers1nWA!

personal_information:
  name: "Kin"
  surname: "Wong"
  country: "United States"
  city: "Kirkland"
  state: "Washington"
  address: "9736 NE 119th Way"
  zip_code: "98034"
  phone type: "mobile"
  phone: "8324368892"
  email: "kinwong.ds@gmail.com"
  github: "https://github.com/kinwong-ds"
  linkedin: "https://linkedin.com/in/ki-wong"
  personal_website: "kinwong.info"

education_details:
  - education_level: "Master's Degree"
    institution: "University of California Riverside"
    field_of_study: "Engineering and Data Science"
    final_evaluation_grade: "3.93"
    start_date: "2019"
    year_of_completion: "2021"

  - education_level: "Bachlor's Degree"
    institution: "University of Houston"
    field_of_study: "Computer and Information System"
    final_evaluation_grade: "3.74"
    start_date: "2013"
    year_of_completion: "2018"

experience_details:
  - position: "Data Scientist II"
    company: "Optum - UnitedHealth Group"
    employment_period: "04/2022 - 02/2025"
    location: "Remote"
    industry: "Healthcare"
    key_responsibilities:
      - responsibility_1: "Implemented a Large Language Model (LLM) for medical contract rate extraction to prevent rate mismatches."
      - responsibility_2: "Created an ML pipeline reduce 30% of claims in post-pay claim inventory with an increase of 20% true positive rate, reducing auditor needs by 2 across 3 platforms."
      - responsibility_3: "Optimized claim audit prioritization and saved over $144K annually by using PySpark for data cleaning, feature selection, and feature engineering in a claim tiering pipeline."
      - responsibility_4: "Supervised a production claim tiering pipeline in Apache Airflow, account for $13.8M in annual savings by ensuring system performance through resolving Kubernetes errors, managing Docker image builds, and performing Spark version upgrades."
      - responsibility_5: "Collaborated with engineering and operations teams to address system performance issues and engaged with business stakeholders to provide insights and answers."
      - responsibility_6: "Developed a Streamlit dashboard for a claim tiering pipeline, leveraged by leadership to track KPIs and key metrics like feature drift and recovery amounts, enabling actionable insights, business decisions, and early issue detection."

  - position: "NLP Data Scientist"
    company: "HP Inc."
    employment_period: "07/2021 - 04/2022"
    location: "Houston, TX"
    industry: "Consumer Technology"
    key_responsibilities:
      - responsibility_1: "Developed a deep learning MLOps pipeline to process over 2 million call logs weekly, providing insights into product issues and enabling targeted actions by the operational team."
      - responsibility_2: "Fine-tuned BERT models to classify unstructured text data from helpdesk call logs, improving classification accuracy by 15% as part of a MLOps pipeline."
      - responsibility_3: "Implemented FastText and mBART models on premise to identify languages of conversational text and translate non- English text, enabling analysis of product issues from overseas customers."
      - responsibility_4: "Apply mBART model to translate non-English text on premise to address customer issues in multiple languages."
      - responsibility_5: "Increased classification model accuracy by 20% by summarizing call logs using a GPT model."
      - responsibility_6: "Created an OCR image to text pipeline using easyocr and cv2, saving 50 hours of manual data entry per month."

  - position: "Data Scientist"
    company: "Calpine Corporation"
    employment_period: "08/2019 - 07/2021"
    location: "Houston, TX"
    industry: "Energy"
    key_responsibilities:
      - responsibility_1: "Engineered features and developed time series models for machine learning projects, including anomaly detection to correct faulty turbine sensor outputs."
      - responsibility_2: "Developed data pipelines and a classification system using ensemble methods to transform power plant data and accelerate turbine maintenance processes."
      - responsibility_3: "Created an NLP model to categorize business reports, enhancing report classification efficiency."

  - position: "Data Analyst"
    company: "Calpine Corporation"
    employment_period: "07/2017 - 12/2018"
    location: "Houston, TX"
    industry: "Energy"
    key_responsibilities:
      - responsibility_1: "Streamlined system report for power plant users by developing a PowerApps application integrated with SharePoint."
      - responsibility_2: "Designed, enhanced, and tested BIRT reports from EAM software Maximo utilizing SQL and JavaScript, delivering tailored solutions to meet business needs."
      - responsibility_3: "Created on-demand SSRS reports using real-time data to improve power plant operational insights."

skills:
  - "Streamlit Dashboard"
  - "Spark"
  - "Apache Airflow"
  - "Code reviews"
  - "Streamlit Dashboard"
  - "MLOps pipeline management"
  - "Docker"
  - "Data Analytic"
  - "Data Cleaning"
  - "Deep Learning"
  - "Transformer"
  - "Fine Tuning LLM"
  - "GPT"
  - "OCR"
  - "Machine Learning"
  - "Time Series Analysis"
  - "Anomaly Detection"
  - "Data Pipelines"
  - "Ensemble Methods"
  - "Natural Language Processing"
  - "PowerApps"
  - "SharePoint"
  - "SQL"
  - "JavaScript"
  - "BIRT Reporting"
  - "SSRS Reporting"

achievements:
  - name: "Hackathon winner"
    description: "Open Source AI 14th Hackathon - AI Agent"
  - name: "Diamond Award"
    description: "UnitedHealth Group Employee Recognition Program"

certifications:
  - name: "Azure DP-100"
    description: "Azure Data Scientist Associate"
  - name: "Azure AZ-900"
    description: "Azure Fundamentals"
  - name: "Azure AI-900"
    description: "Azure AI Fundamentals"
  - name: "Azure AZ-900"
    description: "Azure Data Fundamentals"

languages:
  - language: "English"
    proficiency: "Fluent or Native"
  - language: "Chinese"
    proficiency: "Fluent or Native"

interests:
  - "Cybersecurity"
  - "Home Server and Private Cloud"
  - "Machine Learning"

availability:
  notice_period: "1 week"

salary_expectations:
  salary_range_usd: "120000 - 140000"
  salary_usd: "130000"

self_identification:
  gender: "Male"
  pronouns: "he/him"
  veteran: "No"
  disability: "No"
  ethnicity: "Asian"

legal_authorization:
  us_work_authorization: "Yes"
  requires_us_visa: "No"
  requires_us_sponsorship: "No"
  legally_allowed_to_work_in_us: "Yes"

work_preferences:
  remote_work: "Yes"
  in_person_work: "Yes"
  open_to_relocation: "No"
  willing_to_complete_assessments: "Yes"
  willing_to_undergo_drug_tests: "Yes"
  willing_to_undergo_background_checks: "Yes"

How did I hear about the job: "Job Board"
  site: "Dice, Indeed"
"""
