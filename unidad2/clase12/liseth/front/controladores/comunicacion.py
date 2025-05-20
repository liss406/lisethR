import requests

class Comunicacion:
    def __init__(self, ventanaPrincipal):
        self.ventanaPrincipal = ventanaPrincipal
        self.url = " http://127.0.0.1:8000/api/Formula1/"
        pass

    def guardar(self, piloto, escuderia, rendimiento, genero):
        try:
            print(piloto, escuderia, rendimiento, genero)
            data = {
                'piloto': piloto,
                'escuderia': escuderia,
                'rendimiento': int(rendimiento),
                'genero': genero,
            }
            resultado = requests.post(self.url, json=data)
            print(resultado.json())
            return resultado
        except ValueError:
            return False
        

    def actualizar(self, id, piloto, escuderia, rendimiento, genero):
        try:
            print(piloto, escuderia, rendimiento, genero)
            rendimiento_num = int(rendimiento) if rendimiento and rendimiento.isdigit() else 0
            data = {
                'piloto': piloto,
                'escuderia': escuderia,
                'rendimiento': rendimiento_num,
                'genero': genero
            }
            resultado = requests.put(self.url + str(id) + '/', json=data)
            print(resultado.json())
            return resultado
        except:
            pass

    def consultar(self, id):
        resultado = requests.get(f"{self.url}{id}")
        return resultado.json()
        
    def consultar_todo(self, piloto, escuderia, rendimiento, genero):
        url = self.url + "?"
        
        if piloto != '':
            url += 'piloto=' + str(piloto) + "&"
        if escuderia != '':
            url += 'escuderia=' + str(escuderia) + "&"
        if rendimiento != '':
            url += 'rendimiento=' + str(rendimiento) + "&"
        if genero != '':
            url += 'genero' + str(genero) + "&"
        
        print(url)
        resultado = requests.get(url)
        return resultado.json()

    def eliminar(self, id):
        resultado = requests.delete(self.url + str(id))
        return resultado.status_code

