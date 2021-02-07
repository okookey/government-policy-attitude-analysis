# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import baostock as bs


import WordSplit as jt
import MakeWordCloud as mw

def bs_login():
    return bs.login()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # lg = bs_login()
    # print("login respond error_code:" + lg.error_code)
    # print("login respond error_message：" + lg.error_msg)
    #
    # result = bs.query_history_k_data_plus(
    #     "sz.399417",
    #     "date,code,open,high,low,close,preclose,volume,amount,pctChg",
    #     start_date='2021-01-01',
    #     end_date='2021-02-03',
    #     frequency='d'
    # )
    #
    # print("query_history_k_data_plus respond error_code:" + result.error_code)
    # print("query_history_k_data_plus respond error_message" + result.error_msg)
    #
    # data_list = []
    #
    # while(result.error_code == '0') & result.next():
    #     data_list.append(result.get_row_data())
    # result = pd.DataFrame(data_list, columns=result.fields)
    # print(result)
    # result.to_csv("E:\data-temp-warehouse",header=True,index=True)
    # bs.logout()
    #
    #
    # print(result.dtypes)
    # result[["close"]] = result[["close"]].astype("float")
    # plt.subplots(figsize=(20,6))
    # plt.title("test-fig")
    # plt.plot(result.reset_index()["date"],result.reset_index()["close"],"b--")
    # plt.show()

    ttt = jt.WordSplit()
    srcName = "2020-11-13.txt"
    fileName = "2020-11-13.csv"
    return_dict = ttt.jieba_start(
        path="E:\\data-temp-warehouse\\"+srcName,
        save_path="E:\\data-temp-warehouse\\output\\"+fileName,
        save_to_csv=False
    )

    # print(return_dict)
    mw.MakeWordCloud().cloud_set(input_dict=return_dict)




