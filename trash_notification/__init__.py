"""This is an app of notify trash pickup date."""

import datetime
import pandas as pd
import streamlit as st


def main():
    """表示系と大枠の流れを記載する。

    Args:
        none

    Returns:
        webpage(streamlit)

    """

    st.title("海田町ゴミ捨て日確認アプリ")

    # ①日にち情報の取得（選択した日と＋2日）
    min_date = datetime.date(2023, 1, 1)
    max_date = datetime.date(2024, 12, 31)
    selected_date = st.sidebar.date_input('確認したい日を入力してください。', datetime.date.today(),
                                          min_value=min_date, max_value=max_date)

    # ②地区情報の取得
    # TODO:選択履歴を残しておきたい。COOKIE。
    series_region = get_region_list(
        '/home/nee/git/notification_trash_pickup_day/input/2023/db_region_to_regioncode.csv')
    selected_region = st.sidebar.selectbox('表示する地区を選択：', series_region)

    # ③例外日取得（可燃ごみ、資源ごみ、大型ごみ）

    # ④各ゴミが出せる日であるか判定する。


def get_region_list(path_region_list_csv: str) -> pd.Series:
    """対象地区一覧を取得する。

    Args:
        path_region_list_csv (str): 地区の一覧を記載したCSVファイルのパス

    Returns:
        pd.Series: 地区の一覧を記載したSeries

    """
    df_region = pd.read_csv(path_region_list_csv)

    return df_region['地区']


def get_exceptday_list(path_eday_list_csv: str) -> pd.Series:
    """例外日を取得する。

    Args:
        path_eday_list_csv (str): 例外日の一覧を記載したCSVファイルのパス

    Returns:
        pd.Series: 例外日の一覧を記載したSeries
    """
    df_eday = pd.read_csv(path_eday_list_csv)

    return


if __name__ == '__main__':
    main()
