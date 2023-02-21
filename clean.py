import pandas as pd

def clean(input_file1, input_file2):
    df1 = pd.read_csv(input_file1)
    df2 = pd.read_csv(input_file2)
    df = df1.merge(df2, left_on='respondent_id', right_on='id', how='outer')
    df = df.drop('id', axis=1)
    df = df.dropna()
    df = df[~(df['job'].str.contains('insurance|Insurance'))]
    return df

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('input_1', help='respondent_contact file (CSV)')
    parser.add_argument('input_2', help='respondent_other file (CSV)')
    parser.add_argument('output', help='cleaned data file (CSV)')
    args = parser.parse_args()

    cleaned = clean(args.input_1, args.input_2)
    cleaned.to_csv(args.output, index=False)

    print('Output file shape: {}'.format(cleaned.shape))