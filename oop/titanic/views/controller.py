from oop.titanic.models.dataset import Dataset
from oop.titanic.models.service import Service
import pandas as pd

class Controller (object):
    dataset = Dataset()
    service = Service()

    def modeling(self, train, test):
        service = self.service
        this = self.preprocess(train, test)
        this.label = service.create_label(this)
        this.train = service.create_train(this)
        return this


    def preprocess(self, train, test) -> object:
        service = self.service
        this = self.dataset
        this.train = service.new_model(train)
        this.test = service.new_model(test)
        this.id = this.test['PassengerId']
        #print(f'트레인 삭제 전 컬럼:{this.train.columns}')
        '''
        Index(['PassengerId', 'Survived ', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp',
               'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked'],
              dtype='object')
        '''
        this = service.drop_feature(this, 'Cabin')
        this = service.drop_feature(this, 'Ticket')
        this = service.drop_feature(this, 'PassengerId')
        #print(f'트레인 삭제 전 컬럼:{this.train.columns}')

        # 데이터 정재
        print(f'트레인 정제 전:\n{this.train}')
        this = service.embarked_nominal(this)
        this = service.fare_ordinal(this)
        this = service.fareBand_nominal(this)
        this = service.title_nominal(this)
        this = service.drop_feature(this, 'Name')
        this = service.sex_nominal(this)
        this = service.age_ordinal(this)
        this = service.drop_feature(this, 'Age')
        this = service.drop_feature(this, 'Fare')
        this = service.drop_feature(this, 'SibSp')
        this = service.drop_feature(this, 'Parch')

        print(f'트레인 정제 후:\n{this.train}')
        print(f'트레인 정제 후:\n{this.train.columns}')
        print(f'트레인 정제 후:\n{this.train.isnull().sum()}')

        return this




