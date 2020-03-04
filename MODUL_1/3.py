vokal = "aiueoAIUEO"

def jumlahHurufVokal(x):
    hrfVokal = 0
    jmlHuruf = len(x)
    for i in x:
        if i in vokal:
            hrfVokal = hrfVokal+1
    print(jmlHuruf, ",", hrfVokal)

def jumlahHurufKonsonan(x):
    hrfkonsonan = 0
    jmlHuruf = len(x)
    for i in x:
        if i not in vokal:
            hrfkonsonan = hrfkonsonan+1
    print(jmlHuruf, ",", hrfkonsonan)
