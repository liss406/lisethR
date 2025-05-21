import requests

class Comunicacion():

    def __init__(self, ventanaPrincipal):
        self.url = 'http://127.0.0.1:8000/api/cancion/'
        self.ventanaPrincipal = ventanaPrincipal
        pass
        
    def guardar(self, titulo, artista, duracion, genero):
        try:
            print(titulo, artista, duracion, genero)
            data = {
                'titulo': titulo,
                'artista': artista,
                'duracion': int(duracion),
                'genero': genero
            }
            resultado = requests.post(self.url, json=data)
            print(resultado.json())
            return resultado
        except ValueError:
            return False

    def actualizar(self, id, titulo, artista, duracion, genero):
        try:
            print(titulo, artista, duracion, genero)
            data = {
                'titulo': titulo,
                'artista': artista,
                'duracion': duracion,
                'genero': genero
            }
            resultado = requests.put(self.url + str(id)+ '/', json=data)
            print(resultado.json)
            return resultado
        except:
            pass
    
    def consultar(self, id):
        try:
            resultado = requests.get(self.url + str(id))
            if resultado.status_code == 200:
                return resultado.json()
            else:
                return None
        except Exception as e:
            print(f"Error en consulta por ID: {e}")
            return None
 

    def consultar_todo(self, titulo, artista, duracion, genero):
        url = self.url + "?"

        if titulo != '':
            url += 'titulo=' + str(titulo) + "&"
        if artista != '':
            url += 'artista=' + str(artista) + "&"
        if duracion != '':
            url += 'duracion=' + str(duracion) + "&"
        if genero !='':
            url += 'genero=' + str(genero) + "&"
            
            print(url)
        resultado = requests.get(url)
        return resultado.json()


    def eliminar(self, id):
        resultado = requests.delete(self.url + '/' + str(id))
        return resultado.status_code
