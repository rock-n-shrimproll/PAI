# Лабораторная работа №3

### Тема: Выделение контуров на изображении

|**Студент:**|*Долидзе Александра*|
|------------|--------------|
|**Группа:** |*Б18-514*     |
|**Вариант:**|*3*           |

#### Задание:

Оператор Собеля 3x3
```
    -1 -2 -1
Gx = 0 0 0    * A
     1 2 1
```
```
     -1 0 1
Gy = -2 0 2   * A
     -1 0 1
```
---

### Пример №1

|**Исходное изображение**|**Полутоновое изображение**|
|------------------------|---------------------------|
|![](original/eagle.jpg)|![](res/eagle/semitone_eagle.jpg)|

|**Gx**|**Gy**|**G**|
|------|------|-----|
|![](res/eagle/resx_eagle.jpg)|![](res/eagle/resy_eagle.jpg)|![](res/eagle/res_eagle.jpg)|

|**T=124**|**T=126**|**T=128**|**T=130**|
|---------|---------|---------|------|
|![](res/eagle/bin_t124_eagle.jpg)|![](res/eagle/bin_t126_eagle.jpg)|![](res/eagle/bin_t128_eagle.jpg)|![](res/eagle/bin_t130_eagle.jpg)|
---
### Пример №2 (Баночки)

|**Исходное изображение**|**Полутоновое изображение**|
|------------------------|---------------------------|
|![](original/colours.jpg)|![](res/colours/semitone_colours.jpg)|

|**Gx**|**Gy**|**G**|
|------|------|-----|
|![](res/colours/resx_colours.jpg)|![](res/colours/resy_colours.jpg)|![](res/colours/res_colours.jpg)|

|**T=120**|**T=130**|**T=140**|**T=150**|
|---------|---------|---------|---------|
|![](res/colours/bin_t120_colours.jpg)|![](res/colours/bin_t130_colours.jpg)|![](res/colours/bin_t140_colours.jpg)|![](res/colours/bin_t150_colours.jpg)|
---
### Пример №3 (Текст)

|**Исходное изображение**|**Полутоновое изображение**|
|------------------------|---------------------------|
|![](original/text.jpg)|![](res/text/semitone_text.jpg)|

|**Gx**|**Gy**|**G**|
|------|------|-----|
|![](res/text/resx_text.jpg)|![](res/text/resy_text.jpg)|![](res/text/res_text.jpg)|

|**T=138**|**T=140**|**T=142**|**T=144**|
|---------|---------|---------|---------|
|![](res/text/bin_t138_text.jpg)|![](res/text/bin_t140_text.jpg)|![](res/text/bin_t142_text.jpg)|![](res/text/bin_t144_text.jpg)|
---
### Пример №4 (Горы)

|**Исходное изображение**|**Полутоновое изображение**|
|------------------------|---------------------------|
|![](original/mountain.jpg)|![](res/mountain/semitone_mountain.jpg)|

|**Gx**|**Gy**|**G**|
|------|------|-----|
|![](res/mountain/resx_mountain.jpg)|![](res/mountain/resy_mountain.jpg)|![](res/mountain/res_mountain.jpg)|

|**T=136**|**T=138**|**T=140**|**T=142**|
|---------|---------|---------|---------|
|![](res/mountain/bin_t136_mountain.jpg)|![](res/mountain/bin_t138_mountain.jpg)|![](res/mountain/bin_t140_mountain.jpg)|![](res/mountain/bin_t142_mountain.jpg)|
---
### Пример №6 (Книга)

|**Исходное изображение**|**Полутоновое изображение**|
|------------------------|---------------------------|
|![](original/book12.jpg)|![](res/book12/semitone_book12.jpg)|

|**Gx**|**Gy**|**G**|
|------|------|-----|
|![](res/book12/resx_book12.jpg)|![](res/book12/resy_book12.jpg)|![](res/book12/res_book12.jpg)|

|**T=132**|**T=134**|**T=136**|
|---------|---------|---------|
|![](res/book12/bin_t132_book12.jpg)|![](res/book12/bin_t134_book12.jpg)|![](res/book12/bin_t136_book12.jpg)|
