#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()


# In[3]:


sys = pd.read_csv(r"D:\Stock Market\Dataset\AXISBANK.csv")
sys.head()


# In[4]:


def show_dfaxis():
    return sys.head()


# In[ ]:





# In[5]:


sys['Date'] = pd.to_datetime(sys.Date)
sys = sys.set_index('Date')
sys['Close'].plot(legend = True)


# In[6]:


def ClosingAxisPlot():
    return sys['Close'].plot(legend = True)


# In[7]:


days = 50
col_name = "MV avg for "+str(days)+" days"
sys[col_name] = sys['Close'].rolling(days).mean()
print(sys)
sys[['Close','MV avg for 50 days']].plot()


# In[8]:


def MovingAVG_AXIS(x):
    days = x
    col_name = "MV avg for "+str(days)+" days"
    sys[col_name] = sys['Close'].rolling(days).mean()
    return sys[['Close',f'MV avg for {days} days']].plot()
    


# In[9]:


MovingAVG_AXIS(10)


# In[ ]:





# In[10]:


daily_returns = sys['Close'].pct_change()
sys['daily_returns'] = daily_returns
plt.ylabel("Percentage Change")
sys['daily_returns'].plot(legend = True)


# In[11]:


sys


# In[12]:


plot =sns.displot(sys['daily_returns'].dropna())
plot.set_ylabels("Probability Density Value")


# In[13]:


sys_HDFC = pd.read_csv(r"C:\Users\91881\Dropbox\My PC (LAPTOP-O9H6PI79)\Downloads\NIFTY data\HDFCBANK.csv")
sys_HDFC.head()


# In[14]:


sys_HDFC['Date']= pd.to_datetime(sys_HDFC.Date)
sys_HDFC = sys_HDFC.set_index('Date')
sys_HDFC['Close'].plot(legend = True)


# In[15]:


def Closing_HDFC():
    return sys_HDFC['Close'].plot(legend = True) 


# In[16]:


Closing_HDFC()


# In[ ]:





# In[ ]:





# In[ ]:





# In[17]:


days = 50
col_name = "MV avg for "+str(days)+" days"
sys_HDFC[col_name] = sys_HDFC['Close'].rolling(days).mean()
print(sys_HDFC)
sys_HDFC[['Close','MV avg for 50 days']].plot()


# In[18]:


def MovingAVG_HDFC(x):
    days = x
    col_name = "MV avg for "+str(days)+" days"
    sys_HDFC[col_name] = sys_HDFC['Close'].rolling(days).mean()
    return sys_HDFC[['Close',f'MV avg for {days} days']].plot()


# In[19]:


MovingAVG_HDFC(100)



# In[ ]:





# In[ ]:





# In[20]:


daily_returns = sys_HDFC['Close'].pct_change()
sys_HDFC['daily_returns'] = daily_returns
plt.ylabel("Percentage Change")
sys_HDFC['daily_returns'].plot(legend = True)


# In[21]:


plot2 =sns.displot(sys_HDFC['daily_returns'].dropna())
plot2.set_ylabels("Probability Density Value")


# In[22]:


sys_ICICI = pd.read_csv(r"C:\Users\91881\Dropbox\My PC (LAPTOP-O9H6PI79)\Downloads\NIFTY data\ICICIBANK.csv")
sys_ICICI.head()


# In[23]:


sys_ICICI['Date'] = pd.to_datetime(sys_ICICI.Date)
sys_ICICI = sys_ICICI.set_index('Date')
sys_ICICI['Close'].plot(legend = True)


# In[24]:


def Closing_ICICI():
    return sys_ICICI['Close'].plot(legend = True)


# In[25]:


Closing_ICICI()


# In[ ]:





# In[ ]:





# In[ ]:





# In[26]:


days = 50
col_name = "MV avg for "+str(days)+" days"
sys_ICICI[col_name] = sys_ICICI['Close'].rolling(days).mean()
print(sys_ICICI)
sys_ICICI[['Close','MV avg for 50 days']].plot()


# In[27]:


def MovingAVG_ICICI(x):
    days = x
    col_name = "MV avg for "+str(days)+" days"
    sys_ICICI[col_name] = sys_ICICI['Close'].rolling(days).mean()
    return sys_ICICI[['Close',f'MV avg for {days} days']].plot()


# In[28]:


MovingAVG_ICICI(365)



# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[29]:


daily_returns = sys_ICICI['Close'].pct_change()
sys_ICICI['daily_returns'] = daily_returns
plt.ylabel("Percentage Change")
sys_ICICI['daily_returns'].plot(legend = True)


# In[30]:


plot3 =sns.displot(sys_ICICI['daily_returns'].dropna())
plot3.set_ylabels("Probability Density Value")


# In[31]:


sys_KMB = pd.read_csv(r"C:\Users\91881\Dropbox\My PC (LAPTOP-O9H6PI79)\Downloads\NIFTY data\KOTAKBANK.csv")
sys_KMB.head()


# In[32]:


sys_KMB['Date'] = pd.to_datetime(sys_KMB.Date)
sys_KMB = sys_KMB.set_index('Date')
sys_KMB['Close'].plot(legend = True)


# In[33]:


def Closing_KMB():
    return sys_KMB['Close'].plot(legend = True)


# In[34]:


Closing_KMB()


# In[ ]:





# In[ ]:





# In[35]:


days = 50
col_name = "MV avg for "+str(days)+" days"
sys_KMB[col_name] = sys_KMB['Close'].rolling(days).mean()
print(sys_KMB)
sys_KMB[['Close','MV avg for 50 days']].plot()


# In[36]:


def MovingAVG_KMB(x):
    days = x
    col_name = "MV avg for "+str(days)+" days"
    sys_KMB[col_name] = sys_KMB['Close'].rolling(days).mean()
    return sys_KMB[['Close',f'MV avg for {days} days']].plot()


# In[37]:


MovingAVG_KMB(365)


# In[ ]:





# In[ ]:





# In[ ]:





# In[38]:


daily_returns = sys_KMB['Close'].pct_change()
sys_KMB['daily_returns'] = daily_returns
plt.ylabel("Percentage Change")
sys_KMB['daily_returns'].plot(legend = True)


# In[39]:


plot4 =sns.displot(sys_KMB['daily_returns'].dropna())
plot4.set_ylabels("Probability Density Value")


# In[40]:


df = pd.DataFrame({'AxisBank':sys['Close'],
                  'HDFC Bank':sys_HDFC['Close'],
                  'ICICI Bank':sys_ICICI['Close'],
                  'Kotak Mahindra Bank':sys_KMB['Close']})
df


# In[41]:


corr = df.dropna().corr()
print(corr)
sns.heatmap(corr,annot = True,vmax=1,vmin=-1)
#plt.show()


# In[ ]:





# In[ ]:





# In[42]:


df2 = pd.DataFrame({'Axis Bank':sys['daily_returns'],
                   'HDFC Bank':sys_HDFC['daily_returns'],
                   'ICICI Bank':sys_ICICI['daily_returns'],
                   'Kotak Mahindra Bank':sys_KMB['daily_returns']})
df2


# In[43]:


corr2 = (df2.dropna()).corr()
sns.heatmap(corr2,annot=True,vmax=1,vmin=-1)


# In[ ]:





# In[ ]:





# In[44]:


all_returns = df.pct_change()
investment = 1000000
loss = (abs(all_returns.quantile(0.1)))*investment
print(loss)


# In[ ]:





# In[ ]:





# In[45]:


import numpy as np


# In[46]:


daily_returns = sys['Close'].pct_change()
log_returns = np.log(1+daily_returns)
avg = log_returns.mean()
var = log_returns.var()
drift = avg-(var/2)
drift = np.array(drift)
print(drift)


# In[ ]:





# In[47]:


from scipy.stats import norm
pred_price_overDays = 60
pred_count = 10
std = log_returns.std()
std = np.array(std)
x = np.random.rand(pred_price_overDays,pred_count)
Rv = std*norm.ppf(x)
print(Rv)


# In[48]:


e_value = np.exp(drift+Rv)
current_price = sys['Close'].iloc[-1]
new_prices = np.zeros_like(e_value)
new_prices[0] = current_price
print(new_prices)

for i in range(1,pred_price_overDays):
    new_prices[i]=new_prices[i-1]*e_value[i]
    
print("Minimum:",new_prices[pred_price_overDays-1].min())
print("Maximum:",new_prices[pred_price_overDays-1].max())


print(new_prices)


# In[65]:


print("Minimum:",new_prices[pred_price_overDays-1].min().round(2))
print("Maximum:",new_prices[pred_price_overDays-1].max().round(2))
plt.xlabel('Days')
plt.ylabel('Price')
plt.title("Monte Carlo Analysis for system")
plt.plot(new_prices)


# In[78]:


def future_trends_AXIS():
    return str(f'The maximum price will be :{new_prices[pred_price_overDays-1].max().round(2)}') + str(f' and The minimum price will be :{new_prices[pred_price_overDays-1].min().round(2)}')


# In[79]:


def all_curves_AXIS():
    plt.xlabel('Days')
    plt.ylabel('Price')
    plt.title("Monte Carlo Analysis for system")
    return plt.plot(new_prices)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[51]:


daily_returns1 = sys_HDFC['Close'].pct_change()
log_returns1 = np.log(1+daily_returns1)
avg1 = log_returns1.mean()
var1 = log_returns1.var()
drift1 = avg1-(var1/2)
drift1 = np.array(drift1)
print(drift1)


# In[52]:


from scipy.stats import norm
pred_price_overDays = 60
pred_count = 10
std1 = log_returns1.std()
std1 = np.array(std1)
x1 = np.random.rand(pred_price_overDays,pred_count)
Rv1 = std*norm.ppf(x1)
print(Rv1)


# In[53]:


e_value1 = np.exp(drift1+Rv1)
current_price1 = sys_HDFC['Close'].iloc[-1]
new_prices1 = np.zeros_like(e_value1)
new_prices1[0] = current_price1
print(new_prices1)

for i in range(1,pred_price_overDays):
    new_prices1[i]=new_prices1[i-1]*e_value1[i]
    
print("Minimum:",new_prices1[pred_price_overDays-1].min())
print("Maximum:",new_prices1[pred_price_overDays-1].max())


print(new_prices1)


# In[54]:


print("Minimum:",new_prices1[pred_price_overDays-1].min())
print("Maximum:",new_prices1[pred_price_overDays-1].max())

plt.xlabel('Days')
plt.ylabel('Price')
plt.title("Monte Carlo Analysis for system")
plt.plot(new_prices1)


# In[82]:


def future_trends_HDFC():
    return str(f'The maximum value will be :{new_prices1[pred_price_overDays-1].max().round(2)}') + str(f' and The minimum value will be :{new_prices1[pred_price_overDays-1].min().round(2)}')


# In[84]:


def all_curves_HDFC():
    plt.xlabel('Days')
    plt.ylabel('Price')
    plt.title("Monte Carlo Analysis for system")
    return plt.plot(new_prices1)


# In[ ]:





# In[55]:


daily_returns2 = sys_ICICI['Close'].pct_change()
log_returns2 = np.log(1+daily_returns2)
avg2 = log_returns2.mean()
var2 = log_returns2.var()
drift2 = avg2-(var2/2)
drift2 = np.array(drift2)
print(drift2)


# In[56]:


from scipy.stats import norm
pred_price_overDays = 60
pred_count = 10
std2 = log_returns2.std()
std2 = np.array(std2)
x2 = np.random.rand(pred_price_overDays,pred_count)
Rv2 = std*norm.ppf(x2)
print(Rv2)


# In[57]:


e_value2 = np.exp(drift2+Rv2)
current_price2 = sys_ICICI['Close'].iloc[-1]
new_prices2 = np.zeros_like(e_value2)
new_prices2[0] = current_price2
print(new_prices2)

for i in range(1,pred_price_overDays):
    new_prices2[i]=new_prices2[i-1]*e_value2[i]
    
print("Minimum:",new_prices2[pred_price_overDays-1].min())
print("Maximum:",new_prices2[pred_price_overDays-1].max())


print(new_prices2)


# In[58]:


print("Minimum:",new_prices2[pred_price_overDays-1].min())
print("Maximum:",new_prices2[pred_price_overDays-1].max())

plt.xlabel('Days')
plt.ylabel('Price')
plt.title("Monte Carlo Analysis for system")
plt.plot(new_prices2)


# In[86]:


def future_trends_ICICI():
    return str(f'The maximum value will be :{new_prices2[pred_price_overDays-1].max().round(2)}') + str(f' and The minimum value will be :{new_prices2[pred_price_overDays-1].min().round(2)}')


# In[88]:


def all_curves_ICICI():
    plt.xlabel('Days')
    plt.ylabel('Price')
    plt.title("Monte Carlo Analysis for system")
    return plt.plot(new_prices2)


# In[ ]:





# In[ ]:





# In[59]:


daily_returns3 = sys_KMB['Close'].pct_change()
log_returns3 = np.log(1+daily_returns3)
avg3 = log_returns3.mean()
var3 = log_returns3.var()
drift3 = avg3-(var3/2)
drift3 = np.array(drift3)
print(drift3)


# In[60]:


from scipy.stats import norm
pred_price_overDays = 60
pred_count = 10
std3 = log_returns3.std()
std3 = np.array(std3)
x3 = np.random.rand(pred_price_overDays,pred_count)
Rv3 = std*norm.ppf(x3)
print(Rv3)


# In[61]:


e_value3 = np.exp(drift3+Rv3)
current_price3 = sys_KMB['Close'].iloc[-1]
new_prices3 = np.zeros_like(e_value3)
new_prices3[0] = current_price3
print(new_prices3)

for i in range(1,pred_price_overDays):
    new_prices3[i]=new_prices3[i-1]*e_value3[i]
    

print(new_prices3)


# In[62]:


print("Minimum:",new_prices3[pred_price_overDays-1].min())
print("Maximum:",new_prices3[pred_price_overDays-1].max())

plt.xlabel('Days')
plt.ylabel('Price')
plt.title("Monte Carlo Analysis for system")
plt.plot(new_prices3)


# In[90]:


def future_trends_KMB():
    return str(f'The maximum value will be :{new_prices3[pred_price_overDays-1].max().round(2)}') + str(f' and The minimum value will be :{new_prices3[pred_price_overDays-1].min().round(2)}')


# In[92]:


def all_curves_KMB():
    plt.xlabel('Days')
    plt.ylabel('Price')
    plt.title("Monte Carlo Analysis for system")
    return plt.plot(new_prices3)


# In[ ]:




