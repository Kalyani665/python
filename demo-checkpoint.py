{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 305,
   "id": "66f2b914",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:xlabel='yyyy'>"
      ]
     },
     "execution_count": 305,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAXAAAAEbCAYAAADDKt+mAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjMuNCwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8QVMy6AAAACXBIWXMAAAsTAAALEwEAmpwYAAAlA0lEQVR4nO3deZxU5ZX/8c+BpsWWHZq1wUYEWZodlbig0YFBZDSAC4gxRgij/nDJYsDxZ0Z0GHBFJEaDskRlwIyKLAGiISzGUZmWnQCCitKIAq0IoYUGPPNHVe97V/Vyq7/v14sXXfc+t+rU6arT9z73uc81d0dERIKnVlUHICIi5aMCLiISUCrgIiIBpQIuIhJQKuAiIgGlAi4iElBxlflizZo18+Tk5Mp8SRGRwPvwww8PuXti/uWVWsCTk5NJTU2tzJcUEQk8M/ussOXqQhERCSgVcKkxbrvtNpo3b05KSkqBdU888QRmxqFDh4rc/vTp0/Tu3ZuhQ4dmL7vvvvvo3LkzPXr0YNiwYRw+fLgiQhcplAq41Bi33norK1asKLB87969vP3227Rr167Y7adPn06XLl3yLBs4cCBbt25l8+bNdOrUiSlTpkQ1ZpHiVGofuEhVGjBgAHv27Cmw/Oc//zmPPfYY1157bZHbpqWl8ac//YkHHniAp556Knv5oEGDsn/u378/r732WlRjrslOnjxJWloax48fr+pQKk3dunVJSkqiTp06pWqvAi412uLFi2nTpg09e/Ystt29997LY489xtGjR4tsM3v2bG688cZoh1hjpaWlUb9+fZKTkzGzqg6nwrk76enppKWl0b59+1Jtoy4UqbEyMjKYPHkyDz/8cLHtli5dSvPmzenbt2+RbSZPnkxcXByjR4+Odpg11vHjx2natGmNKN4AZkbTpk3LdMShAi411scff8ynn35Kz549SU5OJi0tjT59+vDll1/maffuu++yePFikpOTGTlyJH/961+5+eabs9f/4Q9/YOnSpcybN6/GFJvKUtPyWdb3qwIuNVb37t05cOAAe/bsYc+ePSQlJbF+/XpatmyZp92UKVNIS0tjz549LFiwgCuuuIJXXnkFgBUrVvDoo4+yePFiEhISquJtSAU5fPgwv/vd76o6jGKpD1xiQvLEP5XY5uDixzjx+RZOf3eEuPrNaHjJaOr3DJ2E3DP16jxtv/jiC8aOHcuyZcuKfc7x48dz4sQJBg4cCIROZD7//PPlfBdSnNL8jssi/+88v6wCfuedd0b1daNJBVxqjMRrfl3s+twjVFq3bl1o8b788su5/PLLsx/v3r07WuFJNTNx4kQ+/vhjevXqRZ06dUhISKBFixZs3LiR4cOH0717d6ZPn853333Hm2++SYcOHViyZAn/8R//QWZmJk2bNmXevHm0aNGCu+++m2bNmvGb3/yGP//5z0yePJnVq1dTq1ZknSDqQhERKcTUqVPp0KEDGzdu5PHHH2fTpk1Mnz6dLVu28PLLL/PRRx+xbt06xo4dy4wZMwC45JJLeP/999mwYQMjR47ksccey36uV199lVWrVnH33XczZ86ciIs3lGIP3MxmA0OBA+6ekm/dr4DHgUR3L/oSNhGRgDv//PNp1aoVAB06dMi+BqB79+6sWrUKCA19vPHGG9m/fz+ZmZnZwwETEhJ44YUXGDBgANOmTaNDhw5Riak0fwLmAoPzLzSztsBA4POoRCIiUgX27NnDxo0b2bZtW/ayffv28dFHH3HixAk++ugjTp48yRlnnJG9vlatWpxxxhmcOnWK/fv3880337B161buvPNOxo8fz5YtW/j973+fZ0jgli1baNq0KV988UXUYi+xgLv7WuDrQlZNA34N6Lb2IhJYTZs2pWPHjnmWtWzZkr59+5KZmUnDhg1JT08vdNu9e/dy1llnUb9+fbp27crRo0dp06YNEBpemuWzzz7jySefZMOGDSxfvpwPPvggKrGXqxPGzK4B9rn7plK0HWdmqWaWevDgwfK8nIhEWWETez344IP06NGDXr16MWjQoGL3FAub2OvGG2+kV69e9OrVi+TkZHr16lWRbyFq6tevT1xc3t7k2rVr07RpUy6++GIuu+yyQue4OX36NEePHqVhw4ZAaK980qRJXH/99Vx66aU0a9YMCF1hOWbMGJ544glat27NrFmzGDt2bFSmCDD3knegzSwZWOruKWaWAKwCBrn7t2a2B+hXmj7wfv36ueYDl4oQ6RCzkoaUxZq1a9dSr149brnlFrZu3QrAkSNHaNCgAQDPPPMMf//734scEvnUU0+RmprKkSNHWLp0aYH1v/zlL2nYsCG/+c1vyh3j9u3bC0weVlFOnDjB7t276datW/ayffv2kZ6eTu3atenUqVOB+UkyMjL47LPPqFu3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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "import pandas as pd \n",
    "import re\n",
    "\n",
    "input_file1= open(\"C:\\\\Users\\\\hp\\\\Desktop\\\\Kalyani\\\\Python\\\\data.txt\", \"rt\")\n",
    "output_file1= open(\"C:\\\\Users\\\\hp\\\\Desktop\\\\Kalyani\\\\Python\\\\outputfile1.txt\",\"wt\")\n",
    "\n",
    "for line in input_file1:\n",
    "   line=(re.sub(' +','\\t',line.strip()) ) +'\\n'\n",
    "   output_file1.write(line)\n",
    "\n",
    "input_file1.close()\n",
    "output_file1.close()\n",
    "\n",
    "output_file1 = pd.read_csv(\"C:\\\\Users\\\\hp\\\\Desktop\\\\Kalyani\\\\Python\\\\outputfile1.txt\",  delimiter = '\\t')\n",
    "output_file1.to_csv('C:\\\\Users\\\\hp\\\\Desktop\\\\Kalyani\\\\Python\\\\data_csv.csv', index = None)\n",
    "\n",
    "#print(output_file1['yyyy'][0:15] )  print( output_file1['mm'][0:12])\n",
    "new_df= pd.DataFrame(columns =output_file1.keys())\n",
    "\n",
    "x=0\n",
    "y=11\n",
    "\n",
    "def argxy(x,y):\n",
    "    arg= output_file1.loc[x:y]\n",
    "    return(arg_var)\n",
    "     \n",
    "def avg(arg):\n",
    "    yr=int(output_file1['yyyy'][x:y].mean())\n",
    "    avg_tmax=float(output_file1['tmax'][x:y].mean())\n",
    "    avg_tmin=float(output_file1['tmin'][x:y].mean())\n",
    "    avg_af=float(output_file1['af'][x:y].mean())\n",
    "    avg_rain=float(output_file1['rain'][x:y].mean())\n",
    "    #avg_sun=float(output_file1['sun'][x:y].mean())\n",
    "    \n",
    "    new_row = {'yyyy':yr, 'mm':12, 'tmax':avg_tmax, 'tmin':avg_tmin, 'af':avg_af,'rain':avg_rain,'sun':12}\n",
    "    return new_row\n",
    " \n",
    "for i in range(5):\n",
    "    arg_var=argxy(x,y)\n",
    "    x=y+1\n",
    "    y=x+11\n",
    "    new_row=avg(arg_var)\n",
    "    new_df=new_df.append(new_row, ignore_index=True)\n",
    "\n",
    "import matplotlib.pyplot as plt\n",
    "fig, ax = plt.subplots()\n",
    "\n",
    "new_df.plot.bar(x = 'yyyy', y = ['tmax', 'tmin'], rot = 40, ax = ax)\n",
    "for p in ax.patches: \n",
    "    ax.annotate(np.round(p.get_height(),decimals=2), (p.get_x()+p.get_width()/2., p.get_height()))\n",
    "\n",
    "new_df.plot(x=\"yyyy\", y=\"af\", kind=\"bar\")\n",
    "new_df.plot(x=\"yyyy\", y=\"rain\", kind=\"bar\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2d1d2fed",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "218e00cb",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "75a310df",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b6f6fc03",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ecbe1ed4",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ee3d89e1",
   "metadata": {},
   "outputs": [],
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
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
