import os
import pandas as pd
import warnings
warnings.filterwarnings('ignore', '.*do not.*', )
pathVarzeshi=r"C:\Users\ghazal\PycharmProjects\pythonProject\data\Varzeshi"
pathSiasi=r"C:\Users\ghazal\PycharmProjects\pythonProject\data\Siasi"
pathFarhangHonarVaResane=r"C:\Users\ghazal\PycharmProjects\pythonProject\data\FarhangHonarVaResane"
pathElmiVaDaneshghai=r"C:\Users\ghazal\PycharmProjects\pythonProject\data\ElmiVaDaneshghai"
pathEjtemaee=r"C:\Users\ghazal\PycharmProjects\pythonProject\data\Ejtemaee"
pathEghtesadi=r"C:\Users\ghazal\PycharmProjects\pythonProject\data\Eghtesadi"
pathBeinolmelal=r"C:\Users\ghazal\PycharmProjects\pythonProject\data\Beinolmelal"

output=r"C:\Users\ghazal\PycharmProjects\pythonProject\data\new.csv"



element = []
def read_text_file(file_path,label):

    df = pd.DataFrame(columns=['news','label'])

    with open(file_path, 'r', encoding='utf-8-sig') as f:
        data=f.read().splitlines()
        datanews=''.join(data)
        # datanews=f.read()
        # print(datanews)
        element.append([datanews,label])




def varzeshi():
    os.chdir(pathVarzeshi)
    for file in os.listdir():

        # Check whether file is in text format or not
        if file.endswith(".txt"):
            file_path = f"{pathVarzeshi}\{file}"
            read_text_file(file_path, 'varzeshi')


def siasi():
    os.chdir(pathSiasi)
    for file in os.listdir():

        # Check whether file is in text format or not
        if file.endswith(".txt"):
            file_path = f"{pathSiasi}\{file}"
            read_text_file(file_path, 'siasi')


def FarhangHonarVaResane():
    os.chdir(pathFarhangHonarVaResane)
    for file in os.listdir():

        # Check whether file is in text format or not
        if file.endswith(".txt"):
            file_path = f"{pathFarhangHonarVaResane}\{file}"
            read_text_file(file_path, 'FarhangHonarVaResane')


def ElmiVaDaneshghai():
    os.chdir(pathElmiVaDaneshghai)
    for file in os.listdir():

        # Check whether file is in text format or not
        if file.endswith(".txt"):
            file_path = f"{pathElmiVaDaneshghai}\{file}"
            read_text_file(file_path, 'ElmiVaDaneshghai')


def Ejtemaee():
    os.chdir(pathEjtemaee)
    for file in os.listdir():

        # Check whether file is in text format or not
        if file.endswith(".txt"):
            file_path = f"{pathEjtemaee}\{file}"
            read_text_file(file_path, 'Ejtemaee')



def Eghtesadi():
    os.chdir(pathEghtesadi)
    for file in os.listdir():

        # Check whether file is in text format or not
        if file.endswith(".txt"):
            file_path = f"{pathEghtesadi}\{file}"
            read_text_file(file_path, 'Eghtesadi')


def Beinolmelal():
    os.chdir(pathBeinolmelal)
    for file in os.listdir():

        # Check whether file is in text format or not
        if file.endswith(".txt"):
            file_path = f"{pathBeinolmelal}\{file}"
            read_text_file(file_path, 'Beinolmelal')




varzeshi()
Beinolmelal()
Eghtesadi()
Ejtemaee()
ElmiVaDaneshghai()
FarhangHonarVaResane()
siasi()

df=pd.DataFrame(element,columns=['news','label'])
print(df.head(200))
df.to_csv(r"C:\Users\ghazal\PycharmProjects\pythonProject\data\new.csv", encoding='utf-8-sig')

