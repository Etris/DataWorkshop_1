import click
import pandas as pd


def read_raw(file_name):
    df = pd.read_csv(file_name, header=[0], sep=',', error_bad_lines=False)
    return df.drop(df.columns[0], axis=1)


def concat(df_1, df_2):
    dframe_1 = df_1.copy()
    dframe_2 = df_2.copy()
    return pd.concat([dframe_1, dframe_2], sort=False)


@click.command()
@click.argument('input_file', type=click.STRING)
@click.argument('output_file', type=click.Path(writable=True, dir_okay=False))
@click.option('--multi', type=click.BOOL)
def main(input_file, output_file, multi):
    print('Preprocessing data')
    if multi is True:
        print("list: ", input_file, ' -> ', output_file)
        files_list = input_file.split(',')
        base = pd.DataFrame()
        for element in files_list:
            df = read_raw(element)
            base = concat(base, df)
        base.dropna(axis=0, how="any", inplace=True)
        base.to_csv(output_file)
    else:
        print("single: ", input_file, ' -> ', output_file)
        base = read_raw(input_file)
        base.dropna(axis=0, how="any", inplace=True)
        base.to_csv(output_file)


if __name__ == '__main__':
    main()
