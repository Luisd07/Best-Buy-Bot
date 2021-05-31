from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




PATH = "C:\Program Files (x86)\chromedriver.exe"
browser = wd.Chrome(PATH)
itemLink = "https://www.bestbuy.com/site/hp-pavilion-x360-2-in-1-14-touch-screen-laptop-intel-core-i5-8gb-memory-512gb-ssd-32gb-intel-optane-warm-gold/6453186.p?skuId=6453186"
gpuLink = "https://www.bestbuy.com/site/nvidia-geforce-rtx-3060-ti-8gb-gddr6-pci-express-4-0-graphics-card-steel-and-black/6439402.p?skuId=6439402"


browser.get(itemLink)

foundButton = False

while not foundButton:

    try:
        atcbutton = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".add-to-cart-button"))
        )
    except:
        browser.refresh()
        continue

    try:
        atcbutton.click()

        browser.get("https://www.bestbuy.com/cart")

        checkoutbtn = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/main/div/div[2]/div[1]/div/div[1]/div[1]/section[2]/div/div/div[3]/div/div[1]/button"))
        )

        guestbtn = WebDriverWait(browser, 5).until(
            EC.element_to_be_located((By.XPATH, "/html/body/div[1]/div/section/main/div[2]/div[4]/div/div[2]/button"))
        )
        guestBtn.click()

        emailfield = WebDriverWait(browser, 5).until(
            EC.presence_of_element_located((By.ID, "fld-e"))
        )
        emailfield.send_keys(info.email)

        pnField = WebDriverWait(browser, 5).until(
            EC.presence_of_element_located((By.ID, "fld-p1"))
        )
        pnField.send_keys(info.pnumber)

        paymentBtn = WebDriverWait(browser, 5).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[2]/form/section/div/div[2]/div/div/button"))
        )
        browser.click(paymentBtn)

        cvvField = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, "credit-card-cvv"))
        )
        cvvField.send_keys(info.cvv)

        placeOrderBtn = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".button__fast-track"))
        )
        placeOrderBtn.click()

        isComplete = True
    except:
        browser.get(itemLink)
        continue
