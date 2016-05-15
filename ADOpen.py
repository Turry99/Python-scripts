import webbrowser,os,time
ie = webbrowser.get('c:\\program Files\\internet explorer\\iexplore.exe')
ie.open('http://google.com')  # Change the URL with the AD/site you want the 'victim' to see
time.sleep(5)  # Change the number for more/less seconds
os.system('taskkill /f /im iexplore.exe')
