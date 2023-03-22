import csv
from selenium import webdriver
from datetime import datetime
from shutil import copyfile
#CSV
def csv_url_reader(url_obj):
    reader=csv.DictReader(url_obj,delimiter =',')
    for line in reader:
        url=line["URL"]
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"
        options = webdriver.ChromeOptions()
        chrome_prefs = {}
        options.experimental_options["prefs"] = chrome_prefs
        chrome_prefs["profile.default_content_settings"] = {"images": 2}
        chrome_prefs["profile.managed_default_content_settings"] = {"images": 2}
        options.headless = False
        options.add_argument(f'user-agent={user_agent}')
        options.add_argument("--window-size=1920,1080")
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--allow-running-insecure-content')
        options.add_argument("--disable-extensions")
        options.add_argument("--proxy-server='direct://'")
        options.add_argument("--proxy-bypass-list=*")
        options.add_argument("--start-maximized")
        options.add_argument('--disable-gpu')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--no-sandbox')
        driver = webdriver.Chrome(executable_path="chromedriver.exe", options=options)
        driver.get(url)
        driver.implicitly_wait(10) #Now loop it to execute only one website at a time and printing the FP and Name (Doubt)
        FP=driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/div[1]/div/div/div[2]/div[2]/div[1]/div/div[1]/div[2]/div[2]/span').text
        FP1=FP.replace('◎','')
        Name=driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/div[1]/div/div/div[2]/div[1]/div/div/div/div[1]').text
        driver.close()
        print(Name)
        print(FP1)
        Name_list=[Name]
        FP_list=[FP1]
        print(Name_list)
        print(FP_list)
        row=Name_list+FP_list
        with open('Floorprice.csv','a',encoding='utf-8',newline='') as f:
            thewriter = csv.writer(f)
            thewriter.writerow(row)

      

if __name__=="__main__":
    with open('Floorprice.csv','w',encoding='utf-8',newline='') as f:
        data=csv.writer(f)
        data.writerow(['Name','FP'])
    with open("goodprojects.csv",'r') as url_obj:
        csv_url_reader(url_obj)

datetime_backup=datetime.now()
print(datetime_backup)

str_datetime_backup=str(datetime_backup).replace('-','.')
a=str_datetime_backup[0:13]
a=str(a).replace('-',"") 
print(a)

path_input=r'D:\Python Programs\Floor Price NFT\Floorprice.csv'
path_output=r'D:\Python Programs\Floor Price NFT\Backups' + '\\' + a +" Floor price.csv"

copyfile(path_input,path_output) 