""" This module contains dataframes for testing
    lambdatatoo functions and methods"""

import pandas as pd
import numpy as np

# Setup DataFrame to test MyReadyFrame within module
data = ([[1, '', 1, 4, np.nan, 6, '0', 2],
        [2, 2, 1, 0, 1, 6, 6, 2],
        ['0', 'x', '? ', 'x', '  ', 0, 'x'],
        [np.nan, '?', '? ', 'c ', ' x', ' 0 ', ],
        [.4, .5, .35, ' ?', np.nan, .55, ],
        [5, .55, 0, .5, .2, .4, .0, .6]])

names = ['int_a', 'int_b', 'str_a', 'str_b', 'fl_a', 'fl_b']

DF_TEST_1 = pd.DataFrame(data, index=names).T

# Setup DataFrame to test MyReadyFrame with unittest
data_null_4 = ([[1, '', '?', np.nan, '0', 2],
                ['? ', np.nan, '  x', '  ', 0, 'x '],
                [np.nan, '? ', '0 ', 'x', '1 ', ],
                [0, .35, ' ?', np.nan, .55, ],
                ])

names = ['int_a', 'str_a', 'str_b', 'fl_a']

DF_TEST_2 = pd.DataFrame(data_null_4, index=names).T
