# Importing the required libraries
import streamlit as sl
import yahoo_fin.stock_info as st_info
import pandas_datareader as pdr

# Creating the header in the streamlit Header
sl.header('Benjamin Graham Stock Valuation Calculator')

# Creating Input Field for the parameter and setting default values
ticker = sl.text_input('Stock Ticker', 'INFY.NS')
zg_pe = sl.text_input('Zero Growth PE Ratio', '6')
growth_multi = sl.text_input('Growth Multiplier', '1.5')
margin = sl.text_input('Safety Margin (%)', '30')

# Scraping the required data from yahoo finance and fred page
# Utilizing the Python yahoo-fin and pandas-datareader APIs to automatically scrape the target data

def get_target_data(ticker, zg_pe, growth_multi, margin):
    # using get_quote_table to get stock price and EPS
    quote = st_info.get_quote_table(ticker)
    current_st_price = quote['Quote Price']
    eps = quote['EPS (TTM)']
    # Similarly using get_analysis_info to get growth estimate
    growth_df = st_info.get_analysts_info(ticker)['Growth Estimates']
    # getting the growth estimate and cleaning it
    growth_rate = growth_df.iloc[4][1]
    growth_rate = growth_rate.rstrip('%')
    # Obtain the latest current yield of the AAA Corporate Bond using Pandas data-reader get_data_fred()
    aaa_bond_df = pdr.get_data_fred('AAA')
    current_yield = aaa_bond_df.iloc[-1][0]

    output_data = {
        'current_price': float(current_st_price),
        'eps': float(eps),
        'growth_rate': float(growth_rate),
        'current_yield': float(current_yield),
        'zg_pe': float(zg_pe),
        'growth_multi': float(growth_multi),
        'margin': float(margin)
        }
    return output_data

# Processing the parameters to calculate the intrinsic value of a target stock
target_data = {}
if sl.button('Calculate'):
    # Getting the target data by calling the function
    target_data = get_target_data(ticker, zg_pe, growth_multi, margin)
    # Creating a de-marking line
    sl.markdown('''---''')
    # Creating the 3 columns to show the targeted data
    col1, col2, col3 = sl.columns(3)
    with col1:
        sl.metric(label="EPS($)", value=target_data['eps'])
    with col2:
        sl.metric(label="Projected Growth Rate (5 Yr)(%)", value=target_data['growth_rate'])
    with col3:
        sl.metric(label="Current Yield of AAA Corp Bond(%)", value=target_data['current_yield'])

    sl.markdown('''---''')
    # Calculating the intrinsic value of the stock using the benjamin graham formula
    intr_st_val = (target_data['eps'] * (target_data['zg_pe'] + target_data['growth_multi']*target_data['growth_rate']) * 4.4)/(target_data['current_yield'])
    intr_st_val = round(intr_st_val,2)
    stock_price = round(target_data['current_price'],2)
    margin_rate = target_data['margin']/100
    # Calculate the acceptable buy price based on the margin rate (must be divided by 100 to use in the below formula)
    accept_price = round((1-margin_rate) * intr_st_val, 2)

    # Showing the caclulated values
    col4, col5, col6 = sl.columns(3)
    with col4:
        sl.subheader('Current Stock Price($)')
        sl.subheader('**:pink[' + str(stock_price)+']**')
    with col5:
        sl.subheader('Intrinsic Stock Value($)')
        sl.subheader('**:pink[' + str(intr_st_val) + ']**')
    with col6:
        sl.subheader('Acceptable Price to Buy($)')
        sl.subheader('**:pink[' + str(accept_price) + ']**')
else:
    sl.text('Click on the Calculate button')


