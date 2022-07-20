def clean_df(df):
    y = df['y']
    X = df.drop('y', axis=1)
    
    job_df = pd.get_dummies(df.job, prefix='job')
    marital_df = pd.get_dummies(df.marital, prefix='marital')
    education_df = pd.get_dummies(df.education, prefix='education')