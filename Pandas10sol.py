#1484. Group Sold Products By The Date
import pandas as pd

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    mydictionary = {}
    for i in range (len(activities)):
        sell_date = activities['sell_date'][i]
        product = activities['product'][i]
        if sell_date not in mydictionary:
            mydictionary[sell_date] = set()
        mydictionary[sell_date].add(product)
    result = []
    for key,value in mydictionary.items():
        temp = []
        for product in value:
            temp.append(product)
        temp.sort()
        s - ""
        for i in range(len(temp)):
            s = s + temp[i]
            if i != len(temp) - 1:
                s = s + ','
        result.append([key, len(value),s])
    df = pd.DataFrame(result, columns =['sell_date', 'num_sold', 'product'])
    df.sort_values(by='sell_date', inplace=True)  
    return df



import pandas as pd

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    groups = activities.groupby(['sell_date'])
    result = groups.agg(
        num_sold=('product', 'nunique'), 
        products=('product', lambda x: ','.join(sorted(set(x))))
    ).reset_index()
    result.sort_values(by=['sell_date'], inplace=True)
    return result


#1693. Daily Leads and Partners
import pandas as pd

def daily_leads_and_partners(daily_sales: pd.DataFrame) -> pd.DataFrame:
    df = daily_sales.groupby(['date_id','make_name']).agg({
        'lead_id' : pd.Series.nunique,
        'partner_id' : pd.Series.nunique
    }).reset_index()  
    result = df.rename(columns={'lead_id' : 'unique_leads', 'partner_id' : 'unique_partners'})  
    return result


import pandas as pd

def daily_leads_and_partners(daily_sales: pd.DataFrame) -> pd.DataFrame:
    # Grouping by date_id and make_name and aggregating the lead_ids and partner_ids into lists
    grouped = daily_sales.groupby(['date_id', 'make_name']).agg({
        'lead_id': lambda x: list(x),
        'partner_id': lambda x: list(x)
    }).reset_index()
    
    # Function to count unique elements in a list
    def count_unique(lst):
        return len(set(lst))
    
    # Applying the count_unique function to lead_id and partner_id columns
    grouped['unique_leads'] = grouped['lead_id'].apply(count_unique)
    grouped['unique_partners'] = grouped['partner_id'].apply(count_unique)
    
    # Dropping the lead_id and partner_id columns
    grouped.drop(['lead_id', 'partner_id'], axis=1, inplace=True)
    
    return grouped


