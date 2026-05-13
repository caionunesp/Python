from flask import Flask

app = Flask(__name__)


@app.route("/")
def ola_mundo():
    return """
    <!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Currículo Profissional - Técnico em TI</title>

  <style>
    *{
      margin:0;
      padding:0;
      box-sizing:border-box;
      font-family: Arial, Helvetica, sans-serif;
    }

    body{
      background-color:#f4f4f4;
      padding:30px;
      color:#333;
    }

    .curriculo{
      max-width:900px;
      margin:auto;
      background:white;
      display:flex;
      box-shadow:0 0 10px rgba(0,0,0,0.2);
      border-radius:10px;
      overflow:hidden;
    }

    .lado-esquerdo{
      width:35%;
      background:#0f172a;
      color:white;
      padding:30px;
    }

    .foto{
      width:140px;
      height:140px;
      border-radius:50%;
      background:#ccc;
      margin:0 auto 20px;
      border:4px solid white;
    }

    .lado-esquerdo h2{
      margin-bottom:10px;
      border-bottom:2px solid #38bdf8;
      padding-bottom:5px;
    }

    .info{
      margin-bottom:25px;
    }

    .info p{
      margin:8px 0;
      font-size:15px;
    }

    .skills li{
      margin:8px 0;
    }

    .lado-direito{
      width:65%;
      padding:35px;
    }

    .nome{
      margin-bottom:10px;
    }

    .nome h1{
      color:#0f172a;
      font-size:36px;
    }

    .nome h3{
      color:#555;
      font-weight:normal;
    }

    .secao{
      margin-top:30px;
    }

    .secao h2{
      color:#0f172a;
      margin-bottom:10px;
      border-bottom:2px solid #38bdf8;
      padding-bottom:5px;
    }

    .secao p,
    .secao li{
      margin:8px 0;
      line-height:1.5;
    }

    ul{
      padding-left:20px;
    }

    .curso{
      margin-bottom:15px;
    }

    .curso h4{
      color:#111827;
    }

    .curso span{
      color:#666;
      font-size:14px;
    }

    @media(max-width:768px){
      .curriculo{
        flex-direction:column;
      }

      .lado-esquerdo,
      .lado-direito{
        width:100%;
      }
    }
  </style>
</head>

<body>

  <div class="curriculo">

    <!-- Lado esquerdo -->
    <div class="lado-esquerdo">

      <div class="foto"></div>

      <div class="info">
        <h2>Contato</h2>
        <p>📞 (31) 97577-9474</p>
        <p>📧 caionupp@gmail.com</p>
        <p>📍 Belo Horizonte - MG</p>
        <p>💻 github.com/caionunesp</p>
      </div>

      <div class="info">
        <h2>Habilidades</h2>
        <ul class="skills">
          <li>HTML e CSS</li>
          <li>JavaScript</li>
          <li>Python</li>
          <li>Banco de Dados</li>
          <li>Pacote Office</li>
          <li>Suporte Técnico</li>
        </ul>
      </div>

      <div class="info">
        <h2>Idiomas</h2>
        <p>Português - Fluente</p>
        <p>Inglês - Básico</p>
      </div>

    </div>

    <!-- Lado direito -->
    <div class="lado-direito">

      <div class="nome">
        <h1>Caio Nunes Pereira</h1>
        <h3>Estudante de Técnico em TI</h3>
      </div>

      <div class="secao">
        <h2>Objetivo</h2>
        <p>
          Busco oportunidade de estágio na área de Tecnologia da Informação
          para desenvolver minhas habilidades técnicas e adquirir experiência
          profissional na área de desenvolvimento e suporte de sistemas.
        </p>
      </div>

      <div class="secao">
        <h2>Formação</h2>

        <div class="curso">
          <h4>Curso Técnico em Informática</h4>
          <span>Colégio Cotemig - 2024 até 2026</span>
        </div>
"""


if __name__ == "__main__":
    app.run(debug=True)
