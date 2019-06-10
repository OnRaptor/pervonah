# Pervonah
![ya malaletniy debil kstati](https://imgur.com/eS3JORO.jpg)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/06e4cdc0fb714bcab752af1b046fda75)](https://www.codacy.com/app/jieggii/pervonah?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=jieggii/pervonah&amp;utm_campaign=Badge_Grade)

Замечали ли вы людей в комментариях различных пабликов, которые пытаются выделиться, написав первыми комментарий с любой информацией, которая никак не относится к посту? <b>Pervonah</b> позволит вам прочувствовать всю их ничтожность на собственной шкуре!

## инсталейшн
1. Клонируем (или <a href="https://github.com/jieggii/pervonah/archive/master.zip">скачиваем</a>) репо: ```git clone https://github.com/jieggii/pervonah``` 
2. Переходим в папку проекта: ```cd pervonah/```
3. Очень важный шаг. Без него бот не заработает: ```echo ya malaletniy debil kstati > IMPORTANT.txt```
4. Устанавливаем зависимости: ```pip install -r requirements.txt``` если у вас Windows, или ```pip3 install -r requirements.txt``` если у вас Linux (если у вас линукс я думаю такой фигней вы не страдаете)
5. Получите access token <a href="https://vkhost.github.io">тут</a> (выберите <b>Kate Mobile</b>)
6. Откройте любым текстовым редактором <b>config.json</b>
7. Заполните переменные:
```access_token``` - токен доступа к вашей странице странице (вы его получили на 5 шаге если что).
```delay``` - задержка (сек) между проверками новых постов (<b>чем <, тем быстрее бот комментит</b>).

```group_ids``` - id групп, посты которых нужно комментировать.
```messages```  - текст комментариев, которые будет постить бот.
```json
{  
  "access_token": "ваш токен доступа",  
  "delay": 1,  
  
  "group_ids": [  
    123,
    456,
    789
  ],  
  
  "messages": [  
    "Текст комментария 1",  
    "Текст комментария 2",  
    "Текст комментария 3"  
  ]  
}
```

## использов ис использова вание
Используйте на свой страх и риск, т.к. нормальные админы пабликов банят за такие шалости 

## License
MIT
