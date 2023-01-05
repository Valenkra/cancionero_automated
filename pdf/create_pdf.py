import jinja2
import pdfkit

def createPdf(ruta_template,info,rutacss=""):
    nombre_template = ruta_template.split('/')[-1]
    ruta_template = ruta_template.replace(nombre_template, '')

    env = jinja2.Environment(loader=jinja2.FileSystemLoader(ruta_template))
    template = env.get_template(nombre_template)
    #html = template.render(info)

if __name__ == '__main__':
    ruta_template = r'cancionero\pdf\template.html' #C:\Users\Computadora\valencha\
    info = {
        'cancion': 'Dimelo',
        'artista': 'Paulo Londra',
        'lyrics': 'Dimelo, si el cabron no vale la pena'
    }
    createPdf(ruta_template, info, r'C:\Users\Computadora\valencha\cancionero\pdf\styles.css')