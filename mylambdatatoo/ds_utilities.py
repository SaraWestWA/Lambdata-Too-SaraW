"""A collection of data science utility functions."""

import warnings
import pandas as pd
import numpy as np

from test_frames import DF_TEST_1


class MyReadyFrame():
    """The MyReadyFrame class is used to examine and clean dataframes."""

    def __init__(self, frame, npnan=True, zero=True, qmark=True, missing=True):
        """
        Param 'frame' is a dataframe which can have both catagorical and numeric
        data. Other attributes describe possible null values in the frame.

        Class exists to examine and clean dataframes.
        """
        self.frame = frame
        self.npnan = npnan
        self.zero = zero
        self.qmark = qmark
        self.missing = missing

    def __repr__(self):
        """__rep__ describes the shape of the dataframe self.frame"""
        return (f"""The dataframe to be examined/cleaned has shape {self.frame.shape}.""")

    def __str__(self):
        """
        __str__ describes the shape of the dataframe self.frame
        and the boolean status of other attributes.
        """
        x = self.npnan + self.zero + self.qmark + self.missing
        return (f"""Frame shape: {self.frame.shape}. Null types: {x}.""")

    def null_counts(self):
        """
        Param MyReadyFrame object: self.frame is a dataframe.
        npnan, zero, qmark, and missing determine which null values are counted.

        Method returns a dataframe of counts for specified null values and 0,
        includes a total column.
        """
        # surpress warning comparing pd objects to np.nan
        warnings.simplefilter(action='ignore', category=FutureWarning)
        df_null = self.frame.applymap(lambda x: x.strip() if isinstance(x, str) else x)
        columns = list(df_null.columns)
        options = [self.npnan, self.zero, self.qmark, self.missing]
        null_name = ['NaN', 0, '?', 'Missing']
        keeper = []
        index = []
        n_c = []

        for j in range(4):
            if options[j] is True:
                index.append(null_name[j])
                n_c = []
                for i in columns:
                    null_function = [
                                    df_null[i].isnull().sum(),
                                    (sum(df_null[i] == '0') + sum(df_null[i] == 0)),
                                    sum(df_null[i] == '?'),
                                    sum(df_null[i] == '')
                                    ]
                    nan_count = null_function[j]
                    n_c.append(nan_count)
                keeper.append(n_c)
        if keeper == []:
            null_count = "No count of null values requested. Please change an attribute to True."
        else:
            null_count = pd.DataFrame(data=keeper, index=index, columns=columns)
            null_count['TOTAL'] = null_count.sum(axis=1)
        return null_count

    def clean_frame(self):
        """
        Param MyReadyFrame object.

        Method returns the dataframe with leading and trailing zeros removed;
        '?','', and empty cells replaced with NaN, dtype changed to float,
        if possible.
        """
        self.frame = (self.frame).applymap(lambda x: x.strip()
                        if isinstance(x, str) else x)
        self.frame = (self.frame).applymap(lambda x: np.nan
                        if isinstance(x, str) and x == '' or
                        x is None or x == '?' else x)
        self.frame.apply(pd.to_numeric, errors='ignore')
        return self.frame

if __name__ == '__main__':
# Make class variable
    # dft = MyReadyFrame(DF_TEST_1, False, False, False, False)
    dft = MyReadyFrame(DF_TEST_1)
    print('---'*8)
    print(dft.frame, '\n', '---'*8)

# Simple Test for null_counts function,
    z = MyReadyFrame.null_counts(dft)
    print(z, '\n', '---'*8)

# Simple Test for clean_frame method
    dfc = MyReadyFrame.clean_frame(dft)
    print(dfc,'\n', '---'*8)

    z2 = MyReadyFrame.null_counts(dft)
    print(z2, '\n', '---'*8)

    print(dft.frame.dtypes)

# Simple Test for dunder methods
    print(repr(dft), '\n', '---'*8)

    print(dft)
