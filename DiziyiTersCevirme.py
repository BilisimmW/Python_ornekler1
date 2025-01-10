def reverse_array(nums):
    # Başlangıç ve bitiş göstergeleri
    left = 0
    right = len(nums) - 1
    
    # Göstergeler ortada buluşana kadar devam et
    while left < right:
        # Elemanları değiştir
        nums[left], nums[right] = nums[right], nums[left]
        
        # Göstergeleri kaydır
        left += 1
        right -= 1
    
    return nums

# Örnek girdi
nums = [1, 2, 3, 4, 5]
print("Orijinal Dizi:", nums)

# Fonksiyonu çağır ve çıktıyı yazdır
reversed_nums = reverse_array(nums)
print("Ters Çevrilmiş Dizi:", reversed_nums)
