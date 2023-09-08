largest = 0   # degisken tanimliyoruz, een buyuk sayiyi tutmak icin

input_numbers = input("aralarinda bosluk olacak sekilde 5 adet sayi giriniz: ")


numbers = input_numbers.split()   # input u split ile listeye ceviriyoruz


if len(numbers) != 5:   # kullanicinin 5 sayi girdiginden emin olmak icin kontrol.
    print("Lutfen 5 adet sayi giriniz")
else:
    for num in numbers:
        try: # girilen sey sayi mi, dene, degilse hata yaz.
            num = int(num) # string i int a ceviriyoruz
            if num > largest:  # her iterasyonda ele aldigimiz sayiyi largest degiskeni ile kiyasliyoruz
                largest = num  # eger buyuk ise yeni atama yapiyoruz
        except ValueError:
            print(f"girdiginiz '{num}' degeri bir sayi degildir!")


    print(f"verilen sayilarin en buyugu: {largest}")
    