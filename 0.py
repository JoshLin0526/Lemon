import time
def sendmail(message):
    import smtplib
    from email.mime.text import MIMEText

    # 寄件者，收件者
    from_addr = '810271@stu.nknush.kh.edu.tw'
    to_addr = '810271@stu.nknush.kh.edu.tw'


    smtpssl=smtplib.SMTP_SSL("smtp.gmail.com", 465)
    smtpssl.login(from_addr, "E126150439")

    msg = 'PM2.5=' + message
    mime=MIMEText(msg, "plain", "utf-8")
    mime["Subject"]="Python中文信件!!!(MIME)"
    # 顯示的名稱
    mime["From"]="PM2.5監視器"
    mime["To"]= to_addr

    smtpssl.sendmail(from_addr, to_addr, mime.as_string())
    smtpssl.quit()

while True:

    import requests, json
    import urllib3
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    # 若來源資料為 https 則加上 verify=False 參數
    response = requests.get('https://opendata.epa.gov.tw/ws/Data/ATM00625/?$format=json', verify=False)

    sites = response.json()
    for site in sites:
        if site['Site'] == '復興':
            sendmail(site['PM25'])
            break
    time.sleep(3600)
