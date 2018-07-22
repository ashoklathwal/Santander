from base import Feature, get_arguments, generate_features
import pandas as pd


class select_features(Feature):
    def create_features(self):
        select =  [
            'f190486d6', 'c47340d97', 'eeb9cd3aa', '66ace2992', 'e176a204a',
            '491b9ee45', '1db387535', 'c5a231d81', '0572565c2', '024c577b9',
            '15ace8c9f', '23310aa6f', '9fd594eec', '58e2e02e6', '91f701ba2',
            'adb64ff71', '2ec5b290f', '703885424', '26fc93eb7', '6619d81fc',
            '0ff32eb98', '70feb1494', '58e056e12', '1931ccfdd', '1702b5bf0',
            '58232a6fb', '963a49cdc', 'fc99f9426', '241f0f867', '5c6487af1',
            '62e59a501', 'f74e8f13d', 'fb49e4212', '190db8488', '324921c7b',
            'b43a7cfd5', '9306da53f', 'd6bb78916', 'fb0f5dbfe', '6eef030c1'
            ]
        self.train = train[select]
        self.test = test[select]

if __name__ == '__main__':
    args = get_arguments()

    train = pd.read_csv('input/train.csv')
    test = pd.read_csv('input/test.csv')

    select_features().run().save()