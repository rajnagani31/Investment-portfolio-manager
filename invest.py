import json

# load data
def load_data():
    try:
        with open('portfolio.txt',"r")as file:
            read=json.load(file)
            return read
        
    except FileNotFoundError:
        return []    


# show data


def show_all_data(data):
    print("+---------------------------------+")
    print("| select data According your need |")
    print("+---------------------------------+")

    print("\n\n")

    print("1.show all data.")
    print("2.show selected data.")
    choice=int(input("Enter a your choice:"))

    # data selcetion and show logic
    
    
    # 1.according user


    if choice == 1:
        print("+-------------------------------------------------------------+")
        print(f"| {'month':<8}{'Type':<8}{'amount':<10}{'value':<10}{'Gain Amount':<13}{'Gain(%)':<10} |")
        print("+-------------------------------------------------------------+")

        for datas in data:
            month=datas['month']
            types=datas['type']
            values=datas['values']
            gains=datas["gain amount"]
            gains_per=datas['gain_percentage']

            first=True
            for invest_type,amount in types.items():
                value=values.get(f"{invest_type}_value","")
                gain_amount=gains.get(f"{invest_type} gain","")
                gain_per=gains_per.get(f"{invest_type} gain_percentage","")

                if first:
                    print(f"| {month:<8}{invest_type:<10}{amount:<10}{value:<10}{gain_amount:<10}{gain_per:<10.2f}  |")
                    first=False
                else:
                    print(f"| {"":<8}{invest_type:<10}{amount:<10}{value:<10}{gain_amount:<10}{gain_per:<10.2f}  |")
            print("+-------------------------------------------------------------+")

                
           
    elif choice == 2:
    
        select=input("Enter month name for show data (eg..jan,feb,):")
        found=False
        for index,datas in enumerate(data,start=1):

            if datas['month'] == select:
                print("+-------------------------------------------------------------+")
                print(f"| {'month':<8}{'Type':<8}{'amount':<10}{'value':<10}{'Gain Amount':<13}{'Gain(%)':<10} |")
                print("+-------------------------------------------------------------+")

                
                month=datas['month']
                types=datas['type']
                values=datas['values']
                gains=datas["gain amount"]
                gains_per=datas['gain_percentage']

                first=True
                for invest_type,amount in types.items():
                    value=values.get(f"{invest_type}_value","")
                    gain_amount=gains.get(f"{invest_type} gain","")
                    gain_per=gains_per.get(f"{invest_type} gain_percentage","")

                    if first:
                        print(f"| {month:<8}{invest_type:<10}{amount:<10}{value:<10}{gain_amount:<10}{gain_per:<10.2f}  |")
                        first=False
                    else:
                        print(f"| {"":<8}{invest_type:<10}{amount:<10}{value:<10}{gain_amount:<10}{gain_per:<10.2f}  |")
                print("+-------------------------------------------------------------+")
                found=True
                

        if not found:
            print("Data Not available for this month!")    
        # 2.user choose and data show
         
        


    
def data_load(data):
    with open('portfolio.txt','w')as f:
        json.dump(data,f) 

# Add data

def add_data(data):
    print('\n\n')
    month=input("Enter a month (ex.. jan,feb,march..) :")
    print("\n")
    type=int(input("How many type of data enter (eg.. 1,2,3...) :"))

    types={}
    values={}
    gain_amounts={}
    gain_percentages={}
    for _ in range(1,type+1):
        ty=input("Enter a investment type :")
        amount=int(input(f"--->{ty} investment amount :"))
        value=int(input(f"---> {ty} investment value :"))
        gain_amounts[f"{ty} gain"]=value-amount
        gain_percentages[f"{ty} gain_percentage"]=((value/amount)*100)-100
        types[ty]=amount
        values[f"{ty}_value"]=value
    data.append({'month':month,'type':types,'values':values,'gain amount':gain_amounts,'gain_percentage':gain_percentages})
    data_load(data)        
# update data

def update_data(data):
    show_all(data)
    index=int(input("Enter a Number , which data do you want to update?:"))
    if 1 <= index <=len(data):

        types={}
        
        month_name=input("Enter your investment Month name (ex.. jan,feb,march..) :")
        type_num=int(input("How many type of data you enter (ex..1,2,3,4..):"))

        for _ in range(1,type_num+1):
            ty=input("Enter your invetment type (eg.. stock,bond,etf..) :")
            amount=int(input("Enter investment Amount :"))
            types[ty]=amount
            data[index-1]={'month':month_name,'type':types}
            data_load(data)
    else:
        print("+---------------------+")
        print("| Invalid data number |")
        print("+---------------------+")

def show_all(data):
        print("all data.")
    # data selcetion and show logic
        print("+-------------------------------------------------------------+")
        print(f"| {'month':<8}{'Type':<8}{'amount':<10}{'value':<10}{'Gain Amount':<13}{'Gain(%)':<10} |")
        print("+-------------------------------------------------------------+")

        for datas in data:
            month=datas['month']
            types=datas['type']
            values=datas['values']
            gains=datas["gain amount"]
            gains_per=datas['gain_percentage']

            first=True
            for invest_type,amount in types.items():
                value=values.get(f"{invest_type}_value","")
                gain_amount=gains.get(f"{invest_type} gain","")
                gain_per=gains_per.get(f"{invest_type} gain_percentage","")

                if first:
                    print(f"| {month:<8}{invest_type:<10}{amount:<10}{value:<10}{gain_amount:<10}{gain_per:<10.2f}  |")
                    first=False
                else:
                    print(f"| {"":<8}{invest_type:<10}{amount:<10}{value:<10}{gain_amount:<10}{gain_per:<10.2f}  |")
            print("+-------------------------------------------------------------+")
               
# delete dat
def after_delete_data(data):
    with open('portfolio.txt','w') as f:
        json.dump(data,f)

         

def delete_data(data):
    show_all(data)
    index=int(input("Enter number for delete data:"))
    if 1<= index <=len(data):
        del data[index-1]
        after_delete_data(data)
    else:
        print("+--------------------------------+")
        print("| pleace enter a cureact number! |")    
        print("+--------------------------------+")

def main():
    data=load_data()


    while True:
        print("\n")
        print("+------------------------------+ ")
        print("| Welcome Investment Portfolio |")
        print("+------------------------------+ ")

        # Ditails
        print('\n')
        print("1.Show data.")
        print("2.Add data.")
        print("3.Update data.")
        print("4.Delete data.")
        print("5.Exit App")
        print("\n")
        choice=input("Enter your choice:")

        match choice:
            case '1':
                show_all_data(data)

            case '2':
                add_data(data)
            case '3':
                update_data(data)

            case '4':
                delete_data(data)

            case '5':
                break

            case _:
                print("+-----------------+ ")
                print("| Invalide Choice |") 
                print("+-----------------+")
if __name__ == "__main__":
    main()