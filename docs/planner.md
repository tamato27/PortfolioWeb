## My Personal Portfolio Website
### Vcard Template for qr code generator

### 1) Portfolio Pages to showcase Projects UI
- [ ] Create a Home page with responsive design
  - Created Homepage need to create the UI
  - Color Scheme -> 
  - Fonts Used -> 
  

- [ ] Create an About page with some project descriptions and sample external pages etc.
- [ ] Create a Professional history page with qualifications with a watermark in


### 2) QR code generator for 
- [ ] Create a qr generator page
  - [Flask-QR_code Link](https://pypi.org/project/Flask-QRcode/) 
  - Sample vcard structure for qr code
      ```angular2html
V2.1
  BEGIN:VCARD
  VERSION:2.1
  N:Gump;Forrest;;Mr.
  FN:Forrest Gump
  ORG:Bubba Gump Shrimp Co.
  TITLE:Shrimp Man
  PHOTO;GIF:http://www.example.com/dir_photos/my_photo.gif
  TEL;WORK;VOICE:(111) 555-1212
  TEL;HOME;VOICE:(404) 555-1212
  ADR;WORK;PREF:;;100 Waters Edge;Baytown;LA;30314;United States of America
  LABEL;WORK;PREF;ENCODING#QUOTED-PRINTABLE;CHARSET#UTF-8:100 Waters Edge#0D#
  #0ABaytown\, LA 30314#0D#0AUnited States of America
  ADR;HOME:;;42 Plantation St.;Baytown;LA;30314;United States of America
  LABEL;HOME;ENCODING#QUOTED-PRINTABLE;CHARSET#UTF-8:42 Plantation St.#0D#0A#
  Baytown, LA 30314#0D#0AUnited States of America
  EMAIL:forrestgump@example.com
  REV:20080424T195243Z
  END:VCARD

V3.0
  BEGIN:VCARD
  VERSION:3.0
  N:Gump;Forrest;;Mr.;
  FN:Forrest Gump
  ORG:Bubba Gump Shrimp Co.
  TITLE:Shrimp Man
  PHOTO;VALUE#URI;TYPE#GIF:http://www.example.com/dir_photos/my_photo.gif
  TEL;TYPE#WORK,VOICE:(111) 555-1212
  TEL;TYPE#HOME,VOICE:(404) 555-1212
  ADR;TYPE#WORK,PREF:;;100 Waters Edge;Baytown;LA;30314;United States of America
  LABEL;TYPE#WORK,PREF:100 Waters Edge\nBaytown\, LA 30314\nUnited States of America
  ADR;TYPE#HOME:;;42 Plantation St.;Baytown;LA;30314;United States of America
  LABEL;TYPE#HOME:42 Plantation St.\nBaytown\, LA 30314\nUnited States of America
  EMAIL:forrestgump@example.com
  REV:2008-04-24T19:52:43Z
  END:VCARD

V4.0
  BEGIN:VCARD
  VERSION:4.0
  N:Gump;Forrest;;Mr.;
  FN:Sheri Nom
  ORG:Sheri Nom Co.
  TITLE:Ultimate Warrior
  PHOTO;MEDIATYPE#image/gif:http://www.sherinnom.com/dir_photos/my_photo.gif
  TEL;TYPE#work,voice;VALUE#uri:tel:+1-111-555-1212
  TEL;TYPE#home,voice;VALUE#uri:tel:+1-404-555-1212
  ADR;TYPE#WORK;PREF#1;LABEL#"Normality\nBaytown\, LA 50514\nUnited States of America":;;100 Waters Edge;Baytown;LA;50514;United States of America
  ADR;TYPE#HOME;LABEL#"42 Plantation St.\nBaytown\, LA 30314\nUnited States of America":;;42 Plantation St.;Baytown;LA;30314;United States of America
  EMAIL:sherinnom@example.com
  REV:20080424T195243Z
  x-qq:21588891
  END:VCARD
      ```


### 3) PDF File combiner
- [ ] Create a Pdf page combiner to combine multiple pdf


### 4) Web scraper (searcher)


### 5) Simple automated tasks (samples)


### 6) Countdown timer Widget


Sources Used
https://crop-circle.imageonline.co/

Clouds done by Antonio
https://codepen.io/antonioescudero/pen/zrxGve

https://fonts.google.com/icons?preview.text=MN&preview.text_type=custom&category=Serif,Sans+Serif&query=MON
Bootstrap5
Emojis on Mac Command + Control + Space
www.favicon.cc
https://favicon.io/favicon-generator/
https://www.brandcrowd.com/maker/logo


### API Plans
Need a API Generator - temporarily /api/keygen
  temp Key = "a1623e5ed0402a2b6ee15315fb16e5111097c6a77a52abf59a26beca4db61960"

Json Structure for qrcodes 

{
  "client": { "client_id": "int",
                "api_key": "string",
              }
  "username": "username",
  "surname": "surname",
  "mobile_phone": "",
  "job_title": "",
  "department": "",
  "business_unit": "",
  
}

Use Mysql DB for customers

Db Layouts
Niekor DB

Customer table

| CLIENT_ID   | CLIENT_NAME | API_KEY  | NO-OF_QR_CODES |
| ----------- |:-----------:| ----- :  | -------------- |
|      1      | co name     | api-key  |       1        |







