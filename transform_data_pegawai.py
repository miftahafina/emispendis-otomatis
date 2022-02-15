import csv
from os import environ
from dotenv import load_dotenv

load_dotenv()

# Open file
file = open(environ.get("data_source_pegawai"), "r")
csv_reader = csv.reader(file, delimiter="\t")



# Get header
header = []
header = next(csv_reader)


# Fetch data
rows = []
for row in csv_reader:
    rows.append({
        "no": row[header.index("no")],
        "satminkal": row[header.index("satminkal")],

        "nama_lengkap" : row[header.index("nama_lengkap")],
        "tempat_lahir" : row[header.index("tempat_lahir")],
        "tanggal_lahir": row[header.index("tanggal_lahir")],
        "jenis_kelamin": row[header.index("jenis_kelamin")],
        "agama"        : row[header.index("agama")],

        "no_telp_rumah": row[header.index("no_telp_rumah")],
        "no_hp"        : row[header.index("no_hp")],

        "nama_ibu"           : row[header.index("nama_ibu")],
        "kewarganegaraan"    : row[header.index("kewarganegaraan")],
        "nik_passport"       : row[header.index("nik_passport")],
        "pendidikan_terakhir": row[header.index("pendidikan_terakhir")],
        "npwp"               : row[header.index("npwp")],

        "status_keaktifan"      : row[header.index("status_keaktifan")],
        "tanggal_mulai_bertugas": row[header.index("tanggal_mulai_bertugas")],
        "status_kepegawaian"    : row[header.index("status_kepegawaian")],
        "nip_nrp"               : row[header.index("nip_nrp")],
        "status_penugasan"      : row[header.index("status_penugasan")],
        "tugas_utama"           : row[header.index("tugas_utama")],

        "no_rekening"  : row[header.index("no_rekening")],
        "nama_rekening": row[header.index("nama_rekening")],
        "nama_bank"    : row[header.index("nama_bank")],
        "cabang"       : row[header.index("cabang")]
    })

file.close()
