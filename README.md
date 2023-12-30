<img style='width:100px; height:100px;' src='https://github.com/vlopess/MyCollageFm/blob/master/assets/logo.png'></img>
<h1 align="left"><b>MyCollageFm API</b></h1>

Bem-vindo à documentação do LastCollage-API. Esta API permite que você crie collages de imagens de forma eficiente.

![status](https://img.shields.io/badge/status-desenvolvimento-brightgreen.svg?style=flat)
![contributions](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)



## Tecnologias utilizadas
Esse projeto foi desenvolvido utilizando as seguintes tecnologias:

![](https://skillicons.dev/icons?i=flask,py)

## Documentação

### Base URL
> https://victorsites.pythonanywhere.com/api/v1/

### Autenticação ? (Em Breve)

### Endpoint
```
POST /generateCollage
```
### Parâmetros da Solicitação

- id : (string) id da collage
- size : (int) o tamanho da collage [(3x3), (4x4), (5x5)]
- cellList : (array de objetos) Informações sobre as músicas e suas URLs.
    - urlImage : (string) url da imagem
    - name : nome do artista/album/música
```json
"data":
    {
       "id":"",
       "size": 1,
       "cellList":[
          {
             "urlImage":"",
             "name":""
          }
       ]
    }
```
### Resposta
- Retorna o arquivo em bytes pelo body.

### Status Codes

|    Code            |    Status                           |
| ------------------ | :-----------------------------------|
| 200 | OK: A solicitação foi bem-sucedida.                |
| 400 |  Bad Request: Parâmetros inválidos na solicitação. |
| 401 |  Unauthorized: Falha na autenticação.              |
| 404 | Not Found: Recurso não encontrado.                 |
| 500 | Internal Server Error: Erro interno do servidor.   |



### Example Query Request in Dart

``` dart
String address = "https://victorsites.pythonanywhere.com/api/v1/generateCollage";
var url = Uri.parse(address);
var data = dados.toMap(); // Aqui está convertendo o objeto da request para um map
final response = await http.post(url, body: {'data':json.encode(data)});
if (response.statusCode == 200) {
    Directory tempDir = await getTemporaryDirectory();
    String tempPath = tempDir.path;
    filename = '$tempPath/${dados.id}.pdf';
    File file = File(filename);
    await file.writeAsBytes(response.bodyBytes);      
}
```

## Feedback

Se você tiver algum feedback, por favor me deixe saber por meio de victorldev8@gmail.com

## License

This project is under MIT license. See the [LICENSE](LICENSE.MD) file for more details.

---
<h4 align="center">
    Made by <a href="github.com/vlopess" target="_blank">Victor L</a>
</h4>
