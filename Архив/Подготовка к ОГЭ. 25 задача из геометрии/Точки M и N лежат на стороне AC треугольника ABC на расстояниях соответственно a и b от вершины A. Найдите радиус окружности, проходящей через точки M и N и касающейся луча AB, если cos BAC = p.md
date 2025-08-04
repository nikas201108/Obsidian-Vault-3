Важные формулы перед решением:
a) Пусть $AB$ — касательная к окружности, а прямая $a$ их той же точки пересекает окружность в точках $E$ и $L$. Тогда: $AB^2 = AE\times AL$
б) Следствия теоремы синусов: $\dfrac{a}{\sin a} = 2R$

Сделаем рисунок:
![[Pasted image 20240420161906.png]]

1) Проведём отрезок к касательной, который образует прямой угол.![[Pasted image 20240420162221.png]]
2) Тогда $AH^2 = AM \times MN$ и значит $$AH = \sqrt{a\times b}$$
3) Рассмотрим $\triangle AHM$ ![[Pasted image 20240420162706.png]]
   По теореме косинусов: $$HM^2 = AH^2+AM^2-2\times AH\times AM \times \cos \angle HAM$$Подставляем наши значения и получаем: $$HM = \sqrt{a\times b + a^2 - 2\times a^2 \times b \times p } = c$$
4) Рассмотрим $\triangle AHN$ и опять попробуем применить теорему косинусов![[Pasted image 20240420163243.png]]
   По теореме косинусов: $$HN^2 = AH^2+AN^2-2\times AH\times AN \times \cos \angle HAM$$Подставляем наши значения и получаем: $$HN = \sqrt{a\times b + b^2 - 2\times a \times b^2 \times p }$$
5) Стороны $HN$ и $AH$ окажутся равны, поэтому $\angle HAN = \angle HNA$ и их косинусы будут равны
6) Из основного тригонометрического тождества говорим: $$\sin{\angle HNA} = \sqrt{1 - p^2}$$
7) По следствию теоремы синусов находим радиус описанной окружности: $$\dfrac{c}{2\sin{\angle HNA}} = R$$

## Пример

>[!info] Входные данные
>$a = 12$
>$b = 21$
>$p = \dfrac{\sqrt{7}}4$ 

Начнём с 2 пункта:
2) $$AH = \sqrt{12\times 21} = 6\sqrt{7}$$
3) $$HM = \sqrt{(6\sqrt{7})^2+12^2-2\times12\times6\sqrt{7}\times\dfrac{\sqrt7}{4}}=12$$
4) $$HN = \sqrt{(6\sqrt{7})^2+21^2-2\times21\times6\sqrt{7}\times\dfrac{\sqrt7}{4}}=6\sqrt7$$
5) Доказываем равенство углов
6) $$\sin{\angle HNA} = \sqrt{1-\dfrac{7}{16}} =\dfrac{3}4$$
7) $$R = \dfrac{HM}{2\sin{\angle HNA}} = \dfrac{12\times4}{6}=8$$

