from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

# Configuracion del navegador
chrome_options = Options()
service = Service("Driver/chromedriver.exe")
driver = webdriver.Chrome(options=chrome_options, service=service)
driver.maximize_window()

# Navegar a la pagina inicial
driver.get(
    "https://www.udemy.com/join/passwordless-auth/?locale=es_ES&next=https%3A%2F%2Fwww.udemy.com%2F%3Futm_source%3Dadwords%26utm_medium%3Dudemyads%26utm_campaign%3DBranded-Topic_la.ES_cc.LATAM%26campaigntype%3DSearch%26portfolio%3DBrandTopic%26language%3DES%26product%3DCourse%26test%3D%26audience%3DKeyword%26topic%3D%26priority%3D%26utm_content%3Ddeal4584%26utm_term%3D_._ag_122876139243_._ad_604231009895_._kw_cursos%2520en%2520l%25C3%25ADnea%2520udemy_._de_c_._dm__._pl__._ti_kwd-1394266915329_._li_9218294_._pd__._%26matchtype%3Db%26gad_source%3D1%26gclid%3DEAIaIQobChMI1vCC-uCbigMVgUxHAR3dGDfaEAAYASAAEgJXU_D_BwE&response_type=html")

# Salir
driver.close()
