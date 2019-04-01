import numpy as np
import pandas as pd
import spacy
from spacy import displacy
nlp = spacy.load('en_core_web_sm')
import nltk
from sklearn import *
from sklearn.ensemble import RandomForestClassifier
import xgboost as xgb
from xgboost import XGBClassifier

import warnings
warnings.filterwarnings('ignore')

test = pd.read_csv('test_stage_1.tsv', delimiter='\t').rename(columns={'A': 'A_Noun', 'B': 'B_Noun'})
sub = pd.read_csv('sample_submission_stage_1.csv')
test.shape, sub.shape

# True test here:
#gh_train = pd.read_csv("https://raw.githubusercontent.com/google-research-datasets/gap-coreference/master/gap-development.tsv", delimiter='\t')

gh_test = pd.read_csv("https://raw.githubusercontent.com/google-research-datasets/gap-coreference/master/gap-test.tsv", delimiter='\t')
gh_valid = pd.read_csv("https://raw.githubusercontent.com/google-research-datasets/gap-coreference/master/gap-validation.tsv", delimiter='\t')
train = pd.concat((gh_test, gh_valid)).rename(columns={'A': 'A_Noun', 'B': 'B_Noun'}).reset_index(drop=True)
a = train.shape


def name_replace(s, r1, r2):
    s = str(s).replace(r1, r2)
    for r3 in r1.split(' '):
        s = str(s).replace(r3, r2)
    return s


def get_features(df):
    df['section_min'] = df[['Pronoun-offset', 'A-offset', 'B-offset']].min(axis=1)
    df['Pronoun-offset2'] = df['Pronoun-offset'] + df['Pronoun'].map(len)
    df['A-offset2'] = df['A-offset'] + df['A_Noun'].map(len)
    df['B-offset2'] = df['B-offset'] + df['B_Noun'].map(len)
    df['section_max'] = df[['Pronoun-offset2', 'A-offset2', 'B-offset2']].max(axis=1)
    # df['Text'] = df.apply(lambda r: r['Text'][: r['Pronoun-offset']] + 'pronountarget' + r['Text'][r['Pronoun-offset'] + len(str(r['Pronoun'])): ], axis=1)
    df['Text'] = df.apply(lambda r: name_replace(r['Text'], r['A_Noun'], 'subjectone'), axis=1)
    df['Text'] = df.apply(lambda r: name_replace(r['Text'], r['B_Noun'], 'subjecttwo'), axis=1)

    df['A-dist'] = (df['Pronoun-offset'] - df['A-offset']).abs()
    df['B-dist'] = (df['Pronoun-offset'] - df['B-offset']).abs()
    return (df)


train = get_features(train)
test = get_features(test)

def get_nlp_features(s, w):
    doc = nlp(str(s))
    tokens = pd.DataFrame([[token.text, token.dep_] for token in doc], columns=['text', 'dep'])
    return len(tokens[((tokens['text']==w) & (tokens['dep']=='poss'))])

train['A-poss'] = train['Text'].map(lambda x: get_nlp_features(x, 'subjectone'))
train['B-poss'] = train['Text'].map(lambda x: get_nlp_features(x, 'subjecttwo'))
test['A-poss'] = test['Text'].map(lambda x: get_nlp_features(x, 'subjectone'))
test['B-poss'] = test['Text'].map(lambda x: get_nlp_features(x, 'subjecttwo'))

train = train.rename(columns={'A-coref':'A', 'B-coref':'B'})
train['A'] = train['A'].astype(int)
train['B'] = train['B'].astype(int)
train['NEITHER'] = 1.0 - (train['A'] + train['B'])

col = ['Pronoun-offset', 'A-offset', 'B-offset', 'section_min', 'Pronoun-offset2', 'A-offset2', 'B-offset2', 'section_max', 'A-poss', 'B-poss', 'A-dist', 'B-dist']
x1, x2, y1, y2 = model_selection.train_test_split(train[col].fillna(-1), train[['A', 'B', 'NEITHER']], test_size=0.2, random_state=1)
x1.head()

model = multiclass.OneVsRestClassifier(ensemble.RandomForestClassifier(max_depth = 7, n_estimators=1000, random_state=33))
# model = multiclass.OneVsRestClassifier(ensemble.ExtraTreesClassifier(n_jobs=-1, n_estimators=100, random_state=33))

# param_dist = {'objective': 'binary:logistic', 'max_depth': 1, 'n_estimators':1000, 'num_round':1000, 'eval_metric': 'logloss'}
# model = multiclass.OneVsRestClassifier(xgb.XGBClassifier(**param_dist))

model.fit(x1, y1)
print('log_loss', metrics.log_loss(y2, model.predict_proba(x2)))
model.fit(train[col].fillna(-1), train[['A', 'B', 'NEITHER']])
results = model.predict_proba(test[col])
test['A'] = results[:,0]
test['B'] = results[:,1]
test['NEITHER'] = results[:,2]
test[['ID', 'A', 'B', 'NEITHER']].to_csv('submission.csv', index=False)