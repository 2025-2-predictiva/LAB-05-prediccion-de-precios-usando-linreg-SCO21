import pandas as pd

def load_and_process_data():
    import pandas as pd
    
    train_path = '../files/input/train_data.csv.zip'
    test_path = '../files/input/test_data.csv.zip'
    
    df_train = pd.read_csv(train_path, index_col=False, compression='zip')
    df_test = pd.read_csv(test_path, index_col=False, compression='zip')
    
    # Re nombranndo y removiendo columnas no necesarias
    df_train.rename(columns={'default payment next month': 'default'}, inplace=True)
    df_test.rename(columns={'default payment next month': 'default'}, inplace=True)
    df_train.drop(columns=['ID'], inplace=True)
    df_test.drop(columns=['ID'], inplace=True)

    # removiendo registros con informacion no disponible. Ceros en MARRIAGE y EDUCATION
    df_train = df_train.loc[df_train['EDUCATION'] != 0]
    df_train = df_train.loc[df_train['MARRIAGE'] != 0]
    df_test = df_test.loc[df_test['EDUCATION'] != 0]
    df_test = df_test.loc[df_test['MARRIAGE'] != 0]

    df_train['EDUCATION'] = df_train['EDUCATION'].apply(lambda x: 4 if x > 4 else x)
    df_test['EDUCATION'] = df_test['EDUCATION'].apply(lambda x: 4 if x > 4 else x)

    df_train = df_train.dropna()
    df_test = df_test.dropna()
    
    return df_train, df_test

def split_features_target(df_train, df_test):
    x_train = df_train.drop(columns=['default'])
    y_train = df_train['default']
    x_test = df_test.drop(columns=['default'])
    y_test = df_test['default']
    
    return x_train, y_train, x_test, y_test