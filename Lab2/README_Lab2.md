# Лабораторная работа №2

### Тема: Фильтрация изображений и морфологические операции

|**Студент:**|*Долидзе Александра*|
|------------|--------------|
|**Группа:** |*Б18-514*     |
|**Вариант:**|*3*           |
---
- #### Задание №1: Фильтрация медианным фильтром с ядром в виде равнины (единичные веса), креста прямого, креста косого;

  - Ядро в виде равнины
    ```
    1 1 1
    1 1 1
    1 1 1
    ```

  - Ядро в виде креста

    ```
    0 1 0
    1 1 1
    0 1 0
    ```

  - Ядро в виде косого креста

    ```
    1 0 1
    0 1 0
    1 0 1
    ```

- #### Задание №2: Разностное изображение (попиксельный xor)
---
## Пример №1 (Цвета)
- #### Цветное изображение
 ![Original](./original/colours.jpg)

- #### Исходное черно-белое изображение

    ![Original](./res/colours.jpg_svsp0.5_amount0.05/threshold_B20K0.4_colours.jpg)

- #### Изображение с шумом и перцем

    ![](./res/colours.jpg_svsp0.5_amount0.05/with_salt_0.5_0.05_colours.jpg)

s_vs_p = 0.5
amount = 0.05

- ##### Ядро в виде равнины

    ![](./res/colours.jpg_svsp0.5_amount0.05/median_plane_0.5_0.05_colours.jpg)

- #### Ядро в виде креста

    ![](./res/colours.jpg_svsp0.5_amount0.05/median_cross_0.5_0.05_colours.jpg)

- #### Ядро в виде косого креста
    ![](./res/colours.jpg_svsp0.5_amount0.05/median_x_cross_0.5_0.05_colours.jpg)

|**Равнина**|**Крест**|**Косой крест**|
|--------|------------|--------------|
|![](./res/colours.jpg_svsp0.5_amount0.05/median_plane_0.5_0.05_colours.jpg)|![](./res/colours.jpg_svsp0.5_amount0.05/median_cross_0.5_0.05_colours.jpg) |![](./res/colours.jpg_svsp0.5_amount0.05/median_x_cross_0.5_0.05_colours.jpg)|

|**Разностное равнины и креста**|**Разностное равнины и косого креста**|**Разностное креста и косого креста**|
|--------|--------|------|
|![](./res/colours.jpg_svsp0.5_amount0.05/xor_cross_plane_0.5_0.05_colours.jpg)|![](./res/colours.jpg_svsp0.5_amount0.05/xor_x_cross_plane_0.5_0.05_colours.jpg)|![](./res/colours.jpg_svsp0.5_amount0.05/xor_cross_x_cross_0.5_0.05_colours.jpg)|

---
## Пример №2 (Пицца)
- #### Цветное изображение

![Original](./original/pizza.jpg)

- #### Исходное черно-белое изображение

    ![Original](./res/pizza.jpg_svsp1.0_amount0.5/threshold_B20K0.4_pizza.jpg)

- #### Изображение с шумом и перцем

    ![](./res/pizza.jpg_svsp1.0_amount0.5/with_salt_1.0_0.5_pizza.jpg)

    s_vs_p = 1.0
    amount = 0.5

    - ##### Ядро в виде равнины

        ![](./res/pizza.jpg_svsp1.0_amount0.5/median_plane_1.0_0.5_pizza.jpg)

    - #### Ядро в виде креста

        ![](./res/pizza.jpg_svsp1.0_amount0.5/median_cross_1.0_0.5_pizza.jpg)

    - #### Ядро в виде косого креста
        ![](./res/pizza.jpg_svsp1.0_amount0.5/median_x_cross_1.0_0.5_pizza.jpg)

    |**Равнина**|**Крест**|**Косой крест**|
    |--------|------------|--------------|
    |![](./res/pizza.jpg_svsp1.0_amount0.5/median_plane_1.0_0.5_pizza.jpg)|![](./res/pizza.jpg_svsp1.0_amount0.5/median_cross_1.0_0.5_pizza.jpg)|![](./res/pizza.jpg_svsp1.0_amount0.5/median_x_cross_1.0_0.5_pizza.jpg)|

    |**Разностное равнины и креста**|**Разностное равнины и косого креста**|**Разностное креста и косого креста**|
    |--------|--------|------|
    |![](./res/pizza.jpg_svsp1.0_amount0.5/xor_cross_plane_1.0_0.5_pizza.jpg)|![](./res/pizza.jpg_svsp1.0_amount0.5/xor_x_cross_plane_1.0_0.5_pizza.jpg)|![](./res/pizza.jpg_svsp1.0_amount0.5/xor_cross_x_cross_1.0_0.5_pizza.jpg)|
---
## Пример №3 (Ещё пицца)
- #### Цветное изображение

![Original](./original/pizza2.jpg)

- #### Исходное черно-белое изображение

    ![Original](./res/pizza2.jpg_svsp1.0_amount0.05/threshold_B20K0.4_pizza2.jpg)

- #### Изображение с шумом и перцем

    ![](./res/pizza2.jpg_svsp1.0_amount0.05/with_salt_1.0_0.05_pizza2.jpg)

    s_vs_p = 1.0
    amount = 0.05

    - ##### Ядро в виде равнины

        ![](./res/pizza2.jpg_svsp1.0_amount0.05/median_plane_1.0_0.05_pizza2.jpg)

    - #### Ядро в виде креста

        ![](./res/pizza2.jpg_svsp1.0_amount0.05/median_cross_1.0_0.05_pizza2.jpg)

    - #### Ядро в виде косого креста
        ![](./res/pizza2.jpg_svsp1.0_amount0.05/median_x_cross_1.0_0.05_pizza2.jpg)

    |**Равнина**|**Крест**|**Косой крест**|
    |--------|------------|--------------|
    |![](./res/pizza2.jpg_svsp1.0_amount0.05/median_plane_1.0_0.05_pizza2.jpg)|![](./res/pizza2.jpg_svsp1.0_amount0.05/median_cross_1.0_0.05_pizza2.jpg)|![](./res/pizza2.jpg_svsp1.0_amount0.05/median_x_cross_1.0_0.05_pizza2.jpg)|

    |**Разностное равнины и креста**|**Разностное равнины и косого креста**|**Разностное креста и косого креста**|
    |--------|--------|------|
    |![](./res/pizza2.jpg_svsp1.0_amount0.05/xor_cross_plane_1.0_0.05_pizza2.jpg)|![](./res/pizza2.jpg_svsp1.0_amount0.05/xor_x_cross_plane_1.0_0.05_pizza2.jpg)|![](./res/pizza2.jpg_svsp1.0_amount0.05/xor_cross_x_cross_1.0_0.05_pizza2.jpg)|
---
## Пример №4 (Единорожка)
- #### Цветное изображение
 ![Original](./original/unicorn.png)

- #### Исходное черно-белое изображение

    ![Original](./res/unicorn.png_svsp0.5_amount0.05/threshold_B20K0.4_unicorn.png)

- #### Изображение с шумом и перцем

    ![](./res/unicorn.png_svsp0.5_amount0.05/with_salt_0.5_0.05_unicorn.png)

s_vs_p = 0.5
amount = 0.05

- ##### Ядро в виде равнины

    ![](./res/unicorn.png_svsp0.5_amount0.05/median_plane_0.5_0.05_unicorn.png)

- #### Ядро в виде креста

    ![](./res/unicorn.png_svsp0.5_amount0.05/median_cross_0.5_0.05_unicorn.png)

- #### Ядро в виде косого креста
    ![](./res/unicorn.png_svsp0.5_amount0.05/median_x_cross_0.5_0.05_unicorn.png)

|**Равнина**|**Крест**|**Косой крест**|
|--------|------------|--------------|
|![](./res/unicorn.png_svsp0.5_amount0.05/median_plane_0.5_0.05_unicorn.png)|![](./res/unicorn.png_svsp0.5_amount0.05/median_cross_0.5_0.05_unicorn.png) |![](./res/unicorn.png_svsp0.5_amount0.05/median_x_cross_0.5_0.05_unicorn.png)|

|**Разностное равнины и креста**|**Разностное равнины и косого креста**|**Разностное креста и косого креста**|
|--------|--------|------|
|![](./res/unicorn.png_svsp0.5_amount0.05/xor_cross_plane_0.5_0.05_unicorn.png)|![](./res/unicorn.png_svsp0.5_amount0.05/xor_x_cross_plane_0.5_0.05_unicorn.png)|![](./res/unicorn.png_svsp0.5_amount0.05/xor_cross_x_cross_0.5_0.05_unicorn.png)|
---
## Пример №5.1 (Уже с шумом)
- #### Цветное изображение

![Original](./original/3d.jpg)

- #### Исходное черно-белое изображение

    ![Original](./res/3d.jpg_svsp1.0_amount0.1/threshold_B20K0.4_3d.jpg)

- #### Изображение с шумом и перцем

    ![](./res/3d.jpg_svsp1.0_amount0.1/with_salt_1.0_0.1_3d.jpg)

    s_vs_p = 1.0
    amount = 0.1

    - ##### Ядро в виде равнины

        ![](./res/3d.jpg_svsp1.0_amount0.1/median_plane_1.0_0.1_3d.jpg)

    - #### Ядро в виде креста

        ![](./res/3d.jpg_svsp1.0_amount0.1/median_cross_1.0_0.1_3d.jpg)

    - #### Ядро в виде косого креста
        ![](./res/3d.jpg_svsp1.0_amount0.1/median_x_cross_1.0_0.1_3d.jpg)

    |**Равнина**|**Крест**|**Косой крест**|
    |--------|------------|--------------|
    |![](./res/3d.jpg_svsp1.0_amount0.1/median_plane_1.0_0.1_3d.jpg)|![](./res/3d.jpg_svsp1.0_amount0.1/median_cross_1.0_0.1_3d.jpg)|![](./res/3d.jpg_svsp1.0_amount0.1/median_x_cross_1.0_0.1_3d.jpg)|

    |**Разностное равнины и креста**|**Разностное равнины и косого креста**|**Разностное креста и косого креста**|
    |--------|--------|------|
    |![](./res/3d.jpg_svsp1.0_amount0.1/xor_cross_plane_1.0_0.1_3d.jpg)|![](./res/3d.jpg_svsp1.0_amount0.1/xor_x_cross_plane_1.0_0.1_3d.jpg)|![](./res/3d.jpg_svsp1.0_amount0.1/xor_cross_x_cross_1.0_0.1_3d.jpg)|
---
## Пример №5.2 (Уже с шумом. С другим количеством шума)
- #### Цветное изображение

![Original](./original/3d.jpg)

- #### Исходное черно-белое изображение

    ![Original](./res/3d.jpg_svsp1.0_amount0.03/threshold_B20K0.4_3d.jpg)

- #### Изображение с шумом и перцем

    ![](./res/3d.jpg_svsp1.0_amount0.03/with_salt_1.0_0.03_3d.jpg)

    s_vs_p = 1.0
    amount = 0.03

    - ##### Ядро в виде равнины

        ![](./res/3d.jpg_svsp1.0_amount0.03/median_plane_1.0_0.03_3d.jpg)

    - #### Ядро в виде креста

        ![](./res/3d.jpg_svsp1.0_amount0.03/median_cross_1.0_0.03_3d.jpg)

    - #### Ядро в виде косого креста
        ![](./res/3d.jpg_svsp1.0_amount0.03/median_x_cross_1.0_0.03_3d.jpg)

    |**Равнина**|**Крест**|**Косой крест**|
    |--------|------------|--------------|
    |![](./res/3d.jpg_svsp1.0_amount0.03/median_plane_1.0_0.03_3d.jpg)|![](./res/3d.jpg_svsp1.0_amount0.03/median_cross_1.0_0.03_3d.jpg)|![](./res/3d.jpg_svsp1.0_amount0.03/median_x_cross_1.0_0.03_3d.jpg)|

    |**Разностное равнины и креста**|**Разностное равнины и косого креста**|**Разностное креста и косого креста**|
    |--------|--------|------|
    |![](./res/3d.jpg_svsp1.0_amount0.03/xor_cross_plane_1.0_0.03_3d.jpg)|![](./res/3d.jpg_svsp1.0_amount0.03/xor_x_cross_plane_1.0_0.03_3d.jpg)|![](./res/3d.jpg_svsp1.0_amount0.03/xor_cross_x_cross_1.0_0.03_3d.jpg)|
---
## Пример №6 (Спираль)
- #### Цветное изображение

![Original](./original/spiral.jpg)

- #### Исходное черно-белое изображение

    ![Original](./res/spiral.jpg_svsp0.5_amount0.5/threshold_B20K0.4_spiral.jpg)

- #### Изображение с шумом и перцем

    ![](./res/spiral.jpg_svsp0.5_amount0.5/with_salt_0.5_0.5_spiral.jpg)

    s_vs_p = 0.5
    amount = 0.5

    - ##### Ядро в виде равнины

        ![](./res/spiral.jpg_svsp0.5_amount0.5/median_plane_0.5_0.5_spiral.jpg)

    - #### Ядро в виде креста

        ![](./res/spiral.jpg_svsp0.5_amount0.5/median_cross_0.5_0.5_spiral.jpg)

    - #### Ядро в виде косого креста
        ![](./res/spiral.jpg_svsp0.5_amount0.5/median_x_cross_0.5_0.5_spiral.jpg)

    |**Равнина**|**Крест**|**Косой крест**|
    |--------|------------|--------------|
    |![](./res/spiral.jpg_svsp0.5_amount0.5/median_plane_0.5_0.5_spiral.jpg)|![](./res/spiral.jpg_svsp0.5_amount0.5/median_cross_0.5_0.5_spiral.jpg)|![](./res/spiral.jpg_svsp0.5_amount0.5/median_x_cross_0.5_0.5_spiral.jpg)|

    |**Разностное равнины и креста**|**Разностное равнины и косого креста**|**Разностное креста и косого креста**|
    |--------|--------|------|
    |![](./res/spiral.jpg_svsp0.5_amount0.5/xor_cross_plane_0.5_0.5_spiral.jpg)|![](./res/spiral.jpg_svsp0.5_amount0.5/xor_x_cross_plane_0.5_0.5_spiral.jpg)|![](./res/spiral.jpg_svsp0.5_amount0.5/xor_cross_x_cross_0.5_0.5_spiral.jpg)|
---
## Пример №7 (Спираль)
- #### Цветное изображение

![Original](./original/book11.jpg)

- #### Исходное черно-белое изображение

    ![Original](./res/book11.jpg_svsp1.0_amount0.05/threshold_B20K0.4_book11.jpg)

- #### Изображение с шумом и перцем

    ![](./res/book11.jpg_svsp1.0_amount0.05/with_salt_1.0_0.05_book11.jpg)

    s_vs_p = 1.0
    amount = 0.05

    - ##### Ядро в виде равнины

        ![](./res/book11.jpg_svsp1.0_amount0.05/median_plane_1.0_0.05_book11.jpg)

    - #### Ядро в виде креста

        ![](./res/book11.jpg_svsp1.0_amount0.05/median_cross_1.0_0.05_book11.jpg)

    - #### Ядро в виде косого креста
        ![](./res/book11.jpg_svsp1.0_amount0.05/median_x_cross_1.0_0.05_book11.jpg)

    |**Равнина**|**Крест**|**Косой крест**|
    |--------|------------|--------------|
    |![](./res/book11.jpg_svsp1.0_amount0.05/median_plane_1.0_0.05_book11.jpg)|![](./res/book11.jpg_svsp1.0_amount0.05/median_cross_1.0_0.05_book11.jpg)|![](./res/book11.jpg_svsp1.0_amount0.05/median_x_cross_1.0_0.05_book11.jpg)|

    |**Разностное равнины и креста**|**Разностное равнины и косого креста**|**Разностное креста и косого креста**|
    |--------|--------|------|
    |![](./res/book11.jpg_svsp1.0_amount0.05/xor_cross_plane_1.0_0.05_book11.jpg)|![](./res/book11.jpg_svsp1.0_amount0.05/xor_x_cross_plane_1.0_0.05_book11.jpg)|![](./res/book11.jpg_svsp1.0_amount0.05/xor_cross_x_cross_1.0_0.05_book11.jpg)|
