# Python_ornekler1

## English

This repository contains a simple Python function to reverse an array (list) in-place. The function utilizes a two-pointer approach to swap elements from the start and end of the list until the entire list is reversed.

#### Problem Statement

Given an array of integers, the goal is to reverse the array in-place without using any additional arrays. This means the original array should be modified to contain the elements in reverse order.

#### Example

```
Input: [1, 2, 3, 4, 5]
Output: [5, 4, 3, 2, 1]
```



#### Solution
The solution uses a two-pointer technique:

One pointer starts at the beginning of the array (left), and the other starts at the end (right).
The elements at these two positions are swapped, and the pointers move towards the center.
This process continues until the pointers meet or cross each other.

#### How to Use?
Clone this repository to your local machine.
Run the Python script to see the reverse function in action.


#### Example Usage
nums = [1, 2, 3, 4, 5]
print("Original Array:", nums)
reversed_nums = reverse_array(nums)
print("Reversed Array:", reversed_nums)

#### Output
Original Array: [1, 2, 3, 4, 5]
Reversed Array: [5, 4, 3, 2, 1]

#### Contributing
If you'd like to contribute to this project, feel free to fork the repository and submit a pull request.

#### License
This project is licensed under the MIT License. Feel free to use and modify the code as needed.



## Türkçe

Bu depo, bir diziyi (listeyi) yerinde tersine çevirmek için basit bir Python fonksiyonu içeriyor. Fonksiyon, dizinin başından ve sonundan elemanları değiştirerek tüm diziyi tersine çeviren bir iki gösterge yaklaşımını kullanır.

#### Problem Tanımı
Bir tam sayı dizisi verildiğinde, diziyi yerinde tersine çevirmelisiniz, yani ekstra bir dizi kullanmadan orijinal dizi üzerinde işlem yapmalısınız. Bu, dizinin elemanlarının ters sırayla düzenlenmesi gerektiği anlamına gelir.

#### Örnek
Girdi: [1, 2, 3, 4, 5]
Çıktı: [5, 4, 3, 2, 1]


#### Çözüm
Çözüm, iki gösterge tekniğini kullanır:

Bir gösterge dizinin başından (left), diğeri ise sonundan (right) başlar.
Bu iki pozisyondaki elemanlar değiştirilir ve göstergeler merkeze doğru hareket eder.
Bu işlem, göstergeler birbirine yaklaşana veya birbirini geçene kadar devam eder.


#### Kullanım
Bu depoyu yerel bilgisayarınıza klonlayın.
Python betiğini çalıştırarak tersine çevirme fonksiyonunu gözlemleyin.


#### Örnek Kullanım
nums = [1, 2, 3, 4, 5]
print("Orijinal Dizi:", nums)
reversed_nums = reverse_array(nums)
print("Ters Çevrilmiş Dizi:", reversed_nums)


#### Çıktı
Orijinal Dizi: [1, 2, 3, 4, 5]
Ters Çevrilmiş Dizi: [5, 4, 3, 2, 1]

#### Katkı Sağlamak
Bu projeye katkı sağlamak isterseniz, depo üzerinde fork yapabilir ve bir pull request gönderebilirsiniz.

#### Lisans
Bu proje MIT Lisansı altında lisanslanmıştır. Kodu ihtiyacınıza göre kullanabilir ve değiştirebilirsiniz.





