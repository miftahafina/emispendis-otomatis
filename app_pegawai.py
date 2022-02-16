from os import environ
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import operator
from transform_data_pegawai import rows
from datetime import datetime

load_dotenv()

short_waiting_time  = 0.5
medium_waiting_time = 1.5
long_waiting_time   = 3

# Read data source
pegawai_list = rows


# For captcha purpose
operators = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv
}


# Getting credentials
browser             = webdriver.Chrome("./chromedriver/stable/chromedriver")
emispendis_url      = environ.get('emispendis_url')
emispendis_username = environ.get('emispendis_username')
emispendis_password = environ.get('emispendis_password')


# Begin browsing
browser.get(emispendis_url)
browser.set_window_size(1920, 1080)
browser.maximize_window()


# Fill login form
browser.find_element(By.NAME, "username").send_keys(emispendis_username)
browser.find_element(By.NAME, "password").send_keys(emispendis_password)

captcha_problem  = browser.find_element(By.TAG_NAME, "h6").text
captcha_arr      = captcha_problem.split(" ")
number_1         = int(captcha_arr[0])
number_2         = int(captcha_arr[2])
operator         = operators[captcha_arr[1]]
captcha_solution = operator(number_1, number_2)

browser.find_element(By.NAME, "captcha").send_keys(captcha_solution)
browser.find_element(By.TAG_NAME, "button").click()

# Begin fill the form pegawai with data from source
for pegawai in pegawai_list:
    # Open form
    browser.implicitly_wait(10)
    browser.find_element(By.XPATH, "//span[contains(text(),'Ustad/Ustadzah')]").click()

    browser.implicitly_wait(10)
    browser.find_element(By.XPATH, "//a[@class='nav-link'][contains(text(), 'Daftar Ustad/Ustadzah')]").click()

    browser.implicitly_wait(10)
    browser.find_element(By.XPATH, "//i[@class='fas fa-plus']").click()
    browser.implicitly_wait(10)


    # Fill data pegawai columns
    browser.find_element(By.ID, "select2-lembaga_profile_id-container").click()
    browser.find_element(By.XPATH, "//input[@aria-controls='select2-lembaga_profile_id-results']").send_keys(pegawai["satminkal"])
    sleep(long_waiting_time)
    browser.find_element(By.XPATH, "//input[@aria-controls='select2-lembaga_profile_id-results']").send_keys(Keys.ENTER)

    browser.find_element(By.NAME, "nama_lengkap").send_keys(pegawai["nama_lengkap"])
    browser.find_element(By.NAME, "tempat_lahir").send_keys(pegawai["tempat_lahir"])

    browser.find_element(By.NAME, "tgl_lahir").send_keys(Keys.CONTROL, 'a')
    browser.find_element(By.NAME, "tgl_lahir").send_keys(pegawai["tanggal_lahir"])
    browser.find_element(By.NAME, "tgl_lahir").send_keys(Keys.ESCAPE)

    browser.find_element(By.ID, "select2-gender-container").click()
    browser.find_element(By.XPATH, "//input[@aria-controls='select2-gender-results']").send_keys(pegawai["jenis_kelamin"])
    sleep(medium_waiting_time)
    browser.find_element(By.XPATH, "//input[@aria-controls='select2-gender-results']").send_keys(Keys.ENTER)
    sleep(medium_waiting_time)

    browser.find_element(By.ID, "select2-agama-container").click()
    browser.find_element(By.XPATH, "//input[@aria-controls='select2-agama-results']").send_keys(pegawai["agama"])
    sleep(medium_waiting_time)
    browser.find_element(By.XPATH, "//input[@aria-controls='select2-agama-results']").send_keys(Keys.ENTER)

    browser.find_element(By.NAME, "no_telp").send_keys(pegawai["no_telp_rumah"])
    browser.find_element(By.NAME, "no_hp").send_keys(pegawai["no_hp"])
    browser.find_element(By.NAME, "nama_ibu").send_keys(pegawai["nama_ibu"])

    browser.find_element(By.ID, "select2-kewarganegaraan-container").click()
    browser.find_element(By.XPATH, "//input[@aria-controls='select2-kewarganegaraan-results']").send_keys(pegawai["kewarganegaraan"])
    sleep(medium_waiting_time)
    browser.find_element(By.XPATH, "//input[@aria-controls='select2-kewarganegaraan-results']").send_keys(Keys.ENTER)

    browser.execute_script("window.scrollTo(0, 250)")
    sleep(short_waiting_time)

    browser.find_element(By.NAME, "nik").send_keys(pegawai["nik_passport"])

    browser.find_element(By.ID, "select2-pendidikan_terakhir-container").click()
    browser.find_element(By.XPATH, "//input[@aria-controls='select2-pendidikan_terakhir-results']").send_keys(pegawai["pendidikan_terakhir"])
    sleep(medium_waiting_time)
    browser.find_element(By.XPATH, "//input[@aria-controls='select2-pendidikan_terakhir-results']").send_keys(Keys.ENTER)

    browser.find_element(By.NAME, "npwp").send_keys(pegawai["npwp"])

    browser.find_element(By.ID, "select2-status_keaktifan-container").click()
    browser.find_element(By.XPATH, "//input[@aria-controls='select2-status_keaktifan-results']").send_keys(pegawai["status_keaktifan"])
    sleep(medium_waiting_time)
    browser.find_element(By.XPATH, "//input[@aria-controls='select2-status_keaktifan-results']").send_keys(Keys.ENTER)
    
    browser.find_element(By.NAME, "tgl_mulai_bertugas").send_keys(Keys.CONTROL, 'a')
    browser.find_element(By.NAME, "tgl_mulai_bertugas").send_keys(pegawai["tanggal_mulai_bertugas"])
    browser.find_element(By.NAME, "tgl_mulai_bertugas").send_keys(Keys.ESCAPE)
    sleep(medium_waiting_time)

    browser.find_element(By.ID, "select2-status_pegawai-container").click()
    browser.find_element(By.XPATH, "//input[@aria-controls='select2-status_pegawai-results']").send_keys(pegawai["status_kepegawaian"])
    sleep(medium_waiting_time)
    browser.find_element(By.XPATH, "//input[@aria-controls='select2-status_pegawai-results']").send_keys(Keys.ENTER)
    
    browser.find_element(By.NAME, "nip").send_keys(pegawai["nip_nrp"])

    browser.find_element(By.ID, "select2-status_penugasan-container").click()
    browser.find_element(By.XPATH, "//input[@aria-controls='select2-status_penugasan-results']").send_keys(pegawai["status_penugasan"])
    sleep(long_waiting_time)
    browser.find_element(By.XPATH, "//input[@aria-controls='select2-status_penugasan-results']").send_keys(Keys.ENTER)

    browser.find_element(By.ID, "select2-tugas_utama-container").click()
    browser.find_element(By.XPATH, "//input[@aria-controls='select2-tugas_utama-results']").send_keys(pegawai["tugas_utama"])
    sleep(medium_waiting_time)
    browser.find_element(By.XPATH, "//input[@aria-controls='select2-tugas_utama-results']").send_keys(Keys.ENTER)

    browser.find_element(By.NAME, "no_rek").send_keys(pegawai["no_rekening"])
    browser.find_element(By.NAME, "nama_rek").send_keys(pegawai["nama_rekening"])
    browser.find_element(By.NAME, "nama_bank").send_keys(pegawai["nama_bank"])
    browser.find_element(By.NAME, "cabang_bank").send_keys(pegawai["cabang"])


    # Submit data
    browser.find_element(By.ID, "btnKirim").click()
    sleep(long_waiting_time)


    # Check NIK validation
    if (browser.find_element(By.ID, "swal2-html-container").text == "NIK Sudah terdaftar, silakan lakukan penarikan data"):
        browser.find_element(By.XPATH, "//button[@class='swal2-confirm swal2-styled']").click()
        sleep(long_waiting_time)

        # Better stop the process because we're unable to delete submitted data
        timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

        f = open(environ.get('log_file_pegawai'), 'a')
        f.write("\n")
        f.write(f"""{timestamp} :: {pegawai["nik_passport"]} - {pegawai["nama_lengkap"]}: Gagal diinput (NIK Sudah Terdaftar)""")
        f.close()

    # Check if success
    elif (browser.find_element(By.ID, "swal2-html-container").text == "Data berhasil tersimpan"):
        browser.find_element(By.XPATH, "//button[@class='swal2-confirm swal2-styled']").click()
        sleep(long_waiting_time)

        timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

        f = open(environ.get('log_file_pegawai'), 'a')
        f.write("\n")
        f.write(f"""{timestamp} :: {pegawai["nik_passport"]} - {pegawai["nama_lengkap"]}: Berhasil diinput""")
        f.close()
        # Repeat the proccess until the loop is done
