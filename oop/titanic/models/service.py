from oop.titanic.models.dataset import Dataset
import pandas as pd #alias 표기
import numpy as np

'''
PassengerId  고객ID,
Survived 생존여부,
Pclass 승선권 1 = 1등석, 2 = 2등석, 3 = 3등석,
Name,
Sex,
Age,
SibSp 동반한 형제, 자매, 배우자,
Parch 동반한 부모, 자식,
Ticket 티켓번호,
Fare 요금,
Cabin 객실번호,
Embarked 승선한 항구명 C = 쉐브루, Q = 퀸즈타운, S = 사우스햄튼
'''
class Service (object):

    dataset = Dataset()

    def new_model(self, payload):
        this = self.dataset
        this.context = './data/'
        this.fname = payload
        return pd.read_csv(this.context + this.fname)

    @staticmethod
    def create_train(this):
        return this.train.drop('Survived', axis = 1)

    @staticmethod
    def create_label(this):
        return this.train['Survived']

    @staticmethod
    def drop_feature(this, feature) -> object:
        this.train = this.train.drop([feature], axis=1)
        this.test = this.test.drop([feature], axis=1)
        return this

    @staticmethod
    def embarked_nominal(this) -> object:
        this.train = this.train.fillna({'Embarked' : 'S'})
        this.test = this.test.fillna({'Embarked': 'S'})
        this.train['Embarked'] = this.train['Embarked'].map({'S' : 1, 'C' : 2, 'Q' : 3})
        this.test['Embarked'] = this.test['Embarked'].map({'S' : 1, 'C' : 2, 'Q' : 3})
        return this

    @staticmethod
    def fare_ordinal(this) -> object:
        this.train['FareBand'] = pd.qcut(this.train['Fare'], 4, labels={1, 2, 3, 4}) #FareBand는 new feature가 된다
        this.test['FareBand'] = pd.qcut(this.test['Fare'], 4, labels={1, 2, 3, 4})

        return this

    @staticmethod
    def fareBand_nominal(this) -> object:
        this.train = this.train.fillna({'FareBand': 1})
        this.test = this.test.fillna({'FareBand': 1})
        return this

    @staticmethod
    def title_nominal(this) -> object:
        combine = [this.train, this.test]

        for dataset in combine:
            dataset['Title'] = dataset['Name'].str.extract('([A-Za-z]+)\.', expand=False)

        for dataset in combine:
            dataset['Title'] = dataset['Title'].replace(
                ['Capt', 'Col', 'Don', 'Dr', 'Major', 'Rev', 'Jonkheer', 'Dona'], 'Rare')
            dataset['Title'] = dataset['Title'].replace(['Countess', 'Lady', 'Sir'], 'Royal')
            dataset['Title'] = dataset['Title'].replace('Mlle', 'Mr')
            dataset['Title'] = dataset['Title'].replace('Ms', 'Miss')
            dataset['Title'] = dataset['Title'].replace('Mme', 'Rare')

            title_mapping = {'Mr':1, 'Miss':2, 'Mrs':3, 'Master':4, 'Royal':5, 'Rare':6}

        for dataset in combine:
            dataset['Title'] = dataset['Title'].map(title_mapping)
            dataset['Title'] = dataset['Title'].fillna(0)

        #this.train = this.train
        #this.test = this.test

        return this

    @staticmethod
    def sex_nominal(this) -> object:
        combine = [this.train, this.test]
        sex_mapping = {'male': 0, 'female': 1}
        for dataset in combine:
            dataset['Sex'] = dataset['Sex'].map(sex_mapping)

        this.train = this.train
        this.test = this.test
        return this

    @staticmethod
    def age_ordinal(this) -> object:
        train = this.train
        test = this.test
        train['Age'] = train['Age'].fillna(-0.5)
        test['Age'] = test['Age'].fillna(-0.5)

        bins = [-1, 0, 5, 12, 18, 24, 35, 60, np.inf]
        labels = ['Unknown', 'Baby', 'Child', 'Teenager', 'Student', 'Young Adult', 'Adult', 'Senior']

        train['AgeGroup'] = pd.cut(train['Age'], bins, labels=labels)
        test['AgeGroup'] = pd.cut(test['Age'], bins, labels=labels)

        age_title_mapping = {0: 'Unknown', 1: 'Baby', 2: 'Child', 3: 'Teenager', 4: 'Student', 5: 'Young Adult', 6: 'Adult', 7:'Senior' }

        for x in range(len(train['AgeGroup'])):
            if train['AgeGroup'][x] == 'Unknown':
               train['AgeGroup'][x] = age_title_mapping[train['Title'][x]]

        for x in range(len(test['AgeGroup'])):
            if test['AgeGroup'][x] == 'Unknown':
               test['AgeGroup'][x] = age_title_mapping[test['Title'][x]]

        age_mapping = {
            'Unknown': 0, 'Baby': 1, 'Child': 2, 'Teenager': 3, 'Student': 4,
            'Young Adult': 5, 'Adult': 6, 'Senior': 7
        }

        train['AgeGroup'] = train['AgeGroup'].map(age_mapping)
        test['AgeGroup'] = test['AgeGroup'].map(age_mapping)

        this.train = train
        this.test = test

        return this

