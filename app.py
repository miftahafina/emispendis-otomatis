from os import environ
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from random import randint
from time import sleep
import operator
from data_siswa import rows
from datetime import datetime

load_dotenv()

short_waiting_time  = 0.5
medium_waiting_time = 0.7
long_waiting_time   = 1.5

# Read data source
siswa_list = rows


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


# Begin fill the form siswa with data from source
for siswa in siswa_list:
    # Open form
    browser.implicitly_wait(10)
    browser.find_element(By.XPATH, "//span[contains(text(),'Santri')]").click()

    browser.implicitly_wait(10)
    browser.find_element(By.XPATH, "//a[@class='nav-link'][contains(text(), 'Data Santri')]").click()

    browser.implicitly_wait(10)
    browser.find_element(By.XPATH, "//i[@class='fas fa-plus']").click()
    browser.implicitly_wait(10)


    # Fill data siswa columns
    browser.find_element(By.NAME, "nama_siswa").send_keys(siswa["nama_siswa"])
    browser.find_element(By.NAME, "nisn").send_keys(siswa["nisn"])
    browser.find_element(By.NAME, "nik").send_keys(siswa["nik"])
    browser.find_element(By.NAME, "tmt_lahir").send_keys(siswa["tempat_lahir"])
    browser.find_element(By.NAME, "tgl_lhr").send_keys(Keys.CONTROL, 'a')
    browser.find_element(By.NAME, "tgl_lhr").send_keys(siswa["tanggal_lahir"])
    browser.find_element(By.NAME, "tgl_lhr").send_keys(Keys.ESCAPE)
    browser.find_element(By.ID, "select2-gender-container").click()
    browser.find_element(By.XPATH, "//input[@aria-controls='select2-gender-results']").send_keys(siswa["jenis_kelamin"], Keys.ENTER)
    sleep(medium_waiting_time)

    browser.find_element(By.ID, "select2-agama-container").click()
    browser.find_element(By.XPATH, "//input[@aria-controls='select2-agama-results']").send_keys(siswa["agama"])
    sleep(medium_waiting_time)
    browser.find_element(By.XPATH, "//input[@aria-controls='select2-agama-results']").send_keys(Keys.ENTER)

    browser.execute_script("window.scrollTo(0, 900)")
    sleep(short_waiting_time)

    browser.find_element(By.ID, "select2-hobi-container").click()
    browser.find_element(By.XPATH, "//input[@aria-controls='select2-hobi-results']").send_keys(siswa["hobi"])
    sleep(medium_waiting_time)
    browser.find_element(By.XPATH, "//input[@aria-controls='select2-hobi-results']").send_keys(Keys.ENTER)

    browser.find_element(By.ID, "select2-cita_cita-container").click()
    browser.find_element(By.XPATH, "//input[@aria-controls='select2-cita_cita-results']").send_keys(siswa["cita_cita"])
    sleep(medium_waiting_time)
    browser.find_element(By.XPATH, "//input[@aria-controls='select2-cita_cita-results']").send_keys(Keys.ENTER)

    browser.find_element(By.ID, "select2-kebutuhan_khusus_id-container").click()
    browser.find_element(By.XPATH, "//input[@aria-controls='select2-kebutuhan_khusus_id-results']").send_keys(siswa["kebutuhan_khusus"])
    sleep(medium_waiting_time)
    browser.find_element(By.XPATH, "//input[@aria-controls='select2-kebutuhan_khusus_id-results']").send_keys(Keys.ENTER)

    browser.find_element(By.ID, "select2-status_rumah_id-container").click()
    browser.find_element(By.XPATH, "//input[@aria-controls='select2-status_rumah_id-results']").send_keys(siswa["status_rumah"])
    sleep(medium_waiting_time)
    browser.find_element(By.XPATH, "//input[@aria-controls='select2-status_rumah_id-results']").send_keys(Keys.ENTER)


    # Fill data ayah columns
    browser.find_element(By.NAME, "nomor_kk").send_keys(siswa["no_kk"])
    browser.find_element(By.NAME, "nik_ayah").send_keys(siswa["nik_ayah"])
    browser.find_element(By.NAME, "nama_ayah").send_keys(siswa["nama_ayah"])

    browser.find_element(By.ID, "select2-pekerjaan_ayah_id-container").click()
    browser.find_element(By.XPATH, "//input[@aria-controls='select2-pekerjaan_ayah_id-results']").send_keys(siswa["pekerjaan_ayah"])
    sleep(medium_waiting_time)
    browser.find_element(By.XPATH, "//input[@aria-controls='select2-pekerjaan_ayah_id-results']").send_keys(Keys.ENTER)

    browser.find_element(By.ID, "select2-pendidikan_ayah_id-container").click()
    browser.find_element(By.XPATH, "//input[@aria-controls='select2-pendidikan_ayah_id-results']").send_keys(siswa["pendidikan_ayah"])
    sleep(medium_waiting_time)
    browser.find_element(By.XPATH, "//input[@aria-controls='select2-pendidikan_ayah_id-results']").send_keys(Keys.ENTER)

    browser.find_element(By.ID, "select2-penghasilan_ortu_id-container").click()
    browser.find_element(By.XPATH, "//input[@aria-controls='select2-penghasilan_ortu_id-results']").send_keys(siswa["rata_rata_penghasilan"])
    sleep(medium_waiting_time)
    browser.find_element(By.XPATH, "//input[@aria-controls='select2-penghasilan_ortu_id-results']").send_keys(Keys.ENTER)

    browser.execute_script("window.scrollTo(0, 0)")
    sleep(short_waiting_time)


    # Fill data ibu column
    browser.find_element(By.NAME, "nik_ibu").send_keys(siswa["nik_ibu"])
    browser.find_element(By.NAME, "nama_ibu").send_keys(siswa["nama_ibu"])

    browser.find_element(By.ID, "select2-pekerjaan_ibu_id-container").click()
    browser.find_element(By.XPATH, "//input[@aria-controls='select2-pekerjaan_ibu_id-results']").send_keys(siswa["pekerjaan_ibu"])
    sleep(medium_waiting_time)
    browser.find_element(By.XPATH, "//input[@aria-controls='select2-pekerjaan_ibu_id-results']").send_keys(Keys.ENTER)

    browser.find_element(By.ID, "select2-pendidikan_ibu_id-container").click()
    browser.find_element(By.XPATH, "//input[@aria-controls='select2-pendidikan_ibu_id-results']").send_keys(siswa["pendidikan_ibu"])
    sleep(medium_waiting_time)
    browser.find_element(By.XPATH, "//input[@aria-controls='select2-pendidikan_ibu_id-results']").send_keys(Keys.ENTER)

    browser.execute_script("window.scrollTo(0, 1000)")
    sleep(short_waiting_time)


    # Fill data alamat column
    browser.find_element(By.NAME, "alamat_rumah").send_keys(siswa["alamat_rumah"])
    browser.find_element(By.NAME, "rt").send_keys(siswa["rt"])
    browser.find_element(By.NAME, "rw").send_keys(siswa["rw"])

    browser.find_element(By.ID, "select2-cprov-container").click()
    browser.find_element(By.XPATH, "//input[@aria-controls='select2-cprov-results']").send_keys(siswa["provinsi"])
    sleep(long_waiting_time)
    browser.find_element(By.XPATH, "//input[@aria-controls='select2-cprov-results']").send_keys(Keys.ENTER)

    browser.find_element(By.ID, "select2-ckabko-container").click()
    browser.find_element(By.XPATH, "//input[@aria-controls='select2-ckabko-results']").send_keys(siswa["kabupaten_kota"])
    sleep(long_waiting_time)
    browser.find_element(By.XPATH, "//input[@aria-controls='select2-ckabko-results']").send_keys(Keys.ENTER)

    browser.find_element(By.ID, "select2-ckec-container").click()
    browser.find_element(By.XPATH, "//input[@aria-controls='select2-ckec-results']").send_keys(siswa["kecamatan"])
    sleep(long_waiting_time)
    browser.find_element(By.XPATH, "//input[@aria-controls='select2-ckec-results']").send_keys(Keys.ENTER)

    # fill zip code with fake data because it's impossible to search on its select2
    browser.find_element(By.ID, "select2-lokasi_kodepos-container").click()
    sleep(long_waiting_time)
    browser.find_element(By.XPATH, "//input[@aria-controls='select2-lokasi_kodepos-results']").send_keys(Keys.DOWN)
    browser.find_element(By.XPATH, "//input[@aria-controls='select2-lokasi_kodepos-results']").send_keys(Keys.ENTER)


    # Submit data
    browser.find_element(By.ID, "btnKirim").click()
    sleep(long_waiting_time)


    # Check NIK validation
    if (browser.find_element(By.ID, "swal2-html-container").text == "NIK sudah terdaftar"):
        browser.find_element(By.XPATH, "//button[@class='swal2-confirm swal2-styled']").click()

        browser.execute_script("window.scrollTo(0, 0)")
        sleep(short_waiting_time)

        browser.find_element(By.NAME, "nik").send_keys(Keys.BACK_SPACE)
        browser.find_element(By.NAME, "nik").send_keys(Keys.BACK_SPACE)
        browser.find_element(By.NAME, "nik").send_keys(Keys.BACK_SPACE)
        browser.find_element(By.NAME, "nik").send_keys(Keys.BACK_SPACE)
        browser.find_element(By.NAME, "nik").send_keys(randint(1000,9999))

        browser.execute_script("window.scrollTo(0, 1000)")
        sleep(short_waiting_time)

        browser.find_element(By.ID, "btnKirim").click()
        sleep(long_waiting_time)


    # Check if success
    if (browser.find_element(By.ID, "swal2-html-container").text == "Data berhasil tersimpan"):
        browser.find_element(By.XPATH, "//button[@class='swal2-confirm swal2-styled']").click()
        sleep(long_waiting_time)

        timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

        f = open(environ.get('log_file'), 'a')
        f.write("\n")
        f.write(f"""{timestamp} :: {siswa["nik"]} - {siswa["nisn"]} - {siswa["nama_siswa"]}: Berhasil diinput""")
        f.close()
        # Repeat the proccess until the loop is done

