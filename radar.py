cheklov = int(input("Cheklangan tezlikni kiriting: "))
tezlik = int(input("Tezligini kiriting: "))
buzilishi = int(input("Nechinchi qoida buzilishi: "))
farq = tezlik - cheklov
BHM = 375_000
match farq:
    case x if (cheklov or tezlik or buzilishi) < 0:
        print("Siz noto'g'ri qiymat kiritdingiz!")
    case y if farq <= 0:
        print("Jarima qo'llanilmaydi!")
    case z if 0 < farq <= 20 and buzilishi == 1:
        print("Jarima: ", BHM, "so'm bo'ladi!")
    case a if 0 < farq <= 20 and buzilishi == 2:
        print("Jarima: ",BHM * 5,"so'm bo'ladi!")
    case b if 0 < farq <= 20 and buzilishi >= 3:
        print("Jarima: ", BHM * 15,"so'm bo'ladi va yana 1 yilga haydovchilik guvohnomasidan mahrum etilsin!")
    case c if 21 <= farq <= 40 and buzilishi == 1:
        print("Jarima: ", BHM *5, "so'm bo'ladi!")
    case d if 21 <= farq <= 40 and buzilishi >= 2:
        print("Jarima: ", BHM * 15,"so'm bo'ladi va yana 1 yilga haydovchilik guvohnomasidan mahrum etilsin!")
    case e if 40 < farq and buzilishi == 1:
        print("Jarima: ", BHM *9, "so'm bo'ladi!")
    case f if 40 < farq and buzilishi >= 2:
        print("Jarima: ", BHM * 25,"so'm bo'ladi va yana 2 yilga haydovchilik guvohnomasidan mahrum etilsin!")
    case _:
        print("Xatolik")