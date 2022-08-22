'''
 --> Name:- Varij Rughani
 --> Creating a CLI application using argparse to get userinput from terminal and 
     it will show to get data from db and show on terminal & then it creates a histogram if option -p is given to it 
'''

import sqlite3
import argparse
import matplotlib.pyplot as mtpt
from collections import Counter

    #Class Final_Project declared
class Final_Project: 
    def __init__(data,args):
        data.db=args.d
        data.statement=args.s
        data.conn = sqlite3.connect(data.db)
        data.cursor_obj = data.conn.cursor()
        
    #Function to fetch data using query 
    def get_data(data):
        data.cursor_obj.execute(data.statement)
        result = data.cursor_obj.fetchall()
        return result
        
    #Function to show data     
    def show_table(data):
        result =data.get_data()   
        for row in result:
            try:
                # For adding and removing spaces in code
                l1=20-int(len(row[1]))
                sp1=" "*l1
                l=20-int(len(row[0]))
                sp=" "*l
                # Using f string to print data that is fetched
                print(f"{row[0]} {sp} {row[1]} {sp1}   {row[2]}")  
            except:
                print(row)
            
       
    #Function for Histrogram
    def make_hist(data):
        result =data.get_data()
        li=[]
        for row in result:
            li.append(row[2])  
        print(Counter(li))   
        ''' 
        Creating  histogram adding color to bar,title,
        x and y axis label,
        saving png
        '''
        mtpt.hist(li,color='#0612aa',rwidth = 10, bins =20)
        mtpt.title("Histogram for each invoice with number of occurrences") #Histogram's heading
        mtpt.ylabel('(Frequency / Count)') #For Y label
        mtpt.xlabel('Invoice Value')  #For X label
        mtpt.savefig('histogram.png') #Saving Histogram in png format
        mtpt.show()

 # Main Function
def main():  
    #creating argument parser
    p_args = argparse.ArgumentParser(description='Please provide database file path and query.')     
    
    #Adding histogram which is optional  
    p_args.add_argument('-p', '--simulate', action='store_true', help=" Histogram ")  
    
    #Adding and parsing arguments 1 for Db name
    p_args.add_argument('-d', type=str, required=True, help="Provide Database name with complete path ")
    
    #Adding and parsing arguments 2 for Sql query
    p_args.add_argument('-s', type=str, default=2, help=" Provide valid Sql Query ")
    
    args = p_args.parse_args()
  
    try:
        d1=Final_Project(args)  
        # checking option -p is working or not 
        if args.simulate == True:  
            #if -p is called then Histogram will be shown
            d1.make_hist()         
        else:
            #if -p is not called then only data table will be shown
            d1.show_table() 
    except Exception as e:
        print(e)           
if __name__ == "__main__":
    main()
    
