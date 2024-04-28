# -*- coding: cp1254 -*-
import sys
import locale

from flask import Flask, jsonify, request

app = Flask(__name__)

organizations = []

@app.route('/organizations', methods=['POST'])
def register_organization():
    data = request.json
    org_id = len(organizations) + 1  # Generate a unique ID for the organization
    organization = {
        "id": org_id,
        "org_name": data.get("org_name", " -*- coding: cp1254 -*-"),
        "subject": data.get("subject"),
        "description": data.get("description")  # Add description field
    }
    organizations.append(organization)
    return jsonify({"message": "Organization registered successfully", "id": org_id}), 201

@app.route('/organizations', methods=['GET'])
def list_organizations():
    return jsonify(organizations)

if __name__ == '__main__':
    # Adding provided organization names and descriptions
    organizations.extend([
        {"id": 1, "org_name": "K�z�lay Derne�i (T�rk K�z�lay�)", "subject": "Humanitarian aid", "description": "T�rk K�z�lay� olarak da bilinen K�z�lay Derne�i, acil durumlar, felaketler ve �at��malar s�ras�nda yard�m ve destek sa�layan bir insani yard�m kurulu�udur. Kan ba����, felaket yard�m� ve sa�l�k hizmetleri gibi �e�itli hizmetler sunar."},
        {"id": 2, "org_name": "Ye�ilay Cemiyeti (Derne�i)", "subject": "Public health", "description": "Ye�ilay Cemiyeti, ba��ml�l�k ve madde kullan�m�yla m�cadelede kamu sa�l���na odaklan�r. Ba��ml�l�kla m�cadelede e�itim, �nleme programlar� ve rehabilitasyon hizmetleri sunar."},
        {"id": 3, "org_name": "UNICEF T�rkiye Milli Komitesi", "subject": "Child welfare", "description": "UNICEF, T�rkiye'de Milli Komite arac�l���yla faaliyet g�sterir. �ocuk haklar�n� destekler, ihtiya� sahibi �ocuklara sa�l�k, e�itim ve koruma sa�lar ve onlar�n refah� i�in �al���r."},
        {"id": 4, "org_name": "Uluslararas� �ocuk Merkezi", "subject": "Child welfare", "description": "Bu, 'International Children's Center'�n T�rk�e �evirisidir. Muhtemelen uluslararas� �l�ekte �ocuklar�n refah� ve geli�imi i�in �al��an bir organizasyonu ifade eder, ancak spesifik detaylar de�i�ebilir."},
        {"id": 5, "org_name": "T�rk Psikologlar Derne�i", "subject": "Psychology", "description": "T�rk Psikologlar Derne�i, T�rkiye'deki psikologlar i�in bir meslek �rg�t�d�r. Psikolojiyi bir bilim olarak tan�tmak, e�itim ve e�itim sa�lamak ve n�fusun ruh sa�l��� ihtiya�lar�n� savunmak amac�yla �al���rlar."},
        {"id": 6, "org_name": "T�rk Hem�ireler Derne�i", "subject": "Nursing", "description": "T�rk Hem�ireler Derne�i, T�rkiye'deki hem�ireleri temsil eder. Hem�irelik mesle�ini ilerletmek, hem�irelere destek ve kaynak sa�lamak ve y�ksek standartlarda hem�irelik uygulamas�n� ve hasta bak�m�n� te�vik etmek i�in �al���rlar."},
        {"id": 7, "org_name": "T�rkiye �la� Sanayii Derne�i (TS�D)", "subject": "Pharmaceuticals", "description": "T�rkiye �la� Sanayii Derne�i, T�rkiye'deki ila� �irketlerini temsil eder. �la� end�strisi ile ilgili konular �zerinde, ara�t�rma, geli�tirme ve d�zenlemeler gibi konularda �al���rlar."},
        {"id": 8, "org_name": "Ara�t�rmac� �la� Firmalar� Derne�i (A�FD)", "subject": "Pharmaceuticals", "description": "Bu, 'Association of Research-based Pharmaceutical Companies'nin T�rk�e �evirisidir. Muhtemelen ara�t�rma odakl� ila� �irketlerini temsil eder."},
        {"id": 9, "org_name": "�zel Hastaneler ve Sa�l�k Kurulu�lar� Derne�i (OHSAD)", "subject": "Healthcare", "description": "�zel Hastaneler ve Sa�l�k Kurulu�lar� Derne�i, T�rkiye'deki �zel sa�l�k tesislerini temsil eder. �zel sa�l�k hizmeti sunumu, d�zenleme ve kalite iyile�tirmesi ile ilgili konularda �al���rlar."},
        {"id": 10, "org_name": "Sa�l�k G�n�ll�leri T�rkiye Derne�i", "subject": "Healthcare", "description": "Sa�l�k G�n�ll�leri T�rkiye Derne�i, T�rkiye'de sa�l�k hizmetleri, sa�l�k e�itimi ve insani yard�m sa�lamak amac�yla g�n�ll�leri harekete ge�iren bir organizasyondur."},
        {"id": 11, "org_name": "S���nmac�lar ve G��menlerle Dayan��ma Derne�i (SGDD)", "subject": "Refugee support", "description": "S���nmac�lar ve G��menlerle Dayan��ma Derne�i, T�rkiye'deki s���nmac�lara ve g��menlere destek sa�lamay� ama�lar. Yasal yard�m, e�itim, sa�l�k hizmetleri ve sosyal destek gibi �e�itli hizmetler sunarlar."},
        {"id": 12, "org_name": "�ltica ve G�� Ara�t�rmalar� Merkezi Derne�i (�GAM)", "subject": "Refugee research", "description": "�ltica ve G�� Ara�t�rmalar� Merkezi, T�rkiye'deki m�lteciler, s���nmac�lar ve g�� konular�yla ilgili ara�t�rma ve savunma yapar. M�lteciler ve g��menlerle ilgili politikalar� ve uygulamalar� iyile�tirmeyi ama�larlar."},
        {"id": 13, "org_name": "M�lteci Destek Derne�i (MUDEM)", "subject": "Refugee support", "description": "M�lteci Destek Derne�i, T�rkiye'deki m�ltecilere yard�m ve destek sa�lar. E�itim, sa�l�k hizmetleri, ge�im deste�i ve m�ltecilerin sosyal entegrasyonu i�in programlar sunarlar."},
        {"id": 14, "org_name": "Sa�l�k Gere�leri �reticileri ve Temsilcileri Derne�i (SADER)", "subject": "Medical equipment", "description": "Sa�l�k Gere�leri �reticileri ve Temsilcileri Derne�i, T�rkiye'de t�bbi ekipman �retimi ve da��t�m�yla ilgilenen �irketleri temsil eder. T�bbi cihazlar i�in kalite standartlar�, d�zenlemeler ve pazar eri�imi konular�nda �al���rlar."},
        {"id": 15, "org_name": "Ara�t�rmac� T�p Teknolojileri �reticileri Derne�i (ARTED)", "subject": "Medical technology", "description": "Ara�t�rmac� T�p Teknolojileri �reticileri Derne�i, T�rkiye'de t�bbi teknolojilerin ara�t�r�lmas�, geli�tirilmesi ve �retimiyle ilgilenen �irketleri temsil eder. T�bbi cihazlar i�in inovasyonu, kalite standartlar�n� ve pazar eri�imini te�vik ederler."},
        {"id": 16, "org_name": "T�m T�bbi Cihaz �reticileri Derne�i (TUDER)", "subject": "Medical equipment", "description": "T�m T�bbi Cihaz �reticileri Derne�i, T�rkiye'deki t�bbi cihaz end�strisinde faaliyet g�steren �irketleri temsil eder. T�bbi cihazlar i�in d�zenleme, pazar eri�imi ve end�stri standartlar� konular�nda �al���rlar."},
        {"id": 17, "org_name": "Acil Ambulans Hekimleri Derne�i (AAHD)", "subject": "Emergency medicine", "description": "Acil Ambulans Hekimleri Derne�i, T�rkiye'deki ambulans hizmetlerinde �al��an acil t�p profesyonellerini temsil eder. Acil t�bbi bak�m, e�itim ve ambulans personeli i�in protokoller konusunda �al���rlar."},
        {"id": 18, "org_name": "T�rkiye Gazeteciler Cemiyeti (�stanbul)", "subject": "Journalism", "description": "T�rkiye Gazeteciler Cemiyeti, �stanbul'da faaliyet g�steren gazeteciler i�in bir meslek �rg�t�d�r. Bas�n �zg�rl���n� korumak, gazetecilerin haklar�n� savunmak ve gazetecilikte etik standartlar� te�vik etmek i�in �al���rlar."},
        {"id": 19, "org_name": "Gazeteciler Cemiyeti (Ankara)", "subject": "Journalism", "description": "Gazeteciler Cemiyeti, Ankara'da faaliyet g�steren gazetecilere hizmet veren bir �rg�t�r. �stanbul'daki muadili gibi, bas�n �zg�rl���n� korurlar, gazetecilere destek olurlar ve gazetecilikte profesyonel standartlar� y�kseltmeyi ama�larlar."},
        {"id": 20, "org_name": "Medya ve �leti�im Akademisi Derne�i (M�ADER)", "subject": "Media and communication", "description": "Medya ve �leti�im Akademisi, T�rkiye'de medya ve ileti�im alan�nda e�itimi ve ara�t�rmay� te�vik eden bir organizasyondur. Medya profesyonelleri ve ��renciler i�in e�itim, at�lye �al��malar� ve seminerler d�zenlerler."},
        {"id": 21, "org_name": "T�rkiye Sa�l�k Vakf� (TSV)", "subject": "Healthcare", "description": "T�rkiye Sa�l�k Vakf�, T�rkiye'de halk sa�l���n� iyile�tirmeye adanm�� bir kar amac� g�tmeyen bir organizasyondur. Sa�l�k e�itimi, hastal�k �nleme ve dezavantajl� topluluklar�n sa�l�k hizmetlerine eri�imini destekleyen �e�itli projeler �zerinde �al���rlar."},
        {"id": 22, "org_name": "Sa�l�k ve Sosyal Yard�m Vakf� (SSYV)", "subject": "Healthcare and social assistance", "description": "Sa�l�k ve Sosyal Yard�m Vakf�, ihtiya� sahibi bireylere ve toplumlara destek ve yard�m sa�lar. Sa�l�k hizmetleri, sosyal hizmetler ve insani yard�m konular�nda �al���rlar."},
        {"id": 23, "org_name": "Anne �ocuk E�itim Vakf� (A�EV)", "subject": "Child and mother education", "description": "Anne �ocuk E�itim Vakf�, T�rkiye'de e�itimin kalitesini art�rmay� ve erken �ocukluk d�neminin geli�imini desteklemeyi ama�lar. Ebeveynlere ve �ocuklara y�nelik e�itim programlar� ve kaynaklar sa�larlar."},
        {"id": 24, "org_name": "TOHUM Otizim Vakf�", "subject": "Autism", "description": "TOHUM Otizim Vakf�, T�rkiye'de otizm spektrum bozuklu�u olan bireylerin ve ailelerinin ya�amlar�n� iyile�tirmeyi ama�lar. Otizm fark�ndal��� yarat�r, erken m�dahale hizmetleri sa�lar ve otizmli bireylerin e�itim ve istihdam�na destek olur."},
        {"id": 25, "org_name": "�nsan Kayna��n� Geli�tirme Vakf� (IKGV)", "subject": "Human resources development", "description": "�nsan Kayna��n� Geli�tirme Vakf�, T�rkiye'de i�g�c� yeteneklerini geli�tirmeye odaklanan bir vak�ft�r. E�itim, meslek edindirme ve istihdam projeleri �zerinde �al���rlar."},
        {"id": 26, "org_name": "T�rkiye Ekonomik ve Sosyal Et�dler Vakf� (TESEV)", "subject": "Economic and social studies", "description": "T�rkiye Ekonomik ve Sosyal Et�dler Vakf�, T�rkiye'deki ekonomik ve sosyal kalk�nmay� desteklemeyi ama�layan bir d���nce kurulu�udur. Ara�t�rmalar yapar, politika �nerileri sunar ve kamuoyunu bilgilendirirler."},
        {"id": 27, "org_name": "T�rk Kalp Vakf�", "subject": "Heart health", "description": "T�rk Kalp Vakf�, T�rkiye'de kalp sa�l���n� iyile�tirmeyi ama�lar. Kalp hastal�klar�yla m�cadelede fark�ndal�k yarat�r, e�itim programlar� d�zenler ve kalp sa�l���na eri�imi art�rmay� hedefler."},
        {"id": 28, "org_name": "�orbada Tuzun Olsun", "subject": "Social aid", "description": "�orbada Tuzun Olsun, T�rkiye'de yoksullara ve ihtiya� sahiplerine yard�m sa�lamay� ama�layan bir sosyal yard�m kurulu�udur. G�da yard�m�, bar�nma destekleri ve di�er temel ihtiya�lar�n kar��lanmas� i�in �al���rlar."}
    ])

    app.run(debug=True)
