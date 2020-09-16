#from flask import Flask
#
#app = Flask(__name__) 
#
#'''
#Pythonda özel bir değişkendir. bir uygulama oluşturduk. şimdi bunu çalıştırmak 
#gerekiyor. Bu uygulamamızı şöyşe çalıştıracağız. biz python dosyalarını terminalden direk çalıştıracak #burdaki __name__ in ismi __main__ olacak. o yüzden bunun bir if koşulu ile kontrol edilmesi gerekiyor. #Buradaki name değişkeni main e eşit mi diye kontrol ediyorum. yani bu dosya direk terminalden mi #çalıştırılmış diye onu kontrol ediyorum böylelikle. eğer öyleyse buradaki web sunucumu çalıştırmam #gerekiyor. bunun için de app.run() diyerek lokaldaki web sunucumu çalıştırıyorum. Eğer biz geliştirici #ortamında isek bu parantezin içine debug = True şeklinde yazmam gerekiyor. Eğer web sitesinde  hata #varsa bize hatalarımızı söyleyecek ve böylelikle hatalarımzıı ortaya çıkarmamızı sağlayacak. 
#'''
#
#if __name__ == "__main__":
#    app.run(debug = True)
#
##Aslında bizim web sayfamızın çalışması için gerekli iskeleti kurduk. şimdi bu dosyayı çalıştıralım. #Bu çalıştırıldığında web sayfamızın çalıştığını gösteren 4 mesaj gelir. şu an bizim web sayfamız 127.0.#0.1:5000 de çalışıyormuş ve port'u 5000 miş. websayfasına git ve 127.0.0.1:5000 ya da localhost:5000 #yaz. Not Found un döndüğü görülür. Neden not fount hatası geldi. çünkü biz bu url ye erişmek #istiyoruz. yani server ımıza diyoruz ki sen bana bu url yi ve yani bir request yapıyoruz ama bir #response göremiyoruz. Buradaki response nedir? bu response html dosyası ya da bir string bile #dönebilir. Bu şekilde bir response dönmesi için flask daki url yapısını da öğrenmem gerekiyor. Şimdi #bu 5000 benim kök dizinim. Bu kök dizinine gelddiğimde bir respınse dönmem gerekiyor. Yani app den #hemen sonra bir response dönmesini söylemem gerekiyor. Bunları da python'daki decorator yapıları ile #oluyor. Bu decorator yapıları özel yapılardır ve direk fonksiyonlardan önce gelir ve @app.route("/") #şeklinde bir decorator kullanılır. yani eğer / a erişilirse web sayfasınbda burada bir fonksiyon #çalıştırmasını söylüyoruz. Diğer bir değişle eğer / kök dizininde bir request gelirse bu durumda @app.route("/") bize altındaki fonksiyonu çalıştıracak ve bir http respons dönmesini söyleyeceğiz. Bu response string de olabilir http sayfası da olabilir. Bunu öğrenmemiz çok önemli. İşte flask daki url yapıları bu şekilde. 




from flask import Flask

app = Flask(__name__)

# İlk olarak bunu  yaz
@app.route("/")
def head():
    return "Hello World!"

# İkinci olarak bunu yaz ve request 
@app.route("/second")
def second():
    return "This is the second page"

# Üçüncü olarak bunu yaz
@app.route("/third/subthird")
def third():
    return "This is the subpage of third page"

# Dördüncü olarak yaz. Dinamik URL yapısı ne demek. En son kısmın sürekli değiştiği URL yapılarıdır
@app.route("/forth/<string:id>")
def forth(id):
    return f'Id of this page is {id}'

if __name__== "__main__":
    app.run(debug=True)