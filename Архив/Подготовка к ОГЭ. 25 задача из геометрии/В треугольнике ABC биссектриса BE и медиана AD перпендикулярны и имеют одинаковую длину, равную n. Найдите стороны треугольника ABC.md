Важные формулы перед решением:
a) $S_{\triangle} = a \times b \times \sin \alpha \times \dfrac{1}2$  
б) $\sin \alpha = \sin(180^\circ-\alpha)$

Сделаем рисунок:
![[Pasted image 20240420153122.png]]

1) По свойству биссектрисы: $$\dfrac{AB}{BC}=\dfrac{AE}{EC}$$
2) Докажем равенство треугольников $\triangle AFB$ и $\triangle BFD$ по углам и равной стороне:
	   1) $\angle AFB$ = $\angle BFD$ ($90^\circ$)
	   2) $\angle ABF = \angle DBF$ (биссектриса)
	   3) $BF$ — общая
3) Возвращаясь к шагу номер 1, говорим, исходя из того что $BC$ разделён медианой: $$\dfrac{AB}{BC} = \dfrac{AE}{EC} = \dfrac12$$
4) Проведём отрезок $ED$:   ![[Pasted image 20240420153145.png]]
5) Возьмем площадь $\triangle AFE$ за $S$. Тогда у треугольника $\triangle FED$ площадь так же равняется $S$ (одинаковые стороны и смежные углы)
   ![[Pasted image 20240420153926.png]]
6) Рассмотрим $\triangle AED$ и $\triangle EDC$. У них будут смежные углы и одна общая сторона, которые не повлияют на площадь. Тем не менее, из 3 пункта сторона $EC = 2\times AE$, а значит: $$S_{\triangle EDC} = 2S_{\triangle AED}=2S \times 2 = 4S$$ ![[Pasted image 20240420154452.png]]
7) Рассмотрим $\triangle BDE$ и $\triangle DEC$. Их площади по формуле площади будут равны(смежный угол, общая сторона и сторона, разделенная медианой). Значит: $$S_{\triangle FBD} = S_{\triangle ABF} = S_{\triangle DEC} - S_{\triangle EFD} = 4S-S = 3S$$![[Pasted image 20240420154835.png]]
8) Найдем на величину отрезков $FE$ и $BF$ $S_{\triangle AFE} = 3S_{\triangle BAF}$
   $AF \times FE \times 0.5 = 3 \times AF \times BF \times 0.5$ 
   $FE =  3 BF$
   $FE + 3FE = n$$$FE = \dfrac{n}4;\text{  }BF = \dfrac{3n}{4}$$
9) Стороны $AB$ и $AE$ можно найти по теореме Пифагора. Дальше через умножение на 2

## Пример при n = 208
Начнём с пункта 8.

8) Вычисляем по формулам:
   $$FE = 52;\text{  }BF = 156$$
9) По теореме Пифагора в $\triangle ABF$: $AB^2 = AF^2 + BF^2$$$AB = 52\sqrt{13}$$
10) $BD = AB \Rightarrow$ $$BC = 2AB = 104\sqrt{13}$$
11) $AE = AF^2 + FE^2 = 52\sqrt{5}$
12) Сумма всех равных частей отрезка $3$, поэтому: $$AC = 3AE = 156\sqrt{5}$$


   