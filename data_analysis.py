# data_analysis.py

import pandas as pd
from datetime import datetime

def commits_to_dataframe(commits):
    data = []
    for commit in commits:
        try:
            data.append({
                "author": commit.commit.author.name,
                "date": commit.commit.author.date,
                "message": commit.commit.message,
                "sha": commit.sha
            })
        except:
            continue  # pode ter commit sem autor (bot ou erro)

    df = pd.DataFrame(data)
    df["date"] = pd.to_datetime(df["date"])
    return df


def contributors_to_dataframe(contributors):
    data = []
    for user in contributors:
        data.append({
            "login": user.login,
            "contributions": user.contributions
        })

    return pd.DataFrame(data)
