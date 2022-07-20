def clean_df(df):
    y = df['y']
    X = df.drop('y', axis=1)
    
    job_df = pd.get_dummies(df.job, prefix='job')
    marital_df = pd.get_dummies(df.marital, prefix='marital')
    education_df = pd.get_dummies(df.education, prefix='education')
    
    
X.drop(['job', 'marital', 'education'], axis=1, inplace=True)
X = pd.concat([X, job_df, marital_df, education_df], axis=1)
X.month.replace(month_dic, inplace=True)
X.replace({"no": 0, "yes": 1}, inplace=True)