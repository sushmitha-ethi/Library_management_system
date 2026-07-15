def clean_books(df):
    df['title'] = df['title'].str.strip().str.upper()
    df['copies'] = df['copies'].fillna(0)
    df = df.drop_duplicates(subset=['title'])
    return df


def clean_members(df):
    df['email'] = df['email'].str.strip().str.lower()
    df = df.drop_duplicates(subset=['email'])
    return df