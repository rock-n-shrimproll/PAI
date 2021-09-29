# Лабораторная работа №1

## Тема: Передискретизация, обесцвечивание и бинаризация растровых изображений

|**Студент:**|*Долидзе Александра*|
|------------|--------------|
|**Группа:** |*Б18-514*     |
|**Вариант:**|*3*           |

### 1. Передискретизация

#### 1.1 Растяжение (интерполяция) изображения в M раз

|**Исходное**|**Размер исходного**| Интерполяция х4 | Размер | Интерполяция x6 | Размер |
|------------|--------------|------------|--------------|------------|--------------|
|![Original](original/spiral.jpg)| 600  x  600 | ![upsampling4](res/upsampling_spiral.jpg) | 2400  x  2400 | ![upsampling6](res/upsampling2_spiral.jpg) | 3600  x  3600 |
|![Original](original/colours.jpg)| 757  x  456 | ![upsampling4](res/upsampling_colours.jpg) | 3028  x  1824 | ![upsampling6](res/upsampling2_colours.jpg) | 4542  x  2736 |

#### 1.2 Сжатие (децимация) изображения в N раз

|**Исходное**|**Размер исходного**| Децимация х3 | Размер | Децимация x7 | Размер |
|------------|--------------|------------|--------------|------------|--------------|
|![Original](original/spiral.jpg)| 600  x  600 | ![downsampling3](res/downsampling2_spiral.jpg) | 200  x  200 | ![downsampling7](res/downsampling_spiral.jpg) | 86  x  86 |
|![Original](original/colours.jpg)| 757  x  456 | ![downsampling3](res/downsampling2_colours.jpg) | 252  x  152 | ![downsampling7](res/downsampling_colours.jpg) | 108  x  65 |


#### 1.3 Передискретизация изображения в K=M/N раз путём растяжения и последующего сжатия (в два прохода)

Передискретизация изображения в K=3/2 раз за два прохода. Исходный размер `720x458` результирующий размер `1080x687`:

![Resampling2loop](res/downsampling3x2_text1.jpg)

---

Передискретизация изображения в K=3/2 раз за два прохода. Исходный размер `720x720` результирующий размер `1080x1080`:

![Resampling2loop](res/downsampling3x2_spiral1.png)

#### 1.4 Передискретизация изображения в K раз за один проход

Передискретизация изображения в K=3/2 раз за один проход. Исходный размер `720x458` результирующий размер `1080x687`:

![Resampling1loop](res/resampling_text1.jpg)

---

Передискретизация изображения в K=3/2 раз за один проход. Исходный размер `720x720` результирующий размер `1080x1080`:

![Resampling1loop](res/resampling_spiral1.png)

### 2. Приведение полноцветного изображения к полутоновому

Исходное изображение:

![Original](../original/test10.png)

Результирующее изображение с обычными коэффицентами:


![SemitoneNormal](res/halftone_test10.png)

Результирующее изображение с коэффицентами photoshop:

![SemitoneNormal](res/halftonePS_test10.png)

---

Исходное изображение:

![Original](../original/test11.jpg)

Результирующее изображение с обычными коэффицентами:

![SemitoneNormal](res/halftone_test11.jpg)

Результирующее изображение с коэффицентами photoshop:

![SemitoneNormal](res/halftonePS_test11.jpg)

### 3. Приведение полутонового изображения к монохромному методом пороговой обработки

Исходное изображение:

![Original](res/downsampling_cat2.jpg)

|**B \ K**		|					0.2								   |					0.6				    			  |					0.8                                  |
|---------------|------------------------------------------------------|------------------------------------------------------|------------------------------------------------------|
|**20** 		|![kristian_threshold](res/threshold_b20_k0.2_cat2.jpg)|![kristian_threshold](res/threshold_b20_k0.6_cat2.jpg)|![kristian_threshold](res/threshold_b20_k0.8_cat2.jpg)|
|**40**			|![kristian_threshold](res/threshold_b40_k0.2_cat2.jpg)|![kristian_threshold](res/threshold_b40_k0.6_cat2.jpg)|![kristian_threshold](res/threshold_b40_k0.8_cat2.jpg)|
|**80**			|![kristian_threshold](res/threshold_b80_k0.2_cat2.jpg)|![kristian_threshold](res/threshold_b80_k0.6_cat2.jpg)|![kristian_threshold](res/threshold_b80_k0.8_cat2.jpg)|


---

Исходное изображение:

![Original](../original/text1.jpg)

Результирующее изображение c `k = 0.2`, `b = 15`:

![kristian_threshold](res/threshold_text1.jpg)


![Original](res/downsampling2_text1.jpg)


|**B \ K**		|					0.2									|					0.6									|					0.8                                 |
|---------------|-------------------------------------------------------|-------------------------------------------------------|-------------------------------------------------------|
|**20** 		|![kristian_threshold](res/threshold_b20_k0.2_downsampling2_text1.jpg)|![kristian_threshold](res/threshold_b20_k0.6_downsampling2_text1.jpg)|![kristian_threshold](res/threshold_b20_k0.6_downsampling2_text1.jpg)|
|**40**			|![kristian_threshold](res/threshold_b40_k0.2_downsampling2_text1.jpg)|![kristian_threshold](res/threshold_b20_k0.6_downsampling2_text1.jpg)|![kristian_threshold](res/threshold_b20_k0.6_downsampling2_text1.jpg)|
|**80**			|![kristian_threshold](res/threshold_b80_k0.2_downsampling2_text1.jpg)|![kristian_threshold](res/threshold_b40_k0.6_downsampling2_text1.jpg)|![kristian_threshold](res/threshold_b40_k0.6_downsampling2_text1.jpg)|
