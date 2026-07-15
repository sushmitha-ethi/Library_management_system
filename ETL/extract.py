import pandas as pd

def extract_books():
    return pd.read_csv("../books.csv")

def extract_members():
    return pd.read_csv("../members.csv")

def extract_issues():
    return pd.read_csv("../issues.csv")