import sqlite3
import json
import os

db_file = 'otomasyon.db'

def load_json_data(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except json.JSONDecodeError as e:
        print("JSON dosyasını okurken bir hata oluştu:", e)
        return None

conn = sqlite3.connect(db_file)
cursor = conn.cursor()

if os.path.exists(db_file):
    select_data_sql = '''
        SELECT * FROM hasta
    '''

    select_data_sql_doktor = '''
        SELECT * FROM doktor
    '''

    select_data_sql_randevu = '''
        SELECT * FROM randevu
    '''

    select_data_sql_rapor = '''
        SELECT * FROM rapor
    '''

    select_data_sql_yonetici = '''
        SELECT * FROM yonetici
    '''

    cursor.execute(select_data_sql)

    for row in cursor.fetchall():
        print(row)

    cursor.execute(select_data_sql_doktor)

    for row in cursor.fetchall():
        print(row)

    cursor.execute(select_data_sql_randevu)

    for row in cursor.fetchall():
        print(row)

    cursor.execute(select_data_sql_rapor)

    for row in cursor.fetchall():
        print(row)

    cursor.execute(select_data_sql_yonetici)

    for row in cursor.fetchall():
        print(row)

    conn.commit()
    conn.close()

else:
    create_table_sql = '''
        CREATE TABLE IF NOT EXISTS hasta (
            hastaID INTEGER PRIMARY KEY AUTOINCREMENT,
            hastaAdi TEXT,
            hastaSoyadi TEXT,
            hastaCinsiyet TEXT,
            hastaTarih TEXT,
            hastaTelefon TEXT,
            hastaAdres TEXT,
            hastaSifre TEXT
        )
    '''

    create_table_sql_doktor = '''
        CREATE TABLE IF NOT EXISTS doktor (
            doktorID INTEGER PRIMARY KEY AUTOINCREMENT,
            doktorAdi TEXT,
            doktorSoyadi TEXT,
            doktorAlani TEXT,
            doktorHastane TEXT,
            doktorSifre TEXT
        )
    '''
    create_table_sql_randevu = '''
        CREATE TABLE IF NOT EXISTS randevu(
        randevuID INTEGER PRIMARY KEY AUTOINCREMENT,
        randevuTarihi TEXT,
        randevuSaati TEXT,
        hastaID INTEGER,
        doktorID INTEGER,
        doktorAlani TEXT,
        FOREIGN KEY (hastaID) REFERENCES hasta(hastaID),
        FOREIGN KEY (doktorID) REFERENCES doktor(doktorID),
        FOREIGN KEY (doktorAlani) REFERENCES doktor(doktorAlani)
        )
    '''

    create_table_sql_rapor = '''
        CREATE TABLE IF NOT EXISTS rapor(
        raporID INTEGER PRIMARY KEY AUTOINCREMENT,
        raporLink TEXT,
        hastaID INTEGER,
        doktorID INTEGER,
        FOREIGN KEY (hastaID) REFERENCES hasta(hastaID),
        FOREIGN KEY (doktorID) REFERENCES doktor(doktorID)
        )
    '''

    cursor.execute(create_table_sql)
    cursor.execute(create_table_sql_doktor)
    cursor.execute(create_table_sql_randevu)
    cursor.execute(create_table_sql_rapor)

    insert_data_sql = '''
        INSERT INTO hasta (hastaAdi, hastaSoyadi, hastaCinsiyet, hastaTarih, hastaTelefon, hastaAdres, hastaSifre) VALUES (?, ?, ?, ?, ?, ?, ?);
    '''

    insert_data_sql_doktor = '''
        INSERT INTO doktor (doktorAdi, doktorSoyadi, doktorAlani, doktorHastane, doktorSifre) VALUES (?, ?, ?, ?, ?)
    '''

    insert_data_sql_randevu = '''
        INSERT INTO randevu (randevuTarihi,randevuSaati,hastaID,doktorID, doktorAlani) VALUES (?, ?, ?, ?, ?)
    '''

    insert_data_sql_rapor = '''
        INSERT INTO rapor (raporLink, hastaID, doktorID) VALUES (?, ?, ?)
    '''

    data = [
        ('Alice', 'Smith', 'Kadın', '2024-05-09', '1234567890', '123 Street, City', 'sifre1'),
        ('Bob', 'Johnson', 'Erkek', '2024-05-10', '0987654321', '456 Street, Town', 'sifre2'),
        ('Charlie', 'Brown', 'Erkek', '2024-05-11', '1357924680', '789 Street, Village', 'sifre3')
    ]

    data2doktor = [
        ('Dr. Ali', 'Yılmaz', 'Genel Cerrahi', 'Şehir Hastanesi', 'sifre1'),
        ('Dr. Ayşe', 'Kara', 'Dahiliye', 'Devlet Hastanesi', 'sifre2'),
        ('Dr. Mehmet', 'Demir', 'KBB', 'Özel Hastane', 'sifre3'),
        ('Dr. Fatma', 'Yıldız', 'Kardiyoloji', 'Özel Hastane', 'sifre4'),
        ('Dr. Ahmet', 'Şahin', 'Göz Hastalıkları', 'Devlet Hastanesi', 'sifre5')
    ]

    data3randevu = [
        #     TARİH     SAAT hastaID doktorID ALAN
        ('2003-03-12', '12:00', '1', '1', 'Genel Cerrahi'),
        ('2003-03-11', '11:00', '1', '2', 'Dahiliye'),
        ('2024-05-25', '10:00', '2', '2', 'Dahiliye'),
        ('2024-05-25', '13:00', None, '3', 'KBB'),
        ('2024-05-25', '14:00', None, '4', 'Kardiyoloji'),
    ]

    data4rapor = [
        (
            'https://drive.google.com/file/d/0B-75m18wOOIvOEZQWGNvTmdDOE0/view?usp=sharing&resourcekey=0-JhZgSvmten4Rn5o9wcivxA',
            2, 5)
    ]

    cursor.executemany(insert_data_sql, data)
    cursor.executemany(insert_data_sql_doktor, data2doktor)
    cursor.executemany(insert_data_sql_randevu, data3randevu)
    cursor.executemany(insert_data_sql_rapor, data4rapor)


    select_data_sql = '''
        SELECT * FROM hasta
    '''

    select_data_sql_doktor = '''
        SELECT * FROM doktor
    '''

    select_data_sql_randevu = '''
        SELECT * FROM randevu
    '''

    select_data_sql_rapor = '''
        SELECT * FROM rapor
    '''

    cursor.execute(select_data_sql)

    for row in cursor.fetchall():
        print(row)

    cursor.execute(select_data_sql_doktor)

    for row in cursor.fetchall():
        print(row)

    cursor.execute(select_data_sql_randevu)

    for row in cursor.fetchall():
        print(row)

    cursor.execute(select_data_sql_rapor)

    for row in cursor.fetchall():
        print(row)

    conn.commit()
    conn.close()
