from http import HTTPStatus
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from fast_zero.schemas import Message

app = FastAPI()


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Olá Mundo!'}


@app.get('/exercicio-html', status_code=HTTPStatus.OK, response_class=HTMLResponse)
def exercicio_aula_02():
    html_content = """
        <html>
            <head>
                <title>Olá Mundo em HTML</title>
            </head>
            <body>
                <h1>Olá Mundo</h1>
                <p>Em HTML pelo próprio fastAPI.</p> 
            </body>
        </html>
    """

    return html_content
