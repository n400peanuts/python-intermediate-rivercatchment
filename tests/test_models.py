"""Tests for statistics functions within the Model layer."""

import pandas as pd
import pandas.testing as pdt
import datetime
import pytest


def test_daily_mean_zeros():
    """Test that mean function works for an array of zeros."""
    from catchment.models import daily_mean

    test_input = pd.DataFrame(
                     data=[[0.0, 0.0],
                           [0.0, 0.0],
                           [0.0, 0.0]],
                     index=[pd.to_datetime('2000-01-01 01:00'),
                            pd.to_datetime('2000-01-01 02:00'),
                            pd.to_datetime('2000-01-01 03:00')],
                     columns=['A', 'B']
    )
    test_result = pd.DataFrame(
                     data=[[0.0, 0.0]],
                     index=[datetime.date(2000, 1, 1)],
                     columns=['A', 'B']
    )

    # Need to use Pandas testing functions to compare arrays
    pdt.assert_frame_equal(daily_mean(test_input), test_result)


def test_daily_mean_integers():
    """Test that mean function works for an array of positive integers."""
    from catchment.models import daily_mean

    test_input = pd.DataFrame(
                     data=[[1, 2],
                           [3, 4],
                           [5, 6]],
                     index=[pd.to_datetime('2000-01-01 01:00'),
                            pd.to_datetime('2000-01-01 02:00'),
                            pd.to_datetime('2000-01-01 03:00')],
                     columns=['A', 'B']
    )
    test_result = pd.DataFrame(
                     data=[[3.0, 4.0]],
                     index=[datetime.date(2000, 1, 1)],
                     columns=['A', 'B']
    )

    # Need to use Pandas testing functions to compare arrays
    pdt.assert_frame_equal(daily_mean(test_input), test_result)


def test_daily_min():
    """Test that daily min works as expected"""
    from catchment.models import daily_min

    test_input = pd.DataFrame(
        data=[[1, 2],
              [7, 4],
              [9, 6]],
        index=[pd.to_datetime('2000-01-01 01:00'),
               pd.to_datetime('2000-01-01 02:00'),
               pd.to_datetime('2000-01-01 03:00')],
        columns=['A', 'B']
    )
    test_result = pd.DataFrame(
                     data=[[1, 2]],
                     index=[datetime.date(2000, 1, 1)],
                     columns=['A', 'B']
    )

    pdt.assert_frame_equal(daily_min(test_input), test_result)

def test_daily_max():
    """Test that daily max works as expected"""
    from catchment.models import daily_max

    test_input = pd.DataFrame(
        data=[[1, 2],
              [7, 4],
              [9, 6]],
        index=[pd.to_datetime('2000-01-01 01:00'),
               pd.to_datetime('2000-01-01 02:00'),
               pd.to_datetime('2000-01-01 03:00')],
        columns=['A', 'B']
    )
    test_result = pd.DataFrame(
                     data=[[9, 6]],
                     index=[datetime.date(2000, 1, 1)],
                     columns=['A', 'B']
    )

    pdt.assert_frame_equal(daily_max(test_input), test_result)

def test_daily_max_alternative():
    """Test that daily max works as expected"""
    from catchment.models import daily_max

    test_input = pd.DataFrame(
        data=[[1, 2],
              [7, 4],
              [9, 6]],
        index=[pd.to_datetime('2000-01-01 01:00'),
               pd.to_datetime('2000-01-01 02:00'),
               pd.to_datetime('2000-01-01 03:00')],
        columns=['A', 'B']
    )
    test_result_max = []
    for i in range(len(test_input.columns)):
        test_result_max.append(max(test_input.iloc[:, i]))
    test_result = pd.DataFrame(
        data=[test_result_max],
        index=[datetime.date(2000, 1, 1)],
        columns=['A', 'B']
    )
    pdt.assert_frame_equal(daily_max(test_input), test_result)

@pytest.mark.parametrize(
    "test_data, test_index, test_columns, expected_data, expected_index, expected_columns",
    [
        (
            [[0.0, 0.0], [0.0, 0.0], [0.0, 0.0]],
            [pd.to_datetime('2000-01-01 01:00'),
             pd.to_datetime('2000-01-01 02:00'),
             pd.to_datetime('2000-01-01 03:00')],
            ['A', 'B'],
            [[0.0, 0.0]],
            [datetime.date(2000, 1, 1)],
            ['A', 'B']
        ),
        (
            [[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]],
            [pd.to_datetime('2000-01-01 01:00'),
             pd.to_datetime('2000-01-01 02:00'),
             pd.to_datetime('2000-01-01 03:00')],
            ['A', 'B'],
            [[3.0, 4.0]],
            [datetime.date(2000, 1, 1)],
            ['A', 'B']
        )
    ]
)


def test_daily_mean(test_data, test_index, test_columns,
                    expected_data, expected_index, expected_columns):
    """Test whether mean function works with zeros and positive integers"""
    from catchment.models import daily_mean
    pdt.assert_frame_equal(
        daily_mean(pd.DataFrame(
            data=test_data,
            index=test_index,
            columns=test_columns
            )
        ),
        pd.DataFrame(
            data=expected_data,
            index=expected_index,
            columns=expected_columns
        )
    )

@pytest.mark.parametrize(
    "test_data_max, test_index_max, test_columns_max, expected_data_max, expected_index_max, expected_columns_max",
    [
        (
            [[1.0, 2.0], [7.0, 4.0], [9.0, 6.0]],
            [pd.to_datetime('2000-01-01 01:00'),
             pd.to_datetime('2000-01-01 02:00'),
             pd.to_datetime('2000-01-01 03:00')],
            ['A', 'B'],
            [[9.0, 6.0]],
            [datetime.date(2000, 1, 1)],
            ['A', 'B']
        )
    ]
)

def test_daily_max(test_data_max, test_index_max, test_columns_max,
                    expected_data_max, expected_index_max, expected_columns_max):
    """Test whether mean function works with zeros and positive integers"""
    from catchment.models import daily_max
    pdt.assert_frame_equal(
        daily_max(pd.DataFrame(
            data=test_data_max,
            index=test_index_max,
            columns=test_columns_max
            )
        ),
        pd.DataFrame(
            data=expected_data_max,
            index=expected_index_max,
            columns=expected_columns_max
        )
    )


