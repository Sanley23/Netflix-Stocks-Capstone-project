{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Introduction\n",
    "\n",
    "In this project, you will act as a data visualization developer at Yahoo Finance! You will be helping the \"Netflix Stock Profile\" team visualize the Netflix stock data. In finance, a _stock profile_ is a series of studies, visualizations, and analyses that dive into different aspects a publicly traded company's data. \n",
    "\n",
    "For the purposes of the project, you will only visualize data for the year of 2017. Specifically, you will be in charge of creating the following visualizations:\n",
    "+ The distribution of the stock prices for the past year\n",
    "+ Netflix's earnings and revenue in the last four quarters\n",
    "+ The actual vs. estimated earnings per share for the four quarters in 2017\n",
    "+ A comparison of the Netflix Stock price vs the Dow Jones Industrial Average price in 2017 \n",
    "\n",
    "Note: We are using the Dow Jones Industrial Average to compare the Netflix stock to the larter stock market. Learn more about why the Dow Jones Industrial Average is a general reflection of the larger stock market [here](https://www.investopedia.com/terms/d/djia.asp).\n",
    "\n",
    "During this project, you will analyze, prepare, and plot data. Your visualizations will help the financial analysts asses the risk of the Netflix stock.\n",
    "\n",
    "After you complete your visualizations, you'll be creating a presentation to share the images with the rest of the Netflix Stock Profile team. Your slides should include:\n",
    "\n",
    "- A title slide\n",
    "- A list of your visualizations and your role in their creation for the \"Stock Profile\" team\n",
    "- A visualization of the distribution of the stock prices for Netflix in 2017\n",
    "- A visualization and a summary of Netflix stock and revenue for the past four quarters and a summary\n",
    "- A visualization and a brief summary of their earned versus actual earnings per share\n",
    "- A visualization of Netflix stock against the Dow Jones stock (to get a sense of the market) in 2017\n",
    "\n",
    "Financial Data Source: [Yahoo Finance](https://finance.yahoo.com/quote/DATA/)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 1\n",
    "\n",
    "Let's get our notebook ready for visualizing! Import the modules that you'll be using in this project:\n",
    "- `from matplotlib import pyplot as plt`\n",
    "- `import pandas as pd`\n",
    "- `import seaborn as sns`"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "from matplotlib import pyplot as plt\n",
    "import pandas as pd\n",
    "import seaborn as sns"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 2"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Let's load the datasets and inspect them."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Load **NFLX.csv** into a DataFrame called `netflix_stocks`. Then, quickly inspect the DataFrame using `print()`.\n",
    "\n",
    "Hint: Use the `pd.read_csv()`function).\n",
    "\n",
    "Note: In the Yahoo Data, `Adj Close` represents the adjusted close price adjusted for both dividends and splits. This means this is the true closing stock price for a given business day."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "         Date        Open        High         Low       Close   Adj Close  \\\n",
      "0  2017-01-01  124.959999  143.460007  124.309998  140.710007  140.710007   \n",
      "1  2017-02-01  141.199997  145.949997  139.050003  142.130005  142.130005   \n",
      "2  2017-03-01  142.839996  148.289993  138.259995  147.809998  147.809998   \n",
      "3  2017-04-01  146.699997  153.520004  138.660004  152.199997  152.199997   \n",
      "4  2017-05-01  151.910004  164.750000  151.610001  163.070007  163.070007   \n",
      "\n",
      "      Volume  \n",
      "0  181772200  \n",
      "1   91432000  \n",
      "2  110692700  \n",
      "3  149769200  \n",
      "4  116795800  \n"
     ]
    }
   ],
   "source": [
    "netflix_stocks = pd.read_csv('NFLX.csv')\n",
    "\n",
    "print(netflix_stocks.head())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Load **DJI.csv** into a DataFrame called `dowjones_stocks`. Then, quickly inspect the DataFrame using `print()`.\n",
    "\n",
    "Note: You can learn more about why the Dow Jones Industrial Average is a industry reflection of the larger stock market [here](https://www.investopedia.com/terms/d/djia.asp). \n"
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
      "          Date          Open          High           Low         Close  \\\n",
      "0   2017-01-01  19872.859375  20125.580078  19677.939453  19864.089844   \n",
      "1   2017-02-01  19923.810547  20851.330078  19831.089844  20812.240234   \n",
      "2   2017-03-01  20957.289063  21169.109375  20412.800781  20663.220703   \n",
      "3   2017-04-01  20665.169922  21070.900391  20379.550781  20940.509766   \n",
      "4   2017-05-01  20962.730469  21112.320313  20553.449219  21008.650391   \n",
      "5   2017-06-01  21030.550781  21535.029297  20994.220703  21349.630859   \n",
      "6   2017-07-01  21392.300781  21929.800781  21279.300781  21891.119141   \n",
      "7   2017-08-01  21961.419922  22179.109375  21600.339844  21948.099609   \n",
      "8   2017-09-01  21981.769531  22419.509766  21709.630859  22405.089844   \n",
      "9   2017-10-01  22423.470703  23485.250000  22416.000000  23377.240234   \n",
      "10  2017-11-01  23442.900391  24327.820313  23242.750000  24272.349609   \n",
      "11  2017-12-01  24305.400391  24876.070313  23921.900391  24719.220703   \n",
      "\n",
      "       Adj Close      Volume  \n",
      "0   19864.089844  6482450000  \n",
      "1   20812.240234  6185580000  \n",
      "2   20663.220703  6941970000  \n",
      "3   20940.509766  5392630000  \n",
      "4   21008.650391  6613570000  \n",
      "5   21349.630859  7214590000  \n",
      "6   21891.119141  5569720000  \n",
      "7   21948.099609  6150060000  \n",
      "8   22405.089844  6342130000  \n",
      "9   23377.240234  7302910000  \n",
      "10  24272.349609  7335640000  \n",
      "11  24719.220703  6589890000  \n"
     ]
    }
   ],
   "source": [
    "dowjones_stocks = pd.read_csv('DJI.csv')\n",
    "print(dowjones_stocks)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Load **NFLX_daily_by_quarter.csv** into a DataFrame called `netflix_stocks_quarterly`. Then, quickly inspect the DataFrame using `print()`.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "         Date        Open        High         Low       Close   Adj Close  \\\n",
      "0  2017-01-03  124.959999  128.190002  124.309998  127.489998  127.489998   \n",
      "1  2017-01-04  127.489998  130.169998  126.550003  129.410004  129.410004   \n",
      "2  2017-01-05  129.220001  132.750000  128.899994  131.809998  131.809998   \n",
      "3  2017-01-06  132.080002  133.880005  129.809998  131.070007  131.070007   \n",
      "4  2017-01-09  131.479996  131.990005  129.889999  130.949997  130.949997   \n",
      "\n",
      "     Volume Quarter  \n",
      "0   9437900      Q1  \n",
      "1   7843600      Q1  \n",
      "2  10185500      Q1  \n",
      "3  10657900      Q1  \n",
      "4   5766900      Q1  \n"
     ]
    }
   ],
   "source": [
    "netflix_stocks_quarterly = pd.read_csv('NFLX_daily_by_quarter.csv')\n",
    "print(netflix_stocks_quarterly.head())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 3"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Let's learn more about our data. The datasets are large and it may be easier to view the entire dataset locally on your computer. Open the CSV files directly from the folder you downloaded for this project.\n",
    " - `NFLX` is the stock ticker symbol for Netflix and `^DJI` is the stock ticker symbol for the Dow Jones industrial Average, which is why the CSV files are named accordingly\n",
    " - In the Yahoo Data, `Adj Close` is documented as adjusted close price adjusted for both dividends and splits.\n",
    " - You can learn more about why the Dow Jones Industrial Average is a industry reflection of the larger stock market [here](https://www.investopedia.com/terms/d/djia.asp). \n",
    " \n",
    "Answer the following questions by inspecting the data in the **NFLX.csv**,**DJI.csv**, and **NFLX_daily_by_quarter.csv** in your computer."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "What year is represented in the data? Look out for the latest and earliest date."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2017"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "2017"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "+ Is the data represented by days, weeks, or months? \n",
    "+ In which ways are the files different? \n",
    "+ What's different about the columns for `netflix_stocks` versus `netflix_stocks_quarterly`?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "#In netflix_stocks the data is represented Monthly, in netflix_stocks_quarterly de data is for every working day in 2017,\n",
    "#and also there is mentioned the quarter those dates represent over the year"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 4\n",
    "\n",
    "Great! Now that we have spent sometime looking at the data, let's look at the column names of the DataFrame `netflix_stocks` using `.head()`. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "         Date        Open        High         Low       Close   Adj Close  \\\n",
      "0  2017-01-01  124.959999  143.460007  124.309998  140.710007  140.710007   \n",
      "1  2017-02-01  141.199997  145.949997  139.050003  142.130005  142.130005   \n",
      "2  2017-03-01  142.839996  148.289993  138.259995  147.809998  147.809998   \n",
      "3  2017-04-01  146.699997  153.520004  138.660004  152.199997  152.199997   \n",
      "4  2017-05-01  151.910004  164.750000  151.610001  163.070007  163.070007   \n",
      "\n",
      "      Volume  \n",
      "0  181772200  \n",
      "1   91432000  \n",
      "2  110692700  \n",
      "3  149769200  \n",
      "4  116795800  \n"
     ]
    }
   ],
   "source": [
    "print(netflix_stocks.head())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "What do you notice? The first two column names are one word each, and the only one that is not is `Adj Close`! \n",
    "\n",
    "The term `Adj Close` is a confusing term if you don't read the Yahoo Documentation. In Yahoo, `Adj Close` is documented as adjusted close price adjusted for both dividends and splits.\n",
    "\n",
    "This means this is the column with the true closing price, so these data are very important.\n",
    "\n",
    "Use Pandas to change the name of of the column to `Adj Close` to `Price` so that it is easier to work with the data. Remember to use `inplace=True`.\n",
    "\n",
    "Do this for the Dow Jones and Netflix Quarterly pandas dataframes as well.\n",
    "Hint: Use [`.rename()`](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.rename.html)).\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [],
   "source": [
    "netflix_stocks.rename(columns = {'Adj Close': 'Price'}, inplace = True)\n",
    "netflix_stocks_quarterly.rename(columns = {'Adj Close': 'Price'}, inplace = True)\n",
    "dowjones_stocks.rename(columns = {'Adj Close': 'Price'}, inplace = True)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Run `netflix_stocks.head()` again to check your column name has changed."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "         Date        Open        High         Low       Close       Price  \\\n",
      "0  2017-01-01  124.959999  143.460007  124.309998  140.710007  140.710007   \n",
      "1  2017-02-01  141.199997  145.949997  139.050003  142.130005  142.130005   \n",
      "2  2017-03-01  142.839996  148.289993  138.259995  147.809998  147.809998   \n",
      "3  2017-04-01  146.699997  153.520004  138.660004  152.199997  152.199997   \n",
      "4  2017-05-01  151.910004  164.750000  151.610001  163.070007  163.070007   \n",
      "\n",
      "      Volume  \n",
      "0  181772200  \n",
      "1   91432000  \n",
      "2  110692700  \n",
      "3  149769200  \n",
      "4  116795800  \n"
     ]
    }
   ],
   "source": [
    "print(netflix_stocks.head())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Call `.head()` on the DataFrame `dowjones_stocks` and `netflix_stocks_quarterly`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "         Date          Open          High           Low         Close  \\\n",
      "0  2017-01-01  19872.859375  20125.580078  19677.939453  19864.089844   \n",
      "1  2017-02-01  19923.810547  20851.330078  19831.089844  20812.240234   \n",
      "2  2017-03-01  20957.289063  21169.109375  20412.800781  20663.220703   \n",
      "3  2017-04-01  20665.169922  21070.900391  20379.550781  20940.509766   \n",
      "4  2017-05-01  20962.730469  21112.320313  20553.449219  21008.650391   \n",
      "\n",
      "          Price      Volume  \n",
      "0  19864.089844  6482450000  \n",
      "1  20812.240234  6185580000  \n",
      "2  20663.220703  6941970000  \n",
      "3  20940.509766  5392630000  \n",
      "4  21008.650391  6613570000  \n",
      "         Date        Open        High         Low       Close       Price  \\\n",
      "0  2017-01-03  124.959999  128.190002  124.309998  127.489998  127.489998   \n",
      "1  2017-01-04  127.489998  130.169998  126.550003  129.410004  129.410004   \n",
      "2  2017-01-05  129.220001  132.750000  128.899994  131.809998  131.809998   \n",
      "3  2017-01-06  132.080002  133.880005  129.809998  131.070007  131.070007   \n",
      "4  2017-01-09  131.479996  131.990005  129.889999  130.949997  130.949997   \n",
      "\n",
      "     Volume Quarter  \n",
      "0   9437900      Q1  \n",
      "1   7843600      Q1  \n",
      "2  10185500      Q1  \n",
      "3  10657900      Q1  \n",
      "4   5766900      Q1  \n"
     ]
    }
   ],
   "source": [
    "print(dowjones_stocks.head())\n",
    "print(netflix_stocks_quarterly.head())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 5\n",
    "\n",
    "In this step, we will be visualizing the Netflix quarterly data! \n",
    "\n",
    "We want to get an understanding of the distribution of the Netflix quarterly stock prices for 2017. Specifically, we want to see in which quarter stock prices flucutated the most. We can accomplish this using a violin plot with four violins, one for each business quarter!\n",
    "\n",
    "\n",
    "1. Start by creating a variable `ax` and setting it equal to `sns.violinplot()`. This will instantiate a figure and give us access to the axes through the variable name `ax`.\n",
    "2. Use `sns.violinplot()` and pass in the following arguments:\n",
    "+ The `Quarter` column as the `x` values\n",
    "+ The `Price` column as your `y` values\n",
    "+ The `netflix_stocks_quarterly` dataframe as your `data`\n",
    "3. Improve the readability of the chart by adding a title of the plot. Add `\"Distribution of 2017 Netflix Stock Prices by Quarter\"` by using `ax.set_title()`\n",
    "4. Change your `ylabel` to \"Closing Stock Price\"\n",
    "5. Change your `xlabel` to \"Business Quarters in 2017\"\n",
    "6. Be sure to show your plot!\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "ax = sns.violinplot(x = netflix_stocks_quarterly['Quarter'], y = netflix_stocks_quarterly['Price'], data = netflix_stocks_quarterly)\n",
    "\n",
    "sns.set_palette('Accent')\n",
    "sns.set_style('darkgrid')\n",
    "\n",
    "plt.title('Distribution of 2017 Netflix Stock Prices by Quarter')\n",
    "plt.xlabel('Business quarters in 2017')\n",
    "plt.ylabel('Closing Stock Price')\n",
    "\n",
    "plt.savefig('Step 5.jpg')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Graph Literacy\n",
    "- What are your first impressions looking at the visualized data?\n",
    "\n",
    "- In what range(s) did most of the prices fall throughout the year?\n",
    "\n",
    "- What were the highest and lowest prices? "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    " "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    " "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 6\n",
    "\n",
    "Next, we will chart the performance of the earnings per share (EPS) by graphing the estimate Yahoo projected for the Quarter compared to the actual earnings for that quarters. We will accomplish this using a scatter chart. \n",
    "\n",
    "1. Plot the actual EPS by using `x_positions` and `earnings_actual` with the `plt.scatter()` function. Assign `red` as the color.\n",
    "2. Plot the actual EPS by using `x_positions` and `earnings_estimate` with the `plt.scatter()` function. Assign `blue` as the color\n",
    "\n",
    "3. Often, estimates and actual EPS are the same. To account for this, be sure to set your transparency  `alpha=0.5` to allow for visibility pf overlapping datapoint.\n",
    "4. Add a legend by using `plt.legend()` and passing in a list with two strings `[\"Actual\", \"Estimate\"]`\n",
    "\n",
    "5. Change the `x_ticks` label to reflect each quarter by using `plt.xticks(x_positions, chart_labels)`\n",
    "6. Assing \"`\"Earnings Per Share in Cents\"` as the title of your plot.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "x_positions = [1, 2, 3, 4]\n",
    "chart_labels = [\"1Q2017\",\"2Q2017\",\"3Q2017\",\"4Q2017\"]\n",
    "earnings_actual =[.4, .15,.29,.41]\n",
    "earnings_estimate = [.37,.15,.32,.41 ]\n",
    "\n",
    "ax2 = plt.subplot()\n",
    "\n",
    "plt.scatter(x_positions, earnings_actual, color='red', alpha = 0.5)\n",
    "plt.scatter(x_positions, earnings_estimate, color='blue', alpha = 0.5)\n",
    "plt.legend(['Actual', 'Estimate'])\n",
    "plt.xticks(x_positions,chart_labels)\n",
    "\n",
    "plt.title('Earnings Per Share in Cents')\n",
    "\n",
    "plt.savefig('Step 6.jpg')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "collapsed": true
   },
   "source": [
    "## Graph Literacy\n",
    "\n",
    "+ What do the purple dots tell us about the actual and estimate earnings per share in this graph? Hint: In color theory red and blue mix to make purple.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    " "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    " "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 7"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Next, we will visualize the earnings and revenue reported by Netflix by mapping two bars side-by-side. We have visualized a similar chart in the second Matplotlib lesson [Exercise 4](https://www.codecademy.com/courses/learn-matplotlib/lessons/matplotlib-ii/exercises/side-by-side-bars).\n",
    "\n",
    "As you may recall, plotting side-by-side bars in Matplotlib requires computing the width of each bar before hand. We have pasted the starter code for that exercise below. \n",
    "\n",
    "1. Fill in the `n`, `t`, `d`, `w` values for the revenue bars\n",
    "2. Plot the revenue bars by calling `plt.bar()` with the newly computed `x_values` and the `revenue_by_quarter` data\n",
    "3. Fill in the `n`, `t`, `d`, `w` values for the earnings bars\n",
    "4. Plot the revenue bars by calling `plt.bar()` with the newly computed `x_values` and the `earnings_by_quarter` data\n",
    "5. Create a legend for your bar chart with the `labels` provided\n",
    "6. Add a descriptive title for your chart with `plt.title()`\n",
    "7. Add labels to each quarter by assigning the position of the ticks through the code provided. Hint:  `plt.xticks(middle_x, quarter_labels)`\n",
    "8. Be sure to show your plot!\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# The metrics below are in billions of dollars\n",
    "revenue_by_quarter = [2.79, 2.98,3.29,3.7]\n",
    "earnings_by_quarter = [.0656,.12959,.18552,.29012]\n",
    "quarter_labels = [\"2Q2017\",\"3Q2017\",\"4Q2017\", \"1Q2018\"]\n",
    "\n",
    "# Revenue\n",
    "n = 1  # This is our first dataset (out of 2)\n",
    "t = 2 # Number of dataset\n",
    "d = len(earnings_by_quarter) # Number of sets of bars\n",
    "w = 0.8 # Width of each bar\n",
    "bars1_x = [t*element + w*n for element\n",
    "             in range(d)]\n",
    "\n",
    "plt.bar(bars1_x, revenue_by_quarter)\n",
    "\n",
    "# Earnings\n",
    "n = 2  # This is our second dataset (out of 2)\n",
    "t = 2 # Number of dataset\n",
    "d = len(earnings_by_quarter) # Number of sets of bars\n",
    "w = 0.8 # Width of each bar\n",
    "bars2_x = [t*element + w*n for element\n",
    "             in range(d)]\n",
    "\n",
    "middle_x = [ (a + b) / 2.0 for a, b in zip(bars1_x, bars2_x)]\n",
    "labels = [\"Revenue\", \"Earnings\"]\n",
    "\n",
    "plt.bar(bars2_x, earnings_by_quarter)\n",
    "\n",
    "plt.legend(labels)\n",
    "plt.title('Revenue vs Earnings by quarter')\n",
    "plt.xticks(middle_x, quarter_labels)\n",
    "\n",
    "plt.savefig('Step 7.jpg')\n",
    "plt.show()\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Graph Literacy\n",
    "What are your first impressions looking at the visualized data?\n",
    "\n",
    "- Does Revenue follow a trend?\n",
    "- Do Earnings follow a trend?\n",
    "- Roughly, what percentage of the revenue constitutes earnings?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Both Revenue and Earnings follow the same trend of growing steadely each quarter. \n",
    "#The revenue constitutes about 10 % of the earnings, roughly."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 8\n",
    "\n",
    "In this last step, we will compare Netflix stock to the Dow Jones Industrial Average in 2017. We will accomplish this by plotting two line charts side by side in one figure. \n",
    "\n",
    "Since `Price` which is the most relevant data is in the Y axis, let's map our subplots to align vertically side by side.\n",
    "- We have set up the code for you on line 1 in the cell below. Complete the figure by passing the following arguments to `plt.subplots()` for the first plot, and tweaking the third argument for the second plot\n",
    "    - `1`-- the number of rows for the subplots\n",
    "    - `2` -- the number of columns for the subplots\n",
    "    - `1` -- the subplot you are modifying\n",
    "\n",
    "- Chart the Netflix Stock Prices in the left-hand subplot. Using your data frame, access the `Date` and `Price` charts as the x and y axes respectively. Hint: (`netflix_stocks['Date'], netflix_stocks['Price']`)\n",
    "- Assign \"Netflix\" as a title to this subplot. Hint: `ax1.set_title()`\n",
    "- For each subplot, `set_xlabel` to `\"Date\"` and `set_ylabel` to `\"Stock Price\"`\n",
    "- Chart the Dow Jones Stock Prices in the left-hand subplot. Using your data frame, access the `Date` and `Price` charts as the x and y axes respectively. Hint: (`dowjones_stocks['Date'], dowjones_stocks['Price']`)\n",
    "- Assign \"Dow Jones\" as a title to this subplot. Hint: `plt.set_title()`\n",
    "- There is some crowding in the Y axis labels, add some space by calling `plt.subplots_adjust(wspace=.5)`\n",
    "- Be sure to `.show()` your plots.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAmEAAAH5CAYAAADJKOn4AAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADh0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uMy4xLjMsIGh0dHA6Ly9tYXRwbG90bGliLm9yZy+AADFEAAAgAElEQVR4nOzde1xUdf4/8Nc5Z25cBhFBS5Eu5t1M8VZJVvYtrbRSjIii0twSXU1p28xLbVu4lam1+nNd3UpX3ZTCLbts5ZpZooFhiRewUtvETGUAhRHmds7vj5FJFGQGZubM5fX8pzh85nPe8MjTy8/ncz4fQVEUBURERETkV6LaBRARERGFI4YwIiIiIhUwhBERERGpgCGMiIiISAUMYUREREQqYAgjIiIiUgFDGHmkrKwM3bt3xzvvvNPg+htvvIGZM2de9LPvvPMO1q5dCwCoqalBeno67rzzTrz11lvo378/AODtt9/G8uXLfVM8EVErlZWVoWfPnrj77rtx9913Y/To0UhPT8fHH3/s83tnZmbik08+8fl9yH80ahdAwUcURbz88ssYMGAArrzySrc/V1RUhK5duwIASkpKYDKZsGnTJpSVleGvf/0rAOD+++/3Sc1ERN5iMBjw/vvvu74+evQoHnnkEUiShBEjRqhYGQUbjoSRxwwGA8aPH48//OEPsFqtDb5ntVoxb948jBkzBnfddRdmzpyJmpoabNq0CZ9//jlWrlyJVatWYdasWTh+/DjuvvtuWCwW1+cXL16MP//5zygvL0dKSgq2bt0KAHjttdcwfvx4yLLs15+ViKg5nTp1wrRp0/DGG28AAKqrq/GHP/wBo0aNwujRo/HKK6/AbrcjJycHr732GgDgxIkT6N69O77++msAwPvvv4/p06e7fc9vvvkGaWlpGD16NMaOHYsvv/wSALBhwwZkZWVhypQpGDVqFMaNG4eDBw+66po5cybGjh2L0aNHY968ebDb7QCAv/71r66+Hn30UZw4ccJrvx9qGkMYtUhWVhYiIyOxaNGiBteXL18OSZKwYcMGbNy4Ee3bt8err76KW2+9FcOHD8cjjzyChx9+GC+++CKSkpLw/vvvQ6/XX9B/fHw8XnrpJcydOxebNm3Ce++9hwULFkAU+Z8sEQWeHj164PvvvwcAvPjii4iNjcUHH3yAvLw8HDhwAG+++SZuu+02V1j66quvkJCQgO3btwMAPv/8c9x2221u3auyshLTpk3D7Nmz8cEHH+Dll1/GU089hSNHjgAAdu7ciblz5+LDDz/ENddc41riMW/ePPTu3RsbNmzAe++9h8rKSrz11ls4duwYVq1ahby8PGzYsAFDhw5FcXGxt39F1AhOR1KLiKKI+fPn45577kFKSorr+hdffIHq6mrXg8Vms6Fdu3YtukdKSgruuOMOTJ06FWvWrEFcXJxXaici8jZBEGAwGAAAX375Jd5++20IggCdTof09HSsWrUKEydOxPHjx1FeXo6vvvoKWVlZ2LBhA37/+99j586dmDdvnlv3Ki4uRlJSEq655hoAQNeuXZGcnIzCwkIIgoDevXvjkksuAQD06tULmzZtAuB8Pu/ZswfvvvsuAKCurg4A0KFDB/To0QNjxozBsGHDMGzYMFx33XVe/f1Q4xjCqMUuvfRSPP/883j66adxzz33AABkWcasWbNw4403AgDMZnOD6UZPKIqCgwcPIj4+Ht999x0GDhzotdqJiLxpz5496NatGwDnc1AQBNf3ZFmG3W6HKIq46aabsHXrVhQXF+OVV17B3//+d3zyySfo378/oqKiGvR5/PhxHDp0yBWIFEWBRqOBw+Fo0H/99+x2O7RarSsMAs5wWH9EtCzLeP3119GlSxcAwOnTpyEIAkRRxJo1a7Bnzx7s2LED8+bNww033IA//vGP3v9FUQOc26FWGTlyJIYNG4ZVq1YBcI5erV27FlarFbIsY+7cuVi4cCEAQJIk1/oDd6xcuRJnzpxBXl4eVq5cyeFxIgpIhw8fxtKlSzFhwgQAzufgmjVroCgKrFYrcnNzcf311wMAbrvtNvzjH/9At27doNPpcO2112LhwoWNTkUeOXIEc+fOhc1mQ01NDX766SckJSWhX79+OHTokOuZ+MMPP2Dnzp0YPHjwRetMSUnBypUrXXVlZWVhzZo1KC0txahRo9ClSxc8/vjjeOSRR7Bnzx4v/5aoMRwJo1abM2cOioqKAACTJ0/Gyy+/jDFjxsDhcKBnz56urSuGDRuGl156CQDQr1+/i/a5f/9+LFu2DO+++y46dOiAWbNm4cknn8S///1vREdH+/YHIiK6iLq6Otx9990AnEsz9Ho9srOzcdNNNwFwPhNffPFFjB49GjabDTfccAMmTZoEALjuuutw4sQJ15vgKSkp+PjjjzF8+PAL7jNw4EDcfPPNuOuuu2Cz2ZCenu4abXv99dfxwgsvoK6uDoIg4C9/+QuuuOIKfPvtt03WPXv2bOTk5Ljquv766zFx4kRotVrcfvvtSE1NRWRkJAwGA+bMmePNXxk1QVDqxymJiIiIyG84HUlERESkAoYwIiIiIhUwhBERERGpgCGMiIiISAUMYUREREQqCLotKmRZhsPR/AudkiS41c4d3uor0PrxZl+syb/9eLMvd/vRaqVW34vU4+9nZzD/t+7PvkK5plD+2Tzp62LPzqALYQ6HgqqqM822i42NdKudO7zVV6D1482+WJN/+/FmX+72k5BgbPW9SD3+fnYG83/r/uwrlGsK5Z/Nk74u9uzkdCQRERGRChjCiIiIiFTAEEZERESkAoYwIiIiIhUwhBERERGpgCGMiIiISAUMYUREREQqYAgjIiIiUgFDGBEREZEKGMKIiIiIVMAQRkRERKQChjAiIiIiFTCEEREREamAIYyIiIhIBQxhRH6gz8tFXHJvaPRaxCX3hj4vV+2SiIioBfLyNEhOjoJeLyI5OQp5eZoW99XyTxKRW/R5uTBmT4VQWwsAkMqOwJg9FQBgSU1TszQiIvJAXp4G2dkG1NYKAICyMgHZ2QYAdUhNtXvcH0fCiHwsKud5VwCrJ9TWIirneZUqIiKilsjJ0bsCWL3aWgE5OfoW9ccQRuRj4tGypq87HH6uhoiIWuroUcGj681hCCPyMblTYqPXBUVBXL+eiJr7DDTf7QIUxc+VERGRJzp1avw53dT15jCEEfmYefZzUCIiGlxTIiJwZuLjsCcPRMRbK9D2tpvQ9voBiJz/F4iHDqpUKRERXcyjj1oBNAxcEREKZs+2tKg/hjAiH7OkpsH8xJMAAEUQ4EjsjOqFi2GeNx+nV/0Lpr0/oHrhYsiXXIrIV19Cu2v7I3bkzYhYvhTC8eMqV09ERPX27pWg1QKXXipDEBQkJspYuLBli/IBhjAiv5A7dgIA2Iv3omLXvgZvRSqxbVH34MM49e+PUPHtftQ89yJgtSF6zky0u6Y72tx7N/Tr1kKoPg2A210QEanh++9FbNigwaRJVuzebYbFImPXLnOLAxjALSqI/EJTWgJFrwe6dAFqrE22kzt2Qu2UaaidMg3SgVLoN+TCkPcuYqZlQfnjDNh69YF2bzEEq7MPbndBROQfr76qQ2QkMHmyzWt9ciSMyA80pfth79od0Lj/9x5H9x4488yzqNi5G5UfbULdAw9B+90uVwCrx+0uiIh8a/9+Ee+/r8HvfmdFu3bee4mKIYzID6TSEjh69GzZhwUB9kFDUPOXV5t8g7KpbTCIiKj1Xn1Vh6goICur6ZmMlmAII/Ix4VQVpF+Owt6jV6v7amq7i6auExFR6+zdK+LDD7V4/HEr2rb1bt8MYUQ+JpWWAgAcvVofwhrd7kKrhXn2c63um4iILjR/vg4xMQomTfLuKBjAEEbkc5qSfQDglZEwS2oaqhcuhiOxMxRBgGIwALIMe/cWTnUSEVGTdu8W8Z//aDFpkhVt2ni/f4YwIh/TlO6HHG302pShJTUNFbv2wW6xwbRrP+T4BMQ89ghgNnulfyIicpo/X4/YWAWPPeb9UTCAIYzI51yL8oWWnS12MUp8PKqXroB08EdEz/6j1/snIgpX334r4rPPNJg82YqYGN/cgyGMyJcUxbk9Rc/WT0U2xXbDjTgz/UlE/Gs19Bve8dl9iIjCySuv6BEXJ2PiRN+MggEMYUQ+JZw4AbGiouXbU7jpzFOzYBt8LaL/MB3i4UM+vRcRUajbuVPE5s0aTJ5sQ3S07+7DEEbkQ5rS/QC8syj/4jfS4PTf/gFIEmIeHw9Yffc3NyKiUPfKK3rEx8uYMMG3z1KGMCIf8lsIAyB3TkL1oiXQfvctoub92ef3IyIKRV9/LWHrVg1+/3urT0fBAIYwIp+SSksgxydASUjwy/2so+5C7SOPInLpX6Hb/Jlf7klEFErmz9chIUHGI49474zIpjCEEfmQpmSfTxflN6bm+Xmw9+wN49RJEI//6td7ExEFs/x8CV99pcG0aVZERvr+fgxhRL4iy9CUlsLu40X5F4iIwOkVKyGYzTBOfgyQZf/en4goCCkK8MorOnToIOOhh3w/CgYwhBH5jHjkZwhnzHD4YT3Y+RzduqNm3nzovvoCEYsX+f3+RETB5quvJOzYocH06VacdzqczzCEEfmIprQEAPw/EnZWXUYm6u4Zi6iXXoSmsECVGoiIgoGiAC+/rEfHjjIeeMA/o2AAQxiRz0hn34z09R5hTRIE1Lz6OuROnRGT9SiEU1Xq1EFEFOC++ELCzp0SnnjCCoPBf/dlCCPyEU3JfudB20YfnXfhBiWmDU7//Q2Ix36BccZU51/3iIjIxbkWTI/ERBkZGf4bBQMYwoh8RlNaotpU5LnsAwbB/Myz0H/4Pgz/fEvtcoiIAsrmzRKKiiTMmGGFXu/fezOEEfmCzQbphwNw9OytdiUAgNop02C9aTii586EVLJf7XKIiAJC/ShYUpKM9HT/joIBDGFEPiEdOgjBZguIkTAAgCji9JLlUIwxiHnsEeDMGbUrIiJS3WefSfjuOwnZ2RZotf6/P0MYkQ/487gidynt2+P0/1sOzYFSRM99Ru1yiIhUVf9G5OWXy7j3XrsqNTCEEfmAVLIfiijC0bWb2qU0YLtpOM5MnYGI1W9Bt/HfapdDRKSajz/WYO9eCU8+qc4oGMAQRuQTmtISOK7sAr++6+wm88w5sA0YCOPvJyGub3do9FrEJfeGPi9X7dKIiPxClp2743fpIiM1VZ1RMIAhjMgnpNL9quyU7xatFnV3p0Koq4X06zEIigKp7AiM2VMZxIgoLHz4oQYlJc5RMI1GvToYwoi8rbYW0uFDgbMovxGRy5dCOO+aUFuLqJznVamHiMhfHA5g/nwdunZ1YMwY9UbBAEDF/EcUmjQ/HICgKLD3DNCRMADi0TKPrhMRhYqNGzU4cEDC8uW1kCR1a+FIGJGXSfv3AUDA7BHWGLlTokfXiYhCQf0oWI8eDtx1l7qjYABDGJHXaUpLoOj1cFx+hdqlNMk8+zkoERENrikRETDPfk6lioiIfCcvT4Pk5ChERIj48UcJKSkOiAGQgAKgBKLQoindD3vX7lB1tWczLKlpqF642Hm2pSDAkdgZ1QsXw5KapnZpRERelZenQXa2AWVlInB2NezatVrk5an/jGYII/IyqbQEjgBelF/PkpqGil37YLfYULFrHwMYEYWknBw9amsbvopUWysgJ8fPB0U2giGMyIuEU1WQfjkaUDvlExGFs6NHz38X/OLX/YkhjMiLpNJSAICjZ+CPhBERhYNOnRSPrvsTQxiRFwXimZFEROFs9mwLDIaGgSsiQsHs2RaVKvoNQxiRF2lK90OONkJO7Kx2KUREBCA11Y5777UBAARBQWKijIUL61Q9rqie+q8GEIUQqWS/c1G+oP5aAyIicrJaBcTFyfjlFwWnT59RuxwXjoQReYuiOLenCOCd8omIwo2iAPn5Eq6/PjD2BjuXz8rZvXs3MjMzAQD79u3DuHHjkJGRgRdeeAGyLAMAlixZgnHjxiE9PR3FxcW+KoXIL4QTJyBWVATF9hREROHif/8TUFYmYuhQh9qlXMAn05ErVqzAxo0bEXF2R+65c+dizpw5SE5OxqJFi/DBBx/gqquuQmFhId555x0cO3YMU6dORV5eni/KIfILLsonIgo8+fnOqJOS4gCgVbeY8/hkJCwpKQmLFy92fX38+HEkJycDAJKTk1FUVISioiKkpKRAEAR07NgRDocDFRUVviiHyC8YwoiIAk9+voT4eBnduslql3IBn4yEjRgxAmVlZa6vO3fujMLCQgwePBhbtmxBbW0tampqEBsb62oTFRWF6upqxMXFXbRvSRIQGxvZbA2SJLrVzh3e6ivQ+vFmX6wJkA79ACUhAW26XhYwNfmzHyKiQFO/HmzoUEdAvi/ll7cj582bh5ycHPzjH//A1VdfDZ1Oh+joaJjNZlcbs9kMo9HYbF8Oh4KqqubfbIiNjXSrnTu81Veg9ePNvlgTEFtcDKV7T5y6SLtg/j0lJDT/55OIKJAcPizg2DERQ4da1S6lUX55T2Dr1q2YN28eli9fjqqqKgwdOhTJycnYtm0bZFnGL7/8AlmWmx0FIwpYsgyptJRvRhIRBZBt2+rXg6m/J1hj/DISdtlll+Gxxx5DREQEhgwZghtvvBEAMHDgQNx3332QZRnPPvusP0oh8gnxyM8QzTVwcD0YEVHAyM+X0KGDjC5d1D+iqDE+C2GJiYnIzc0FAAwfPhzDhw+/oM3UqVMxdepUX5VA5Dea0hIAgJ3bUxARBYT69WApKYG5HgzgZq1EXiGdfTOSe4QREQWGH38UceJEYO4PVo8hjMgLNCX74UjsDMUYo3YpREQEYNs2CQAwdGhgrgcDGMKIvEJTWsKpSCKiAJKfL6FjRxlXXBGY68EAhjCi1rPZIP34PRflExEFCEUBtm8P3P3B6jGEEbWSdPgQBKuVI2FERAHiwAER5eViwG5NUY8hjKiV6hfl23v2VrkSCjQ2mw1PPfUUMjIyMG7cOGzevNn1vQ8++AD33Xef6+vc3FyMHTsWaWlp2LJlCwCgoqICEyZMQEZGBqZPn47a2tom2xLRb/LznevBrr8+cBflA37aJ4wolGn274MiinB07aZ2KRRgNm7ciNjYWMyfPx+VlZUYM2YMbrnlFpSUlODdd9+FojjXqpw8eRKrV69GXl4eLBYLMjIyMHToUCxduhSjRo3C2LFjsXz5cqxfvx533nlno211Op3KPy1R4Ni2TULnzjIuuyxw14MBHAkjajVNaQkcV3YBDAa1S6EAM3LkSDzxxBOuryVJQmVlJV599VXMmjXLdb24uBj9+/eHTqeD0WhEUlISSktLUVRUhBtuuAEAMGzYMGzfvr3JtkTkJMvA9u2agN6aoh5HwohaSSrdD0evPmqXQQEoKioKAFBTU4Np06bhiSeewOzZszFr1izo9XpXu5qamgZn50ZFRaGmpqbB9aioKFRXVzfZtjmSJLh1UHsgHgzPmvzbV6D142lfu3cDlZUCbr1VuuAzgfb7Zggjao3aWkiHD8Ey9l61K6EAdezYMUyZMgUZGRm4/PLL8b///Q9/+tOfYLFY8OOPPyInJwfXXnstzGaz6zNmsxlGoxHR0dEwm80wGAwwm82IiYlxXTu/bXMcDsWtg9r9fTC8P/tiTcHZj6d9ffqpFoCE/v3PoKqq4XSkGjUlJDT955PTkUStoPnhAARF4cHd1Kjy8nJMmDABTz31FMaNG4e+ffvio48+wurVq7Fw4UJcddVVmD17Nvr27YuioiJYLBZUV1fj4MGD6NatG5KTk7F161YAwJdffokBAwY02ZaInLZtk3DZZTISEwN7PRjAkTCiVpFK6o8rYgijCy1btgynT5/G0qVLsXTpUgDAihUrYDhv/WBCQgIyMzORkZEBRVEwY8YM6PV6ZGVl4emnn0Zubi7atm2LBQsWIDIystG2RAQ4HMCOHRqMGmVTuxS3MIQRtYKmtASKXg/HFVeqXQoFoDlz5mDOnDmNfi8xMRG5ubmur9PS0pCWltagTXx8PN54440LPttYWyIC9u0TceqUEBSL8gFORxK1ilS6H/au3QEN/z5DRKS2386LZAgjCnmakv1wcKd8IqKAsH27BldeKePSSwN/PRjAEEbUYsKpKki/HIWd68GIiFRntwM7dkgYOjSwjyo6F0MYUQtJZzfIdPTkSBgRkdr27BFRXS0gJSU4piIBhjCiFtPUnxnJkTAiItVt2+Zcmxvo50WeiyGMqIU0pfshR0VDTuysdilERGEvP19Ct24OdOgQHOvBAIYwohaTSkuci/IFQe1SiIjCms0GFBRIQTUKBjCEEbWMokBTsg/2Xr3VroSIKOzt3i3CbA6u9WAAQxhRiwgnT0KsqOD2FEREASA/P/jWgwEMYUQtoinZB4CL8omIAsG2bRJ69nQgPj541oMBDGFELcI3I4mIAoPVCuzcKQXNLvnnYggjagGptARyfDyUhAS1SyEiCmvffivhzBkh6KYiAYYwohbRlO7nKBgRUQDIz5cgCAquvz54dsqvxxBG5ClZhlRaCjsX5RMRqS4/X0KvXjLi4tSuxHMMYUQeEsuOQDTXwMGRMCIiVVkszvVgwbY1RT2GMCIPuRbl92QIIyJS065dEurqhKA6tPtcDGFEHpJKnCGMe4QREalr2zbnerBrr+VIGFFY0JTshyOxMxRjjNqlEBGFtfx8CVdfLSM2Vu1KWoYhjMhDmtISLsonIlJZbS3wzTfBuT9YPYYwIk/YbJB+/J6L8omIVPbNNxKsVgEpKcG5HgxgCCPyiHT4EASrlSNhREQqy8+XIIrBux4MYAgj8oh09s1IB9+MJCJSVX6+hGuukWE0ql1JyzGEEXlAU7IfiijCflU3tUshIgpbZ844t6cI1q0p6jGEEXlAU1oCx5VdgIgItUshIgpbhYUSbDYhaDdprccQRuQBqWQfF+UTEaksP1+CRqNg8GCGMKLwUFsL6fAhLsonIlJZfr4G/frJiI5Wu5LWYQgjcpPmhwMQFIXHFRERqaimBvjuOzHo14MBDGFEbvvtuCKGMCIitRQWSrDbhaDepLUeQxiRmzSlJVB0OjiuuFLtUoiIwta2bRK02uBfDwYwhBG5TSrdD0fX7oBGo3YpRERhKz9fg+RkByIj1a6k9RjCiNzEMyOJiNRVXQ3s3i2GxFQkwBBG5J5TpyAdLYO9Z2+1KyEiCltffy1BlkNjPRjAEEbkFmHfXgCAoydHwoiI1LJtmwY6nYKBAxnCiMKGsG8fAMDONyOJiFSTny9h4EBHyBxawhBG5I59+yBHRUNO7Kx2JUREYenUKWDPntBZDwYwhBG5Rdi3F44ePQFBULsUIqKwtGOHBEUJnfVgAEMYUfMUBcLevdwpn4hIRfn5GhgMCgYMYAgjChvCyZMQTCbnSBgREali2zYJgwY5oNerXYn3MIRRwNDn5SIuuTc0ei3ikntDn5erdkkAAE2p87gibk9BRKQOkwnYt08KqalIAODW3xQQ9Hm5MGZPhVBbCwCQyo7AmD0VAGBJTVOztN9CGN+MJCJSxVdfOf8ZaiGMI2EUEKJynncFsHpCbS2icp5XqSInfV4uIue9AAVA2xE3BczoHBFRONm6VUBkpIL+/UMrhHEkjAKCeLTMo+v+EMijc0RE4eSLLwQMGuSATqd2Jd7FkTAKCHKnRI+u+0Ogjs4REYWT8nIB+/YJSEkJrVEwgCGMAoR59nNQ9IYG15SICJhnP6dSRYE5OkdEFE7y8jRISYkEAKxYoUVeXmhN4DGEUUCwpKbhTNYUAIACQNFoUL3gr6pO+wXi6BwRUbjIy9MgO9uAigpnVDlxQkR2tiGkghhDGAUMe5++AAD591Mh2O1wdLlK1XrMTz4N5bxrao/OERGFi5wcPWprG55SUlsrICcndDYKYwijgCGWlwMA5McnQTEYYFi3VtV6BEGAAMCR0B6KIMCR2BnVCxdzUT4RkR8cPdr4MXFNXQ9GDGEUMMQKk/NfrrwSljtGQf/vdwGLRbV6DGtWwd6tOyr2/gC7xYaKXfsYwIiI/KRTp/PnIi5+PRgxhFHAEE3lkGNjAa0Wdfc9ALGqCrrP/qNKLVJpCbTfFKLugYd5aDcRkQpmz7ZAo2kYuCIiFMyerd5fzr2NIYwChmAqhxzXDgBgG3YTHJd2VG1K0rD2n1C0WtTdm67K/YmIwl1qqh1JSTJ0OgWCoCAxUcbChXVITbWrXZrX+CyE7d69G5mZmQCAkpISpKWl4f7778czzzwDWZYBALm5uRg7dizS0tKwZcsWX5VCQUI0VUBpF+/8QpJguTcdus//C+H4cf8WYrHA8M7bsNw+Ckp8vH/vTUREAIC6OqCsTMTEiTZYLDJ27TKHVAADfBTCVqxYgTlz5sBydj3PkiVLMGXKFLz99tuwWq344osvcPLkSaxevRrr1q3DG2+8gYULF8JqtfqiHAoSoqkccrvfQk/dfRkQHA4Y/HxUkP4/H0KsqEDdgw/79b5ERPSb776TYLUKGDIk9DZpreeTEJaUlITFixe7vu7ZsyeqqqqgKArMZjM0Gg2Ki4vRv39/6HQ6GI1GJCUlobS01BflUJAQTOWQ27Vzfe3o2g22AYNgWL8WUPy3ENOw5p9wdE6CbdhNfrsnERE1VFgoAQAGDQrdEOaTHc9GjBiBsrLfdhW//PLL8ec//xl/+9vfYDQaMWTIEHzyyScwGo2uNlFRUaipqWm2b0kSEBsb6UY70a127vBWX4HWjzf7anU/igKxwgRdx0sgnNOXOGE8pCmTEXu4FEge4PuaDh+G9sstcDz3J8TGRbeuL2/V5OO+vFkTEZG3FBZKuOoqB+LjQ+dtyPP5ZdvZnJwcrF27Fl27dsXatWvx0ksvISUlBWaz2dXGbDY3CGVNcTgUVFWdabZdbGykW+3c4a2+Aq0fb/bV2n6E06cQb7OhNjoWeofs6ku4bRTa6WfAvuIN1Pylp89rilz2d2hEEVVj7oN8zmcD5ffki77c7Schofk/n0RE3iDLzhB25502tUvxKb+8HdmmTRtERztHFdq3b4/Tp0+jb9++KCoqgsViQXV1NQ4ePIhu3br5oxwKQEL9Rq1xcQ2uK3xcaOoAACAASURBVG1iYbn9Tug3vOP7PcPsdhjeXgvrLbdC7tjJt/ciIqIm/fCDiKqq0F4PBvhpJOzFF1/EjBkzoNFooNVq8cILLyAhIQGZmZnIyMiAoiiYMWMG9PrQOYqAPFO/UWtjbyPWpT8Aw3sboNv0Kayj7vJZDbrPN0H69RhqXlrgs3sQEVHzCgqc68EGD2YIa5HExETk5jrfahs4cCDWrVt3QZu0tDSkpXEHcgJEkzOE1e8Tdi7bjcPhuORSGNav9WkIM6z5J+SE9rDeOsJn9yAiouYVFEiIj5dxxRWhux4M4GatFCCEsyNh525R4SJJsIy7D7r/fgbhxAmf3F88/it0mz5BXfoDgFbrk3sQEZF7CgslDBniCPkDSxjCKCC4Du9uLIThnD3DNvhmzzD9urUQHA7UPZDpk/6JiMg9v/4q4H//E0N+KhJgCKMAIZrKoRgMQGTjWyU4uveALXkADG/7YM8wWUbE2n/COvQGOK68yrt9ExGRR+r3Bwv1RfkAQxgFCLHC5BwFu8jYc919D0BTsg+avcVevbd2+zZIPx1G3QMPebVfIiLyXGGhhIgIBVdfLatdis8xhFFAEM47sqgxlnvGQtHpoPfyod6GNasgt4mF5U7fLfonIiL3FBRISE52hMXyXIYwCgiiqRzKeXuEnU9pGwfLyDth2PAO4KVzRoXKCug/2gjLuDQgIsIrfRIRUcvU1AB794phMRUJMIRRgBBNpmZHwgDAkp4B0WSC7r+feeW+hnfXQ7BYUPvgI17pj4iIWm7XLgkOhxAWi/IBhjAKEILJBLmRjVrPZ73pFjjad4DBG1OSigLDmlWw9U+Go3ef1vdHREStUlAgQRAUDBzIEEbkHxYLxJpqKI1s1HoBjebsnmGfuo46ainNt0XQlOxH3QMPt6ofIiLyjsJCCb16yYiJUbsS/2AII9WJF9uotRF192VAsNtbvWeYYc0qKJGRsIxJbVU/RETUenY78M03UtisBwMYwigACM1s1Ho+R89esPXrD/26f7X8njXVMGx4F3V3j4ViDJO/chERBbD9+0WYzeGzHgxgCKMA4Dq8u50b05Fn1d33ALR7iyHtadmeYfr3/w3hjBl1D3IqkogoEITTJq31GMJIdaLJs5EwALCMSYWi1cKQ27LRMMOaVbB37wH7wMEt+jwREXlXQYGExEQZnTqF9qHd52III9W5Qpg7C/PPUuLawTriDhjycgGbzaP7SSX7oS3a6dwhP9RPhyUiCgKK4gxh4TQVCTCEUQAQTCYoogilbVuPPleXngGxvBy6zZs8+pxh7SooOh3q7r3fo88REZFvHDki4Ndfw+PQ7nNp1C6ASDSZnLvli579ncB68/9BTmgPw7q1sI68w70P1dXB8M46WO4Y5dEaNKKWsNlsmDVrFo4ePQqr1YqsrCxcdtllmDt3LhRFQY8ePTB37lxIkoTc3FysW7cOGo0GWVlZuPnmm1FRUYE//OEPqKurQ/v27fGXv/wFERERjbYlCmYFBc71YAxhRH4mmso9mop00WpRl5qGiDf+7hxNcyNU6f/zIcTKSu4NRn6xceNGxMbGYv78+aisrMSYMWPQq1cvZGdnY9CgQZg5cyY+//xz9OvXD6tXr0ZeXh4sFgsyMjIwdOhQLF26FKNGjcLYsWOxfPlyrF+/HnfeeWejbXU6ndo/LlGLFRRIMBoV9OwZ+od2n4vTkaQ6ocK9I4saU3dfBgSbDfp/v+NWe8OaVXAkXQbbDTe26H5Enhg5ciSeeOIJ19eSJGHx4sUYNGgQrFYrTp48iXbt2qG4uBj9+/eHTqeD0WhEUlISSktLUVRUhBtuuAEAMGzYMGzfvr3JtkTBbOdOCYMGOSBJalfiXxwJI9WJpnI4unZv0WcdvfvA1rcfDOv+hbqJky5+n8OHoPtqK8wz53g89UnUElFRUQCAmpoaTJs2DdOnT4ckSTh69CjGjx+P6OhoXHHFFThy5AiMRmODz9XU1KCmpsZ1PSoqCtXV1Q2undu2OZIkIDY20o12olvt/NWPN/tiTYHZT2UlUFIi4b775CbbB9rP5q2+GMJIdaKpHLYh17f483XpGTDO+iOkfXsvegak4e01UEQRdfc/2OJ7EXnq2LFjmDJlCjIyMjB69GgAQKdOnfDZZ5/hnXfewUsvvYTbbrsNZrPZ9Rmz2Qyj0Yjo6GiYzWYYDAaYzWbExMS4rp3ftjkOh4KqqjPNtouNjXSrnb/68WZfrCkw+/nvfyUAkbjmmjpUVTW+JizQfjZP+kpIaPrPJ4cDSF2yDKGiAnJ8yxfJW8bc69wzbP1F9gyz22F4ew2s/3cb5Es7tvheRJ4oLy/HhAkT8NRTT2HcuHEAgEmTJuGnn34C4BzFEkURffv2RVFRESwWC6qrq3Hw4EF069YNycnJ2Lp1KwDgyy+/xIABA5psSxSsCgslaDQK+vcPr0X5AEfCSGVCVSUEWYbSwjVhgHOnfeutI2HIy4V57vOAVntBG91/P4N0/FfUcEE++dGyZctw+vRpLF26FEuXLgUATJ8+HTNnzoRWq0VERARefPFFJCQkIDMzExkZGVAUBTNmzIBer0dWVhaefvpp5Obmom3btliwYAEiIyMbbUsUrAoKJPTtKyPSO7OEQYUhjFQlVlQA8Gyj1sbUpT8A/ccfQLflv7DedvsF3zesXQVH+w6w/t9trboPkSfmzJmDOXPmXHB93bp1F1xLS0tDWlpag2vx8fF444033GpLFIwsFuDbbyWMH+/ZptuhgtORpCpPD+9uivWWWyHHx8PQyKHe4rFfoNv0KSzpDzQ6SkZEROooLhZhsQhhdV7kuRjCSFX1Rxa1euNUrRZ1qfdB9+nHEM4eCF7PsP5fEGQZtRmZrbsHERF5Vf0mrYMGMYQR+Z14NjC1diQMOHfPsLzfLsoyDGv+CWvKMMhXdmn1PYiIyHsKCyVceaWM9u3D59DuczGEkapacnh3Uxx9roatT18Y1q91XdNu+xLSzz85D+smIqKAoSjOEBauU5EAQxipTDCVQ46KBgwGr/RnSc+A9rtvIZXsB+BckC/HxsJy511e6Z+IiLzjxx9FVFSE36Hd52III1WJJlOrtqc4X93YNCgajXPPMJMJ+o8+QN296V4LeURE5B3168GGDLGrXIl6GMJIVaKpvFUbtZ5PiY+HvVcfRCxbAs2lHSBYrZDbd/Ba/0RE5B2FhRLatZPRpUt4rgcDGMJIZYLJ5JX1YPX0ebnQlO6HIMsQzl6LWvgK9Hm5XrsHERG1XkGB89BuQWi+bahiCCNViRXenY6MynkegtXa4JpQW4uonOe9dg8iImqdEycEHD4shvWifIAhjFQmmsq9sj2Fq7+jZR5dJyIi/yssrF8PxhBGpI4zZyDU1np1OlLulOjRdSIi8r+CAgkGg4K+fWW1S1EVQxipxrVbfrz3RsLMs5+DEhHR4JoSEQHz7Oe8dg8iImqdwkIJ/fs7oNOpXYm6GMJINd7cqLWeJTUN1QsXw5HYGYogwJHYGdULF8OSysOOiYgCgdkM7NnD9WAAoFG7AApfguvIIu+FMMAZxCypaYiNjURV1Rmv9k1ERK3z7bcS7HYhrDdprceRMFKNWH52JMyLC/OJiCiwFRRIEAQFAwcyhDGEkWpEk3MkTPHySBgREQWuwkIJPXrIiI1VuxL1MYSRasQKExStFkpMG7VLISIiP3A4gJ07JU5FnsUQRqoRTOXORfnhvF0yEVEY2b9fRE2NwEX5ZzGEkWrE8nIoXnwzkoiIAhs3aW2IIYxUI1aYIHtxjzAiIgpshYUSLr1URmJi+B7afS6GMFKNYCr3+vYUREQUuAoKJAwZEt6Hdp+LIYxUI1aYOB1JRBQmysoE/PILN2k9F0MYqcNuh1hZyT3CiIjCREGBcz0Y34z8DUMYqUKoqADg3SOLiIgocBUUSIiOVtCzZ3gf2n0uhjBShXj2yCJvHt5NRESBq7BQwsCBDmh4YKILQxipwnV4N6cjiYhC3qlTQEmJyKnI8zCEkSqE+hDG6UgiopD3zTcSFIWbtJ6PIYxUUX9uJEfCiIhCX2GhBElSkJzMEHYuhjBSRf10pBIXp3IlRETkawUFEq6+WkZUlNqVBBa3QlhNTQ0OHDiAM2fO+LoeChOiqRxym1hAq1W7FCKP8HlI5BmrFdi1S+JUZCOafUfhk08+wbJly+BwODBy5EgIgoDJkyf7ozYKYUKFibvlU9Dh85DIc3v2iKirE7govxHNjoStXLkSubm5iI2NxeTJk/Hf//7XH3VRiBPLTVC4HoyCDJ+HRJ7jJq1NazaEiaIInU4HQRAgCAIiIiL8UReFOJEjYRSE+Dwk8lxhoYTLL5fRoQMP7T5fsyFs4MCByM7OxvHjx/Hss8/i6quv9kddFOKch3dzJIyCC5+HRJ5RFGcI4yhY45pdE5adnY0vv/wSvXr1QpcuXXDzzTf7oy4KZYoC0VTOw7sp6PB5SOSZQ4cElJeLGDLEqnYpAanZkbDPP/8c3377LSZOnIg1a9Zg27Zt/qiLQphQUw3BZuNIGAUdPg+JPFNY6FwPxjcjG9dsCFu8eDEefPBBAMBrr72GJUuW+LwoCm1Cef2RRRwJo+DC5yGRZwoKJLRtq+Cqq3hod2OaDWEajQbtzv7P0mg0QhS5vyu1jmujVoYwCjJ8HhJ5pqBAg8GDHeAflcY1uyasb9++ePLJJ9GvXz8UFxejV69e/qiLQphYwSOLKDjxeUjkvpMngYMHRWRk2NQuJWA1G8LmzJmDzZs349ChQ7j99tsxfPhwf9RFIUzguZEUpPg8JHLf9u3Of/LNyKY1OUC4ZcsWAEBubi5MJhPatGmDkydPYv369W51vHv3bmRmZgIAZsyYgczMTGRmZmL48OGYMWMGAGDJkiUYN24c0tPTUVxc3NqfhYKEWL8mjG9HUpBo7fOQKBxt3y5Ar1fQrx9DWFOaHAmrqqoCAJw8edLjTlesWIGNGze6NjJctGgRAODUqVN46KGH8Mwzz2Dfvn0oLCzEO++8g2PHjmHq1KnIy8tryc9AQUasMEExGMCTXClYtOZ5SBRu8vI0yMnRo6xMgE4HfPihBqmpdrXLCkhNhrAxY8YAAA4fPowFCxZ41GlSUhIWL16MP/7xjw2u179Z1L59e3zyySdISUmBIAjo2LEjHA4HKioqEBcX14Ifg4KJWL9RqyCoXQqRW1rzPCQKJ3l5GmRnG1Bb63y+W61AdrYBQB2DWCOaXRNms9lQWlqKK664AsLZ/2nqdLqLfmbEiBEoKytrcM1kMmHHjh145plnAAA1NTWIjY11fT8qKgrV1dXNhjBJEhAbG9lc2ZAk0a127vBWX4HWjzf78qQf6XQlhISEJtvz9+TfvrxZU6hryfOQKJzk5OhdAaxeba2AnBw9Q1gjmg1hhw4dwuTJkyEIAhRFgSAI2Lx5s8c3+uSTTzBq1ChIknPjtujoaJjNZtf3zWYzjEZjs/04HAqqqs402y42NtKtdu7wVl+B1o83+/Kkn9jjJ6DEtsWpJtrz9+TfvtztJyGh+T+foc5bz0OiUHX0aOMzHE1dD3fNhrAPP/zQKzfasWMHsrKyXF8nJydj/vz5ePTRR/Hrr79ClmVORYYJsbwctsuuULsMIo9563lIFKo6dVJQVnZh4OrUiYd3N6bJtyP/85//4MYbb8SIESO88ubi4cOH0blzZ9fXffr0wcCBA3Hfffdh6tSpePbZZ1t9DwoOQkUF5HhuT0HBw9vPQ6JQNXu2BaLYMHBFRCiYPduiUkWBrcmRsFWrVmHjxo04ffo0cnJysGzZMo86TkxMRG5uruvrjz766II2U6dOxdSpUz3ql4KcxQKx+jQU7hFGQaS1z0OicNG5swxZFtCmjYzTpwV06uQMYFwP1rgmQ5hOp0ObNm3Qpk0b1NbW+rMmCmGu3fK5RxgFET4PidyzYIEe8fEydu40o1Mn762BDVVuneakKJzLJe/gbvkU7Pg8JGpcUZGILVs0yMqycRtINzU5EnbkyBEsXLgQiqK4/r1edna2X4qj0OM6vJtrwiiI8HlI1LxXX9UjLk7G+PFWtUsJGk2GsGnTpjX670StUR/COB1JwYTPQ6KL27VLxObNGsyebUF0tNrVBI9md8wn8iahgtORFHz4PCS6uAUL9GjbVsGjj3IUzBNurQkj8haxvByKKEI557QEIiIKXt99J2LTJg0mTbJyFMxDDGHkV6LJBKVtW+DsyQlERBTcFizQIzZWwcSJHAXzVLMh7Nwdok+ePImJEyf6tCAKbWKFiVORFLT4PCRqqLhYxKefavD441a4cfIgnafZY4vee+89REVFwWKxYNGiRVyUSq0imMq5KJ+CFp+HRA29+qoObdoo+N3vOArWEs2GsCVLlmDSpEmwWCx4++23eb4jtYpYYYKjS1e1yyBqET4PiX6zZ4+ITz7R4qmnLIiJUbua4NRkCMvOzoYgOA/hNBgMKC4uRk5ODgBgwYIF/qmOQo5YXg7b4OvULoPII3weEl1o4UIdYmIUPPYYR8FaqskQlp6e3uDrCRMm+LwYCnGyDKGyAnI7jh5QcOHzkKihfftEfPSRFk8+aUGbNmpXE7yaXJg/ePBgDB48GDU1NdixYwcGDx6Mv//977BYeBI6tYxwqgqCw8HDuyno8HlI1NDChTpER3MUrLWafTty8eLFePDBBwEAr732Gv7f//t/Pi+KQpPIcyMpyPF5SASUlIj44AMtfvc7K9q2Vbua4NZsCNNoNGjXzvk2m9FohChyazFqGaGcRxZRcOPzkMg5ChYVpeDxxzkK1lrNvh3Zt29fPPnkk+jXrx+Ki4vRq1cvf9RFIUg8e2QRD++mYMXnIYW7AwdEbNyowbRpVvDl4NZrNoTNmTMHmzdvxuHDh3H77bdj+PDh/qiLQpDr8G5OR1KQ4vOQwt3ChTpERACTJtnULiUkNDuWbjabUVRUhMLCQnz99deoqqryR10UglwhjNORFKT4PKRw9v33It57T4NHH7WiXTtF7XJCQrMhbNasWejYsSOys7PRqVMnzJw50x91UQgSTCbIUdGAwaB2KUQtwuchhbP6UbCsLI6CeUuz05GVlZXIzMwEAPTs2ROffvqpz4ui0CSayqG04ygYBS8+Dylc/fijgPfe0yAry4b4eI6CeUuzI2EWiwUnT54EAJSXl0OWZZ8XRaHJeXg3QxgFLz4PKVwtWqSHwQBMnsw3Ir2p2ZGwJ554Aunp6TAajaipqcELL7zgj7ooBAkmE+SEBLXLIGoxPg8pHB06JCAvT4PHH7chIYGjYN7UbAiLiYnB5s2bUVFRgbi4OBQWFvqjLgpBoqkcju491C6DqMX4PKRwtGiRHjodR8F8ockQ9s033+DHH3/EypUrMX78eACALMtYu3YtPvzwQ78VSKHDOR3J7Sko+PB5SOHq8GEB776rwcSJNnTowFEwb2syhMXExKC8vBxWq9W1BkIQBDz11FN+K45CyJkzEM6cYQijoMTnIYWr117TQ6sFfv97joL5QpMhrFu3bujWrRvuvfdedOjQAadPn4YoioiOjvZnfRQi6vcI49uRFIz4PKRw9NNPAnJzNZgwgaNgvtLk25H79u3DPffcg7i4OHz22WcYOXIkUlNT8fnnn/uzPgoR9UcWcSSMglFLn4c2mw1PPfUUMjIyMG7cOGzevBklJSXIyMhAZmYmHn30UZSfPVM1NzcXY8eORVpaGrZs2QIAqKiowIQJE5CRkYHp06ejtra2ybZE3vb66zpoNMDUqRwF85UmR8IWLVqEl156CVqtFq+99hpWrFiByy67DBMnTuRRHeQxwXVkEUfCKPi09Hm4ceNGxMbGYv78+aisrMSYMWOQmJiIuXPnomfPnli3bh1WrFiBiRMnYvXq1cjLy4PFYkFGRgaGDh2KpUuXYtSoURg7diyWL1+O9evX484772y0rU6n8+NvhELdzz8LWL9ei4cftuGSSzgK5itNjoQpioIePXrg+PHjqK2tRe/evREdHQ1RbHZrMaILiOWcjqTg1dLn4ciRI/HEE0+4vpYkCQsXLkTPnj0BAA6HA3q9HsXFxejfvz90Oh2MRiOSkpJQWlqKoqIi3HDDDQCAYcOGYfv27U22JfKm11/XQRQ5CuZrTY6E1W9C+NVXX+G6664DAFitVpjNZv9URiGF05EUzFr6PIyKigIA1NTUYNq0aZg+fTrat28PANi1axfWrFmDtWvX4quvvoLRaGzwuZqaGtTU1LiuR0VFobq6usG1c9s2R5IExMZGutFOdKudv/rxZl+syT1lZSLeflvExIkKevWKUL0eb/YVaDU1GcKuu+46pKen49dff8Xf/vY3/Pzzz/jTn/6EO+64o1U3pPAkmkxQNBooMW3ULoXIY615Hh47dgxTpkxBRkYGRo8eDQD4+OOP8be//Q3Lly9HXFwcoqOjGwQ6s9kMo9Houm4wGGA2mxETE9Nk2+Y4HAqqqs402y42NtKtdv7qx5t9saaLy8vTICdHj7Iy59edO1tRVdXycyID6Wfzdj+e9JWQ0PSfzyZD2GOPPYZbbrkFcXFxaNu2LX7++Wfcf//9uPXWW1tWLYU1ocIEOa4dIAhql0LksZY+D8vLyzFhwgQ8++yzrhG0999/H+vXr8fq1asRGxsLAOjbty9ee+01WCwWWK1WHDx4EN26dUNycjK2bt2KsWPH4ssvv8SAAQOabEvUGnl5GmRnG1Bb+9sz+sUX9YiLU5CaalexstB20R3zu3Tp4vr3pKQkJCUl+bwgCk1ieTkUTkVSEGvJ83DZsmU4ffo0li5diqVLl8LhcOCHH35Ax44dMXXqVADAoEGDMG3aNGRmZiIjIwOKomDGjBnQ6/XIysrC008/jdzcXLRt2xYLFixAZGRko22JWkpRgD/9Sd8ggAFAba2AnBw9Q5gPNXtsEZE3iKZyvhlJYWfOnDmYM2eOW23T0tKQlpbW4Fp8fDzeeOMNt9oSuUtRgIMHBWzbpsH27RLy8yWcPNn4SyZHj3L2wpcYwsgvhAoTHL2vVrsMIqKwoyjO44fODV3HjztD1yWXyBg2zIHPPwcqKy8MYp06cXsKX2III78QTeXcnoKIyAfqF9QfPSqgU6cozJplQXKyA9u3a7Btm4Tt2yX8+qszYLVvLyMlxYGhQ60YOtSOK65QIAiNrwmLiFAwe7ZFrR8rLDCEke/Z7RArK50L84mIyGvOD09lZQKmTDFAUZxfJyTIGDr0t9DVpYvS6PtRznVfdeeEOWcA43ow32III58TKisBcI8wIiJvy8m5cEG9ogiIjZXx0Ue1uOoq2e2X0lNT7UhNtXt1Gwe6OIYw8jnX4d3xDGFERN7U1ML5U6cEdO0q+7ka8hTPICKfqw9hnI4kIvKuSy9tfOE8F9QHB4Yw8jmBRxYREfnEtddeuGaLC+qDB0NYmNLn5SIuuTc0ei3ikntDn5frs3vx8G4iIu+TZWDXLg2uvNKBxEQZgqAgMVHGwoV1XFAfJLgmLAzp83JhzJ4KobYWACCVHYEx27l7tyXV+xtAug7v5nQkEZHXfPGFhJ9+ErFsWS3GjuWC+mDEkbAwFJXzvCuA1RNqaxGV87xP7ieYyiG3iQW0Wp/0T0QUjt58U4eEBBmjRnHUK1gxhIUh8WiZR9dbfT9TOeS4OJ/0TUQUjv73PwGbNknIzLRBp1O7GmophrAwJHdK9Oh6a4mmCh7eTUTkRStX6iCKwEMP2dQuhVqBISwMmWc/B0XTcGpQiYiAefZzPrmfaCqHzD3CiIi8orYW+Ne/tBg50o6OHbkVRTBjCAtDltQ0OLp2Rf0fXbldPKoXLvbJonzg7JowLsonIvKK99/XoLJSwIQJHAULdgxh4chuh/jzz7DclwFFEFD76GM+C2BQFIgVJk5HEhF5yZtv6tCtmwMpKQ61S6FWYggLQ5p9eyCaa2Ad/n/AVV2h2VPss3sJNdUQrFZu1EpE5AW7don47jsJ48fb3D4TkgIXQ1gY0u7IBwDYrr0eSr9+0Oz1YQgrrz+yiG9HEhG11ptv6hAVpSAtjVORoYAhLAxpv94Bx2WXQ760I5R+/SAd+RlCVaVP7lW/USsP7yYiah2TScD772uQlmaD0ah2NeQNDGHhRlGgLdwB27XXO7/s1w8AoNm7xye34+HdRETesXatFhaLgPHjOQoWKhjCwoz04w8Qy8t/C2HXnA1hPloXJlRUAODh3UREreFwAKtWaTF0qB09eshql0NewhAWZrRfbwcA2K69znmhfXs4LrkUmj27fXK/+sO7GcKIiFpu0yYJR46I3JYixDCEhRntjnzI8QlwXHmV65r96r7Q7PPddKSi1wNRUT7pn4goHLz5pg6XXCJj5EieExlKGMLCjLZgB2zXDcW57zbbr+4L6fsDzm2YvUyoMDlHwfguNRFRixw8KOCLLzR46CEbtNrm21PwYAgLI+LRMkhHfv5tKvIse+++EBwOaEr3e/+epnJORRIRtcLKlTpoNAoyMzkVGWoYwsLIb+vBrm9w3X51XwC+WZwvmsqhcI8wIqIWMZuBt9/WYtQoOzp04DmRoYYhLIxod2yHbIyBvVefBtflyy6HbIzxyaatosnEkTAiohbasEGL06d5TmSoYggLI9qC7bANHgJIUsNvCALsfa72yUiYYDJB5katREQeUxTgzTe16NXLgSFDeE5kKGIICxNChQmaA6UXTEXWs1/dF5qSfc7NaLzFYoFYfRoKN2olIvJYQYGEffskTJjAcyJDFUNYmNAWfA0AsA1pIoT16QvhzBlIhw567Z5iJTdqJSJqqbfe0iImRkFqKqciQ5XPQtju3buRmZkJADCZTMjKysIDDzyA9PR0/PzzzwCA3NxcjB07FmlpadiyZYuvSiE49wdT9HrY+yc3+n371dcAgFc3bf3t8G6OhBEReeL4cQEffqhBerqN2yyGMI0vOl2xYgU2btyIiIgIAMD8+fMxzq3/cgAAIABJREFUevRo3HHHHfj6669x6NAhREREYPXq1cjLy4PFYkFGRgaGDh0KnU7ni5LCnrZgO2zJAwG9vtHvO7p1h6LTQbOnGJax93rlnjy8m4ioZdas0cJmEzB+vFXtUsiHfDISlpSUhMWLF7u+3rVrF44fP45HHnkEH3zwAQYPHozi4mL0798fOp0ORqMRSUlJKC0t9UU5VFMDTfHuC/YHa0Crhb1HL68uzncd3s3pSCIit9ntwD//qcWNN9rRpQu3pQhlPhkJGzFiBMrKylxfHz16FDExMVi5ciWWLFmCFStW4PLLL4fRaHS1iYqKQk1NTbN9S5KA2NhIN9qJbrVzh7f6UqsfoWg7BIcD+ltuhu68z53blzQgGcIHGxHbJsLjHe4bq0k8cxoAYLwiEfCg3kD7fXuzr1CviYha7z//0eDYMREvvWRRuxTyMZ+EsPPFxsZi+PDhAIDhw4dj0aJF6NOnD8xms6uN2WxuEMqa4nAoqKo648Y9I91q5w5v9aVWP5GbPockiqjqeQ2U8z53bl+Gbj1hLH8Tp0t+hNyxU6triiw7hkhBQJVoADyoN9B+397sK5hrSkho/s8nEbXeW29pkZgo47bbeE5kqPPL25EDBgzA1q1bAQA7d+7EVVddhb59+6KoqAgWiwXV1dU4ePAgunXr5o9ywo62YAfsffpCMcZctJ29T/3ifO9MSbp2yz9/XzIiImrUgQMitm3T4OGHbXx0hgG/jIQ9/fTTmDNnDtatW4fo6GgsWLAAbdq0QWZmJjIyMqAoCmbMmAF9E4vGqRWsVmiLdqL24QnNNrX37gNFEKDZsxvWEbe3+taiycQ3I4mIPPDmm1rodAoeeIDbUoQDn4WwxMRE5ObmAgA6deqEt95664I2aWlpSEtL81UJBECz+1sIdXVN7g/WQHQ0HFd2gWbvHq/cW6jgkUVERO6qrgZyc7W4+2474uO5ID8ccLPWEKf9egcAwDbkIm9GnsPep6/XzpAUTeVQGMKIiNySm6uF2SxgwgRuSxEuGMJCnPbrfNiv6golIcGt9var+0L6+X8QqipbfW+xvJzTkUREblAU54L8a65xIDlZVrsc8hOGsFAmy9AWFsB23VC3P2Lv0xcAWj8lKcsQKisgxzOEERE1Jz9fwvffS5gwwcpzIsMIQ1gIk0r2QzxV5fZUJHBuCGvdlKRwqgqCw8HDu4mI3PDmm1q0bavgnnu4LUU4YQgLYdqvtwP/v707D4iyzh84/n7m4lY8UEM88AQRVPLATS1tTSvL3Wxts7Vct37llmWmWZIpmbaVmVlZaeVmZYVHZdpmWZp5DN4X5oF5H9yoAwPM8fz+wCE1kAFmGGb4vP7ZZXzmM59hhk+f5/t8n+8XsCQ4MSn/ErVJE2xNm1V7mQrHlkUyMV8IIa7tzBmF//1Px733Wri025+oI6QJ82F64yZs4c2xt2hZqedZY6s/OV/JkiZMCCGcsWiRHrsdRo2SCfl1jTRhvkpV0Rs3lewXWckJBtbYOLSHDkJhYZVf3rFvpNpILkcKIUR5iovh44/13HyzjdatZVmKukaaMB+lOXYUbfo5LAnOT8p3sHaOQ7HZ0B3YX/XXl8uRQghRoeXLFTIzNbIsRR0lTZiP0qdcWh+sEvPBHEon51djXphyaSRMlqgQQog/WrZMR3x8EPffr6DVquTmyi2RdVGNbFskap5+80bsDRpg69Cx0s+1t2qNPaQeur27q/z6mqws1MAgZJapEEJcadkyHePH+2M2lzReNhtMmOCPRlPIsGFyd2RdIiNhPkpv3FSyNIWmCh+xRoO1c2y11grT5GRjbyyXIoUQ4mozZviVNmAOZrPCjBmyf3JdI02YD1LS09Ed/a1K88EcrJ1j0e3fV3KKVgWa7CzsMilfCCH+4PTpsi89lve48F3ShPkgfYpjfTDnF2m9mjW2C0pBAdrfjlTp+Up2tswHE0KIMlx3Xdl3QTZvLndH1jXShPkgvXETamAg1tguVY7x++T8qs0L0+Rky+bdQghRhpYt7cCVDVdAgEpiYpFnEhIeI02YDzJs3oTl+p6g11c5hq1DR1S9vsrzwkouR0oTJoQQl/vhBy1Go45bb7USEWFHUVQiIuzMni2T8usiuTvSxyjn89Du30fRhGeqF8hgwBrVqWojYQUFKAUFMidMCCEuk5cHTz3lT3S0jfnzC/Hzg9DQQPLyCjydmvAQGQnzMfqtKSiqiqV31SflO5RuX6RWbp6CY6FWuRwphBC/e/55fzIzFd54o6QBE0KaMB+jN25G1euxxHevdixrbBya7Gw0585W6nkaWahVCCGusGaNls8/1zN2bDFdu9o9nY6oJaQJ8zH6zRuxxnWFwMBqx7LGVG1yvpItWxYJIYTD+fMllyE7drTx1FOyPZH4nTRhvsRsRrdrR5W2KiqLrXNnVEWp9PZFpZt3N5aRMCGEmDrVj4wMhblz5TKkuJI0YT5Ev3M7isWCpbdrmjA1OARbZJsqN2FyOVIIUdf99JOWxYsNPPZYMd26yWVIcSVpwnyI3rgJVVGw9ExwWUxrbJdKL1Oh5OSg6nSo9UNdlocQQnibCxdg/PiSy5ATJshlSPFH0oT5EP3mjdiiOqGGNnBZTGvnWLQnjqGcz3P6OZrsrJJRMEW24BBC1F3Tpvlx7pzcDSnKJ02Yr7Ba0W3bWq2tisoMG3tpcn4lRsM0WVmoskaYEKIOW7tWyyefGHj00WLi4+UypCibNGE+QrdvD5p8k0vWB7uctXPJ1keVuUNSk5Mtd0YKIeqsixdLLkO2b29j4kS5DCnKJyvm+wi90bFpt2sm5TuoTZpga9K0UiNhSnYWtphYl+YhhBDeYto0P86eVVi50oy/v6ezEbWZjIT5CP3mTdhatcbe7DqXx7bGxlXqDklNdhZqw4Yuz0MIIWq7n3/W8vHHBsaMsdC9u1yGFNcmTZgvUFX0Wza7fBTMwRrbBe2hA1BY6MTBVpS8PLkcKYSoc0wmePJJf9q1s/H000WeTkd4AWnCfID28CE02dlubMLiUGw2dAd/rfBYJTcXRVVl824hRJ2TlOTH6dMld0MGBHg6G+ENpAnzAaXzwVy0SOvVrJfmdzlzSVI27xZC1EXr12v56CMDjzxioUcPuQwpnCNNmA/QGzdhD2uCLbKtW+LbW0diDw5x6g7J0tXypQkTQtQRjsuQbdvaeeYZuQwpnCd3R/oAvXFTyaVIdy2OqtFg7Rzr1EiYIlsWCSHqmOnT/Th1SmHFCrNchhSVIiNhXk5z6iTaUyddvkjr1aydY9HtTwWb7dr5ZF+6HNlYRsKEEL5vwwYtCxca+L//s9Cr17XroxBXkybMyznmgxUnuHaR1qtZY7ugFOSjPfrbNY+TzbuFEHWFyQTjxvkTGWnn2WflMqSoPGnCvJzeuBl7SD1snWLc+jrWzpe2L6pgXpiSnYW9Xn3Q692ajxBCeNqMGX6cPFlyN2RgoKezEd5ImjAvpzduxNKzF2i1bn0dW8coVL2+wnlhJVsWySiYEMI3LVumIz4+CD8/DR98YKB/fxsJCXIZUlSNNGFeTMnORnfooNvWB7uCwYC1YzS6fRU0YVnZsjyFEJdYLBYmTpzIiBEjuPvuu/nxxx9L/23mzJl89tlnpT8nJydz1113MXz4cNauXQtATk4Oo0ePZsSIEYwbNw6z2VzuscL9li3TMX68P6dOaVDVkhuhNm/WsmyZ3OMmqkaaMC+mT9kMgKVXDTRhXNq+aN8eUNVyj9FkZ8lImBCXrFixgtDQUBYvXsyCBQuYPn06OTk5PPjgg/z000+lx2VmZvLxxx/z+eef88EHHzB79myKi4uZN28eQ4YMYfHixXTq1Ikvvvii3GOF+82Y4YfZfOVd6GazwowZfh7KSHg7acK8mN64CdXPD2u3+Bp5PWtsHJqsLDTnzpZ7jJKTLWuECXHJ4MGDeeKJJ0p/1mq15OfnM3bsWIYOHVr6+J49e+jWrRsGg4GQkBBatmzJgQMH2L59O3379gWgX79+bNq0qdxjhfvk5cHy5TpOnSp7GaDTp920PJDweTKG6sX0xo1Y4ruDX82chVk7dwFAt28PxdeF//EAVb20ebeMhAkBEBQUBIDJZOLxxx9n3LhxtGjRghYtWrB+/frS40wmEyEhIVc8z2QyXfF4UFAQFy9eLPfYimi1CqGhFc8e12o1Th1XU3FcGasycQ4fhlWrFFatUtiwAWw2BY1GxV7GYvgtWlDl/Lz991QTcVwZq7blJE2YtzKZ0O3dQ8HjT9bYS9piSu7A1O3dQ/HAwX/4dyXfhFJcLCNhQlzm7NmzPProo4wYMYI77rijzGOCg4PJz88v/Tk/P5+QkJDSx/39/cnPz6devXrlHlsRm00lL6+gwuNCQwOdOq6m4rgy1rXiWK2wdauW1at1fP+9lrS0kpudoqNtPPaYlVtusXLsmIYJE/yvuCQZEKDy7LOF5OVZXZ6Tp2LVtjiujOWJnMLCyv/7lMuRXkq/bQuKzVZj88EA1JB6WCPblHuHpJLl2LJIRsKEAMjKymL06NFMnDiRu+++u9zj4uLi2L59O0VFRVy8eJEjR47QoUMH4uPj+fnnnwFYv349119/fbnHivJdfkdjfHxQ6UT6Cxfgq690jBnjT0xMMEOHBrJggZ7mzVVmzixk2zYTP/9cQGJiMT162Pnb36zMnl1IRIQdRVGJiLAze3Yhw4ZVrQETQkbCvJTeuAlVo8Has1eNvq41tgv6XTvL/DfHQq2qNGFCAPDuu+9y4cIF5s2bx7x58wBYsGAB/v7+VxwXFhbGyJEjGTFiBKqq8uSTT+Ln58eYMWOYNGkSycnJNGjQgNdee43AwMAyjxVlc9zR6Bi9OnVK4fHH/Zkzx86RIxqsVoWGDe0MHGhl0CArN91k5VoDi8OGWRk2zOrSERVRd0kT5qX0xk1YY7ugBld8GcKVbJ1j8V/xJcr5PNT6oVf8myanZMsiuRwpRInnnnuO5557rsx/Gzt27BU/Dx8+nOHDh1/xWOPGjfnggw/+8NyyjhVlK+uORotF4cgRDWPGFHPLLTa6d7e5e6lFIcoklyO9UVER+h3b3L5fZFmssZdWzk/d94d/U7KlCRNC1C7l3blos8GUKcX06iUNmPAcacK8kLJjO0phYY3OB3OwOO6QLGP7Ik2WXI4UQtQu111X9rqGzZuXv96hEDVFmjAvpGzYAIClV82PhKlNm2Jr0rTMyfmanGxUPz/UoOAaz0sIIa5msUBwsApc2XAFBKgkJsqG28LzpAnzIn7LkmkYH4MmcTKqTodhvWe2K7F1jkW3b+8fHleys0ouRSqycKEQwvOef96PQ4e0jBxpkTsaRa0kE/O9hN+yZELGj0W5tHccVish40sm9hYNq9kJutbYLgSsXwdFRVcsFKvJzsIuC7UKIWqBTz7R88EHBh5+uJjp04uAIrmjUdQ6MhLmJYJmJP3egF2imM0EzUiq8VwssXEoViu6A/uveFyTnS3zwYQQHmc0apk0yY+bbrIydapcdhS1lzRhXkJz+lSlHncnW+dYgD/MC5PNu4UQnnbqlMLo0f60aKEyf74ZnVzvEbWYNGFewt48olKPu5OtdRvswSHo9l3ZhCk5ObI8hRB1XHmr09eEggJ44IEACgsVFi0yExpa8XOE8CRpwrxE/jPPoV414V0NCCA/cWrNJ6PRYIvpfOVIWHExmgvnUaUJE6LOcqxOf+qUBlVVOHVKw/jx/jXSiKkqjBvnz759Gt57z0yHDmXstC1ELSNNmJdQLl5EUVXsjRqhKgq2iBZcnP1mjU/Kd7DExpUs2GqzlTzg2DdSJuYLUWeVtTq92awwY4b7t1WaO9fAV1/pSUwsZuBAm9tfTwhXkKvlXkDJyiLoPy9S3K8/55d8RWiDII/f4WPrHIdSkI/22G/Y2rb/vQmTkTAh6qzyVqcv73FXWb1ay8yZBu66y8LYscVufS0hXElGwrxA0EsvoOSbMM18pdaswVW6fdGlS5JKViYAamNpwoSoq8pbhb5BAxXVTQvUHzyoYcyYAOLiStb/qiUlUginSBNWy+l2bsf/k48wPzQGW4eOnk6nlLVjNKpe//u8sEy5HClEXZeYWERAwJXdlqKo5ORoeOABf9LTXdsh5ebCyJEBBASofPSRmcBAl4YXwu2kCavN7HaCn52APawJBRMmeTqbKxkMWDtGl+4hqWTL5Ugh6rphw6w8/bRjXa6S1enfequQqVMLWbdOR58+QXz+uc4lo2JWKzz0UABnzigsXGgmPFz2ghTeR+aE1WJ+XyxGv2M7F956DzWknqfT+QNb51gMa1aX3JaUmYmqKKgNGng6LSGEB9W7VKr27rXTtOnvc1cHD7Yybpw/jz8ewFdfWXnttcJqbaKdlOTH+vU65swx07On3AkpvJOMhNVSyvk8gqc/j6VnAkV/+7un0ymTNTYOTVYWmvRzkJVV0oBptZ5OSwjhQUajlsaN7XTocOXjbduqfP21mZkzCzEatfTtG8SiRfoqjYp9/rmO994z8NBDxYwYIXtACu8lTVgtFfjKTJTsbEwvvVprJuNfzRrbBQDd3t0oWVlyKVIIQUqKll69bGWWLY0GHnzQwrp1+XTrZmPCBH/uvjuA48edr3Fbt2qYMMGfvn2tJCXJlkTCu0kTVgtp96cS8OECCh8YXdro1EbWmM7ApTskszJRZVK+EHXamTMKJ05oSEi49jpdrVurLF1qZtasQnbu1HLjjUG8/74eewVXFc+eVfjnPwMID1dZsEC2JBLeT5qw2kZVCZ48EbV+ffKfneLpbK5JDamHrXUkun17UbKyZSRMiDrOaCyZjtC7d8WLpSoK3H+/hfXr8+nVy8bkyf4MHRrAkSNlj4qZzSVbEuXnl2xJ1LChS1MXwiPc1oTt3r2bkSNHApCamkrfvn0ZOXIkI0eO5NtvvwXgrbfe4u677+bvf/87e/bsuVa4OsPv6+UYNm0g/9nnURvU/ipjje1ScodkVqY0YULUcZs3awkOVomJcX6ifESEyuefm5k718yBA1r69w/i7bf1pZtxQMm9P+PH+7N7t4Z33jETFSUT8YVvcMtg7oIFC1ixYgUBAQEA7N+/n3/+85+MHj269JjU1FS2bNnCkiVLOHv2LGPHjmXZsmXuSMd7mEwETU3EEteVwn884OlsnGKNjcPvm69QNRrsjeRypBB1WUqKlh49bJW+P0dR4O9/t3LTTfk8/bQfSUn+fPONnttvt7BwoYFTpxRAy513Whg8WLYkEr7DLSNhLVu25M033yz9ed++faxbt4777ruPyZMnYzKZ2L59O3369EFRFMLDw7HZbOTk5LgjHa8RNGcW2rNnSibje8ldhtbOsQAodjuqNGFC1Fk5OXDggLbC+WDX0qyZykcfFfLuu2YOHlSYPt2PU6c0QMklyh9+0NXIZuBC1BS3fJsHDRrEqVOnSn+Oi4vjb3/7G507d+add97h7bffJiQkhNDQ0NJjgoKCuHjxIg0ruNCv1SqEhla8LLJWq3HqOGe4KtY14xw6hO6dN7GPvJ/ggf1rJB+XxLohofT/+rdojp+7f08eiOPKWL6ek6i7tmwpOXGsThMGJaNid91lJSnJj/z8sjcDHzZMlqUQvqFGTikGDhxIvUsr+A0cOJDp06dz8803k5+fX3pMfn4+ISEhFcay2VSnNq8ODQ102SbXropVbhxVpd4TT6D6B5Dz9BTUCl6rNr03v29Xo9NoUOx2lAlPUWAupmjYcI/m5Oo4rozlzTmFhVX89ynqLqNRh8Gg0q2bay4Xnjvnmc3AhahJNXJ35L/+9a/SifebN28mJiaG+Ph4NmzYgN1u58yZM9jt9gpHwXyV4fvv8PvxBwomPoPatKmn03Ga37JkQsaPRbl0X7k2K5OQ8WPxW5bs4cyEEDXNaNTSrZsNf3/XxCtvNf3qrLIvRG1TIyNh06ZNY/r06ej1eho3bsz06dMJDg6me/fu3HPPPdjtdp5//vmaSKX2KSwkOHES1o5RmP/1sKezqZSgGUkoZvMVjylmM0Ezkqo9GiaE8B75+bBnj4ZHHy12WczExCLGj/fHbP595CsgQCUxURZoFb7DbU1YREQEycklIyIxMTF8/vnnfzhm7NixjB071l0peIXAt99Ae+IYecu+Ab3e0+lUiub0qUo9LoTwTdu3a7FalWrPB7tcybyvQmbM8OP0aYXmzUsaMJkPJnyJ3GbiQZqTJwicO5vCO/+Kpe+Nnk6n0uzNI9CeOlnm40KIusNo1KIoKj16uHb5iGHDrAwbZnXpXEohahNZMd+DgqcmgqKQP+1FT6dSJfmJU1EvrQXnoAYEkJ841UMZCSE8ISVFS0yMnUv3XwkhnCRNmIfof16L38qvKXjiKewRLTydTpUUDRvOxdlvYotogaoo2CJacHH2mzIfTIg6pLgYtm2r3vpgQtRVcjnSE4qLCZ48EVvrSArGePecuKJhwykaNlwuFwhRR+3Zo8FsVpzaL1IIcSVpwjwg4P330B0+xPlPk3HZ/dxCCOEBjk27e/WSJkyIypLLkTVMk36OwFn/oWjgIIoHDvZ0OkIIUS0pKTratLHTpIms3yVEZUkTVsOCXngepbgI0/T/eDoVIYSoFru9ZFJ+QoIsGyFEVUgTVgP8liXTMD4GnZ8e/yWfUzTgz9jbtPV0WkIIUS0HD2rIy3Pt+mBC1CXShLmZY2sf7amTKGrJcL3fz2tlax8hhNeT+WBCVI80YW52ra19hBDCmxmNWpo1s9O6tcwHE6IqpAlzM9naRwjhi1S1pAlLSLChKBUfL4T4I2nC3Ky8LXxkax8hhDc7cULh7FmNXIoUohqkCXOz/GefR73qNFG29hFCeDvHfDCZlC9E1UkT5mZqSAiKqmJv2Ei29hFC+IyUFC3166tER9s9nYoQXktWzHezwLffwNaiJTkpuwhtXE+29hFC+ASjUUvPnjY0ciovRJXJn48b6bZtQZ+yGfPD/wad9LtCCN+QkaGQliabdgtRXdKEuVHg23Oxh4ZiHnG/p1MRQgiXSUlxzAeTlfKFqA5pwtxEe+Qwhm+/wTzqQQgO9nQ6QgjhMikpWgICVLp0kflgQlSHNGFuEvDO22AwYP7Xw55ORQghXMpo1BIfb8Ng8HQmQng3acLcQMnMxP+LTykcfi9q06aeTkcIIVzm4kXYt0/WBxPCFaQJc4OAD96D4mLMY8Z6OhUhhHCprVu12O0KvXtLEyZEdUkT5mr5+QQsXEDxoNuwtWvv6WyEEMKljEYtWq3K9ddLEyZEdUkT5mL+n3+CJjeXgkef8HQqQgjhckajlrg4u9xvJIQLSBPmSlYrge+8jaV7T6y9EjydjRBCuFRREezcqZX5YEK4iDRhLuS38mu0J45R8Ng4T6cihBAut3OnlqIiRRZpFcJFpAlzFVUl4O25WNu2o3jwbZ7ORgghXM6xSKuMhAnhGtKEuYh+4y/od+8suSNSNlMTQvigzZu1dOxoo1Ej1dOpCOETpFtwkYC338DeOIzC4fd6OhUhhHA5m61keQoZBRPCdaQJcwHtr/vx+/EHzA8+DP7+nk5HCCFcbv9+DRcvynwwIVxJmjAXCJw3FzUwEPM/H/R0KkII4RZGo2PTbmnChHAVacKqSXPmNH7LkjHfdz9qg4aeTkcIIdzCaNQSEWEnIkLmgwnhKtKEVVPA/HdAVTE//KinUxFCCLdQ1ZImTOaDCeFa0oRVg3LhPP6LFlJ051+wt2zl6XSEEMItfvtNITNTI/tFCuFi0oRVg/+i/6IxXcQsWxQJIXyY0agDZD6YEK4mTVhVFRcTsOAdivveiDWuq6ezEUIItzEatTRqZKd9e7unUxHCp0gTVkV+y5egPXtGNuoWQvg8o1FLz542FMXTmQjhW6QJqwpVJXDeXKydOmPpf7OnsxFCCLc5d07h+HGNXIoUwg2kCasCw4/fozvwKwX/HoucGgohfJmsDyaE+0gTVgUBb8/FFt6cor/e7elUhBDCrTZv1hIYqBIbK/PBhHA1acIqSbdrB4aNv2D+v3+DXu/pdIQQwq2MRi09etjQ6TydiRC+R5qwSgp4ey72kHoUjnzA06kIIYRb5eXBgQMyH0wId5EmrBI0x47i981XFI76F2pIPU+nI4QQbrVlixZVlU27hXAXacIqIfC9t0GrxfzQI55ORQgh3M5o1KLXq8THSxMmhDtIE+YkJTsb/8UfU3j3PdibXefpdIQQwu2MRh1dutgJCPB0JkL4JmnCnBSwcAGK2Yz53497OhUhhHC7ggLYtUtD795WT6cihM+SJswZZjMBH86naOAgbB2jPJ2NEEK43Y4dWqxWmQ8mhDtJE+YEzceL0GRlyUbdQog6w2jUoigqPXtKEyaEu8jKLxWx2dDMeR1L/PVYet/g6WyEEF7EYrEwefJkTp8+TXFxMWPGjKFdu3Y888wzKIpC+/btmTp1KhqNhrfeeot169ah0+mYPHkycXFxHD9+3OljXc1o1BIdbad+fZeHFkJcIiNh1+C3LJlGnduhpKWhPX4Mv+VLPJ2SEMKLrFixgtDQUBYvXsyCBQuYPn06L730EuPGjWPx4sWoqsqPP/5IamoqW7ZsYcmSJcyePZukpCSASh3rShYLbNumlUuRQriZjISVw29ZMiHjx6KYzQBosrMJGT8WgKJhwz2ZmhDCSwwePJhBgwaV/qzVaklNTaVnz54A9OvXj40bNxIZGUmfPn1QFIXw8HBsNhs5OTmVOrZhw4Yuy3vvXg0FBTIfTAh3kyasHEHTnittwBwUs5mgGUnShAkhnBIUFASAyWTi8ccfZ9y4cbz88ssoilL67xcvXsRkMhEaGnrF8y5evIiqqk4fW1ETptUqhIYGVpizVqth9+6SNSluucVAaKihcm/6sjjOvF5NxpKcvDOOK2PVtpykCbuKkp5O0Kz/oEk/V+a/a06fquGMhBDe7OzZszz66KOMGDGCO+7OHLOIAAAfy0lEQVS4g1dffbX03/Lz86lXrx7BwcHk5+df8XhISAgajcbpYytis6nk5RVUeFxoaCBr19pp3RoCAwvIy3PyjZYRx5nXq8lYkpN3xnFlLE/kFBZW/t+nzAlzMJkIfGUmjXp1xf/Tj1CDgss8zN48ooYTE0J4q6ysLEaPHs3EiRO5++67AejUqRMpKSkArF+/nu7duxMfH8+GDRuw2+2cOXMGu91Ow4YNK3Wsq9jtJdsVyaVIIdxPRsIsFvw/XUTQqy+hycyg6I6/kJ/4PLqdO66YEwagBgSQnzjVg8kKIbzJu+++y4ULF5g3bx7z5s0DIDExkRdffJHZs2fTpk0bBg0ahFarpXv37txzzz3Y7Xaef/55ACZNmsSUKVOcOtZVDhyAnBwNCQlFLo0rhPgjRVVV1dNJVIbFYnN6SP2ax6kqhv+tIujFqejSDmPp1RvT1OlYu/csPcRvWTJBM5LQnD6FvXkE+YlTqzUfzJuHU2sqjitjSU6ujXOtIXVR+zlbO5csCeLRRzUYjSbatKn6fx68+btek7F8OSdffm+ViXWt2lknR8J0W1IITnoO/dYUrO07cH7R5xQPuhUuTYB1KBo2nKJhw136oQkhRG32yy8QFmYnMtKrzs+F8Ep1qgnTHjlM0ItJ+K1aga1JUy7OeoPCESNBV6d+DUIIUa6NGxV697ZefU4qhHCDOtF9KBkZBL32H/wXLUT1DyB/UiIFjzwGl24fF0IIASdPKpw8qTBmjEzKF6Im+FwTdvk8robXhWOJvx7D2p9QigopvP+f5D/1DGqTJp5OUwghapVly3RMnuwHwJw5Bho0UBk2zOrhrITwbT7VhF29yr32zGm0Z05j6RrPxXcWYGvb3sMZCiFE7bNsmY7x4/0xm0uuQWZkaBg/3h8olEZMCDfyqXXCgmYk/WGVewBNVqY0YEIIUY4ZM/xKGzAHs1lhxgw/D2UkRN3gU01YeavZyyr3QghRvtOny56FX97jQgjX8KkmrLzV7GWVeyGEKF/z5mUvR1He40II13BbE7Z7925Gjhx5xWPffPMN99xzT+nPycnJ3HXXXQwfPpy1a9dW+zXzE6eiBgRc8Zisci+EENeWmFhEQMCVDVdAgEpioqyaL4Q7uWVi/oIFC1ixYgUBlzVEv/76K0uXLsWxQH9mZiYff/wxy5Yto6ioiBEjRnDDDTdgMBiq/LqO1exducq9EEL4upLJ94XMmOHH6dMKzZuXNGAyKV8I93LLSFjLli158803S3/Ozc1l1qxZTJ48ufSxPXv20K1bNwwGAyEhIbRs2ZIDBw5U+7WLhg0nZ0cq1iILOTtSpQETQggnDBtmZceOfIqK7OzYkS8NmBA1wC0jYYMGDeLUqZLJ8DabjcTERCZPnoyf3+932phMJkJCft9PKSgoCJPJVGFsrVYhNDTQieM0Th3nDFfFqm1xXBlLcqrZOK6M5cqchBBCOM/t64SlpqZy/Phxpk2bRlFREWlpacyYMYOEhATy8/NLj8vPz7+iKSuPzaa6ZgPvSqhtG4f68ntzZSzJybVxZANvIYRwLbc3YXFxcaxatQqAU6dOMX78eBITE8nMzGTOnDkUFRVRXFzMkSNH6NChg7vTEUIIIYSoFTy2Yn5YWBgjR45kxIgRqKrKk08+ecXlSiGEEEIIX+a2JiwiIoLk5ORrPjZ8+HCGD5eJ80IIIYSoe3xqsVYhhBBCCG8hTZgQQgghhAdIEyaEEEII4QHShAkhhBBCeIA0YUIIIYQQHiBNmBBCCCGEB0gTJoQQQgjhAdKECSGEEEJ4gDRhQgghhBAeoKiqqno6CSGEEEKIukZGwoQQQgghPECaMCGEEEIID5AmTAghhBDCA6QJE0IIIYTwAGnChBBCCCE8QJowIYQQQggPkCZMCCGEEMIDpAkTQgghhPAAacK8kN1uL/3/RUVFLo0H4On1ex2v74o8PP1e3Onqz00IcW1SOysfyxfVptrpk02Yq3/Bropns9kAMJvNnD59uspxNJqSj23hwoVs27at2nlpNBosFgszZ87kwoULKIpS7ZjV4Xj9pUuXcvTo0SrHsdvtKIqCzWbj5MmTVS4ql3/+js+wqs6ePcuZM2eqFcNBo9FQUFBAcnIyUPWi6XhPtakwCc+Q2ln5eFI7rx3HoTq105V1E2pX7fS5JkxV1dI/tG3btpGRkUFBQUGV49nt9tJ4JpOJjIyMKsfSarUAPPXUU9UqJADffvsty5cv54YbbijNszo0Gg0ajYb09PQqx3M8Z9++faxevZo9e/ZUKs7lfwh5eXkcOHCAAwcOVDoPRy6Oz+2ll15ixowZHDhwgOLi4krFufz79N///pekpCSWLFlCdnZ2lfLKy8tj6dKlvPbaa/z222+lr1FVx44d4+DBg0BJAa5sLLvdXvq9nD59Ol988UW1vuPCe0ntrJrq1s7q1k3w/drp6roJtad2+lwT5jgTmD9/Ps8//zyvvfYa33//PVlZWZWOdezYMcxmMwAvvPACiYmJzJo1i/fff7/K+S1dupSTJ08SFRVV6ede/iXJz89HURS+/vproKQQVLWYFBQUoNVqadeuHXPnzi2NV9ncNBoN+/btY/LkyeTk5DB27FhWrFjhdAzHZ2e32wkNDWX48OEsXbqUnTt3VioX+D3/mTNnYrVaCQwMZNGiRWzbtq1SlyEcOS1btgyj0ciAAQNYu3Yt//3vfyudE0Djxo3ZuXMnX375ZWmRrM7Zc2RkJBcuXGDWrFlViuX4PU2aNAm73U6rVq1o0qQJu3btwmKx+PQlCXElqZ2VV93a6Yq6Cb5fO11dN6H21E7ttGnTplXqlb2A0Wjk119/5bXXXkOj0ZCamsq5c+cIDQ0lNDTUqRhWq5WkpCR27tzJmTNnSE9P59lnn6VNmzb89NNPNGjQgPDw8ErnZjKZsFgsbN++nSZNmtCoUSOnnuc4O3EMy2o0Gvr168fmzZs5ePAg119/fZW+lGvWrGHJkiXs2rWLe++9l23btmGz2WjTpk3pkLQzFEXBYrHwzjvv8PDDD9OuXTv27dtHcHAwOp2O6667rtzn2mw2EhMT6datG+fPn+fee+/FZrNht9uJiooiPz+fdu3aVfq9HTx4kC+//JI33niDQYMGcfLkSd5//32aNm1K27ZtnY5z5MgRXnvtNcaPH0/v3r3p27cv7733HtHR0TRp0sSpGI7fpV6vp3nz5nTs2JFjx45x5swZ6tevT3FxMYGBgU7ntGjRIlJTUyksLGTEiBFs3bqV9u3bExQU5HQMh5ycHNasWcMrr7xCREQEZ8+e5bPPPqNv376lZ3qibpDa6TxX1M7q1E3w/drp6roJta92+txImNlsZtasWZw4cYLAwEAGDx7Mn/70J9LS0rBarU7H0el0vPrqqxgMBpYsWUJsbCwNGjSgc+fOtGzZkrNnzzoVx/GaP/74I6+//jp6vZ6BAwfSpEkTkpOTSUlJqTCGo4jk5+czbtw4Fi5cyFdffcXq1au59dZbOXjwID/99JPT781x1ldQUEBcXBwDBgzAZrPx+OOPc+7cOT755BPAuTO6y88g9Xo97dq14+OPP+a5557jww8/xGq1kpqaes0YWq0WnU7Hgw8+iM1mIykpiWbNmrF06VI+/PBD/vOf/zg9f8Nx9mE2m2nZsiUajYbvv/8egBEjRmAwGHjllVfYunWr0+9Lq9XStWtXFi5cyNGjR6lXrx4Gg8HpOQ6Oz2/nzp3cf//9nDt3jptuuomOHTty+vRpRo0a5dT36fIzq6ioKAoLC1m9ejWPPPIIGzZsKP3cnHF5rHr16pGVlcVnn30GgMVi4fDhw2RmZjodT3g/qZ0Vc1XtdEXdBN+una6qm5e/N6h9tdMnRsJsNhsajYbi4mL8/f255ZZbWLFiBVu3buXmm2+mVatWxMTE0KJFC6fiObpvrVZL37590Wg0rF69mpYtWwLw8ccf06NHDyIjI68ZR1VVtFot27Zt47333qNJkyb873//o3379rRt2xaz2UxkZCRhYWHlPl9RlNIzqo8++ohOnTrx1FNP0bFjR3bt2kVsbCy33HILsbGxTv++FEXhyJEjjB8/nvT0dDp37szQoUOJj48nISGBzZs3k5+fX2HMy6/5b9myBYPBgN1u5+DBgwQFBZGdnc369eu51lfMarWi0WgYMGAA9evXZ9KkSXTv3p2BAwdyxx130KFDByIiIsjKyiIuLs6p95abm8u7776LVqslOjqaTZs28fPPP7No0SKmTJlC48aNycrKokuXLmXGsNlsaLVaTCYT3377LRcuXKBdu3Y0a9aMOXPm8N1339G7d29uv/320s+oopxMJhPjxo3j4Ycf5k9/+hMNGzZk27ZtDBo0iISEBLp163bNGI6ClJqayrx587BYLDRr1oyHHnqIFi1a0KJFCyIiIpw663XEOnDgAOvWrePcuXP079+fV199lSNHjvDFF19w3333ER8fX2Es4d2kdtZ87XRF3QTfr52uqJtQ+2un1zdhjslxqqoybtw41q5dS1ZWFklJSfzwww/MnTuXv/71r9SvX79Sl9bS09N56623+O677+jXrx8hISF89NFHrF+/nqFDh3LrrbdeM8acOXPYsmULHTp04Msvv2TMmDF07NiRDRs2sGbNGgICAhgwYAAdO3YsN0Zubi4BAQHY7Xb27NnDa6+9Rq9evYiJiSE0NJQ1a9ZQv3790i9iRV/qtLQ0GjZsiMVi4YknnuCRRx5h165drFu3jrCwMJo2bUrz5s1p3rw5O3bsoE+fPhX+ngAWLFjAu+++y7FjxwgNDaVDhw5ERUVx9uxZJkyYQEBAQLkxHMXoxRdfpHv37gwdOpSpU6dy/vx5evbsSbNmzdDr9Xz++ecMGDAAvV5f5nu8/L3n5eVx8uRJjh07BsAtt9xCUFAQYWFhREVF8frrr3PfffeVOxzuyOmZZ55BURSOHz/Orl276N27N61atSItLY0ePXrQoUOHa/6+d+zYwbFjx9iwYQPR0dEcPnyYBx98kICAAE6cOMHatWsZMmQIzZs3v+bvOScnh8DAwNL5IrfeeisXL17kyJEjaDQaEhISiImJcfqyg6IoZGZm8uijj9K/f39mzpxJeHg4zz33HBEREQwYMIA//elPTsUS3ktqp2dqpyvqJvhu7XRV3QTvqJ1e3YSlp6cTHByMoigkJSXRtm1bBg8ezPvvv8/Zs2eZMmUKBoOBLl26OFVEduzYQcOGDdHpdDzxxBPccccdZGVlsXjxYkaNGkVCQgKqqnLfffeVG0NVVQoLC5kzZw67du3i3Llz2O12DAYDy5Yt46233mL79u2EhYUxcODAcuPk5OQwdOhQLBYLP//8MzfccAOhoaGsXbuWoKAgDh8+zC+//MIDDzxAcHAwcO2Jhd9++y1TpkwhMDCQ9PR0wsPDueWWW9i0aRP169dnyZIlREZGEhkZycaNG2nRogXt27ev8Hd2+RwSu93OkSNHUBSFPn36cOONN1ZYSC5/vwsXLqR169Y88cQTvPzyy6Snp9O7d2/27t1L48aN6d69+x/e49VnvGfOnCE8PJzWrVuTm5vL7t27sVqtDBkyhLy8PBYsWMDf//730jujLpeXl0dmZib+/v6sX7+e8+fPM27cOBYsWMDAgQMxGAzccMMNhIWF8eWXX9KsWbNy57b88MMPfPjhhwQHB7Nu3TrWrFnDqlWraNq0KdHR0XzzzTekpaVx2223XfP3snnzZn744QdCQ0PZuXMn9evX55///CfXX389Bw4c4NChQ2W+l7JcvHgRk8mETqfjyy+/JCEhgRtvvJFNmzYRERHB+fPn6dOnT7mjC8J3SO30bO10Vd10vF9fqZ2uqpvgPbXTa5swxzBlXl4e9erVY9euXfzrX/9iyZIlJCQk8P3337N582bGjx/vVLw1a9aQnJxM//79OXjwIEePHuUvf/kLS5cu5cEHH+Snn37ipptuqvBDc0wijI+P5/z583To0IHTp09jNpvR6/WcPHmSQ4cOkZSUdM04ubm5/PLLL7Ru3Zrw8HDeeOMNdDodO3fu5Oeff2bfvn0888wztGvXzqlJoOfPn2f16tWYTCZOnTqFzWYjJSWFhx9+mAYNGnDixAkeeeQRNBoNbdu2JTo6utxYjtcrLi7m6aefpri4mL/+9a+0b9+e4uJitm3bRocOHcqdOJuenk5aWhrNmjXj6NGjGAwG4uLiaNu2LfPnz8dsNvPyyy8TFRVFQEAAkZGR5Q6nX37Gu23bNiZPnkzbtm1L38OaNWvQ6/UkJCTQpk0bevbsSdeuXf8Q5+TJk0yaNImtW7eSk5NDZGQk+/fvZ+XKldx77700atSI999/n6FDh9K8eXO6detGp06dyszp4MGDvPXWW0ydOpX+/fszdOhQ9Ho9RqORrVu3cvHiRYxGIy+//DL+/v7X/NwyMjL49ddfyczMxGw2s2HDBtq3b0/Tpk3Zt28f2dnZ3HjjjdeMAfDdd9/x4Ycf8umnn3L+/Hk2b97M0aNH+eSTT5g/fz7p6ens2rXLqVjCu0nt9EztrG7dBN+una6sm+A9tdNrmzCDwUB0dDTLli0jIyOD6Ohotm7dSnh4OP369ePw4cOMGTOGhg0bVhjL8eE/9thjtGjRAr1ez44dO3jjjTcYNWoUbdu25ZNPPuEvf/kLBoOh3DiX/0ErisKmTZvQ6XT07NmTgwcPsmbNGqxWKzNnzqzwSxQSEkK9evXYtGkTEyZMYP/+/ZjNZuLi4sjIyECj0VBUVER0dLRTd4eEh4ej0+kICwujXbt2pKWlkZ6ezo4dO1i1ahUzZsygfv362Gy2a75Hx3vLzc0lJSWFf//733z99delc0hat25NTExM6RyQsqxbt445c+aQn5/PunXruHDhAmFhYbRp0waz2czKlStJSEigadOmpXNWynL1Ge9NN92EVqvlq6++ol69euzfv5/du3czbtw4AgMDsdvtpWe+lysqKmLy5MnceeedPPnkk8TExHD69Glef/11tFotQ4YM4aWXXmLs2LG0bNkSnU53zTvFfvjhBzp16sQNN9xQ+h+Qdu3aoSgKzZo1Y9y4cdxyyy3Ur1//mr9nKPncWrVqxb59+9Dr9TRr1oyVK1eya9cuNmzYwAsvvFDhWfPBgwd5++23efrpp7ntttvQ6XQcP36ckJAQdDodFy5cYMWKFUybNq1SZ+DCO0nt9EztrG7dBN+una6sm+A9tdNrmzC73U5YWBh9+/ZlzZo1ZGZmEh0dTUZGBjNnzuQf//gH3bt3rzBObm4uDz30EJMmTSI+Pp5Dhw7xyiuvcP3111NUVERubi5fffUVEydOJCIiotw4OTk5vPjii2RkZBAREUHDhg3p2rUrRqOR9u3b06RJE/R6PY899hhNmza9Zk6OYeJmzZqRlpbGL7/8wsWLF5k+fTp9+vTh9ttv57777mPlypXEx8dTr169MuPYbDZMJhN+fn4AFBcXk5ycTKdOnWjWrBlHjhwhKyuL559/nrZt216x+FxFjh8/zqxZs7BYLKVzSN544w2n5pB06NCB5s2bl/5HQFVVcnJysNlsrFmzhkceeYSoqKgrJrCWpawzXoPBwK5duzh27BiHDh1i9OjRtG/f/ooFCK/muANo1KhRZGRkcO+995KXl8fRo0c5f/48MTEx9OrVi759+zo1EX/btm2kpaVx0003odfrSwtKTk4OxcXF9OzZE4PBUG6c3Nxcli5dyrFjx7DZbFgsFrp37156C3x0dDStW7fmoYceqnD4Ozc3l3//+99MnDiRzp07U79+fSIiIqhXrx6HDx8uvaxz//33V3g7vPANUjs9VzurUzfBt2tndeum4315W+302iZMURTsdjsBAQHcfPPNbNmyhffee48uXbpw55138uc//9mpOEeOHOGbb74hKiqKTp06kZSURP/+/Rk2bBhRUVF06NCBvn37lnvpyWHjxo28/fbb/Prrr2zatAmr1UpaWhpNmzYlMDCQAQMGEBcXR7NmzZx6b1Byxnr27FnmzZvH008/TYsWLbDb7eh0OrRaLX/+85/LLSIAo0ePZtWqVZw9e5aoqCgiIyNp27YtGRkZ9O7dG0VRuP322+nSpUuFf7Tnzp0rPRMymUyEh4eTkJDAihUr2L17N1OnTkWv11c4h8Txh9iyZUu6devG3r17OXLkCK1ateKbb74hMjKSu+6664rfQ3muPuNNTU3FbDbTqVMnzp8/zzPPPENsbGyF781sNvPf//6XrVu3sm7dOiIjI5kxYwaDBw9Go9EwatQo2rRp41ROUHIGZjQa0Wq1tG7dGr1eD8CsWbOIjo4mJibmmnE2btzIlClT2LRpEyaTiVWrVrF79262bt1KSkoKBw8eZMyYMU794W/ZsoVNmzbRrVu30veg0Who2bIlK1eupF+/fgwYMMDpNaCE95PaWXO101V1E3y/dla3boJ31k6vbcIcHB9Knz59OHbsGEOGDKFXr15OP79Jkyb069ePxYsX89JLL9G/f3/uv/9+oGQNkLCwMKcWBWzVqhVdu3bF39+f/Px8evToQVpaGosXL+b777+nX79+Tt3NcbVOnTqh0WhQFIWOHTuiKIpT63cVFxeTlpbGqVOn2LFjB5mZmWzevJm9e/eSl5dH586d6dOnT+nkyGt9uR1zSAoKCjh9+jQbNmwgLCyMli1b0rFjRz799FP27t3Lo48+WmFejtex2Ww0bNiQfv36sWXLFho1asSECRNKr6tXdNZ0rTPefv360bVrV1q3bl3he4OS70Dr1q2x2WwMHjyYf/zjHwC88847mEwm+vfvX+H7ulxgYCB5eXmkpqayZcuW0lhNmjTh4YcfrvD5rVq1olu3bgQFBdG0aVNeeuklBg0aRJ8+fRg5ciQ9evRwetXwiIgI2rRpw3fffcehQ4fo1q1b6fdn5cqVdOrU6ZqjFMJ3Se0sm6tqpyvr5uWv46u1s7p1E7yzdnp1E+aY5Pj++++zfPlyMjMzGT16dKXjNGjQgN69e3PixInSu0oc8w6cvTVbo9HQvHlz6tWrR2ZmJqdPn+bxxx+nb9++dO/e3an1TMrz22+/sXLlSm6//Xant8TQarV0796dsLAwNBoNfn5+3HPPPWzfvp2NGzdisVjo3bu3U7EMBgNRUVEsX76cdevWodPpyM3NJTQ0FKvVSm5uLqNGjbrmmeXVHGsTBQQEkJOTQ2FhYelt3c6uveXIrawzXsfZibOxWrRowfXXX4+qqqxevZpffvmF1NRUZs+e7XScy+NFRUXh7+/PiRMn+O2332jVqhWPPfaYU8/XaDSll2VSUlJISUkpvQwSHBzMddddV+nvZXh4ONu3b2fLli306tWLN998k+DgYO655x6n4gjfIrWzfK6qne6om+C7tbO6dRO8s3Yqqg9sDrdmzRqKi4u58cYbq7T1gIOjKK1atYq5c+dWanuGyx0/fpzly5dz9OhREhMTK5zH4IyMjAynt8i5XHFxMVu3bmXlypV07tyZ++67j/T09Erl5JgTYDKZePXVV0lNTSU6Opr69evz7bff8txzzzFgwIBK5/bpp5+yZ88efv31Vz744APCwsIq1excbv78+Vx33XXccccdlX6ug91uZ/v27XzzzTfUr1+fBx54gMaNG5cuQOgJJ06c4Ouvv+bXX38lMTGxSiMCl8dasWIFy5cvp1OnTrz11lsuzFR4I6md5atu7XRX3QSpnc7wmtqpij9YtWqVWlBQUK0YGRkZanJyslpYWOiSnOx2e5Wfa7PZ1NTUVHXixInq3LlzqxTTZrOVPufNN99UhwwZoqampqo7d+6scl5Wq1U9efKkmpGRUfpzVSUnJ6ujR49WLRZLlWNczvF+Hf/rSa78LmVmZqqLFi1STSaTCzIT4kpSO//4fMfxrqqbqiq101neUDt9YiSstlKreGbiLsePH8fPz8+pCa5Xu/q9PPXUUzz00ENOX1+vCVU94y1LbfvsXJlPbXtvQlyttn1Hq1o7vaFugtROT8Ry0Lk0mrhCbfoiQsmkxapyzCFZuHAhx48fx2Qy1bpC4sqV3mvbZ+fKfGrbexPiarXtO1rV2ukNdROkdnoiloM0YcJpBoOBtm3b0qJFi1q5snpt++MXQojaXjdBaqcnyeVIIYQQQggPcO6eXSGEEEII4VLShAkhhBBCeIA0YUIIIYQQHiBNmBBCCCGEB8jdkcIlUlJSGDduHO3atUNVVaxWK/fffz+33XZbmcefOXOGAwcOVHnFaCGE8AVSO+s2acKEyyQkJPD6668DkJ+fz8iRI4mMjCQ6OvoPxxqNRn777TcpJEKIOk9qZ90lTZhwi6CgIO655x6+/fZbPvnkE86dO0dubi79+vVj7NixzJ8/n8LCQrp160ZERAQvvvgiAKGhocycOZOQkBAPvwMhhKh5UjvrFpkTJtymUaNG7N+/n65du/LBBx/w2Wef8dlnn6HVavm///s/hgwZws0338yUKVOYOnUqH3/8Mf369eP999/3dOpCCOExUjvrDhkJE25z5swZunXrxt69ezEajQQHB1NcXPyH444cOUJSUhIAFouFyMjImk5VCCFqDamddYc0YcItTCYTS5Ys4e6778ZsNvPCCy9w/PhxkpOTUVUVjUaD3W4HIDIykpdffpnw8HC2b99OZmamh7MXQgjPkNpZt0gTJlzGaDQycuRINBoNNpuNsWPHEhkZyfjx49m+fTsBAQG0atWKjIwMOnTowDvvvENMTAzTpk1j0qRJ2Gw2AGbMmOHhdyKEEDVHamfdJXtHCiGEEEJ4gEzMF0IIIYTwAGnChBBCCCE8QJowIYQQQggPkCZMCCGEEMIDpAkTQgghhPAAacKEEEIIITxAmjAhhBBCCA+QJkwIIYQQwgP+HyjyieNNrzoeAAAAAElFTkSuQmCC\n",
      "text/plain": [
       "<Figure size 720x576 with 2 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'July', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']\n",
    "# Left plot Netflix\n",
    "plt.figure(figsize = (10, 8))\n",
    "ax1 = plt.subplot(1, 2, 1)\n",
    "\n",
    "plt.plot(netflix_stocks['Date'], netflix_stocks['Price'], marker = 'o', color = 'red')\n",
    "\n",
    "ax1.set_title('Netflix')\n",
    "ax1.set_xlabel('Date')\n",
    "ax1.set_ylabel('Stock Price')\n",
    "ax1.set_xticklabels(months, rotation = 50)\n",
    "\n",
    "# Right plot Dow Jones\n",
    "ax2 = plt.subplot(1, 2, 2)\n",
    "\n",
    "plt.plot(dowjones_stocks['Date'], dowjones_stocks['Price'], marker = 'o', color = 'blue')\n",
    "\n",
    "ax2.set_title('Dow Jones')\n",
    "ax2.set_xlabel('Date')\n",
    "ax2.set_ylabel('Stock Price')\n",
    "ax2.set_xticklabels(months, rotation = 50)\n",
    "\n",
    "\n",
    "plt.subplots_adjust(wspace = .5)\n",
    "\n",
    "plt.savefig('Step 8 new.jpg')\n",
    "plt.show()\n",
    "\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "- How did Netflix perform relative to Dow Jones Industrial Average in 2017?\n",
    "- Which was more volatile?\n",
    "- How do the prices of the stocks compare?"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    " "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Step 9\n",
    "\n",
    "It's time to make your presentation! Save each of your visualizations as a png file with `plt.savefig(\"filename.png\")`.\n",
    "\n",
    "As you prepare your slides, think about the answers to the graph literacy questions. Embed your observations in the narrative of your slideshow!\n",
    "\n",
    "Remember that your slideshow must include:\n",
    "- A title slide\n",
    "- A list of your visualizations and your role in their creation for the \"Stock Profile\" team\n",
    "- A visualization of the distribution of the stock prices for Netflix in 2017\n",
    "- A visualization and a summary of Netflix stock and revenue for the past four quarters and a summary\n",
    "- A visualization and a brief summary of their earned versus actual earnings per share\n",
    "- A visualization of Netflix stock against the Dow Jones stock (to get a sense of the market) in 2017\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<Figure size 432x288 with 0 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
