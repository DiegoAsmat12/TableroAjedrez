from flask import Flask, render_template

app = Flask(__name__)

@app.route("/", methods=["GET"])
def AjedrezBase():
    return render_template('index.html',column=8, row=8,colorPar="black", colorImpar="red")

@app.route("/<int:row>", methods=["GET"])
def AjedrezConFila(row:int):
    return render_template('index.html',column=8, row=row,colorPar="black", colorImpar="red")

@app.route("/<int:row>/<int:column>", methods=["GET"])
def AjedrezConFilaColumna(row:int,column:int):
    return render_template('index.html',column=column, row=row,colorPar="black", colorImpar="red")

@app.route("/<int:row>/<int:column>/<colorPar>", methods=["GET"])
def AjedrezConFilaColumnaPar(row:int,column:int,colorPar:str):
    return render_template('index.html',column=column, row=row,colorPar=colorPar, colorImpar="red")

@app.route("/<int:row>/<int:column>/<colorPar>/<colorImpar>", methods=["GET"])
def AjedrezConFilaColumnaParImpar(row:int,column:int,colorPar:str,colorImpar:str):
    return render_template('index.html',column=column, row=row,colorPar=colorPar, colorImpar=colorImpar)

if(__name__=="__main__"):
    app.run(debug=True)