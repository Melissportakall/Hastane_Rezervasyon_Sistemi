from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
import sqlite3

def home(request):
    return render(request, 'index.html')

@csrf_exempt #güvenlik için
def doctor_login(request):
    global doktorKullanici
    global doktorIsim

    if request.method == 'POST':  # post isteği front endten gelen istek
        received_file = json.loads(request.body)
        print(received_file)

        db_file = 'otomasyon.db'

        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()

        select_data_sql = '''
                SELECT * FROM doktor WHERE doktorAdi = ? AND doktorSifre = ? AND doktorSoyadi = ?
            '''

        cursor.execute(select_data_sql,
                       ("Dr. " + received_file['username'], received_file['password'], received_file['last-name']))

        kullanici = cursor.fetchone()

        if kullanici is None:
            conn.close()
            return JsonResponse({'success': False, 'message': 'Kullanıcı bulunamadı'})

        doktorKullanici = kullanici[0]
        doktorIsim = kullanici[1]

        conn.close()

        return JsonResponse({'success': True, 'message': 'Kullanıcı bulundu', 'flg': 1})

    else:
        print("aaa views.py line 40")
        return JsonResponse({'success': False, 'resu': 404})


def patient_login(request):
    return JsonResponse({'success': True, 'message': 'Hasta girişi başarılı'})

def admin_login(request):
    return JsonResponse({'success': True, 'message': 'Yönetici girişi başarılı'})

def login(request):
    return JsonResponse({'success': False, 'message': 'Geçersiz istek'})

@csrf_exempt #güvenlik için
def test(request):
    global hastaKullanici
    global hastaIsim

    if request.method == 'POST': #post isteği front endten gelen istek
        received_file = json.loads(request.body)
        print(received_file)

        db_file = 'otomasyon.db'

        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()

        select_data_sql = '''
            SELECT * FROM hasta WHERE hastaAdi = ? AND hastaSifre = ? AND hastaSoyadi = ?
        '''

        cursor.execute(select_data_sql, (received_file['username'], received_file['password'],received_file['last-name']))

        kullanici = cursor.fetchone()

        if kullanici is None:
            conn.close()
            return JsonResponse({'success': False, 'message': 'Kullanıcı bulunamadı'})


        hastaKullanici = int(kullanici[0])
        hastaIsim = str(kullanici[1])

        conn.close()

        return JsonResponse({'success': True, 'message': 'Kullanıcı bulundu', 'flg': 1})

    else:
        print("aaa views.py line 40")
        return JsonResponse({'success': False, 'resu': 404})

def hastalogin_view(request):

 return render(request, 'hastaekran.html', {'isim': hastaIsim})

def doctorlogin_view(request):

 return render(request, 'doctorekran.html', {'isim': doktorIsim})

@csrf_exempt #güvenlik için
def patient_signup(request):
    if request.method == 'POST':
        received_data = json.loads(request.body)
        print(received_data)  # Gelen veriyi konsola yazdırma (hata ayıklama amaçlı)

        insert_data_sql = '''
            INSERT INTO hasta (hastaAdi, hastaSoyadi, hastaCinsiyet, hastaTarih, hastaTelefon, hastaAdres, hastaSifre)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        '''
        values = (
            received_data.get('name', ''),
            received_data.get('lastname', ''),
            received_data.get('gender', ''),
            received_data.get('date', ''),
            received_data.get('phone_no', ''),
            received_data.get('address', ''),
            received_data.get('password', '')
        )

        conn = sqlite3.connect('otomasyon.db')
        cursor = conn.cursor()

        cursor.execute(insert_data_sql, values)

        conn.commit()
        conn.close()

        return JsonResponse({'success': True, 'message': 'Patient signup successful'})

    else:
        return JsonResponse({'success': False, 'message': 'Invalid request method'})

@csrf_exempt #güvenlik için
def doctor_signup(request):
    if request.method == 'POST':
        received_data = json.loads(request.body)
        print(received_data)  # Gelen veriyi konsola yazdırma (hata ayıklama amaçlı)

        insert_data_sql = '''
            INSERT INTO doktor (doktorAdi, doktorSoyadi, doktorAlani, doktorHastane, doktorSifre)
            VALUES (?, ?, ?, ?, ?)
        '''
        values = (
            "Dr. " + received_data.get('doctor_name', ''),
            received_data.get('doctor_lastname', ''),
            received_data.get('doctor_major', ''),
            received_data.get('doctor_hospital', ''),
            received_data.get('doctor_signup_password', '')
        )

        conn = sqlite3.connect('otomasyon.db')
        cursor = conn.cursor()

        cursor.execute(insert_data_sql, values)

        conn.commit()
        conn.close()

        return JsonResponse({'success': True, 'message': 'Doctor signup successful'})

    else:
        return JsonResponse({'success': False, 'message': 'Invalid request method'})

def hastaisimtanimlama(request):
    hasta_isim = request.GET.get('hasta_isim')
    context = {'hasta_isim': hasta_isim}
    return render(request, 'hastaekran.html', context)
@csrf_exempt #güvenlik için
def randevu_ekrani(request):

    return render(request, 'randevu.html')
@csrf_exempt #güvenlik için
def hastarandevual(request):

    return render(request, 'randevual.html')
def rapor_view(request):

    return render(request, 'rapor.html')

@csrf_exempt #güvenlik için
def randevu_ekrani(request):
    connection = sqlite3.connect('otomasyon.db')
    cursor = connection.cursor()

    select_data_sql = '''
        SELECT randevu.randevuID, randevu.randevuTarihi, randevu.randevuSaati, hasta.hastaAdi AS hastaAdi, doktor.doktorAdi AS doktorAdi, doktor.doktorAlani AS doktorAlani
        FROM randevu 
        INNER JOIN doktor ON randevu.doktorID = doktor.doktorID 
        INNER JOIN hasta ON randevu.hastaID = hasta.hastaID
        WHERE randevu.hastaID = ?
    '''

    cursor.execute(select_data_sql,(hastaKullanici,))
    randevular = cursor.fetchall()

    if randevular is None:
        print("Hata")
    print(randevular)

    connection.close()

    return render(request, 'randevu.html', {'randevular': randevular, 'user_type': 'hasta', 'isim': hastaIsim})

@csrf_exempt #güvenlik için
def randevu_ekrani_doktor(request):
    connection = sqlite3.connect('otomasyon.db')
    cursor = connection.cursor()

    select_data_sql = '''
        SELECT randevu.randevuID, randevu.randevuTarihi, randevu.randevuSaati, hasta.hastaAdi AS hastaAdi, doktor.doktorAdi AS doktorAdi, doktor.doktorAlani AS doktorAlani
        FROM randevu 
        INNER JOIN doktor ON randevu.doktorID = doktor.doktorID 
        INNER JOIN hasta ON randevu.hastaID = hasta.hastaID
        WHERE randevu.doktorID = ? AND randevu.hastaID IS NOT NULL
    '''
    cursor.execute(select_data_sql, (doktorKullanici,))
    randevular = cursor.fetchall()

    print(doktorKullanici)

    connection.close()

    return render(request, 'randevu.html', {'randevular': randevular, 'user_type': 'doktor', 'isim': doktorIsim})

def randevual(request):
    return render(request, 'randevual.html', {'isim': hastaIsim})
@csrf_exempt #güvenlik için
def randevualkaydet(request):
    if request.method == 'POST':
        received_data = json.loads(request.body)
        print(received_data)

        connection = sqlite3.connect('otomasyon.db')
        cursor = connection.cursor()

        select_data_sql = '''
            SELECT randevu.randevuID, randevu.randevuTarihi, randevu.randevuSaati, doktor.doktorAdi AS doktorAdi, doktor.doktorAlani AS doktorAlani, doktor.doktorID
            FROM randevu 
            INNER JOIN doktor ON randevu.doktorID = doktor.doktorID 
            WHERE randevu.randevuTarihi = ? AND randevu.hastaID IS NULL
        '''

        cursor.execute(select_data_sql, (received_data['randevutarih'],))
        randevualkaydett = cursor.fetchall()

        print(received_data['randevutarih'])
        print(randevualkaydett)

        connection.close()

        table_html = render(request, 'table_partial.html', {'randevualkaydet': randevualkaydett}).content.decode("utf-8")
        return JsonResponse({'table_html': table_html})
    else:
        return JsonResponse({'message': 'Method not allowed'}, status=405)

@csrf_exempt #güvenlik için
def randevualekle(request):
    veriler = json.loads(request.body)["veriler"]

    print("Alınan veriler:", veriler)

    conn = sqlite3.connect('otomasyon.db')
    cursor = conn.cursor()

    insert_data_sql_randevu = '''
    INSERT INTO randevu (randevuTarihi, randevuSaati, hastaID, doktorID, doktorAlani) VALUES (?, ?, ?, ?, ?)
    '''

    print(veriler)

    values = [
        veriler[0],
        veriler[1],
        hastaKullanici,
        veriler[4],
        veriler[3]
    ]

    cursor.execute(insert_data_sql_randevu, values)

    delete_data_sql_randevu = '''
        DELETE FROM randevu
        WHERE randevuTarihi = ? 
        AND randevuSaati = ?
        AND hastaID IS NULL 
        AND doktorID = ?
        AND doktorAlani = ?
    '''


    valuesDelete = [
        veriler[0],
        veriler[1],
        veriler[4],
        veriler[3]
    ]

    cursor.execute(delete_data_sql_randevu, valuesDelete)

    select_data_sql_randevu = '''
        SELECT * FROM randevu
    '''

    cursor.execute(select_data_sql_randevu)

    for row in cursor.fetchall():
        print(row)


    conn.commit()
    conn.close()

    return JsonResponse({"success": True})

@csrf_exempt #güvenlik için
def randevuiptal(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        randevu_id = data.get('randevuID')

        conn = sqlite3.connect('otomasyon.db')

        with conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE randevu SET hastaID = NULL WHERE randevuID = ?", (randevu_id,))
            updated = cursor.rowcount

        if updated:
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'error': 'Randevu bulunamadı'})

def yonetici_loginview(request):

    return render(request, 'yoneticiekran.html')

