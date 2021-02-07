import jieba as jb
import numpy as np
from typing import List, Dict
import pandas as pd
from pandas import DataFrame


class WordSplit:

    def read_file(self, path: str) -> str:
        p = ""
        f = open(path, "r", encoding="utf-8")
        for line in f:
            p = p + line

        f.close()
        return p

    def has_biao_dian(self, string: str) -> bool:
        biao_dian_list: List[str] = ["’", "‘", "”", "“", "，", "。", "；", "：", "？", "【", "】", "、", "·", "`", "\t",
                                     "）", "（", "《", "》", "<", ">", "+", "-", "*", "/", "=", "——", "…"]
        for one in biao_dian_list:
            if one in string:
                return True
            else:
                pass

    def has_number(self, string: str) -> bool:
        number_list: List[str] = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

        for one in number_list:
            if one in string:
                return True
            else:
                pass

    def jieba_start(self, path: str, save_path: str = None, save_to_csv=True) -> Dict[str, int]:
        fin = np.array([])
        words: List[str] = jb.lcut(self.read_file(path), cut_all=True)
        npa = np.array(words)

        for index in range(len(npa)):
            cell: str = npa[index]
            if len(cell) == 1 or self.has_biao_dian(cell) or self.has_number(cell) or cell == "":
                pass
            else:
                x = npa[index]
                fin = np.append(fin, x)

        # result = pd.value_counts(fin)

        # print(pd.DataFrame(result).head())

        p: DataFrame = pd.DataFrame({'name': fin})
        print(p.head(10))
        p['score'] = 1
        print(p.head(10))

        p: DataFrame = p.groupby("name")['score'].sum().reset_index()
        if save_to_csv:
            p.to_csv(save_path, index=False)
        else:
            pass

        final_dict = p.set_index(['name'])['score'].to_dict()
        return final_dict
