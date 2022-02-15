import csv
from os import environ
from dotenv import load_dotenv

load_dotenv()

# Open file
file = open(environ.get("data_source"), "r")
csv_reader = csv.reader(file, delimiter="\t")



# Get header
header = []
header = next(csv_reader)


# Fetch data
rows = []
for row in csv_reader:
    rows.append({
        "no": row[header.index("no")],

        "nama_siswa"      : row[header.index("nama_siswa")],
        "nisn"            : row[header.index("nisn")],
        "nik"             : row[header.index("nik")],
        "tempat_lahir"    : row[header.index("tempat_lahir")],
        "tanggal_lahir"   : row[header.index("tanggal_lahir")],
        "jenis_kelamin"   : row[header.index("jenis_kelamin")],
        "agama"           : row[header.index("agama")],
        "hobi"            : row[header.index("hobi")],
        "cita_cita"       : row[header.index("cita_cita")],
        "kebutuhan_khusus": row[header.index("kebutuhan_khusus")],
        "status_rumah"    : row[header.index("status_rumah")],

        "no_kk"                : row[header.index("no_kk")],
        "nik_ayah"             : row[header.index("nik_ayah")],
        "nama_ayah"            : row[header.index("nama_ayah")],
        "pekerjaan_ayah"       : row[header.index("pekerjaan_ayah")],
        "pendidikan_ayah"      : row[header.index("pendidikan_ayah")],
        "rata_rata_penghasilan": row[header.index("rata_rata_penghasilan")],

        "nik_ibu"       : row[header.index("nik_ibu")],
        "nama_ibu"      : row[header.index("nama_ibu")],
        "pekerjaan_ibu" : row[header.index("pekerjaan_ibu")],
        "pendidikan_ibu": row[header.index("pendidikan_ibu")],

        "alamat_rumah"  : row[header.index("alamat_rumah")],
        "rt"            : row[header.index("rt")],
        "rw"            : row[header.index("rw")],
        "provinsi"      : row[header.index("provinsi")],
        "kabupaten_kota": row[header.index("kabupaten_kota")],
        "kecamatan"     : row[header.index("kecamatan")],
        "kode_pos"      : row[header.index("kode_pos")]
    })

file.close()
