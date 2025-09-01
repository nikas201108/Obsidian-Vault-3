#Python

>[!task]
>Суть в том, чтобы из URL-адреса составить цепочку-строку вида:
>`<a href="/">HOME</a> + <a href="/very-long-url-to-make-a-silly-yet-meaningful-example/">VLUMSYME</a> + <span class="active">EXAMPLE</span>`
>
>При составлении строки надо учитывать:
> - При длине отдельной части ссылки $>30$ её надо сокращать, убирая a, by, from и так далее
> - Из ссылки надо убирать параметры (?) и # 


 

-----------
## Решения
##### Решение 
Я считаю, что такое решение является вполне хорошим:
```python
import re  
  
def generate_bc(url, separator):  
    url_parts = url.split("/")  
    home = ['<a href="/">HOME</a>']  
    end_without_extension = re.search(r".+(?=\.)", url_parts[-1])[0].replace("-", " ")  
    print(end_without_extension)  
    active = ['<span class="active">{}</span>'.format(end_without_extension.upper())]  
    pattern = r"(?:the-)|(?:of-)|(?:in-)|(?:from-)|(?:by-)|(?:with-)|(?:and-)|(?:or-)|(?:for-)|(?:to-)|(?:at-)|(?:a-)|(?:)"  
    for x in range(1, len(url_parts)):  
        if len(url_parts[x]) > 30:  
            url_parts[x] = (re.sub(r"(?:\#\D+)|(?:\?\D+)", "", url_parts[x]), "".join([y[0].upper() for y in re.sub(pattern, "", url_parts[x]).split("-")]))  
    middle = [r'<a href="/{}/">{}</a>'.format(url_parts[x][0], url_parts[x][1].upper().replace("-", " ")) for x in range(1, len(url_parts) - 1)]  
  
    return "{}".format(separator).join(home + middle + active)  
```

--------
## Комментарий
Здесь мне очень помогли регулярные выражения, которые пришлось вспоминать. Без них было бы очень сложно

***Made by me (based: Codewars [URL](https://www.codewars.com/kata/563fbac924106b8bf7000046/python))***