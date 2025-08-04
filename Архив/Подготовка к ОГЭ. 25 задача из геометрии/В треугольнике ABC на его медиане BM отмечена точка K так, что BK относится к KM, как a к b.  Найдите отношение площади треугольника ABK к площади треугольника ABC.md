Полезные формулы:
	a) $S_{\triangle ABC} = 0.5\times AB \times AC \times \sin\alpha$
	б) $\sin (180-\alpha) = \sin\alpha$ 

Сделаем рисунок:
![[Pasted image 20240502204143.png]]

1) Рассмотрим $\triangle AKM$ и $\triangle AKB$:$$\dfrac{S_{\triangle AKM}}{S_{\triangle AKB}} = \dfrac{0.5\times MK\times AK
\times \sin \alpha}{0.5\times BK \times AK\times \sin (180-\alpha)}=\dfrac{b}{a}$$
2) Из первого следует, что $S_{\triangle ABK} = \dfrac{S_{\triangle AKM}\times a}b$ 
3) $S_{\triangle ABM} = S_{\triangle BMC} = 0.5\times S_{\triangle ABC}$, так как медиана
4) Выразим $S_{\triangle ABM}$ через сумму двух составляющих треугольников: $$S_{\triangle ABM}=\dfrac{S_{\triangle AKM}\times a}b + S_{\triangle AKM} =\dfrac{S_{\triangle AKM}\times(a+b)}{b}$$
5) $S_{\triangle ABC}$ третьего и четвертого пунктов: $$S_{\triangle ABC} = \dfrac{2S_{\triangle AKM}\times(a+b)}{b}$$
6) Составляем отношение: $$\dfrac{S_{\triangle ABK}}{S_{\triangle ABC}}=\dfrac{S_{\triangle AKM}\times a}b:\dfrac{2S_{\triangle AKM}\times(a+b)}{b}$$$$\dfrac{S_{\triangle ABK}}{S_{\triangle ABC}}=\dfrac12:\left(1+\dfrac{b}{a}\right)$$

## Пример

>[!info] Входные данные
>$a = 3$
>$b = 7$ 

6) $$\dfrac{S_{\triangle ABK}}{S_{\triangle ABC}}=\dfrac12:\left(1+\dfrac{7}{3}\right)=0.15$$