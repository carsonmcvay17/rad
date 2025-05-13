# imports
import pandas as pd

class Data:
    def clean_data(self, data):
        df = pd.read_csv(data)

        # standardize string cases
        df['InjDefn'] = df['InjDefn'].str.lower().fillna('')
        df['InjJoint'] = df['InjJoint'].str.lower().fillna('')
        df['SpecInjury'] = df['SpecInjury'].str.lower().fillna('')

        # no injury mask
        is_uninjured = (
            (df['InjDefn'] == 'no injury') &
             ((df['InjJoint'] == 'no injury') | (df['InjJoint'] == '')) &
             (df['SpecInjury'] == '')
        )

        # filter
        df_clean = df[is_uninjured].copy()

        # drop injury columns
        injury_cols = [col for col in df_clean.columns if col.lower().startswith('inj')]
        inj_cols = [col for col in df_clean.columns if col.lower().startswith('spec')]
        race_cols = [col for col in df_clean.columns if col.lower().startswith('race')]
        activity_cols = [col for col in df_clean.columns if col.lower().startswith('activities')]
        lvl_cols = [col for col in df_clean.columns if col.lower().startswith('level')]
        yr_cols = [col for col in df_clean.columns if col.lower().startswith('yr')]
        num_cols = [col for col in df_clean.columns if col.lower().startswith('num')]
        df_clean.drop(columns=injury_cols, inplace=True)
        df_clean.drop(columns=inj_cols, inplace=True)
        df_clean.drop(columns=race_cols, inplace=True)
        df_clean.drop(columns=activity_cols, inplace=True)
        df_clean.drop(columns=lvl_cols, inplace=True)
        df_clean.drop(columns=yr_cols, inplace=True)
        df_clean.drop(columns=num_cols, inplace=True)
        df_clean.to_csv("non_injured_runners_metadata.csv", index=False)