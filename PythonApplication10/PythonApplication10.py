# Imports 
import random
import time
import os
import time
clear = lambda: os.system('cls')

#####################################################################
# Material Name Gen
def Material_Name_Gen ():
    Mat_Name_1 = ["Cob", "Bax", "Yak" , "Min", "Spleesh", "Rend", "Carls", "Strong", "Met", "The "]
    Mat_Name_2 = ["ite", "gen", "inum", "ek", "alt", "erium", "berg", "tope", "ich", "al"]
    Nam_No_One = random.randint(0,(len(Mat_Name_1)-1))
    Nam_No_Two = random.randint(0,(len(Mat_Name_2)-1))
    Mineral_Name = Mat_Name_1[Nam_No_One] + Mat_Name_2[Nam_No_Two]
    Mat_Name_1.remove(Mat_Name_1[Nam_No_One])
    Mat_Name_2.remove(Mat_Name_2[Nam_No_Two])
    return Mineral_Name

# Material Rarity
def Material_Rarity():
    Material_Rarity = (random.randint(1,100))
    return Material_Rarity 

# Material Quantities 
def Spawn(Rarity):
    TT = 0
    for mats in range(0,len(Materials)):
        if Materials[TT][Rarity] <= 100:
            Materials[TT]["Spawn Rate"] = 1

# Material Prices
def Mat_Price(MT):
    if Materials[MT]["Rarity"] <= 20:
        return 10
    else:
        return 20

def Name_Gen ():

    Name_Number_One = random.randint(0,(len(First_Name)-1))
    Name_Number_Two = random.randint(0,(len(Second_Name)-1))
    Name_To_Be_Returned = First_Name[Name_Number_One] + Second_Name[Name_Number_Two]
    First_Name.remove(First_Name[Name_Number_One])
    Second_Name.remove(Second_Name[Name_Number_Two])
    return Name_To_Be_Returned

def Location_Gen():
    Location_Name_One = random.randint(0,len(First_Location_Names)-1)
    Location_Name_Two = random.randint(0,len(Second_Location_Names)-1)
    Location_Name = First_Location_Names[Location_Name_One] + Second_Location_Names[Location_Name_Two]
    First_Location_Names.remove(First_Location_Names[Location_Name_One])
    Second_Location_Names.remove(Second_Location_Names[Location_Name_Two])
    return Location_Name

def Leader_Gen():
    Suffix = (random.randint(0,len(First_Leader_Name)-1))
    Prefix = (random.randint(0,len(Second_Leader_Name)-1))
    Final_Name = First_Leader_Name[Suffix] + Second_Leader_Name[Prefix]
    First_Leader_Name.remove(First_Leader_Name[Suffix])
    Second_Leader_Name.remove(Second_Leader_Name[Prefix])
    return Final_Name

#Tax
def Tax_Reduction(Profit):
    Tax_To_Bank = (Profit / 100) * 15
    World_Bank_Funds = World_Bank_Funds + Tax_To_Bank
    return Tax_To_Bank

def Fund_Check(All_Corps):
    Tick_no = 0
    for funds in range(0, len(All_Corps)):
        All_Corps[Tick_no]["Funds"]
        if All_Corps[Tick_no]["Funds"] >= 1:
            Potential_Clients.append(All_Corps[Tick_no]["Name"])
            Tick_no = Tick_no + 1
        else:
            Tick_no = Tick_no + 1
 # Material Check 
Potential_Materials = []
def Mat_Check(Materials):
    TN = 0
    for mats in range(0, len(Materials)):
        Materials[TN]["Quantity"]
        if Materials[TN]["Quantity"] >= 1:
            Potential_Materials.append(Materials[TN]["Name"])
            TN = TN + 1
        else:
            TN = TN + 1

def Who_Wins():
    N = 0
    for corps in range(0,len(Potential_Clients)):
        Chance = random.randint(0,100)
        #Potential_Clients = Bid_Order
        Potential_Clients[N][Chance] = [Chance]
        Potential_Clients.sort
        N = N + 1
    return Potential_Clients[0]

def Mat_To_Buy():
    Potential_Materials.sorted
    return Materials[str(Potential_Materials[0])]


def Purchase():
    Fund_Check(All_Corps)
    Mat_Check(Materials)
    if len(Potential_Clients) and len(Potential_Materials) >= 1:
        if len(Potential_Clients) >=2:
            Who_Wins()
            Mat_To_Buy
            All_Corps[str(Who_Wins())]["Funds"] - (Mat_To_Buy()["Price"])
            (Mat_To_Buy()["Quantity"]) - 1
            All_Corps[str(Who_Wins())]["Material Bank"] + [Mat_To_Buy()]["Name"]


##########################################################


# Locations 
First_Location_Names = ["Wood ", "Saint ", "Upper ", "Lower ", "Mild ", "Tomato ", "Tilted ", "Greasy ","Salty "]
Second_Location_Names = ["House", "Way", "Towers", "Town", "Mire", "Grove","Springs"]

# Leader
First_Leader_Name = ["Sir ", "Mrs ","Mr ","Doctor ", "Steve ", "Bill ", "Vicky "]
Second_Leader_Name = ["Blinket", "Andamale", "Wheile", "Crroragan", "Ousbourne", "Coyne"]

# Name Gen
First_Name = ["The Guys ", "Some People ", "Fat Head ", "Summit ", "Nortons ", "Ammy ", "Starbucks ", "Indie Prince ", "Spoons ", "Soda "]
Second_Name = ["Corp", "industries", "Incoproated", "Inc", "Studios", "Limited", "Global", ".CO", "Inc", "Since 1996" ]

# Corps
Number_Of_Corps = random.randint(2,4)
All_Corps = {}
Corp_Names = All_Corps.keys()

# Materials
Material_Number = random.randint(5,10)
Materials = {}

# Corp Gen (finish corp funds)
Corp_No = 0

for corps in range(Number_Of_Corps):
    All_Corps[Corp_No] = { "Name" : Name_Gen(),  "Location" : Location_Gen(), "Leader": Leader_Gen() , "Funds" : 10000, "Material Bank" : 0, "Roll": 0}
    Corp_No = Corp_No + 1

  
  # Matieral Creation
Mat_No = 0

Mat_No = 0
for mats in range(Material_Number):
    Materials[Mat_No] = {"Name" : Material_Name_Gen() ,"Rarity" : Material_Rarity(), "Quantity" : 1, "Price" : 0,  }
    Mat_No = Mat_No + 1
Mat_No = 0
for mats in range(Material_Number):
    Materials[Mat_No]["Price"] = Mat_Price(Mat_No)
    Mat_No = Mat_No + 1

# Material Gen 
def Mat_Gen():
    NM = 0
    for mats in range(0,len(Materials)):
        if Materials[NM]["Rarity"] <= 10:
            Materials[NM]["Quantity"] = Materials[NM]["Quantity"] + 100
        elif Materials[NM]["Rarity"] >= 30:
            Materials[NM]["Quantity"] = Materials[NM]["Quantity"] + 70
        elif Materials[NM]["Rarity"] <= 50:
            Materials[NM]["Quantity"] = Materials[NM]["Quantity"] + 30
        elif Materials[NM]["Rarity"] <= 80:
            Materials[NM]["Quantity"] = Materials[NM]["Quantity"] + 10
        elif Materials[NM]["Rarity"] <= 90:
            Materials[NM]["Quantity"] = Materials[NM]["Quantity"] + 1

 #Environment
 #Weather (to do)
 

# Legality (TO DO)
Legal = True

# World Bank Gen

World_Bank= {}
World_Bank_Funds = 1000
World_Bank["World Bank"] = ((0), "Metropolis", (Leader_Gen)(), World_Bank_Funds)



# Purchasing Mechanics
Potential_Clients = []
 # Funds Check
Tick_no = 0

Fund_Check(All_Corps)

# Bidding Tech (ToDo)
Bid_Order = []
Successful_Corp = []
N = 0

# Time
Hour = 0
Day = 0
Month = 0
Year = 0
Time = 9
AM_PM = "AM"
 # Day Properties
Daytime = 1
Nighttime = 0

#Day Cycle
while 1 == 1:
    for Day in range(0,8):
        Mat_Gen()
        Hour = Hour + 1
        Time = str(9) + str(AM_PM)
        Purchase()
        print (Time)
        time.sleep(5)
        clear()
    
    
# Time
Hour = 0
Day = 0
Month = 0
Year = 0
 # Day Properties
Daytime = 1
Nighttime = 0
    

        

    
