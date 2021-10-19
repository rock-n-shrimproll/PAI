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

|**Исходное**|**Размер исходного**| Передискретизация х9/2 | Размер |
|------------|--------------|------------|--------------|
|![Original](original/spiral.jpg)| 600  x  600 | ![resampling_double](res/resampling_double_spiral.jpg) | 2700  x  2700 | 
|![Original](original/colours.jpg)| 757  x  456 | ![resampling_double](res/resampling_double_colours.jpg) | 3406  x  2052 | 


#### 1.4 Передискретизация изображения в K раз за один проход

|**Исходное**|**Размер исходного**| Передискретизация х9/2 | Размер |
|------------|--------------|------------|--------------|
|![Original](original/spiral.jpg)| 600  x  600 | ![resampling_single](res/resampling_single_spiral.jpg) | 2700  x  2700 | 
|![Original](original/colours.jpg)| 757  x  456 | ![resampling_single](res/resampling_single_colours.jpg) | 3406  x  2052 | 


### 2. Приведение полноцветного изображения к полутоновому

|**Исходное**|Полутоновое|
|------------|--------------|
|![Original](original/text.jpg)| ![Halftone](res/halftonetext.jpg)| 
|![Original](original/flowers.jpg)| ![Halftone](res/halftoneflowers.jpg) | 

### 3. Приведение полутонового изображения к монохромному методом пороговой обработки

1) Исходное:

![Original](res/text/downsampling_singletext.jpg)

|**B \ K**		|					0.2								   |					0.6				    			  |					0.8                                  |
|---------------|------------------------------------------------------|------------------------------------------------------|------------------------------------------------------|
|**20** 		|![threshold](res/text/threshold_b20_k0.2_text.jpg)|![threshold](res/text/threshold_b20_k0.6_text.jpg)|![threshold](res/text/threshold_b20_k0.8_text.jpg)|
|**40**			|![threshold](res/text/threshold_b40_k0.2_text.jpg)|![threshold](res/text/threshold_b40_k0.6_text.jpg)|![threshold](res/text/threshold_b40_k0.8_text.jpg)|
|**80**			|![threshold](res/text/threshold_b80_k0.2_text.jpg)|![threshold](res/text/threshold_b80_k0.6_text.jpg)|![threshold](res/text/threshold_b80_k0.8_text.jpg)|


---

2) Исходное:

![Original](res/flowers/downsampling_singleflowers.jpg)

|**B \ K**		|					0.2								   |					0.6				    			  |					0.8                                  |
|---------------|------------------------------------------------------|------------------------------------------------------|------------------------------------------------------|
|**20** 		|![threshold](res/flowers/threshold_b20_k0.2_flowers.jpg)|![threshold](res/flowers/threshold_b20_k0.6_flowers.jpg)|![threshold](res/flowers/threshold_b20_k0.8_flowers.jpg)|
|**40**			|![threshold](res/flowers/threshold_b40_k0.2_flowers.jpg)|![threshold](res/flowers/threshold_b40_k0.6_flowers.jpg)|![threshold](res/flowers/threshold_b40_k0.8_flowers.jpg)|
|**80**			|![threshold](res/flowers/threshold_b80_k0.2_flowers.jpg)|![threshold](res/flowers/threshold_b80_k0.6_flowers.jpg)|![threshold](res/flowers/threshold_b80_k0.8_flowers.jpg)|

---

3) Исходное

![Original](res/book12/resamplingbook12.jpg)

|**B \ K**		|					0.2								   |					0.6				    			  |					0.8                                  |
|---------------|------------------------------------------------------|------------------------------------------------------|------------------------------------------------------|
|**20** 		|![threshold](res/book12/threshold_b20_k0.2_book12.jpg)|![threshold](res/book12/threshold_b20_k0.6_book12.jpg)|![threshold](res/book12/threshold_b20_k0.8_book12.jpg)|
|**40**			|![threshold](res/book12/threshold_b40_k0.2_book12.jpg)|![threshold](res/book12/threshold_b40_k0.6_book12.jpg)|![threshold](res/book12/threshold_b40_k0.8_book12.jpg)|
|**80**			|![threshold](res/book12/threshold_b80_k0.2_book12.jpg)|![threshold](res/book12/threshold_b80_k0.6_book12.jpg)|![threshold](res/book12/threshold_b80_k0.8_book12.jpg)|

