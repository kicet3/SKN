{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Series 생성"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0    NVDA\n",
      "1    MSFT\n",
      "2    AAPL\n",
      "3    GOOG\n",
      "4    TSLA\n",
      "Name: 미국 주식, dtype: object\n"
     ]
    }
   ],
   "source": [
    "stocks = ['NVDA','MSFT','AAPL','GOOG','TSLA']\n",
    "stocks_ser = pd.Series(stocks)\n",
    "stocks_ser.name = '미국 주식'\n",
    "print(stocks_ser)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "a   -1.689384\n",
      "b   -1.584735\n",
      "c   -0.544513\n",
      "d   -0.659866\n",
      "e    0.875222\n",
      "dtype: float64\n",
      "-0.5445132762994761 -0.5445132762994761\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "/var/folders/9s/h365kc_s4rnb9jvnmgth1cq40000gn/T/ipykernel_62999/3079987366.py:3: FutureWarning: Series.__getitem__ treating keys as positions is deprecated. In a future version, integer keys will always be treated as labels (consistent with DataFrame behavior). To access a value by position, use `ser.iloc[pos]`\n",
      "  print(nums_ser[2],nums_ser['c'])\n"
     ]
    }
   ],
   "source": [
    "nums_ser = pd.Series(np.random.randn(5),index=['a','b','c','d','e'])\n",
    "print(nums_ser)\n",
    "print(nums_ser[2],nums_ser['c'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "a    10\n",
      "b    20\n",
      "c    30\n",
      "dtype: int64\n"
     ]
    }
   ],
   "source": [
    "info = {\n",
    "    'a':10,\n",
    "    'b':20,\n",
    "    'c':30\n",
    "}\n",
    "\n",
    "info_ser = pd.Series(info)\n",
    "print(info_ser)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "---"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Series 속성"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "movies = ['말 할수 없는 비밀','뷰티인사이드','아이언맨','모르겠다.','진짜 모르겠다.']\n",
    "movies_ser = pd.Series(movies)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['말 할수 없는 비밀', '뷰티인사이드', '아이언맨', '모르겠다.', '진짜 모르겠다.'], dtype=object)"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "movies_ser.values\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<NumpyExtensionArray>\n",
       "['말 할수 없는 비밀', '뷰티인사이드', '아이언맨', '모르겠다.', '진짜 모르겠다.']\n",
       "Length: 5, dtype: object"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "movies_ser.array"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['1st', '2nd', '3rd', '4th', '5th'], dtype='object')"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# index를 별도 지정하지 않은 경우 기본적으로 숫자 인덱스\n",
    "movies_ser.index = ['1st','2nd','3rd','4th','5th']\n",
    "movies_ser.index # 라벨을 지정한 경우 라벨 인덱스"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "object\n",
      "(5,)\n",
      "1\n",
      "5\n"
     ]
    }
   ],
   "source": [
    "print(movies_ser.dtype)\n",
    "print(movies_ser.shape)\n",
    "print(movies_ser.ndim)\n",
    "print(movies_ser.size)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Series 메서드"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [],
   "source": [
    "nums_ser = pd.Series([2025,3,4,12,41])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2085\n",
      "11955600\n",
      "417.0\n"
     ]
    }
   ],
   "source": [
    "print(nums_ser.sum())\n",
    "print(nums_ser.product())\n",
    "print(nums_ser.mean())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0    2025\n",
      "1       3\n",
      "2       4\n",
      "3      12\n",
      "4      41\n",
      "dtype: int64\n",
      "0    2025\n",
      "1       3\n",
      "dtype: int64\n",
      "3    12\n",
      "4    41\n",
      "dtype: int64\n"
     ]
    }
   ],
   "source": [
    "print(nums_ser)\n",
    "print(nums_ser.head(2))\n",
    "print(nums_ser.tail(2))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.series.Series'>\n",
      "RangeIndex: 5 entries, 0 to 4\n",
      "Series name: None\n",
      "Non-Null Count  Dtype\n",
      "--------------  -----\n",
      "5 non-null      int64\n",
      "dtypes: int64(1)\n",
      "memory usage: 172.0 bytes\n"
     ]
    }
   ],
   "source": [
    "nums_ser.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "count       5.000000\n",
       "mean      417.000000\n",
       "std       899.031423\n",
       "min         3.000000\n",
       "25%         4.000000\n",
       "50%        12.000000\n",
       "75%        41.000000\n",
       "max      2025.000000\n",
       "dtype: float64"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "nums_ser.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "pandas.core.frame.DataFrame"
      ]
     },
     "execution_count": 33,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sp_500_df = pd.read_csv('./data/S_P500_Prices.csv')\n",
    "\n",
    "\n",
    "sp_500_ser = pd.Series(sp_500_df)\n",
    "type(sp_500_df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(2159,)\n",
      "0       1295.500000\n",
      "1       1289.089966\n",
      "2       1293.670044\n",
      "3       1308.040039\n",
      "4       1314.500000\n",
      "           ...     \n",
      "2154    3327.770020\n",
      "2155    3349.159912\n",
      "2156    3351.280029\n",
      "2157    3360.469971\n",
      "2158    3333.689941\n",
      "Name: sp500, Length: 2159, dtype: float64\n",
      "0       1295.500000\n",
      "1       1289.089966\n",
      "2       1293.670044\n",
      "3       1308.040039\n",
      "4       1314.500000\n",
      "           ...     \n",
      "2154    3327.770020\n",
      "2155    3349.159912\n",
      "2156    3351.280029\n",
      "2157    3360.469971\n",
      "2158    3333.689941\n",
      "Name: sp500, Length: 2159, dtype: float64\n"
     ]
    }
   ],
   "source": [
    "#형태, 요소의 개수 , 깊이\n",
    "print(sp_500_ser.shape)\n",
    "print(sp_500_ser)\n",
    "print(sp_500_ser)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "sp500    2159\n",
      "dtype: int64\n",
      "sp500    1278.040039\n",
      "dtype: float64\n",
      "sp500    2106.629883\n",
      "dtype: float64\n",
      "sp500    3386.149902\n",
      "dtype: float64\n",
      "sp500    2218.749554\n",
      "dtype: float64\n",
      "sp500    537.321727\n",
      "dtype: float64\n",
      "sp500    288714.638185\n",
      "dtype: float64\n"
     ]
    }
   ],
   "source": [
    "# 갯수, 최소값,중위값,최대값,평균값,표준편차값,분산값\n",
    "print(sp_500_df.count())\n",
    "print(sp_500_df.min())\n",
    "print(sp_500_df.median())\n",
    "print(sp_500_df.max())\n",
    "print(sp_500_df.mean())\n",
    "print(sp_500_df.std())\n",
    "print(sp_500_df.var())\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1416.51001\n",
      "1416.51001\n",
      "100    1315.130005\n",
      "101    1314.989990\n",
      "102    1325.660034\n",
      "103    1308.930054\n",
      "104    1324.180054\n",
      "          ...     \n",
      "196    1433.819946\n",
      "197    1413.109985\n",
      "198    1408.750000\n",
      "199    1412.969971\n",
      "200    1411.939941\n",
      "Name: sp500, Length: 101, dtype: float64\n",
      "100    1315.130005\n",
      "101    1314.989990\n",
      "102    1325.660034\n",
      "103    1308.930054\n",
      "104    1324.180054\n",
      "          ...     \n",
      "196    1433.819946\n",
      "197    1413.109985\n",
      "198    1408.750000\n",
      "199    1412.969971\n",
      "200    1411.939941\n",
      "Name: sp500, Length: 101, dtype: float64\n"
     ]
    }
   ],
   "source": [
    "# 인덱스 번호로 인덱스 및 슬라이싱 : 인덱스 50의 값 가져오기 , 인덱스 100~200의 값 가져오기\n",
    "print(sp_500_ser[50])\n",
    "print(sp_500_ser.iloc[50])\n",
    "\n",
    "print(sp_500_ser[100:201])\n",
    "print(sp_500_ser.iloc[100:201])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1000    2016.709961\n",
       "2000    3223.379883\n",
       "Name: sp500, dtype: float64"
      ]
     },
     "execution_count": 61,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#fancy  indexing 써보기\n",
    "sp_500_ser[[1000,2000]]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1885    3013.770020\n",
       "1886    3014.300049\n",
       "1887    3004.040039\n",
       "1892    3005.469971\n",
       "1893    3019.560059\n",
       "           ...     \n",
       "2154    3327.770020\n",
       "2155    3349.159912\n",
       "2156    3351.280029\n",
       "2157    3360.469971\n",
       "2158    3333.689941\n",
       "Name: sp500, Length: 160, dtype: float64"
      ]
     },
     "execution_count": 67,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#bollean indexing 써보기\n",
    "\n",
    "sp_500_ser.iloc[sp_500_ser.values > 3000]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n",
      "True\n",
      "True\n"
     ]
    }
   ],
   "source": [
    "print(3013.770020 in sp_500_ser.values) # 특정 값을 가지고 있는지에 대한 여부\n",
    "\n",
    "print(2000 in sp_500_ser)  # .values를 붙이지 않으면 기본 값은 index로 찾음\n",
    "print(2000 in sp_500_ser.index)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "97      1278.040039\n",
       "98      1278.180054\n",
       "99      1285.500000\n",
       "1       1289.089966\n",
       "2       1293.670044\n",
       "           ...     \n",
       "2038    3373.229980\n",
       "2034    3373.939941\n",
       "2033    3379.449951\n",
       "2035    3380.159912\n",
       "2037    3386.149902\n",
       "Name: sp500, Length: 2159, dtype: float64"
      ]
     },
     "execution_count": 70,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#정렬\n",
    "sp_500_ser = sp_500_ser.sort_values()\n",
    "sp_500_ser"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "pystudy_env",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
