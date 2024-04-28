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
        {"id": 1, "org_name": "Kızılay Derneği (Türk Kızılayı)", "subject": "Humanitarian aid", "description": "Türk Kızılayı olarak da bilinen Kızılay Derneği, acil durumlar, felaketler ve çatışmalar sırasında yardım ve destek sağlayan bir insani yardım kuruluşudur. Kan bağışı, felaket yardımı ve sağlık hizmetleri gibi çeşitli hizmetler sunar."},
        {"id": 2, "org_name": "Yeşilay Cemiyeti (Derneği)", "subject": "Public health", "description": "Yeşilay Cemiyeti, bağımlılık ve madde kullanımıyla mücadelede kamu sağlığına odaklanır. Bağımlılıkla mücadelede eğitim, önleme programları ve rehabilitasyon hizmetleri sunar."},
        {"id": 3, "org_name": "UNICEF Türkiye Milli Komitesi", "subject": "Child welfare", "description": "UNICEF, Türkiye'de Milli Komite aracılığıyla faaliyet gösterir. Çocuk haklarını destekler, ihtiyaç sahibi çocuklara sağlık, eğitim ve koruma sağlar ve onların refahı için çalışır."},
        {"id": 4, "org_name": "Uluslararası Çocuk Merkezi", "subject": "Child welfare", "description": "Bu, 'International Children's Center'ın Türkçe çevirisidir. Muhtemelen uluslararası ölçekte çocukların refahı ve gelişimi için çalışan bir organizasyonu ifade eder, ancak spesifik detaylar değişebilir."},
        {"id": 5, "org_name": "Türk Psikologlar Derneği", "subject": "Psychology", "description": "Türk Psikologlar Derneği, Türkiye'deki psikologlar için bir meslek örgütüdür. Psikolojiyi bir bilim olarak tanıtmak, eğitim ve eğitim sağlamak ve nüfusun ruh sağlığı ihtiyaçlarını savunmak amacıyla çalışırlar."},
        {"id": 6, "org_name": "Türk Hemşireler Derneği", "subject": "Nursing", "description": "Türk Hemşireler Derneği, Türkiye'deki hemşireleri temsil eder. Hemşirelik mesleğini ilerletmek, hemşirelere destek ve kaynak sağlamak ve yüksek standartlarda hemşirelik uygulamasını ve hasta bakımını teşvik etmek için çalışırlar."},
        {"id": 7, "org_name": "Türkiye İlaç Sanayii Derneği (TSİD)", "subject": "Pharmaceuticals", "description": "Türkiye İlaç Sanayii Derneği, Türkiye'deki ilaç şirketlerini temsil eder. İlaç endüstrisi ile ilgili konular üzerinde, araştırma, geliştirme ve düzenlemeler gibi konularda çalışırlar."},
        {"id": 8, "org_name": "Araştırmacı İlaç Firmaları Derneği (AİFD)", "subject": "Pharmaceuticals", "description": "Bu, 'Association of Research-based Pharmaceutical Companies'nin Türkçe çevirisidir. Muhtemelen araştırma odaklı ilaç şirketlerini temsil eder."},
        {"id": 9, "org_name": "Özel Hastaneler ve Sağlık Kuruluşları Derneği (OHSAD)", "subject": "Healthcare", "description": "Özel Hastaneler ve Sağlık Kuruluşları Derneği, Türkiye'deki özel sağlık tesislerini temsil eder. Özel sağlık hizmeti sunumu, düzenleme ve kalite iyileştirmesi ile ilgili konularda çalışırlar."},
        {"id": 10, "org_name": "Sağlık Gönüllüleri Türkiye Derneği", "subject": "Healthcare", "description": "Sağlık Gönüllüleri Türkiye Derneği, Türkiye'de sağlık hizmetleri, sağlık eğitimi ve insani yardım sağlamak amacıyla gönüllüleri harekete geçiren bir organizasyondur."},
        {"id": 11, "org_name": "Sığınmacılar ve Göçmenlerle Dayanışma Derneği (SGDD)", "subject": "Refugee support", "description": "Sığınmacılar ve Göçmenlerle Dayanışma Derneği, Türkiye'deki sığınmacılara ve göçmenlere destek sağlamayı amaçlar. Yasal yardım, eğitim, sağlık hizmetleri ve sosyal destek gibi çeşitli hizmetler sunarlar."},
        {"id": 12, "org_name": "İltica ve Göç Araştırmaları Merkezi Derneği (İGAM)", "subject": "Refugee research", "description": "İltica ve Göç Araştırmaları Merkezi, Türkiye'deki mülteciler, sığınmacılar ve göç konularıyla ilgili araştırma ve savunma yapar. Mülteciler ve göçmenlerle ilgili politikaları ve uygulamaları iyileştirmeyi amaçlarlar."},
        {"id": 13, "org_name": "Mülteci Destek Derneği (MUDEM)", "subject": "Refugee support", "description": "Mülteci Destek Derneği, Türkiye'deki mültecilere yardım ve destek sağlar. Eğitim, sağlık hizmetleri, geçim desteği ve mültecilerin sosyal entegrasyonu için programlar sunarlar."},
        {"id": 14, "org_name": "Sağlık Gereçleri Üreticileri ve Temsilcileri Derneği (SADER)", "subject": "Medical equipment", "description": "Sağlık Gereçleri Üreticileri ve Temsilcileri Derneği, Türkiye'de tıbbi ekipman üretimi ve dağıtımıyla ilgilenen şirketleri temsil eder. Tıbbi cihazlar için kalite standartları, düzenlemeler ve pazar erişimi konularında çalışırlar."},
        {"id": 15, "org_name": "Araştırmacı Tıp Teknolojileri Üreticileri Derneği (ARTED)", "subject": "Medical technology", "description": "Araştırmacı Tıp Teknolojileri Üreticileri Derneği, Türkiye'de tıbbi teknolojilerin araştırılması, geliştirilmesi ve üretimiyle ilgilenen şirketleri temsil eder. Tıbbi cihazlar için inovasyonu, kalite standartlarını ve pazar erişimini teşvik ederler."},
        {"id": 16, "org_name": "Tüm Tıbbi Cihaz Üreticileri Derneği (TUDER)", "subject": "Medical equipment", "description": "Tüm Tıbbi Cihaz Üreticileri Derneği, Türkiye'deki tıbbi cihaz endüstrisinde faaliyet gösteren şirketleri temsil eder. Tıbbi cihazlar için düzenleme, pazar erişimi ve endüstri standartları konularında çalışırlar."},
        {"id": 17, "org_name": "Acil Ambulans Hekimleri Derneği (AAHD)", "subject": "Emergency medicine", "description": "Acil Ambulans Hekimleri Derneği, Türkiye'deki ambulans hizmetlerinde çalışan acil tıp profesyonellerini temsil eder. Acil tıbbi bakım, eğitim ve ambulans personeli için protokoller konusunda çalışırlar."},
        {"id": 18, "org_name": "Türkiye Gazeteciler Cemiyeti (İstanbul)", "subject": "Journalism", "description": "Türkiye Gazeteciler Cemiyeti, İstanbul'da faaliyet gösteren gazeteciler için bir meslek örgütüdür. Basın özgürlüğünü korumak, gazetecilerin haklarını savunmak ve gazetecilikte etik standartları teşvik etmek için çalışırlar."},
        {"id": 19, "org_name": "Gazeteciler Cemiyeti (Ankara)", "subject": "Journalism", "description": "Gazeteciler Cemiyeti, Ankara'da faaliyet gösteren gazetecilere hizmet veren bir örgütür. İstanbul'daki muadili gibi, basın özgürlüğünü korurlar, gazetecilere destek olurlar ve gazetecilikte profesyonel standartları yükseltmeyi amaçlarlar."},
        {"id": 20, "org_name": "Medya ve İletişim Akademisi Derneği (MİADER)", "subject": "Media and communication", "description": "Medya ve İletişim Akademisi, Türkiye'de medya ve iletişim alanında eğitimi ve araştırmayı teşvik eden bir organizasyondur. Medya profesyonelleri ve öğrenciler için eğitim, atölye çalışmaları ve seminerler düzenlerler."},
        {"id": 21, "org_name": "Türkiye Sağlık Vakfı (TSV)", "subject": "Healthcare", "description": "Türkiye Sağlık Vakfı, Türkiye'de halk sağlığını iyileştirmeye adanmış bir kar amacı gütmeyen bir organizasyondur. Sağlık eğitimi, hastalık önleme ve dezavantajlı toplulukların sağlık hizmetlerine erişimini destekleyen çeşitli projeler üzerinde çalışırlar."},
        {"id": 22, "org_name": "Sağlık ve Sosyal Yardım Vakfı (SSYV)", "subject": "Healthcare and social assistance", "description": "Sağlık ve Sosyal Yardım Vakfı, ihtiyaç sahibi bireylere ve toplumlara destek ve yardım sağlar. Sağlık hizmetleri, sosyal hizmetler ve insani yardım konularında çalışırlar."},
        {"id": 23, "org_name": "Anne Çocuk Eğitim Vakfı (AÇEV)", "subject": "Child and mother education", "description": "Anne Çocuk Eğitim Vakfı, Türkiye'de eğitimin kalitesini artırmayı ve erken çocukluk döneminin gelişimini desteklemeyi amaçlar. Ebeveynlere ve çocuklara yönelik eğitim programları ve kaynaklar sağlarlar."},
        {"id": 24, "org_name": "TOHUM Otizim Vakfı", "subject": "Autism", "description": "TOHUM Otizim Vakfı, Türkiye'de otizm spektrum bozukluğu olan bireylerin ve ailelerinin yaşamlarını iyileştirmeyi amaçlar. Otizm farkındalığı yaratır, erken müdahale hizmetleri sağlar ve otizmli bireylerin eğitim ve istihdamına destek olur."},
        {"id": 25, "org_name": "İnsan Kaynağını Geliştirme Vakfı (IKGV)", "subject": "Human resources development", "description": "İnsan Kaynağını Geliştirme Vakfı, Türkiye'de işgücü yeteneklerini geliştirmeye odaklanan bir vakıftır. Eğitim, meslek edindirme ve istihdam projeleri üzerinde çalışırlar."},
        {"id": 26, "org_name": "Türkiye Ekonomik ve Sosyal Etüdler Vakfı (TESEV)", "subject": "Economic and social studies", "description": "Türkiye Ekonomik ve Sosyal Etüdler Vakfı, Türkiye'deki ekonomik ve sosyal kalkınmayı desteklemeyi amaçlayan bir düşünce kuruluşudur. Araştırmalar yapar, politika önerileri sunar ve kamuoyunu bilgilendirirler."},
        {"id": 27, "org_name": "Türk Kalp Vakfı", "subject": "Heart health", "description": "Türk Kalp Vakfı, Türkiye'de kalp sağlığını iyileştirmeyi amaçlar. Kalp hastalıklarıyla mücadelede farkındalık yaratır, eğitim programları düzenler ve kalp sağlığına erişimi artırmayı hedefler."},
        {"id": 28, "org_name": "Çorbada Tuzun Olsun", "subject": "Social aid", "description": "Çorbada Tuzun Olsun, Türkiye'de yoksullara ve ihtiyaç sahiplerine yardım sağlamayı amaçlayan bir sosyal yardım kuruluşudur. Gıda yardımı, barınma destekleri ve diğer temel ihtiyaçların karşılanması için çalışırlar."}
    ])

    app.run(debug=True)
